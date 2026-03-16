"""RAG Ingestion Pipeline Web UI — scripts/ui.py

Start with:
    python scripts/ui.py
    open http://localhost:7842

Port is fixed at 7842 (FR-012). Single-user local server only.
"""
from __future__ import annotations

import json
import os
import queue
import sqlite3
import sys
import threading
import uuid
import datetime
from pathlib import Path
from typing import Optional

import anthropic

# Ensure scripts/ is on sys.path so `lib.*` imports work.
sys.path.insert(0, str(Path(__file__).parent))

import chromadb
import tomli_w
from flask import Flask, Response, jsonify, render_template, request, stream_with_context

from lib.config import load_config, ConfigError, LocalSourceConfig
from lib.logger import init_logger
from lib.registry import open_registry
from lib.store import get_or_create_collection, check_model_consistency, ModelMismatchError
from lib.pipeline import run_ingestion, SourceResult, IngestionEvent
from lib.ingest_tool import (
    TOOL_SCHEMAS,
    execute_ingest_documents,
    execute_query_registry,
    execute_search_knowledge_base,
)

app = Flask(__name__, template_folder="templates")

_DEFAULT_CONFIG = ".rag-plugin.toml"

# ---------------------------------------------------------------------------
# SSE announcer
# ---------------------------------------------------------------------------

class MessageAnnouncer:
    """Fan-out SSE announcer. Each listener gets its own queue."""

    def __init__(self) -> None:
        self._listeners: list[queue.Queue] = []
        self._lock = threading.Lock()

    def listen(self) -> queue.Queue:
        q: queue.Queue = queue.Queue(maxsize=200)
        with self._lock:
            self._listeners.append(q)
        return q

    def announce(self, msg: str) -> None:
        with self._lock:
            dead = []
            for i, q in enumerate(self._listeners):
                try:
                    q.put_nowait(msg)
                except queue.Full:
                    dead.append(i)
            for i in reversed(dead):
                self._listeners.pop(i)

    def remove_listener(self, q: queue.Queue) -> None:
        with self._lock:
            try:
                self._listeners.remove(q)
            except ValueError:
                pass


_announcer = MessageAnnouncer()

# ---------------------------------------------------------------------------
# In-memory run state (module-level, session-scoped)
# ---------------------------------------------------------------------------

_run_lock = threading.Lock()
_active_run: Optional[dict] = None
_run_history: list[dict] = []   # newest first, max 5

_MAX_HISTORY = 5


# ---------------------------------------------------------------------------
# SSE helpers
# ---------------------------------------------------------------------------

def _format_sse(data: dict) -> str:
    return f"data: {json.dumps(data)}\n\n"


# ---------------------------------------------------------------------------
# Background pipeline runner
# ---------------------------------------------------------------------------

