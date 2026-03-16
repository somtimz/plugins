"""Unit tests for scripts/lib/pipeline.py — T006

Tests written BEFORE implementing run_ingestion (constitution III compliance).
"""
from __future__ import annotations

import sys
import sqlite3
from pathlib import Path
from unittest.mock import MagicMock, patch, call
from dataclasses import dataclass, field

import pytest

# Ensure scripts/ is on sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.pipeline import (
    SourceResult,
    IngestionEvent,
    run_ingestion,
    process_source,
    _emit,
)
from lib.config import LocalSourceConfig, PipelineConfig, EmbeddingConfig, VectorStoreConfig


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def _make_cfg(tmp_path):
    """Minimal config for testing."""
    cfg = MagicMock()
    cfg.pipeline.chunk_size = 200
    cfg.pipeline.chunk_overlap = 20
    cfg.pipeline.supported_formats = ["txt", "md"]
    cfg.pipeline.max_file_size_mb = 10
    cfg.pipeline.registry_path = str(tmp_path / "registry.db")
    cfg.embedding.model = "test-model"
    cfg.embedding.api_base = "http://localhost"
    cfg.embedding.api_key_env = "TEST_KEY"
    return cfg


def _make_reg_conn(tmp_path):
    from lib.registry import open_registry, create_schema
    conn = open_registry(str(tmp_path / "registry.db"))
    create_schema(conn)
    return conn


@dataclass
class FakeEmbeddedChunk:
    text: str
    vector: list[float]
    model: str
    source: str = ""
    chunk_index: int = 0


# ---------------------------------------------------------------------------
# _emit tests
# ---------------------------------------------------------------------------

class TestEmit:
    def test_calls_callback(self):
        events = []
        ev = IngestionEvent(file_path="a.txt", source_name="src", event_type="succeeded", status="succeeded")
        _emit(events.append, ev)
        assert events == [ev]

    def test_none_callback_is_noop(self):
        ev = IngestionEvent(file_path="a.txt", source_name="src", event_type="succeeded", status="succeeded")
        _emit(None, ev)  # should not raise

    def test_swallows_callback_exception(self):
        def bad_callback(ev):
            raise RuntimeError("boom")

        ev = IngestionEvent(file_path="a.txt", source_name="src", event_type="succeeded", status="succeeded")
        _emit(bad_callback, ev)  # should not raise


# ---------------------------------------------------------------------------
# process_source tests
# ---------------------------------------------------------------------------

class TestProcessSource:
    def test_callback_called_once_per_document(self, tmp_path):
        # Create two text files
        f1 = tmp_path / "a.txt"
        f2 = tmp_path / "b.txt"
        f1.write_text("hello world " * 5)
        f2.write_text("goodbye world " * 5)

        cfg = _make_cfg(tmp_path)
        reg_conn = _make_reg_conn(tmp_path)
        logger = MagicMock()
        result = SourceResult(label="test")

        from lib.registry import RunDedupSet
        dedup = RunDedupSet()

        events: list[IngestionEvent] = []

        mock_collection = MagicMock()

        with patch("lib.pipeline.embed_chunks") as mock_embed, \
             patch("lib.pipeline.upsert_chunks"):
            mock_embed.return_value = [
                FakeEmbeddedChunk(text="chunk", vector=[0.1] * 3, model="test-model")
            ]
            process_source(
                [str(f1), str(f2)],
                "test-source",
                mock_collection,
                cfg,
                logger,
                result,
                reg_conn,
                dedup,
                progress_callback=events.append,
            )

        assert len(events) == 2
        assert all(ev.source_name == "test-source" for ev in events)
        assert all(ev.file_path in (str(f1), str(f2)) for ev in events)

    def test_callback_exception_does_not_abort_run(self, tmp_path):
        f1 = tmp_path / "a.txt"
        f2 = tmp_path / "b.txt"
        f1.write_text("hello " * 5)
        f2.write_text("world " * 5)

        cfg = _make_cfg(tmp_path)
        reg_conn = _make_reg_conn(tmp_path)
        logger = MagicMock()
        result = SourceResult(label="test")

        from lib.registry import RunDedupSet
        dedup = RunDedupSet()

        call_count = [0]

        def bad_callback(ev):
            call_count[0] += 1
            raise RuntimeError("callback exploded")

        mock_collection = MagicMock()

        with patch("lib.pipeline.embed_chunks") as mock_embed, \
             patch("lib.pipeline.upsert_chunks"):
            mock_embed.return_value = [
                FakeEmbeddedChunk(text="chunk", vector=[0.1] * 3, model="test-model")
            ]
            process_source(
                [str(f1), str(f2)],
                "test-source",
                mock_collection,
                cfg,
                logger,
                result,
                reg_conn,
                dedup,
                progress_callback=bad_callback,
            )

        # Both files should still be processed despite callback exploding
        assert result.succeeded == 2
        assert call_count[0] == 2

    def test_skipped_unchanged_emits_correct_event(self, tmp_path):
        f1 = tmp_path / "a.txt"
        f1.write_text("hello " * 5)

        cfg = _make_cfg(tmp_path)
        reg_conn = _make_reg_conn(tmp_path)
        logger = MagicMock()
        result = SourceResult(label="test")

        from lib.registry import RunDedupSet, open_registry, create_schema, insert, DocumentRecord
        import hashlib

        # Pre-insert with the same hash so it skips
        content = f1.read_bytes()
        h = hashlib.md5(content).hexdigest()
        import datetime
        conn2 = open_registry(str(tmp_path / "registry.db"))
        create_schema(conn2)
        insert(conn2, DocumentRecord(
            source_name="test-source",
            origin_path=str(f1),
            content_hash=h,
            chunk_count=1,
        ))
        conn2.commit()
        conn2.close()

        dedup = RunDedupSet()
        events: list[IngestionEvent] = []
        result2 = SourceResult(label="test")

        process_source(
            [str(f1)],
            "test-source",
            MagicMock(),
            cfg,
            MagicMock(),
            result2,
            reg_conn,
            dedup,
            progress_callback=events.append,
        )

        assert len(events) == 1
        assert events[0].event_type == "skipped_unchanged"
        assert events[0].status == "skipped"

    def test_result_counts_match_callback_events(self, tmp_path):
        f1 = tmp_path / "a.txt"
        f2 = tmp_path / "b.txt"
        f1.write_text("success content " * 5)
        f2.write_text("")  # empty — will be skipped

        cfg = _make_cfg(tmp_path)
        reg_conn = _make_reg_conn(tmp_path)
        logger = MagicMock()
        result = SourceResult(label="test")

        from lib.registry import RunDedupSet
        dedup = RunDedupSet()

        events: list[IngestionEvent] = []
        mock_collection = MagicMock()

        with patch("lib.pipeline.embed_chunks") as mock_embed, \
             patch("lib.pipeline.upsert_chunks"):
            mock_embed.return_value = [
                FakeEmbeddedChunk(text="chunk", vector=[0.1] * 3, model="test-model")
            ]
            process_source(
                [str(f1), str(f2)],
                "test-source",
                mock_collection,
                cfg,
                logger,
                result,
                reg_conn,
                dedup,
                progress_callback=events.append,
            )

        succeeded_events = [e for e in events if e.status == "succeeded"]
        skipped_events = [e for e in events if e.status == "skipped"]
        failed_events = [e for e in events if e.status == "failed"]

        assert len(succeeded_events) == result.succeeded
        assert len(skipped_events) == result.skipped
        assert len(failed_events) == result.failed


