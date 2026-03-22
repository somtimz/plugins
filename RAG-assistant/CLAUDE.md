# RAG-assistant Development Guidelines

Last updated: 2026-03-19

## Active Technologies

- **Runtime**: Python 3.11+
- **Embedding**: `openai` (OpenAI-compatible API client)
- **Vector store**: `chromadb` (local filesystem, `PersistentClient`)
- **Config**: `tomllib` (stdlib read), `tomli_w` (write)
- **Document extraction**: `pypdf` (PDF), `python-docx` (Word .docx)
- **SharePoint**: `Office365-REST-Python-Client`, `msal` (transitive)
- **Web UI**: `flask` + vanilla JS (single `index.html`), SSE for real-time progress
- **Chat**: `anthropic` (Claude API, streaming)
- **Registry**: `sqlite3` (stdlib)
- **Logging**: `logging` (stdlib)

## Project Structure

```text
.claude-plugin/plugin.json     plugin manifest
skills/
├── doc-ingestion-pipeline/
│   └── SKILL.md               auto-activation skill (ingestion)
└── rag-chat/
    └── SKILL.md               auto-activation skill (chat Q&A)

scripts/
├── ingest.py                  CLI entrypoint: python scripts/ingest.py [--source PATH] [--config PATH]
├── ui.py                      Web UI entrypoint: python scripts/ui.py  →  http://localhost:7842
├── load-corpus.py             utility: load a corpus from the command line
├── templates/
│   └── index.html             single-page web UI (4 tabs: Ingestion, Registry, Config, Chat)
└── lib/
    ├── config.py              load_config(path) → Config dataclass; raises ConfigError
    ├── sources.py             discover_local(), discover_sharepoint()
    ├── reader.py              read_document(path, max_mb) → str; raises UnreadableError / EmptyDocumentError
    ├── chunker.py             chunk_text(text, size, overlap) → list[Chunk]
    ├── embedder.py            embed_chunks(chunks, cfg) → list[EmbeddedChunk]; retry/backoff
    ├── store.py               ChromaDB helpers; check_model_consistency(); delete_by_document()
    ├── registry.py            SQLite registry: open_registry(), lookup/insert/update, RunDedupSet
    ├── logger.py              init_logger(path) → logging.Logger
    ├── pipeline.py            run_ingestion(sources, cfg, logger, progress_callback) → list[SourceResult]
    ├── searcher.py            vector similarity search helpers
    └── ingest_tool.py         Claude/OpenAI tool schemas + execute_* functions for chat tool use

tests/
├── unit/                      one test file per lib module
└── integration/               end-to-end tests (in-memory ChromaDB + tmp SQLite)

specs/
├── 001-doc-ingestion-pipeline/  ingestion pipeline spec, plan, tasks, contracts
├── 002-ingestion-web-ui/        web UI spec, plan, tasks, contracts
└── 003-conversational-rag-ui/   chat UI spec

docs/                           sample documents for testing
requirements.txt                runtime + dev dependencies
.rag-plugin.toml                runtime config (not committed — contains env var references)
.rag-registry.db                SQLite document registry (generated)
.rag-store/                     ChromaDB vector store (generated)
.rag-pipeline.log               structured log file (generated)
```

## Commands

Run from the project root (`plugins/RAG-assistant/`):

```bash
# Install dependencies
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt

# Run ingestion pipeline (CLI)
python3 scripts/ingest.py
python3 scripts/ingest.py --source ./docs/
python3 scripts/ingest.py --source ./report.pdf --config .rag-plugin.toml

# Start the web UI
python3 scripts/ui.py          # → http://localhost:7842

# Run tests
python3 -m pytest tests/
python3 -m pytest tests/unit/
python3 -m pytest tests/integration/

# Lint
ruff check scripts/ tests/
```

## Code Style

- Python 3.11+ — use `tomllib` (stdlib) for reads, `tomli_w` for writes
- No global logger — pass logger via parameter injection
- Credentials always from environment variables, never in config files or code
- Atomic registry + vector store writes: if the vector store write fails, roll back the registry transaction
- Never expose API key values in API responses — only the env var name (`embedding_key_env` / `llm_key_env`)

## Implemented Features

| Feature | Status | Spec |
|---------|--------|------|
| 001 — Document ingestion pipeline | Implemented | specs/001-doc-ingestion-pipeline/ |
| 002 — Ingestion web UI | Implemented | specs/002-ingestion-web-ui/ |
| 003 — Conversational RAG chat UI | Implemented | specs/003-conversational-rag-ui/ |
| 001 — Transparent RAG search | Implemented | specs/001-rag-search-transparency/ |

SharePoint source (feature 001 phase 6, tasks T023–T025) is deferred — local and device_flow auth scaffolding exists but SharePoint tests are skipped.