def _run_pipeline(run_id: str) -> None:
    """Executed in a background thread. Releases _run_lock in a finally block."""
    global _active_run, _run_history

    started_at = datetime.datetime.utcnow().isoformat() + "Z"
    _announcer.announce(_format_sse({
        "event": "run_started",
        "run_id": run_id,
        "started_at": started_at,
    }))

    try:
        cfg = load_config(_DEFAULT_CONFIG)
        logger = init_logger(cfg.pipeline.log_path)

        chroma_client = chromadb.PersistentClient(path=cfg.vector_store.path)
        collection = get_or_create_collection(
            chroma_client, cfg.vector_store.collection, cfg.embedding.model
        )
        check_model_consistency(collection, cfg.embedding.model)

        reg_conn = open_registry(cfg.pipeline.registry_path)

        def progress_callback(event: IngestionEvent) -> None:
            _announcer.announce(_format_sse({
                "event": "document_processed",
                "run_id": run_id,
                "source_name": event.source_name,
                "file_path": event.file_path,
                "status": event.status,
                "reason": event.reason,
            }))

        results = run_ingestion(
            cfg.sources, cfg, logger, chroma_client, collection, reg_conn,
            progress_callback=progress_callback,
        )
        reg_conn.close()

        # Build per-source summaries
        source_dicts = []
        for r in results:
            source_dicts.append({
                "label": r.label,
                "discovered": r.discovered,
                "succeeded": r.succeeded,
                "skipped": r.skipped,
                "failed": r.failed,
                "skipped_unchanged": r.skipped_unchanged,
                "skipped_duplicate": r.skipped_duplicate,
                "failed_docs": r.failed_docs,
                "status": r.status,
                "error_message": r.error_message,
            })
            _announcer.announce(_format_sse({
                "event": "source_complete",
                "run_id": run_id,
                "source_name": r.label,
                "discovered": r.discovered,
                "succeeded": r.succeeded,
                "skipped": r.skipped,
                "failed": r.failed,
            }))

        completed_at = datetime.datetime.utcnow().isoformat() + "Z"
        summary = {
            "total_discovered": sum(r["discovered"] for r in source_dicts),
            "total_succeeded": sum(r["succeeded"] for r in source_dicts),
            "total_skipped": sum(r["skipped"] for r in source_dicts),
            "total_failed": sum(r["failed"] for r in source_dicts),
        }

        run_record = {
            "run_id": run_id,
            "started_at": started_at,
            "completed_at": completed_at,
            "status": "completed",
            "error_message": None,
            "sources": source_dicts,
            "summary": summary,
        }

        _run_history.insert(0, run_record)
        if len(_run_history) > _MAX_HISTORY:
            _run_history.pop()

        _active_run = None

        _announcer.announce(_format_sse({
            "event": "run_complete",
            "run_id": run_id,
            "completed_at": completed_at,
            **summary,
        }))

    except Exception as exc:
        completed_at = datetime.datetime.utcnow().isoformat() + "Z"
        error_message = str(exc)

        run_record = {
            "run_id": run_id,
            "started_at": started_at,
            "completed_at": completed_at,
            "status": "failed",
            "error_message": error_message,
            "sources": [],
            "summary": None,
        }
        _run_history.insert(0, run_record)
        if len(_run_history) > _MAX_HISTORY:
            _run_history.pop()

        _active_run = None

        _announcer.announce(_format_sse({
            "event": "run_error",
            "run_id": run_id,
            "error_message": error_message,
        }))

    finally:
        # Always release the lock — even if an unhandled exception escapes the
        # broad except above (e.g. SystemExit, KeyboardInterrupt). Fixes I1.
        if _run_lock.locked():
            try:
                _run_lock.release()
            except RuntimeError:
                pass  # already released


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/")
def index():
    return render_template("index.html")


@app.post("/api/ingest/run")
def ingest_run():
    global _active_run

    import tomllib

    # Step 1: check config file exists and is valid TOML
    config_path = Path(_DEFAULT_CONFIG)
    if not config_path.exists():
        return jsonify({"error": "config_invalid", "message": f"{_DEFAULT_CONFIG} not found"}), 422

    try:
        raw = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except Exception as exc:
        return jsonify({"error": "config_invalid", "message": str(exc)}), 422

    # Step 2: preflight — check API key env var before full config validation
    api_key_env = raw.get("embedding", {}).get("api_key_env", "")
    if api_key_env and not os.environ.get(api_key_env):
        return jsonify({
            "error": "preflight_failed",
            "reason": f"Environment variable {api_key_env} is not set",
        }), 412

    # Step 3: full config validation (validates URLs, chunk sizes, etc.)
    try:
        load_config(_DEFAULT_CONFIG)
    except ConfigError as exc:
        return jsonify({"error": "config_invalid", "message": str(exc)}), 422

    # Concurrency guard
    if not _run_lock.acquire(blocking=False):
        return jsonify({
            "error": "run_in_progress",
            "run_id": _active_run["run_id"] if _active_run else None,
        }), 409

    run_id = str(uuid.uuid4())
    _active_run = {
        "run_id": run_id,
        "started_at": datetime.datetime.utcnow().isoformat() + "Z",
        "status": "running",
    }

    t = threading.Thread(target=_run_pipeline, args=(run_id,), daemon=True)
    t.start()

    return jsonify({"run_id": run_id}), 202


