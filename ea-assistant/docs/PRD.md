# EA Assistant — Product Requirements Document

**Version:** 0.9.11
**Status:** Current
**Author:** Costa Pissaris

---

## 1. Product Overview

EA Assistant is a Claude Code plugin for **EA Practitioners** leading Enterprise Architecture engagements. It provides a structured, interview-driven workflow grounded in **TOGAF 10** (process), **Zachman Framework** (classification), and **ArchiMate 3.x** (notation).

The plugin turns Claude into an EA facilitator: it interviews practitioners and stakeholders, populates TOGAF artifacts from those interviews, tracks decisions and traceability chains, and produces consolidated architecture reports. It replaces the unstructured Word/spreadsheet/shared-drive workflow that most teams use to run engagements today.

It is not an EA modelling tool (that is Sparx, Archi, or MEGA). It is the **engagement management and documentation layer** that most EA tooling omits.

**Platform:** The current version runs inside **Claude Code** and relies on the Claude Code plugin framework (commands, skills, agents). A future version is planned as a standalone application backed by an LLM API, removing the Claude Code dependency. Implementation decisions should avoid deep Claude Code-specific coupling where a framework-agnostic alternative exists.

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

The engagement's strategic context is captured as a complete linked chain from executive intent to practical execution:

```
Vision ──inspires──► Mission ──contextualizes──► Business Drivers (DRV)
                                                          │
                                                       drives
                                                          ▼
Issues (ISS) ──threatens──► Goals (G) ◄──achieves── Strategies (STR)
    │                           │
   causes                 operationalizes
    ▼                           ▼
Problems (PRB) ──blocks──► Objectives (OBJ)
                                │
                             informs
                                ▼
                        Capability Model          ◄── Capability Gap (prevents Goals)
                       (What the org does)
                                │
                            shapes
                                ▼
                         Operating Model
                       (How the org functions)
                                │
                           measured by
                                ▼
                      Metrics (Leading & Lagging)
                       /          |          \
                 surfaces    identifies    evaluates
                     ▼            ▼             ▼
                New Issues   New Problems   Cap. Maturity
                                │
                             defines
                                ▼
                     Requirements Register
                    (traces to ALL layers above)
```

- **Vision** — long-term aspirational destination (3–5 years); the "North Star" all Drivers and Strategies must align with
- **Mission** — the organisation's fundamental purpose today; bounds which Drivers are in scope
- **Business Drivers** — forces making the engagement necessary (internal/external, opportunity/threat/mandate)
- **Goals** — qualitative desired outcomes linked to drivers
- **Objectives** — measurable, time-bound results that operationalise goals
- **Issues** — systemic barriers that *threaten* goals (structural, persistent — not a single-fix symptom)
- **Problems** — specific, observable symptoms that *block* objectives
- **Strategies** — chosen approaches for achieving goals; recorded in §7 Strategic Direction Summary of the Architecture Vision (STR-NNN)
- **Capability Model** — stable, hierarchical map of what the organisation must be able to do (people + process + info + tools), independent of org structure; informed by Objectives and Strategies
- **Capability Gap** — a missing or immature capability that prevents Goals; identified through Gap Analysis; triggers Phase E work packages
- **Operating Model** — how the organisation functions to deliver value (process, information, technology, governance); shaped by the Capability Model; measured by Metrics
- **Metrics** — specific, quantifiable measures (leading or lagging) that validate whether Strategies are working and Goals/Objectives are being achieved; close the feedback loop by surfacing new Issues and Problems when performance falls below threshold

Requirements Register entries carry a Motivation field that links each requirement to its source — any layer of the chain above.

> 📎 Source framework: `skills/ea-artifact-templates/references/ea-concepts-source.pdf` — *Enterprise Architecture Strategic Context: Terms, Concepts, and Relationship Models*

### EA Concepts (13 total)

Vision, Mission, Principle, Goal, Objective, Strategy, Plan, Risk, Issue, Problem, Capability Model, Operating Model, Metrics — each with a formal definition, TOGAF phase placement, ArchiMate 3.x element, and a disambiguation checklist. Full definitions in `skills/ea-artifact-templates/references/ea-concepts.md`.

**Disambiguation summary:**

