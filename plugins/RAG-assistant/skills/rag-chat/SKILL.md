---
name: RAG Chat
description: >
  Use this skill when the user wants to ask natural-language questions about their
  ingested documents, search the knowledge base, or interact with their document
  corpus conversationally. Activates when the user mentions: asking questions about
  documents, searching the knowledge base, "what do my docs say about...", "find
  information about...", chatting with documents, or getting cited answers from
  ingested content. Also activates when the user wants to explore the document
  registry conversationally ("what documents do I have?", "list files from source X")
  or trigger ingestion from the chat interface ("ingest this folder via chat").

  Do NOT activate for: running the ingestion pipeline directly (use the
  doc-ingestion-pipeline skill), or starting/configuring the web UI server.
---

## RAG Chat Skill

The chat interface provides conversational Q&A over ingested documents, powered by
Claude with three tools: semantic search, ingestion, and registry lookup.

---

### Prerequisites

**1. Documents ingested** — run the pipeline first (see doc-ingestion-pipeline skill).

**2. API keys set:**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."      # for chat (Claude)
export RAG_EMBEDDING_API_KEY="sk-..."      # for search (embeddings)
```

**3. Server running** (from project root):
```bash
python3 scripts/ui.py
```
Open **http://localhost:7842** → Chat tab.

---

### What Claude can do in chat

Claude has three tools available on every request:

| Tool | Triggered by |
|------|-------------|
| `search_knowledge_base` | Questions about document content |
| `ingest_documents` | "ingest ./path", "add X to knowledge base" |
| `query_registry` | "what documents do you have?", "list files from source X" |

Claude selects the right tool automatically — no commands needed.

---

### Example prompts

```
What does the onboarding policy say about remote work?
Summarise the key points from the Q1 report.
What documents do I have about SharePoint?
Ingest ./docs/new-policy.pdf
List all documents ingested from the hr-source.
```

---

### Transparent Search

When Claude retrieves documents, a **chunk panel** appears above the answer showing:

- Numbered chunk cards (`[1]`, `[2]`, ...) with source name, file path, similarity score (3 decimal places), and a 300-character excerpt
- "Show full text" toggle on each card to expand the complete chunk text
- "(file no longer on disk)" indicator when the source file has been moved or deleted
- "(N of 5 chunks available)" note when fewer than 5 chunks are returned

Claude's answer uses **inline citations** (e.g. `[1]`, `[2]`) matching the chunk numbers.

An **"Inspect prompt"** panel beneath each answer lets you expand and copy the exact
augmented prompt sent to the LLM — including the system instruction, all numbered
context entries, and the original question.

If the knowledge base is empty, an error message directs you to ingest documents first.
If no relevant content is found, Claude says so rather than fabricating an answer.

---

### Session behaviour

- Conversation history is kept in the browser for the current tab session (up to 10 turns).
- History is lost on page reload — this is intentional; each reload starts a fresh session.
- Messages over 4,000 characters are rejected before submission.

---

### Troubleshooting

| Symptom | Fix |
|---------|-----|
| Chat tab shows "API key not set" | Export `ANTHROPIC_API_KEY` and restart the server |
| "No relevant information found" | Run ingestion first; verify documents are in `.rag-registry.db` |
| Streaming cuts off mid-response | Reload the page and retry |
| Ingestion via chat blocked | Another pipeline run is already active; wait for it to finish |

### Configuring the LLM

Add an optional `[llm]` section to `.rag-plugin.toml` to change model or key env var:

```toml
[llm]
model = "claude-sonnet-4-6"       # default
llm_key_env = "ANTHROPIC_API_KEY" # default
```
