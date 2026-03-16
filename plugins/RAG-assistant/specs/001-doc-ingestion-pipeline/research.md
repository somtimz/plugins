# Research: Document Ingestion Pipeline Skill

**Feature**: 001-doc-ingestion-pipeline
**Date**: 2026-03-15
**Status**: Complete — all unknowns resolved

## Decision 1: Embedding Provider Abstraction

**Decision**: Use the OpenAI-compatible HTTP API as the embedding abstraction layer.

**Rationale**: The spec requires embedding provider to be config-file-driven, not
hardcoded. The OpenAI REST API for embeddings (`POST /v1/embeddings`) has become a
de-facto standard implemented by OpenAI, Azure OpenAI, Ollama, LM Studio, Together AI,
and others. Using it as the abstraction means users can point the config at any
OpenAI-compatible endpoint — local or cloud — without changing the pipeline code.
The `openai` Python library supports custom `base_url` and `api_key` configuration,
making it the cleanest single-dependency solution.

**Alternatives considered**:
- `sentence-transformers` (local only, no API abstraction, large dependency footprint)
- `litellm` (broader abstraction but heavier dependency, more complex for a plugin script)
- Custom HTTP client (more portable but reinvents what the `openai` library already does)

---

## Decision 2: Vector Store Default

**Decision**: ChromaDB as the default local vector store.

**Rationale**: ChromaDB is a pure-Python, embedded vector database that requires no
separate server process. It stores data on the local filesystem, aligns with the spec
assumption that everything runs locally, and has a simple Python API. It supports
metadata filtering (needed for incremental ingestion change detection) and is the most
commonly used local vector store in RAG prototypes as of 2026.

**Alternatives considered**:
- FAISS (no metadata support, no built-in persistence layer, harder to query by metadata)
- Qdrant local mode (binary dependency, heavier footprint)
- SQLite + pgvector extension (requires PostgreSQL or sqlite-vec, more complex setup)
- Pinecone / Weaviate cloud (violates local-first assumption from spec)

---

## Decision 3: Configuration File Format

**Decision**: TOML format, file named `.rag-plugin.toml` at the project root.

**Rationale**: TOML is the standard configuration format for Python tooling (used by
`pyproject.toml`, `ruff.toml`, etc.), is human-readable without the indentation
sensitivity of YAML, and is natively supported in Python 3.11+ via `tomllib`. A
dotfile (`.rag-plugin.toml`) follows the convention of project-scoped config files
(`.eslintrc`, `.prettierrc`) and is easy to gitignore or commit per project preference.

**Alternatives considered**:
- YAML (more ambiguous syntax, no stdlib parser in older Python)
- JSON (no comments, less readable for config)
- INI/configparser (limited nesting support for embedding + store sections)
- Environment variables only (hard to version-control or share across team)

**Config schema** (resolved for data-model and contracts):
```toml
[embedding]
provider = "openai-compatible"
model = "text-embedding-3-small"
api_base = "https://api.openai.com/v1"
api_key_env = "RAG_EMBEDDING_API_KEY"

[vector_store]
provider = "chroma"
path = ".rag-store"
collection = "documents"

[pipeline]
chunk_size = 1000
chunk_overlap = 200
supported_formats = ["txt", "md"]
```

---

## Decision 4: Chunking Strategy

**Decision**: Fixed-size character window with overlap. Default: 1000-char chunks,
200-char overlap.

**Rationale**: The spec explicitly states this as the default strategy and defers
advanced strategies to future iterations. A 1000/200 split is the most widely cited
baseline in RAG literature — large enough to preserve context, small enough to stay
within typical embedding model token limits (most models handle 512–8192 tokens;
1000 chars ≈ 200–250 tokens). Overlap prevents context loss at chunk boundaries.

**Alternatives considered**:
- Sentence-boundary chunking (requires NLP library, out of scope per spec)
- Semantic chunking (requires additional embedding pass, significantly more complex)
- Token-based chunking (requires tokenizer per model, adds coupling to embedding choice)