| Concept | Qualitative or Measurable | Time-bound | Owns a mitigation | Links to |
|---|---|---|---|---|
| Vision | Aspirational (future state) | No | No | Inspires Mission and Drivers |
| Mission | Declarative (present purpose) | No | No | Bounds Drivers and Goals |
| Principle | Rule (non-negotiable) | No | No | Architecture decisions |
| Goal | Qualitative | No | No | Drivers |
| Objective | Measurable | Yes | No | Goals |
| Strategy | Directional | No | No | Goals (STR-NNN) |
| Plan | Ordered action set | Yes | No | Strategies |
| Issue | Qualitative (systemic barrier) | No | Yes (action plan) | Goals (threatens) |
| Problem | Specific symptom | No | Yes (requirement) | Objectives (blocks) |
| Risk | Potential future event | No | Yes (mitigation) | Goals or Objectives |
| Capability Model | What the org does | No | No | Informed by Objectives and Strategies; shapes Operating Model |
| Capability Gap | Missing/immature capability | No | Yes (work package) | Prevents Goals; triggers Gap Analysis and Phase E WPs |
| Operating Model | How the org functions | No | No | Shaped by Capability Model; measured by Metrics |
| Metrics | Quantifiable measure (leading/lagging) | Yes (target + deadline) | No | Validates Objectives; surfaces new Issues and Problems |

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

**23 TOGAF artifact templates:**

| Artifact | Phase | A3 | A4 | A5 |
|---|---|---|---|---|
| Architecture Principles | Prelim | — | — | — |
| Engagement Charter | Prelim | — | — | ✓ |
| Governance Framework | Prelim | — | — | ✓ |
| Requirements Register (with Motivation field) | Requirements | — | — | ✓ |
| Traceability Matrix | Requirements | — | — | — |
| Architecture Vision (15 sections) | A | ✓ | ✓ | ✓ |
| Statement of Architecture Work | A | ✓ | — | ✓ |
| Stakeholder Map | A | — | — | — |
| Business Architecture | B | ✓ | ✓ | ✓ |
| Business Model Canvas | B | — | — | — |
| Data Architecture | C-Data | ✓ | ✓ | ✓ |
| Application Architecture | C-App | ✓ | ✓ | ✓ |
| Technology Architecture | D | ✓ | ✓ | ✓ |
| Gap Analysis | B–D | — | — | ✓ |
| Architecture Roadmap (Strategic Alignment + per-WP goal/strategy links) | E | ✓ | — | ✓ |
| Migration Plan | F | — | — | ✓ |
| Architecture Contract | G | ✓ | — | — |
| Implementation Governance Plan | G | — | — | ✓ |
| Compliance Assessment | G | — | — | ✓ |
| Risk Register | Cross-cutting | — | — | — |
| Architecture Decision Record | Cross-cutting | — | — | — |
| ADR Register | Cross-cutting | — | — | — |
| Zachman Diagram | Cross-cutting | — | — | ✓ |

**Appendix columns:** A3 = Decision Log; A4 = Stakeholder Concerns & Objections; A5 = Related Architecture Decisions

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

**Transition path:** Provisional may move directly to Verified, Voted, or Fiat when no formal review step is needed. Awaiting is an optional holding state used when stakeholder confirmation or a governance vote is pending before resolution. Returned sends the decision back to Provisional; a reason must be recorded.

```
Provisional ──────────────────────────────► Verified / Voted / Fiat
     │                                              ▲
     └──► Awaiting (optional) ─────────────────────┘
                                    │
                                    └──► Returned ──► Provisional
```

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
- **Apply findings (Step 7)** — after the grill output is produced, offers to apply recommended revisions back to the artifact one at a time (apply / skip / edit per revision); each applied revision bumps the artifact version (patch increment) and updates `lastModified`; `reviewStatus` is set to `Revised`; Approved artifacts require explicit confirmation before any revision is written

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

### 5.11 Architecture Roadmap Agent

The `ea-roadmap` agent creates and manages the Architecture Roadmap artifact (Phase E/F). It auto-selects one of three modes based on what exists in the engagement:

