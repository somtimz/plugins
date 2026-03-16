# Data Model: Ingestion Pipeline Web UI

**Feature**: 002-ingestion-web-ui
**Date**: 2026-03-16

---

## Entities

### IngestionRun

A single pipeline execution. Stored in-memory (capped at 5 per session).

| Field | Type | Description |
|-------|------|-------------|
| `run_id` | str | UUID4, generated at run start |
| `started_at` | str (ISO 8601) | UTC timestamp when run started |
| `completed_at` | str \| None | UTC timestamp when run completed; null while running |
| `status` | RunStatus | `"running"` \| `"completed"` \| `"failed"` \| `"blocked"` |
| `error_message` | str \| None | Top-level fatal error (e.g., config invalid, preflight failure) |
| `sources` | list[SourceResult] | Per-source outcomes |
| `summary` | RunSummary \| None | Aggregate counts; null until run completes |

**State transitions**:
```
created → running → completed
                 → failed       (fatal error, e.g. config load fails)
                 → blocked      (preflight check fails: API key not set)
```

**Validation rules**:
- Only one `IngestionRun` with `status == "running"` may exist at a time
- History list holds the last 5 completed/failed/blocked runs; oldest is discarded when a 6th is added

---

### SourceResult

Per-source outcome within an `IngestionRun`. Mirrors the existing `SourceResult` dataclass in `ingest.py`.

| Field | Type | Description |
|-------|------|-------------|
| `label` | str | Source name from config (e.g., `"my-docs"`) |
| `discovered` | int | Total documents found |
| `succeeded` | int | Documents successfully embedded |
| `skipped` | int | Documents skipped (unchanged + duplicate) |
| `failed` | int | Documents that could not be processed |
| `skipped_unchanged` | int | Subset of skipped: hash matches registry |
| `skipped_duplicate` | int | Subset of skipped: duplicate within this run |
| `failed_docs` | list[DocumentEntry] | Per-document failure details |
| `status` | str | `"ok"` \| `"auth_failed"` \| `"unreachable"` \| `"permission_denied"` |
| `error_message` | str \| None | Source-level fatal error |

---

### DocumentEntry

Per-document status emitted as an SSE event during a run and stored in `SourceResult.failed_docs`.

| Field | Type | Description |
|-------|------|-------------|
| `file_path` | str | Absolute or relative path to the document |
| `source_name` | str | Owning source label |
| `status` | str | `"succeeded"` \| `"skipped"` \| `"failed"` |
| `reason` | str \| None | Human-readable reason for skip or failure |

---

### RunSummary

Aggregate counts across all sources. Computed at run completion.

| Field | Type | Description |
|-------|------|-------------|
| `total_discovered` | int | Sum of `discovered` across all sources |
| `total_succeeded` | int | Sum of `succeeded` |
| `total_skipped` | int | Sum of `skipped` |
| `total_failed` | int | Sum of `failed` |

---

### RegistryRecord

A row from `.rag-registry.db`. Mirrors the existing `DocumentRecord` dataclass in `lib/registry.py`.

| Field | Type | Description |
|-------|------|-------------|
| `source_name` | str | Source label |
| `origin_path` | str | File path at time of ingestion |
| `content_hash` | str | MD5 hex digest of file content |
| `chunk_count` | int | Number of chunks stored in the vector store |
| `version_count` | int | How many times this document has been re-ingested |
| `last_ingested` | str (ISO 8601) | UTC timestamp of last successful ingestion |

**Read-only from UI**: The registry is written only by the ingestion pipeline, never directly by the UI.

---

### PipelineConfig

The full contents of `.rag-plugin.toml`. Mirrors the `Config` dataclass hierarchy in `lib/config.py`.

```
PipelineConfig
├── embedding: EmbeddingConfig
│   ├── provider: str        (e.g. "openai-compatible")
│   ├── model: str           (e.g. "text-embedding-3-small")
│   ├── api_base: str        (e.g. "https://api.openai.com/v1")
│   └── api_key_env: str     (name of the env var, not the key itself)
├── vector_store: VectorStoreConfig
│   ├── provider: str        (e.g. "chroma")
│   ├── path: str            (e.g. ".rag-store")
│   └── collection: str      (e.g. "documents")
├── pipeline: PipelineSettings
│   ├── chunk_size: int
│   ├── chunk_overlap: int
│   ├── supported_formats: list[str]
│   ├── registry_path: str
│   ├── log_path: str
│   └── max_file_size_mb: int
└── sources: list[SourceConfig]
    └── (name, type, path) per [[sources]] entry
```

**Validation rules**:
- `chunk_overlap` must be < `chunk_size` (FR-010)
- `api_key_env` must be a non-empty string
- `sources` must have at least one entry
- Source `path` must be a non-empty string

**Note**: The API key value is never exposed via any endpoint. Only `api_key_env` (the env var name) is shown.

---

## SSE Event Envelope

Events pushed over the `/api/ingest/stream` SSE connection.

```json
{
  "event": "<event_type>",
  "data": { ... }
}
```

| Event type | When | Data fields |
|------------|------|-------------|
| `run_started` | Run thread begins | `run_id`, `started_at` |
| `preflight_failed` | API key env var not set | `run_id`, `reason` |
| `document_processed` | Each document completes | `run_id`, `source_name`, `file_path`, `status`, `reason` |
| `source_complete` | Each source completes | `run_id`, `source_name`, SourceResult fields |
| `run_complete` | All sources done | `run_id`, `completed_at`, RunSummary fields |
| `run_error` | Fatal error mid-run | `run_id`, `error_message` |

---

## State: In-Memory Run Store

Module-level state in `scripts/ui.py`:

```python
_run_history: list[dict]  # max 5 entries, newest first
_active_run: dict | None  # the currently running run, or None
_run_lock: threading.Lock  # prevents concurrent runs
```

No persistence. Reset on server restart.
