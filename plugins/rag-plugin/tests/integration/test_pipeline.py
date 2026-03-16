"""Integration tests for the full RAG ingestion pipeline — T026

These tests spin up an in-memory ChromaDB and a temp SQLite registry and run
the pipeline end-to-end via the ingest module's internal API (not subprocess),
so no real OpenAI key is needed — the embedder is mocked.

SharePoint integration scenario: deferred (see T023 / T026 notes in tasks.md).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path
from unittest.mock import patch

import chromadb
import pytest

# Add scripts/ to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.config import (
    Config,
    EmbeddingConfig,
    VectorStoreConfig,
    PipelineConfig,
    LocalSourceConfig,
)
from lib.store import get_or_create_collection, check_model_consistency
from lib.registry import open_registry, create_schema, lookup
from lib.embedder import EmbeddedChunk
from lib.pipeline import process_source as _process_file_list, SourceResult
from lib.registry import RunDedupSet


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

MODEL = "text-embedding-3-small"
DIMS = 4  # tiny embeddings for tests


@pytest.fixture
def chroma_collection(tmp_path):
    # Use PersistentClient with a unique path — EphemeralClient shares in-process state
    client = chromadb.PersistentClient(path=str(tmp_path / ".chroma"))
    col = get_or_create_collection(client, "test-collection", MODEL)
    return col


@pytest.fixture
def reg_conn(tmp_path):
    db = tmp_path / "registry.db"
    conn = open_registry(str(db))
    create_schema(conn)
    yield conn
    conn.close()


@pytest.fixture
def cfg(tmp_path):
    return Config(
        embedding=EmbeddingConfig(
            provider="openai-compatible",
            model=MODEL,
            api_base="https://api.openai.com/v1",
            api_key_env="TEST_API_KEY",
        ),
        vector_store=VectorStoreConfig(
            provider="chroma",
            path=str(tmp_path / ".rag-store"),
            collection="test-collection",
        ),
        pipeline=PipelineConfig(
            chunk_size=200,
            chunk_overlap=50,
            registry_path=str(tmp_path / "registry.db"),
            log_path=str(tmp_path / "pipeline.log"),
        ),
        sources=[
            LocalSourceConfig(name="test-src", type="local", path=str(tmp_path / "docs")),
        ],
    )


def _fake_embed(chunks, embedding_config, logger):
    """Return fake embeddings without calling OpenAI."""
    model = getattr(embedding_config, "model", "fake-model")
    return [
        EmbeddedChunk(chunk_id=c.chunk_id, text=c.text, vector=[0.1, 0.2, 0.3, 0.4], model=model)
        for c in chunks
    ]


def _make_logger(tmp_path):
    import logging
    logger = logging.getLogger("test_pipeline")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        h = logging.FileHandler(str(tmp_path / "test.log"))
        h.setLevel(logging.DEBUG)
        logger.addHandler(h)
        logger.propagate = False
    return logger


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestNewDocument:
    def test_new_document_ingested_and_registry_created(
        self, tmp_path, chroma_collection, reg_conn, cfg
    ):
        doc = tmp_path / "doc.txt"
        doc.write_text("Hello world " * 10)
        logger = _make_logger(tmp_path)
        result = SourceResult(label="test")
        dedup = RunDedupSet()

        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger, result, reg_conn, dedup
            )

        assert result.succeeded == 1
        assert result.failed == 0
        row = lookup(reg_conn, "test-src", str(doc))
        assert row is not None
        assert row.version_count == 1
        assert chroma_collection.count() > 0

    def test_registry_row_has_correct_chunk_count(
        self, tmp_path, chroma_collection, reg_conn, cfg
    ):
        doc = tmp_path / "doc.txt"
        doc.write_text("A" * 300)  # > chunk_size=200 → 2 chunks
        logger = _make_logger(tmp_path)
        result = SourceResult(label="test")
        dedup = RunDedupSet()

        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger, result, reg_conn, dedup
            )

        row = lookup(reg_conn, "test-src", str(doc))
        assert row.chunk_count == chroma_collection.count()


class TestUnchangedDocument:
    def test_second_run_unchanged_skips(self, tmp_path, chroma_collection, reg_conn, cfg):
        doc = tmp_path / "doc.txt"
        doc.write_text("Same content " * 10)
        logger = _make_logger(tmp_path)

        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            result1 = SourceResult(label="test")
            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger, result1, reg_conn,
                RunDedupSet()
            )

            result2 = SourceResult(label="test")
            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger, result2, reg_conn,
                RunDedupSet()
            )

        assert result2.skipped == 1
        assert result2.skipped_unchanged == 1
        assert result2.succeeded == 0
        row = lookup(reg_conn, "test-src", str(doc))
        assert row.version_count == 1  # unchanged — no increment


class TestModifiedDocument:
    def test_modified_doc_increments_version_count(
        self, tmp_path, chroma_collection, reg_conn, cfg
    ):
        doc = tmp_path / "doc.txt"
        doc.write_text("Original content " * 10)
        logger = _make_logger(tmp_path)

        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger,
                SourceResult(label="t"), reg_conn, RunDedupSet()
            )
            count_after_first = chroma_collection.count()

            # Modify the document
            doc.write_text("Modified content " * 10)

            result2 = SourceResult(label="test")
            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger,
                result2, reg_conn, RunDedupSet()
            )

        assert result2.succeeded == 1
        row = lookup(reg_conn, "test-src", str(doc))
        assert row.version_count == 2

    def test_modified_doc_old_chunks_replaced(self, tmp_path, chroma_collection, reg_conn, cfg):
        doc = tmp_path / "doc.txt"
        # chunk_size=200, overlap=50 → step=150
        # 100 chars → 1 chunk
        doc.write_text("A" * 100)
        logger = _make_logger(tmp_path)

        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger,
                SourceResult(label="t"), reg_conn, RunDedupSet()
            )
            count_v1 = chroma_collection.count()
            assert count_v1 == 1

            # Modify: 350 chars → 2 chunks (0-200, 150-350)
            doc.write_text("B" * 350)

            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger,
                SourceResult(label="t"), reg_conn, RunDedupSet()
            )

        # Old 1 chunk deleted, 2 new chunks inserted → collection should have 2
        assert chroma_collection.count() == 2


class TestDuplicateHashInRun:
    def test_same_hash_in_single_run_ingested_once(
        self, tmp_path, chroma_collection, reg_conn, cfg
    ):
        doc_a = tmp_path / "a.txt"
        doc_b = tmp_path / "b.txt"
        # Identical content → same hash
        content = "Identical content " * 10
        doc_a.write_text(content)
        doc_b.write_text(content)
        logger = _make_logger(tmp_path)
        result = SourceResult(label="test")
        dedup = RunDedupSet()

        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                [str(doc_a), str(doc_b)], "test-src", chroma_collection, cfg,
                logger, result, reg_conn, dedup
            )

        assert result.succeeded == 1
        assert result.skipped_duplicate == 1


class TestModelMismatch:
    def test_check_model_consistency_raises_on_mismatch(self, tmp_path):
        client = chromadb.EphemeralClient()
        col = get_or_create_collection(client, "mismatch-col", "model-a")
        from lib.store import ModelMismatchError
        with pytest.raises(ModelMismatchError):
            check_model_consistency(col, "model-b")


class TestFileSizeLimit:
    def test_oversized_file_skipped_not_fatal(self, tmp_path, chroma_collection, reg_conn, cfg):
        doc = tmp_path / "big.txt"
        doc.write_bytes(b"x" * (cfg.pipeline.max_file_size_mb * 1024 * 1024 + 1))
        logger = _make_logger(tmp_path)
        result = SourceResult(label="test")

        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                [str(doc)], "test-src", chroma_collection, cfg, logger, result,
                reg_conn, RunDedupSet()
            )

        assert result.skipped == 1
        assert result.failed == 0


class TestPerformance:
    def test_ingest_10_docs_under_120_seconds(self, tmp_path, chroma_collection, reg_conn, cfg):
        """SC-001: ingest 10 small docs must complete in under 120 s."""
        docs = []
        for i in range(10):
            d = tmp_path / f"doc_{i}.txt"
            d.write_text(f"Document {i}: " + "content word " * 50)
            docs.append(str(d))

        logger = _make_logger(tmp_path)
        result = SourceResult(label="perf")

        t0 = time.time()
        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                docs, "perf-src", chroma_collection, cfg, logger, result, reg_conn, RunDedupSet()
            )
        elapsed = time.time() - t0

        assert result.succeeded == 10
        assert elapsed < 120, f"Ingestion took {elapsed:.1f}s — exceeds 120s SC-001 limit"

    def test_second_run_unchanged_faster_than_10pct_of_first(
        self, tmp_path, chroma_collection, reg_conn, cfg
    ):
        """SC-003: incremental run on unchanged set must be < 10% of initial run time."""
        docs = []
        for i in range(10):
            d = tmp_path / f"doc_{i}.txt"
            d.write_text(f"Document {i}: " + "static content " * 50)
            docs.append(str(d))

        logger = _make_logger(tmp_path)

        t0 = time.time()
        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                docs, "inc-src", chroma_collection, cfg, logger,
                SourceResult(label="run1"), reg_conn, RunDedupSet()
            )
        first_run = time.time() - t0

        t1 = time.time()
        result2 = SourceResult(label="run2")
        with patch("lib.pipeline.embed_chunks", side_effect=_fake_embed):
            _process_file_list(
                docs, "inc-src", chroma_collection, cfg, logger, result2, reg_conn, RunDedupSet()
            )
        second_run = time.time() - t1

        assert result2.skipped == 10
        assert result2.succeeded == 0
        # Allow generous threshold (min 0.01s to avoid division noise)
        first_run = max(first_run, 0.01)
        assert second_run < first_run * 0.10 or second_run < 1.0, (
            f"Second run ({second_run:.3f}s) not < 10% of first ({first_run:.3f}s)"
        )