---

## Decision 5: Change Detection for Incremental Ingestion

**Decision**: MD5 hash of file content, stored as metadata on each ChromaDB entry.

**Rationale**: Content hash is more reliable than last-modified timestamp (mtime can be
reset by git checkout, file copies, or filesystem operations). MD5 is fast and sufficient
for change detection (not a security hash — collisions irrelevant here). The hash is
stored as a metadata field on the ChromaDB collection entry, enabling O(1) lookup per
document on re-run.

**Alternatives considered**:
- `mtime` (unreliable across git operations and file copies)
- SHA-256 (slower, no benefit for change detection use case)
- Storing a separate manifest file (extra state to manage, can go out of sync)

---

## Decision 11: Document Registry Storage

**Decision**: SQLite database file (`.rag-registry.db`) using Python's `sqlite3` stdlib.

**Rationale**: The registry must be persistent, queryable, and require no new
dependencies. `sqlite3` is part of the Python stdlib (no pip install), stores data in a
single portable file, supports ACID transactions (needed for FR-015 atomicity), and is
easily inspected with any SQLite browser. A single-file database sits naturally alongside
`.rag-store/` in the project directory.

**Registry location**: Defaults to `.rag-registry.db` at project root; path is
configurable in `.rag-plugin.toml` under `[pipeline].registry_path`.

**Schema**:
```sql
CREATE TABLE documents (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    source_name     TEXT NOT NULL,
    origin_path     TEXT NOT NULL,
    content_hash    TEXT NOT NULL,
    file_size_bytes INTEGER,
    chunk_count     INTEGER NOT NULL DEFAULT 0,
    version_count   INTEGER NOT NULL DEFAULT 1,
    first_ingested  TEXT NOT NULL,   -- ISO 8601
    last_ingested   TEXT NOT NULL,   -- ISO 8601
    UNIQUE(source_name, origin_path)
);
```

**Atomicity (FR-015)**: Registry updates are wrapped in a SQLite transaction with the
vector store operation. If the vector store write raises an exception, the transaction
is rolled back — the registry is never updated for a failed ingestion.

**Alternatives considered**:
- JSON file (no query support, grows unbounded, not atomic without file locking)
- TOML/YAML file (same problems as JSON)
- Separate PostgreSQL/MySQL (massive overhead, requires server process)
- ChromaDB metadata only (not a separate queryable registry; stats not easily retrieved)

---

## Decision 8: Multi-Source Configuration Schema

**Decision**: TOML array of tables (`[[sources]]`) for multiple named data sources.

**Rationale**: TOML's array-of-tables syntax (`[[sources]]`) is the natural way to
express a list of heterogeneous configuration objects. Each `[[sources]]` block defines
one source with its type-specific fields. This is consistent with the existing TOML
config approach (Decision 3) and allows local and SharePoint sources to coexist with
different field sets per source type.

**Alternatives considered**:
- Numbered sections (`[source.1]`, `[source.2]`) — non-idiomatic TOML, harder to read
- Inline array of inline tables — loses multi-line readability
- Separate config file per source — over-engineered for typical usage

---

## Decision 9: SharePoint Client Library

**Decision**: `Office365-REST-Python-Client` for SharePoint file listing and downloading.

**Rationale**: `Office365-REST-Python-Client` provides a high-level Python API purpose-
built for SharePoint and Microsoft 365. It supports both delegated (device code flow)
and application (client credentials) authentication via MSAL internally. File listing
(`Folder.files`) and binary download (`File.open_binary`) match exactly what the
pipeline needs. It is pure Python and cross-platform (Principle IV compliant).

**Alternatives considered**:
- `msgraph-sdk-python` (official MS SDK, broader scope, more complex for SharePoint
  file operations specifically — higher learning curve, more boilerplate)
- `msal` + raw `requests` against Graph API (more portable but requires manual
  handling of pagination, drive item resolution, and download URLs — significant
  boilerplate for no functional gain)