@app.get("/api/ingest/stream")
def ingest_stream():
    q = _announcer.listen()

    def generate():
        try:
            while True:
                msg = q.get()
                yield msg
        finally:
            _announcer.remove_listener(q)

    return Response(
        stream_with_context(generate()),
        mimetype="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/api/ingest/runs")
def ingest_runs():
    return jsonify({
        "runs": _run_history,
        "active_run": _active_run,
    })


@app.get("/api/registry")
def registry():
    search = request.args.get("search", "").strip()
    sort_col = request.args.get("sort", "last_ingested")
    order = request.args.get("order", "desc").lower()

    # Whitelist columns to prevent SQL injection
    _VALID_COLS = {"source_name", "origin_path", "chunk_count", "version_count", "last_ingested"}
    if sort_col not in _VALID_COLS:
        sort_col = "last_ingested"
    if order not in ("asc", "desc"):
        order = "desc"

    import tomllib as _tomllib
    registry_path = ".rag-registry.db"
    try:
        raw = _tomllib.loads(Path(_DEFAULT_CONFIG).read_text(encoding="utf-8"))
        registry_path = raw.get("pipeline", {}).get("registry_path", registry_path)
    except Exception:
        pass

    if not Path(registry_path).exists():
        return jsonify({"error": "registry_missing", "message": f"{registry_path} not found"}), 404

    conn = open_registry(registry_path)
    try:
        if search:
            rows = conn.execute(
                f"""SELECT source_name, origin_path, content_hash, chunk_count,
                           version_count, last_ingested
                    FROM documents
                    WHERE source_name LIKE ? OR origin_path LIKE ?
                    ORDER BY {sort_col} {order}""",
                (f"%{search}%", f"%{search}%"),
            ).fetchall()
        else:
            rows = conn.execute(
                f"""SELECT source_name, origin_path, content_hash, chunk_count,
                           version_count, last_ingested
                    FROM documents
                    ORDER BY {sort_col} {order}"""
            ).fetchall()

        records = [dict(row) for row in rows]
    finally:
        conn.close()

    return jsonify({"records": records, "total": len(records)})


@app.get("/api/config")
def get_config():
    if not Path(_DEFAULT_CONFIG).exists():
        return jsonify({"error": "config_missing", "message": f"{_DEFAULT_CONFIG} not found"}), 404
    try:
        cfg = load_config(_DEFAULT_CONFIG)
    except ConfigError as exc:
        return jsonify({"error": "config_invalid", "message": str(exc)}), 422

    sources = []
    for src in cfg.sources:
        if isinstance(src, LocalSourceConfig):
            sources.append({"name": src.name, "type": src.type, "path": src.path})
        else:
            sources.append({"name": src.name, "type": src.type})

    return jsonify({
        "embedding": {
            "provider": cfg.embedding.provider,
            "model": cfg.embedding.model,
            "api_base": cfg.embedding.api_base,
            "api_key_env": cfg.embedding.api_key_env,
        },
        "vector_store": {
            "provider": cfg.vector_store.provider,
            "path": cfg.vector_store.path,
            "collection": cfg.vector_store.collection,
        },
        "pipeline": {
            "chunk_size": cfg.pipeline.chunk_size,
            "chunk_overlap": cfg.pipeline.chunk_overlap,
            "supported_formats": cfg.pipeline.supported_formats,
            "registry_path": cfg.pipeline.registry_path,
            "log_path": cfg.pipeline.log_path,
            "max_file_size_mb": cfg.pipeline.max_file_size_mb,
        },
        "sources": sources,
    })


