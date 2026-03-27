# EA Assistant — Product Requirements Document

**Version:** 0.9.0
**Status:** Current
**Author:** Costa Pissaris

---

## 1. Product Overview

EA Assistant is a Claude Code plugin that manages Enterprise Architecture engagements from initiation through closeout. It provides a structured, interview-driven workflow grounded in **TOGAF 10** (process), **Zachman Framework** (classification), and **ArchiMate 3.x** (notation).

The plugin turns Claude into an EA facilitator — guiding practitioners through ADM phases, populating architecture artifacts from stakeholder interviews, generating documents, and producing consolidated reports.

---

## 2. Problem Statement

Enterprise Architecture engagements are complex, multi-phase efforts involving many stakeholders, dozens of artifacts, and months of iterative work. Practitioners face three core problems:

- **Structure without tools** — TOGAF provides a framework but no execution tooling. Teams manage engagements in Word documents, spreadsheets, and shared drives with no traceability or consistency enforcement.
- **Interview quality** — Capturing good architecture direction (drivers, goals, objectives) requires skilled facilitation. Concepts like Goal vs. Objective vs. Strategy are routinely confused, producing poor artifacts.
- **Continuity** — EA engagements span multiple sessions and facilitators. Context is lost between sessions, decisions are undocumented, and artifacts drift out of sync.

---

## 3. Target Users

| User | Role | Primary Need |
|---|---|---|
| **EA Practitioner** | Lead architect running the engagement | Structured workflow, artifact generation, traceability |
| **EA Facilitator** | Runs stakeholder interviews | Question bank, guided interview flow, session notes |
| **Sponsor / Stakeholder** | Provides direction, reviews artifacts | Consolidated reports, Decision Register |
| **Business Analyst** | Captures requirements | Requirements Register, traceability to architecture |

---

## 4. Core Concepts

### Motivation Framework

The engagement's strategic context is captured as a linked chain:

```
Business Drivers (DRV) → Goals (G) → Objectives (OBJ)
                               ↑               ↑
                          Issues (ISS)    Problems (PRB)
                                              ↓
                                    Requirements Register
```

- **Business Drivers** — forces making the engagement necessary (internal/external, opportunity/threat/mandate)
- **Goals** — qualitative desired outcomes linked to drivers
- **Objectives** — measurable, time-bound results that operationalise goals
- **Issues** — systemic barriers that threaten goals
- **Problems** — specific, observable symptoms that block objectives
- **Strategies** — chosen approaches for achieving goals (captured in Direction Summary)

### EA Concepts (8 total)

Principle, Goal, Objective, Strategy, Plan, Risk, Issue, Problem — each with formal definition, TOGAF placement, ArchiMate element, and disambiguation checklist. See `skills/ea-artifact-templates/references/ea-concepts.md`.

---

## 5. Features

### 5.1 Engagement Management

- Create engagements with type (Greenfield / Brownfield / Assessment-only / Migration), domains, sponsor, scope, and dates
- Open, edit metadata, archive, restore, delete
- Portfolio dashboard showing all engagements with phase progress and artifact counts
- Per-engagement `CLAUDE.md` auto-generated on `/ea-new`; refreshed on every `/ea-open` — loads session context automatically when Claude is opened from the engagement folder

### 5.2 ADM Lifecycle

- 11 phases: Prelim, Requirements, A–H
- Phase applicability rules by engagement type and domain selection
- Phase status tracking with timestamps (Not Started / In Progress / Complete / On Hold / Not Applicable)
- Non-linear navigation — jump to any phase at any time

### 5.3 Phase Interviews

- Curated question banks for every ADM phase with output routing tables
- Four modes: **Web** (default, input form), **Voice** (Web Speech API mic button), **Text** (chat Q&A), **Display**
- Question preview before answering — see all questions, choose mode, brainstorm first, or jump to a specific question
- ID scheme for Phase A: DRV-NNN, G-NNN, OBJ-NNN, ISS-NNN, PRB-NNN, STR-NNN, MET-NNN (documented at top of Phase A section)
- Section markers on every question group — each question links to its target Architecture Vision section
- Session attribution (facilitator, participants) and chronological session log per engagement

### 5.4 Artifact Generation

15 TOGAF artifact templates:

| Artifact | Phase |
|---|---|
| Architecture Principles | Prelim |
| Requirements Register (with Motivation field) | Requirements |
| Traceability Matrix | Requirements |
| Architecture Vision (15 sections) | A |
| Statement of Architecture Work | A |
| Stakeholder Map | A |
| Business Architecture | B |
| Business Model Canvas | B |
| Data Architecture | C-Data |
| Application Architecture | C-App |
| Technology Architecture | D |
| Gap Analysis | B–D |
| Architecture Roadmap | E |
| Migration Plan | F |
| Architecture Contract | G |
| Compliance Assessment | G |

**Architecture Vision sections:**
§1 Executive Summary · §2 Business Drivers · §3 Goals · §4 Objectives · §5 Issues · §6 Problems · §7 Strategic Direction Summary · §8 Scope · §9 Stakeholders · §10 Architecture Principles · §11 Constraints · §12 Assumptions · §13 High-Level Target Architecture · §14 Key Risks · §15 Next Steps · Appendix A3 Decision Log

