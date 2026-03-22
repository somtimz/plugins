"""Public pipeline API — T003/T004

Provides run_ingestion() and the SourceResult/IngestionEvent types used by
both the CLI (scripts/ingest.py) and the web UI (scripts/ui.py).
"""
from __future__ import annotations

import hashlib
import datetime
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional


# ---------------------------------------------------------------------------
# Types
# ---------------------------------------------------------------------------

@dataclass
class SourceResult:
    label: str
    discovered: int = 0
    succeeded: int = 0
    skipped: int = 0
    failed: int = 0
    skipped_unchanged: int = 0
    skipped_duplicate: int = 0
    failed_docs: list[tuple[str, str]] = field(default_factory=list)
    status: str = "ok"   # "ok" | "auth_failed" | "unreachable" | "permission_denied"
    error_message: Optional[str] = None


@dataclass
class IngestionEvent:
    file_path: str
    source_name: str
    event_type: str   # "succeeded" | "skipped_unchanged" | "skipped_duplicate" | "skipped_size" | "skipped_empty" | "failed"
    status: Optional[str] = None   # "succeeded" | "skipped" | "failed"
    reason: Optional[str] = None


ProgressCallback = Callable[[IngestionEvent], None]


# Module-level imports from sibling libs (no circular dependency risk).
# Placed here so tests can patch them at lib.pipeline.<name>.
from lib.reader import read_document, UnreadableError, EmptyDocumentError, FileSizeLimitError
from lib.chunker import chunk_text
from lib.embedder import embed_chunks, EmbeddingError
from lib.sources import discover_local
from lib.store import upsert_chunks, delete_by_document
from lib.registry import (
    lookup,
    insert as registry_insert,
    update as registry_update,
    DocumentRecord,
    create_schema,
    RunDedupSet,
    open_registry,
)
from lib.config import LocalSourceConfig


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _md5(path: str) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            h.update(block)
    return h.hexdigest()


def _emit(callback: Optional[ProgressCallback], event: IngestionEvent) -> None:
    """Call the progress callback, swallowing any exception it raises."""
    if callback is None:
        return
    try:
        callback(event)
    except Exception:
        pass


# ---------------------------------------------------------------------------
# Core per-source file processing
# ---------------------------------------------------------------------------

