# Tasks: Document Ingestion Pipeline Skill

**Input**: Design documents from `/specs/001-doc-ingestion-pipeline/`
**Prerequisites**: plan.md ✅ spec.md ✅ research.md ✅ data-model.md ✅ contracts/ ✅ quickstart.md ✅

**Tests**: Included per Constitution Principle III (Test-First Development — NON-NEGOTIABLE).
Tests are written before the implementation they cover within each phase.

**Organization**: Tasks are grouped by user story to enable independent implementation
and testing. Constitution Principle III requires tests before implementation within each phase.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no shared state dependencies)
- **[Story]**: User story label — US1, US2, US3 (as defined in spec.md)
- Exact file paths are required in every task description

## Path Conventions

Plugin root: repository root (`/`)

```
skills/doc-ingestion-pipeline/SKILL.md
scripts/ingest.py
scripts/lib/config.py | sources.py | reader.py | chunker.py | embedder.py | store.py | registry.py | logger.py
tests/unit/test_config.py | test_sources.py | test_reader.py | test_chunker.py | test_embedder.py | test_store.py | test_registry.py | test_logger.py
tests/integration/test_pipeline.py
```

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the plugin directory skeleton, dependency manifest, and the SKILL.md
that enables auto-activation. No business logic yet.

- [X] T001 Create plugin directory structure: `skills/doc-ingestion-pipeline/`, `scripts/lib/`, `tests/unit/`, `tests/integration/` (all empty `__init__.py` files where needed)
- [X] T002 Create `requirements.txt` at project root listing all runtime dependencies: `openai`, `chromadb`, `pypdf`, `python-docx`, `Office365-REST-Python-Client`; and dev dependencies: `pytest`, `pytest-cov`
- [X] T003 [P] Create `skills/doc-ingestion-pipeline/SKILL.md` with YAML frontmatter (`name`, `description`, `version: 1.0.0`); description MUST include auto-activation keywords: ingest, embed, SharePoint, track, registry, statistics, pipeline

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Config loading and structured logging are required by every downstream
module. Nothing else can be implemented or tested until these pass.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [X] T004 Write `tests/unit/test_config.py`: cover config load from valid TOML; missing required fields raise `ConfigError`; `chunk_overlap >= chunk_size` raises `ConfigError`; `max_file_size_mb` must be positive integer; `[[sources]]` with duplicate names raises `ConfigError`; `registry_path`, `log_path`, `max_file_size_mb` defaults applied when absent; env var referenced by `api_key_env` not set raises `ConfigError`
- [X] T005 [P] Write `tests/unit/test_logger.py`: log file created at configured path; entries match format `YYYY-MM-DD HH:MM:SS [LEVEL] message`; default path `.rag-pipeline.log` used when not configured; logger does not suppress entries on success
- [X] T006 Implement `scripts/lib/config.py`: load `.rag-plugin.toml` via `tomllib`; validate all fields per config-schema.md contract (embedding, vector_store, pipeline, sources); apply defaults for `registry_path`, `log_path`, `max_file_size_mb`; raise `ConfigError` with descriptive message on any violation; expose a `load_config(path) -> Config` function returning a typed dataclass
- [X] T007 [P] Implement `scripts/lib/logger.py`: thin wrapper around Python stdlib `logging`; `init_logger(log_path: str) -> logging.Logger`; file handler writes timestamped entries `YYYY-MM-DD HH:MM:SS [LEVEL] message`; call once from `ingest.py` at startup; all other modules receive the logger via parameter injection (no global logger)

**Checkpoint**: Config loads and logger writes — user story implementation can begin.

---

## Phase 3: User Story 1 — Ingest Documents End-to-End (Priority: P1) 🎯 MVP

**Goal**: A user can run `python scripts/ingest.py --source <path>` and have a single
document (any supported format) read, chunked, embedded, and stored in ChromaDB.
Logging writes to `.rag-pipeline.log`. Files exceeding `max_file_size_mb` are rejected
with a clear error. Changing the embedding model after first ingestion aborts with a
clear remediation message.

**Independent Test**: Point the pipeline at a single `.txt` file, run it, confirm
ChromaDB collection contains entries with correct metadata, and log file contains
structured entries. Then change `embedding.model` in config and confirm startup abort.

