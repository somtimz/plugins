"""Config loading and validation for the RAG ingestion pipeline — T006"""
from __future__ import annotations

import os
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Union
from urllib.parse import urlparse


class ConfigError(ValueError):
    """Raised when the configuration file is invalid or missing required values."""


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class EmbeddingConfig:
    provider: str
    model: str
    api_base: str
    api_key_env: str


@dataclass
class VectorStoreConfig:
    provider: str
    path: str
    collection: str


@dataclass
class PipelineConfig:
    chunk_size: int = 1000
    chunk_overlap: int = 200
    supported_formats: list[str] = field(default_factory=lambda: ["txt", "md", "pdf", "docx"])
    registry_path: str = ".rag-registry.db"
    log_path: str = ".rag-pipeline.log"
    max_file_size_mb: int = 100
    top_k: int = 5


@dataclass
class LlmConfig:
    model: str = "claude-sonnet-4-6"
    api_key_env: str = "ANTHROPIC_API_KEY"


@dataclass
class LocalSourceConfig:
    name: str
    type: str
    path: str


@dataclass
class SharePointSourceConfig:
    name: str
    type: str
    site_url: str
    folder: str
    auth_type: str
    tenant_id_env: str
    client_id_env: str
    client_secret_env: str | None = None
    max_depth: int = 0  # 0 = unlimited


SourceConfig = Union[LocalSourceConfig, SharePointSourceConfig]


@dataclass
class Config:
    embedding: EmbeddingConfig
    vector_store: VectorStoreConfig
    pipeline: PipelineConfig
    sources: list[SourceConfig]
    llm: LlmConfig = field(default_factory=LlmConfig)


# ---------------------------------------------------------------------------
# Validators
# ---------------------------------------------------------------------------

def _require(section: dict, key: str, section_name: str) -> object:
    val = section.get(key)
    if val is None or (isinstance(val, str) and not val.strip()):
        raise ConfigError(f"{section_name}.{key} is required")
    return val


def _validate_url(value: str, field_name: str) -> None:
    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        raise ConfigError(f"{field_name} must be a valid URL (got: {value!r})")


def _parse_embedding(raw: dict) -> EmbeddingConfig:
    if "embedding" not in raw:
        raise ConfigError("Missing required section: [embedding]")
    e = raw["embedding"]
    provider = str(_require(e, "provider", "embedding"))
    if provider != "openai-compatible":
        raise ConfigError(f"Unsupported embedding provider: {provider!r}")
    model = str(_require(e, "model", "embedding"))
    api_base = str(_require(e, "api_base", "embedding"))
    _validate_url(api_base, "embedding.api_base")
    api_key_env = str(_require(e, "api_key_env", "embedding"))
    if not os.environ.get(api_key_env):
        raise ConfigError(
            f"Environment variable {api_key_env!r} is not set. "
            f"Export it before running the pipeline."
        )
    return EmbeddingConfig(provider=provider, model=model, api_base=api_base, api_key_env=api_key_env)


def _parse_vector_store(raw: dict) -> VectorStoreConfig:
    if "vector_store" not in raw:
        raise ConfigError("Missing required section: [vector_store]")
    v = raw["vector_store"]
    provider = str(_require(v, "provider", "vector_store"))
    if provider != "chroma":
        raise ConfigError(f"Unsupported vector_store provider: {provider!r}")
    path = str(_require(v, "path", "vector_store"))
    collection = str(v.get("collection", ""))
    if not collection:
        raise ConfigError("vector_store.collection is required")
    return VectorStoreConfig(provider=provider, path=path, collection=collection)


def _parse_pipeline(raw: dict) -> PipelineConfig:
    p = raw.get("pipeline", {})
    cfg = PipelineConfig(
        chunk_size=int(p.get("chunk_size", 1000)),
        chunk_overlap=int(p.get("chunk_overlap", 200)),
        supported_formats=list(p.get("supported_formats", ["txt", "md", "pdf", "docx"])),
        registry_path=str(p.get("registry_path", ".rag-registry.db")),
        log_path=str(p.get("log_path", ".rag-pipeline.log")),
        max_file_size_mb=int(p.get("max_file_size_mb", 100)),
    )
    if cfg.chunk_overlap >= cfg.chunk_size:
        raise ConfigError(
            f"chunk_overlap must be less than chunk_size "
            f"(got chunk_size={cfg.chunk_size}, chunk_overlap={cfg.chunk_overlap})"
        )
    if cfg.max_file_size_mb <= 0:
        raise ConfigError(
            f"max_file_size_mb must be a positive integer (got {cfg.max_file_size_mb})"
        )
    return cfg


