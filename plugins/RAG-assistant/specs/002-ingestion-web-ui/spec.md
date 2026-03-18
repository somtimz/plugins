# Feature Specification: Ingestion Pipeline Web UI

**Feature Branch**: `002-ingestion-web-ui`
**Created**: 2026-03-15
**Status**: Implemented
**Input**: User description: "Build a web UI for the ingestion pipeline"

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Trigger Ingestion from the Browser (Priority: P1)

A user opens a web page, sees their configured sources, and clicks a button to start ingestion. The page shows live progress as each document is discovered, processed, and embedded. When complete, a summary shows how many documents succeeded, were skipped, or failed.

**Why this priority**: Replacing the command-line requirement is the core value of the UI. Everything else depends on this working first.

**Independent Test**: With `.rag-plugin.toml` configured and documents in a source folder, open the UI, click "Run Ingestion", and verify progress updates in real time and the final summary matches the CLI output.

**Acceptance Scenarios**:

1. **Given** a valid config and at least one source, **When** the user clicks "Run Ingestion", **Then** a progress view appears showing per-source status updating in real time.
2. **Given** ingestion is running, **When** a document is processed, **Then** the document name, status (succeeded / skipped / failed), and reason appear in the progress list.
3. **Given** ingestion completes, **When** the final document is processed, **Then** a summary panel shows total discovered, succeeded, skipped, and failed counts.
4. **Given** ingestion is running, **When** a second user tries to start another run, **Then** the start button is disabled and a "run in progress" message is shown.

---

### User Story 2 — View the Document Registry (Priority: P2)

A user opens a registry view and sees a table of all previously ingested documents: source name, file path, chunk count, version count, and last ingested date. They can search and sort the list.

**Why this priority**: The registry is the primary way to confirm what is in the vector store. High value, low risk once the backend is in place.

**Independent Test**: After running at least one ingestion, open the registry tab and verify every ingested document appears as a row with correct metadata.

**Acceptance Scenarios**:

1. **Given** documents have been ingested, **When** the user opens the registry view, **Then** a table lists each document with source name, path, chunk count, version count, and last ingested timestamp.
2. **Given** the registry table is visible, **When** the user types in the search box, **Then** rows are filtered in real time to show only matching documents.
3. **Given** the registry table is visible, **When** the user clicks a column header, **Then** rows sort by that column.

---

### User Story 3 — View and Edit Configuration (Priority: P3)

A user opens a configuration view that displays the current `.rag-plugin.toml` settings in a readable form. They can see which sources are configured, what embedding model is in use, and what pipeline defaults are active — and optionally edit and save changes.

**Why this priority**: Read-only config visibility reduces friction for first-time users. In-place editing avoids the need to open a file.

**Independent Test**: With `.rag-plugin.toml` present, open the config view, verify all sections display correctly, change a source path, save, and confirm the next ingestion run uses the updated path.

**Acceptance Scenarios**:

1. **Given** `.rag-plugin.toml` exists, **When** the user opens the config view, **Then** all sections (embedding, vector store, pipeline, sources) are displayed with current values.
2. **Given** the config view is open, **When** the user changes a source path and saves, **Then** the config file is updated and the next ingestion uses the new path.
3. **Given** the user enters an invalid value (e.g., `chunk_overlap >= chunk_size`), **When** they attempt to save, **Then** a validation error is shown and the file is not written.

---

### Edge Cases

