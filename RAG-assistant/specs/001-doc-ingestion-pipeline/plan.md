# Implementation Plan: Document Ingestion Pipeline Skill

**Branch**: `001-doc-ingestion-pipeline` | **Date**: 2026-03-15 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-doc-ingestion-pipeline/spec.md`

## Summary

Build a Claude Code plugin skill that ingests documents from multiple configurable sources
(local filesystem and SharePoint Online) into a ChromaDB vector store. Supported formats:
`.txt`, `.md`, `.pdf`, `.docx`. Sources are defined in `.rag-plugin.toml` as a
`[[sources]]` array. A persistent SQLite document registry (`.rag-registry.db`) tracks
every ingested document with statistics. Deduplication is hash-based: unchanged documents
are skipped; changed documents have their old embeddings fully deleted before re-ingestion;
identical documents encountered more than once in a single run are skipped as duplicates.
The pipeline writes structured logs to `.rag-pipeline.log` (Python logging format),
enforces a 100 MB per-file hard limit, and detects embedding model changes on startup to
prevent vector dimension mismatches.

## Technical Context

**Language/Version**: Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill)
**Primary Dependencies**: `openai`, `chromadb`, `tomllib` (stdlib), `pypdf`, `python-docx`, `Office365-REST-Python-Client`, `msal` (transitive), `sqlite3` (stdlib), `logging` (stdlib)
**Storage**: ChromaDB local filesystem store; SQLite document registry (`.rag-registry.db`); log file (`.rag-pipeline.log`)
**Testing**: `pytest`; manual Claude Code session for skill auto-activation
**Target Platform**: macOS, Linux, Windows/WSL (Principle IV)
**Project Type**: Claude Code plugin (skill + scripts)
**Performance Goals**: 10 docs in < 2 minutes (SC-001); incremental re-run < 10% of initial time (SC-003)
**Constraints**: All script paths use `CLAUDE_PLUGIN_ROOT`; pure-Python deps only; credentials from env vars only; registry updates atomic with vector store writes; files > 100 MB rejected; embedding model change detected on startup

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-design check

| Principle | Gate | Status |
|-----------|------|--------|
| I. Standard Directory Layout | Skill in `skills/doc-ingestion-pipeline/SKILL.md`; all scripts in `scripts/lib/`; tests in `tests/` | ✅ Pass |
| II. Skill-First Design | SKILL.md covers ingestion, SharePoint, and deduplication intent triggers | ✅ Pass |
| III. Test-First Development | Tests required for registry, deduplication logic, clean-delete, and all source types | ✅ Pass |
| IV. Portability & Platform Parity | All deps pure Python; `sqlite3` stdlib; no compiled extensions | ✅ Pass |
| V. Simplicity & Incremental Complexity | SharePoint and registry justified by explicit requests; complexity documented below | ✅ Pass (with justification) |

### Post-design check

| Principle | Gate | Status |
|-----------|------|--------|
| I. Standard Directory Layout | `registry.py` and `logger.py` added to `scripts/lib/`; no new component types | ✅ Pass |
| II. Skill-First Design | SKILL.md to include "track", "registry", "statistics" in description | ✅ Pass |
| III. Test-First Development | `test_registry.py` covers all deduplication paths; atomic failure test required; `test_logger.py` covers log output | ✅ Pass |
| IV. Portability | SQLite stdlib; `logging` stdlib; no OS-specific file operations | ✅ Pass |
| V. Simplicity | Registry is a single SQLite file, no ORM, minimal schema; logger uses stdlib `logging` | ✅ Pass |

**No gate failures.**

## Project Structure

### Documentation (this feature)

```text
specs/001-doc-ingestion-pipeline/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── config-schema.md
│   └── cli-contract.md
└── tasks.md             # Phase 2 output (/speckit.tasks — NOT created here)
```

### Source Code (plugin root)

```text
skills/
└── doc-ingestion-pipeline/
    └── SKILL.md              # Auto-activation: ingest / embed / SharePoint / track / registry

scripts/
├── ingest.py                 # CLI entrypoint; resolves sources; orchestrates pipeline
└── lib/
    ├── config.py             # Config loading/validation; parses [[sources]], registry_path, log_path, max_file_size_mb
    ├── sources.py            # Source discovery: local dir walk + SharePoint folder listing (max_depth aware)
    ├── reader.py             # Text extraction: txt, md, pdf (pypdf), docx (python-docx); enforces file size limit
    ├── chunker.py            # Fixed-size chunking with overlap
    ├── embedder.py           # OpenAI-compatible embedding + retry/backoff (5 retries, exp backoff + jitter, max 30s)
    ├── store.py              # ChromaDB: upsert new chunks, delete stale chunks by doc path; model mismatch detection
    ├── registry.py           # SQLite registry: lookup, insert, update, dedup within-run
    └── logger.py             # Pipeline logger: Python logging module, timestamped text format, configurable path

tests/
├── unit/
│   ├── test_config.py        # Config parsing; valid/invalid [[sources]]; registry_path; log_path; max_file_size_mb
│   ├── test_sources.py       # Local walk; SharePoint listing with max_depth (mocked)
│   ├── test_reader.py        # Extraction for all 4 formats + error cases + file size limit enforcement
│   ├── test_chunker.py       # Chunking correctness
│   ├── test_embedder.py      # Embedding dispatch (mock API); retry/backoff logic
│   ├── test_store.py         # Upsert; delete-by-doc-path (in-memory ChromaDB); model mismatch detection
│   ├── test_registry.py      # Lookup/insert/update; dedup logic; atomic failure rollback
│   └── test_logger.py        # Log file creation; entry format; configurable path
└── integration/
    └── test_pipeline.py      # End-to-end: new doc, unchanged doc (skip), changed doc
                              #   (delete+re-embed), duplicate within run (skip),
                              #   registry populated correctly; model mismatch abort;
                              #   file size rejection; SharePoint mocked
```

**Structure Decision**: Single plugin layout. `registry.py` owns all SQLite interactions.
`store.py` gains a `delete_by_document(source_name, origin_path)` method called by
`ingest.py` before re-ingesting a changed document. `store.py` also gains a
`check_model_consistency(model_name)` method called on startup to detect dimension
mismatches. `logger.py` wraps the stdlib `logging` module and is initialised once in
`ingest.py`. Both vector store and registry operations are wrapped in a single try/except
in `ingest.py` so that if the vector store write fails, the registry transaction is
rolled back.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
| SharePoint OAuth2 + `Office365-REST-Python-Client` | User explicitly requested SharePoint source support | Local-only pipeline cannot satisfy the requirement |
| Per-source `SourceResult` tracking | Multi-source runs require per-source failure reporting | Aggregate-only hides which source failed |
| SQLite registry (`registry.py`) | User explicitly requested persistent document statistics and deduplication | ChromaDB metadata alone cannot provide human-readable history, version counts, or atomic rollback guarantees |
| `logger.py` wrapper module | FR-016 requires dedicated log file separate from stdout; path must be configurable | Using print() or stderr cannot satisfy the log file requirement |