**Artifact content policy:** content comes only from interviews, uploaded documents, or explicit user input.

Answer state markers:
- `⚠️ Not answered` — skipped, can return later
- `➖ Not applicable`
- `⊘ Opted out — {reason}` — deliberate exclusion, tracked
- `🤖 AI Draft — Review Required`
- `✓ Default accepted`
- `📎 Source: uploads/{file}`

### 5.5 Interview Quality Controls

- **Compliance check** — three-tier check (frontmatter, template structure, artifact-specific) on every artifact open; offer to remediate or accept as-is
- **Cross-topic detection** — flags answers belonging in a different artifact; offers to route immediately, flag for later, or continue as-is
- **Concept-check** — catches Goal/Objective/Strategy/Issue/Problem confusion inline; offers reclassification
- **Opt-out tracking** — question and artifact level; reason + timestamp recorded in `engagement.json → optOuts[]`; surfaced in `/ea-status` and consolidated reports
- **Brainstorm integration** — capture freeform thoughts before or during interviews; surfaced as `💭` hints on semantically related questions

### 5.6 Facilitator Config

Controlled via `.claude/ea-assistant.local.md`:

| Setting | Options | Default | Effect |
|---|---|---|---|
| `facilitatorStyle` | `patient` / `direct` / `executive` | `patient` | Tone, pacing, acknowledgement, section pauses |
| `audienceLevel` | `executive` / `architect` / `technical` / `mixed` | `mixed` | Terminology depth and TOGAF jargon level |
| `requireConfirmBeforeRecord` | `true` / `false` | `false` | Confirm before writing each answer to artifact |
| `researchPrompts` | `true` / `false` | `true` | Show `@research-agent` prompts on drivers/risks/assumptions |
| `sessionSummary` | `true` / `false` | `true` | End-of-session topic/theme summary |

**Style behaviour:**

| | `patient` | `direct` | `executive` |
|---|---|---|---|
| Preamble | One sentence why question matters | Question only | Business-outcome framing |
| Acknowledgement | Brief and warm | None | None |
| Short answer | One gentle probe | Accept as-is | Accept as-is |
| Examples | Proactive | On request | On request |
| Transitions | "Anything else?" pause | None | Checkpoint every 5–7 Qs |
| Jargon | TOGAF with gloss | Full TOGAF | Business language only |

### 5.7 Decision Register

- Every artifact has an **Appendix A3 Decision Log** table
- `/ea-decisions` aggregates all A3 rows into a cross-artifact register
- Governance states: Provisional → Awaiting → Verified / Voted / Fiat / Returned
- Filter flags: `--audience`, `--owner`, `--domain`, `--authority`, `--cost`, `--impact`, `--risk`, `--subject`, `--status`
- Audience presets: `executive` / `architect` / `business` / `technical`

### 5.8 Artifact Review and Grill

- Per-artifact review workflow: Not Reviewed / In Review / Approved / Needs Revision
- `/ea-review` — opens artifact for review with compliance check
- `/ea-grill [artifact] [--skill]` — deep-review using a grill-me skill; auto-selects skill by artifact type; saves output to `reviews/` folder

**Grill skill routing (auto-selection):**

| Artifact type | Default skill |
|---|---|
| Architecture Vision, Strategy | stress-test |
| Architecture Roadmap, Migration Plan | premortem |
| Architecture Principles, Decisions | decision |
| Business Architecture, BMC | design |
| Application Architecture | software-design |
| Technology Architecture, Infra | infra-design |
| Any structured document | artifact |
| Any diagram | diagram |
| Executive presentation | boardroom-strategy |

### 5.9 Publishing

- **Pre-publish compliance check** — all selected artifacts scanned before assembly; non-compliant items flagged with option to proceed or remediate
- Consolidates artifacts in TOGAF ADM order into a single Markdown or Word document
- Cover page, Artifact Status Summary table, Table of Contents, per-artifact status headers
- Opted-out items and non-standard artifacts flagged inline
- Pandoc-based Word export (`.docx`)

### 5.10 Research Agent Integration

- `@research-agent` invocable at any point during interviews or facilitation
- Validates business drivers, technology claims, risks, and assumptions with cited evidence
- Findings paste directly into brainstorm notes or artifact fields
- Documented in Phase A facilitation notes and `/ea-help`

---

## 6. Data Model

### Folder Structure

```
EA-projects/
└── {slug}/
    ├── engagement.json        # all state: phases, artifacts, direction, metrics, optOuts
    ├── CLAUDE.md              # auto-generated session context; refreshed on /ea-open
    ├── artifacts/             # .md artifact files + .review.md review files
    ├── interviews/            # session-log.md + dated interview notes per session
    ├── brainstorm/            # brainstorm-notes.md
    ├── diagrams/              # .mmd, .dot, .drawio files
    ├── uploads/               # source documents for ingestion
    ├── reviews/               # grill-me review outputs
    └── ui/                    # generated HTML interview/brainstorm forms
```

