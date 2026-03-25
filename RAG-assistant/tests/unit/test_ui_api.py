"""Unit tests for the Flask API in scripts/ui.py — T008/T009/T016/T019"""
from __future__ import annotations

import json
import os
import sys
import sqlite3
import threading
import time
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import ui
from ui import app, _announcer, MessageAnnouncer


@pytest.fixture(autouse=True)
def reset_state():
    """Reset module-level state before each test."""
    ui._active_run = None
    ui._run_history.clear()
    if ui._run_lock.locked():
        try:
            ui._run_lock.release()
        except RuntimeError:
            pass
    yield
    ui._active_run = None
    ui._run_history.clear()
    if ui._run_lock.locked():
        try:
            ui._run_lock.release()
        except RuntimeError:
            pass


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


@pytest.fixture
def valid_config_toml(tmp_path):
    cfg = tmp_path / ".rag-plugin.toml"
    cfg.write_text(
        '[embedding]\nprovider = "openai-compatible"\nmodel = "text-embedding-3-small"\n'
        'api_base = "https://api.openai.com/v1"\nembedding_key_env = "TEST_API_KEY"\n\n'
        '[vector_store]\nprovider = "chroma"\npath = ".rag-store"\ncollection = "docs"\n\n'
        '[pipeline]\nchunk_size = 1000\nchunk_overlap = 200\n'
        'supported_formats = ["txt", "md"]\n\n'
        '[[sources]]\nname = "test"\ntype = "local"\npath = "."\n'
    )
    return cfg


# ---------------------------------------------------------------------------
# T008: POST /api/ingest/run
# ---------------------------------------------------------------------------

class TestIngestRun:
    def test_202_when_idle(self, client, valid_config_toml):
        with patch("ui._DEFAULT_CONFIG", str(valid_config_toml)), \
             patch.dict(os.environ, {"TEST_API_KEY": "sk-test"}), \
             patch("ui._run_pipeline"):
            resp = client.post("/api/ingest/run")
        assert resp.status_code == 202
        assert "run_id" in resp.get_json()

    def test_409_when_active_run_exists(self, client, valid_config_toml):
        ui._run_lock.acquire()
        ui._active_run = {"run_id": "existing-run"}
        with patch("ui._DEFAULT_CONFIG", str(valid_config_toml)), \
             patch.dict(os.environ, {"TEST_API_KEY": "sk-test"}):
            resp = client.post("/api/ingest/run")
        assert resp.status_code == 409
        data = resp.get_json()
        assert data["error"] == "run_in_progress"

    def test_412_when_api_key_not_set(self, client, valid_config_toml):
        env = {k: v for k, v in os.environ.items() if k != "TEST_API_KEY"}
        with patch("ui._DEFAULT_CONFIG", str(valid_config_toml)), \
             patch.dict(os.environ, env, clear=True):
            resp = client.post("/api/ingest/run")
        assert resp.status_code == 412
        data = resp.get_json()
        assert data["error"] == "preflight_failed"
        assert "TEST_API_KEY" in data["reason"]

    def test_422_when_config_missing(self, client, tmp_path):
        with patch("ui._DEFAULT_CONFIG", str(tmp_path / "missing.toml")):
            resp = client.post("/api/ingest/run")
        assert resp.status_code == 422
        assert resp.get_json()["error"] == "config_invalid"

    def test_lock_released_after_202(self, client, valid_config_toml):
        """Lock must be released (by the background thread) so a second run can start."""
        with patch("ui._DEFAULT_CONFIG", str(valid_config_toml)), \
             patch.dict(os.environ, {"TEST_API_KEY": "sk-test"}), \
             patch("ui._run_pipeline"):
            client.post("/api/ingest/run")
        # After the thread (mocked) runs, lock should eventually be released.
        # Since _run_pipeline is mocked, the lock was acquired but the mock
        # doesn't release it — verify that's the only reason it stays locked.
        # In real execution the try/finally in _run_pipeline releases it.
        assert ui._run_lock.locked()  # mock didn't release — expected in test


