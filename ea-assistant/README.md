# EA Assistant

A Claude Code plugin for managing Enterprise Architecture engagements from start to finish.

## Overview

EA Assistant supports the full EA engagement lifecycle using **TOGAF 10** as the process backbone, **Zachman** as the classification framework, and **ArchiMate 3.x** as the notation language. It manages multiple concurrent engagements, generates and reviews artifacts, facilitates stakeholder interviews, and produces consolidated architecture reports.

## Platform Support

EA Assistant works on both **Windows** and **Ubuntu Linux** (including WSL). All plugin components — commands, skills, agents, and Python scripts — use cross-platform paths and standard libraries.

## Features

- **Multi-engagement management** — create, open, track, edit, archive, and delete EA projects with engagement type classification (Greenfield/Brownfield/Assessment-only/Migration)
- **Full ADM lifecycle** — start, edit, or resume any TOGAF ADM phase (Prelim, A–H)
- **Motivation framework** — structured Business Drivers (DRV), Goals (G), Objectives (OBJ), Issues (ISS), and Problems (PRB) with ID-based traceability chains in the Architecture Vision (15 sections including Strategic Direction Summary with Strategies and Key Metrics)
- **Business Model Canvas** — Phase B BMC template (9 building blocks) with 27-question interview bank and linkage table to Business Architecture elements
- **Architecture Requirements** — manage requirements with Corporate (read-only, waiveable) and Project (editable) scope distinction; Motivation field links each requirement to its driver, issue, problem, goal, or objective
- **Artifact generation** — all TOGAF artifacts from templates, guided by interviews
- **Format export** — generate Word (.docx), PowerPoint (.pptx), and Mermaid diagrams from any artifact
- **Phase interviews** — curated question bank for each ADM phase (Text, Web, or Display mode) with output routing to artifacts; ID scheme reference and section markers for Phase A
- **Interview shortcuts** — single-key shortcuts for defaults, skip, N/A, opt-out, brainstorm, A3 logging, and governance transitions; type `?` at any prompt for contextual help
- **Contextual help** — type `?` during any interview to see the artifact's purpose, value, current progress, and a link to the EA concepts reference
- **EA concepts reference** — canonical definitions of Principle, Goal, Objective, Strategy, Plan, Risk, Issue, and Problem with TOGAF/ArchiMate alignment and common-confusion disambiguation
- **Cross-topic detection** — flags answers that belong in a different artifact and offers to route them correctly or save for later
- **Session tracking** — records facilitator, participants, topics, and next recommended step for every interview session; prior session summary shown at session start
- **Brainstorming** — capture freeform thoughts before or during interviews; surfaced automatically as context during Q&A
- **Requirements analysis** — extract structured requirements from uploaded documents, map to ADM phases and Zachman cells
- **Stakeholder interviews** — chat-based or interactive web form; dated and versioned notes
- **Diagram support** — Mermaid, Graphviz (.dot), Draw.io (.drawio), ArchiMate notation
- **Decision Register** — cross-artifact decision tracking with governance states (Provisional → Verified/Voted/Fiat), owner attribution, and on-demand registers tailored by audience, domain, authority, cost, impact, or risk
- **Artifact grill** — deep-review any artifact using grill-me skills (stress-test, premortem, decision, design, software-design, infra-design, artifact, diagram, boardroom-strategy); auto-selects best skill by artifact type
- **Opt-out tracking** — explicitly opt out of any question or artifact; reasons and timestamps recorded; surfaced in status reports and consolidated documents
- **Artifact compliance** — automatic compliance check when opening any artifact; offer to remediate missing fields/sections or accept as-is with sensible defaults
- **Pre-publish compliance** — `/ea-publish` runs compliance scan on all selected artifacts before assembly; non-compliant items flagged with option to proceed or remediate
- **Review & consistency** — per-artifact review workflow; cross-artifact consistency checking
- **Consolidated reporting** — merge all artifacts into a single Markdown or Word document; opted-out and non-standard items flagged inline
- **Research agent integration** — invoke `@research-agent` at any point during interviews for evidence-based validation of drivers, risks, technology choices, or assumptions
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
| `/ea-status` | Portfolio dashboard with type, domains, phase progress, artifact counts, opt-outs, and non-standard artifact flags |
| `/ea-phase [phase]` | Start, edit, or resume an ADM phase |
| `/ea-artifact [action]` | Create, view, or list artifacts; runs compliance check on view |
| `/ea-brainstorm [phase]` | Capture freeform thoughts and context before or during interviews |
| `/ea-interview [mode]` | Start or resume a stakeholder interview (artifact or phase mode; Text/Web/Display) |
| `/ea-generate [artifact] [format]` | Export an artifact as Word (.docx), PowerPoint (.pptx), or Mermaid diagram |
| `/ea-review [artifact]` | Open an artifact for review and assessment; runs compliance check on load |
| `/ea-requirements [action]` | Manage architecture requirements |
| `/ea-decisions [options]` | Generate a Decision Register from all A3 decision logs; filter by audience, owner, domain, authority, cost, impact, risk, subject, or status |
| `/ea-grill [artifact] [--skill]` | Deep-review an artifact using a grill-me skill (stress-test, premortem, decision, design, boardroom-strategy, etc.) |
| `/ea-publish` | Merge all artifacts into a consolidated document; compliance pre-check, opted-out and non-standard items flagged |
| `/ea-help` | Getting-started guide, full command reference, and interview shortcuts |

