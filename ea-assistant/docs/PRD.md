# EA Assistant — Product Requirements Document

**Version:** 0.9.1
**Status:** Current
**Author:** Costa Pissaris

---

## 1. Product Overview

EA Assistant is a Claude Code plugin for **EA Practitioners** leading Enterprise Architecture engagements. It provides a structured, interview-driven workflow grounded in **TOGAF 10** (process), **Zachman Framework** (classification), and **ArchiMate 3.x** (notation).

The plugin turns Claude into an EA facilitator: it interviews practitioners and stakeholders, populates TOGAF artifacts from those interviews, tracks decisions and traceability chains, and produces consolidated architecture reports. It replaces the unstructured Word/spreadsheet/shared-drive workflow that most teams use to run engagements today.

It is not an EA modelling tool (that is Sparx, Archi, or MEGA). It is the **engagement management and documentation layer** that most EA tooling omits.

---

## 2. Problem Statement

Enterprise Architecture engagements typically span 3–6 months, involve 5–15 stakeholders, and produce 10–20 artifacts across 4–8 ADM phases. Practitioners face three core problems:

- **Structure without tools** — TOGAF provides a framework but no execution tooling. Teams manage engagements in Word documents, spreadsheets, and shared drives with no traceability or consistency enforcement. Artifacts drift out of sync; decisions are undocumented; there is no single source of truth for engagement state.
- **Interview quality** — Capturing good architecture direction (drivers, goals, objectives) requires skilled facilitation. Concepts like Goal vs. Objective vs. Strategy are routinely confused, producing artifacts whose motivation chain cannot be traced and whose objectives cannot be measured. A poorly facilitated Phase A interview produces an Architecture Vision that cannot drive downstream phases.
- **Continuity** — EA engagements span multiple sessions and facilitators. Context is lost between sessions, decisions made in one session are not visible in the next, and artifacts populated by different people contradict each other.

---

## 3. Target Users

The **EA Practitioner** is the primary user. All design decisions should favour this user when trade-offs arise.

| Priority | User | Role | Primary Need | Entry Point |
|---|---|---|---|---|
| 1 | **EA Practitioner** | Lead architect running the engagement | Structured workflow, artifact generation, traceability | `/ea-new`, `/ea-open`, `/ea-phase` |
| 2 | **EA Facilitator** | Runs stakeholder interviews (may be same person as practitioner) | Question bank, guided interview flow, session notes | `/ea-interview`, `/ea-brainstorm` |
| 3 | **Sponsor** | Authorises the engagement; provides strategic direction | Consolidated reports, Decision Register filtered to their level | `/ea-publish`, `/ea-decisions --audience executive` |
| 4 | **Business Analyst** | Captures and manages architecture requirements | Requirements Register with motivation traceability | `/ea-requirements` |

> Stakeholders (non-sponsor) participate in interviews but do not use the tool directly — they interact via the Web or Voice interview form.

---

## 4. Core Concepts

### Motivation Framework

The engagement's strategic context is captured as a linked chain:

```
Business Drivers (DRV) ──drives──► Goals (G) ──operationalises──► Objectives (OBJ)
                                        ▲                                  ▲
                               threatens│                         blocks   │
                                        │                                  │
                                   Issues (ISS)                  Problems (PRB)
                                                                           │
                                                                    Requirements Register
                                                                  (links to any of the above)
```

- **Business Drivers** — forces making the engagement necessary (internal/external, opportunity/threat/mandate)
- **Goals** — qualitative desired outcomes linked to drivers
- **Objectives** — measurable, time-bound results that operationalise goals
- **Issues** — systemic barriers that *threaten* goals (not observable symptoms — structural, persistent)
- **Problems** — specific, observable symptoms that *block* objectives
- **Strategies** — chosen approaches for achieving goals; recorded in §7 Strategic Direction Summary of the Architecture Vision (STR-NNN)

Requirements Register entries carry a Motivation field that links each requirement to its source — any of: DRV, ISS, PRB, G, or OBJ.

### EA Concepts (8 total)

Principle, Goal, Objective, Strategy, Plan, Risk, Issue, Problem — each with a formal definition, TOGAF phase placement, ArchiMate 3.x element, and a disambiguation checklist to prevent concept confusion during interviews. Full definitions in `skills/ea-artifact-templates/references/ea-concepts.md`.