def _parse_local_source(s: dict) -> LocalSourceConfig:
    name = str(_require(s, "name", "source"))
    path = s.get("path")
    if not path:
        raise ConfigError(f"sources[{name!r}].path is required for local sources")
    return LocalSourceConfig(name=name, type="local", path=str(path))


def _parse_sharepoint_source(s: dict) -> SharePointSourceConfig:
    name = str(_require(s, "name", "source"))
    for field_name in ("site_url", "folder", "auth_type", "tenant_id_env", "client_id_env"):
        if not s.get(field_name):
            raise ConfigError(f"sources[{name!r}].{field_name} is required for sharepoint sources")
    auth_type = str(s["auth_type"])
    if auth_type not in ("device_flow", "client_credentials"):
        raise ConfigError(
            f"sources[{name!r}].auth_type must be 'device_flow' or 'client_credentials' "
            f"(got {auth_type!r})"
        )
    client_secret_env = s.get("client_secret_env")
    if auth_type == "client_credentials" and not client_secret_env:
        raise ConfigError(
            f"sources[{name!r}].client_secret_env required for client_credentials auth"
        )
    max_depth = int(s.get("max_depth", 0))
    if max_depth < 0:
        raise ConfigError(
            f"sources[{name!r}].max_depth must be a non-negative integer (got {max_depth})"
        )
    return SharePointSourceConfig(
        name=name,
        type="sharepoint",
        site_url=str(s["site_url"]),
        folder=str(s["folder"]),
        auth_type=auth_type,
        tenant_id_env=str(s["tenant_id_env"]),
        client_id_env=str(s["client_id_env"]),
        client_secret_env=str(client_secret_env) if client_secret_env else None,
        max_depth=max_depth,
    )


def _parse_llm(raw: dict) -> LlmConfig:
    if "llm" not in raw:
        return LlmConfig()
    l = raw["llm"]
    model = str(l.get("model", "claude-sonnet-4-6"))
    if not model.strip():
        raise ConfigError("llm.model must be a non-empty string")
    api_key_env = str(l.get("api_key_env", "ANTHROPIC_API_KEY"))
    if not api_key_env.strip():
        raise ConfigError("llm.api_key_env must be a non-empty string")
    return LlmConfig(model=model, api_key_env=api_key_env)


def _parse_sources(raw: dict) -> list[SourceConfig]:
    raw_sources = raw.get("sources", [])
    sources: list[SourceConfig] = []
    seen_names: set[str] = set()
    for s in raw_sources:
        name = s.get("name", "")
        if name in seen_names:
            raise ConfigError(f"Duplicate source name: {name!r}")
        seen_names.add(name)
        src_type = s.get("type", "")
        if src_type == "local":
            sources.append(_parse_local_source(s))
        elif src_type == "sharepoint":
            sources.append(_parse_sharepoint_source(s))
        else:
            raise ConfigError(f"Unsupported source type: {src_type!r}")
    return sources


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def load_config(path: str) -> Config:
    """Load and validate the TOML configuration file at *path*.

    Raises ConfigError with a descriptive message on any validation failure.
    """
    config_path = Path(path)
    if not config_path.exists():
        raise ConfigError(
            f"Configuration file not found: {path}\n"
            "Run the skill to create it, or pass --config to specify a different path."
        )

    try:
        raw = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"Invalid TOML in {path}: {exc}") from exc

    embedding = _parse_embedding(raw)
    vector_store = _parse_vector_store(raw)
    pipeline = _parse_pipeline(raw)
    sources = _parse_sources(raw)
    llm = _parse_llm(raw)

    return Config(
        embedding=embedding,
        vector_store=vector_store,
        pipeline=pipeline,
        sources=sources,
        llm=llm,
    )