## Interview Shortcuts

Type these at any interview prompt:

| Shortcut | Action |
|---|---|
| `d` / `default` | Accept the suggested default answer |
| `s` / `skip` | Skip for now — field marked ⚠️ (can return later) |
| `n/a` | Mark not applicable — field marked ➖ |
| `opt-out` | Opt out of this question — field marked ⊘, reason tracked |
| `opt-out artifact` | Opt out of the entire artifact |
| `y` | Keep the existing answer |
| `a: {text}` | Log as a governance decision (Appendix A3) |
| `govern` / `g` | Update A3 governance state |
| `b:` / `brainstorm` | Start a freeform brainstorm pause |
| `?` / `help` | Show artifact purpose, current progress, and shortcuts |
| `concepts` | Show EA concepts quick reference (Principle/Goal/Objective/Strategy/Plan/Risk/Issue/Problem) |

> **Skip vs. Opt-out:** `skip` is temporary — the field can be filled in later. `opt-out` is a deliberate decision — recorded in `engagement.json`, visible in `/ea-status`, and flagged in reports.

## Engagement Management

After creating an engagement, use `/ea-open` to:

- **View full details** — metadata, phase-by-phase progress, artifact list
- **Edit metadata** — update name, description, sponsor, dates, status (Active/On Hold/Planning/Completed)
- **Edit phase status** — manually advance or adjust any ADM phase with automatic timestamp tracking
- **Edit artifact status** — update artifact and review status without opening files
- **Archive** — move completed engagements to `.archive/` to declutter your portfolio
- **Delete** — permanently remove engagements (requires slug confirmation)

Use `/ea-status` for a portfolio-level dashboard showing all engagements with type, domains, progress, artifact counts, opt-outs, and any non-standard artifacts.

## Artifact Content Policy

> **Important:** Artifacts are populated from user interviews, uploaded documents, and explicit input — not arbitrary AI-generated content.

| Marker | Meaning |
|---|---|
| `⚠️ Not answered` | Field skipped — can be filled in later |
| `➖ Not applicable` | Field does not apply to this engagement |
| `⊘ Opted out` / `⊘ Opted out — {reason}` | Deliberately excluded; reason and timestamp tracked |
| `🤖 AI Draft — Review required` | AI-suggested content awaiting human confirmation |
| `✓ Default accepted` | User accepted the suggested default |
| `📎 Source: uploads/{file}` | Answer sourced from an uploaded document |

## Artifact Compliance

When any artifact is opened for interview, review, or viewing, EA Assistant runs a three-tier compliance check:

- **Tier 1** — frontmatter fields, heading structure
- **Tier 2** — engagement header block, content sections, unresolved template tokens
- **Tier 3** — artifact-specific requirements (e.g., Appendix A3 Decision Log)

If gaps are found, you are offered:
1. **Achieve compliance** — add missing fields and sections; all existing content is preserved
2. **Accept as-is** — apply minimal defaults only; document structure unchanged; gaps noted in reports

## Project Storage

All engagement data is stored in `EA-projects/` relative to your working directory:

```
EA-projects/
├── engagement-name/
│   ├── engagement.json       # metadata, ADM phases, settings, opt-outs
│   ├── requirements/         # local architecture requirements
│   ├── artifacts/            # generated artifacts + review files
│   ├── diagrams/             # Mermaid, Graphviz, Draw.io files
│   ├── uploads/              # source documents and diagrams
│   └── interviews/
│       ├── session-log.md    # chronological session history (who, what, next step)
│       └── interview-*.md    # dated, versioned interview notes
└── .archive/                 # archived engagements (hidden)
    └── old-engagement/
        └── engagement.json
```

## Frameworks Supported

- **TOGAF 10** — ADM process backbone
- **Zachman Framework** — full 6×6 classification
- **ArchiMate 3.x** — architecture notation and modelling

## License

[MIT](./LICENSE)