- [X] T008 [US1] Write `tests/unit/test_reader.py`: `.txt` and `.md` files return full UTF-8 text; `.pdf` with selectable text returns extracted text; encrypted/password-protected PDF raises `UnreadableError`; scanned PDF (no text) raises `EmptyDocumentError`; `.docx` paragraphs concatenated; legacy `.doc` raises `UnreadableError`; file exceeding `max_file_size_mb` raises `FileSizeLimitError` before any content is read; non-existent file raises `FileNotFoundError`
- [X] T009 [P] [US1] Write `tests/unit/test_chunker.py`: document shorter than `chunk_size` produces exactly one chunk; longer document produces correct chunk count; overlap between consecutive chunks is exactly `chunk_overlap` chars; last chunk is shorter than `chunk_size`; `char_start`/`char_end` offsets are correct; empty string raises `ValueError`
- [X] T010 [P] [US1] Write `tests/unit/test_embedder.py`: successful API call returns list of floats; 5-retry backoff on `RateLimitError` with exponential delay + jitter (mock `time.sleep`); 6th failure raises `EmbeddingError`; `EmbeddingError` raised on non-retryable API error without retrying; API key read from env var named in config
- [X] T011 [P] [US1] Write `tests/unit/test_store.py`: `upsert_chunks` adds entries to in-memory ChromaDB collection; `check_model_consistency` returns True when collection is new; returns True when stored model matches config model; raises `ModelMismatchError` when stored model differs from config; `delete_by_document` removes all chunks for a given `source_name`+`origin_path`; confirms no entries remain after deletion
- [X] T012 [US1] Implement `scripts/lib/reader.py`: `read_document(path, max_file_size_mb) -> str`; check file size via `os.stat` before opening (raise `FileSizeLimitError` if exceeded); dispatch to format handler by extension; `.txt`/`.md` — `open(..., encoding="utf-8")`; `.pdf` — `pypdf.PdfReader`, concatenate page text, raise `UnreadableError` on `PdfReadError`, raise `EmptyDocumentError` if all pages empty; `.docx` — `python_docx.Document`, join paragraphs; `.doc` and unsupported — raise `UnreadableError`
- [X] T013 [P] [US1] Implement `scripts/lib/chunker.py`: `chunk_text(text, chunk_size, chunk_overlap) -> list[Chunk]`; sliding window with step = `chunk_size - chunk_overlap`; each `Chunk` has `chunk_id`, `chunk_index`, `text`, `char_start`, `char_end`; `chunk_id` = `{source_path}::chunk::{index}`
- [X] T014 [US1] Implement `scripts/lib/embedder.py`: `embed_chunks(chunks, config) -> list[EmbeddedChunk]`; initialise `openai.OpenAI(base_url=config.api_base, api_key=os.environ[config.api_key_env])`; call `/v1/embeddings` per chunk (or batch); retry up to 5 times on `RateLimitError` using exponential backoff with jitter (cap total wait at 30 s); raise `EmbeddingError` after all retries exhausted
- [X] T015 [US1] Implement `scripts/lib/store.py`: `check_model_consistency(collection, model_name)`; `upsert_chunks(collection, embedded_chunks, source_path, content_hash)`; `delete_by_document(collection, source_name, origin_path)`; `get_or_create_collection(client, collection_name, model_name) -> Collection`; store `embedding_model` in ChromaDB collection metadata on creation; raise `ModelMismatchError` when metadata model ≠ config model
- [X] T016 [US1] Implement `scripts/ingest.py` (US1 slice): `argparse` CLI with `--source PATH` and `--config PATH`; load config; init logger; call `store.check_model_consistency` and abort with exit code 1 on `ModelMismatchError`; for `--source` path: hash file, call reader → chunker → embedder → store; print completion summary to stdout (per cli-contract.md format); log every step to `.rag-pipeline.log`; exit 0 on success, exit 1 on fatal error

---

## Phase 4: User Story 2 — Batch/Multi-Source Ingestion (Priority: P2)

**Goal**: Sources are defined as a `[[sources]]` array in `.rag-plugin.toml`. Running
`python scripts/ingest.py` (no `--source`) processes all configured sources. A `--source`
override skips the config sources and processes only that local path. Unsupported files
are skipped with a report; an empty directory reports no documents found.

**Independent Test**: Create a config with one `local` source pointing to a directory
of mixed-format files, run the pipeline, confirm the summary shows discovered/succeeded/
skipped counts per source.

- [X] T017 [US2] Write `tests/unit/test_sources.py` (local): `discover_local` returns all files matching `supported_formats` in a directory; non-matching extensions excluded; empty directory returns empty list; single file path returns that file only; nested subdirectories included (no depth limit for local)
- [X] T018 [US2] Implement `scripts/lib/sources.py` — local source: `discover_local(path, supported_formats) -> list[SourceFile]`; if `path` is a file, return `[path]`; if directory, `os.walk` recursively, yield files whose extension is in `supported_formats`; each `SourceFile` has `origin_path`, `source_name`, `file_size_bytes`
- [X] T019 [US2] Extend `scripts/ingest.py` for multi-source: if `--source` provided → wrap in a synthetic `local` SourceConfig and process; if no `--source` → iterate all `[[sources]]` from config; per-source `SourceResult` (discovered/succeeded/skipped/failed); aggregate totals; print per-source + total summary per cli-contract.md; fatal error (exit 1) if neither `--source` nor `[[sources]]` configured

