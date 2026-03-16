# API Contract: Ingestion Pipeline Web UI

**Feature**: 002-ingestion-web-ui
**Server**: Flask, port 7842
**Base URL**: `http://localhost:7842`

All JSON endpoints use `Content-Type: application/json`.
Error responses always include `{ "error": "<message>" }`.

---

## GET /

Serves the single-page HTML UI.

**Response**: `200 OK`, `Content-Type: text/html`

---

## GET /api/config

Returns the current `.rag-plugin.toml` contents as a JSON object.

**Response `200`**:
```json
{
  "embedding": {
    "provider": "openai-compatible",
    "model": "text-embedding-3-small",
    "api_base": "https://api.openai.com/v1",
    "api_key_env": "RAG_EMBEDDING_API_KEY"
  },
  "vector_store": {
    "provider": "chroma",
    "path": ".rag-store",
    "collection": "documents"
  },
  "pipeline": {
    "chunk_size": 1000,
    "chunk_overlap": 200,
    "supported_formats": ["txt", "md", "pdf", "docx"],
    "registry_path": ".rag-registry.db",
    "log_path": ".rag-pipeline.log",
    "max_file_size_mb": 100
  },
  "sources": [
    { "name": "my-docs", "type": "local", "path": "./docs" }
  ]
}
```

**Response `404`** (config file missing):
```json
{ "error": "config_missing", "message": ".rag-plugin.toml not found" }
```

**Response `422`** (config file present but invalid):
```json
{ "error": "config_invalid", "message": "<validation error description>" }
```

---

## PUT /api/config

Validates and saves updated config values to `.rag-plugin.toml`.

**Request body**: Same shape as `GET /api/config` response.

```json
{
  "embedding": { ... },
  "vector_store": { ... },
  "pipeline": { "chunk_size": 1500, "chunk_overlap": 300, ... },
  "sources": [ ... ]
}
```

**Response `200`** (saved successfully):
```json
{ "ok": true }
```

**Response `422`** (validation failure — file not written):
```json
{
  "error": "validation_failed",
  "fields": [
    { "field": "pipeline.chunk_overlap", "message": "chunk_overlap must be less than chunk_size" }
  ]
}
```

**Response `500`** (write failure):
```json
{ "error": "write_failed", "message": "<OS error>" }
```

---

## POST /api/ingest/run

Starts a new ingestion run in a background thread.

**Request body**: empty or `{}`

**Response `202 Accepted`** (run started):
```json
{ "run_id": "a1b2c3d4-..." }
```

**Response `409 Conflict`** (another run is already in progress):
```json
{ "error": "run_in_progress", "run_id": "<active run_id>" }
```

**Response `412 Precondition Failed`** (preflight check failed — API key not set):
```json
{
  "error": "preflight_failed",
  "reason": "Environment variable RAG_EMBEDDING_API_KEY is not set"
}
```

**Response `422`** (config missing or invalid):
```json
{ "error": "config_invalid", "message": "..." }
```

---

## GET /api/ingest/stream

SSE endpoint. Pushes progress events for the currently active run.

**Response**: `200 OK`, `Content-Type: text/event-stream`

Each event is formatted as:
```
data: {"event": "<type>", ...fields...}\n\n
```

**Event types** (see `data-model.md` for full field list):

| Type | Description |
|------|-------------|
| `run_started` | Run thread begins processing |
| `preflight_failed` | API key env var not set (run blocked) |
| `document_processed` | One document completed |
| `source_complete` | One source finished |
| `run_complete` | All sources processed |
| `run_error` | Fatal error mid-run |

**Example event sequence**:
```
data: {"event": "run_started", "run_id": "abc", "started_at": "2026-03-16T10:00:00Z"}

data: {"event": "document_processed", "run_id": "abc", "source_name": "my-docs", "file_path": "./docs/a.md", "status": "succeeded", "reason": null}

data: {"event": "document_processed", "run_id": "abc", "source_name": "my-docs", "file_path": "./docs/b.md", "status": "skipped", "reason": "unchanged"}

data: {"event": "source_complete", "run_id": "abc", "source_name": "my-docs", "discovered": 2, "succeeded": 1, "skipped": 1, "failed": 0}

data: {"event": "run_complete", "run_id": "abc", "completed_at": "2026-03-16T10:00:05Z", "total_discovered": 2, "total_succeeded": 1, "total_skipped": 1, "total_failed": 0}
```

---

## GET /api/ingest/runs

Returns the run history for the current server session (last 5 runs).

**Response `200`**:
```json
{
  "runs": [
    {
      "run_id": "abc",
      "started_at": "2026-03-16T10:00:00Z",
      "completed_at": "2026-03-16T10:00:05Z",
      "status": "completed",
      "error_message": null,
      "sources": [
        {
          "label": "my-docs",
          "discovered": 2,
          "succeeded": 1,
          "skipped": 1,
          "failed": 0,
          "skipped_unchanged": 1,
          "skipped_duplicate": 0,
          "failed_docs": [],
          "status": "ok",
          "error_message": null
        }
      ],
      "summary": {
        "total_discovered": 2,
        "total_succeeded": 1,
        "total_skipped": 1,
        "total_failed": 0
      }
    }
  ],
  "active_run": null
}
```

`active_run` is the in-progress run object (status `"running"`) or `null`.

---

## GET /api/registry

Returns all rows from `.rag-registry.db`.

**Query parameters**:
- `search` (optional): filter rows where `source_name` or `origin_path` contains the value (case-insensitive)
- `sort` (optional): column to sort by — one of `source_name`, `origin_path`, `chunk_count`, `version_count`, `last_ingested` (default: `last_ingested`)
- `order` (optional): `asc` or `desc` (default: `desc`)

**Response `200`**:
```json
{
  "records": [
    {
      "source_name": "my-docs",
      "origin_path": "./docs/guide.md",
      "content_hash": "d41d8cd98f00b204e9800998ecf8427e",
      "chunk_count": 5,
      "version_count": 2,
      "last_ingested": "2026-03-16T10:00:05Z"
    }
  ],
  "total": 1
}
```

**Response `404`** (registry file missing):
```json
{ "error": "registry_missing", "message": ".rag-registry.db not found" }
```

---

## Error Response Format

All error responses follow:
```json
{
  "error": "<machine_readable_code>",
  "message": "<human_readable_description>"
}
```

HTTP status codes used:
- `200` — success
- `202` — accepted (async operation started)
- `404` — resource not found
- `409` — conflict (concurrent operation)
- `412` — precondition failed (preflight check)
- `422` — unprocessable entity (validation error)
- `500` — internal server error
