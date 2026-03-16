# Contract: Configuration File Schema

**Feature**: 001-doc-ingestion-pipeline
**Contract type**: Configuration file
**File**: `.rag-plugin.toml` (at project root)

## Purpose

This file is the single source of truth for the ingestion pipeline's runtime behaviour.
It MUST exist at the project root before the pipeline can run. The pipeline reads it on
startup and fails immediately with a clear error if it is missing or invalid.

## Schema

```toml
[embedding]
# Required. Only "openai-compatible" is supported in the initial version.
provider = "openai-compatible"

# Required. Model name passed to the embedding API.
model = "text-embedding-3-small"

# Required. Base URL of the OpenAI-compatible embeddings endpoint.
api_base = "https://api.openai.com/v1"

# Required. Env var name holding the API key. Set to "DUMMY" for keyless providers.
api_key_env = "RAG_EMBEDDING_API_KEY"

[vector_store]
# Required. Only "chroma" is supported in the initial version.
provider = "chroma"

# Required. Filesystem path for ChromaDB data. Created automatically on first run.
path = ".rag-store"

# Required. ChromaDB collection name.
collection = "documents"

[pipeline]
# Optional. Characters per chunk. Default: 1000.
chunk_size = 1000

# Optional. Overlap between consecutive chunks. Default: 200. MUST be < chunk_size.
chunk_overlap = 200

# Optional. File extensions to process. Default: all four supported formats.
supported_formats = ["txt", "md", "pdf", "docx"]

# Optional. Path for the document registry SQLite database. Default: ".rag-registry.db".
registry_path = ".rag-registry.db"

# Optional. Path for the pipeline log file. Default: ".rag-pipeline.log".
log_path = ".rag-pipeline.log"

# Optional. Maximum file size in MB. Files exceeding this are skipped. Default: 100.
max_file_size_mb = 100

# ── Sources ──────────────────────────────────────────────────────────────────
# At least one [[sources]] entry is required when --source is not passed on CLI.
# Multiple entries are processed in order.

# Local filesystem source
[[sources]]
name = "local-docs"         # Required. Unique identifier used in run summary.
type = "local"              # Required. "local" or "sharepoint".
path = "./docs"             # Required for local. File or directory path.

# SharePoint source — device code flow (interactive, recommended for Claude Code sessions)
[[sources]]
name = "sharepoint-reports"
type = "sharepoint"
site_url = "https://mycompany.sharepoint.com/sites/mysite"  # Required.
folder = "/Shared Documents/Reports"                         # Required.
auth_type = "device_flow"    # Required. "device_flow" or "client_credentials".
max_depth = 2               # Optional. Max subfolder recursion depth. Default: unlimited (0 or omit).
tenant_id_env = "SP_TENANT_ID"    # Required. Env var for Azure AD tenant ID.
client_id_env = "SP_CLIENT_ID"    # Required. Env var for Azure AD app client ID.

# SharePoint source — client credentials (headless, for automation/CI)
[[sources]]
name = "sharepoint-policies"
type = "sharepoint"
site_url = "https://mycompany.sharepoint.com/sites/mysite"
folder = "/Shared Documents/Policies"
auth_type = "client_credentials"
tenant_id_env = "SP_TENANT_ID"
client_id_env = "SP_CLIENT_ID"
client_secret_env = "SP_CLIENT_SECRET"  # Required for client_credentials only.
```

## Validation Rules

| Field | Rule | Error if violated |
|-------|------|-------------------|
| `embedding.provider` | MUST equal `"openai-compatible"` | "Unsupported embedding provider: {value}" |
| `embedding.model` | MUST be non-empty string | "embedding.model is required" |
| `embedding.api_base` | MUST be valid https:// or http:// URL | "embedding.api_base must be a valid URL" |
| `embedding.api_key_env` | MUST be non-empty; referenced env var MUST be set | "Environment variable {api_key_env} is not set" |
| `vector_store.provider` | MUST equal `"chroma"` | "Unsupported vector_store provider: {value}" |
| `vector_store.collection` | MUST be non-empty string | "vector_store.collection is required" |
| `pipeline.chunk_overlap` | MUST be less than `pipeline.chunk_size` | "chunk_overlap must be less than chunk_size" |
| `pipeline.max_file_size_mb` | MUST be a positive integer if present | "max_file_size_mb must be a positive integer" |
| `sources[*].max_depth` | MUST be a non-negative integer if present; `0` means unlimited | "max_depth must be a non-negative integer" |
| `[[sources]]` | MUST have ≥ 1 entry when `--source` not on CLI | "No sources configured. Add [[sources]] to config or pass --source." |
| `sources[*].name` | MUST be unique across all sources | "Duplicate source name: {name}" |
| `sources[*].type` | MUST be `"local"` or `"sharepoint"` | "Unsupported source type: {value}" |
| `local` source | `path` MUST be present | "sources[{name}].path is required for local sources" |
| `sharepoint` source | `site_url`, `folder`, `auth_type`, `tenant_id_env`, `client_id_env` MUST be present | "sources[{name}].{field} is required for sharepoint sources" |
| `client_credentials` | `client_secret_env` MUST be present and env var set | "sources[{name}].client_secret_env required for client_credentials auth" |

## Versioning

The config schema is not versioned in the initial release. A `schema_version` field
will be introduced when breaking changes are needed. Pipelines MUST fail with a clear
error if an unrecognised top-level section is present (forward-compatibility guard).