| Mode | Triggers when | Behaviour |
|---|---|---|
| **Review** | `artifacts/architecture-roadmap.md` exists | Checks completeness, traceability (GAP/REQ refs), wave/dependency logic; presents issues for fix |
| **Artifact-informed** | Source artifacts exist, no roadmap yet | Reads Architecture Vision (G/OBJ/STR), Gap Analysis, Requirements Register → builds goal/strategy coverage register → derives candidate WPs → elicits wave/effort/owner → writes artifact |
| **Clean-slate** | No artifacts at all | 7-question elicitation sequence (horizon → waves → WPs → plateaus → prioritisation) → writes artifact |

In artifact-informed mode, **every candidate work package is anchored to at least one Goal (G-NNN), Objective (OBJ-NNN), or Strategy (STR-NNN)** from the Architecture Vision before any WP is confirmed. Goals and Strategies with no covering WP are flagged as coverage gaps. This alignment is recorded in the Strategic Alignment section of the roadmap template and in the `Advances Goals/Objectives` and `Executes Strategies` fields of each WP.

Invoke by asking Claude: *"Let's build the architecture roadmap"* or *"Review the current roadmap."*

### 5.12 Document Ingestion Layer

Document handling is split across two components with clear responsibilities:

- **`ea-document-ingestion` skill** — **format layer**: how to read each file type (.docx, .pdf, .xlsx, .csv, .mmd, .drawio, .png). Handles format-specific extraction only.
- **`ea-document-analyst` agent** — **EA mapping layer**: what to extract and where it belongs. Reads the extracted content and maps it to artifact fields, artifact types, and ADM phases. Presents a confirmation summary before writing anything.

This separation ensures format changes (e.g., adding .pptx support) only touch the ingestion skill, while EA mapping logic (e.g., "strategy content → Architecture Vision §7") is centralised in the analyst agent.

Invoke by asking Claude: *"Analyse the uploaded documents"* or *"Use this document to populate the artifacts."*

### 5.13 Undocumented Agents (Planned Features)

Two agents exist in the plugin but have no dedicated command workflow yet:

- **`ea-consistency-checker`** — flags cross-artifact inconsistencies (e.g., a Goal in the Architecture Vision that has no corresponding entry in the Business Architecture); invoke by asking: *"Check for cross-artifact inconsistencies in this engagement."*
- **`ea-advisor`** — answers EA methodology questions (TOGAF, Zachman, ArchiMate) in context; invoke by asking any methodology question in chat.

These will gain dedicated commands and workflow integration in a future version.

### 5.14 Risk Management

`/ea-risks` generates and maintains a cross-cutting Risk Register by scanning existing artifacts for risk content:

- **Sources scanned:** Architecture Vision §14, Statement of Architecture Work, Migration Plan risk section, Compliance Assessment, and any existing `risk-register-*.md` files
- **RIS-NNN ID scheme** — unified, domain-agnostic
- **Risk rating:** Likelihood × Impact matrix → Critical / High / Medium / Low
- **Modes:** `generate` (default, writes file), `status` (inline summary), `update RIS-NNN <field> <value>`
- **Template:** `risk-register.md`

### 5.15 Architecture Change Management

`/ea-changes` generates a Change Register (`change-register.md`) by aggregating all ACR (Architecture Change Request) artifacts for Phase H.

- **Modes:** `generate` (default), `status` (inline summary), `update <ACR-ID> <field> <value>`
- **Template:** `change-register.md` (aggregate view of all change request artifacts)

### 5.16 Stakeholder Concerns & Objections

`/ea-concerns` manages CON-NNN entries captured during stakeholder engagement. Concerns are stored in **Appendix A4** within each applicable artifact.

- **CON-NNN ID scheme** — stakeholder concern / objection
- Records the concern statement, stakeholder, artifact context, and resolution status
- Concerns feed into the Stakeholder Map and can trigger ADR threshold scoring

### 5.17 Architecture Decision Records (ADR)

ADRs are standalone documents capturing significant architecture decisions — technology/vendor selection, pattern choices, make-vs-buy, data governance, security architecture, or any decision that is hard to reverse.

**ADR vs A3 Decision Log:**
- **A3** = governance state tracking inside an artifact (who decided what, at what authority, verified or not)
- **ADR** = standalone full-context document (situation, options analysis, rationale, consequences)
- **A5** = cross-reference appendix inside artifacts listing related ADR-NNN IDs