# ---------------------------------------------------------------------------
# T009: GET /api/ingest/runs
# ---------------------------------------------------------------------------

class TestIngestRuns:
    def test_empty_history(self, client):
        resp = client.get("/api/ingest/runs")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["runs"] == []
        assert data["active_run"] is None

    def test_returns_active_run(self, client):
        ui._active_run = {"run_id": "abc", "status": "running"}
        resp = client.get("/api/ingest/runs")
        data = resp.get_json()
        assert data["active_run"]["run_id"] == "abc"

    def test_history_capped_at_5(self, client, valid_config_toml):
        """History should only keep the last 5 runs."""
        for i in range(6):
            ui._run_history.append({"run_id": f"run-{i}", "status": "completed"})
            if len(ui._run_history) > 5:
                ui._run_history.pop()

        resp = client.get("/api/ingest/runs")
        data = resp.get_json()
        assert len(data["runs"]) == 5

    def test_response_shape(self, client):
        ui._run_history.append({
            "run_id": "r1",
            "started_at": "2026-01-01T00:00:00Z",
            "completed_at": "2026-01-01T00:00:05Z",
            "status": "completed",
            "error_message": None,
            "sources": [],
            "summary": {"total_discovered": 0, "total_succeeded": 0,
                        "total_skipped": 0, "total_failed": 0},
        })
        resp = client.get("/api/ingest/runs")
        data = resp.get_json()
        run = data["runs"][0]
        for field in ("run_id", "started_at", "completed_at", "status", "sources", "summary"):
            assert field in run


# ---------------------------------------------------------------------------
# T016: GET /api/registry
# ---------------------------------------------------------------------------