---

## Phase 5: User Story 3 — Incremental Ingestion + Registry (Priority: P3)

**Goal**: Re-running the pipeline on an unchanged document set skips all documents.
Re-running after modifying a document deletes its old embeddings and re-ingests. A
document seen twice in one run (same hash from two sources) is ingested once. The
registry at `.rag-registry.db` records statistics for every ingested document.

**Independent Test**: Ingest 3 documents, confirm registry has 3 rows. Re-run unchanged —
confirm all skipped, `version_count` unchanged. Modify one file, re-run — confirm that
document's `version_count` incremented and old chunks deleted.

- [X] T020 [US3] Write `tests/unit/test_registry.py`: `lookup` returns `None` for new doc; `insert` creates row with correct fields; second `lookup` returns row; `update` increments `version_count`, updates `content_hash`, `last_ingested`, `chunk_count`; within-run dedup set: second doc with same hash returns `DUPLICATE`; atomic rollback: if vector store write raises, registry row not committed (use `sqlite3` rollback in test)
- [X] T021 [US3] Implement `scripts/lib/registry.py`: `open_registry(path) -> sqlite3.Connection`; `create_schema(conn)` (idempotent `CREATE TABLE IF NOT EXISTS`); `lookup(conn, source_name, origin_path) -> DocumentRecord | None`; `insert(conn, record)`; `update(conn, source_name, origin_path, content_hash, chunk_count)`; `RunDedupSet` class: `seen(content_hash) -> bool`, `mark(content_hash)`; all writes use explicit transactions
- [X] T022 [US3] Extend `scripts/ingest.py` with incremental logic: initialise `RunDedupSet` per run; for each document: compute MD5 `content_hash`; check `RunDedupSet` — if seen, skip as duplicate; lookup registry — if found and hash matches, skip as unchanged; if found and hash differs, call `store.delete_by_document` then re-embed then `registry.update`; if not found, embed then `registry.insert`; wrap vector store write + registry write in try/except: on vector store failure, rollback registry transaction (FR-015 atomicity)

---

## Phase 6: SharePoint Source (Extension of US2)

**Goal**: A `[[sources]]` entry with `type = "sharepoint"` lists and downloads files from
a SharePoint Online folder, recursively up to `max_depth` (if set). Two auth modes work:
`device_flow` (interactive, re-prompts each run — known limitation) and
`client_credentials` (headless). Auth failures skip the source with a clear message;
the remaining sources continue processing.

**Independent Test**: Configure a mocked SharePoint source, run the pipeline, confirm
the mock folder listing is called with correct credentials and `max_depth` is respected.
Simulate auth failure and confirm source is skipped with the correct error code in the summary.

- [ ] T023 [SKIP] [US2] ~~Extend `tests/unit/test_sources.py` with SharePoint tests~~ — **Inactive**: SharePoint tests deferred; re-enable when SharePoint integration is ready for testing. Tests to cover: `discover_sharepoint` with mocked folder; `max_depth` depth limiting; `device_flow` and `client_credentials` auth (mocked); `SharePointAuthError`, `SharePointPermissionError`, `SharePointUnreachableError`
- [ ] T024 [US2] Implement SharePoint source in `scripts/lib/sources.py`: `discover_sharepoint(source_config, logger) -> list[SourceFile]`; initialise `ClientContext` from `Office365-REST-Python-Client`; authenticate via `device_flow` (print URL+code to stdout) or `client_credentials`; recursively list folder with depth tracking against `max_depth`; download file bytes; yield `SourceFile` objects; raise typed errors on auth/permission/network failure; no token caching between runs (document as known limitation in code comment)
- [ ] T025 [US2] Extend `scripts/ingest.py` for SharePoint error handling: catch `SharePointAuthError` → set `SourceResult.status = "auth_failed"`, print remediation guidance, continue next source; catch `SharePointUnreachableError` → set status `"unreachable"`; catch `SharePointPermissionError` → set status `"permission_denied"`; none of these abort the entire pipeline

---

## Phase 7: Integration & Polish

**Purpose**: End-to-end verification, final SKILL.md review, and sample config.

