# Tasks: Ingestion Pipeline Web UI

**Input**: Design documents from `/specs/002-ingestion-web-ui/`
**Prerequisites**: plan.md ✓, spec.md ✓, research.md ✓, data-model.md ✓, contracts/api.md ✓, quickstart.md ✓
**Branch**: `002-ingestion-web-ui`

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Exact file paths included in all descriptions

---

## Phase 1: Setup

**Purpose**: Install new dependencies and create directory scaffolding

- [X] T001 Install `flask` and `tomli-w` into `.venv` and document in `README.md` install section
- [X] T002 Create `scripts/templates/` directory (will hold `index.html`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Extract `lib/pipeline.py` public API and scaffold `ui.py` — blocks all three user stories

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 Create `scripts/lib/pipeline.py` — move `SourceResult` dataclass from `scripts/ingest.py`; add `IngestionEvent` dataclass with fields `(file_path: str, source_name: str, event_type: str, status: str | None, reason: str | None)`; define `ProgressCallback = Callable[[IngestionEvent], None]` type alias
- [X] T004 Implement `run_ingestion(sources, cfg, logger, progress_callback=None) -> list[SourceResult]` in `scripts/lib/pipeline.py` — extract the source-iteration loop and `_process_file_list` logic from `scripts/ingest.py`; call `progress_callback` (wrapped in try/except) at each document outcome: `succeeded`, `skipped_unchanged`, `skipped_duplicate`, `failed`
- [X] T005 Update `scripts/ingest.py` to import `SourceResult` and call `lib.pipeline.run_ingestion()` instead of the inline loop — no user-visible CLI behavior change; all 126 existing tests must still pass
- [X] T006 [P] Write `tests/unit/test_pipeline.py` — test `run_ingestion()` with a mock progress_callback: verify callback is called once per document with correct `event_type` and `file_path`; verify callback exceptions do not abort the run; verify `SourceResult` counts match callback events
- [X] T007 Create `scripts/ui.py` scaffold — Flask app instance; `MessageAnnouncer` class with `listen() -> queue.Queue` and `announce(msg: str)`; module-level state: `_announcer`, `_run_lock: threading.Lock`, `_active_run: dict | None`, `_run_history: list[dict]` (max 5); `GET /` route serving `scripts/templates/index.html`; `if __name__ == "__main__": app.run(host="0.0.0.0", port=7842)` entry point; `sys.path.insert` so `lib.*` imports work

**Checkpoint**: `python scripts/ui.py` starts on port 7842; all existing 126 tests still pass

---

## Phase 3: User Story 1 — Trigger Ingestion (Priority: P1) 🎯 MVP

**Goal**: User can click "Run Ingestion" in the browser, see per-document progress in real time via SSE, and view an aggregate summary when the run completes. Concurrent runs are blocked.

**Independent Test**: With `.rag-plugin.toml` configured and `RAG_EMBEDDING_API_KEY` set, open `http://localhost:7842`, click "Run Ingestion", verify progress events appear and summary shows correct counts. Open a second browser tab during an active run, click "Run Ingestion" — verify button is disabled and "run in progress" message appears.

### Tests for User Story 1

- [X] T008 [P] [US1] Write `tests/unit/test_ui_api.py` — Flask test client tests for `POST /api/ingest/run`: assert `202` when idle; assert `409` when `_active_run` is set; assert `412` when embedding API key env var is unset; assert `422` when `.rag-plugin.toml` is missing or invalid
- [X] T009 [P] [US1] Add tests to `tests/unit/test_ui_api.py` for `GET /api/ingest/runs`: assert response shape includes `runs` list and `active_run` field; assert history is capped at 5 entries when a 6th run completes

### Implementation for User Story 1

- [X] T010 [US1] Implement `POST /api/ingest/run` in `scripts/ui.py` — preflight check: load config (return `422` on missing/invalid), check `os.environ.get(cfg.embedding.api_key_env)` (return `412` if unset); acquire `_run_lock` non-blocking (return `409` if locked); start `threading.Thread(target=_run_pipeline, args=(run_id,), daemon=True)`; set `_active_run`; return `202 {"run_id": run_id}`
- [X] T011 [US1] Implement `_run_pipeline(run_id)` background function in `scripts/ui.py` — loads config and logger; defines `progress_callback` that calls `_announcer.announce(format_sse(event_dict))`; calls `lib.pipeline.run_ingestion()`; on completion builds `RunSummary`; appends to `_run_history` (trim to 5); clears `_active_run`; releases `_run_lock`; announces `run_complete` or `run_error` SSE event
- [X] T012 [US1] Implement `GET /api/ingest/stream` SSE endpoint in `scripts/ui.py` — calls `_announcer.listen()`; returns `Response(stream_with_context(generate()), mimetype="text/event-stream", headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})`; `generate()` blocks on `q.get()` and yields each message
- [X] T013 [US1] Implement `GET /api/ingest/runs` endpoint in `scripts/ui.py` — returns `{"runs": _run_history, "active_run": _active_run}`
- [X] T014 [US1] Create `scripts/templates/index.html` — base layout with three-tab navigation (Ingestion / Registry / Config); tab switching via vanilla JS; responsive CSS; no external dependencies beyond CDN-free inline styles
- [X] T015 [US1] Implement ingestion tab in `scripts/templates/index.html` — "Run Ingestion" button (`POST /api/ingest/run`); `EventSource("/api/ingest/stream")` on click; per-document progress list updating on `document_processed` events (file path, status badge: succeeded/skipped/failed, reason); aggregate summary panel appearing on `run_complete` (total discovered/succeeded/skipped/failed); button disabled with "run in progress" message while active; scrollable run history list showing last 5 runs from `GET /api/ingest/runs` on page load

**Checkpoint**: User Story 1 fully functional — trigger ingestion, see live progress, view summary, concurrent run blocked

---

## Phase 4: User Story 2 — View Document Registry (Priority: P2)

**Goal**: User can open the Registry tab and see a table of all ingested documents with source name, file path, chunk count, version count, and last ingested date. They can filter rows by typing in a search box and sort by any column.

**Independent Test**: After at least one successful ingestion, open the Registry tab — verify every ingested document appears as a row. Type a partial filename in the search box — verify only matching rows remain. Click "Chunk Count" column header — verify rows sort numerically; click again to reverse order.

### Tests for User Story 2

- [X] T016 [P] [US2] Add tests to `tests/unit/test_ui_api.py` for `GET /api/registry`: assert response shape `{"records": [...], "total": N}`; assert `search` param filters `source_name` and `origin_path` case-insensitively; assert `sort` and `order` params change row order; assert `404` response when `.rag-registry.db` is missing

### Implementation for User Story 2

- [X] T017 [US2] Implement `GET /api/registry` endpoint in `scripts/ui.py` — open registry with `lib.registry.open_registry(cfg.pipeline.registry_path)`; build SQL `SELECT` with optional `WHERE origin_path LIKE ? OR source_name LIKE ?` for `search` param; `ORDER BY <col> <ASC|DESC>` for `sort`/`order` params (whitelist valid column names); return `{"records": [...], "total": N}`; return `404` if registry file does not exist
- [X] T018 [US2] Implement registry tab in `scripts/templates/index.html` — fetch `GET /api/registry` on tab activation; render table with columns: Source, File Path, Chunks, Versions, Last Ingested; search `<input>` that re-fetches `GET /api/registry?search=<value>` on `input` event (debounced 200ms); column header `<th>` click toggles sort direction and re-fetches with `sort=<col>&order=<asc|desc>`; show row count; handle registry-missing `404` with informational message

**Checkpoint**: User Stories 1 AND 2 both work independently

---

## Phase 5: User Story 3 — View and Edit Configuration (Priority: P3)

**Goal**: User can open the Config tab and see all current `.rag-plugin.toml` settings in a readable form. They can edit values and save; inline validation blocks writes for invalid values (e.g., `chunk_overlap >= chunk_size`). A missing config shows an error banner with a "Create config" button.

**Independent Test**: With `.rag-plugin.toml` present, open Config tab — verify all sections render with current values. Change `chunk_size` to 500, save — verify `.rag-plugin.toml` is updated on disk. Set `chunk_overlap` equal to `chunk_size`, save — verify error shown, file unchanged. Delete `.rag-plugin.toml`, reload page — verify error banner with "Create config" button appears.

### Tests for User Story 3

- [X] T019 [P] [US3] Add tests to `tests/unit/test_ui_api.py` for `GET /api/config`: assert `200` response with correct shape; assert `404` when config missing; assert `422` when config invalid. Add tests for `PUT /api/config`: assert `200` and disk write on valid payload; assert `422` with `fields` array when `chunk_overlap >= chunk_size`; assert file is NOT written on validation failure

### Implementation for User Story 3

- [X] T020 [US3] Implement `GET /api/config` endpoint in `scripts/ui.py` — attempt `lib.config.load_config(config_path)`; on `FileNotFoundError` return `{"error": "config_missing", "message": "..."}` with `404`; on `ConfigError` return `{"error": "config_invalid", "message": str(e)}` with `422`; on success serialize config dataclasses to dict and return `200`
- [X] T021 [US3] Implement `PUT /api/config` endpoint in `scripts/ui.py` — deserialize request JSON; run inline validation (check `chunk_overlap < chunk_size`, required string fields non-empty, at least one source); on failure return `422 {"error": "validation_failed", "fields": [...]}` without writing; on pass serialize to TOML using `tomli_w.dumps()` and write to `.rag-plugin.toml`; return `200 {"ok": true}`
- [X] T022 [US3] Implement config tab in `scripts/templates/index.html` — fetch `GET /api/config` on tab activation; render sections (Embedding, Vector Store, Pipeline, Sources) as labeled form fields with current values; "Save" button submits `PUT /api/config` with form data as JSON; show per-field inline validation errors from `422` response `fields` array; show success toast on `200`; do NOT expose API key value — display only `api_key_env` name

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Edge-case handling, integration tests, documentation

- [X] T023 Implement missing config error banner in `scripts/templates/index.html` — on page load, `GET /api/config`; if `404` show a top-level dismissible error banner: "Configuration file not found — [Create config]"; "Create config" button opens the Config tab pre-filled with default values from the TOML example; if `422` show banner: "Configuration file is invalid: <message>"
- [X] T024 [P] Write `tests/integration/test_ui_integration.py` — end-to-end tests using Flask test client: mock `lib.pipeline.run_ingestion` to emit synthetic progress events; `POST /api/ingest/run`, consume SSE stream, assert `run_started` and `run_complete` events received with correct fields; assert second `POST /api/ingest/run` while first is running returns `409`; assert `_run_history` has correct entry after completion; use `tmp_path` for registry and config files
- [X] T025 Update `README.md` with web UI section — add "Starting the Web UI" subsection under Usage: `export RAG_EMBEDDING_API_KEY=...`, `.venv/bin/pip install flask tomli-w`, `.venv/bin/python scripts/ui.py`, open `http://localhost:7842`

---

## Dependencies

```
Phase 1 (Setup)
    └── Phase 2 (Foundational: pipeline refactor + ui.py scaffold)
            ├── Phase 3 (US1: Ingestion trigger + SSE)
            │       └── Phase 4 (US2: Registry view) ← depends on working server
            │               └── Phase 5 (US3: Config view/edit) ← depends on working server
            └── Phase 6 (Polish) ← depends on all stories complete
```

US2 and US3 each only need the Phase 2 scaffold (Flask app + config loading) to be in place — they do not depend on US1 being complete. A single developer can work US2 and US3 in parallel with US1 once Phase 2 is done.

---

## Parallel Execution Examples

### Phase 2 — Tests and scaffold can run in parallel once T003-T005 are done

```
Task T006: tests/unit/test_pipeline.py
Task T007: scripts/ui.py scaffold
(different files, no dependencies between them)
```

### Phase 3 (US1) — Tests can run in parallel before implementation

```
Task T008: test_ui_api.py POST /api/ingest/run tests
Task T009: test_ui_api.py GET /api/ingest/runs tests
(different test blocks, same file — run sequentially to avoid conflicts)
```

### After Phase 2 — Stories can proceed in parallel

```
Developer A: Phase 3 (US1) — T008–T015
Developer B: Phase 4 (US2) — T016–T018 (only needs T007 Flask scaffold)
Developer C: Phase 5 (US3) — T019–T022 (only needs T007 Flask scaffold)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T002)
2. Complete Phase 2: Foundational (T003–T007) — **CRITICAL blocker**
3. Complete Phase 3: User Story 1 (T008–T015)
4. **STOP and VALIDATE**: Open `http://localhost:7842`, trigger ingestion, verify SSE events and summary
5. Demo-ready at this point

### Incremental Delivery

1. Setup + Foundational → server boots, pipeline lib in place
2. US1 → ingestion trigger + live progress (MVP)
3. US2 → registry browsing
4. US3 → config editing
5. Polish → edge cases + integration tests + README

---

## Notes

- All tasks modify files in `scripts/` (PEP 8 snake_case filenames) or `tests/` — no kebab-case conflicts
- The `[P]` marker on test tasks (T006, T008, T009, T016, T019, T024) means they can be written in parallel with other [P] tasks; they are test-first but the suite is not gated before implementation starts
- `scripts/ingest.py` changes in T005 must not alter CLI behavior — run `pytest tests/` after T005 to confirm
- Never expose the API key value in any endpoint — only `api_key_env` (the env var name) is serialized
- `tomli_w` (with underscore) is the correct package name for `pip install tomli-w`
