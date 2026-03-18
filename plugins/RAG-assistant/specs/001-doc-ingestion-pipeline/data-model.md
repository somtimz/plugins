# Data Model: Document Ingestion Pipeline Skill

**Feature**: 001-doc-ingestion-pipeline
**Date**: 2026-03-15

## Entities

### Document

Represents a source file submitted for ingestion.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `source_path` | string (absolute path) | Full filesystem path to the file | MUST be unique per pipeline run; MUST exist and be readable |
| `format` | enum: `txt`, `md`, `pdf`, `docx` | File format determined by extension | MUST be in supported formats list from config |
| `content` | string | Full extracted text content | MUST NOT be empty; empty files are skipped |
| `content_hash` | string (MD5 hex) | MD5 hash of raw file content | Used for change detection on incremental runs |
| `last_modified` | ISO 8601 datetime | File system last-modified timestamp | Informational; content_hash is authoritative for change detection |
| `file_size_bytes` | integer | File size in bytes | Informational |

**Format-specific extraction notes**:
- `txt`, `md`: Read as UTF-8 text directly
- `pdf`: Text extracted via `pypdf`; encrypted/password-protected PDFs → UNREADABLE;
  pages with no selectable text (scanned) → content treated as empty → EMPTY
- `docx`: Text extracted paragraph-by-paragraph via `python-docx`;
  legacy `.doc` files → UNREADABLE (format not supported)

**State transitions**:
```
DISCOVERED → READABLE → CHUNKED → EMBEDDED → STORED
           ↘ UNREADABLE (skip, report error: encrypted PDF, .doc format, corrupt file)
                       ↘ EMPTY (skip, report: empty file, scanned PDF with no text)
```

---

### Chunk

A sub-section of a Document produced when the document exceeds the embedding size limit.
A document with content within the chunk size limit produces exactly one chunk.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `chunk_id` | string | `{source_path}::chunk::{index}` | Globally unique within a pipeline run |
| `document_source_path` | string | Parent document's source path | Foreign reference to Document |
| `chunk_index` | integer (0-based) | Position of this chunk within the document | MUST be sequential, starting at 0 |
| `text` | string | Text content of this chunk | MUST NOT be empty |
| `char_start` | integer | Start character offset in the original document | Inclusive |
| `char_end` | integer | End character offset in the original document | Exclusive |

**Chunking rules**:
- Chunk size and overlap are read from config (`pipeline.chunk_size`, `pipeline.chunk_overlap`)
- Last chunk MAY be shorter than `chunk_size`
- Chunks overlap by `chunk_overlap` characters with the preceding chunk

---

### Embedding

The numerical vector representation of a Chunk's semantic content.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `chunk_id` | string | Reference to the parent Chunk | 1:1 with Chunk |
| `vector` | list of float | Embedding vector values | Dimension determined by the configured model |
| `model` | string | Embedding model identifier used | Read from config (`embedding.model`) |
| `created_at` | ISO 8601 datetime | Timestamp when embedding was generated | Set at generation time |

---

### VectorStoreEntry

The persisted record in ChromaDB combining chunk text, embedding, and retrieval metadata.
This is the queryable unit in the vector repository.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | string | Same as `chunk_id` | Primary key in the ChromaDB collection |
| `document` | string | Chunk text content | Used for retrieval result display |
| `embedding` | list of float | Embedding vector | Indexed for similarity search |
| `metadata.source_path` | string | Origin file path | Used for filtering and provenance |
| `metadata.chunk_index` | integer | Chunk position within document | Used for result ordering |
| `metadata.content_hash` | string | Parent document's MD5 hash | Used for incremental change detection |
| `metadata.ingested_at` | ISO 8601 datetime | Ingestion timestamp | Audit trail |
| `metadata.model` | string | Embedding model used | Stored in collection metadata; compared on startup to detect model mismatch (Decision 14) |

---

### DocumentRecord

A persistent record in the document registry (`.rag-registry.db`) tracking every
successfully ingested document. One row per unique `(source_name, origin_path)`.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `id` | integer (auto) | Surrogate primary key | Auto-incremented |
| `source_name` | string | Name of the source that provided this document | References a `[[sources]]` name |
| `origin_path` | string | Full path or SharePoint item URL | Together with `source_name`, globally unique |
| `content_hash` | string (MD5 hex) | Hash of the document content at last ingestion | Used for deduplication and change detection |
| `file_size_bytes` | integer | File size at last ingestion | Informational |
| `chunk_count` | integer | Number of chunks stored in the vector store | Updated on each successful ingestion |
| `version_count` | integer | How many times this document has been (re-)ingested | Starts at 1; increments on each re-ingestion |
| `first_ingested` | ISO 8601 datetime | Timestamp of original ingestion | Set once; never updated |
| `last_ingested` | ISO 8601 datetime | Timestamp of most recent ingestion | Updated on every successful re-ingestion |

**Deduplication logic** (per document during a pipeline run):
1. Compute `content_hash` of current document content
2. Look up `(source_name, origin_path)` in registry
3. If found AND `content_hash` matches → **SKIP** (already ingested, no changes)
4. If found AND `content_hash` differs → **DELETE** all ChromaDB entries for this doc,
   then re-embed, then update registry row (`content_hash`, `chunk_count`, `version_count += 1`, `last_ingested`)
5. If not found → **INSERT** new registry row after successful ingestion

