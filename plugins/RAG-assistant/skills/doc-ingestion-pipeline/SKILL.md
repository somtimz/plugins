---
name: Document Ingestion Pipeline
description: >
  Use this skill when the user wants to ingest, embed, or index documents into a vector
  store for RAG (Retrieval-Augmented Generation). Activates when the user mentions:
  ingesting documents, embedding files, loading a corpus, populating the vector store,
  setting up a pipeline, tracking documents in the registry, viewing document statistics,
  or configuring a SharePoint source. Also activates for incremental re-ingestion,
  registry inspection, or troubleshooting the document pipeline.

  Do NOT activate for: querying the vector store, answering questions from documents,
  or any retrieval/search task (use the rag-chat skill for those).
---

## Document Ingestion Pipeline Skill

This skill guides you through ingesting documents from local filesystem or SharePoint
Online sources into a ChromaDB vector store, with automatic deduplication, structured
logging, and a persistent document registry.

---

### Quick start

**1. Ensure `.rag-plugin.toml` exists** in your project root. If not, create it:

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

[[sources]]
name = "local-docs"
type = "local"
path = "./docs"
```

**2. Set your embedding API key:**
```bash
export RAG_EMBEDDING_API_KEY="sk-..."
```

**3. Run the pipeline** (from the project root):
```bash
# Ingest all configured sources
python3 scripts/ingest.py

# Or ingest a specific path (overrides [[sources]])
python3 scripts/ingest.py --source ./docs/
```

---

### Supported document formats

| Format | Notes |
|--------|-------|
| `.txt` | Plain text, UTF-8 |
| `.md` | Markdown, UTF-8 |
| `.pdf` | Selectable text only; scanned PDFs are skipped |
| `.docx` | Office Open XML; legacy `.doc` is not supported |

Files larger than `max_file_size_mb` (default: 100 MB) are skipped with a clear message.

---

### Incremental re-ingestion

Re-running the pipeline on an unchanged document set skips all documents (< 10% of
initial run time). Only new or modified documents are processed. Changed documents have
their old embeddings deleted before re-ingestion — no stale chunks remain.

```bash
python3 scripts/ingest.py
```

---

### Document registry

Every successfully ingested document is recorded in `.rag-registry.db`. Inspect it:

```bash
sqlite3 .rag-registry.db \
  "SELECT source_name, origin_path, chunk_count, version_count, last_ingested FROM documents;"
```

---

### SharePoint source

Add a SharePoint source to `.rag-plugin.toml`:

```toml
[[sources]]
name = "sharepoint-docs"
type = "sharepoint"
site_url = "https://mycompany.sharepoint.com/sites/mysite"
folder = "/Shared Documents"
auth_type = "device_flow"          # or "client_credentials"
tenant_id_env = "SP_TENANT_ID"
client_id_env = "SP_CLIENT_ID"
# max_depth = 2                    # optional: limit subfolder depth
```

Export credentials before running:
```bash
export SP_TENANT_ID="your-tenant-id"
export SP_CLIENT_ID="your-client-id"
# export SP_CLIENT_SECRET="..."    # only for client_credentials
```

> **Note**: Device flow re-authenticates on every run in v1 (token caching not yet supported).
> Use `client_credentials` for unattended/automated runs.

---

### Troubleshooting

| Symptom | Fix |
|---------|-----|
| `ConfigError: Environment variable ... is not set` | Export the required env var |
| `ModelMismatchError` on startup | Delete `.rag-store/` and `.rag-registry.db`, then re-run |
| File skipped with size error | Increase `max_file_size_mb` in config or split the file |
| All docs skipped on first run | Delete `.rag-store/` to force full re-ingestion |
| SharePoint prompts for auth every run | Use `client_credentials` auth type |

See `quickstart.md` for the full setup guide.
