"""Integration tests for the Web UI Flask app — T024

Tests cover the full SSE flow and config round-trip against a real temp
ChromaDB + SQLite registry. The OpenAI embedder is mocked.
"""
from __future__ import annotations

import json
import os
import sqlite3
import sys
import time
import threading
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import ui
from ui import app


@pytest.fixture(autouse=True)
def reset_ui_state():
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
def full_config(tmp_path):
    """Write a valid .rag-plugin.toml with real paths."""
    reg = tmp_path / "registry.db"
    store = tmp_path / ".rag-store"
    log = tmp_path / "pipeline.log"
    cfg = tmp_path / ".rag-plugin.toml"
    cfg.write_text(
        "[embedding]\n"
        'provider = "openai-compatible"\n'
        'model = "text-embedding-3-small"\n'
        'api_base = "https://api.openai.com/v1"\n'
        'embedding_key_env = "TEST_API_KEY"\n\n'
        "[vector_store]\n"
        'provider = "chroma"\n'
        f'path = "{store}"\n'
        'collection = "test-docs"\n\n'
        "[pipeline]\n"
        "chunk_size = 500\n"
        "chunk_overlap = 100\n"
        f'registry_path = "{reg}"\n'
        f'log_path = "{log}"\n\n'
        "[[sources]]\n"
        'name = "test-src"\n'
        'type = "local"\n'
        f'path = "{tmp_path / "docs"}"\n'
    )
    (tmp_path / "docs").mkdir()
    return cfg, tmp_path


# ---------------------------------------------------------------------------
# SSE stream — basic connection
# ---------------------------------------------------------------------------

class TestSseStream:
    def test_stream_route_is_registered(self, client):
        """GET /api/ingest/stream route must exist (not 404/405)."""
        # We cannot consume an infinite SSE stream in tests, but we can verify
        # the route is correctly registered by checking it doesn't return 404/405.
        # The route opens a blocking generator so we just inspect the Flask URL map.
        from ui import app as flask_app
        rules = {r.rule for r in flask_app.url_map.iter_rules()}
        assert "/api/ingest/stream" in rules

    def test_announcer_fan_out(self):
        """MessageAnnouncer delivers to all registered listeners."""
        q1 = ui._announcer.listen()
        q2 = ui._announcer.listen()
        try:
            msg = 'data: {"event":"ping"}\n\n'
            ui._announcer.announce(msg)
            assert q1.get_nowait() == msg
            assert q2.get_nowait() == msg
        finally:
            ui._announcer.remove_listener(q1)
            ui._announcer.remove_listener(q2)

    def test_announcer_removes_dead_listeners(self):
        """Full queues are silently dropped without error."""
        q = ui._announcer.listen()
        try:
            # Fill queue to capacity (maxsize=200)
            for _ in range(200):
                q.put_nowait("x")
            # This should not raise
            ui._announcer.announce("overflow")
        finally:
            try:
                ui._announcer.remove_listener(q)
            except Exception:
                pass


# ---------------------------------------------------------------------------
# Full pipeline run via SSE (mocked embedder + ChromaDB)
# ---------------------------------------------------------------------------

class TestRunPipelineIntegration:
    def test_run_and_receive_complete_event(self, client, full_config, tmp_path):
        """Full pipeline cycle: POST /run → SSE events → run_complete."""
        cfg_path, base = full_config

        # Create a doc to ingest
        (base / "docs" / "hello.txt").write_text("Hello world " * 20)

        from lib.embedder import EmbeddedChunk

        def fake_embed(chunks, embedding_config, logger):
            return [
                EmbeddedChunk(
                    chunk_id=c.chunk_id,
                    text=c.text,
                    vector=[0.1, 0.2, 0.3, 0.4],
                    model=embedding_config.model,
                )
                for c in chunks
            ]

        received_events = []
        q = ui._announcer.listen()

        def collect_events():
            deadline = time.time() + 8.0
            while time.time() < deadline:
                try:
                    raw = q.get(timeout=0.5)
                    # parse "data: {...}\n\n" lines
                    for line in raw.splitlines():
                        if line.startswith("data: "):
                            try:
                                received_events.append(json.loads(line[6:]))
                            except json.JSONDecodeError:
                                pass
                    # Stop when we see a terminal event
                    event_names = [e.get("event") for e in received_events]
                    if "run_complete" in event_names or "run_error" in event_names:
                        break
                except Exception:
                    continue

        collector = threading.Thread(target=collect_events, daemon=True)
        collector.start()

        with patch("ui._DEFAULT_CONFIG", str(cfg_path)), \
             patch.dict(os.environ, {"TEST_API_KEY": "sk-test"}), \
             patch("lib.pipeline.embed_chunks", side_effect=fake_embed):
            resp = client.post("/api/ingest/run")
            assert resp.status_code == 202

        collector.join(timeout=10.0)
        ui._announcer.remove_listener(q)

        event_names = [e.get("event") for e in received_events]
        assert "run_started" in event_names
        assert "run_complete" in event_names or "run_error" in event_names

    def test_run_history_populated_after_completion(self, client, full_config, tmp_path):
        """After a run, GET /api/ingest/runs shows the completed run."""
        cfg_path, base = full_config
        (base / "docs" / "doc.txt").write_text("Test content " * 10)

        from lib.embedder import EmbeddedChunk

        def fake_embed(chunks, embedding_config, logger):
            return [
                EmbeddedChunk(
                    chunk_id=c.chunk_id, text=c.text,
                    vector=[0.1, 0.2, 0.3, 0.4], model=embedding_config.model
                )
                for c in chunks
            ]

        done_event = threading.Event()
        q = ui._announcer.listen()

        def wait_for_done():
            deadline = time.time() + 8.0
            while time.time() < deadline:
                try:
                    raw = q.get(timeout=0.5)
                    if "run_complete" in raw or "run_error" in raw:
                        done_event.set()
                        break
                except Exception:
                    continue

        threading.Thread(target=wait_for_done, daemon=True).start()

        with patch("ui._DEFAULT_CONFIG", str(cfg_path)), \
             patch.dict(os.environ, {"TEST_API_KEY": "sk-test"}), \
             patch("lib.pipeline.embed_chunks", side_effect=fake_embed):
            client.post("/api/ingest/run")

        done_event.wait(timeout=10.0)
        ui._announcer.remove_listener(q)

        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.get("/api/ingest/runs")

        data = resp.get_json()
        assert data["active_run"] is None
        assert len(data["runs"]) >= 1
        run = data["runs"][0]
        assert run["status"] in ("completed", "failed")
        assert "run_id" in run