**ADR lifecycle:** `Candidate → In Progress → Completed → Superseded (by ADR-NNN) | Deprecated`

**ADR threshold:** `ea-interviewer` suggests an ADR when 2+ of 8 indicators apply: technology/vendor selection, high cost/risk, hard to reverse, make-vs-buy, contested by stakeholder, affects data governance / security / compliance / principles.

**`/ea-adrs` modes:** `generate` (writes ADR Register), `status` (inline summary), `new` (create ADR from template), `update ADR-NNN <field> <value>`

**Templates:** `architecture-decision-record.md` (individual ADR), `adr-register.md` (aggregate register)

### 5.18 Zachman Diagram

The Zachman Diagram is a cross-cutting classification artifact mapping all engagement content across the 6×6 grid (Rows: Contextual → Functioning; Columns: What / How / Where / Who / When / Why). Row 6 (Functioning) is always 🚫 — it represents the running enterprise, not a specification.

**Coverage indicator:** ✅ Populated / ⚠️ Partial / ❌ Empty / 🚫 Out of scope

**`/ea-zachman` modes:** `generate` (auto-populate from existing artifacts), `review` (inline 6×6 matrix with % coverage), `gap` (prioritised gap list with remediation actions), `interview` (guided Q&A row by row), `classify <artifact>` (cell classification for any artifact/concept)

**Template:** `zachman-diagram.md`

### 5.19 Governance Artifacts

Three governance templates covering Preliminary through Phase H:

| Template | Phase | Purpose |
|---|---|---|
| `governance-framework.md` | Prelim | Enterprise governance structure: ARB ToR, decision rights, ADM tailoring, compliance process |
| `implementation-governance-plan.md` | G | Engagement-specific governance: review schedule, checkpoints, waiver process, escalation |
| `change-register.md` | H | Aggregated view of all ACR artifacts |

Created via `/ea-artifact create <template-name>` or generated automatically by `/ea-changes`.

### 5.20 Diagram Generation

Diagrams are generated and rendered through two paths:

**`ea-diagram` agent** — creates `.mmd` (Mermaid), `.dot` (Graphviz), or `.drawio` files. Uses a standard diagram catalogue per artifact type (e.g., Architecture Vision → motivation map + stakeholder power/interest grid; Business Architecture → capability map + process flow + org map). Naming convention: `{artifact-id}-{diagram-type}.mmd` in `EA-projects/{slug}/diagrams/`.

**`/ea-generate png|svg`** — renders `.mmd` files to images using mermaid-cli (`mmdc`). Auto-discovers `mmdc` on PATH, falls back to `npx -y @mermaid-js/mermaid-cli`. Options: `--theme`, `--bg`, `--all` (batch render all `.mmd` in the engagement).

**Diagram inclusion in deliverables (default on):** When generating docx or pptx, `/ea-generate` automatically:
1. Scans `diagrams/{artifact-id}-*.png` for pre-rendered images
2. Auto-renders any `{artifact-id}-*.mmd` without a matching PNG
3. Passes the diagram list to the script via `--diagrams @/tmp/ea-diagrams-{artifact-id}.json`
4. Embeds diagrams as a final appendix (docx) or appended slides (pptx)

No prompt is shown — diagrams are included by default when they exist.

### 5.21 Engagement Review and Migration

**`/ea-engage-review`** runs a full-scope consistency, alignment, governance, and quality review for the active engagement. Produces an Engagement Review Report covering:
- ADM phase coverage and artifact completeness
- Motivation chain traceability (DRV→G→OBJ)
- ADR status (Candidate/In Progress counts, stale/overdue)
- Governance and compliance gaps
- Zachman coverage summary

**`/ea-migrate`** aligns a legacy engagement with the current plugin version's templates and conventions. Applies non-destructive structural patches (adds missing appendices, missing frontmatter fields, missing compliance notes). Use `--report` to preview without applying.

### 5.22 Research & References

The `ResearchAndReferences/` folder is the engagement library for external context: whitepapers, reference architectures, analyst reports, standards documents, repository links, and ad-hoc research notes.

