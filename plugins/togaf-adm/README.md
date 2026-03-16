# togaf-adm

A Claude Code plugin for enterprise architects and technical stakeholders to develop TOGAF 10 ADM-compliant architecture artifacts through guided interviews, document analysis, and structured deliverable generation.

## Features

- **ADM Phase Guidance** — Step-by-step facilitation through all 9 ADM phases + Requirements Management
- **Stakeholder Interviews** — Structured question sets per phase, with auto-mapping to artifact fields
- **Document Ingestion** — Load existing strategy docs, requirements specs, and architecture documents
- **Artifact Generation** — 9 priority TOGAF artifacts as Mermaid diagrams, Word documents, and PowerPoint slides
- **Session Persistence** — Project context retained across sessions via `.claude/togaf-adm.local.md`

## Commands

| Command | Description |
|---------|-------------|
| `/togaf:phase [phase]` | Start or continue an ADM phase interactively |
| `/togaf:generate [artifact]` | Generate a TOGAF artifact |
| `/togaf:load [file]` | Ingest a document as architecture input |
| `/togaf:status` | View project progress dashboard |
| `/togaf:export [format]` | Export artifact as word, powerpoint, or mermaid |

## Agents

| Agent | Role |
|-------|------|
| `adm-guide` | Interactive ADM phase facilitator |
| `artifact-generator` | Produces formatted TOGAF deliverables |
| `requirements-analyst` | Extracts and maps requirements from documents |

## Prerequisites

```bash
pip3 install python-docx python-pptx
```

For `.docx` document loading:
```bash
pip3 install python-docx
```

## Quick Start

1. **Set up your project:**
   ```
   /togaf:phase preliminary
   ```

2. **Work through a phase:**
   ```
   /togaf:phase a
   ```

3. **Generate an artifact:**
   ```
   /togaf:generate vision
   ```

4. **Export as Word:**
   ```
   /togaf:export word
   ```

5. **Load an existing document:**
   ```
   /togaf:load requirements.md
   ```

## Project Context File

The plugin stores project state in `.claude/togaf-adm.local.md`. Copy `togaf-adm.local.md.example` to `.claude/togaf-adm.local.md` and edit the frontmatter to set your project metadata.

## Supported Artifacts

| Artifact | Phase | Formats |
|----------|-------|---------|
| Architecture Vision Document | A | Word, PowerPoint |
| Stakeholder Map | A | Mermaid, Word, PowerPoint |
| Business Capability Map | B | Mermaid |
| Process Flow Diagram | B | Mermaid |
| Application Portfolio Catalog | C | Word (table) |
| Technology Landscape | D | Mermaid (C4) |
| Gap Analysis | B/C/D | Word (table), PowerPoint |
| Architecture Roadmap | F | Mermaid (Gantt), PowerPoint |
| Requirements Register | All | Word (table) |

## Skills Reference

The plugin includes four auto-activating skills:
- `togaf-adm-phases` — ADM phase knowledge and phase map
- `togaf-artifacts` — Artifact structures and generation patterns
- `togaf-interview-techniques` — Stakeholder interview question sets
- `togaf-generation` — Word, PowerPoint, and Mermaid generation guide