@app.put("/api/config")
def put_config():
    data = request.get_json(force=True)
    errors = []

    # Inline validation
    pipeline = data.get("pipeline", {})
    chunk_size = pipeline.get("chunk_size")
    chunk_overlap = pipeline.get("chunk_overlap")
    if chunk_size is not None and chunk_overlap is not None:
        try:
            if int(chunk_overlap) >= int(chunk_size):
                errors.append({
                    "field": "pipeline.chunk_overlap",
                    "message": "chunk_overlap must be less than chunk_size",
                })
        except (TypeError, ValueError):
            errors.append({"field": "pipeline.chunk_size", "message": "must be an integer"})

    embedding = data.get("embedding", {})
    if not embedding.get("api_key_env", "").strip():
        errors.append({"field": "embedding.api_key_env", "message": "must not be empty"})

    sources = data.get("sources", [])
    if not sources:
        errors.append({"field": "sources", "message": "at least one source is required"})

    if errors:
        return jsonify({"error": "validation_failed", "fields": errors}), 422

    # Build TOML dict
    toml_dict: dict = {}

    if "embedding" in data:
        toml_dict["embedding"] = data["embedding"]
    if "vector_store" in data:
        toml_dict["vector_store"] = data["vector_store"]
    if "pipeline" in data:
        toml_dict["pipeline"] = data["pipeline"]
    if "sources" in data:
        toml_dict["sources"] = data["sources"]

    try:
        with open(_DEFAULT_CONFIG, "wb") as f:
            f.write(tomli_w.dumps(toml_dict).encode())
    except OSError as exc:
        return jsonify({"error": "write_failed", "message": str(exc)}), 500

    return jsonify({"ok": True})


# ---------------------------------------------------------------------------
# Chat endpoints (Feature 003)
# ---------------------------------------------------------------------------

_MAX_CHAT_MESSAGE_LEN = 4000
_MAX_HISTORY_MESSAGES = 20  # 10 turns × 2 messages each


@app.get("/api/chat/preflight")
def chat_preflight():
    """Check whether the LLM API key is available.

    Returns:
        200 {"ok": true, "model": "<model>"} — key is set
        412 {"ok": false, "reason": "..."} — key not set or config missing
    """
    try:
        cfg = load_config(_DEFAULT_CONFIG)
    except ConfigError:
        return jsonify({"ok": False, "reason": "Configuration file invalid or missing"}), 412

    api_key = os.environ.get(cfg.llm.api_key_env)
    if not api_key:
        return jsonify({
            "ok": False,
            "reason": f"Environment variable {cfg.llm.api_key_env!r} is not set.",
        }), 412

    return jsonify({"ok": True, "model": cfg.llm.model})


@app.post("/api/chat")
def chat():
    """Conversational RAG endpoint. Streams SSE events."""
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    history = data.get("history", [])

    if not isinstance(message, str) or len(message) > _MAX_CHAT_MESSAGE_LEN:
        return jsonify({
            "error": "message_too_long",
            "message": f"Message exceeds {_MAX_CHAT_MESSAGE_LEN} character limit.",
        }), 400

    # Trim history server-side as a safety measure
    if len(history) > _MAX_HISTORY_MESSAGES:
        history = history[-_MAX_HISTORY_MESSAGES:]

    try:
        cfg = load_config(_DEFAULT_CONFIG)
    except ConfigError as exc:
        return jsonify({"error": "config_invalid", "message": str(exc)}), 422

    return Response(
        stream_with_context(_chat_stream(message, history, cfg)),
        content_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )


