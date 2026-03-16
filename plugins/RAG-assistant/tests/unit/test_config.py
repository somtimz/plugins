"""Tests for scripts/lib/config.py — T004"""
import os
import textwrap
import pytest
from pathlib import Path

# Adjust import path so tests can find scripts/lib
import sys
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.config import load_config, ConfigError, LlmConfig


VALID_TOML = textwrap.dedent("""\
    [embedding]
    provider = "openai-compatible"
    model = "text-embedding-3-small"
    api_base = "https://api.openai.com/v1"
    api_key_env = "TEST_API_KEY"

    [vector_store]
    provider = "chroma"
    path = ".rag-store"
    collection = "documents"

    [pipeline]
    chunk_size = 1000
    chunk_overlap = 200
    supported_formats = ["txt", "md", "pdf", "docx"]

    [[sources]]
    name = "local-docs"
    type = "local"
    path = "./docs"
""")


@pytest.fixture(autouse=True)
def set_api_key(monkeypatch):
    monkeypatch.setenv("TEST_API_KEY", "sk-test")


def write_toml(tmp_path, content):
    p = tmp_path / ".rag-plugin.toml"
    p.write_text(content)
    return str(p)


class TestValidConfig:
    def test_loads_embedding(self, tmp_path):
        cfg = load_config(write_toml(tmp_path, VALID_TOML))
        assert cfg.embedding.provider == "openai-compatible"
        assert cfg.embedding.model == "text-embedding-3-small"
        assert cfg.embedding.api_base == "https://api.openai.com/v1"
        assert cfg.embedding.api_key_env == "TEST_API_KEY"

    def test_loads_vector_store(self, tmp_path):
        cfg = load_config(write_toml(tmp_path, VALID_TOML))
        assert cfg.vector_store.provider == "chroma"
        assert cfg.vector_store.path == ".rag-store"
        assert cfg.vector_store.collection == "documents"

    def test_loads_pipeline(self, tmp_path):
        cfg = load_config(write_toml(tmp_path, VALID_TOML))
        assert cfg.pipeline.chunk_size == 1000
        assert cfg.pipeline.chunk_overlap == 200

    def test_loads_local_source(self, tmp_path):
        cfg = load_config(write_toml(tmp_path, VALID_TOML))
        assert len(cfg.sources) == 1
        assert cfg.sources[0].name == "local-docs"
        assert cfg.sources[0].type == "local"
        assert cfg.sources[0].path == "./docs"


class TestDefaults:
    def test_registry_path_default(self, tmp_path):
        cfg = load_config(write_toml(tmp_path, VALID_TOML))
        assert cfg.pipeline.registry_path == ".rag-registry.db"

    def test_log_path_default(self, tmp_path):
        cfg = load_config(write_toml(tmp_path, VALID_TOML))
        assert cfg.pipeline.log_path == ".rag-pipeline.log"

    def test_max_file_size_mb_default(self, tmp_path):
        cfg = load_config(write_toml(tmp_path, VALID_TOML))
        assert cfg.pipeline.max_file_size_mb == 100

    def test_defaults_overridden(self, tmp_path):
        toml = VALID_TOML + textwrap.dedent("""\
            registry_path = ".my-registry.db"
            log_path = ".my-log.log"
            max_file_size_mb = 50
        """).replace("\n", "\n", 1)
        # Insert under [pipeline]
        toml = VALID_TOML.replace(
            "chunk_overlap = 200",
            "chunk_overlap = 200\nregistry_path = \".my-registry.db\"\nlog_path = \".my-log.log\"\nmax_file_size_mb = 50"
        )
        cfg = load_config(write_toml(tmp_path, toml))
        assert cfg.pipeline.registry_path == ".my-registry.db"
        assert cfg.pipeline.log_path == ".my-log.log"
        assert cfg.pipeline.max_file_size_mb == 50