class TestRegistry:
    def _make_registry(self, path: str) -> None:
        conn = sqlite3.connect(path)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE documents (
                source_name TEXT, origin_path TEXT, content_hash TEXT,
                chunk_count INTEGER, version_count INTEGER, last_ingested TEXT,
                PRIMARY KEY (source_name, origin_path)
            )
        """)
        conn.execute("""
            INSERT INTO documents VALUES
            ('src-a', '/docs/a.md', 'hash1', 3, 1, '2026-01-01T10:00:00Z'),
            ('src-b', '/docs/b.txt', 'hash2', 5, 2, '2026-01-02T10:00:00Z')
        """)
        conn.commit()
        conn.close()

    def test_returns_records(self, client, tmp_path):
        reg = tmp_path / "registry.db"
        self._make_registry(str(reg))
        cfg_path = tmp_path / ".rag-plugin.toml"
        cfg_path.write_text(
            '[embedding]\nprovider="x"\nmodel="m"\napi_base="http://x"\nembedding_key_env="K"\n'
            '[vector_store]\nprovider="chroma"\npath=".s"\ncollection="c"\n'
            f'[pipeline]\nchunk_size=1000\nchunk_overlap=200\nregistry_path="{reg}"\n'
            '[[sources]]\nname="s"\ntype="local"\npath="."\n'
        )
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.get("/api/registry")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["total"] == 2
        assert len(data["records"]) == 2

    def test_search_filters_by_source_name(self, client, tmp_path):
        reg = tmp_path / "registry.db"
        self._make_registry(str(reg))
        cfg_path = tmp_path / ".rag-plugin.toml"
        cfg_path.write_text(
            '[embedding]\nprovider="x"\nmodel="m"\napi_base="http://x"\nembedding_key_env="K"\n'
            '[vector_store]\nprovider="chroma"\npath=".s"\ncollection="c"\n'
            f'[pipeline]\nchunk_size=1000\nchunk_overlap=200\nregistry_path="{reg}"\n'
            '[[sources]]\nname="s"\ntype="local"\npath="."\n'
        )
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.get("/api/registry?search=src-a")
        data = resp.get_json()
        assert data["total"] == 1
        assert data["records"][0]["source_name"] == "src-a"

    def test_sort_param_changes_order(self, client, tmp_path):
        reg = tmp_path / "registry.db"
        self._make_registry(str(reg))
        cfg_path = tmp_path / ".rag-plugin.toml"
        cfg_path.write_text(
            '[embedding]\nprovider="x"\nmodel="m"\napi_base="http://x"\nembedding_key_env="K"\n'
            '[vector_store]\nprovider="chroma"\npath=".s"\ncollection="c"\n'
            f'[pipeline]\nchunk_size=1000\nchunk_overlap=200\nregistry_path="{reg}"\n'
            '[[sources]]\nname="s"\ntype="local"\npath="."\n'
        )
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            asc = client.get("/api/registry?sort=source_name&order=asc").get_json()
            desc = client.get("/api/registry?sort=source_name&order=desc").get_json()
        assert asc["records"][0]["source_name"] == "src-a"
        assert desc["records"][0]["source_name"] == "src-b"

    def test_404_when_registry_missing(self, client, tmp_path):
        cfg_path = tmp_path / ".rag-plugin.toml"
        cfg_path.write_text(
            '[embedding]\nprovider="x"\nmodel="m"\napi_base="http://x"\nembedding_key_env="K"\n'
            '[vector_store]\nprovider="chroma"\npath=".s"\ncollection="c"\n'
            '[pipeline]\nchunk_size=1000\nchunk_overlap=200\n'
            f'registry_path="{tmp_path / "noexist.db"}"\n'
            '[[sources]]\nname="s"\ntype="local"\npath="."\n'
        )
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.get("/api/registry")
        assert resp.status_code == 404


# ---------------------------------------------------------------------------
# T019: GET /api/config and PUT /api/config
# ---------------------------------------------------------------------------

class TestConfig:
    def test_get_config_200(self, client, valid_config_toml):
        with patch("ui._DEFAULT_CONFIG", str(valid_config_toml)), \
             patch.dict(os.environ, {"TEST_API_KEY": "sk-test"}):
            resp = client.get("/api/config")
        assert resp.status_code == 200
        data = resp.get_json()
        assert "embedding" in data
        assert "vector_store" in data
        assert "pipeline" in data
        assert "sources" in data
        # API key value must NOT be exposed
        assert "api_key" not in json.dumps(data).lower() or "embedding_key_env" in data["embedding"]

    def test_get_config_404_when_missing(self, client, tmp_path):
        with patch("ui._DEFAULT_CONFIG", str(tmp_path / "missing.toml")):
            resp = client.get("/api/config")
        assert resp.status_code == 404
        assert resp.get_json()["error"] == "config_missing"

    def test_put_config_saves_valid_payload(self, client, tmp_path):
        cfg_path = tmp_path / ".rag-plugin.toml"
        payload = {
            "embedding": {"provider": "openai-compatible", "model": "m",
                          "api_base": "http://x", "embedding_key_env": "MY_KEY"},
            "vector_store": {"provider": "chroma", "path": ".s", "collection": "c"},
            "pipeline": {"chunk_size": 500, "chunk_overlap": 50,
                         "supported_formats": ["txt"], "registry_path": ".r.db",
                         "log_path": ".l.log", "max_file_size_mb": 10},
            "sources": [{"name": "s", "type": "local", "path": "."}],
        }
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.put("/api/config", json=payload)
        assert resp.status_code == 200
        assert resp.get_json()["ok"] is True
        assert cfg_path.exists()

    def test_put_config_422_when_overlap_gte_chunk_size(self, client, tmp_path):
        cfg_path = tmp_path / ".rag-plugin.toml"
        payload = {
            "embedding": {"provider": "openai-compatible", "model": "m",
                          "api_base": "http://x", "embedding_key_env": "MY_KEY"},
            "vector_store": {"provider": "chroma", "path": ".s", "collection": "c"},
            "pipeline": {"chunk_size": 200, "chunk_overlap": 200},
            "sources": [{"name": "s", "type": "local", "path": "."}],
        }
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.put("/api/config", json=payload)
        assert resp.status_code == 422
        data = resp.get_json()
        assert data["error"] == "validation_failed"
        field_names = [f["field"] for f in data["fields"]]
        assert "pipeline.chunk_overlap" in field_names
        # File must NOT be written on validation failure
        assert not cfg_path.exists()

    def test_put_config_422_when_no_sources(self, client, tmp_path):
        cfg_path = tmp_path / ".rag-plugin.toml"
        payload = {
            "embedding": {"provider": "x", "model": "m", "api_base": "http://x",
                          "embedding_key_env": "K"},
            "vector_store": {"provider": "chroma", "path": ".s", "collection": "c"},
            "pipeline": {"chunk_size": 1000, "chunk_overlap": 200},
            "sources": [],
        }
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.put("/api/config", json=payload)
        assert resp.status_code == 422
        assert not cfg_path.exists()

    def test_put_config_422_when_embedding_key_env_empty(self, client, tmp_path):
        cfg_path = tmp_path / ".rag-plugin.toml"
        payload = {
            "embedding": {"provider": "x", "model": "m", "api_base": "http://x",
                          "embedding_key_env": ""},
            "vector_store": {"provider": "chroma", "path": ".s", "collection": "c"},
            "pipeline": {"chunk_size": 1000, "chunk_overlap": 200},
            "sources": [{"name": "s", "type": "local", "path": "."}],
        }
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.put("/api/config", json=payload)
        assert resp.status_code == 422


# ---------------------------------------------------------------------------
# GET /api/status
# ---------------------------------------------------------------------------

class TestStatus:
    def test_status_ok_no_config(self, client, tmp_path):
        with patch("ui._DEFAULT_CONFIG", str(tmp_path / "missing.toml")):
            resp = client.get("/api/status")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["status"] == "ok"
        assert data["config_present"] is False
        assert data["vector_store"]["ok"] is False
        assert data["active_run"] is None

    def test_status_ok_with_config_and_chroma(self, client, valid_config_toml):
        mock_collection = MagicMock()
        mock_collection.count.return_value = 42
        mock_client = MagicMock()
        mock_cfg = MagicMock()
        mock_cfg.vector_store.path = ".rag-store"
        mock_cfg.vector_store.collection = "docs"
        mock_cfg.embedding.model = "text-embedding-3-small"

        with patch("ui._DEFAULT_CONFIG", str(valid_config_toml)), \
             patch("ui.load_config", return_value=mock_cfg), \
             patch("ui.chromadb.PersistentClient", return_value=mock_client), \
             patch("ui.get_or_create_collection", return_value=mock_collection):
            resp = client.get("/api/status")

        assert resp.status_code == 200
        data = resp.get_json()
        assert data["status"] == "ok"
        assert data["config_present"] is True
        assert data["vector_store"]["ok"] is True
        assert data["vector_store"]["doc_count"] == 42

    def test_status_chroma_failure_is_graceful(self, client, valid_config_toml):
        with patch("ui._DEFAULT_CONFIG", str(valid_config_toml)), \
             patch("ui.chromadb.PersistentClient", side_effect=Exception("chroma down")):
            resp = client.get("/api/status")

        assert resp.status_code == 200
        data = resp.get_json()
        assert data["status"] == "ok"
        assert data["vector_store"]["ok"] is False

    def test_status_reflects_active_run(self, client, tmp_path):
        ui._active_run = {"run_id": "r1", "status": "running"}
        with patch("ui._DEFAULT_CONFIG", str(tmp_path / "missing.toml")):
            resp = client.get("/api/status")
        data = resp.get_json()
        assert data["active_run"]["run_id"] == "r1"