def _chat_stream(message: str, history: list, cfg):
    """Generator that yields SSE events for a conversational RAG exchange.

    SSE event types:
        text_delta   — streaming text token from Claude
        tool_start   — Claude is invoking a tool
        tool_result  — tool execution completed
        citations    — source documents retrieved (search only)
        error        — an error occurred
        done         — stream is complete (always emitted in finally)
    """
    api_key = os.environ.get(cfg.llm.api_key_env, "")

    def _sse(payload: dict) -> str:
        return f"data: {json.dumps(payload)}\n\n"

    try:
        client = anthropic.Anthropic(api_key=api_key)

        # Build Anthropic messages list
        messages = list(history) + [{"role": "user", "content": message}]

        # --- First stream pass ---
        with client.messages.stream(
            model=cfg.llm.model,
            max_tokens=4096,
            tools=TOOL_SCHEMAS,
            messages=messages,
        ) as stream:
            for text in stream.text_stream:
                yield _sse({"event": "text_delta", "text": text})

            final_msg = stream.get_final_message()

        # Tool use loop — may repeat for chained tool calls
        while final_msg.stop_reason == "tool_use":
            tool_use_blocks = [b for b in final_msg.content if b.type == "tool_use"]
            tool_results_for_api = []

            for tool_block in tool_use_blocks:
                yield _sse({"event": "tool_start", "name": tool_block.name, "id": tool_block.id})

                tool_input = tool_block.input or {}
                result_str = ""

                if tool_block.name == "search_knowledge_base":
                    query = tool_input.get("query", "")
                    n_results = tool_input.get("n_results", cfg.pipeline.top_k)
                    # Load ChromaDB for search
                    try:
                        chroma_client = chromadb.PersistentClient(path=cfg.vector_store.path)
                        collection = get_or_create_collection(
                            chroma_client, cfg.vector_store.collection, cfg.embedding.model
                        )
                        result_str, chunks = execute_search_knowledge_base(
                            query=query,
                            n_results=n_results,
                            embedding_cfg=cfg.embedding,
                            collection=collection,
                        )
                        if chunks:
                            sources = [
                                {"source_name": c.source_name, "origin_path": c.origin_path}
                                for c in chunks
                            ]
                            yield _sse({"event": "citations", "sources": sources})
                    except Exception as exc:
                        result_str = f"ERROR: Search failed: {exc}"

                elif tool_block.name == "ingest_documents":
                    path = tool_input.get("path", "")
                    try:
                        reg_conn = open_registry(cfg.pipeline.registry_path)
                        chroma_client = chromadb.PersistentClient(path=cfg.vector_store.path)
                        collection = get_or_create_collection(
                            chroma_client, cfg.vector_store.collection, cfg.embedding.model
                        )
                        logger = init_logger(cfg.pipeline.log_path)
                        result_str = execute_ingest_documents(
                            path=path,
                            cfg=cfg,
                            chroma_client=chroma_client,
                            collection=collection,
                            reg_conn=reg_conn,
                            run_lock=_run_lock,
                            logger=logger,
                        )
                        reg_conn.close()
                    except Exception as exc:
                        result_str = f"ERROR: Ingestion failed: {exc}"

                elif tool_block.name == "query_registry":
                    query = tool_input.get("query") or None
                    limit = int(tool_input.get("limit", 50))
                    try:
                        reg_conn = open_registry(cfg.pipeline.registry_path)
                        result_str = execute_query_registry(
                            query=query,
                            limit=limit,
                            reg_conn=reg_conn,
                        )
                        reg_conn.close()
                    except Exception as exc:
                        result_str = f"ERROR: Registry query failed: {exc}"

                else:
                    result_str = f"ERROR: Unknown tool {tool_block.name!r}"

                yield _sse({"event": "tool_result", "name": tool_block.name, "result": result_str})
                tool_results_for_api.append({
                    "type": "tool_result",
                    "tool_use_id": tool_block.id,
                    "content": result_str,
                })

            # Build messages for continuation stream
            assistant_content = [
                {"type": b.type, "id": b.id, "name": b.name, "input": b.input}
                for b in final_msg.content
            ]
            messages = messages + [
                {"role": "assistant", "content": assistant_content},
                {"role": "user", "content": tool_results_for_api},
            ]

            # Continuation stream
            with client.messages.stream(
                model=cfg.llm.model,
                max_tokens=4096,
                tools=TOOL_SCHEMAS,
                messages=messages,
            ) as stream:
                for text in stream.text_stream:
                    yield _sse({"event": "text_delta", "text": text})
                final_msg = stream.get_final_message()

    except Exception as exc:
        yield _sse({"event": "error", "message": str(exc)})

    finally:
        yield _sse({"event": "done"})


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7842, debug=False, threaded=True)