**Within-run deduplication**: A seen-set of `content_hash` values is maintained per
pipeline run. If two sources yield a document with the same hash, the second is skipped
and reported as a duplicate.

---

### SourceConfig

A configured data source, defined as one entry in the `[[sources]]` array in
`.rag-plugin.toml`. Drives document discovery for each source type.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| `name` | string | Human-readable identifier for this source | MUST be unique across all sources in config; used in run summary |
| `type` | enum: `local`, `sharepoint` | Source type | MUST be `local` or `sharepoint` |
| `path` | string | *(local only)* Filesystem path to file or directory | MUST exist and be readable |
| `site_url` | string | *(sharepoint only)* SharePoint site URL | MUST be a valid HTTPS URL |
| `folder` | string | *(sharepoint only)* Relative folder path within the site | e.g., `/Shared Documents/Reports` |
| `auth_type` | enum: `device_flow`, `client_credentials` | *(sharepoint only)* Auth mode | MUST be set for SharePoint sources |
| `tenant_id_env` | string | *(sharepoint only)* Env var name for Azure AD tenant ID | Referenced env var MUST be set |
| `client_id_env` | string | *(sharepoint only)* Env var name for Azure AD client ID | Referenced env var MUST be set |
| `client_secret_env` | string | *(sharepoint, client_credentials only)* Env var name for client secret | Required when `auth_type = "client_credentials"` |
| `max_depth` | integer (optional) | *(sharepoint only)* Max subfolder traversal depth; `0` or omitted = unlimited | MUST be non-negative integer if present |

---

### PipelineRun

Represents a single execution of the ingestion pipeline. Held in memory during execution;
logged to stdout on completion. Results are broken down per source.

| Field | Type | Description |
|-------|------|-------------|
| `started_at` | ISO 8601 datetime | Pipeline start timestamp |
| `completed_at` | ISO 8601 datetime | Pipeline end timestamp |
| `sources_processed` | list of string | Names of sources attempted |
| `per_source` | list of `SourceResult` | Per-source breakdown (see below) |
| `total_discovered` | integer | Total documents found across all sources |
| `total_succeeded` | integer | Documents successfully ingested |
| `total_skipped` | integer | Documents skipped (unchanged or unsupported format) |
| `total_failed` | integer | Documents that failed with an error |

**SourceResult** (per-source summary within PipelineRun):

| Field | Type | Description |
|-------|------|-------------|
| `source_name` | string | Name of the source |
| `source_type` | string | `local` or `sharepoint` |
| `status` | enum: `ok`, `auth_failed`, `unreachable`, `partial` | Overall outcome for this source |
| `discovered` | integer | Documents found |
| `succeeded` | integer | Successfully ingested |
| `skipped` | integer | Skipped |
| `failed` | integer | Failed |
| `failures` | list of `{path, reason}` | Per-document failure details |

---

## Configuration Schema

The `.rag-plugin.toml` file at the project root drives all runtime decisions.
Sources are now defined as an array of tables.

```toml
[embedding]
provider = "openai-compatible"
model = "text-embedding-3-small"
api_base = "https://api.openai.com/v1"
embedding_key_env = "RAG_EMBEDDING_API_KEY"

[vector_store]
provider = "chroma"
path = ".rag-store"
collection = "documents"

[pipeline]
chunk_size = 1000
chunk_overlap = 200
supported_formats = ["txt", "md", "pdf", "docx"]
log_path = ".rag-pipeline.log"      # optional, default shown
max_file_size_mb = 100              # optional, default shown

# Local source example
[[sources]]
name = "local-docs"
type = "local"
path = "./docs"

# SharePoint source — device flow (interactive)
[[sources]]
name = "sharepoint-reports"
type = "sharepoint"
site_url = "https://mycompany.sharepoint.com/sites/mysite"
folder = "/Shared Documents/Reports"
auth_type = "device_flow"
tenant_id_env = "SP_TENANT_ID"
client_id_env = "SP_CLIENT_ID"

# SharePoint source — client credentials (headless)
[[sources]]
name = "sharepoint-policies"
type = "sharepoint"
site_url = "https://mycompany.sharepoint.com/sites/mysite"
folder = "/Shared Documents/Policies"
auth_type = "client_credentials"
tenant_id_env = "SP_TENANT_ID"
client_id_env = "SP_CLIENT_ID"
client_secret_env = "SP_CLIENT_SECRET"
```

**Validation rules**:
- `[[sources]]` MUST contain at least one entry (unless `--source` is passed on CLI)
- Each source `name` MUST be unique within the config
- `local` sources: `path` MUST be present
- `sharepoint` sources: `site_url`, `folder`, `auth_type`, `tenant_id_env`, `client_id_env` MUST be present
- `client_credentials` sources: `client_secret_env` MUST also be present
- `embedding.embedding_key_env` MUST be set and the referenced env var MUST be non-empty at runtime
- `pipeline.chunk_overlap` MUST be less than `pipeline.chunk_size`

---

## Entity Relationships

```text
.rag-plugin.toml
       │ configures
       ▼
PipelineRun
       │ processes 1..N
       ▼
   Document ──── content_hash (for change detection vs VectorStoreEntry.metadata)
       │ split into 1..N
       ▼
    Chunk
       │ embedded into 1
       ▼
  Embedding
       │ persisted as 1
       ▼
VectorStoreEntry  (lives in ChromaDB collection)
```