**Disambiguation summary:**

| Concept | Qualitative or Measurable | Time-bound | Owns a mitigation |
|---|---|---|---|
| Goal | Qualitative | No | No |
| Objective | Measurable | Yes | No |
| Strategy | Directional | No | No |
| Issue | Qualitative (systemic barrier) | No | Yes (action plan) |
| Problem | Specific symptom | No | Yes (requirement) |
| Risk | Potential future event | No | Yes (mitigation) |

---

## 5. Features

### 5.1 Engagement Management

- Create engagements with type (Greenfield / Brownfield / Assessment-only / Migration), domains, sponsor, scope, and dates
- Open, edit metadata, archive, restore, delete
- Portfolio dashboard (`/ea-status`) showing all engagements with: type, domains, current phase, artifact counts, opt-out count, non-standard artifact flags
- Per-engagement `CLAUDE.md` auto-generated on `/ea-new`; refreshed (overwritten from template + current engagement state) on every `/ea-open` — loads session context automatically when Claude is opened from the engagement folder

> Note: The `CLAUDE.md` refresh on `/ea-open` overwrites the file. Do not add manual notes to `CLAUDE.md`; use `brainstorm/brainstorm-notes.md` instead.

### 5.2 ADM Lifecycle

- 11 phases: Prelim, Requirements (custom non-TOGAF phase for structured requirements capture), A–H
- Phase status tracking with timestamps (Not Started / In Progress / Complete / On Hold / Not Applicable)
- Non-linear navigation — jump to any phase at any time
- **Phase applicability** is determined by engagement type and domain selection at creation time:

| Phase | Greenfield | Brownfield | Assessment-only | Migration |
|---|---|---|---|---|
| Prelim | Required | Required | Required | Required |
| Requirements | Required | Required | Required | Required |
| A — Architecture Vision | Required | Required | Required | Required |
| B — Business Architecture | Required | Required | Optional | Required |
| C — Data Architecture | Domain† | Domain† | Optional | Domain† |
| C — Application Architecture | Domain† | Domain† | Optional | Domain† |
| D — Technology Architecture | Domain† | Domain† | Optional | Domain† |
| E — Opportunities & Solutions | Required | Required | Not Applicable | Required |
| F — Migration Planning | Optional | Required | Not Applicable | Required |
| G — Implementation Governance | Required | Required | Not Applicable | Required |
| H — Architecture Change Mgmt | Optional | Required | Not Applicable | Optional |

† *Domain-dependent*: phase is Required if the corresponding domain (Data / Application / Technology) was selected; Not Applicable if not selected.

### 5.3 Phase Interviews

- Curated question banks for every ADM phase with output routing tables linking each question to its target artifact section
- Four modes:
  - **Web** (default) — interactive input form rendered as a React artifact; one question card at a time with progress bar
  - **Voice** — Web mode with 🎤 mic button per question; uses `window.SpeechRecognition`; transcript is editable before submission; falls back gracefully if speech recognition unavailable
  - **Text** — chat-based Q&A; question preview with 6-option menu before answering
  - **Display** — read-only list of all questions for the phase/artifact; no answer recording; used for preparation or reference
- **Question preview** (Text mode) — shows full question list before starting; menu options: Start Web / Voice / Text, Brainstorm first, Jump to specific question, Display only, Resume (if prior answers exist)
- **ID scheme for Phase A:** DRV-NNN, G-NNN, OBJ-NNN, ISS-NNN, PRB-NNN, STR-NNN, MET-NNN — documented in the phase header; each question group carries a `§N` section marker linking to its target Architecture Vision section
- Session attribution — step 0 of every interview collects facilitator name and participant list; recorded in session log and interview note frontmatter
- Chronological session log per engagement (`interviews/session-log.md`); prior session summary shown at the start of each new session

### 5.4 Artifact Generation

Artifacts are populated from interview answers, uploaded documents, or explicit user input. No AI-generated content is written to an artifact without a `🤖 AI Draft — Review Required` marker.

**15 TOGAF artifact templates:**