### engagement.json Schema

```json
{
  "name": "",
  "slug": "",
  "description": "",
  "sponsor": "",
  "organisation": "",
  "scope": "",
  "engagementType": "Greenfield | Brownfield | Assessment-only | Migration",
  "architectureDomains": ["Business", "Data", "Application", "Technology"],
  "startDate": "YYYY-MM-DD",
  "targetEndDate": "YYYY-MM-DD or null",
  "status": "Active | On Hold | Planning | Completed",
  "currentPhase": "Prelim",
  "requirementsRepoPath": "",
  "lastModified": "",
  "direction": {
    "Business": {
      "goals": [{ "id": "G-001", "statement": "", "priority": "" }],
      "objectives": [{ "id": "OBJ-001", "statement": "", "measure": "", "target": "", "deadline": "", "priority": "" }],
      "strategies": [{ "id": "STR-001", "statement": "", "supports": ["G-001"], "priority": "" }]
    }
  },
  "metrics": {
    "Business": [{ "id": "MET-001", "name": "", "type": "outcome | performance | activity", "measure": "", "baseline": "", "target": "", "deadline": "", "frequency": "", "source": "", "supports": ["G-001"], "status": "" }]
  },
  "phases": {
    "Prelim": { "status": "Not Started", "startedAt": null, "completedAt": null }
  },
  "artifacts": [{ "id": "", "name": "", "phase": "", "file": "", "status": "Draft", "reviewStatus": "Not Reviewed", "createdAt": "", "lastModified": "" }],
  "optOuts": [{ "type": "question | artifact", "artifactId": "", "questionRef": "", "reason": "", "timestamp": "" }]
}
```

---

## 7. Commands

| Command | Description |
|---|---|
| `/ea-new` | Create engagement — collects name, type, domains, sponsor, scope, dates |
| `/ea-open` | Open engagement, refresh CLAUDE.md, next-action menu |
| `/ea-status` | Portfolio dashboard — all engagements with progress, opt-outs, non-standard flags |
| `/ea-phase [phase]` | Start, edit, or resume an ADM phase |
| `/ea-interview [mode]` | Run stakeholder interview (Web / Voice / Text / Display) |
| `/ea-artifact [action]` | Create, view, or list artifacts; compliance check on view |
| `/ea-brainstorm [phase]` | Capture freeform thoughts before or during interviews |
| `/ea-generate [artifact] [format]` | Export artifact as Word, PPTX, or Mermaid diagram |
| `/ea-review [artifact]` | Review and assess an artifact; compliance check on load |
| `/ea-grill [artifact] [--skill]` | Deep-review artifact using a grill-me skill |
| `/ea-requirements [action]` | Manage architecture requirements |
| `/ea-decisions [options]` | Generate Decision Register from all A3 logs |
| `/ea-publish [format]` | Consolidated report with pre-publish compliance check |
| `/ea-help` | Command reference, interview shortcuts, research agent guide |

---

## 8. Agents

| Agent | Role |
|---|---|
| `ea-facilitator` | Guides users through ADM phases; reads facilitatorStyle config |
| `ea-interviewer` | Conducts structured interviews; all 4 modes, brainstorm, cross-topic detection |
| `ea-requirements-analyst` | Extracts structured requirements from uploaded documents |
| `ea-consistency-checker` | Flags cross-artifact inconsistencies |
| `ea-document-analyst` | Analyses uploaded documents for architecture content |
| `ea-advisor` | Answers EA questions and provides TOGAF/ArchiMate guidance |
| `ea-diagram` | Generates and interprets architecture diagrams |

---

## 9. Quality Gates

| Gate | When | Mechanism |
|---|---|---|
| Artifact compliance | Every artifact open | 3-tier check: frontmatter → structure → artifact-specific |
| Pre-publish compliance | Before `/ea-publish` assembles | All selected artifacts scanned; user chooses proceed or remediate |
| Frontmatter validation | Before every commit | `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts <plugin>/` |
| Content policy | Throughout interview | No AI content without `🤖` marker; no overwrite of Approved fields without confirmation |
| Opt-out audit | Ongoing | Every exclusion tracked with reason + timestamp in `engagement.json` |

---

## 10. Success Metrics

- An experienced EA can complete a full Phase A interview and produce an approved Architecture Vision artifact in a single session
- All motivation chain elements (DRV → G → OBJ, ISS → G, PRB → OBJ) are captured with ID-based traceability
- A non-EA stakeholder can participate in a Voice or Web mode interview without training
- The consolidated report is publishable without manual editing
- Every decision made during the engagement is traceable via the Decision Register

---

## 11. Out of Scope (Current Version)

- Reference architecture library
- Cost-benefit analysis / investment case templates
- Portfolio management across multiple engagements
- Architecture pattern detection / pattern library
- Multi-user collaboration with locking or conflict resolution
- External compliance framework mapping (GDPR, ISO 27001, HIPAA)
- SharePoint integration for requirements repository

---

*This document is maintained in `ea-assistant/docs/PRD.md`. Update it when features are added or changed.*
