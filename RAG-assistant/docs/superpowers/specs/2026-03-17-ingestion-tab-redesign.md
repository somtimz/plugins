# Ingestion Tab Redesign

**Date**: 2026-03-17
**Status**: Approved

## Overview

Redesign the Ingestion tab to show the configured source directory contents, ChromaDB collection information, statistics, and a scrollable document/chunk browser — all within the existing single-page UI at `http://localhost:7842`.

## Layout

```
┌─────────────────────────────────────────────────────────┐
│  ZONE 1: Two-column split                                │
│  ┌──────────────────────┬────────────────────────────┐  │
│  │ Left: Run + Log      │ Right: Source Files        │  │
│  └──────────────────────┴────────────────────────────┘  │
├─────────────────────────────────────────────────────────┤
│  ZONE 2: Run History table (unchanged DOM, full width)  │
├─────────────────────────────────────────────────────────┤
│  ZONE 3: ChromaDB Store panel (collapsible)             │
└─────────────────────────────────────────────────────────┘
```

### Zone 1 — Two-column split (top)

**Left column**: Run controls + log (unchanged behaviour).

**Right column: Source Files panel**
- Lists every file matching `cfg.pipeline.supported_formats` discovered in all configured `[[sources]]` directories. Matching uses `Path(filename).suffix.lstrip(".").lower()` checked against the lowercased `supported_formats` set — identical to `sources.py:discover_local`.
- Each row: filename, human-readable file size, chunk count, status badge (`✅ ingested` / `⬜ not ingested`), last ingested date
- Files with no registry entry show `—` for chunk count and last ingested
- Shows a spinner while `loadSources()` is in flight
- Re-fetches `GET /api/sources` on **every** Ingestion tab activation (not cached) and after both `run_complete` and `run_error` SSE events

**Source Files states:**

| State | Display |
|-------|---------|
| Loading | Spinner |
| Config missing (404 `config_missing`) | "No configuration file found" + link to Config tab |
| Config invalid (422 `config_invalid`) | "Configuration invalid: \<message\>" |
| Source directory missing/inaccessible | Source name + "Directory not found: \<path\>" |
| No supported files | Source name + "No supported files found" |
| Normal | File rows |

Registry missing → all files show as `not_ingested`. `ui.py` must be started from the project root (the directory containing `.rag-plugin.toml`) — this is already the required working directory for config loading, and it ensures `discover_local` receives the same relative source paths as `ingest.py`, keeping `origin_path` values in sync with the registry.

### Zone 2 — Run History table (unchanged)

### Zone 3 — ChromaDB Store panel (collapsible, collapsed by default)

**State machine:**
- Collapsed, fresh → header only
- Expanding (first time or after Retry) → fetch `GET /api/store/stats`, show spinner, then render cards + accordion
- Open, fresh → cards + accordion displayed
- `run_complete`/`run_error` received while **open** → re-fetch stats; on success update cards; on failure show "⚠ Failed to refresh — Retry" inline (Retry re-fetches stats only; already-expanded accordion rows are not re-fetched)
- `run_complete`/`run_error` received while **closed** → show `⟳` stale badge on header; clicking header clears badge and opens (same expand flow as above)

**Stat cards:** Total Chunks · Total Documents · Embedding Model · Collection Name

`total_documents` = count of distinct `origin_path` values in ChromaDB metadata. May differ from Registry tab (ChromaDB is source of truth for this panel).

**Per-document chunk accordion:**
- One collapsed row per distinct `origin_path` in the collection, showing filename and chunk count
- On first expand, fetches `GET /api/store/chunks?document=<origin_path>`; subsequent expands use cached data
- Chunks displayed in ascending `chunk_index` order with 1-based display index
- If `capped: true`, shows "Showing first 500 of \<total\> chunks" below the list

**Store panel states:**

| State | Display |
|-------|---------|
| Store path missing or collection not yet created | "No documents have been ingested yet" |
| Config missing/invalid | Same messages as Source Files panel |
| Empty collection | Stat cards with zeros, no accordion rows |
| Fetch failure | "⚠ Failed to refresh — Retry" |

## New Backend Endpoints

### Implementation notes (shared)

All three new routes use `load_config(_DEFAULT_CONFIG)` for config loading — same pattern as the existing `/api/chat` and `/api/config` routes. `registry_path` is resolved from `cfg.pipeline.registry_path` (default `".rag-registry.db"` is defined in the `Config` dataclass in `lib/config.py`). All three routes are GET-only; Flask returns 405 for other methods automatically.

### `GET /api/sources`