- If `.rag-plugin.toml` is missing on initial page load, a top-level dismissible error banner is shown immediately (before any tab is clicked) with a "Create config" button that switches to the Config tab pre-filled with default values. The check runs once on `DOMContentLoaded`. If it exists but is invalid, a validation error describing the failure is shown.
- If a second ingestion run is triggered while one is already in progress, the "Run Ingestion" button is disabled and a "run in progress" message is shown. The API returns `409 Conflict`. (Covered by FR-005, US1 acceptance scenario 4.)
- If the vector store (`.rag-store/`) or registry (`.rag-registry.db`) is deleted while the server is running, the next ingestion run will recreate them automatically (ChromaDB + registry auto-create on open). Detecting and surfacing a mid-session deletion in the UI is out of scope for v1.
- How does the UI handle a large registry (hundreds or thousands of documents)?
- If the embedding API key env var is not set when ingestion is triggered, a pre-flight check blocks the run and immediately shows an actionable error message before any processing begins.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The UI MUST allow users to trigger a full ingestion run for all configured sources with a single action. Before starting, the UI MUST perform a pre-flight check and block the run with a clear error if the embedding API key env var is not set.
- **FR-002**: The UI MUST display real-time ingestion progress via Server-Sent Events (SSE), updating as each document is processed without requiring a page reload.
- **FR-003**: The UI MUST show per-document status (succeeded, skipped, failed) and reason during and after a run.
- **FR-004**: The UI MUST show an aggregate summary (discovered, succeeded, skipped, failed) when ingestion completes.
- **FR-005**: The UI MUST prevent a second ingestion run from starting while one is already in progress.
- **FR-014**: The UI MUST display the last 5 ingestion runs in a scrollable history list for the current server session. Runs older than the 5 most recent are discarded from memory.
- **FR-006**: The UI MUST display a registry table listing all ingested documents with source name, file path, chunk count, version count, and last ingested timestamp.
- **FR-007**: The registry table MUST support real-time text search filtering.
- **FR-008**: The registry table MUST support sorting by any column.
- **FR-009**: The UI MUST display the current configuration in a readable structured form.
- **FR-010**: The UI MUST allow users to edit and save configuration values with server-side inline validation before writing to disk. The `PUT /api/config` endpoint returns `422` with a `fields` array on validation failure; the frontend renders per-field error messages from this response. No client-side pre-validation is required in v1.
- **FR-011**: When `.rag-plugin.toml` is missing on load, the UI MUST show an error banner with a "Create config" button that opens a pre-filled config editor. When the config exists but is invalid, the UI MUST show a clear error describing the validation failure.
- **FR-012**: The UI MUST be accessible at `http://localhost:7842` after running `python scripts/ui.py`. The port is fixed at 7842 and is not configurable in v1.
- **FR-013**: The UI server MUST be started via a dedicated top-level command (`python scripts/ui.py`) that is separate from the ingestion script.

### Key Entities

- **IngestionRun**: A single pipeline execution — start time, end time, status, and a list of SourceResults.
- **SourceResult**: Per-source outcome within a run — source name, path, discovered/succeeded/skipped/failed counts, and per-document entries.
- **DocumentEntry**: Per-document status — file path, status (succeeded/skipped/failed), and failure reason if applicable.
- **RegistryRecord**: A document registry row — source name, origin path, content hash, chunk count, version count, last ingested timestamp.
- **PipelineConfig**: The full parsed contents of `.rag-plugin.toml`.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user with no command-line experience can trigger a full ingestion run and read the results within 2 minutes of opening the UI.
- **SC-002**: Progress updates appear on screen within 1 second of each document being processed. *Verification*: In `test_ui_integration.py`, assert elapsed time between `progress_callback` call and SSE `document_processed` event receipt is < 1.0s using mock timestamps.
- **SC-003**: The registry view loads and renders up to 1,000 documents in under 2 seconds on a local developer machine. *Verification*: In `test_ui_api.py`, seed registry with 1,000 rows, assert `GET /api/registry` responds in < 2s. Virtualization/pagination deferred to v2 (>1,000 rows is out of scope).
- **SC-004**: Configuration changes are saved and take effect on the next ingestion run without restarting the server.
- **SC-005**: The UI correctly reflects ingestion state after a page reload — no phantom "running" status when the server is idle. *Verification*: In `test_ui_api.py`, assert `GET /api/ingest/runs` returns `{"active_run": null}` after a run completes (i.e., `_active_run` is cleared in `_run_pipeline`).

## Clarifications

### Session 2026-03-16

- Q: How should real-time ingestion progress be delivered to the browser? → A: Server-Sent Events (SSE) — server pushes progress events over a persistent HTTP connection.
- Q: What should the UI show when `.rag-plugin.toml` is missing on load? → A: Show an error banner with a "Create config" button that opens a pre-filled config editor.
- Q: What port should the UI server listen on? → A: Fixed default port 7842, not configurable in v1.
- Q: How many past ingestion runs should the UI display during a session? → A: The last 5 runs, shown in a scrollable history list.
- Q: What happens when the embedding API key env var is not set when the user triggers ingestion? → A: Pre-flight check blocks the run and shows an immediate error before any processing starts.

## Assumptions

- The web UI is served by a local process, not deployed to a remote server.
- A single user accesses the UI at a time; multi-user access and authentication are out of scope for v1.
- The UI reads and writes `.rag-plugin.toml` in the current working directory; multi-config support is out of scope.
- The embedding API key is set as an environment variable in the server process's environment before launch.
- Run history is retained in memory for the current server session; the UI displays the last 5 runs in a scrollable list. Persistence of run history across server restarts is out of scope for v1.
- If the vector store (`.rag-store/`) or registry (`.rag-registry.db`) is deleted while the server is running, the next ingestion run will recreate them automatically. Detecting and surfacing a mid-session deletion in the UI is out of scope for v1.
