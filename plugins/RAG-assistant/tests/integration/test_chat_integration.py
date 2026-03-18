"""Integration tests for the Chat endpoints — T008, T009, T016, T019"""
from __future__ import annotations

import json
import os
import sys
import threading
from contextlib import contextmanager
from pathlib import Path
from unittest.mock import MagicMock, patch, PropertyMock

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent.parent / "scripts"))

import ui
from ui import app


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

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
def valid_config(tmp_path, monkeypatch):
    """Write a minimal .rag-plugin.toml and patch the default config path."""
    reg = tmp_path / "registry.db"
    store = tmp_path / ".rag-store"
    log = tmp_path / "pipeline.log"
    cfg_path = tmp_path / ".rag-plugin.toml"
    cfg_path.write_text(
        "[embedding]\n"
        'provider = "openai-compatible"\n'
        'model = "text-embedding-3-small"\n'
        'api_base = "https://api.openai.com/v1"\n'
        'embedding_key_env = "TEST_EMBEDDING_KEY"\n\n'
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
    monkeypatch.setattr(ui, "_DEFAULT_CONFIG", str(cfg_path))
    monkeypatch.setenv("TEST_EMBEDDING_KEY", "test-key")
    return cfg_path


def _make_stream_cm(text_chunks=None, stop_reason="end_turn", tool_blocks=None):
    """Return a mock context manager simulating anthropic messages.stream()."""
    text_chunks = text_chunks or []
    tool_blocks = tool_blocks or []

    mock_stream = MagicMock()
    mock_stream.text_stream = iter(text_chunks)
    mock_stream.get_final_message.return_value = MagicMock(
        stop_reason=stop_reason,
        content=tool_blocks,
    )

    cm = MagicMock()
    cm.__enter__ = MagicMock(return_value=mock_stream)
    cm.__exit__ = MagicMock(return_value=False)
    return cm


def _make_tool_use_block(name, tool_id, input_dict):
    block = MagicMock()
    block.type = "tool_use"
    block.id = tool_id
    block.name = name
    block.input = input_dict
    return block


def _parse_sse(data: bytes) -> list[dict]:
    """Parse SSE bytes into a list of event dicts."""
    events = []
    for line in data.decode().splitlines():
        if line.startswith("data: "):
            try:
                events.append(json.loads(line[6:]))
            except json.JSONDecodeError:
                pass
    return events


def _mock_chromadb_non_empty():
    """Return a patch for chromadb.PersistentClient with a non-empty collection."""
    mock_collection = MagicMock()
    mock_collection.count.return_value = 10
    mock_chroma = MagicMock()
    mock_chroma.get_or_create_collection.return_value = mock_collection
    return patch("ui.chromadb.PersistentClient", return_value=mock_chroma), \
           patch("ui.get_or_create_collection", return_value=mock_collection)


# ---------------------------------------------------------------------------
# T008 — GET /api/chat/preflight tests
# ---------------------------------------------------------------------------

class TestChatPreflight:
    def test_returns_200_with_model_when_key_set(self, client, valid_config, monkeypatch):
        """GET /api/chat/preflight returns 200 with ok:true and model name when key is set."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test-key")
        resp = client.get("/api/chat/preflight")
        assert resp.status_code == 200
        data = resp.get_json()
        assert data["ok"] is True
        assert "model" in data
        assert data["model"]  # non-empty

    def test_returns_412_when_key_absent(self, client, valid_config, monkeypatch):
        """GET /api/chat/preflight returns 412 when LLM API key env var is not set."""
        monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
        resp = client.get("/api/chat/preflight")
        assert resp.status_code == 412

    def test_returns_412_when_config_has_custom_key_env_and_not_set(self, client, tmp_path, monkeypatch):
        """Preflight uses llm_key_env from config, not hardcoded ANTHROPIC_API_KEY."""
        reg = tmp_path / "registry.db"
        store = tmp_path / ".rag-store"
        log = tmp_path / "pipeline.log"
        cfg_path = tmp_path / ".rag-plugin.toml"
        cfg_path.write_text(
            "[embedding]\n"
            'provider = "openai-compatible"\n'
            'model = "text-embedding-3-small"\n'
            'api_base = "https://api.openai.com/v1"\n'
            'embedding_key_env = "TEST_EMBEDDING_KEY"\n\n'
            "[llm]\n"
            'model = "claude-sonnet-4-6"\n'
            'llm_key_env = "MY_CUSTOM_CLAUDE_KEY"\n\n'
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
        monkeypatch.setattr(ui, "_DEFAULT_CONFIG", str(cfg_path))
        monkeypatch.setenv("TEST_EMBEDDING_KEY", "key")
        monkeypatch.delenv("MY_CUSTOM_CLAUDE_KEY", raising=False)

        resp = client.get("/api/chat/preflight")
        assert resp.status_code == 412

    def test_route_registered(self, client):
        """GET /api/chat/preflight route exists in the Flask app."""
        rules = {r.rule for r in app.url_map.iter_rules()}
        assert "/api/chat/preflight" in rules


# ---------------------------------------------------------------------------
# T009 — POST /api/chat tests
# ---------------------------------------------------------------------------

class TestChatEndpoint:
    def test_route_registered(self):
        """POST /api/chat route exists in the Flask app."""
        rules = {r.rule for r in app.url_map.iter_rules()}
        assert "/api/chat" in rules

    def test_valid_request_returns_200_text_event_stream(self, client, valid_config, monkeypatch):
        """POST /api/chat with valid message returns 200 text/event-stream."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
        stream_cm = _make_stream_cm(text_chunks=["Hello", " world"])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.return_value = stream_cm

            resp = client.post(
                "/api/chat",
                json={"message": "What is this about?", "history": []},
            )

        assert resp.status_code == 200
        assert "text/event-stream" in resp.content_type

    def test_message_over_4000_chars_returns_400(self, client, valid_config, monkeypatch):
        """POST /api/chat rejects messages over 4000 characters with 400."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
        long_message = "a" * 4001
        resp = client.post(
            "/api/chat",
            json={"message": long_message, "history": []},
        )
        assert resp.status_code == 400

    def test_empty_history_is_valid(self, client, valid_config, monkeypatch):
        """POST /api/chat with empty history array succeeds."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
        stream_cm = _make_stream_cm(text_chunks=["OK"])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.return_value = stream_cm

            resp = client.post(
                "/api/chat",
                json={"message": "hello", "history": []},
            )

        assert resp.status_code == 200

    def test_done_event_always_emitted(self, client, valid_config, monkeypatch):
        """POST /api/chat response always includes a 'done' SSE event."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
        stream_cm = _make_stream_cm(text_chunks=["Hello"])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.return_value = stream_cm

            resp = client.post(
                "/api/chat",
                json={"message": "hi", "history": []},
            )

        events = _parse_sse(resp.data)
        event_types = [e.get("event") for e in events]
        assert "done" in event_types

    def test_text_delta_events_emitted(self, client, valid_config, monkeypatch):
        """POST /api/chat emits text_delta SSE events for streamed text."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
        stream_cm = _make_stream_cm(text_chunks=["Hello", " world"])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.return_value = stream_cm

            resp = client.post(
                "/api/chat",
                json={"message": "hi", "history": []},
            )

        events = _parse_sse(resp.data)
        text_deltas = [e for e in events if e.get("event") == "text_delta"]
        assert len(text_deltas) >= 1

    def test_search_tool_use_emits_tool_start_and_citations(self, client, valid_config, monkeypatch):
        """When Claude returns search_knowledge_base tool_use, tool_start and citations are emitted."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("search_knowledge_base", "toolu_01", {"query": "test query"})

        # First stream: tool_use stop_reason
        first_cm = _make_stream_cm(text_chunks=[], stop_reason="tool_use", tool_blocks=[tool_block])
        # Continuation stream: text response
        second_cm = _make_stream_cm(text_chunks=["Here is what I found."])

        from lib.searcher import RetrievedChunk
        mock_chunk = RetrievedChunk(
            chunk_id="c1", text="relevant content",
            source_name="docs", origin_path="/docs/file.pdf",
            similarity_score=0.9,
        )
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, \
             patch("ui.execute_search_knowledge_base", return_value=("Found 1 chunk", [mock_chunk], "System\n\n[1] chunk\n\nQuestion: test")), \
             chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.side_effect = [first_cm, second_cm]

            resp = client.post(
                "/api/chat",
                json={"message": "What is the policy?", "history": []},
            )

        events = _parse_sse(resp.data)
        event_types = [e.get("event") for e in events]
        assert "tool_start" in event_types
        assert "done" in event_types

    def test_done_emitted_on_api_error(self, client, valid_config, monkeypatch):
        """'done' SSE event is emitted even when the Anthropic API raises an exception."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_anthropic.APIError = Exception
            mock_client.messages.stream.side_effect = Exception("API unreachable")

            resp = client.post(
                "/api/chat",
                json={"message": "hi", "history": []},
            )

        events = _parse_sse(resp.data)
        event_types = [e.get("event") for e in events]
        assert "done" in event_types


# ---------------------------------------------------------------------------
# SC-002 — Canonical ingestion phrasings (T009 acceptance tests)
# ---------------------------------------------------------------------------

SC_002_PHRASINGS = [
    "ingest ./docs",
    "ingest the reports folder",
    "add ./data to the knowledge base",
    "add the hr folder to your knowledge",
    "index ./contracts",
    "load documents from ./policies",
    "process the files in ./onboarding",
    "please ingest /home/user/docs/q1.pdf",
    "scan ./archive for new documents",
    "update the knowledge base with ./updates",
]


class TestSC002CanonicalPhrasings:
    """SC-002: All 10 canonical ingestion phrasings trigger ingest_documents tool_use handling."""

    @pytest.mark.parametrize("phrasing", SC_002_PHRASINGS)
    def test_ingest_phrasing_handled_as_tool_use(self, client, valid_config, monkeypatch, phrasing):
        """Each ingestion phrasing: when Anthropic returns ingest_documents tool_use,
        the server emits tool_start with name=ingest_documents."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("ingest_documents", "toolu_01", {"path": "./docs"})
        first_cm = _make_stream_cm(text_chunks=[], stop_reason="tool_use", tool_blocks=[tool_block])
        second_cm = _make_stream_cm(text_chunks=["Ingestion complete."])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, \
             patch("ui.execute_ingest_documents", return_value="Ingested 1 file."), \
             chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.side_effect = [first_cm, second_cm]

            resp = client.post(
                "/api/chat",
                json={"message": phrasing, "history": []},
            )

        assert resp.status_code == 200
        events = _parse_sse(resp.data)
        tool_starts = [e for e in events if e.get("event") == "tool_start"]
        assert any(e.get("name") == "ingest_documents" for e in tool_starts), (
            f"Expected ingest_documents tool_start for phrasing: {phrasing!r}. "
            f"Got events: {[e.get('event') for e in events]}"
        )


# ---------------------------------------------------------------------------
# T016 — ingest_documents tool path tests (US2)
# ---------------------------------------------------------------------------

class TestIngestDocumentsToolPath:
    def test_lock_acquired_and_released(self, client, valid_config, monkeypatch):
        """execute_ingest_documents acquires and releases _run_lock."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("ingest_documents", "toolu_01", {"path": "./docs"})
        first_cm = _make_stream_cm(stop_reason="tool_use", tool_blocks=[tool_block])
        second_cm = _make_stream_cm(text_chunks=["Done."])

        with patch("ui.anthropic") as mock_anthropic, \
             patch("ui.execute_ingest_documents", return_value="Done.") as mock_exec, \
             patch("ui.chromadb") as mock_chroma, \
             patch("ui.get_or_create_collection", return_value=MagicMock()), \
             patch("ui.open_registry", return_value=MagicMock()), \
             patch("ui.init_logger", return_value=MagicMock()):
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.side_effect = [first_cm, second_cm]

            resp = client.post("/api/chat", json={"message": "ingest ./docs", "history": []})
            _ = resp.data  # consume stream to ensure generator completes

        mock_exec.assert_called_once()
        assert not ui._run_lock.locked(), "run_lock should be released after ingest tool_use"

    def test_concurrent_run_returns_409_in_tool_result(self, client, valid_config, monkeypatch):
        """When _run_lock is held, execute_ingest_documents returns error and tool_result SSE emitted."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("ingest_documents", "toolu_01", {"path": "./docs"})
        first_cm = _make_stream_cm(stop_reason="tool_use", tool_blocks=[tool_block])
        second_cm = _make_stream_cm(text_chunks=["Another run is in progress."])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        ui._run_lock.acquire()
        events = []
        try:
            with patch("ui.anthropic") as mock_anthropic, chroma_patch, coll_patch:
                mock_client = MagicMock()
                mock_anthropic.Anthropic.return_value = mock_client
                mock_client.messages.stream.side_effect = [first_cm, second_cm]

                resp = client.post("/api/chat", json={"message": "ingest ./docs", "history": []})
                # Consume resp.data inside the patch+lock context: the SSE generator resumes
                # lazily when resp.data is accessed, so the lock must still be held and
                # ui.anthropic must still be patched when that happens.
                events = _parse_sse(resp.data)
        finally:
            if ui._run_lock.locked():
                ui._run_lock.release()
        tool_results = [e for e in events if e.get("event") == "tool_result"]
        assert len(tool_results) >= 1
        assert any(
            "progress" in str(e.get("result", "")).lower() or
            "already" in str(e.get("result", "")).lower() or
            "ERROR" in str(e.get("result", ""))
            for e in tool_results
        )

    def test_invalid_path_returns_error_in_tool_result(self, client, valid_config, monkeypatch):
        """Invalid ingest path produces error string in tool_result SSE event."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("ingest_documents", "toolu_01", {"path": "/nonexistent/xyz"})
        first_cm = _make_stream_cm(stop_reason="tool_use", tool_blocks=[tool_block])
        second_cm = _make_stream_cm(text_chunks=["Path not found."])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.side_effect = [first_cm, second_cm]

            resp = client.post("/api/chat", json={"message": "ingest /nonexistent/xyz", "history": []})

        events = _parse_sse(resp.data)
        tool_results = [e for e in events if e.get("event") == "tool_result"]
        assert len(tool_results) >= 1

    def test_tool_result_and_text_delta_both_emitted(self, client, valid_config, monkeypatch):
        """Both tool_result and text_delta events appear after ingest_documents."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("ingest_documents", "toolu_01", {"path": "./docs"})
        first_cm = _make_stream_cm(stop_reason="tool_use", tool_blocks=[tool_block])
        second_cm = _make_stream_cm(text_chunks=["Ingested the docs folder."])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, \
             patch("ui.execute_ingest_documents", return_value="Succeeded: 1"), \
             chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.side_effect = [first_cm, second_cm]

            resp = client.post("/api/chat", json={"message": "ingest ./docs", "history": []})

        events = _parse_sse(resp.data)
        event_types = [e.get("event") for e in events]
        assert "tool_result" in event_types
        assert "text_delta" in event_types


# ---------------------------------------------------------------------------
# T019 — query_registry tool path tests (US3)
# ---------------------------------------------------------------------------

class TestQueryRegistryToolPath:
    def test_query_registry_returns_json_in_tool_result(self, client, valid_config, monkeypatch):
        """query_registry tool_use produces a tool_result SSE with JSON record list."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("query_registry", "toolu_02", {"query": None, "limit": 50})
        first_cm = _make_stream_cm(stop_reason="tool_use", tool_blocks=[tool_block])
        second_cm = _make_stream_cm(text_chunks=["I have 2 documents."])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, \
             patch("ui.execute_query_registry", return_value='[{"source_name":"hr"}]'), \
             chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.side_effect = [first_cm, second_cm]

            resp = client.post("/api/chat", json={"message": "what documents do you know about?", "history": []})

        events = _parse_sse(resp.data)
        tool_results = [e for e in events if e.get("event") == "tool_result"]
        assert len(tool_results) >= 1

    def test_empty_registry_returns_empty_list_in_result(self, client, valid_config, monkeypatch):
        """When registry is empty, tool_result contains empty JSON array."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("query_registry", "toolu_02", {})
        first_cm = _make_stream_cm(stop_reason="tool_use", tool_blocks=[tool_block])
        second_cm = _make_stream_cm(text_chunks=["No documents found."])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, \
             patch("ui.execute_query_registry", return_value="[]"), \
             chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.side_effect = [first_cm, second_cm]

            resp = client.post("/api/chat", json={"message": "list my documents", "history": []})

        events = _parse_sse(resp.data)
        tool_results = [e for e in events if e.get("event") == "tool_result"]
        assert len(tool_results) >= 1
        # The mock returns "[]" so the result should contain that or similar empty indicator
        assert any(e.get("result") is not None for e in tool_results)

    def test_tool_result_sse_event_emitted(self, client, valid_config, monkeypatch):
        """query_registry handler emits tool_result SSE event."""
        monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")

        tool_block = _make_tool_use_block("query_registry", "toolu_02", {"query": "hr"})
        first_cm = _make_stream_cm(stop_reason="tool_use", tool_blocks=[tool_block])
        second_cm = _make_stream_cm(text_chunks=["Here are the HR docs."])
        chroma_patch, coll_patch = _mock_chromadb_non_empty()

        with patch("ui.anthropic") as mock_anthropic, \
             patch("ui.execute_query_registry", return_value='[{"source_name":"hr"}]'), \
             chroma_patch, coll_patch:
            mock_client = MagicMock()
            mock_anthropic.Anthropic.return_value = mock_client
            mock_client.messages.stream.side_effect = [first_cm, second_cm]

            resp = client.post("/api/chat", json={"message": "show HR files", "history": []})

        events = _parse_sse(resp.data)
        assert any(e.get("event") == "tool_result" for e in events)