- `shareplum` (older, less maintained, no MSAL support)

---

## Decision 10: SharePoint Authentication Approach

**Decision**: Support both `device_flow` (interactive) and `client_credentials`
(headless) per source, configured via `auth_type` in the source config block.

**Rationale**: Claude Code sessions are interactive — device code flow is natural
(user sees a URL + code in the terminal, opens a browser once, token is cached).
However, automated or CI scenarios need headless auth via a service principal. Both
modes read all credentials from environment variables; nothing sensitive is stored in
the config file.

**Token caching**: MSAL's built-in token cache is used. For device flow, the token is
cached in memory for the duration of the pipeline run. Re-authentication is required on
the next run (acceptable for interactive use; service principal tokens are short-lived
and obtained fresh each run).

**Alternatives considered**:
- Username/password flow (doesn't work with MFA, not recommended by Microsoft)
- Certificate-based auth (more secure than client_secret but significantly more complex
  setup; deferred to future version)
- Shared access tokens in config (security risk — credentials in config file violates
  Principle IV's portability guidance and creates secret-leakage risk)

---

## Decision 6: PDF Text Extraction Library

**Decision**: `pypdf` (pure Python PDF library).

**Rationale**: `pypdf` is pure Python, installs without compiled dependencies, and
handles the common case of selectable-text PDFs. It raises a clear exception for
encrypted/password-protected files and returns empty text for scanned (image-only)
pages — both are detectable conditions that map to FR-006a's skip-with-explanation
requirement. Per Principle V, it is the simplest library that meets the stated scope
(text extraction only; OCR is out of scope).

**Alternatives considered**:
- `pymupdf` / `fitz` (faster, richer, but requires compiled C extension — violates
  Principle IV's portability requirement on some platforms)
- `pdfminer.six` (more accurate layout extraction but slower, more complex API, no
  advantage for plain text extraction)
- `pdfplumber` (wraps `pdfminer`, same tradeoffs with additional dependency)

---

## Decision 7: Word Document (.docx) Text Extraction Library

**Decision**: `python-docx` for `.docx` (Office Open XML) files only.

**Rationale**: `python-docx` is the standard, pure-Python library for reading `.docx`
files. It extracts paragraph text reliably and is a single lightweight dependency.
Legacy `.doc` binary format requires either `antiword` (system binary, not portable)
or `win32com` (Windows-only) — both violate Principle IV. Scoping to `.docx` only
is therefore both a simplicity and portability decision.

**Alternatives considered**:
- `textract` (system-level dependencies, not portable)
- `docx2txt` (simpler API but less actively maintained)
- `win32com` (Windows-only, violates Principle IV)
- `antiword` (system binary, not portable, `.doc` format only)

---

## Decision 12: Pipeline Logging

**Decision**: Python stdlib `logging` module writing to a dedicated file (`.rag-pipeline.log`
by default), with timestamped human-readable entries in the format
`YYYY-MM-DD HH:MM:SS [LEVEL] message`. Log file path configurable via
`pipeline.log_path` in `.rag-plugin.toml`.

**Rationale**: FR-016 requires logging separate from stdout. The stdlib `logging` module
is zero-dependency, handles file rotation if needed in future, and produces the
timestamped format users expect from CLI tools. Keeping it as a thin `logger.py` wrapper
means all pipeline modules can `import logger` and call a single configured logger.
Human-readable text was chosen over JSON or logfmt because this is an interactive CLI
tool — readability outweighs machine parseability.

**Alternatives considered**:
- `structlog` (third-party, JSON output — overkill for a CLI pipeline)
- logfmt (key=value format — machine-friendly but less readable for developers)
- Writing to stdout with `--verbose` flag (cannot satisfy separate-file requirement)

---

## Decision 13: File Size Limit

**Decision**: Hard 100 MB per-file limit. Files exceeding the limit are skipped with a
clear error message. The limit is configurable via `pipeline.max_file_size_mb` in
`.rag-plugin.toml`.

**Rationale**: FR-017 and SC-001 (10 docs < 2 min) require predictable memory usage and
runtime. A 100 MB file read entirely into memory during extraction could exhaust available
RAM on a development machine; chunking a 100 MB document also generates thousands of
chunks and embedding API calls. The limit is enforced before reading the file content
(OS `stat` call) so it adds negligible overhead on valid documents.

**Alternatives considered**:
- No limit (rely on OS memory errors — violates SC-002 zero silent failures)
- 50 MB soft warning (warning without rejection doesn't prevent OOM)
- Streaming extraction (complex, not supported uniformly by pypdf/python-docx)

---

## Decision 14: Embedding Model Change Detection

**Decision**: On startup, `store.py` reads the ChromaDB collection metadata field
`embedding_model` (written at first ingestion). If the collection already exists and the
stored model name differs from the current config value, the pipeline aborts with exit
code 1 and a clear error instructing the user to delete the store and registry and re-run.

**Rationale**: ChromaDB enforces a fixed vector dimension per collection. Mixing embeddings
from models with different dimensions (e.g., `text-embedding-3-small` → `nomic-embed-text`)
causes a hard runtime error at upsert time with an opaque ChromaDB error. Detecting the
mismatch upfront and aborting immediately satisfies SC-002 (zero silent failures) and
gives the user actionable guidance.

**Alternatives considered**:
- Let ChromaDB surface the error (opaque error, no remediation guidance)
- Auto-wipe and re-ingest (data loss without explicit user consent)
- Add a `--force-remodel` flag (scope creep in v1; can be added later)

---

## Decision 15: SharePoint Subfolder Traversal Depth

**Decision**: Recursive traversal by default (unlimited depth). Each SharePoint source
config MAY include an optional `max_depth` integer to cap traversal depth.
`max_depth = 1` means the configured folder only, with no sub-folder recursion. Omitting
`max_depth` (or setting it to `0`) means unlimited recursion.

**Rationale**: SharePoint document libraries are often deeply nested. A default depth cap
would silently miss documents (violates SC-002). Unlimited recursion as default with an
opt-in cap gives users control without unexpected omissions.

**Alternatives considered**:
- Top-level only by default (silently misses deeply nested documents)
- Unlimited only, no cap option (prevents users from scoping large libraries)

---

## All NEEDS CLARIFICATION Resolved

| Item | Resolution |
|------|------------|
| FR-004: Embedding provider | OpenAI-compatible API, configured in `.rag-plugin.toml` |
| FR-010: Vector store target | ChromaDB local, path configured in `.rag-plugin.toml` |
| FR-006 (amended): PDF support | `pypdf`; scanned and encrypted PDFs skipped with explanation |
| FR-006 (amended): Word support | `python-docx`; `.docx` only; `.doc` skipped with explanation |
| FR-008 (strengthened): deduplication | Hash-based skip; delete old chunks before re-ingestion |
| FR-014: Document registry | SQLite `.rag-registry.db` via stdlib `sqlite3` |
| FR-015: Atomicity | SQLite transaction wrapping registry update + vector store write |
| FR-011: Multi-source config | TOML `[[sources]]` array of tables |
| FR-012: SharePoint source | `Office365-REST-Python-Client` |
| FR-013: SharePoint auth | `device_flow` + `client_credentials` via MSAL; credentials from env vars |
| FR-016: Pipeline logging | Python `logging` stdlib; timestamped text format; `.rag-pipeline.log`; configurable path |
| FR-017: File size limit | 100 MB hard limit; configurable via `pipeline.max_file_size_mb`; skip with clear error |
| FR-012 (depth): SharePoint traversal | Recursive unlimited by default; `max_depth` per source caps traversal |
| Model mismatch edge case | Startup check via ChromaDB collection metadata; abort with remediation instructions |
| SharePoint token caching | No caching in v1; device flow re-authenticates each run (known limitation) |