class TestValidationErrors:
    def test_missing_embedding_section(self, tmp_path):
        toml = "[vector_store]\nprovider=\"chroma\"\npath=\".rag-store\"\ncollection=\"docs\"\n"
        with pytest.raises(ConfigError, match="embedding"):
            load_config(write_toml(tmp_path, toml))

    def test_unsupported_embedding_provider(self, tmp_path):
        toml = VALID_TOML.replace('provider = "openai-compatible"', 'provider = "huggingface"', 1)
        with pytest.raises(ConfigError, match="Unsupported embedding provider"):
            load_config(write_toml(tmp_path, toml))

    def test_unsupported_vector_store_provider(self, tmp_path):
        toml = VALID_TOML.replace('provider = "chroma"', 'provider = "pinecone"')
        with pytest.raises(ConfigError, match="Unsupported vector_store provider"):
            load_config(write_toml(tmp_path, toml))

    def test_chunk_overlap_gte_chunk_size(self, tmp_path):
        toml = VALID_TOML.replace("chunk_overlap = 200", "chunk_overlap = 1000")
        with pytest.raises(ConfigError, match="chunk_overlap must be less than chunk_size"):
            load_config(write_toml(tmp_path, toml))

    def test_max_file_size_mb_zero(self, tmp_path):
        toml = VALID_TOML.replace(
            "chunk_overlap = 200",
            "chunk_overlap = 200\nmax_file_size_mb = 0"
        )
        with pytest.raises(ConfigError, match="max_file_size_mb must be a positive integer"):
            load_config(write_toml(tmp_path, toml))

    def test_max_file_size_mb_negative(self, tmp_path):
        toml = VALID_TOML.replace(
            "chunk_overlap = 200",
            "chunk_overlap = 200\nmax_file_size_mb = -5"
        )
        with pytest.raises(ConfigError, match="max_file_size_mb must be a positive integer"):
            load_config(write_toml(tmp_path, toml))

    def test_duplicate_source_names(self, tmp_path):
        toml = VALID_TOML + textwrap.dedent("""\
            [[sources]]
            name = "local-docs"
            type = "local"
            path = "./other"
        """)
        with pytest.raises(ConfigError, match="Duplicate source name"):
            load_config(write_toml(tmp_path, toml))

    def test_unsupported_source_type(self, tmp_path):
        toml = VALID_TOML.replace('type = "local"', 'type = "s3"')
        with pytest.raises(ConfigError, match="Unsupported source type"):
            load_config(write_toml(tmp_path, toml))

    def test_local_source_missing_path(self, tmp_path):
        toml = VALID_TOML.replace('path = "./docs"', "")
        with pytest.raises(ConfigError, match="path is required for local sources"):
            load_config(write_toml(tmp_path, toml))

    def test_api_key_env_not_set(self, tmp_path, monkeypatch):
        monkeypatch.delenv("TEST_API_KEY", raising=False)
        with pytest.raises(ConfigError, match="TEST_API_KEY"):
            load_config(write_toml(tmp_path, VALID_TOML))

    def test_invalid_api_base_url(self, tmp_path):
        toml = VALID_TOML.replace(
            'api_base = "https://api.openai.com/v1"',
            'api_base = "not-a-url"'
        )
        with pytest.raises(ConfigError, match="api_base must be a valid URL"):
            load_config(write_toml(tmp_path, toml))

    def test_empty_collection_name(self, tmp_path):
        toml = VALID_TOML.replace('collection = "documents"', 'collection = ""')
        with pytest.raises(ConfigError, match="vector_store.collection is required"):
            load_config(write_toml(tmp_path, toml))