def process_source(
    candidates: list[str],
    source_name: str,
    collection,
    cfg,
    logger,
    result: SourceResult,
    reg_conn,
    dedup,
    progress_callback: Optional[ProgressCallback] = None,
) -> None:
    """Process a list of file paths with incremental deduplication.

    Emits an IngestionEvent via progress_callback for each document outcome.
    Callback exceptions are swallowed so they never break transaction atomicity.
    """
    result.discovered = len(candidates)

    for file_path in candidates:
        try:
            content_hash = _md5(file_path)

            # Within-run deduplication
            if dedup.seen(content_hash):
                result.skipped += 1
                result.skipped_duplicate += 1
                logger.info("Skipped (duplicate hash in run): %s", file_path)
                _emit(progress_callback, IngestionEvent(
                    file_path=file_path,
                    source_name=source_name,
                    event_type="skipped_duplicate",
                    status="skipped",
                    reason="duplicate in this run",
                ))
                continue

            # Registry lookup
            existing = lookup(reg_conn, source_name, file_path)

            if existing is not None and existing.content_hash == content_hash:
                result.skipped += 1
                result.skipped_unchanged += 1
                dedup.mark(content_hash)
                logger.info("Skipped (unchanged): %s", file_path)
                _emit(progress_callback, IngestionEvent(
                    file_path=file_path,
                    source_name=source_name,
                    event_type="skipped_unchanged",
                    status="skipped",
                    reason="unchanged",
                ))
                continue

            logger.info("Reading %s", file_path)
            text = read_document(file_path, cfg.pipeline.max_file_size_mb)

            logger.info("Chunking %s (%d chars)", file_path, len(text))
            chunks = chunk_text(
                text, cfg.pipeline.chunk_size, cfg.pipeline.chunk_overlap, file_path
            )

            logger.info("Embedding %d chunks from %s", len(chunks), file_path)
            embedded = embed_chunks(chunks, cfg.embedding, logger)

            if existing is not None:
                logger.info("Deleting old vectors for modified doc: %s", file_path)
                delete_by_document(collection, source_name, file_path)

            logger.info(
                "Upserting %d vectors for %s (hash=%s)", len(embedded), file_path, content_hash
            )
            try:
                upsert_chunks(collection, embedded, source_name, file_path, content_hash)
            except Exception as store_exc:
                reg_conn.rollback()
                raise store_exc

            if existing is not None:
                registry_update(reg_conn, source_name, file_path, content_hash, len(embedded))
            else:
                registry_insert(
                    reg_conn,
                    DocumentRecord(
                        source_name=source_name,
                        origin_path=file_path,
                        content_hash=content_hash,
                        chunk_count=len(embedded),
                    ),
                )
            reg_conn.commit()

            dedup.mark(content_hash)
            result.succeeded += 1
            logger.info("Ingested: %s", file_path)
            _emit(progress_callback, IngestionEvent(
                file_path=file_path,
                source_name=source_name,
                event_type="succeeded",
                status="succeeded",
                reason=None,
            ))

        except FileSizeLimitError as exc:
            result.skipped += 1
            logger.warning("Skipped (file too large): %s — %s", file_path, exc)
            _emit(progress_callback, IngestionEvent(
                file_path=file_path,
                source_name=source_name,
                event_type="skipped_size",
                status="skipped",
                reason=str(exc),
            ))
        except EmptyDocumentError as exc:
            result.skipped += 1
            logger.warning("Skipped (empty document): %s — %s", file_path, exc)
            _emit(progress_callback, IngestionEvent(
                file_path=file_path,
                source_name=source_name,
                event_type="skipped_empty",
                status="skipped",
                reason=str(exc),
            ))
        except UnreadableError as exc:
            result.failed += 1
            reason = str(exc)
            result.failed_docs.append((file_path, reason))
            logger.error("Failed (unreadable): %s — %s", file_path, reason)
            _emit(progress_callback, IngestionEvent(
                file_path=file_path,
                source_name=source_name,
                event_type="failed",
                status="failed",
                reason=reason,
            ))
        except EmbeddingError as exc:
            result.failed += 1
            reason = str(exc)
            result.failed_docs.append((file_path, reason))
            logger.error("Failed (embedding): %s — %s", file_path, reason)
            _emit(progress_callback, IngestionEvent(
                file_path=file_path,
                source_name=source_name,
                event_type="failed",
                status="failed",
                reason=reason,
            ))
        except Exception as exc:
            result.failed += 1
            reason = str(exc)
            result.failed_docs.append((file_path, reason))
            logger.error("Failed (unexpected): %s — %s", file_path, reason)
            _emit(progress_callback, IngestionEvent(
                file_path=file_path,
                source_name=source_name,
                event_type="failed",
                status="failed",
                reason=reason,
            ))


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def run_ingestion(
    sources,
    cfg,
    logger,
    chroma_client,
    collection,
    reg_conn,
    progress_callback: Optional[ProgressCallback] = None,
) -> list[SourceResult]:
    """Run ingestion for a list of source configs, returning per-source results.

    Callers are responsible for initialising chroma_client, collection, and
    reg_conn before calling this function (and closing reg_conn afterwards).
    This keeps resource lifecycle in the caller so both the CLI and the web UI
    can manage their own connection lifetimes appropriately.
    """
    create_schema(reg_conn)
    dedup = RunDedupSet()
    results: list[SourceResult] = []

    for src_cfg in sources:
        if isinstance(src_cfg, LocalSourceConfig):
            source_label = f"{src_cfg.name} (local: {src_cfg.path})"
            result = SourceResult(label=source_label)
            results.append(result)
            logger.info("Processing local source: %s → %s", src_cfg.name, src_cfg.path)

            p = Path(src_cfg.path)
            if not p.exists():
                result.status = "unreachable"
                result.error_message = f"Source path does not exist: {src_cfg.path}"
                logger.error("Source path not found: %s", src_cfg.path)
                continue

            candidates = [
                sf.origin_path
                for sf in discover_local(src_cfg.path, cfg.pipeline.supported_formats)
            ]
            process_source(
                candidates, src_cfg.name, collection, cfg, logger,
                result, reg_conn, dedup, progress_callback
            )
        else:
            source_label = f"{src_cfg.name} (sharepoint: {src_cfg.folder})"
            result = SourceResult(
                label=source_label,
                status="unreachable",
                error_message=(
                    "SharePoint source support not yet enabled. "
                    "Set type=local or wait for SharePoint implementation."
                ),
            )
            results.append(result)
            logger.warning("SharePoint source skipped (not implemented): %s", src_cfg.name)

    return results
