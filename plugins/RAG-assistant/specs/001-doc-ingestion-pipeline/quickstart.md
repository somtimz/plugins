# Quickstart: Document Ingestion Pipeline Skill

**Feature**: 001-doc-ingestion-pipeline
**Audience**: Developer setting up and running the pipeline for the first time

## Prerequisites

Before running the pipeline:

1. **Python 3.11+** installed and on your PATH
2. **Plugin dependencies** installed:
   ```bash
   pip install openai chromadb pypdf python-docx Office365-REST-Python-Client
   ```
   *(`Office365-REST-Python-Client` is only required if you use SharePoint sources)*
3. **Embedding API key** set as an environment variable (default name: `RAG_EMBEDDING_API_KEY`):
   ```bash
   export RAG_EMBEDDING_API_KEY="sk-..."
   ```
   For local providers that don't require a key, set it to any non-empty value:
   ```bash
   export RAG_EMBEDDING_API_KEY="local"
   ```

## Step 1: Create your configuration file

Create `.rag-plugin.toml` in your project root:

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
supported_formats = ["txt", "md", "pdf", "docx"]
# log_path = ".rag-pipeline.log"   # optional, this is the default
# max_file_size_mb = 100           # optional, this is the default
```

**For a local Ollama provider**, change the embedding section:
```toml
[embedding]
provider = "openai-compatible"
model = "nomic-embed-text"
api_base = "http://localhost:11434/v1"
api_key_env = "RAG_EMBEDDING_API_KEY"  # set to "local" or any value
```

## Step 1b: Add a SharePoint source (optional)

If you want to ingest from SharePoint, you need an Azure AD app registration first:

1. In the Azure Portal, register an app and note the **Tenant ID** and **Client ID**
2. Grant it `Sites.Read.All` (application permission) in Microsoft Graph
3. For `client_credentials` auth: create a client secret and note the value
4. Export credentials as environment variables:
   ```bash
   export SP_TENANT_ID="your-tenant-id"
   export SP_CLIENT_ID="your-client-id"
   export SP_CLIENT_SECRET="your-client-secret"  # only for client_credentials
   ```
5. Add a `[[sources]]` block to `.rag-plugin.toml`:
   ```toml
   [[sources]]
   name = "sharepoint-docs"
   type = "sharepoint"
   site_url = "https://mycompany.sharepoint.com/sites/mysite"
   folder = "/Shared Documents"
   auth_type = "device_flow"
   tenant_id_env = "SP_TENANT_ID"
   client_id_env = "SP_CLIENT_ID"
   # max_depth = 2   # optional: limit subfolder traversal depth; omit for unlimited
   ```
   For `device_flow`, the pipeline will print a URL and code **on every run** — tokens
   are not cached between runs in v1. Open the URL in your browser, enter the code, and
   sign in when prompted.

## Step 2: Ingest your documents

### Using config-defined sources (normal usage)
```bash
python "$CLAUDE_PLUGIN_ROOT/scripts/ingest.py"
```

### One-off override with a local path (ignores [[sources]] in config)
```bash
python "$CLAUDE_PLUGIN_ROOT/scripts/ingest.py" --source ./docs/
```

## Step 3: Verify ingestion

The pipeline prints a completion summary to stdout. Check that `Succeeded` matches the
number of documents you expected:

```
RAG Ingestion Pipeline — Complete
==================================
Documents discovered : 5
  Succeeded          : 5
  Skipped            : 0
  Failed             : 0
```

The vector store is now populated at the path configured in `.rag-plugin.toml`
(default: `.rag-store/`). A document registry is also created at `.rag-registry.db`,
which tracks every ingested document with its statistics. You can inspect it with any
SQLite browser, or with the sqlite3 CLI:

```bash
sqlite3 .rag-registry.db "SELECT source_name, origin_path, chunk_count, version_count, last_ingested FROM documents;"
```

## Step 4: Re-ingestion (incremental)

Run the same command again after adding or modifying documents. Only changed and new
documents are processed:

```bash
python "$CLAUDE_PLUGIN_ROOT/scripts/ingest.py" --source ./docs/
```

```
Documents discovered : 5
  Succeeded          : 1   ← only the changed/new document
  Skipped (unchanged): 4
  Failed             : 0
```

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| `Configuration file not found` | `.rag-plugin.toml` missing | Create it per Step 1 |
| `Environment variable RAG_EMBEDDING_API_KEY is not set` | API key not exported | Run `export RAG_EMBEDDING_API_KEY="..."` |
| `AuthenticationError` from embedding API | Wrong or expired API key | Check key value and provider settings |
| `UnicodeDecodeError` on a file | File is not UTF-8 encoded | Convert file to UTF-8 or add to exclusions |
| All documents skipped on first run | Store already populated from a previous run | Delete `.rag-store/` to force full re-ingestion |
| `Embedding model mismatch` error | Config model changed after initial ingestion | Delete `.rag-store/` and `.rag-registry.db`, then re-run |
| Large file skipped with size error | File exceeds `max_file_size_mb` (default 100 MB) | Split the file, or increase `max_file_size_mb` in config |
| SharePoint prompts for auth every run | Token caching not supported in v1 | Use `client_credentials` auth for unattended/automated runs |
| `No sources configured` | No `[[sources]]` in config and no `--source` passed | Add a `[[sources]]` block or use `--source` |
| SharePoint `auth_failed` | Credentials missing or expired | Re-export SP env vars; re-run |
| SharePoint `unreachable` | Network error or wrong `site_url` | Check VPN/network; verify `site_url` |
| `Permission denied` on SharePoint folder | App lacks access to that folder | Grant `Sites.Read.All` in Azure Portal |

## Validation test

To confirm end-to-end ingestion works, create a test document and ingest it:

```bash
echo "The capital of France is Paris." > /tmp/test-rag.txt
python "$CLAUDE_PLUGIN_ROOT/scripts/ingest.py" --source /tmp/test-rag.txt
```

Expected output:
```
Documents discovered : 1
  Succeeded          : 1
```

If you see `Succeeded: 1`, the pipeline is working correctly.
