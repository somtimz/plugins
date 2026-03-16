# RAG-plugin Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-03-15

## Active Technologies
- Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill) + `openai` (embedding API client), `chromadb` (local vector store), `tomllib` (stdlib, config parsing), `pypdf` (PDF text extraction), `python-docx` (Word .docx extraction) (001-doc-ingestion-pipeline)
- ChromaDB local filesystem store (path configured in `.rag-plugin.toml`) (001-doc-ingestion-pipeline)
- Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill) + `openai` (embeddings), `chromadb` (vector store), `tomllib` (config), `pypdf` (PDF), `python-docx` (Word), `Office365-REST-Python-Client` (SharePoint), `msal` (SharePoint OAuth2 — transitive via Office365 lib) (001-doc-ingestion-pipeline)
- Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill) + `openai`, `chromadb`, `tomllib` (stdlib), `pypdf`, `python-docx`, `Office365-REST-Python-Client`, `msal` (transitive), `sqlite3` (stdlib) (001-doc-ingestion-pipeline)
- ChromaDB local filesystem store; SQLite document registry (`.rag-registry.db`) (001-doc-ingestion-pipeline)
- Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill) + `openai`, `chromadb`, `tomllib` (stdlib), `pypdf`, `python-docx`, `Office365-REST-Python-Client`, `msal` (transitive), `sqlite3` (stdlib), `logging` (stdlib) (001-doc-ingestion-pipeline)
- ChromaDB local filesystem store; SQLite document registry (`.rag-registry.db`); log file (`.rag-pipeline.log`) (001-doc-ingestion-pipeline)

- Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill) + `openai` (embedding API client), `chromadb` (local vector store), `tomllib` (stdlib, config parsing) (001-doc-ingestion-pipeline)

## Project Structure

```text
src/
tests/
```

## Commands

cd src [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] pytest [ONLY COMMANDS FOR ACTIVE TECHNOLOGIES][ONLY COMMANDS FOR ACTIVE TECHNOLOGIES] ruff check .

## Code Style

Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill): Follow standard conventions

## Recent Changes
- 001-doc-ingestion-pipeline: Added Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill) + `openai`, `chromadb`, `tomllib` (stdlib), `pypdf`, `python-docx`, `Office365-REST-Python-Client`, `msal` (transitive), `sqlite3` (stdlib), `logging` (stdlib)
- 001-doc-ingestion-pipeline: Added Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill) + `openai`, `chromadb`, `tomllib` (stdlib), `pypdf`, `python-docx`, `Office365-REST-Python-Client`, `msal` (transitive), `sqlite3` (stdlib)
- 001-doc-ingestion-pipeline: Added Python 3.11+ (pipeline scripts); Markdown + YAML frontmatter (skill) + `openai` (embeddings), `chromadb` (vector store), `tomllib` (config), `pypdf` (PDF), `python-docx` (Word), `Office365-REST-Python-Client` (SharePoint), `msal` (SharePoint OAuth2 — transitive via Office365 lib)


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