| Artifact | Phase | A3 Decision Log |
|---|---|---|
| Architecture Principles | Prelim | — |
| Requirements Register (with Motivation field) | Requirements | — |
| Traceability Matrix | Requirements | — |
| Architecture Vision (15 sections) | A | ✓ |
| Statement of Architecture Work | A | ✓ |
| Stakeholder Map | A | — |
| Business Architecture | B | ✓ |
| Business Model Canvas | B | — |
| Data Architecture | C-Data | — |
| Application Architecture | C-App | — |
| Technology Architecture | D | — |
| Gap Analysis (covers all selected domains) | B–D | — |
| Architecture Roadmap | E | ✓ |
| Migration Plan | F | — |
| Architecture Contract | G | ✓ |
| Compliance Assessment | G | — |

**Architecture Vision sections:**
§1 Executive Summary · §2 Business Drivers · §3 Goals · §4 Objectives · §5 Issues · §6 Problems · §7 Strategic Direction Summary · §8 Scope · §9 Stakeholders · §10 Architecture Principles · §11 Constraints · §12 Assumptions · §13 High-Level Target Architecture · §14 Key Risks · §15 Next Steps · Appendix A3 Decision Log

**Answer state markers:**
- `⚠️ Not answered` — skipped, can return later
- `➖ Not applicable`
- `⊘ Opted out — {reason}` — deliberate exclusion, tracked
- `🤖 AI Draft — Review Required`
- `✓ Default accepted`
- `📎 Source: uploads/{file}`

### 5.5 Interview Quality Controls

- **Compliance check** — see §9 Quality Gates
- **Cross-topic detection** — flags answers that belong in a different artifact; offers to route immediately, flag for later, or continue as-is
- **Concept-check** — catches Goal/Objective/Strategy/Issue/Problem confusion inline; offers reclassification with reference to the EA Concepts disambiguation table
- **Opt-out tracking** — question and artifact level; reason + timestamp recorded in `engagement.json → optOuts[]`; surfaced in `/ea-status` and consolidated reports
- **Brainstorm integration** — freeform thoughts captured via `/ea-brainstorm` are matched to interview questions by keyword overlap and surfaced as `💭` hints when a question's subject matches the brainstorm content

### 5.6 Facilitator Config

Controlled via `.claude/ea-assistant.local.md` in the working directory:

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

**Precedence:** When `facilitatorStyle` and `audienceLevel` conflict (e.g., `executive` style with `technical` audience), `audienceLevel` governs terminology depth and `facilitatorStyle` governs pacing and tone. The practitioner is responsible for setting a coherent combination.

### 5.7 Decision Register

Decisions captured during interviews are logged in **Appendix A3 Decision Log** tables, which are included in the five key artifacts marked ✓ in §5.4. Other artifacts may include A3 optionally.

`/ea-decisions` aggregates all A3 rows across artifacts into a cross-artifact register.

**Governance states and semantics:**

| State | Meaning | Who sets it |
|---|---|---|
| `Provisional` | Decision recorded but not yet reviewed | Interviewer (automatic on A3 log) |
| `Awaiting` | Under review; stakeholder confirmation or governance vote pending | EA Practitioner |
| `Verified` | Confirmed correct by the responsible architect; no formal vote required | EA Practitioner |
| `Voted` | Approved by a formal governance body or quorum | Sponsor / governance body |
| `Fiat` | Accepted by executive authority without formal vote; sponsor directive | Sponsor |
| `Returned` | Sent back for rework; reason must be recorded | Reviewer |

**Transition path:** Provisional → Awaiting → Verified / Voted / Fiat / Returned → (if Returned) back to Provisional.

**Filter flags:** `--audience`, `--owner`, `--domain`, `--authority`, `--cost`, `--impact`, `--risk`, `--subject`, `--status`
**Audience presets:** `executive` / `architect` / `business` / `technical`

### 5.8 Artifact Review and Grill

**Review workflow:**
- States: Not Reviewed → In Review → Approved / Needs Revision → (if Needs Revision) back to In Review
- `/ea-review [artifact]` — opens the artifact, runs the compliance check, and presents the review interface where the reviewer can update status, add a review note, and trigger Needs Revision with a reason
- Approved artifacts cannot be overwritten without confirmation; the interviewer is warned before writing to an Approved field

