# RAG-assistant

A Claude Code plugin that ingests documents into a ChromaDB vector store for Retrieval-Augmented Generation (RAG). Supports local files and directories, SharePoint Online, incremental re-ingestion, a persistent document registry, and a conversational web UI powered by Claude.

## Features

- Ingest `.txt`, `.md`, `.pdf`, and `.docx` files from local paths or SharePoint Online
- Chunked embedding via any OpenAI-compatible API
- Incremental re-ingestion — only new or changed files are re-embedded
- SQLite document registry tracking chunk counts, versions, and timestamps
- Structured logging to `.rag-pipeline.log`
- Model mismatch detection on startup
- Browser-based web UI with live ingestion progress, registry browser, and config editor
- Conversational chat UI — ask questions, trigger ingestion, and explore the registry in natural language via Claude

## Requirements

- Python 3.11+
- An OpenAI-compatible embeddings API (OpenAI, Azure OpenAI, Ollama, etc.)

## Installation

**1. Clone the repository**

```bash
git clone <repo-url>
cd RAG-assistant
```

**2. Create a virtual environment and install dependencies**

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Configuration

**1. Create `.rag-plugin.toml`** in the project root

**2. Edit `.rag-plugin.toml`**

```toml
[embedding]
provider = "openai-compatible"
model = "text-embedding-3-small"
api_base = "https://api.openai.com/v1"
embedding_key_env = "RAG_EMBEDDING_API_KEY"   # name of your API key env var

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
embedding_key_env = "RAG_EMBEDDING_API_KEY"   # set to any non-empty value
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

The UI provides four tabs:

- **Ingestion** — trigger a pipeline run and watch live SSE progress events; view run history
- **Registry** — search and sort all ingested documents with chunk/version counts
- **Config** — view and edit pipeline configuration; saved back to `.rag-plugin.toml`
- **Chat** — conversational RAG interface (see below)

The server is single-user and binds to `0.0.0.0:7842` (port fixed per FR-012).

### Chat Tab

The Chat tab provides a natural language interface for RAG Q&A, document ingestion, and registry exploration powered by the Anthropic Claude API.

**Requirements:**

Set the `ANTHROPIC_API_KEY` environment variable before starting the server:

```bash
export ANTHROPIC_API_KEY=sk-ant-...
.venv/bin/python scripts/ui.py
```

**Usage examples:**

```
Ask a question:    "What does the onboarding policy say about remote work?"
Ingest documents:  "ingest ./docs"  or  "add ./reports to the knowledge base"
List documents:    "what documents do you know about?"
```

The Chat tab streams responses progressively. Ctrl+Enter submits a message.

**Transparent Search** — When the assistant retrieves documents to answer a question, a chunk panel appears above the answer showing:

- Numbered chunk cards (`[1]`, `[2]`, ...) with source name, file path, similarity score (3 decimal places), and a 300-character excerpt
- "Show full text" toggle on each card to expand the complete chunk
- "(file no longer on disk)" indicator when the source file has been moved or deleted

The assistant's answer uses inline citations (e.g. `[1]`, `[2]`) matching the chunk numbers. An "Inspect prompt" panel beneath each answer lets you expand and copy the exact augmented prompt sent to the LLM, including the system instruction, all numbered context entries, and your original question.

**Optional `[llm]` config section** in `.rag-plugin.toml`:

```toml
[llm]
model = "claude-sonnet-4-6"    # default
llm_key_env = "ANTHROPIC_API_KEY"  # env var name for the API key
```

Conversation history is maintained in the browser for the current session (up to 10 turns). History is lost on page reload.

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
.venv/bin/python -m pytest tests/
```
