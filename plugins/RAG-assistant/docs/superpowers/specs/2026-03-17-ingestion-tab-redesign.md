# Ingestion Tab Redesign

**Date**: 2026-03-17
**Status**: Approved

## Overview

Redesign the Ingestion tab to show the configured source directory contents, ChromaDB collection information, statistics, and a scrollable document/chunk browser — all within the existing single-page UI at `http://localhost:7842`.

## Layout

The Ingestion tab is restructured into three vertical zones:

### Zone 1 — Two-column split (top)

**Left column: Run controls + log (unchanged behaviour)**
- Run Ingestion button + status indicator
- Scrollable log box (SSE-driven, existing)
- Error banner

**Right column: Source Files panel**
- Lists every file discovered in all configured `[[sources]]` directories
- Each row: filename, file size, chunk count, status badge, last ingested date
- Status badges: `✅ ingested` / `⬜ not ingested` / `❌ failed`
- Files with no registry entry show `—` for chunk count and last ingested
- Panel refreshes automatically after an ingestion run completes (on `run_complete` SSE event)
- Loaded on tab activation via `GET /api/sources`

### Zone 2 — Run History table (unchanged)

Existing history table remains below the two-column split, unchanged.

### Zone 3 — ChromaDB Store panel (collapsible, collapsed by default)

**Summary stat cards (always visible when expanded):**
- Total Chunks
- Total Documents
- Embedding Model
- Collection Name

**Per-document chunk accordion:**
- One row per document, showing document name and chunk count
- Click to expand — shows a scrollable list of chunk text previews (first ~150 chars each)
- Chunks loaded lazily on first expand via `GET /api/store/chunks?document=<path>`

## New Backend Endpoints

### `GET /api/sources`

Lists all files in each configured `[[sources]]` directory, cross-referenced with the registry.

**Response:**
```json
{
  "sources": [
    {
      "source_name": "local-docs",
      "type": "local",
      "path": "./docs",
      "files": [
        {
          "origin_path": "docs/rag-overview.md",
          "filename": "rag-overview.md",
          "file_size_bytes": 12480,
          "chunk_count": 8,
          "last_ingested": "2026-03-14T10:22:00",
          "status": "ingested"
        },
        {
          "origin_path": "docs/new-file.pdf",
          "filename": "new-file.pdf",
          "file_size_bytes": 46080,
          "chunk_count": null,
          "last_ingested": null,
          "status": "not_ingested"
        }
      ]
    }
  ]
}
```

Status values: `"ingested"` | `"not_ingested"` | `"failed"` (based on registry lookup; a file that appears in the registry with the latest run marked failed gets `"failed"`).

Returns `422` if config is missing or invalid.

### `GET /api/store/stats`

Returns ChromaDB collection metadata and aggregate counts.

**Response:**
```json
{
  "collection": "documents",
  "embedding_model": "text-embedding-3-small",
  "total_chunks": 1247,
  "total_documents": 4
}
```

Returns `404` if the ChromaDB store does not exist yet. Returns `422` if config is invalid.

### `GET /api/store/chunks`

Returns chunks from the ChromaDB collection, grouped by document.

**Query params:**
- `document` (optional) — filter to a specific `origin_path`; if omitted, returns all documents with their chunks

**Response:**
```json
{
  "documents": [
    {
      "origin_path": "docs/rag-overview.md",
      "source_name": "local-docs",
      "chunk_count": 8,
      "chunks": [
        { "chunk_id": "docs/rag-overview.md::chunk::0", "text": "RAG systems combine retrieval with generation…" }
      ]
    }
  ]
}
```

Chunk text is truncated to 200 characters for the preview. Returns `404` if store does not exist.

## Frontend Changes

**`scripts/templates/index.html`** — Ingestion tab only:

1. Add CSS for two-column layout, file-row styling (status badges, metadata line), stat cards, chunk accordion
2. Replace current single-column tab body with the two-column split
3. Add source files panel (right column) with `loadSources()` function
4. Add ChromaDB panel below history table with `loadStoreStats()` and `loadChunks(docPath)` functions
5. Wire `run_complete` SSE event to call `loadSources()` and reset store stats (mark as stale)

**`scripts/ui.py`** — new routes only:

1. `GET /api/sources` — reads config, walks source directories, cross-references registry
2. `GET /api/store/stats` — opens ChromaDB PersistentClient, reads collection metadata + count
3. `GET /api/store/chunks` — queries ChromaDB, groups results by document, truncates text

## Out of Scope

- No changes to Registry, Config, or Chat tabs
- No changes to existing run/log/SSE/history behaviour
- No pagination for the chunk list (scroll within the accordion)
- No SharePoint source support (deferred, consistent with existing codebase)
- No chunk search or filtering in the store panel

## Files Changed

| File | Change |
|------|--------|
| `scripts/ui.py` | Add 3 new GET routes |
| `scripts/templates/index.html` | Restructure Ingestion tab HTML + JS + CSS |

No new files, no new dependencies.