**Grill (deep review):**
- `/ea-grill [artifact] [--skill]` — runs a grill-me skill against the artifact; output saved to `reviews/{artifact}-review-{YYYY-MM-DD}.md`
- Auto-selects skill by artifact type; override with `--skill`
- When an artifact matches multiple routing rows, the more specific row wins (e.g., Architecture Vision matches both "Architecture Vision, Strategy" and "Any structured document" — `stress-test` wins)

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
- Consolidates artifacts in TOGAF ADM order (Prelim → Requirements → A → B → C-Data → C-App → D → E → F → G → H) into a single Markdown or Word document
- Cover page, Artifact Status Summary table, Table of Contents, per-artifact status headers
- Opted-out items and non-standard artifacts flagged inline

**Export tools:**
- `/ea-publish` — uses **Pandoc** to render Markdown → `.docx`; requires `pandoc` installed
- `/ea-generate [artifact] word` — uses **python-docx** for per-artifact Word export; requires `python-docx`
- `/ea-generate [artifact] pptx` — uses **python-pptx** for PowerPoint export; requires `python-pptx`
- `/ea-generate [artifact] mermaid` — renders Mermaid diagram source from artifact content

### 5.10 Research Agent Integration

- Invoke `@research-agent` at any interview prompt or during facilitation by typing `@research-agent` followed by the claim to validate
- Validates business drivers, technology claims, risks, and assumptions with cited evidence
- If no supporting evidence is found, the agent states this explicitly — absence of evidence is surfaced, not silently omitted
- Findings are pasted by the user directly into the current answer field or brainstorm notes; they are not auto-written to artifacts
- Research prompts are shown automatically on driver, risk, and assumption questions when `researchPrompts: true` (default)
- Documented in Phase A facilitation notes and `/ea-help`

### 5.11 Undocumented Agents (Planned Features)

Three agents exist in the plugin but have no dedicated interview or command workflow yet:

- **`ea-consistency-checker`** — flags cross-artifact inconsistencies (e.g., a Goal in the Architecture Vision that has no corresponding entry in the Business Architecture); invoked manually via chat
- **`ea-document-analyst`** — analyses uploaded documents in `uploads/` for architecture content and suggests artifact mappings; invoked manually via chat
- **`ea-advisor`** — answers EA methodology questions (TOGAF, Zachman, ArchiMate) in context; invoked manually via chat

These will gain dedicated commands and workflow integration in a future version.

---

## 6. Data Model

### Folder Structure

```
EA-projects/
└── {slug}/
    ├── engagement.json        # all state: phases, artifacts, sessions, direction, metrics, optOuts
    ├── CLAUDE.md              # auto-generated session context; refreshed (overwritten) on /ea-open
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
  "sessions": [
    {
      "id": "session-001",
      "date": "YYYY-MM-DD",
      "facilitator": "",
      "participants": [""],
      "phase": "",
      "artifactsWorked": [""],
      "topics": [""],
      "nextStep": "",
      "notesFile": "interviews/interview-YYYY-MM-DD.md"
    }
  ],
  "artifacts": [{ "id": "", "name": "", "phase": "", "file": "", "status": "Draft", "reviewStatus": "Not Reviewed", "createdAt": "", "lastModified": "" }],
  "optOuts": [{ "type": "question | artifact", "artifactId": "", "questionRef": "", "reason": "", "timestamp": "" }]
}
```

> `direction` and `metrics` keys are domain-scoped. When multiple domains are active (e.g., Business + Technology), each domain gets its own key at the same level as `"Business"` in the example above.

---

## 7. Commands

| Command | Key Arguments / Options | Description |
|---|---|---|
| `/ea-new` | — | Create engagement — collects name, type, domains, sponsor, scope, dates; generates CLAUDE.md |
| `/ea-open` | `[slug]` | Open engagement, refresh CLAUDE.md, next-action menu |
| `/ea-status` | — | Portfolio dashboard — all engagements with progress, opt-outs, non-standard flags |
| `/ea-phase` | `[phase name]` | Start, navigate to, or resume an ADM phase |
| `/ea-interview` | `[web|voice|text|display]` | Run stakeholder interview; defaults to Web mode |
| `/ea-artifact` | `[create|view|list]` | Create, view, or list artifacts; compliance check on view |
| `/ea-brainstorm` | `[phase]` | Capture freeform thoughts before or during interviews |
| `/ea-generate` | `[artifact] [word|pptx|mermaid]` | Export artifact using python-docx (word), python-pptx (pptx), or Mermaid source |
| `/ea-review` | `[artifact]` | Open artifact for review; runs compliance check; update review status |
| `/ea-grill` | `[artifact] [--skill name]` | Deep-review artifact using a grill-me skill; auto-selects skill by type |
| `/ea-requirements` | `[list|add|edit|waive]` | Manage architecture requirements; corporate (read-only) and project scope |
| `/ea-decisions` | `[--audience] [--owner] [--domain] [--status] [--cost] [--impact] [--risk]` | Generate Decision Register from all A3 logs with filters |
| `/ea-publish` | `[markdown|word]` | Consolidated report via Pandoc; pre-publish compliance check |
| `/ea-help` | — | Command reference, interview shortcuts, research agent guide |