- [X] T026 Write `tests/integration/test_pipeline.py`: spin up an in-memory ChromaDB and temp SQLite registry; new document → ingested, registry row created, `version_count = 1`; unchanged document on second run → skipped, registry unchanged; modified document → old chunks deleted, new chunks stored, `version_count = 2`; duplicate hash in same run → ingested once, second skipped as duplicate; model mismatch on startup → exit code 1, clear error on stderr; file exceeding `max_file_size_mb` → skipped, failure reported; **performance assertion**: ingest 10 small docs, assert total time < 120 s (SC-001); **incremental timing assertion**: second run on unchanged set, assert time < 10% of first run (SC-003); [SKIP] SharePoint integration scenario deferred — re-enable with T023
- [X] T027 [P] Review and finalise `skills/doc-ingestion-pipeline/SKILL.md`: verify description contains all required auto-activation keywords (ingest, embed, SharePoint, track, registry, statistics, pipeline); confirm YAML frontmatter is valid; confirm the skill references the correct `ingest.py` invocation path using `$CLAUDE_PLUGIN_ROOT`; **simulate first-user experience**: follow `quickstart.md` steps end-to-end in a clean environment and verify first ingestion completes within 5 min (SC-004)
- [X] T028 [P] Create sample `.rag-plugin.toml` at project root with all sections populated (one local source, all optional fields shown as comments with defaults); file MUST be usable as a working example after filling in the API key env var
- [X] T029 Manually trigger `skills/doc-ingestion-pipeline/SKILL.md` in an active Claude Code session: type natural-language phrases expressing ingestion intent (e.g., "ingest documents from ./docs", "embed my files into the vector store", "track my documents in the registry"); verify skill auto-activates for each phrase and guides to the correct `ingest.py` invocation — this is the mandatory acceptance test per Constitution Principle III
- [X] T030 [P] Run performance benchmark and record results: ingest 10 representative documents (mixed formats) end-to-end; assert completion time < 2 minutes (SC-001); document actual time in test output or a `benchmarks/` note

---

## Dependencies

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7
                               ↗ (Phase 4 also unblocked after Phase 3)
                    Phase 3 ──┤
                               ↘ (Phase 5 requires Phase 3 store.delete_by_document)
```

**Detailed blocking relationships**:

| Phase | Blocked By | Reason |
|-------|-----------|--------|
| Phase 2 | Phase 1 (T001, T002) | Needs directory structure and deps |
| Phase 3 | Phase 2 (T006, T007) | `config.py` and `logger.py` required by all lib modules |
| Phase 4 | Phase 3 (T016) | `ingest.py` US1 slice must exist before extending it |
| Phase 5 | Phase 3 (T015, T016) | Needs `store.delete_by_document` and `ingest.py` orchestrator |
| Phase 6 | Phase 4 (T018, T019) | SharePoint extends `sources.py` and `ingest.py` source loop |
| Phase 7 (T026) | Phase 5 (T022) | Integration test covers all non-SharePoint scenarios (T023/SP skipped) |
| Phase 7 (T027–T030) | Phase 1 (T003) | Polish, live test, and benchmark on already-built components |

---

## Parallel Execution Examples

**Phase 3 unit tests** (write all before implementing):
```
T008 test_reader.py  ──┐
T009 test_chunker.py ──┤ All parallelizable — different files
T010 test_embedder.py──┤
T011 test_store.py   ──┘
```

**Phase 3 implementations** (after tests pass):
```
T012 reader.py   ──┐
T013 chunker.py  ──┤ All parallelizable — different files, no inter-dependencies
T014 embedder.py ──┤
T015 store.py    ──┘
T016 ingest.py   ── (after all above complete)
```

**Final phase** (Phase 7):
```
T027 SKILL.md review + first-user walkthrough ──┐ Parallelizable
T028 .rag-plugin.toml sample                    ─┤
T030 performance benchmark                       ─┘
T026 integration test ── (must wait for Phase 5; SharePoint scenario skipped)
T029 live session skill trigger ── (must wait for T027)
```

---

## Implementation Strategy

**MVP (Phase 1 + 2 + 3)**: Delivers US1 — a user can ingest a single document end-to-end
with structured logging and model mismatch detection. Verifiable with the validation test
in `quickstart.md`:
```bash
echo "The capital of France is Paris." > /tmp/test-rag.txt
python "$CLAUDE_PLUGIN_ROOT/scripts/ingest.py" --source /tmp/test-rag.txt
```

**Increment 2 (+ Phase 4)**: Delivers US2 — batch directory ingestion and multi-source
config. Adds `sources.py` and extends `ingest.py`.

**Increment 3 (+ Phase 5)**: Delivers US3 — incremental ingestion with the SQLite
registry. Adds `registry.py` and deduplication logic.

**Increment 4 (+ Phase 6)**: Delivers SharePoint source support.

**Final (+ Phase 7)**: Integration tests and polish.
