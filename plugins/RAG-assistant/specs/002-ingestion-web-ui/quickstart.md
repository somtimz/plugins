# Quickstart: Ingestion Pipeline Web UI

**Feature**: 002-ingestion-web-ui
**Audience**: Developer implementing the feature

---

## Prerequisites

- Feature 001 (doc ingestion pipeline) complete — `scripts/ingest.py` and `scripts/lib/` are in place
- `.venv` with existing dependencies: `openai`, `chromadb`, `pypdf`, `python-docx`
- `.rag-plugin.toml` configured with at least one source
- `RAG_EMBEDDING_API_KEY` exported in the shell environment

---

## New Dependency

```bash
.venv/bin/pip install flask tomli-w
```

- `flask` — web server and SSE transport
- `tomli-w` — TOML serialization (stdlib `tomllib` is read-only in Python 3.11)

---

## New Files

```text
scripts/
├── ui.py                    # Flask app entry point (new)
└── lib/
    └── pipeline.py          # Extracted run_ingestion() public API (new)

scripts/templates/
└── index.html               # Single-page UI (new)
```

---

## Refactoring Required

`scripts/ingest.py` — move `SourceResult` and `_process_file_list()` to `scripts/lib/pipeline.py` and add a `progress_callback` parameter. `ingest.py` becomes a thin CLI wrapper that calls `lib.pipeline.run_ingestion()`. No user-visible behavior change.

---

## Start the UI

```bash
export RAG_EMBEDDING_API_KEY="sk-..."
.venv/bin/python scripts/ui.py
# → Serving on http://localhost:7842
```

Open `http://localhost:7842` in a browser.

---

## Key Workflows

**Trigger ingestion**: Click "Run Ingestion" → progress list updates per document → summary panel appears on completion.

**View registry**: Switch to the Registry tab → search box filters rows in real time → click column headers to sort.

**View/edit config**: Switch to the Config tab → all config sections displayed → edit values → click Save (validation runs before writing to disk).

---

## Smoke Test (manual)

1. Start UI with a valid `.rag-plugin.toml` and at least one document in a source folder
2. Open `http://localhost:7842`
3. Click "Run Ingestion" — verify progress events appear, run completes
4. Switch to Registry tab — verify ingested document appears
5. Switch to Config tab — verify all config sections render
6. Change `chunk_size` to 500, click Save — verify `.rag-plugin.toml` is updated
7. Set `chunk_overlap` equal to `chunk_size`, click Save — verify validation error, file unchanged
8. Open a second browser tab, click "Run Ingestion" in tab 1, try clicking it in tab 2 — verify button disabled and "run in progress" message shown

---

## Architecture Summary

```
Browser (EventSource)          Flask (port 7842)           Pipeline
       |                              |                        |
       |── GET /api/ingest/stream ───>|                        |
       |<── SSE events ───────────────|                        |
       |                              |                        |
       |── POST /api/ingest/run ─────>|── threading.Thread ───>|
       |                              |    run_ingestion()     |
       |                              |    announcer.announce()|
       |<── 202 Accepted ─────────────|                        |
       |<── document_processed ───────|<── progress_callback ──|
       |<── run_complete ─────────────|                        |
```

- `POST /api/ingest/run` returns `202` immediately; pipeline runs in a background thread
- Progress events flow: pipeline calls `progress_callback` → Flask `MessageAnnouncer.announce()` → queued to each SSE listener
- `_run_lock` prevents a second run while one is active