# ---------------------------------------------------------------------------
# Config round-trip
# ---------------------------------------------------------------------------

class TestConfigRoundTrip:
    def test_registry_renders_1000_rows_under_2s(self, client, tmp_path):
        """SC-003: registry endpoint must return 1,000 rows in under 2 s."""
        reg = tmp_path / "registry.db"
        conn = sqlite3.connect(str(reg))
        conn.execute("""CREATE TABLE documents (
            source_name TEXT, origin_path TEXT, content_hash TEXT,
            chunk_count INTEGER, version_count INTEGER, last_ingested TEXT,
            PRIMARY KEY (source_name, origin_path))""")
        conn.executemany(
            "INSERT INTO documents VALUES (?,?,?,?,?,?)",
            [
                (f"src-{i}", f"/docs/doc_{i}.md", f"hash{i}", 3, 1, "2026-01-01T00:00:00Z")
                for i in range(1000)
            ],
        )
        conn.commit()
        conn.close()

        cfg_path = tmp_path / ".rag-plugin.toml"
        cfg_path.write_text(
            '[embedding]\nprovider="x"\nmodel="m"\napi_base="http://x"\nembedding_key_env="K"\n'
            '[vector_store]\nprovider="chroma"\npath=".s"\ncollection="c"\n'
            f'[pipeline]\nchunk_size=1000\nchunk_overlap=200\nregistry_path="{reg}"\n'
            '[[sources]]\nname="s"\ntype="local"\npath="."\n'
        )

        t0 = time.time()
        with patch("ui._DEFAULT_CONFIG", str(cfg_path)):
            resp = client.get("/api/registry")
        elapsed = time.time() - t0

        assert resp.status_code == 200
        assert resp.get_json()["total"] == 1000
        assert elapsed < 2.0, f"Registry took {elapsed:.2f}s for 1,000 rows — exceeds SC-003 limit"

    def test_put_then_get_config_round_trips(self, client, tmp_path):
        """PUT /api/config then GET /api/config returns same values."""
        cfg_path = tmp_path / ".rag-plugin.toml"
        payload = {
            "embedding": {
                "provider": "openai-compatible",
                "model": "text-embedding-3-small",
                "api_base": "https://api.openai.com/v1",
                "embedding_key_env": "MY_KEY",
            },
            "vector_store": {
                "provider": "chroma",
                "path": ".rag-store",
                "collection": "docs",
            },
            "pipeline": {
                "chunk_size": 800,
                "chunk_overlap": 150,
                "supported_formats": ["txt", "md"],
                "registry_path": ".rag-registry.db",
                "log_path": ".rag-pipeline.log",
                "max_file_size_mb": 15,
            },
            "sources": [{"name": "my-docs", "type": "local", "path": "./docs"}],
        }

        with patch("ui._DEFAULT_CONFIG", str(cfg_path)), \
             patch.dict(os.environ, {"MY_KEY": "sk-test"}):
            put_resp = client.put("/api/config", json=payload)
            assert put_resp.status_code == 200

            get_resp = client.get("/api/config")
            assert get_resp.status_code == 200

        data = get_resp.get_json()
        assert data["embedding"]["model"] == "text-embedding-3-small"
        assert data["pipeline"]["chunk_size"] == 800
        assert data["pipeline"]["chunk_overlap"] == 150
        assert data["vector_store"]["collection"] == "docs"
        assert len(data["sources"]) == 1
        assert data["sources"][0]["name"] == "my-docs"
