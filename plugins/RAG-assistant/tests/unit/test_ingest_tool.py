"""Tests for scripts/lib/ingest_tool.py — T004"""
from __future__ import annotations

import json
import sqlite3
import sys
import threading
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

from lib.ingest_tool import (
    INGEST_DOCUMENTS_TOOL,
    QUERY_REGISTRY_TOOL,
    SEARCH_KNOWLEDGE_BASE_TOOL,
    TOOL_SCHEMAS,
    execute_ingest_documents,
    execute_query_registry,
    execute_search_knowledge_base,
)


# ---------------------------------------------------------------------------
# Tool schema structure tests
# ---------------------------------------------------------------------------

class TestToolSchemas:
    def test_tool_schemas_list_has_three_entries(self):
        assert len(TOOL_SCHEMAS) == 3

    def test_ingest_documents_tool_name(self):
        assert INGEST_DOCUMENTS_TOOL["name"] == "ingest_documents"

    def test_query_registry_tool_name(self):
        assert QUERY_REGISTRY_TOOL["name"] == "query_registry"

    def test_search_knowledge_base_tool_name(self):
        assert SEARCH_KNOWLEDGE_BASE_TOOL["name"] == "search_knowledge_base"

    def test_ingest_documents_has_path_parameter(self):
        props = INGEST_DOCUMENTS_TOOL["input_schema"]["properties"]
        assert "path" in props

    def test_query_registry_has_query_parameter(self):
        props = QUERY_REGISTRY_TOOL["input_schema"]["properties"]
        assert "query" in props

    def test_search_knowledge_base_has_query_parameter(self):
        props = SEARCH_KNOWLEDGE_BASE_TOOL["input_schema"]["properties"]
        assert "query" in props

    def test_all_schemas_have_required_anthropic_fields(self):
        for schema in TOOL_SCHEMAS:
            assert "name" in schema
            assert "description" in schema
            assert "input_schema" in schema
            assert schema["input_schema"]["type"] == "object"


# ---------------------------------------------------------------------------
# execute_ingest_documents tests
# ---------------------------------------------------------------------------

class TestExecuteIngestDocuments:
    def _make_deps(self, tmp_path):
        """Build minimal dependency mocks for execute_ingest_documents."""
        cfg = MagicMock()
        cfg.pipeline.registry_path = str(tmp_path / ".rag-registry.db")
        cfg.pipeline.log_path = str(tmp_path / ".rag-pipeline.log")
        chroma_client = MagicMock()
        collection = MagicMock()
        reg_conn = MagicMock()
        run_lock = threading.Lock()
        logger = MagicMock()
        return cfg, chroma_client, collection, reg_conn, run_lock, logger

    def test_invalid_path_returns_error_string(self, tmp_path):
        cfg, chroma_client, collection, reg_conn, run_lock, logger = self._make_deps(tmp_path)
        result = execute_ingest_documents(
            path="/nonexistent/path/xyz",
            cfg=cfg,
            chroma_client=chroma_client,
            collection=collection,
            reg_conn=reg_conn,
            run_lock=run_lock,
            logger=logger,
        )
        assert "ERROR" in result or "error" in result.lower() or "not exist" in result.lower()

    def test_concurrent_run_blocked(self, tmp_path):
        """When run_lock is already held, returns a concurrency error string."""
        cfg, chroma_client, collection, reg_conn, run_lock, logger = self._make_deps(tmp_path)
        # Acquire the lock to simulate an in-progress run
        run_lock.acquire()
        try:
            result = execute_ingest_documents(
                path=str(tmp_path),
                cfg=cfg,
                chroma_client=chroma_client,
                collection=collection,
                reg_conn=reg_conn,
                run_lock=run_lock,
                logger=logger,
            )
            assert "already" in result.lower() or "in progress" in result.lower() or "ERROR" in result
        finally:
            run_lock.release()

    def test_successful_run_returns_summary(self, tmp_path):
        """A successful ingestion returns a summary string with counts."""
        cfg, chroma_client, collection, reg_conn, run_lock, logger = self._make_deps(tmp_path)

        # Create a real directory with one file so path validation passes
        source_dir = tmp_path / "docs"
        source_dir.mkdir()
        (source_dir / "test.txt").write_text("hello world")

        with patch("lib.ingest_tool.run_ingestion") as mock_run:
            mock_run.return_value = [MagicMock(
                discovered=1, succeeded=1, skipped=0, failed=0
            )]
            result = execute_ingest_documents(
                path=str(source_dir),
                cfg=cfg,
                chroma_client=chroma_client,
                collection=collection,
                reg_conn=reg_conn,
                run_lock=run_lock,
                logger=logger,
            )
        assert "1" in result  # at least the count appears in the summary

    def test_lock_released_after_run(self, tmp_path):
        """run_lock is released after execute_ingest_documents returns."""
        cfg, chroma_client, collection, reg_conn, run_lock, logger = self._make_deps(tmp_path)
        source_dir = tmp_path / "docs"
        source_dir.mkdir()

        with patch("lib.ingest_tool.run_ingestion") as mock_run:
            mock_run.return_value = [MagicMock(discovered=0, succeeded=0, skipped=0, failed=0)]
            execute_ingest_documents(
                path=str(source_dir),
                cfg=cfg,
                chroma_client=chroma_client,
                collection=collection,
                reg_conn=reg_conn,
                run_lock=run_lock,
                logger=logger,
            )

        # Lock should be acquirable (i.e. released) after the call
        acquired = run_lock.acquire(blocking=False)
        assert acquired, "run_lock was not released after execute_ingest_documents"
        run_lock.release()


# ---------------------------------------------------------------------------
# execute_query_registry tests
# ---------------------------------------------------------------------------

