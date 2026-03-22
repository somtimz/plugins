# Research: Ingestion Pipeline Web UI

**Feature**: 002-ingestion-web-ui
**Date**: 2026-03-16
**Phase**: 0 — Unknowns resolved before design

---

## Decision 1: Real-time Progress Delivery (SSE Framework)

**Decision**: Flask with Server-Sent Events (SSE) using a `queue.Queue`-based announcer pattern
**Rationale**: SSE is the spec-mandated transport (FR-002). Flask's `Response(stream_with_context(generate()), mimetype='text/event-stream')` requires no additional libraries beyond Flask itself. A `MessageAnnouncer` class holds a list of `queue.Queue` objects — one per connected client — and pushes formatted event strings to each. This pattern is thread-safe on all platforms and handles multiple concurrent browser tabs cleanly. No WebSocket, async, or pub-sub library is required.
**Alternatives considered**:
- WebSockets (flask-sock, socket.io): More complex, bidirectional protocol not needed for one-way progress stream; adds a runtime dependency
- Polling: Wastes bandwidth; spec says "without requiring a page reload" (FR-002), which SSE satisfies more cleanly
- asyncio (Quart, FastAPI): Async adds complexity with no UX benefit for a single-user local tool; the pipeline is inherently synchronous

**Key implementation pattern**:
```python
class MessageAnnouncer:
    def __init__(self):
        self.listeners: list[queue.Queue] = []

    def listen(self) -> queue.Queue:
        q = queue.Queue(maxsize=100)
        self.listeners.append(q)
        return q

    def announce(self, msg: str):
        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]

# SSE endpoint
@app.get("/api/ingest/stream")
def stream():
    q = announcer.listen()
    def generate():
        while True:
            msg = q.get()
            yield msg
    return Response(stream_with_context(generate()), mimetype="text/event-stream")
```

Event format follows the SSE spec: `data: <json>\n\n`

**Browser client note**: `EventSource` auto-reconnects on drop; for intentional close (run complete), the client must call `source.close()` manually and create a new instance for the next run.

---

## Decision 2: Pipeline Integration Approach

**Decision**: Approach A — direct import. Extract `_process_file_list()` and supporting logic into a new public module `scripts/lib/pipeline.py` with a `progress_callback` parameter. Flask calls `run_ingestion()` directly.
**Rationale**: The spec requires per-document real-time progress (FR-002, FR-003). This is only achievable via a callback/queue injected into the processing loop — subprocess stdout parsing cannot provide per-document granularity without redesigning the CLI output format. Direct import also preserves the atomic vector-store + registry transaction guarantees already implemented, reuses `SourceResult` as the structured return type (no stdout parsing), and avoids subprocess overhead (process spawn + Python import = 100-500ms per request).
**Alternatives considered**:
- Subprocess (run `ingest.py` and parse stdout): Fragile — tied to exact `_print_full_summary()` format; no per-document progress; no structured failure details; process cleanup on request cancellation is error-prone
- Subprocess + log tailing (read `.rag-pipeline.log` for progress): Racy (file I/O buffering), complex, still no structured data

**Refactoring scope**: Minimal. The existing `_process_file_list()` function (≈110 lines) is moved to `lib/pipeline.py` and gains an optional `progress_callback: Callable[[str, str, str, str | None], None]` parameter called once per document with `(file_path, source_name, status, reason)`. The existing `ingest.py` CLI is updated to call `lib.pipeline.run_ingestion()` — no user-visible change.

**Threading model**: Flask handles the HTTP request in one thread; a background `threading.Thread` runs `run_ingestion()` and pushes SSE events via `announcer.announce()`. The Flask `/api/ingest/run` endpoint starts the thread and returns `202 Accepted` immediately. The `/api/ingest/stream` SSE endpoint provides the event stream. A module-level `_run_lock` (threading.Lock) prevents concurrent runs (FR-005).

**SourceResult** (already implemented in `ingest.py`, move to `lib/pipeline.py`):
```python
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
    status: str = "ok"
    error_message: str | None = None
```

---

## Decision 3: Frontend Technology

**Decision**: Single HTML file served by Flask with vanilla JavaScript (no framework, no build step)
**Rationale**: The UI is a local developer tool accessed by a single user. A single `templates/index.html` with inline or static CSS/JS avoids a Node.js build pipeline, keeps the install footprint minimal (Flask only), and ships the entire UI as part of the Python package. The interactive requirements (SSE event listener, table sort/filter, form validation) are well within vanilla JS capability.
**Alternatives considered**:
- React/Vue SPA: Requires Node.js build pipeline, adds complexity for a single-user local tool
- HTMX: Interesting fit for SSE-driven UIs, but adds a CDN dependency and learning curve with no UX benefit over vanilla JS

---

## Decision 4: Configuration Edit/Save

**Decision**: Flask reads and writes `.rag-plugin.toml` directly. Validation runs in Python before writing (re-uses the `load_config()` validation logic). Config is re-loaded on each ingestion run — no server restart required (SC-004).
**Rationale**: The config is already a structured TOML file with a validated schema in `lib/config.py`. Python's `tomllib` (stdlib, read-only) + `tomli_w` (or manual TOML serialization) handles the round-trip. Re-running `load_config()` on the submitted payload validates before writing (FR-010 inline validation).
**Alternatives considered**:
- Restart-required reload: Rejected by SC-004 ("without restarting the server")
- In-memory config mutation: Fragile — changes lost on server restart

---

## Decision 5: Run History Storage

**Decision**: In-memory list capped at 5 entries (module-level list in `ui.py`). Each entry is a serializable dict derived from `SourceResult` objects plus start/end timestamps.
**Rationale**: The spec explicitly scopes history to "current server session" and "last 5 runs" (FR-014). Persistence across restarts is out of scope (Assumptions). An in-memory list is the minimum viable approach with no dependencies.
**Alternatives considered**:
- SQLite run history table: Correct for persistence, but persistence is out of scope for v1
- File-based JSON log: Same issue — out of scope, adds I/O complexity

---

## Resolved Unknowns Summary

| Unknown | Resolution |
|---------|-----------|
| Real-time delivery mechanism | SSE via Flask queue-based announcer |
| Pipeline integration approach | Direct import, `lib/pipeline.py` extraction |
| Frontend framework | Vanilla JS single HTML file |
| Config edit persistence | Re-load `load_config()` on each run; write TOML via `tomli_w` |
| Run history storage | In-memory list, max 5 entries |
| Port | Fixed 7842 (from spec FR-012) |
| Missing config behavior | Error banner + "Create config" button (from spec FR-011) |
| Pre-flight API key check | Check env var before starting run (from spec FR-001) |