---

## 8. Agents

| Agent | Role | Invoked by |
|---|---|---|
| `ea-facilitator` | Guides users through ADM phases; reads facilitatorStyle config | `/ea-phase`, `/ea-open` |
| `ea-interviewer` | Conducts structured interviews; all 4 modes, question preview, brainstorm, cross-topic detection | `/ea-interview` |
| `ea-requirements-analyst` | Extracts structured requirements from uploaded documents | `/ea-requirements` |
| `ea-consistency-checker` | Flags cross-artifact inconsistencies (manual invocation only) | Chat (`@ea-consistency-checker`) |
| `ea-document-analyst` | Analyses uploaded documents for architecture content (manual invocation only) | Chat (`@ea-document-analyst`) |
| `ea-advisor` | Answers EA methodology questions — TOGAF, Zachman, ArchiMate (manual invocation only) | Chat (`@ea-advisor`) |
| `ea-diagram` | Generates and interprets architecture diagrams | `/ea-generate [artifact] mermaid` |

---

## 9. Quality Gates

| Gate | When | Mechanism |
|---|---|---|
| Artifact compliance | Every artifact open (interview, review, view) | 3-tier check: frontmatter → template structure → artifact-specific requirements (e.g., A3 presence in key artifacts) |
| Pre-publish compliance | Before `/ea-publish` assembles | All selected artifacts scanned; user chooses proceed or remediate; non-compliant items flagged in output |
| Content policy | Throughout interview | No AI content without `🤖` marker; no overwrite of Approved fields without confirmation |
| Opt-out audit | Ongoing | Every exclusion tracked with reason + timestamp in `engagement.json → optOuts[]`; surfaced in `/ea-status` and published reports |

---

## 10. Success Metrics

| Metric | Baseline (without tool) | Target | How measured |
|---|---|---|---|
| Phase A interview duration (experienced EA) | ~3 hours across 2–3 sessions | ≤ 90 minutes in a single session | Session log timestamps from start of Phase A interview to Architecture Vision Draft status |
| Motivation chain coverage | Typically 0–20% of objectives have a traceable driver | 100% of OBJ-NNN entries link to at least one G-NNN; 100% of G-NNN entries link to at least one DRV-NNN | Compliance check on Architecture Vision §2–§6 |
| Report manual corrections before stakeholder submission | Typically 2–4 hours of formatting and gap-filling | ≤ 3 corrections (missing fields, formatting) per published report | User-reported on post-publish review |
| Non-EA stakeholder participation rate | Low — stakeholders disengage from text-heavy TOGAF interviews | Non-EA stakeholders can complete a Web or Voice interview with no prior TOGAF knowledge, verified by facilitator observation | Facilitator assessment at session close |
| Decision traceability | Decisions made verbally in sessions; rarely documented | 100% of architecture decisions recorded in A3 logs and visible in `/ea-decisions` output before Phase G | `/ea-decisions` row count vs. decisions noted in session logs |

---

## 11. Out of Scope (Current Version)

- Reference architecture library
- Cost-benefit analysis / investment case templates
- Cross-engagement portfolio management (resource allocation, budget tracking, dependency mapping) — `/ea-status` provides a read-only portfolio dashboard only
- Architecture pattern detection / pattern library
- Multi-user collaboration with locking or conflict resolution
- External compliance framework mapping (GDPR, ISO 27001, HIPAA)
- SharePoint / cloud storage integration for requirements repository *(planned for a future version)*

---

*This document is maintained in `ea-assistant/docs/PRD.md`. Update it when features are added or changed.*