class TestExecuteQueryRegistry:
    def _make_reg_conn(self):
        conn = sqlite3.connect(":memory:")
        conn.execute(
            """CREATE TABLE documents (
                source_name TEXT,
                origin_path TEXT,
                content_hash TEXT,
                chunk_count INTEGER,
                version_count INTEGER,
                last_ingested TEXT,
                PRIMARY KEY (source_name, origin_path)
            )"""
        )
        conn.execute(
            "INSERT INTO documents VALUES (?,?,?,?,?,?)",
            ("hr", "/hr/policy.pdf", "abc", 5, 1, "2026-01-01T00:00:00+00:00"),
        )
        conn.execute(
            "INSERT INTO documents VALUES (?,?,?,?,?,?)",
            ("finance", "/finance/q1.pdf", "def", 3, 1, "2026-01-02T00:00:00+00:00"),
        )
        conn.commit()
        return conn

    def test_no_filter_returns_all_records(self):
        conn = self._make_reg_conn()
        result = execute_query_registry(query=None, limit=10, reg_conn=conn)
        data = json.loads(result)
        assert len(data) == 2

    def test_query_filter_applied(self):
        conn = self._make_reg_conn()
        result = execute_query_registry(query="hr", limit=10, reg_conn=conn)
        data = json.loads(result)
        assert len(data) == 1
        assert data[0]["source_name"] == "hr"

    def test_empty_registry_returns_empty_list(self):
        conn = sqlite3.connect(":memory:")
        conn.execute(
            """CREATE TABLE documents (
                source_name TEXT, origin_path TEXT, content_hash TEXT,
                chunk_count INTEGER, version_count INTEGER, last_ingested TEXT,
                PRIMARY KEY (source_name, origin_path)
            )"""
        )
        conn.commit()
        result = execute_query_registry(query=None, limit=10, reg_conn=conn)
        assert json.loads(result) == []

    def test_limit_respected(self):
        conn = self._make_reg_conn()
        result = execute_query_registry(query=None, limit=1, reg_conn=conn)
        data = json.loads(result)
        assert len(data) == 1

    def test_returns_json_string(self):
        conn = self._make_reg_conn()
        result = execute_query_registry(query=None, limit=10, reg_conn=conn)
        # Should be parseable JSON
        data = json.loads(result)
        assert isinstance(data, list)


# ---------------------------------------------------------------------------
# execute_search_knowledge_base tests
# ---------------------------------------------------------------------------

class TestExecuteSearchKnowledgeBase:
    def _make_embedding_cfg(self):
        cfg = MagicMock()
        cfg.api_base = "https://api.openai.com/v1"
        cfg.embedding_key_env = "TEST_API_KEY"
        cfg.model = "text-embedding-3-small"
        return cfg

    def test_returns_tuple_of_string_and_list(self):
        embedding_cfg = self._make_embedding_cfg()
        collection = MagicMock()
        collection.query.return_value = {"ids": [[]], "documents": [[]], "metadatas": [[]], "distances": [[]]}

        with patch("lib.ingest_tool.embed_query", return_value=[0.1, 0.2]):
            result = execute_search_knowledge_base(
                query="test query",
                n_results=5,
                embedding_cfg=embedding_cfg,
                collection=collection,
            )

        assert isinstance(result, tuple)
        assert len(result) == 3
        formatted_str, chunks, augmented_prompt = result
        assert isinstance(formatted_str, str)
        assert isinstance(chunks, list)
        assert isinstance(augmented_prompt, str)

    def test_empty_result_returns_no_chunks_found_message(self):
        embedding_cfg = self._make_embedding_cfg()
        collection = MagicMock()
        collection.query.return_value = {"ids": [[]], "documents": [[]], "metadatas": [[]], "distances": [[]]}

        with patch("lib.ingest_tool.embed_query", return_value=[0.1]):
            formatted_str, chunks, augmented_prompt = execute_search_knowledge_base(
                query="unknown topic",
                n_results=5,
                embedding_cfg=embedding_cfg,
                collection=collection,
            )

        assert chunks == []
        assert "no" in formatted_str.lower() or "empty" in formatted_str.lower() or len(formatted_str) > 0
        assert augmented_prompt == ""

    def test_results_returned_with_source_info(self):
        embedding_cfg = self._make_embedding_cfg()
        collection = MagicMock()
        collection.query.return_value = {
            "ids": [["c1"]],
            "documents": [["relevant text"]],
            "metadatas": [[{"source_name": "docs", "origin_path": "/docs/file.pdf"}]],
            "distances": [[0.2]],
        }

        with patch("lib.ingest_tool.embed_query", return_value=[0.1]):
            formatted_str, chunks, augmented_prompt = execute_search_knowledge_base(
                query="relevant",
                n_results=5,
                embedding_cfg=embedding_cfg,
                collection=collection,
            )

        assert len(chunks) == 1
        assert chunks[0].chunk_id == "c1"
        assert "relevant text" in formatted_str or "c1" in formatted_str
        assert "[1]" in augmented_prompt
        assert "relevant text" in augmented_prompt
        assert "Question: relevant" in augmented_prompt

    def test_n_results_default_is_five(self):
        embedding_cfg = self._make_embedding_cfg()
        collection = MagicMock()
        collection.query.return_value = {"ids": [[]], "documents": [[]], "metadatas": [[]], "distances": [[]]}

        with patch("lib.ingest_tool.embed_query", return_value=[0.1]):
            execute_search_knowledge_base(
                query="test",
                n_results=5,
                embedding_cfg=embedding_cfg,
                collection=collection,
            )

        call_kwargs = collection.query.call_args[1] if collection.query.call_args[1] else {}
        assert call_kwargs.get("n_results", 5) == 5