**`/ea-research` modes:**
- `add` — paste a document; stored as `.md` with frontmatter
- `note` — write a freeform research observation
- `link` — add a URL with title, summary, and tags
- `list` (default) — index table of all items with type/title/date/tags
- `view <item>` — full content + edit/delete/apply options
- `apply [artifact-id]` — synthesise selected research against an artifact

**Apply workflow:** loads selected research items + target artifact → identifies gaps, contradictions, enhancements → `y/n/edit` per revision → bumps artifact version (patch) → writes synthesis report to `ResearchAndReferences/synthesis-{artifact-id}-{date}.md`

**Index file:** `ResearchAndReferences/research-index.md` — auto-maintained, tracks type/title/file/date/tags for every item. Created during `/ea-new` scaffolding; created silently by `/ea-open` for legacy engagements.

---

## 6. Data Model

### Folder Structure

```
EA-projects/
└── {slug}/
    ├── engagement.json           # all state: phases, artifacts, sessions, direction, metrics, optOuts
    ├── CLAUDE.md                 # auto-generated session context; refreshed (overwritten) on /ea-open
    ├── artifacts/                # .md artifact files + .review.md review files
    ├── interviews/               # session-log.md + dated interview notes per session
    ├── brainstorm/               # brainstorm-notes.md
    ├── diagrams/                 # .mmd, .dot, .drawio, .png, .svg files
    ├── uploads/                  # source documents for ingestion
    ├── reviews/                  # grill-me review outputs
    ├── ResearchAndReferences/    # research documents, notes, links; research-index.md; synthesis reports
    └── ui/                       # generated HTML interview/brainstorm forms
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
| `/ea-new` | — | Create engagement — collects name, type, domains, sponsor, scope, dates; scaffolds ResearchAndReferences/; generates CLAUDE.md |
| `/ea-open` | `[slug]` | Open engagement, refresh CLAUDE.md, ensure ResearchAndReferences/ exists, next-action menu |
| `/ea-status` | — | Portfolio dashboard — all engagements with progress, research count, opt-outs, non-standard flags |
| `/ea-phase` | `[phase name]` | Start, navigate to, or resume an ADM phase |
| `/ea-interview` | `[web|voice|text|display]` | Run stakeholder interview; ADR threshold scoring; defaults to Web mode |
| `/ea-artifact` | `[create|view|list]` | Create, view, or list artifacts; compliance check on view |
| `/ea-brainstorm` | `[phase]` | Capture freeform thoughts before or during interviews |
| `/ea-generate` | `[artifact] [docx|pptx|mermaid|png|svg] [--theme] [--bg] [--all]` | Export artifact; embeds diagrams by default in docx/pptx; renders Mermaid to images via mmdc |
| `/ea-review` | `[artifact]` | Open artifact for review; runs compliance check; update review status |
| `/ea-grill` | `[artifact] [--skill name]` | Deep-review artifact using a grill-me skill; auto-selects skill by type; apply findings with y/n/edit |
| `/ea-requirements` | `[list|add|edit|waive]` | Manage architecture requirements; corporate (read-only) and project scope |
| `/ea-decisions` | `[--audience] [--owner] [--domain] [--status] [--cost] [--impact] [--risk]` | Generate Decision Register from all A3 logs with filters |
| `/ea-adrs` | `[generate|status|new|update ADR-NNN <field> <value>]` | Manage Architecture Decision Records; auto-suggested by interviewer at 2+ threshold indicators |
| `/ea-risks` | `[generate|status|update RIS-NNN <field> <value>]` | Generate and maintain Risk Register by scanning all artifacts |
| `/ea-changes` | `[generate|status|update <ACR-ID> <field> <value>]` | Generate Change Register aggregating all Phase H ACR artifacts |
| `/ea-concerns` | — | Manage CON-NNN stakeholder concerns (Appendix A4) |
| `/ea-zachman` | `[generate|review|gap|interview|classify <artifact>]` | Manage Zachman 6×6 classification diagram |
| `/ea-research` | `[add|note|link|list|view <item>|apply [artifact-id]]` | Manage research library; synthesise research against deliverables |
| `/ea-engage-review` | — | Full-scope engagement consistency, alignment, governance, and quality review |
| `/ea-migrate` | `[--report]` | Align legacy engagement to current plugin version conventions |
| `/ea-publish` | `[markdown|word]` | Consolidated report via Pandoc; pre-publish compliance check |
| `/ea-help` | — | Command reference, interview shortcuts, research agent guide |

---

## 8. Agents

| Agent | Role | Invoked by |
|---|---|---|
| `ea-facilitator` | Guides users through ADM phases; reads facilitatorStyle config | `/ea-phase`, `/ea-open` |
| `ea-interviewer` | Conducts structured interviews; all 4 modes, question preview, brainstorm, cross-topic detection, ADR threshold scoring | `/ea-interview` |
| `ea-roadmap` | Creates and manages the Architecture Roadmap in Review / Artifact-informed / Clean-slate mode | Ask Claude: "Let's build the roadmap" or "Review the roadmap" |
| `ea-requirements-analyst` | Extracts structured requirements from uploaded documents | `/ea-requirements` |
| `ea-consistency-checker` | Flags cross-artifact inconsistencies (no dedicated command) | Ask Claude: "Check for cross-artifact inconsistencies" |
| `ea-document-analyst` | EA mapping layer — extracts content from uploaded documents and maps to artifacts (no dedicated command) | Ask Claude: "Analyse the uploaded documents" |
| `ea-advisor` | Answers EA methodology questions — TOGAF, Zachman, ArchiMate (no dedicated command) | Ask any methodology question in chat |
| `ea-diagram` | Creates, edits, and interprets architecture diagrams (Mermaid, Graphviz, Draw.io, ArchiMate); standard diagram catalogue per artifact type; offers mmdc render after saving | `/ea-generate mermaid|png|svg`, ask Claude: "Create a diagram for..." |

---

## 9. Quality Gates

| Gate | When | Mechanism |
|---|---|---|
| Artifact compliance | Every artifact open (interview, review, view) | 3-tier check: T1 frontmatter → T2 template structure → T3 artifact-specific (A3/A5 presence, Strategic Alignment, Scope column, Two-section structure) |
| Pre-publish compliance | Before `/ea-publish` assembles | All selected artifacts scanned; user chooses proceed or remediate; non-compliant items flagged in output |
| Content policy | Throughout interview | No AI content without `🤖` marker; no overwrite of Approved fields without confirmation |
| Opt-out audit | Ongoing | Every exclusion tracked with reason + timestamp in `engagement.json → optOuts[]`; surfaced in `/ea-status` and published reports |
| ADR threshold | During interview (post-answer) | After each answer, `ea-interviewer` scores 8 indicators; if 2+ match → suggest `/ea-adrs new` with pre-populated metadata; adds ADR-NNN to A3 Notes |
| Migration alignment | On `/ea-open` | Lightweight gap scan comparing `lastMigratedVersion` to current plugin version; displays count of detectable gaps; run `/ea-migrate` to align |

---

## 10. Success Metrics

| Metric | Baseline (without tool) | Target | How measured |
|---|---|---|---|
| Phase A interview duration (experienced EA) | ~3 hours across 2–3 sessions | ≤ 90 minutes in a single session | Session log timestamps from start of Phase A interview to Architecture Vision Draft status |
| Motivation chain coverage | Typically 0–20% of objectives have a traceable driver | 100% of OBJ-NNN entries link to at least one G-NNN; 100% of G-NNN entries link to at least one DRV-NNN | Compliance check on Architecture Vision §2–§6 |
| Report manual corrections before stakeholder submission | Typically 2–4 hours of formatting and gap-filling | ≤ 3 corrections (missing fields, formatting) per published report | User-reported on post-publish review |
| Non-EA stakeholder participation rate | Low — stakeholders disengage from text-heavy TOGAF interviews | Non-EA stakeholders can complete a Web or Voice interview with no prior TOGAF knowledge, verified by facilitator observation | Facilitator assessment at session close |
| Decision traceability | Decisions made verbally in sessions; rarely documented | All A3 log entries have a recorded owner and governance state of Awaiting or above before Phase G commences | `/ea-decisions` output inspected at Phase G gate: zero entries with state `Provisional` and no `owner` field |

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
