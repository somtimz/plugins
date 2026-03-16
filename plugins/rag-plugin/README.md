# RAG Plugin

A Claude Code plugin that ingests documents into a ChromaDB vector store for Retrieval-Augmented Generation (RAG). Supports local files and directories, incremental re-ingestion, and a persistent document registry.

## Features

- Ingest `.txt`, `.md`, `.pdf`, and `.docx` files
- Chunked embedding via any OpenAI-compatible API
- Incremental re-ingestion — only new or changed files are re-embedded
- SQLite document registry tracking chunk counts, versions, and timestamps
- Structured logging to `.rag-pipeline.log`
- Model mismatch detection on startup

## Requirements

- Python 3.11+
- An OpenAI-compatible embeddings API (OpenAI, Azure OpenAI, Ollama, etc.)

## Installation

**1. Clone the repository**

```bash
git clone <repo-url>
cd RAG-plugin
```

**2. Create a virtual environment and install dependencies**

```bash
python3 -m venv .venv
.venv/bin/pip install openai chromadb pypdf python-docx flask tomli-w
```

## Configuration

**1. Copy the example config**

```bash
cp .rag-plugin.toml.example .rag-plugin.toml
```

**2. Edit `.rag-plugin.toml`**

```toml
[embedding]
provider = "openai-compatible"
model = "text-embedding-3-small"
api_base = "https://api.openai.com/v1"
api_key_env = "RAG_EMBEDDING_API_KEY"   # name of your API key env var

[vector_store]
provider = "chroma"
path = ".rag-store"
collection = "documents"

[pipeline]
chunk_size = 1000
chunk_overlap = 200
supported_formats = ["txt", "md", "pdf", "docx"]

[[sources]]
name = "my-docs"
type = "local"
path = "./docs"
```

For **Ollama**, change the embedding section:

```toml
[embedding]
provider = "openai-compatible"
model = "nomic-embed-text"
api_base = "http://localhost:11434/v1"
api_key_env = "RAG_EMBEDDING_API_KEY"   # set to any non-empty value
```

**3. Export your API key**

```bash
export RAG_EMBEDDING_API_KEY="sk-..."
# For Ollama or keyless providers:
export RAG_EMBEDDING_API_KEY="local"
```

## Web UI

A browser-based interface for running ingestion, browsing the document registry, and editing config.

**Start the server:**

```bash
.venv/bin/python scripts/ui.py
```

Then open **http://localhost:7842** in your browser.

The UI provides three tabs:

- **Ingestion** — trigger a pipeline run and watch live SSE progress events; view run history
- **Registry** — search and sort all ingested documents with chunk/version counts
- **Config** — view and edit pipeline configuration; saved back to `.rag-plugin.toml`

The server is single-user and binds to `0.0.0.0:7842` (port fixed per FR-012).

## Usage

**Ingest all sources defined in config:**

```bash
.venv/bin/python scripts/ingest.py
```

**Ingest a specific file or directory (overrides `[[sources]]`):**

```bash
.venv/bin/python scripts/ingest.py --source ./docs/
.venv/bin/python scripts/ingest.py --source ./report.pdf
```

**Use a custom config path:**

```bash
.venv/bin/python scripts/ingest.py --config /path/to/config.toml
```

### Example output

```
RAG Ingestion Pipeline — Complete
==================================
Config      : .rag-plugin.toml
Started     : 2026-03-15T10:00:00
Completed   : 2026-03-15T10:00:07

Source: my-docs (local: ./docs)
  Discovered : 5  |  Succeeded : 4  |  Skipped : 1  |  Failed : 0
  Skipped (unchanged) : 1   ← same hash, already in registry

─────────────────────────────────────────
Total discovered : 5
  Succeeded      : 4
  Skipped        : 1
  Failed         : 0
```

## Using as an LLM Tool

`scripts/lib/ingest_tool.py` exposes the pipeline as a callable tool compatible with both the Claude API and OpenAI API.

### Tool schema

```python
from scripts.lib.ingest_tool import CLAUDE_TOOL, OPENAI_TOOL
```

- `CLAUDE_TOOL` — for the Anthropic SDK (`tools` list in `client.messages.create`)
- `OPENAI_TOOL` — for the OpenAI SDK (`tools` list in `client.chat.completions.create`)

### Handling a tool call

```python
from scripts.lib.ingest_tool import handle_tool_call

# When the model returns a tool_use / function call:
result = handle_tool_call(tool_input)
# Returns a dict with: discovered, succeeded, skipped, failed, failed_docs, duration_seconds
```

### Tool parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source` | string | yes | File or directory path to ingest |
| `config_path` | string | no | Path to TOML config (default: `.rag-plugin.toml`) |
| `chunk_size` | integer | no | Token chunk size (overrides config) |
| `chunk_overlap` | integer | no | Token overlap between chunks (overrides config) |
| `embedding_model` | string | no | OpenAI embedding model name (overrides config) |
| `collection_name` | string | no | ChromaDB collection to write into (overrides config) |
| `supported_formats` | string[] | no | File extensions to include, e.g. `[".pdf", ".docx"]` |
| `max_file_size_mb` | integer | no | Skip files larger than this in MB (overrides config) |

Only `source` is required — all other parameters fall back to config file defaults.

### Claude API example

```python
import anthropic
from scripts.lib.ingest_tool import CLAUDE_TOOL, handle_tool_call

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=1024,
    tools=[CLAUDE_TOOL],
    messages=[{"role": "user", "content": "Ingest the docs/ folder using chunk size 500."}],
)

for block in response.content:
    if block.type == "tool_use" and block.name == "ingest_documents":
        result = handle_tool_call(block.input)
        print(result)
```

### OpenAI API example

```python
from openai import OpenAI
from scripts.lib.ingest_tool import OPENAI_TOOL, handle_tool_call
import json

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    tools=[OPENAI_TOOL],
    messages=[{"role": "user", "content": "Ingest the docs/ folder using chunk size 500."}],
)

tool_call = response.choices[0].message.tool_calls[0]
result = handle_tool_call(json.loads(tool_call.function.arguments))
print(result)
```

## Incremental Re-ingestion

Re-running the pipeline skips unchanged documents. Only new or modified files are re-embedded. Changed files have their old embeddings deleted before re-ingestion — no stale chunks remain.

## Document Registry

Every ingested document is recorded in `.rag-registry.db`. Inspect it with the SQLite CLI:

```bash
sqlite3 .rag-registry.db \
  "SELECT source_name, origin_path, chunk_count, version_count, last_ingested FROM documents;"
```

## Troubleshooting

| Symptom | Fix |
|---------|-----|
| `Configuration file not found` | Create `.rag-plugin.toml` from the example |
| `Environment variable ... is not set` | Export your API key env var |
| `Embedding model mismatch` | Delete `.rag-store/` and `.rag-registry.db`, then re-run |
| File skipped with size error | Increase `max_file_size_mb` in config or split the file |
| All docs skipped on first run | Delete `.rag-store/` to force full re-ingestion |

## Running Tests

```bash
.venv/bin/pip install pytest pytest-cov
.venv/bin/python -m pytest tests/
```
