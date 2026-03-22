# Implementation Plan: Ingestion Pipeline Web UI

**Branch**: `002-ingestion-web-ui` | **Date**: 2026-03-16 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/002-ingestion-web-ui/spec.md`

## Summary

Build a local Flask web UI at port 7842 that wraps the existing RAG ingestion pipeline. The UI exposes three views — ingestion control with real-time SSE progress, document registry browsing, and config editing — backed by a thin JSON API. The pipeline is integrated via direct import (extracting `lib/pipeline.py`) rather than subprocess, enabling per-document progress streaming and preserving atomic transaction guarantees.

## Technical Context

**Language/Version**: Python 3.11+ (Flask server, pipeline lib); HTML/CSS/JS vanilla (single-file frontend)
**Primary Dependencies**: `flask` (web server + SSE), `tomli-w` (TOML write); existing: `openai`, `chromadb`, `pypdf`, `python-docx`, `sqlite3` (stdlib)
**Storage**: `.rag-plugin.toml` (config read/write), `.rag-registry.db` (SQLite, read-only from UI), `.rag-store/` (ChromaDB, pipeline-managed)
**Testing**: pytest (unit + integration); manual browser smoke test per acceptance scenario
**Target Platform**: Linux/macOS/Windows WSL, local developer machine
**Project Type**: Local web service + library refactor
**Performance Goals**: SSE events within 1 second of document processing (SC-002); registry renders 1,000 rows without visible lag (SC-003)
**Constraints**: Single user; port fixed at 7842; run history in-memory only (session scope); no auth
**Scale/Scope**: Single-user local tool; registry up to ~1,000 documents in v1

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Standard Directory Layout | ✅ PASS | New files: `scripts/ui.py` (PEP 8 snake_case ✓), `scripts/lib/pipeline.py` (PEP 8 ✓), `scripts/templates/index.html` (kebab-case N/A — HTML). No plugin manifest changes. |
| II. Skill-First Design | ✅ PASS | No new skills needed; this is a new script-based component, not a skill. |
| III. Test-First Development | ✅ PASS | Unit tests for `lib/pipeline.py` written before implementation; Flask endpoints covered by pytest; manual browser smoke test per spec acceptance scenario. |
| IV. Portability & Platform Parity | ✅ PASS | Flask + threading runs identically on Linux/macOS/WSL. No hardcoded paths; config path read from CWD. |
| V. Simplicity | ✅ PASS | Vanilla JS single-file frontend — no build pipeline. Only 2 new pip dependencies (`flask`, `tomli-w`). No abstractions until reuse case exists. |

**Post-design re-check**: All gates pass. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/002-ingestion-web-ui/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── api.md           # Phase 1 output
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
scripts/
├── ingest.py                  # Existing CLI — refactored to call lib.pipeline
├── ui.py                      # New: Flask web server entry point
├── lib/
│   ├── pipeline.py            # New: run_ingestion() public API (extracted from ingest.py)
│   ├── config.py              # Existing — no changes needed
│   ├── logger.py              # Existing — no changes needed
│   ├── reader.py              # Existing — no changes needed
│   ├── chunker.py             # Existing — no changes needed
│   ├── embedder.py            # Existing — no changes needed
│   ├── store.py               # Existing — no changes needed
│   ├── sources.py             # Existing — no changes needed
│   └── registry.py            # Existing — no changes needed
└── templates/
    └── index.html             # New: single-page UI (HTML + CSS + JS)

tests/
├── unit/
│   ├── test_pipeline.py       # New: unit tests for lib/pipeline.py
│   └── test_ui_api.py         # New: unit tests for Flask API endpoints
└── integration/
    └── test_ui_integration.py # New: end-to-end integration tests
```

**Structure Decision**: Single-project layout (scripts/ + tests/). No backend/frontend split — the single-file HTML template is served directly by Flask from `scripts/templates/`. This avoids any Node.js build pipeline while satisfying all UI requirements for a single-user local tool.

## Phase 0 Research Findings

See [research.md](research.md) for full details. Key decisions:

- **SSE transport**: Flask `Response(stream_with_context(generate()), mimetype="text/event-stream")` with a `MessageAnnouncer` using `queue.Queue` per listener. No additional library.
- **Pipeline integration**: Approach A — direct import. Extract `SourceResult` + `_process_file_list()` into `lib/pipeline.py` with `progress_callback` parameter. Background `threading.Thread` + `_run_lock` for concurrency control.
- **Frontend**: Vanilla JS single `index.html` served by Flask from `scripts/templates/`.
- **Config persistence**: `tomli_w` for TOML serialization; `load_config()` re-invoked on each ingestion run for SC-004.
- **Run history**: In-memory list, max 5 entries, module-level in `ui.py`.

## Phase 1 Design Artifacts

- [data-model.md](data-model.md) — entity definitions, SSE event envelope, in-memory state
- [contracts/api.md](contracts/api.md) — full HTTP API contract (6 endpoints)
- [quickstart.md](quickstart.md) — developer setup, architecture summary, smoke test steps

## Implementation Sequence

### Stage 1: Refactor pipeline into reusable lib

1. Create `scripts/lib/pipeline.py`:
   - Move `SourceResult` dataclass from `ingest.py`
   - Move `_process_file_list()` as `process_source()`, add `progress_callback` param
   - Export `run_ingestion(sources, cfg, logger, progress_callback=None) -> list[SourceResult]`
2. Update `scripts/ingest.py` to import from `lib.pipeline` — no user-visible change
3. Write `tests/unit/test_pipeline.py` — unit tests for `run_ingestion()` with mock callback

### Stage 2: Flask API server

4. Create `scripts/ui.py`:
   - `MessageAnnouncer` class
   - `_run_lock`, `_active_run`, `_run_history` module-level state
   - Implement all 6 API endpoints (see contracts/api.md)
   - Flask app factory, `if __name__ == "__main__"` runner on port 7842
5. Write `tests/unit/test_ui_api.py` — Flask test client covering all endpoints

### Stage 3: Frontend

6. Create `scripts/templates/index.html`:
   - Three-tab layout: Ingestion, Registry, Configuration
   - SSE `EventSource` connection to `/api/ingest/stream`
   - Registry table with search (input event) and sort (column header click)
   - Config form with inline validation feedback
7. Manual smoke test against all acceptance scenarios

### Stage 4: Integration tests

8. Write `tests/integration/test_ui_integration.py`:
   - End-to-end: start Flask test client, mock embedder, trigger run, verify SSE events
   - Concurrent run rejection test
   - Config save + validation test

## Complexity Tracking

No violations to document. All constitution gates pass.