class TestSharePointSource:
    def test_valid_sharepoint_device_flow(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SP_TENANT", "tenant-id")
        monkeypatch.setenv("SP_CLIENT", "client-id")
        toml = VALID_TOML + textwrap.dedent("""\
            [[sources]]
            name = "sp-docs"
            type = "sharepoint"
            site_url = "https://myco.sharepoint.com/sites/s"
            folder = "/Shared Documents"
            auth_type = "device_flow"
            tenant_id_env = "SP_TENANT"
            client_id_env = "SP_CLIENT"
        """)
        cfg = load_config(write_toml(tmp_path, toml))
        sp = cfg.sources[1]
        assert sp.name == "sp-docs"
        assert sp.auth_type == "device_flow"

    def test_sharepoint_missing_required_field(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SP_TENANT", "t")
        monkeypatch.setenv("SP_CLIENT", "c")
        toml = VALID_TOML + textwrap.dedent("""\
            [[sources]]
            name = "sp-docs"
            type = "sharepoint"
            site_url = "https://myco.sharepoint.com/sites/s"
            auth_type = "device_flow"
            tenant_id_env = "SP_TENANT"
            client_id_env = "SP_CLIENT"
        """)
        with pytest.raises(ConfigError, match="folder is required for sharepoint sources"):
            load_config(write_toml(tmp_path, toml))

    def test_client_credentials_missing_secret(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SP_TENANT", "t")
        monkeypatch.setenv("SP_CLIENT", "c")
        toml = VALID_TOML + textwrap.dedent("""\
            [[sources]]
            name = "sp-docs"
            type = "sharepoint"
            site_url = "https://myco.sharepoint.com/sites/s"
            folder = "/Shared Documents"
            auth_type = "client_credentials"
            tenant_id_env = "SP_TENANT"
            client_id_env = "SP_CLIENT"
        """)
        with pytest.raises(ConfigError, match="client_secret_env required for client_credentials"):
            load_config(write_toml(tmp_path, toml))

    def test_max_depth_negative_raises(self, tmp_path, monkeypatch):
        monkeypatch.setenv("SP_TENANT", "t")
        monkeypatch.setenv("SP_CLIENT", "c")
        toml = VALID_TOML + textwrap.dedent("""\
            [[sources]]
            name = "sp-docs"
            type = "sharepoint"
            site_url = "https://myco.sharepoint.com/sites/s"
            folder = "/Shared Documents"
            auth_type = "device_flow"
            tenant_id_env = "SP_TENANT"
            client_id_env = "SP_CLIENT"
            max_depth = -1
        """)
        with pytest.raises(ConfigError, match="max_depth must be a non-negative integer"):
            load_config(write_toml(tmp_path, toml))


# ---------------------------------------------------------------------------
# T002 — LlmConfig tests
# ---------------------------------------------------------------------------

class TestLlmConfig:
    """Tests for LlmConfig dataclass and optional [llm] section parsing."""

    def test_defaults_when_llm_section_absent(self, tmp_path, monkeypatch):
        """LlmConfig uses defaults when [llm] section is absent from TOML."""
        monkeypatch.setenv("TEST_API_KEY", "key")
        cfg = load_config(write_toml(tmp_path, VALID_TOML))
        assert cfg.llm.model == "claude-sonnet-4-6"
        assert cfg.llm.api_key_env == "ANTHROPIC_API_KEY"

    def test_custom_model_and_api_key_env(self, tmp_path, monkeypatch):
        """LlmConfig reads model and api_key_env from [llm] section when present."""
        monkeypatch.setenv("TEST_API_KEY", "key")
        toml = VALID_TOML + textwrap.dedent("""\
            [llm]
            model = "claude-opus-4-6"
            api_key_env = "MY_CLAUDE_KEY"
        """)
        cfg = load_config(write_toml(tmp_path, toml))
        assert cfg.llm.model == "claude-opus-4-6"
        assert cfg.llm.api_key_env == "MY_CLAUDE_KEY"

    def test_empty_model_raises(self, tmp_path, monkeypatch):
        """Empty model string in [llm] section raises ConfigError."""
        monkeypatch.setenv("TEST_API_KEY", "key")
        toml = VALID_TOML + textwrap.dedent("""\
            [llm]
            model = ""
        """)
        with pytest.raises(ConfigError, match="llm.model"):
            load_config(write_toml(tmp_path, toml))

    def test_empty_api_key_env_raises(self, tmp_path, monkeypatch):
        """Empty api_key_env string in [llm] section raises ConfigError."""
        monkeypatch.setenv("TEST_API_KEY", "key")
        toml = VALID_TOML + textwrap.dedent("""\
            [llm]
            api_key_env = ""
        """)
        with pytest.raises(ConfigError, match="llm.api_key_env"):
            load_config(write_toml(tmp_path, toml))

    def test_llm_config_dataclass_defaults(self):
        """LlmConfig dataclass has correct field defaults."""
        llm = LlmConfig()
        assert llm.model == "claude-sonnet-4-6"
        assert llm.api_key_env == "ANTHROPIC_API_KEY"

    def test_partial_llm_section_uses_defaults_for_missing_fields(self, tmp_path, monkeypatch):
        """When [llm] has only model set, api_key_env defaults to ANTHROPIC_API_KEY."""
        monkeypatch.setenv("TEST_API_KEY", "key")
        toml = VALID_TOML + textwrap.dedent("""\
            [llm]
            model = "claude-haiku-4-5-20251001"
        """)
        cfg = load_config(write_toml(tmp_path, toml))
        assert cfg.llm.model == "claude-haiku-4-5-20251001"
        assert cfg.llm.api_key_env == "ANTHROPIC_API_KEY"