**File discovery:** call `discover_local(source.path, cfg.pipeline.supported_formats)` (from `lib/sources.py`) to obtain `SourceFile` objects — the same function `ingest.py` uses, so `sf.origin_path` values are guaranteed to match what is stored in the registry. For each `SourceFile`, look up `(source.name, sf.origin_path)` in the registry using the logical source name from the config (`source.name`, e.g. `"local-docs"`), **not** `sf.source_name` (which `discover_local` sets to the file path, not the logical name). Derive `filename` from `Path(sf.origin_path).name`. If the registry file does not exist, skip lookup and default to `not_ingested`. Wrap the `discover_local` call in a try/except to catch `OSError`/`PermissionError` for inaccessible directories; on error set `"error"` on the source object and return an empty `"files"` list (HTTP 200).

**Error responses:**
- `404` — `{"error": "config_missing", "message": "<path> not found"}`
- `422` — `{"error": "config_invalid", "message": "<reason>"}`

Per-source directory errors return HTTP `200` with the `error` field on the source object set to a human-readable string (e.g. `"Directory not found: ./docs"`). For success, `error` is `null`.

**Success response:**
```json
{
  "sources": [
    {
      "source_name": "local-docs",
      "type": "local",
      "path": "./docs",
      "error": null,
      "files": [
        {
          "origin_path": "./docs/rag-overview.md",
          "filename": "rag-overview.md",
          "file_size_bytes": 12480,
          "chunk_count": 8,
          "last_ingested": "2026-03-14T10:22:00+00:00",
          "status": "ingested"
        }
      ]
    }
  ]
}
```

`last_ingested` returned as-is from registry (ISO-8601 with timezone). Frontend formats for display.

### `GET /api/store/stats`

Opens ChromaDB with `PersistentClient(path=cfg.vector_store.path)`. If the named collection does not exist (`ValueError` or `InvalidCollectionException` from ChromaDB), returns `404 {"error": "store_missing", ...}` — same as store path not found.

`total_documents` = `len(set(m["origin_path"] for m in collection.get(include=["metadatas"])["metadatas"]))`.

**Error responses:**
- `404` — `{"error": "config_missing", ...}` or `{"error": "store_missing", ...}`
- `422` — `{"error": "config_invalid", ...}`

**Success response:**
```json
{
  "collection": "documents",
  "embedding_model": "text-embedding-3-small",
  "total_chunks": 1247,
  "total_documents": 4
}
```

### `GET /api/store/chunks`

**Query params:** `document` (required, max 1000 chars).

Queries ChromaDB with `collection.get(where={"origin_path": {"$eq": document}}, include=["metadatas", "documents"])`. Results are sorted ascending by `chunk_index` from metadata. Maximum 500 results. Truncation: `text = text[:199] + "…" if len(text) > 200 else text`. `chunk_id` comes from the ChromaDB document ID (the `ids` field returned by `collection.get()`), which is set to `chunk.chunk_id` (e.g. `"docs/rag-overview.md::chunk::0"`) at upsert time in `store.py`.

Store exists but no chunks match → `200` with `chunks: []`, `total: 0`, `capped: false`.

**Error responses:**
- `400` — `{"error": "invalid_param", ...}`
- `404` — `{"error": "config_missing", ...}` or `{"error": "store_missing", ...}`
- `422` — `{"error": "config_invalid", ...}`

**Success response:**
```json
{
  "origin_path": "docs/rag-overview.md",
  "chunks": [
    { "chunk_index": 0, "chunk_id": "docs/rag-overview.md::chunk::0", "text": "RAG systems combine retrieval with generation…" }
  ],
  "total": 8,
  "capped": false
}
```

## Frontend Changes

**`scripts/templates/index.html`** — Ingestion tab only:
1. CSS: two-column flex layout, file-row badges and metadata, spinner, stat cards, chunk accordion, stale badge
2. Restructure `#tab-ingestion` HTML into three zones
3. `loadSources()` on every tab activation + `run_complete` + `run_error`
4. `loadStoreStats()` on first expand and Retry; `loadChunks(originPath)` on first accordion expand (cached); stale badge state machine as described above

**`scripts/ui.py`** — 3 new GET routes only.

## Out of Scope

- No changes to Registry, Config, Chat tabs or existing SSE/run/history behaviour
- No SharePoint, chunk search, pagination, or authentication

## Files Changed

| File | Change |
|------|--------|
| `scripts/ui.py` | Add 3 new GET routes |
| `scripts/templates/index.html` | Restructure Ingestion tab HTML + JS + CSS |