# ---------------------------------------------------------------------------
# run_ingestion tests
# ---------------------------------------------------------------------------

class TestRunIngestion:
    def test_returns_list_of_source_results(self, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        (docs_dir / "a.txt").write_text("hello world " * 10)

        cfg = _make_cfg(tmp_path)
        cfg.pipeline.registry_path = str(tmp_path / "registry.db")
        logger = MagicMock()

        from lib.config import LocalSourceConfig
        sources = [LocalSourceConfig(name="test", type="local", path=str(docs_dir))]

        import chromadb
        chroma_client = chromadb.PersistentClient(path=str(tmp_path / ".chroma"))
        from lib.store import get_or_create_collection
        collection = get_or_create_collection(chroma_client, "docs", "test-model")
        import sqlite3
        reg_conn = sqlite3.connect(str(tmp_path / "registry.db"))

        with patch("lib.pipeline.embed_chunks") as mock_embed, \
             patch("lib.pipeline.upsert_chunks"):
            mock_embed.return_value = [
                FakeEmbeddedChunk(text="c", vector=[0.1, 0.2, 0.3], model="test-model")
            ]
            results = run_ingestion(sources, cfg, logger, chroma_client, collection, reg_conn)

        reg_conn.close()
        assert len(results) == 1
        assert isinstance(results[0], SourceResult)
        assert results[0].discovered == 1

    def test_unreachable_source_returns_error_result(self, tmp_path):
        cfg = _make_cfg(tmp_path)
        logger = MagicMock()

        from lib.config import LocalSourceConfig
        sources = [LocalSourceConfig(name="ghost", type="local", path="/nonexistent/path")]

        import chromadb, sqlite3
        chroma_client = chromadb.PersistentClient(path=str(tmp_path / ".chroma"))
        from lib.store import get_or_create_collection
        collection = get_or_create_collection(chroma_client, "docs", "test-model")
        reg_conn = sqlite3.connect(str(tmp_path / "registry.db"))

        results = run_ingestion(sources, cfg, logger, chroma_client, collection, reg_conn)
        reg_conn.close()

        assert results[0].status == "unreachable"

    def test_progress_callback_receives_events(self, tmp_path):
        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        (docs_dir / "a.txt").write_text("content " * 20)

        cfg = _make_cfg(tmp_path)
        logger = MagicMock()

        from lib.config import LocalSourceConfig
        sources = [LocalSourceConfig(name="src", type="local", path=str(docs_dir))]

        import chromadb, sqlite3
        chroma_client = chromadb.PersistentClient(path=str(tmp_path / ".chroma"))
        from lib.store import get_or_create_collection
        collection = get_or_create_collection(chroma_client, "docs", "test-model")
        reg_conn = sqlite3.connect(str(tmp_path / "registry.db"))

        events: list[IngestionEvent] = []

        with patch("lib.pipeline.embed_chunks") as mock_embed, \
             patch("lib.pipeline.upsert_chunks"):
            mock_embed.return_value = [
                FakeEmbeddedChunk(text="c", vector=[0.1, 0.2, 0.3], model="test-model")
            ]
            run_ingestion(sources, cfg, logger, chroma_client, collection, reg_conn,
                          progress_callback=events.append)

        reg_conn.close()
        assert len(events) >= 1
        assert events[0].source_name == "src"
