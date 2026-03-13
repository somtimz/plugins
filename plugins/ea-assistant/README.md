# EA Assistant

A Claude Code plugin for managing Enterprise Architecture engagements from start to finish.

## Overview

EA Assistant supports the full EA engagement lifecycle using **TOGAF 10** as the process backbone, **Zachman** as the classification framework, and **ArchiMate 3.x** as the notation language. It manages multiple concurrent engagements, generates and reviews artifacts, facilitates stakeholder interviews, and produces consolidated architecture reports.

## Features

- **Multi-engagement management** — create, open, and track multiple EA projects
- **Full ADM lifecycle** — start, edit, or resume any TOGAF ADM phase (Prelim, A–H)
- **Architecture Requirements** — manage requirements locally with a reference to a shared requirements repository
- **Artifact generation** — all TOGAF artifacts from templates, guided by interviews
- **Stakeholder interviews** — online or via Word export/import; dated and versioned notes
- **Diagram support** — Mermaid, Graphviz (.dot), Draw.io (.drawio), ArchiMate notation
- **Review & consistency** — per-artifact review workflow; cross-artifact consistency checking
- **Consolidated reporting** — merge all artifacts into a single Markdown or Word document
- **Document ingestion** — upload existing docs and diagrams to inform artifacts

## Prerequisites

- Claude Code with plugin support
- `pandoc` (for Word document export) — install via `brew install pandoc` or `apt install pandoc`

## Installation

```bash
/plugin install ea-assistant
```

## Configuration

Create `.claude/ea-assistant.local.md` in your project:

```
requirementsRepoPath: /path/to/shared/requirements-folder
```

> This path currently points to a local folder. SharePoint integration is planned for a future version.

## Commands

| Command | Description |
|---|---|
| `/ea-new` | Create a new EA engagement |
| `/ea-open` | Open or switch between engagements (picklist) |
| `/ea-status` | Dashboard of all engagements and their progress |
| `/ea-phase [phase]` | Start, edit, or resume an ADM phase |
| `/ea-artifact [action]` | Create or list artifacts for the active engagement |
| `/ea-interview [mode]` | Start, export, import, or resume a stakeholder interview |
| `/ea-review [artifact]` | Open an artifact for review and assessment |
| `/ea-requirements [action]` | Manage architecture requirements |
| `/ea-merge` | Merge all artifacts into a consolidated document |

## Project Storage

All engagement data is stored in `EA-projects/` relative to your working directory:

```
EA-projects/
└── engagement-name/
    ├── engagement.json       # metadata, ADM phase, settings
    ├── requirements/         # local architecture requirements
    ├── artifacts/            # generated artifacts + review files
    ├── diagrams/             # Mermaid, Graphviz, Draw.io files
    ├── uploads/              # source documents and diagrams
    └── interviews/           # dated, versioned interview notes
```

## Artifact Content Policy

> **Important:** Artifacts are populated from user interviews, uploaded documents, and explicit input — not arbitrary AI-generated content. Any AI-suggested content is clearly marked with `🤖 AI Draft — Review required`. Unanswered fields are marked `⚠️ Not answered`. N/A fields are marked `➖ Not applicable`.

## Frameworks Supported

- **TOGAF 10** — ADM process backbone
- **Zachman Framework** — full 6×6 classification
- **ArchiMate 3.x** — architecture notation and modelling

## License

MIT
