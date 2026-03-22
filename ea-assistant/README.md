# EA Assistant

A Claude Code plugin for managing Enterprise Architecture engagements from start to finish.

## Overview

EA Assistant supports the full EA engagement lifecycle using **TOGAF 10** as the process backbone, **Zachman** as the classification framework, and **ArchiMate 3.x** as the notation language. It manages multiple concurrent engagements, generates and reviews artifacts, facilitates stakeholder interviews, and produces consolidated architecture reports.

## Platform Support

EA Assistant works on both **Windows** and **Ubuntu Linux** (including WSL). All plugin components — commands, skills, agents, and Python scripts — use cross-platform paths and standard libraries.

## Features

- **Multi-engagement management** — create, open, track, edit, archive, and delete EA projects
- **Full ADM lifecycle** — start, edit, or resume any TOGAF ADM phase (Prelim, A–H)
- **Architecture Requirements** — manage requirements locally with a reference to a shared requirements repository
- **Artifact generation** — all TOGAF artifacts from templates, guided by interviews
- **Format export** — generate Word (.docx), PowerPoint (.pptx), and Mermaid diagrams from any artifact
- **Phase interviews** — curated question bank for each ADM phase (Text, Web, or Display mode) with output routing to artifacts
- **Brainstorming** — capture freeform thoughts before or during interviews; surfaced automatically as context during Q&A
- **Requirements analysis** — extract structured requirements from uploaded documents, map to ADM phases and Zachman cells
- **Stakeholder interviews** — chat-based or interactive web form; dated and versioned notes
- **Diagram support** — Mermaid, Graphviz (.dot), Draw.io (.drawio), ArchiMate notation
- **Review & consistency** — per-artifact review workflow; cross-artifact consistency checking
- **Consolidated reporting** — merge all artifacts into a single Markdown or Word document
- **Document ingestion** — upload existing docs and diagrams to inform artifacts
- **ADM reference material** — detailed phase inputs/outputs, tailoring guidance for agile/programme/capability-based contexts

## Prerequisites

- Claude Code with plugin support
- `pandoc` (for Word document export)
  - **Linux/macOS:** `brew install pandoc` or `apt install pandoc`
  - **Windows:** `winget install pandoc` or download from [pandoc.org](https://pandoc.org/installing.html)
- Python 3.11+ with `python-docx` and `python-pptx` packages (for `/ea-generate` Word/PPTX export)
  - **Linux/macOS:** `pip3 install python-docx python-pptx`
  - **Windows:** `pip install python-docx python-pptx`

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
| `/ea-new` | Create a new EA engagement with guided setup, engagement type selection, domain scoping, and Preliminary phase scaffolding |
| `/ea-open` | Open an engagement with full details, edit metadata/phases/artifacts, archive or delete |
| `/ea-status` | Portfolio dashboard with type, domains, phase progress, artifact counts, and archive management |
| `/ea-phase [phase]` | Start, edit, or resume an ADM phase |
| `/ea-artifact [action]` | Create or list artifacts for the active engagement |
| `/ea-brainstorm [phase]` | Capture freeform thoughts and context before or during interviews |
| `/ea-interview [mode]` | Start or resume a stakeholder interview (artifact or phase mode; Text/Web/Display) |
| `/ea-generate [artifact] [format]` | Export an artifact as Word (.docx), PowerPoint (.pptx), or Mermaid diagram |
| `/ea-review [artifact]` | Open an artifact for review and assessment |
| `/ea-requirements [action]` | Manage architecture requirements |
| `/ea-publish` | Merge all artifacts into a consolidated document |
| `/ea-help` | Getting-started guide and full command reference |

## Engagement Management

After creating an engagement, use `/ea-open` to:

- **View full details** — metadata, phase-by-phase progress, artifact list
- **Edit metadata** — update name, description, sponsor, dates, status (Active/On Hold/Planning/Completed)
- **Edit phase status** — manually advance or adjust any ADM phase with automatic timestamp tracking
- **Edit artifact status** — update artifact and review status without opening files
- **Archive** — move completed engagements to `.archive/` to declutter your portfolio
- **Delete** — permanently remove engagements (requires slug confirmation)

Use `/ea-status` for a portfolio-level dashboard showing all engagements with type, domains, progress, and artifact counts.

## Project Storage

All engagement data is stored in `EA-projects/` relative to your working directory:

```
EA-projects/
├── engagement-name/
│   ├── engagement.json       # metadata, ADM phase, settings
│   ├── requirements/         # local architecture requirements
│   ├── artifacts/            # generated artifacts + review files
│   ├── diagrams/             # Mermaid, Graphviz, Draw.io files
│   ├── uploads/              # source documents and diagrams
│   └── interviews/           # dated, versioned interview notes
└── .archive/                 # archived engagements (hidden)
    └── old-engagement/
        └── engagement.json
```

## Artifact Content Policy

> **Important:** Artifacts are populated from user interviews, uploaded documents, and explicit input — not arbitrary AI-generated content. Any AI-suggested content is clearly marked with `🤖 AI Draft — Review required`. Unanswered fields are marked `⚠️ Not answered`. N/A fields are marked `➖ Not applicable`.

## Frameworks Supported

- **TOGAF 10** — ADM process backbone
- **Zachman Framework** — full 6×6 classification
- **ArchiMate 3.x** — architecture notation and modelling

## License

[MIT](./LICENSE)
