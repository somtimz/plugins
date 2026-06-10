# EA Assistant — Product Requirements Document

**Version:** 0.9.59
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

| Priority | User                 | Role                                                             | Primary Need                                                    | Entry Point                                         |
| -------- | -------------------- | ---------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------- |
| 1        | **EA Practitioner**  | Lead architect running the engagement                            | Structured workflow, artifact generation, traceability          | `/ea-new`, `/ea-open`, `/ea-phase`                  |
| 2        | **EA Facilitator**   | Runs stakeholder interviews (may be same person as practitioner) | Question bank, guided interview flow, session notes             | `/ea-interview`, `/ea-brainstorm`                   |
| 3        | **Sponsor**          | Authorises the engagement; provides strategic direction          | Consolidated reports, Decision Register filtered to their level | `/ea-publish`, `/ea-decisions --audience executive` |
| 4        | **Business Analyst** | Captures and manages architecture requirements                   | Requirements Register with motivation traceability              | `/ea-requirements`                                  |

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
                           exercises
                                ▼
                         Value Streams
                    (End-to-end value delivery)
                                │
                            composed of
                                ▼
                         Business Processes
                                │
                         enables / consumed by
                                ▼
                          Use Cases
                    (Actor goals supported)
                                │
                           generates
                                ▼
                     Requirements Register
                    (traces to ALL layers above)
                                ▲
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
- **Value Stream** — end-to-end chain of activities delivering stakeholder value from trigger to outcome; composed of Business Processes, exercises Capabilities
- **Business Process** — structured, repeatable set of activities with defined actors, inputs, outputs, and decision points; component of a Value Stream
- **Use Case** — discrete goal pursued by a specific actor; consumes Business Processes, generates Requirements
- **Capability Gap** — a missing or immature capability that prevents Goals; identified through Gap Analysis; triggers Phase E work packages
- **Operating Model** — how the organisation functions to deliver value (process, information, technology, governance); shaped by the Capability Model; measured by Metrics
- **Metrics** — specific, quantifiable measures (leading or lagging) that validate whether Strategies are working and Goals/Objectives are being achieved; close the feedback loop by surfacing new Issues and Problems when performance falls below threshold

Requirements Register entries carry a Motivation field that links each requirement to its source — any layer of the chain above.

> 📎 Source framework: `skills/ea-artifact-templates/references/ea-concepts-source.pdf` — *Enterprise Architecture Strategic Context: Terms, Concepts, and Relationship Models*

### EA Concepts (25 total)

Vision, Mission, Business Driver, Principle, Goal, Objective, Strategy, Plan, Risk, Issue, Problem, Opportunity, Capability Model, Capability Gap, Value Stream, Business Process, Use Case, Operating Model, Metrics, Constraint, Stakeholder Concern, ADR, ABB, SBB, User Story — each with a formal definition, TOGAF phase placement, ArchiMate 3.x element, and a disambiguation checklist. Full definitions in `skills/ea-artifact-templates/references/ea-concepts.md`.

**Disambiguation summary:**

| Concept          | Qualitative or Measurable              | Time-bound              | Owns a mitigation  | Links to                                                                               |
| ---------------- | -------------------------------------- | ----------------------- | ------------------ | -------------------------------------------------------------------------------------- |
| Vision           | Aspirational (future state)            | No                      | No                 | Inspires Mission and Drivers                                                           |
| Mission          | Declarative (present purpose)          | No                      | No                 | Bounds Drivers and Goals                                                               |
| Principle        | Rule (non-negotiable)                  | No                      | No                 | Architecture decisions                                                                 |
| Goal             | Qualitative                            | No                      | No                 | Drivers                                                                                |
| Objective        | Measurable                             | Yes                     | No                 | Goals                                                                                  |
| Strategy         | Directional                            | No                      | No                 | Goals (STR-NNN)                                                                        |
| Plan             | Ordered action set                     | Yes                     | No                 | Strategies                                                                             |
| Issue            | Qualitative (systemic barrier)         | No                      | Yes (action plan)  | Goals (threatens)                                                                      |
| Problem          | Specific symptom                       | No                      | Yes (requirement)  | Objectives (blocks)                                                                    |
| Risk             | Potential future event                 | No                      | Yes (mitigation)   | Goals or Objectives                                                                    |
| Capability Model | What the org does                      | No                      | No                 | Informed by Objectives and Strategies; exercises Value Streams; shapes Operating Model |
| Capability Gap   | Missing/immature capability            | No                      | Yes (work package) | Prevents Goals; triggers Gap Analysis and Phase E WPs                                  |
| Value Stream     | End-to-end value delivery              | No                      | No                 | Composed of Business Processes; exercises Capabilities; links to Goals                 |
| Business Process | Structured activity flow               | No                      | No                 | Component of Value Streams; exercises Capabilities; generates Requirements             |
| Use Case         | Actor goal + scenario                  | No                      | No                 | Consumes Processes; generates Requirements; links to Capabilities                      |
| Operating Model  | How the org functions                  | No                      | No                 | Shaped by Capability Model; measured by Metrics                                        |
| Metrics          | Quantifiable measure (leading/lagging) | Yes (target + deadline) | No                 | Validates Objectives; surfaces new Issues and Problems                                 |
| Constraint       | Non-negotiable restriction (certain)   | No                      | No                 | Sourced from Policy, Principle, or external mandate; registered with CST-NNN; `/ea-constraints` |
| Business Principle | Non-negotiable rule (business domain)  | No                      | No                 | Governs Goals, Strategies, and Operating Model decisions; sourced from Policy or self-grounded; BP-NNN; `/ea-principles` |
| Data Principle   | Non-negotiable rule (data domain)      | No                      | No                 | Governs Data Architecture; registered with DP-NNN; `/ea-principles` |
| Application Principle | Non-negotiable rule (application domain) | No               | No                 | Governs Application Architecture and integration patterns; registered with AP-NNN; `/ea-principles` |
| Technology Principle | Non-negotiable rule (technology domain) | No                | No                 | Governs platform and vendor selection; registered with TP-NNN; `/ea-principles` |
| ABB              | Reusable component (solution-independent) | No                   | No                 | Realised by SBB-NNN; supports Phase D/E deliverables; registered with ABB-NNN; `/ea-abbs` |
| SBB              | Concrete implementation                | No                      | No                 | Realises ABB-NNN; specific product or build choice; registered with SBB-NNN; `/ea-sbbs` |
| User Story       | Qualitative (stakeholder goal)         | No                      | No                 | Linked to REQ-NNN and ABB-NNN; registered with STY-NNN; `/ea-stories`                 |

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

| Phase                         | Greenfield | Brownfield | Assessment-only | Migration |
| ----------------------------- | ---------- | ---------- | --------------- | --------- |
| Prelim                        | Required   | Required   | Required        | Required  |
| Requirements                  | Required   | Required   | Required        | Required  |
| A — Architecture Vision       | Required   | Required   | Required        | Required  |
| B — Business Architecture     | Required   | Required   | Optional        | Required  |
| C — Data Architecture         | Domain†    | Domain†    | Optional        | Domain†   |
| C — Application Architecture  | Domain†    | Domain†    | Optional        | Domain†   |
| D — Technology Architecture   | Domain†    | Domain†    | Optional        | Domain†   |
| E — Opportunities & Solutions | Required   | Required   | Not Applicable  | Required  |
| F — Migration Planning        | Optional   | Required   | Not Applicable  | Required  |
| G — Implementation Governance | Required   | Required   | Not Applicable  | Required  |
| H — Architecture Change Mgmt  | Optional   | Required   | Not Applicable  | Optional  |

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

**25 TOGAF artifact templates:**

| Artifact                                                                | Phase             | A3  | A4  | A5  |
| ----------------------------------------------------------------------- | ----------------- | --- | --- | --- |
| Architecture Principles                                                 | Prelim            | —   | —   | —   |
| Engagement Charter                                                      | Prelim            | —   | —   | ✓   |
| Governance Framework                                                    | Prelim            | —   | —   | ✓   |
| Requirements Register (with Motivation field)                           | Requirements      | —   | —   | ✓   |
| Traceability Matrix                                                     | Requirements      | —   | —   | —   |
| Architecture Vision (15 sections)                                       | A                 | ✓   | ✓   | ✓   |
| Statement of Architecture Work                                          | A                 | ✓   | —   | ✓   |
| Stakeholder Map                                                         | A                 | —   | —   | —   |
| Business Architecture                                                   | B                 | ✓   | ✓   | ✓   |
| Business Model Canvas                                                   | B                 | —   | —   | —   |
| Data Architecture                                                       | C-Data            | ✓   | ✓   | ✓   |
| Application Architecture                                                | C-App             | ✓   | ✓   | ✓   |
| Technology Architecture                                                 | D                 | ✓   | ✓   | ✓   |
| Gap Analysis                                                            | B–D               | —   | —   | ✓   |
| Architecture Roadmap (Strategic Alignment + per-WP goal/strategy links) | E                 | ✓   | —   | ✓   |
| Migration Plan                                                          | F                 | —   | —   | ✓   |
| Architecture Contract                                                   | G                 | ✓   | —   | —   |
| Implementation Governance Plan                                          | G                 | —   | —   | ✓   |
| Compliance Assessment                                                   | G                 | —   | —   | ✓   |
| Risk Register                                                           | Cross-cutting     | —   | —   | —   |
| Architecture Decision Record                                            | Cross-cutting     | —   | —   | —   |
| Pending Architecture Decision (PAD)                                     | Cross-cutting     | —   | —   | —   |
| ADR Register                                                            | Cross-cutting     | —   | —   | —   |
| Zachman Diagram                                                         | Cross-cutting     | —   | —   | ✓   |
| Role Catalogue                                                          | A / Cross-cutting | —   | —   | —   |

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

| Setting                      | Options                                           | Default   | Effect                                                      |
| ---------------------------- | ------------------------------------------------- | --------- | ----------------------------------------------------------- |
| `facilitatorStyle`           | `patient` / `direct` / `executive`                | `patient` | Tone, pacing, acknowledgement, section pauses               |
| `audienceLevel`              | `executive` / `architect` / `technical` / `mixed` | `mixed`   | Terminology depth and TOGAF jargon level                    |
| `requireConfirmBeforeRecord` | `true` / `false`                                  | `false`   | Confirm before writing each answer to artifact              |
| `researchPrompts`            | `true` / `false`                                  | `true`    | Show `@research-agent` prompts on drivers/risks/assumptions |
| `sessionSummary`             | `true` / `false`                                  | `true`    | End-of-session topic/theme summary                          |

**Style behaviour:**

|                 | `patient`                         | `direct`      | `executive`              |
| --------------- | --------------------------------- | ------------- | ------------------------ |
| Preamble        | One sentence why question matters | Question only | Business-outcome framing |
| Acknowledgement | Brief and warm                    | None          | None                     |
| Short answer    | One gentle probe                  | Accept as-is  | Accept as-is             |
| Examples        | Proactive                         | On request    | On request               |
| Transitions     | "Anything else?" pause            | None          | Checkpoint every 5–7 Qs  |
| Jargon          | TOGAF with gloss                  | Full TOGAF    | Business language only   |

**Precedence:** When `facilitatorStyle` and `audienceLevel` conflict (e.g., `executive` style with `technical` audience), `audienceLevel` governs terminology depth and `facilitatorStyle` governs pacing and tone. The practitioner is responsible for setting a coherent combination.

### 5.7 Decision Register

Decisions captured during interviews are logged in **Appendix A3 Decision Log** tables, which are included in the five key artifacts marked ✓ in §5.4. Other artifacts may include A3 optionally.

`/ea-decisions` aggregates all A3 rows across artifacts into a cross-artifact register.

**Governance states and semantics:**

| State         | Meaning                                                                 | Who sets it                       |
| ------------- | ----------------------------------------------------------------------- | --------------------------------- |
| `Provisional` | Decision recorded but not yet reviewed                                  | Interviewer (automatic on A3 log) |
| `Awaiting`    | Under review; stakeholder confirmation or governance vote pending       | EA Practitioner                   |
| `Verified`    | Confirmed correct by the responsible architect; no formal vote required | EA Practitioner                   |
| `Voted`       | Approved by a formal governance body or quorum                          | Sponsor / governance body         |
| `Fiat`        | Accepted by executive authority without formal vote; sponsor directive  | Sponsor                           |
| `Returned`    | Sent back for rework; reason must be recorded                           | Reviewer                          |

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

**A3.N Decision Rationale Blocks (v0.9.28)**

Each A3 decision row may have a rationale detail block written directly below the A3 table, capturing the reasoning behind the decision:

```markdown
#### A3.N — {Item value}
- **Rationale:** Why this decision was made
- **Alternatives:** Other options considered and why they were rejected
- **Tradeoffs accepted:** What was sacrificed by choosing this option
- **Implications:** Downstream effects to monitor
```

- All four fields are optional; partial blocks (e.g., only Rationale + Tradeoffs) are valid
- When a user explicitly skips, a sentinel `*(rationale not captured)*` is written instead
- **Created by:** `/ea-interview` — immediately after `a: {text}` capture and before governance classification; `/ea-decisions rationale` — interactive catch-up pass for existing A3 entries
- **Compliance rule T3-RATIONALE:** Strategic-authority A3 entries without a rationale block (and without a sentinel) surface as a T2 warning in `/ea-artifact view`, `/ea-engage-review`, and `/ea-grill`
- **`/ea-decisions generate`** appends a **Decision Detail** section to the register — one card per decision with a documented A3.N block, ordered by Authority then Impact; respects `--audience` filter

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

| Artifact type                        | Default skill                                                        |
| ------------------------------------ | -------------------------------------------------------------------- |
| Architecture Vision, Strategy        | stress-test                                                          |
| Architecture Roadmap, Migration Plan | premortem                                                            |
| Architecture Principles, Decisions   | decision                                                             |
| Business Architecture, BMC           | design                                                               |
| Application Architecture             | software-design                                                      |
| Technology Architecture, Infra       | infra-design                                                         |
| Any structured document              | artifact                                                             |
| Any diagram                          | diagram                                                              |
| Executive presentation               | boardroom-strategy                                                   |
| Any artifact (L3+ engagement)        | practitioner — economic framing, decision quality, optionality audit |
| Any artifact (maturity check)        | maturity — L1–L5 assessment with advancement steps                   |
| Any artifact (pre-mortem)            | failure-mode — symptom scan against 6 failure modes                  |

### 5.9 Advanced Practitioner Content (v0.9.29)

A comprehensive body of advanced TOGAF practitioner guidance is now integrated across the plugin:

**Reference files:**
- `practitioner-tips.md` — 50 original tips + 70 phase-by-phase deep tactics + 25 cross-cutting expert moves, indexed by ADM phase and artifact type
- `adm-maturity-model.md` — 5-level maturity model (L1 Compliance → L5 Adaptive) with indicators, blockers, and advancement steps per level
- `advanced-patterns.md` — 7 patterns: Dual Operating System, Architecture as Product, Intent-Based Architecture, Option Architecture, Fitness Functions, Capability Heatmap → Investment Engine, Fracture Plane Design
- `failure-modes.md` — 6 failure modes: Documentation Trap, Centralized Bottleneck, Fake Governance, Misalignment with Finance, Over-Standardization, Static Target Illusion — each with symptoms, root cause, fix, prevention
- `elite-architect-playbook.md` — Day-to-day behaviors: 70/30 conversation rule, interface control, systems thinking, simplicity as weapon, influence without authority, org design shaping
- `practitioner-white-paper.md` — Synthesized white paper for executive communication: "Beyond Compliance: Using TOGAF as a High-Impact Enterprise Decision System"

**Integration points:**
- `adm-phase-guide.md` — each phase now includes Deep Tactics, Hidden Mechanics, and Maturity Indicators
- `ea-concepts.md` — each concept now includes Practitioner Notes with maturity markers (L1→L5) and economic framing
- `compliance-check.md` — Tier 4 advanced compliance rules (economic traceability, decision latency, optionality preservation, fitness function coverage) with maturity-based enforcement expectations
- `phase-interview-questions.md` — advanced practitioner questions per phase (economic reasoning, decision quality, failure mode symptoms, maturity assessment)
- All 32 artifact templates — collapsible compliance status block showing TOGAF/ADM requirements and completion status; 8 key templates include practitioner tip callouts

### 5.10 Publishing

- **Pre-publish compliance check** — all selected artifacts scanned before assembly; non-compliant items flagged with option to proceed or remediate
- Consolidates artifacts in TOGAF ADM order (Prelim → Requirements → A → B → C-Data → C-App → D → E → F → G → H) into a single Markdown or Word document
- Cover page, Artifact Status Summary table, Table of Contents, per-artifact status headers
- Opted-out items and non-standard artifacts flagged inline

**Export tools:**
- `/ea-publish` — uses **Pandoc** to render Markdown → `.docx`; requires `pandoc` installed
- `/ea-generate [artifact] word` — uses **python-docx** for per-artifact Word export; requires `python-docx`
- `/ea-generate [artifact] pptx` — uses **python-pptx** for PowerPoint export; requires `python-pptx`
- `/ea-generate [artifact] mermaid` — renders Mermaid diagram source from artifact content

### 5.11 Research Agent Integration

- Invoke `@research-agent` at any interview prompt or during facilitation by typing `@research-agent` followed by the claim to validate
- Validates business drivers, technology claims, risks, and assumptions with cited evidence
- If no supporting evidence is found, the agent states this explicitly — absence of evidence is surfaced, not silently omitted
- Findings are pasted by the user directly into the current answer field or brainstorm notes; they are not auto-written to artifacts
- Research prompts are shown automatically on driver, risk, and assumption questions when `researchPrompts: true` (default)
- Documented in Phase A facilitation notes and `/ea-help`

### 5.12 Architecture Roadmap Agent

The `ea-roadmap` agent creates and manages the Architecture Roadmap artifact (Phase E/F). It auto-selects one of three modes based on what exists in the engagement:

| Mode                  | Triggers when                              | Behaviour                                                                                                                                                                                 |
| --------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Review**            | `artifacts/architecture-roadmap.md` exists | Checks completeness, traceability (GAP/REQ refs), wave/dependency logic; presents issues for fix                                                                                          |
| **Artifact-informed** | Source artifacts exist, no roadmap yet     | Reads Architecture Vision (G/OBJ/STR), Gap Analysis, Requirements Register → builds goal/strategy coverage register → derives candidate WPs → elicits wave/effort/owner → writes artifact |
| **Clean-slate**       | No artifacts at all                        | 7-question elicitation sequence (horizon → waves → WPs → plateaus → prioritisation) → writes artifact                                                                                     |

In artifact-informed mode, **every candidate work package is anchored to at least one Goal (G-NNN), Objective (OBJ-NNN), or Strategy (STR-NNN)** from the Architecture Vision before any WP is confirmed. Goals and Strategies with no covering WP are flagged as coverage gaps. This alignment is recorded in the Strategic Alignment section of the roadmap template and in the `Advances Goals/Objectives` and `Executes Strategies` fields of each WP.

Invoke by asking Claude: *"Let's build the architecture roadmap"* or *"Review the current roadmap."*

### 5.13 Document Ingestion Layer

Document handling is split across two components with clear responsibilities:

- **`ea-document-ingestion` skill** — **format layer**: how to read each file type (.docx, .pdf, .xlsx, .csv, .mmd, .drawio, .png). Handles format-specific extraction only.
- **`ea-document-analyst` agent** — **EA mapping layer**: what to extract and where it belongs. Reads the extracted content and maps it to artifact fields, artifact types, and ADM phases. Presents a confirmation summary before writing anything.

This separation ensures format changes (e.g., adding .pptx support) only touch the ingestion skill, while EA mapping logic (e.g., "strategy content → Architecture Vision §7") is centralised in the analyst agent.

Invoke by asking Claude: *"Analyse the uploaded documents"* or *"Use this document to populate the artifacts."*

### 5.14 Undocumented Agents (Planned Features)

Two agents exist in the plugin but have no dedicated command workflow yet:

- **`ea-consistency-checker`** — flags cross-artifact inconsistencies (e.g., a Goal in the Architecture Vision that has no corresponding entry in the Business Architecture); invoke by asking: *"Check for cross-artifact inconsistencies in this engagement."*
- **`ea-advisor`** — answers EA methodology questions (TOGAF, Zachman, ArchiMate) in context; invoke by asking any methodology question in chat.

These will gain dedicated commands and workflow integration in a future version.

### 5.15 Risk Management

`/ea-risks` generates and maintains a cross-cutting Risk Register by scanning existing artifacts for risk content:

- **Sources scanned:** Architecture Vision §14, Statement of Architecture Work, Migration Plan risk section, Compliance Assessment, and any existing `risk-register*.md` files
- **RIS-NNN ID scheme** — unified, domain-agnostic
- **Risk rating:** Likelihood × Impact matrix → Critical / High / Medium / Low
- **Modes:** `generate` (default, writes file), `status` (inline summary), `update RIS-NNN <field> <value>`
- **Template:** `risk-register.md`

### 5.16 Constraints Management

`/ea-constraints` manages architecture constraints as first-class objects with dedicated `CST-NNN` IDs:

- **First-class concept:** Constraints are distinct from requirements (which define outcomes) and risks (which are uncertain). Every constraint has a **Source** (policy, regulation, contract, or mandate) and an **Owner** (accountable person or role).
- **CST-NNN ID scheme** — unified, domain-agnostic; distinct from `CON-NNN` (Stakeholder Concerns) and `REQ-NNN` (Requirements)
- **Constraint types:** Technology, Regulatory, Budget, Timeline, Organisational, Interoperability
- **Modes:** `list` (default, reads register), `add` (interactive capture), `update CST-NNN <field> <value>`, `trace` (artifact/SBB linkage), `impact` (assess bounded capabilities/work packages)
- **Enterprise vs Program scope:** Enterprise constraints have read-only content fields (statement, type, source, owner); Program constraints are fully editable
- **SBB traceability:** SBB records include `Referenced Constraints: [CST-NNN]` field linking vendor lock-in details back to canonical constraints
- **Template:** `constraints-register.md`
- **Skill:** `ea-constraints-management`

### 5.16a Policies Management (v0.9.49)

`/ea-policies` manages architecture policies as first-class governance documents with dedicated `POL-NNN` IDs:

- **First-class concept:** Policies are formal governance documents or mandates enacted by an authority (board, regulator, CISO, governance body). They are the **authorising source** for constraints — policies generate CST-NNN constraints but do not directly restrict solution space.
- **POL-NNN ID scheme** — unified, domain-agnostic; distinct from `CST-NNN` (constraints), `PRB-NNN` (problems), and `ADR-NNN` (decisions)
- **Policy types:** Security, Procurement, Data Governance, Technology, Compliance, HR, Operational
- **Modes:** `list` (default, reads register), `add` (interactive capture), `update POL-NNN <field> <value>`, `trace` (constraint/principle/SBB linkage), `impact` (assess bounded capabilities/ABBs/work packages through linked constraints)
- **Enterprise vs Divisional scope:** Enterprise policies have read-only content fields (title, type, issuing authority, statement); Divisional/Geographic policies are fully editable
- **Constraint traceability:** Policy records include `Linked Constraints: [CST-NNN]` field linking the policy to its derived constraints. Constraints prefer POL-NNN in their Source field over free-text.
- **Stale policy check:** Policies with Review Cycle past due are flagged in `list` mode; may invalidate linked constraints
- **Template:** `policies-register.md`
- **Skill:** `ea-policies-management`

### 5.17 Architecture Change Management

`/ea-changes` generates a Change Register (`change-register.md`) by aggregating all ACR (Architecture Change Request) artifacts for Phase H.

- **Modes:** `generate` (default), `status` (inline summary), `update <ACR-ID> <field> <value>`
- **Template:** `change-register.md` (aggregate view of all change request artifacts)

### 5.17a Stakeholder Concerns & Objections

`/ea-concerns` manages CON-NNN entries captured during stakeholder engagement. Concerns are stored in **Appendix A4** within each applicable artifact.

- **CON-NNN ID scheme** — stakeholder concern / objection
- Records the concern statement, stakeholder, artifact context, and resolution status
- Concerns feed into the Stakeholder Map and can trigger ADR threshold scoring

### 5.18 Architecture Decision Records (ADR)

ADRs are standalone documents capturing significant architecture decisions — technology/vendor selection, pattern choices, make-vs-buy, data governance, security architecture, or any decision that is hard to reverse.

**ADR vs A3 vs A3.N:**
- **A3** = governance state tracking inside an artifact (who decided what, at what authority, verified or not)
- **A3.N** = inline rationale detail block below the A3 table — Rationale, Alternatives, Tradeoffs, Implications per decision; lightweight middle tier between A3 and ADR
- **ADR** = standalone full-context document (situation, options analysis, rationale, consequences) — created when 2+ threshold indicators apply
- **A5** = cross-reference appendix inside artifacts listing related ADR-NNN IDs

**ADR lifecycle:** `Candidate → In Progress → Completed → Superseded (by ADR-NNN) | Deprecated`

**ADR threshold:** `ea-interviewer` suggests an ADR when 2+ of 8 indicators apply: technology/vendor selection, high cost/risk, hard to reverse, make-vs-buy, contested by stakeholder, affects data governance / security / compliance / principles.

**`/ea-adrs` modes:** `generate` (writes ADR Register), `status` (inline summary), `new` (create ADR from template), `update ADR-NNN <field> <value>`

**Templates:** `architecture-decision-record.md` (individual ADR), `adr-register.md` (aggregate register)

### 5.19 Zachman Diagram

The Zachman Diagram is a cross-cutting classification artifact mapping all engagement content across the 6×6 grid (Rows: Contextual → Functioning; Columns: What / How / Where / Who / When / Why). Row 6 (Functioning) is always 🚫 — it represents the running enterprise, not a specification.

**Coverage indicator:** ✅ Populated / ⚠️ Partial / ❌ Empty / 🚫 Out of scope

**`/ea-zachman` modes:** `generate` (auto-populate from existing artifacts), `review` (inline 6×6 matrix with % coverage), `gap` (prioritised gap list with remediation actions), `interview` (guided Q&A row by row), `classify <artifact>` (cell classification for any artifact/concept)

**Template:** `zachman-diagram.md`

### 5.20 Governance Artifacts

Three governance templates covering Preliminary through Phase H:

| Template | Phase | Purpose |
|---|---|---|
| `governance-framework.md` | Prelim | Enterprise governance structure: ARB ToR, decision rights, ADM tailoring, compliance process |
| `implementation-governance-plan.md` | G | Engagement-specific governance: review schedule, checkpoints, waiver process, escalation |
| `change-register.md` | H | Aggregated view of all ACR artifacts |

Created via `/ea-artifact create <template-name>` or generated automatically by `/ea-changes`.

### 5.21 Diagram Generation

Diagrams are generated and rendered through two paths:

**`ea-diagram` agent** — creates `.mmd` (Mermaid), `.dot` (Graphviz), or `.drawio` files. Uses a standard diagram catalogue per artifact type (e.g., Architecture Vision → motivation map + stakeholder power/interest grid; Business Architecture → capability map + process flow + org map). Naming convention: `{artifact-id}-{diagram-type}.mmd` in `EA-projects/{slug}/diagrams/`.

**`/ea-generate png|svg`** — renders `.mmd` files to images using mermaid-cli (`mmdc`). Auto-discovers `mmdc` on PATH, falls back to `npx -y @mermaid-js/mermaid-cli`. Options: `--theme`, `--bg`, `--all` (batch render all `.mmd` in the engagement).

**Diagram inclusion in deliverables (default on):** When generating docx or pptx, `/ea-generate` automatically:
1. Scans `diagrams/{artifact-id}-*.png` for pre-rendered images
2. Auto-renders any `{artifact-id}-*.mmd` without a matching PNG
3. Passes the diagram list to the script via `--diagrams @/tmp/ea-diagrams-{artifact-id}.json`
4. Embeds diagrams as a final appendix (docx) or appended slides (pptx)

No prompt is shown — diagrams are included by default when they exist.

### 5.22 Engagement Review and Migration

**`/ea-engage-review`** runs a full-scope consistency, alignment, governance, and quality review for the active engagement. Produces an Engagement Review Report covering:
- ADM phase coverage and artifact completeness
- Motivation chain traceability (DRV→G→OBJ)
- ADR status (Candidate/In Progress counts, stale/overdue)
- Governance and compliance gaps
- Zachman coverage summary

**`/ea-migrate`** aligns a legacy engagement with the current plugin version's templates and conventions. Applies non-destructive structural patches (adds missing appendices, missing frontmatter fields, missing compliance notes). Use `--report` to preview without applying.

**`/ea-consistency`** runs a focused consistency check without the governance and quality sweep of `/ea-engage-review`. All modes are read-only.

| Mode | Args | What it checks |
|---|---|---|
| Full | (none) | Cross-artifact contradictions, naming consistency, requirement traceability, phase alignment, ID reference validation |
| Artifact | `artifact <id>` | Within-artifact section consistency (same ID labelled differently in §3 vs §14) + ID refs scoped to that file |
| IDs only | `--ids` | Fast scan: builds ID definition registry, reports broken references (ID used but not defined) and orphaned IDs (defined but never referenced elsewhere) |
| Any + report | `--report` | Suppresses interactive menu; prints full report inline |

**Post-artifact-save sequence:** After every artifact write, the writing agent or command automatically runs Tier 1/2/3 compliance silently. If failures are found, the user is offered inline remediation before proceeding. Regardless of compliance outcome, the user is then offered to run `/ea-consistency artifact <id>` or `/ea-engage-review`. This sequence does not apply to generated register files (risk-register, adr-register, change-register, zachman-diagram).

### 5.23 Research & References

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

### 5.24 Engagement Session Rules

Each engagement folder contains `.claude/rules/ea-engagement.md` — a small rules file loaded by Claude Code on every session in the engagement directory. It enforces persistent behavioural guardrails without duplicating them in CLAUDE.md or agent instructions:

- **Session start** — require `/ea-open` before proceeding unless user explicitly skips
- **Artifact protection** — never modify `reviewStatus: Approved` artifacts without explicit confirmation; read frontmatter before any modification
- **Concept SST** — direct Claude to `ea-concepts.md` for all concept definitions; do not paraphrase ADM phases from memory
- **ID scheme** — enforce unified IDs (DRV-NNN, G-NNN, etc.); reject obsolete domain-prefixed variants

The file is seeded by `/ea-new`, backfilled silently by `/ea-open` for legacy engagements, and detected as a gap by `/ea-migrate` if absent.

### 5.25 Security Architecture (v0.9.25)

`/ea-security-review` provides a structured security audit aligned to SABSA, ISO 27001, and NIST CSF 2.0. It operates across a full engagement or against a single artifact.

- **`ea-security-auditor`** — detects security control gaps, maps artifacts to SABSA ADM layers, ISO 27001 Annex A controls, and NIST CSF 2.0 functions; produces a prioritised remediation report
- **`ea-security-advisor`** — answers security architecture Q&A in engagement context; supports security decisions and ADR threshold scoring for security-relevant choices
- **`ea-security` skill** — provides SABSA ADM mapping tables, ISO 27001 control reference, NIST CSF function definitions, per-artifact security checklists, and security interview question banks consumed by ea-interviewer

### 5.26 Engagement CLAUDE.md

The per-engagement `CLAUDE.md` is a **pointer document**, not a data dump. It contains identity fields, a one-sentence vision, engagement state counts (artifact totals, open decisions, research items), a pointer table to content locations, and a quick-command reference. Full strategic detail (goals, objectives, strategies, drivers) lives in `engagement.json → direction` and artifact files only — it is never copied into CLAUDE.md.

### 5.27 Role Catalogue (v0.9.27)

`/ea-roles` provides access to a canonical 15-role catalogue covering all EA engagement roles and generates a per-engagement Role Catalogue artifact.

**Canonical role set:** 15 roles across four domains — Governance, Architecture, Business, and Delivery — with full attribute profiles: description, responsibilities, typical tasks, RACI defaults, triggering events, cadence, and escalation path.

**Source:** `skills/ea-engagement-lifecycle/references/role-catalogue.md`

**`/ea-roles` modes:**

| Invocation | Effect |
|---|---|
| `/ea-roles` | Summary table — all 15 roles with ID, name, domain, one-line description |
| `/ea-roles <ROLE-ID>` | Full entry for one role (all extended attributes) |
| `/ea-roles --domain <domain>` | Filtered summary; valid domains: `governance`, `architecture`, `business`, `data`, `application`, `delivery` |
| `/ea-roles --generate` | Generate `role-catalogue.md` artifact in the active engagement (`artifacts/phase-a/`) |
| `/ea-roles --update <ROLE-ID>` | Assign a named individual and organisation unit to a role in the engagement's Role Catalogue |

**Template:** `templates/role-catalogue.md`

### 5.28 Decide vs Defer Framework and PAD Management (v0.9.30)

A structured decision-quality framework prevents premature commitments and reduces decision rework across the engagement lifecycle.

**Decide vs Defer Matrix — 5-factor assessment:**

| Factor | Question | Ratings |
|---|---|---|
| Evidence | How much evidence supports this decision? | Strong / Moderate / Weak |
| Reversibility | Can this be undone within 6 months without major cost? | High / Medium / Low |
| Impact | If wrong, how many teams or systems are affected? | Low / Medium / High |
| Urgency | What happens if delayed 90 days? | No harm / Some cost / Critical |
| Capability | Does the team have the skills to execute? | Ready / Learnable / Gap |

**Verdicts and actions:**

| Verdict | Condition | Action |
|---|---|---|
| **Decide now** | Evidence = Strong, Reversibility = High, Capability = Ready/Learnable | Log to A3 as committed; offer ADR |
| **Defer** | Evidence = Weak OR Reversibility = Low OR Impact = High | Create PAD-NNN with constraint boundaries, evidence requirements, resolution path, expiry date |
| **Decide with guardrails** | Evidence = Moderate, Reversibility = Medium, Urgency = Some cost | Log to A3 with guardrails note; schedule evidence review |
| **Premature** | Specific tech/pattern in Phase A before B–D analysis | Flag as premature; convert to PAD-NNN with constraint boundaries |
| **Risky commit** | Urgency = Critical AND Evidence = Weak | Log with risk flag; require executive sign-off |

**PAD-NNN (Pending Architecture Decision) template:**
- Lightweight deferred-decision artifact with constraint boundaries, candidate options, evidence required, resolution path, expiry date, and consequences of premature commitment
- Created by `ea-interviewer` when user types `d: {statement}` during interview, or when a decision is flagged as premature
- Linked to GAP-NNN, WP-NNN, and ADR-NNN via frontmatter fields
- Compliance rule T4-PAD: open PADs must have expiry within 90 days and defined resolution path

---

### 5.29 Enterprise/Program Requirements Split and NFR Sub-Types (v0.9.35)

Requirements scope terminology aligned to standard EA language: Corporate → **Enterprise** (org-wide standards, read-only content), Project → **Program** (engagement-specific, fully editable). Legacy `requirements-index.json` files with old values are automatically migrated on next write; `/ea-migrate` scan 3h offers bulk rename.

**NFR sub-type classification:** Non-Functional Requirements now carry two mandatory fields:
- **NFR Sub-Type** — one of 9 ISO/IEC 25010 categories: Availability, Reliability, Performance, Security, Usability, Maintainability, Portability, Compatibility, Recoverability
- **Measurable Target** — quantifiable threshold (e.g. 99.9% uptime, RTO 4h, <200ms p95 response time)

A **NFR Coverage Checklist** in the requirements register template tracks which categories have at least one entry. `/ea-interview start phase requirements` runs a structured NFR discovery session with one discovery question and measurable target prompt per category. `/ea-grill --skill requirements` produces an NFR coverage scorecard (9 categories × covered/missing/no target), traceability gap list, and proceed/pause/rework verdict.

---

### 5.30 Publish Readability Pass and Quality Modes (v0.9.36)

Shared quality rules defined in `skills/ea-artifact-templates/references/publish-quality.md` and applied at three touchpoints:

**`/ea-publish` Steps 5b + 5c:**
- **Readability Pass (5b):** Scans the assembled document for blocking issues (placeholder text, `TBD`/`TODO` markers, `⚠️ Not answered` fields, broken image paths, surviving guidance comments) and non-blocking issues (oversized tables, sections lacking narrative, terminology inconsistencies). Blocking issues trigger a fix/mark/abort choice. Non-blocking issues appear in a `## Publication Quality Notes` section.
- **Rewrite Pass (5c):** AI-assisted pass adds brief narrative introductions to sections that open with a table, transition sentences between back-to-back sections, and standardises inconsistent terminology. Each insertion is tagged `<!-- ai-inserted -->`. Executive Mode (`--executive`) runs blocking checks only; skips the rewrite pass.

**`/ea-review` action (f) — per-artifact quality check:** Scans the open artifact against publish-quality.md rules and reports table sizes, placeholder text, broken images, and narrative gaps scoped to that artifact. Each finding can be added as a review comment with one keystroke.

**`/ea-consistency --quality`:** Engagement-wide quality scan across all artifacts. Aggregates findings by artifact with ⚠️/ℹ️/✅ severity markers. Combinable with `--report` for inline output.

---

### 5.31 Direction Statement Quality (v0.9.37)

Quality rules for all 9 direction item types defined in `skills/ea-engagement-lifecycle/references/grill-direction-quality.md`. Applied at three touchpoints:

**Four concern categories:**
- **Miscategorization** — detects items entered in the wrong bucket (e.g. a measurable time-bound statement as a Goal instead of an Objective, a course-of-action statement as a Goal instead of a Strategy)
- **Missing evidence** — Drivers, Issues, and Problems must cite supporting evidence; flagged if the evidence field is empty
- **Isolated items** — items with no links to other direction elements (orphan Goals, unlinked Strategies, etc.)
- **Ambiguous phrasing** — vague or generic statements ("Improve performance", "Enhance customer experience") flagged as Advisory

**`/ea-direction --quality`:** Engagement-wide scan across all parsed direction items; groups findings by severity (⚠️ Warning / ℹ️ Advisory / ✅ clean); offers jump to revision or grill.

**`/ea-grill --skill direction`:** Interactive deep review of direction items in any artifact; each item type has dedicated challenge questions; added to Architecture Vision recommended skill note.

**`/ea-interview start engagement` — Part 3 inline challenge:** After each direction item is captured during the Motivation part, the interviewer applies quality rules inline: miscategorization is challenged immediately with a reclassification offer; missing evidence prompts for a citation; ambiguous phrasing is flagged. Items declined for revision are noted with a `⚠️ Quality flag` tag. At the end of Part 3, a **Direction Quality Summary** is presented before proceeding to Part 4, with option to revisit flagged items.

**Integration points:**
- `ea-interviewer` — `d:` shortcut triggers 5-factor assessment inline during any interview; advanced decision quality check (post-A3 logging) runs the same assessment for Strategic/High-cost/High-risk decisions
- `ea-grill` — Decision-Specific Grilling Protocol with 5 layers: Decide vs Defer Matrix, Premature Decision Detection, Evidence Sufficiency Check, Political Alignment Probe, Phase-Appropriateness Check
- `phase-interview-questions.md` — `[DECISION]` quality questions added to all 10 phases probing evidence, optionality, reversibility, and political alignment
- `compliance-check.md` — 5 new Tier 4 rules: T4-PREMAT (premature detection), T4-EVID (evidence quality), T4-POLIT (political alignment), T4-PAD (PAD hygiene), T4-WPEVID (work package evidence gating)
- Artifact templates — ADR template includes Evidence Assessment, Decision Timing, and Political Alignment sections; Gap Analysis includes Gap-to-Decision Mapping and orphan gap flagging; Architecture Roadmap includes PAD Resolution Tracking and Evidence-Gated Prioritisation

### 5.32 Formal Concept Definitions for Value Stream, Business Process, and Use Case (v0.9.38)

Three business-architecture-specific concepts elevated to first-class formal concept status in the canonical concept reference (`ea-concepts.md`), with full definitions, traceability chains, and updated artifact templates.

**New concept definitions:**
- **Value Stream (VS-NNN)** — end-to-end chain of activities delivering stakeholder value from trigger to outcome; composed of Business Processes, exercises Capabilities, traces to Goals and Strategies
- **Business Process** — structured, repeatable set of activities with defined actors, inputs, outputs, and decision points; component of a Value Stream
- **Use Case (UC-NNN)** — discrete goal pursued by a specific actor; consumes Business Processes, generates Requirements

**Traceability chain:**
```
G-NNN / STR-NNN ──► CAP-NNN ──► VS-NNN ──► Process ──► UC-NNN ──► REQ-NNN
```

**Motivation Framework diagram updated:** Value Streams inserted between Capability Model and Operating Model; Business Processes and Use Cases inserted between Value Streams and Requirements Register.

**Disambiguation table updated:** Three new rows in the PRD Core Concepts disambiguation summary; Quick Reference Table in `ea-concepts.md` expanded from 15 to 19 rows (including the 3 new concepts).

**Business Architecture template updated:** New §8a Traceability Summary section with explicit chain guidance; enhanced guidance notes in §3 Capabilities, §3a Value Streams, and §4a Use Case Catalog with orphan/gap flagging rules.

**Brainstorm pad updated:** Domain-specific category cards for Business Architecture (Value Streams, Use Cases, Processes), Data Architecture (Conceptual Data Model, Logical Data Model), and Technology Architecture (Platforms, Languages, Infrastructure, Network).

### 5.33 Two Layers of Intent: Business Change vs EA Enablement (v0.9.39)

New canonical section in `ea-concepts.md` that distinguishes **business architecture concepts** (what the business wants to achieve) from **EA/TOGAF program concepts** (how the EA function governs and enables that change). Addresses a common source of miscategorization where both layers use identical vocabulary (Goal, Use Case, Requirement) but describe different subjects.

**New content:**
- **Core distinction table** — Business Architecture = change; EA/TOGAF = control
- **Structural model** — four-layer stack with EA sitting cross-cutting across the stack, not inside the business layer
- **Naming conventions** — explicit prefixes (`Business Use Case`, `EA Capability Use Case`, `Architecture Requirement`) to remove ambiguity while retaining unified ID scheme
- **Quick test** — "Would this still exist without the EA team?" to disambiguate any item
- **Worked example** — AI in case management, cleanly separated into business layer (auto-triage, accuracy thresholds) and EA layer (governance process, model validation standards)
- **Relationship mapping table** — how Business Goals drive solution initiatives that are governed by EA Capability Use Cases
- **When to surface** — guidance for Phase A interviews, Phase B Business Architecture, `/ea-direction --quality`, and `/ea-grill`

**Disambiguation Checklist updated:** New step 0 — tests whether the subject belongs in the EA/TOGAF layer before applying concept-level tests.

**Common Confusions table updated:** Two new rows covering the "Define governance process for AI projects" vs "Automate case management with AI" ambiguity.

### 5.34 Mermaid Diagram — Business vs EA Artifact Separation (v0.9.40)

A validated Mermaid diagram inserted into the `## Two Layers of Intent` section of `ea-concepts.md` between the Structural Model prose and the Naming Conventions table. The diagram renders three subgraphs (Business Architecture, Solution / Initiative, EA / TOGAF) with solid intra-domain arrows and dotted cross-cutting governance/enablement arrows, plus color-coded styling.

**Diagram content:**
- **Business Architecture** subgraph — Vision/Mission → Goals & Objectives → Capabilities → Value Streams & Processes → Business Use Cases → Business Requirements
- **Solution / Initiative** subgraph — Projects & Epics → Solution Implementations
- **EA / TOGAF** subgraph — Architecture Principles → Standards & Reference Architectures → EA Capability Use Cases → Architecture Requirements → Governance Processes → Architecture Decisions
- **Cross-layer dotted edges:** Business Goals informed by Principles; Projects governed by EA Capability Use Cases; Implementations comply with Architecture Requirements; Governance Processes enforce Projects; Architecture Decisions guide Implementations.

**Purpose:** Makes the artifact-type separation immediately visual for stakeholders and interviewers.

### 5.35 Two Layers Integration — Cross-Artifact, Interview, Grill, and Brainstorm (v0.9.41)

The Two Layers of Intent distinction (business change vs EA enablement) is now woven into every touchpoint where concepts are captured or reviewed.

**Updated files:**
- `agents/ea-interviewer.md` — Step 7c-1 adds an explicit **Two Layers check** before the generic concept check. Detects when an answer describes an EA-layer subject (governance, standard, review board, reference architecture) but is being captured in a business-layer artifact/field, or vice versa. Surfaces the "Would this still exist without the EA team?" quick test and offers reclassification.
- `skills/ea-artifact-templates/references/cross-topic-detection.md` — New signal categories: **Two Layers (EA-layer)** detects governance/standard/review-board content in business-layer artifacts and routes to Governance Framework or Architecture Principles; **Two Layers (Business-layer)** detects customer journey/revenue stream content in EA-layer artifacts and routes to Business Architecture. Added to Signal Map and Signal Detection Cues.
- `skills/ea-artifact-templates/references/phase-interview-questions.md` — Phase A Goals question and Phase B Use Cases question each include a **Layer test** that flags EA-layer subjects masquerading as business concepts.
- `skills/ea-engagement-lifecycle/references/grill-direction-quality.md` — Direction quality scan now includes a **Two Layers** categorization warning and a **Two Layers test** probe question.
- `skills/ea-interview-ui/references/brainstorm-app.jsx` — Brainstorm category hints updated: "Concerns" now flags layer-mixing concerns; "Goals & Vision" prompts the Two Layers test.
- `commands/ea-grill.md` — New **Two Layers challenge** paragraph in Step 5: when grilling Business Architecture, Architecture Vision, Requirements Register, or Stakeholder Map, explicitly challenge mixed-layer content (e.g., "governance process" labeled as a Business Use Case).
- `templates/business-architecture.md` — Practitioner Tip and Use Case Catalog guidance both include Two Layers checks.
- `templates/architecture-vision.md` — Practitioner Tip and Goals guidance both include Two Layers checks.
- `templates/requirements-register.md` — Guidance section includes Two Layers check for distinguishing Business Requirements from Architecture Requirements.
- `templates/seeds/brainstorm-notes.md` — New **Two Layers of Intent — Brainstorm Prompt** section with the quick test and layer separation instructions.

---

### 5.36 Bundled Grill-Me Skills (v0.9.42)

The 9 core grill-me skills are now bundled directly inside ea-assistant, making it self-contained. Users no longer need the separate grill-me plugin installed for `/ea-grill` to function.

**Added skills:**
- `skills/grill-me-stress-test/SKILL.md`
- `skills/grill-me-premortem/SKILL.md`
- `skills/grill-me-decision/SKILL.md`
- `skills/grill-me-design/SKILL.md`
- `skills/grill-me-software-design/SKILL.md`
- `skills/grill-me-infra-design/SKILL.md`
- `skills/grill-me-artifact/SKILL.md`
- `skills/grill-me-diagram/SKILL.md`
- `skills/grill-me-boardroom-strategy/SKILL.md`

**Updated files:**
- `commands/ea-grill.md` — Skill ID column in Step 2 mapping table updated to use fully-qualified `ea-assistant:grill-me-*` names. The `practitioner`, `maturity`, `failure-mode`, `requirements`, and `direction` skills are unchanged (they load from reference files within ea-assistant).

---

### 5.37 Plugin Streamlining (v0.9.43)

Reduced slash command and skill count while preserving all existing behaviour.

**Skills: 18 → 10** — The 9 individual `grill-me-*` skill directories are replaced by a single `skills/ea-grill-skills/SKILL.md` containing all 9 modes as named sections. `/ea-grill` loads the consolidated skill and jumps to the matching `## Mode:` section.

**Commands: 35 → 31** — Four thin commands folded into existing hubs:
- `ea-next` → `ea-status --next` (next-action algorithm now a flag on the dashboard command)
- `ea-direction` → `ea-status --direction` (Direction Register now a flag on the dashboard command)
- `ea-summary` → `ea-artifact summary` (executive summary management now a subcommand of the artifact hub)
- `ea-reorganize` → `ea-migrate --reorganize` (file-move utility now a flag on the migration command)

All cross-references in commands and skill reference files updated to use the new entry points.

---

### 5.38 Ad-hoc Note Capture with Lifecycle (v0.9.45)

**`/ea-note [text] [--artifact <id>] | resolve <path>`** — quick-capture notes from anywhere in the engagement lifecycle.

- **Standalone capture:** Run `/ea-note` with or without inline text. The note is saved immediately to `artifacts/{phase}/notes/adhoc/` (or `cross-cutting/` if no phase active). A routing suggestion is offered after each save — classify as requirement, concern, ADR candidate, or cross-phase flag based on text content.
- **Artifact annotation:** `--artifact <id>` to annotate a specific artifact. Choose inline (blockquote callout inserted into the artifact markdown) or linked (separate note file with frontmatter back-reference).
- **Note lifecycle:** Every note includes `status: Open`, a `## Resolution` section, and lifecycle fields (`resolvedDate`, `resolvedBy`). Run `/ea-note resolve <path>` to walk through: resolved-by IDs, per-ID description, rationale, impact, and any residual unresolved impacts.
- **Session interrupt:** Type `n: {text}` during any `/ea-interview` or `/ea-grill` session to capture a note without breaking flow — the session re-presents the current question or revision after confirming the save.
- **Listing and management:** `/ea-notes list` now shows an Ad-hoc Notes section with Status column. `r) Resolve a note` action added to the notes menu.

---

### 5.39 Detail File Cross-Linking and Inline Notes (v0.9.46)

Bidirectional cross-linking between detail files, inline note annotations with Open/Resolved lifecycle, and a generated index.

- **Cross-linking:** `relatedItems: []` frontmatter array is the machine-readable source of truth. A `## Related Items` table in each detail file renders links as human-readable markdown using same-directory relative paths.
- **`/ea-detail link {ID1} {ID2} [relationship]`** — creates a bidirectional link with automatic inverse label. Handles legacy files missing `## Related Items`. Updates `lastModified` in both files.
- **`/ea-detail check [ID]`** — four integrity checks: link existence, back-link symmetry, table/frontmatter sync (full-token matching), and open notes. Interactive fix for single-file mode.
- **`/ea-detail note resolve {ID}`** — lists open `📌` notes in a detail file; user selects one and enters resolution text; blockquote updated in-place.
- **`/ea-detail index`** — generates `artifacts/details/_index.md` grouped by type with Related Items and Open Notes columns.
- **Updated `list` mode** — type-grouped output with `### {Type}` headings, `--type {type}` filter, Open Notes column, cross-link footer.
- **Updated `view` mode** — related-items nav line after content; 5-action menu with "Resolve a note" option; consistency check extended to all 4 check types.
- **`/ea-note --detail {ID}`** — appends inline open `📌` blockquote to a detail file's `## Notes` section; handles legacy files missing that section.

---

### 5.40 ABB, SBB, and User Story Concepts (v0.9.47)

Introduced Architecture Building Blocks (ABB-NNN), Solution Building Blocks (SBB-NNN), and User Stories (STY-NNN) across the plugin to support the full TOGAF hierarchy: Capability → Requirement → ABB → SBB → Story → Task.

- **New concepts in `ea-concepts.md`:** ABB-NNN, SBB-NNN, STY-NNN — each with full structured definition (What it IS, Structural parts, What it is NOT, Common confusions, Practitioner Notes, TOGAF placement, ArchiMate, ID scheme). Disambiguation checklist extended with Step 13 (ABB→SBB→Story→Task branch). Common Confusions table extended with 3 new rows. ASCII hierarchy diagram extended to show the full ABB→SBB→Story→Task tail.
- **Requirements Register template:** NFR Sub-Type expanded from 9 to 19 values. Optional `### Sample Tests` and `### Stories` subsections added to both Enterprise and Program requirement blocks. `Sample Tests` column added to the Requirements Summary table.
- **Business Architecture template:** Capability table expanded with `Capability Type` (Business / Technology) and `Domain` columns. Per-capability `#### ABBs for CAP-NNN` subsection template added with full ABB table.
- **Application Architecture template:** Per-component `#### ABBs for {component}` section with `<!-- GUIDANCE -->` comment and ABB table added to each application component block.
- **Technology Architecture template:** `## 3a. Architecture Building Blocks` global ABB register (columns: ABB-NNN, Name, Description, Satisfies REQ-NNN, Implemented by SBB-NNN). `## Solution Building Blocks Register` placed near end of template before Appendix A3, with SBB table (SBB-NNN, Name, Implements ABB-NNN, Vendor / Source, Version, Constraints / Lock-in Risk).
- **Cross-topic detection:** 4 new signals added — User Story pattern in Requirement, vendor name in ABB, implementation detail in Capability, and "must/shall" language in Story. 3 new Signal Map rows.
- **`/ea-grill`:** Layer 6 — Concept Type Validation added to Step 5, with four probe types: Capability vs Implementation, Requirement vs Story, ABB vs SBB, Story vs Task.
- **ID Scheme:** ABB-NNN, SBB-NNN, STY-NNN registered in `CLAUDE.md`.

---

### 5.41 ABB, SBB, and User Story Registers (v0.9.49)

Dedicated register commands for managing ABB-NNN, SBB-NNN, and STY-NNN entries as first-class objects.

- **`/ea-abbs [mode]`** — Architecture Building Block Register. Modes: `generate` (writes register from artifacts), `status` (inline summary), `new` (create entry from template), `update ABB-NNN <field> <value>` (single field update).
- **`/ea-sbbs [mode]`** — Solution Building Block Register. Modes: `generate`, `status`, `new`, `update SBB-NNN <field> <value>`.
- **`/ea-stories [mode]`** — User Story Register. Modes: `generate`, `status`, `new`, `update STY-NNN <field> <value>`.

---

### 5.42 Architecture Principles Register (`/ea-principles`) (v0.9.49)

Dedicated management register for Architecture Principles (BP/DP/AP/TP-NNN). Principles are established in the Preliminary phase as the non-negotiable rules governing all downstream architecture decisions.

- **Modes:** `list` (default — summary by type with orphan and violation flags), `add` (interactive 4-field capture: Name, Statement, Rationale, Implications), `update {ID} <field> <value>`, `trace [ID]` (shows ADRs, constraints, and artifacts governed by the principle; flags potential violations)
- **ID scheme:** BP-NNN (Business), DP-NNN (Data), AP-NNN (Application), TP-NNN (Technology) — zero-padded 3-digit, TOGAF-standard
- **Source Policy link:** each principle optionally references a POL-NNN that mandates it, completing the governance chain: Policy → Principle → Constraint → Solution
- **Violation detection:** `trace` mode scans completed ADRs for decisions that may contradict the principle's Statement; flags candidates for human review
- **Skill:** `ea-principles-management` — provides ID assignment rules, 4-field completeness checks, traceability hierarchy, and violation heuristics; loaded automatically by `/ea-grill` when reviewing the Architecture Principles artifact

---

### 5.43 Business Drivers Register (`/ea-drivers`) (v0.9.50)

First-class management of Business Drivers (DRV-NNN) as engagement-level motivation objects stored in `engagement.json → direction.drivers[]`.

- **Modes:** `list` (grouped by type External/Internal, with orphan detection — drivers with no linked goal flagged), `add` (interactive capture: statement, type, priority, evidence, linkedGoals), `update DRV-NNN <field> <value>`, `trace DRV-NNN` (walks full DRV→G→OBJ→STR→WP motivation chain), `generate` (writes `artifacts/cross-cutting/drivers-register.md`)
- **ID scheme:** DRV-NNN (sequential, global) — IDs are assigned by reading the current max from `direction.drivers[]` and incrementing
- **Storage:** `engagement.json` is the source of truth; the generated register is a read-only output snapshot
- **Skill:** `ea-drivers-management` — ID assignment algorithm, traceability walk, orphan/cycle validation, register format

---

### 5.44 Architecture Gap Register (`/ea-gaps`) (v0.9.50)

First-class management of Architecture Gaps (GAP-NNN) stored in `engagement.json → direction.gaps[]`, covering both baseline-target gaps and motivation coverage gaps across all architecture domains.

- **Modes:** `list` (grouped by severity Critical → High → Medium → Low), `add` (interactive capture: statement, domain, severity, baseline, target, phase, linkedWorkPackages, linkedArtifact, status), `promote` (formalises raw gap prose from `/ea-trace --gaps` output into a GAP-NNN entry), `update GAP-NNN <field> <value>`, `trace GAP-NNN` (upstream: linked artifact and phase; downstream: linked WP-NNN and roadmap wave), `generate` (writes `artifacts/cross-cutting/gap-register.md` in two sections: Architecture Gaps / Migration Gaps)
- **ID scheme:** GAP-NNN for phases A–E/H; GAP-M-NNN for migration gaps (Phase F/G)
- **Severity escalation:** Critical+Open+no linkedWorkPackages → warning surfaced in `/ea-engage-review` step 4i and `/ea-gaps list`
- **Skill:** `ea-gaps-management` — schema definition, ID assignment, severity escalation rule, promote algorithm, two-section register format, relationship with `/ea-trace --gaps` (complementary, not superseded)

---

### 5.45 Seasoned Architect Lens (`/ea-lens`) (v0.9.50)

Opinionated engagement review from the perspective of a practitioner focused on what actually matters, not completeness theatre.

- **Eight lenses:** (1) Real Problem — signal vs noise; (2) Decision Quality — deferral pattern vs genuine optionality; (3) Real Risk — comfortable vs consequential risk tracking; (4) Stakeholder Reality — attention deficit for high-influence/low-support stakeholders; (5) Motivation Chain Integrity — DRV→G→OBJ→STR→WP breaks with practical implication; (6) Architecture vs Implementation Blur — premature vendor/tech specificity; (7) What a Seasoned Architect Would Do Next — 3–5 specific moves, not TOGAF steps; (8) The One Thing — single sentence, no hedging
- **`--quick` flag:** skips full artifact scan; uses `engagement.json` state only; produces lenses 1, 7, and 8
- **Output:** offered as save to `artifacts/cross-cutting/notes/lens-review-{date}.md`
- **Skill:** `ea-architect-lens` — loads `practitioner-tips.md`, `failure-modes.md`, `adm-phase-guide.md`

---

### 5.46 Phase-Adaptive Interviews and Brainstorms (v0.9.50)

`/ea-interview` and `/ea-brainstorm` now adapt to the active ADM phase using three mechanisms:

- **Phase intent preamble:** reads `adm-phase-guide.md` for the active phase; presents the top 3 objectives, top 4 key questions, and "decide now" Decision Flow items before the first question/pad launch; also surfaces prior-phase handoff context (open GAP-NNN entries and open PAD-NNN entries from the previous phase)
- **Engagement direction filter:** loads `engagement.json → direction` and surfaces only goals, objectives, drivers, and strategies relevant to the current phase per a TOGAF ADM intent mapping (Phase A: all goals and drivers; Phase B: capability-linked goals; Phase C: data/app-linked objectives; Phase D: technology-linked objectives; Phase E/F: strategy→WP coverage)
- **Dynamic question skipping** (interview only): before presenting each question, checks whether the corresponding field already has a non-placeholder value in existing phase artifacts; skips populated fields and reports a count at the start of the session
- **BRAINSTORM_DATA.subtitle:** set from the first objective in `adm-phase-guide.md` for the resolved phase, prefixed with `"This phase must: "`, rendered as a subtitle in the brainstorm pad header

### 5.47 EA Projects Git and GitHub Integration (`/ea-git`) (v0.9.51)

`/ea-git` manages `EA-projects/` as a git repository, enabling version control and optional GitHub collaboration for EA engagement content.

**Subcommands:**

| Subcommand | Purpose |
|---|---|
| `init` | Initialise `EA-projects/` as a git repo; create `.gitignore`; make initial commit; optionally create a private GitHub repo via `gh` CLI |
| `status` | Show branch, remote, uncommitted changes (grouped by engagement), and last 5 commits |
| `commit` | Stage all changes; auto-generate a contextual commit message from changed artifact names; confirm, edit, or cancel before committing |
| `push` | Push committed changes to the GitHub remote |
| `sync` | Pull with rebase then push — keeps local and remote in sync |
| `log` | Show commit history (last 20, graph format) |
| `remote` | View, set, or remove the GitHub remote URL |

**Key design decisions:**

- **Single repo for all engagements** — `EA-projects/` is the repo root; all engagements share one history. This keeps cross-engagement traceability simple and avoids per-engagement repo management overhead.
- **`EA-projects/.ea-workspace.json`** — repo-level config (gitInitialized, githubRepo, gitRemoteUrl, defaultBranch, createdAt); distinct from per-engagement `engagement.json`.
- **`git -C EA-projects/` pattern** — all git commands are scoped to the EA workspace; they do not affect any enclosing repo (e.g., the plugin development repo).
- **Interviews and brainstorm notes are tracked** — all session content is committed by default; privacy managed via GitHub visibility (private repo).
- **`.gitignore` template** — `templates/seeds/ea-gitignore.md` excludes `uploads/` (large client files), `tmp/`, and generated binary report files by default; `.ea-workspace.json` is tracked.
- **`gh` CLI integration** — GitHub repo creation uses `gh repo create --source EA-projects/ --remote origin` (no `--push`); the initial commit is made before GitHub operations so the push always has content to send.
- **`/ea-open` integration** — if `EA-projects/.git` exists, `/ea-open` appends a Version Control table (branch, remote, last commit, uncommitted file count) to the engagement summary.

**Sliced delivery:** Slice 1 (`/ea-git` command + `/ea-open` integration) is the foundation. Slices 2–4 (PR per artifact review, GitHub Issues sync, GitHub Project board) are separate PRs.

### 5.48 Motivation Concept Registers — Phase 1: Goals, Issues, Problems (v0.9.52)

Dedicated register management commands for three Phase A motivation concepts that previously had no standalone interface. All three follow the `/ea-drivers` pattern (list/add/update/trace/generate) and read/write from `engagement.json → direction.X[]`.

**`/ea-goals` (G-NNN):**
- List goals grouped by Domain (Business / Technology / Data / Application / Cross-cutting), with Type classification (Strategic / Operational / Capability / Compliance)
- `add` includes Two-Layers disambiguation check (flags EA-layer goals that belong in Governance Framework, not Architecture Vision) and Objective check (warns if statement contains a measure or deadline, suggesting it should be an Objective instead)
- `trace` walks: ← DRV-NNN → OBJ-NNN → STR-NNN → WP-NNN
- `generate` produces `artifacts/cross-cutting/goals-register.md`

**`/ea-issues` (ISS-NNN):**
- List issues grouped by Domain (Business / Technology / Data / Application / **Engagement**), with Type classification (Organisational / Process / Technology / Regulatory / Capability)
- The **Engagement** domain covers issues about the EA engagement itself (methodology, governance, team, tooling) — not an architecture domain, but a first-class classification for engagement health
- `add` begins with Issue vs Problem disambiguation: *"Is this concern systemic and broad, or specific and fixable?"*; includes specificity check if statement contains individual system names or numbers
- `trace` walks: ← DRV-NNN (contextual) → threatens G-NNN → feeds GAP-NNN
- `generate` produces `artifacts/cross-cutting/issues-register.md`

**`/ea-problems` (PRB-NNN):**
- List problems grouped by Domain (Business / Technology / Data / Application / **Engagement**), with Type classification (Operational / Technical / Data / Engagement / Compliance)
- `add` begins with Problem vs Issue disambiguation and systemic check (warns if statement sounds broad rather than specific); requires Observable Symptom field (ideally a number)
- `trace` walks: ← ISS-NNN (related issues) → blocks OBJ-NNN → generates REQ-NNN
- `generate` produces `artifacts/cross-cutting/problems-register.md`

**Engagement.json schema extensions** — new fields added to existing direction arrays:

| Concept | New fields |
|---|---|
| `goals[]` | `domain`, `type`, `status` |
| `issues[]` | `domain`, `type`, `severity`, `status` |
| `problems[]` | `domain`, `type`, `severity`, `status`, `symptom` (was previously free-text; now a required structured field) |

**Phase 2** (separate PR, v0.9.54): `/ea-objectives`, `/ea-strategies`, `/ea-opportunities`

---

### 5.49 Business Scenarios — TOGAF Phase A Technique (v0.9.53)

New command `/ea-scenarios` and template `templates/business-scenario.md` supporting the TOGAF 10 Business Scenario technique (§25.3.3).

**Command:** `/ea-scenarios [list|new|view|interview|trace|generate] [BS-NNN]`

**New ID prefix:** `BS-NNN` — Business Scenario (Phase A)

**Storage:**
- Index: `engagement.json → scenarios[]` (id, title, status, phase, path, linkedDrivers, linkedIssues, linkedProblems, linkedGoals, linkedObjectives, requirements, lastModified)
- Artifact: `artifacts/phase-a/business-scenario-BS-NNN.md`
- Summary register: `artifacts/cross-cutting/scenarios-register.md`

**Modes:**
- `list` — table of all BS-NNN with status, linked drivers/goals, and requirement count
- `new` — 9-step guided creation through all six TOGAF elements (Problem Statement, Objectives, Environment, Stakeholders, Actors, Requirements) plus Current/Target State narratives and Change Delta; writes artifact from template and indexes in engagement.json
- `view BS-NNN` — display full scenario artifact with compliance checklist status
- `interview BS-NNN` — scan for unfilled sections and guide completion question-by-question; updates artifact and index
- `trace BS-NNN` — walk full upstream (DRV/ISS/PRB) → scenario → downstream (G/OBJ/REQ) motivation chain; orphan detection and broken-link flagging
- `generate` — produce a Scenarios Summary Register cross-cutting artifact

**Template sections:** (1) Problem Statement with ISS/PRB/DRV links, (2) Objectives table with SMART check, (3) Environment (Internal / External / Technology Context), (4) Stakeholders and Concerns, (5) Actors — §5.1 Human Actors + §5.2 Computing Actors with Existing/To Be Built/To Be Modified status, (6) Requirements (REQ-NNN by domain with source tracing), (7) Current State Narrative with friction points, (8) Target State Narrative with success signals, (9) Change Delta table (Process / Data / Application / Technology), (10) Scenario Diagram (optional Mermaid), Traceability Appendix.

### 5.54 Concept Completions, TOGAF Technique Stubs, Schema Versioning (v0.9.59)

P4 (final band) of the 2026-06-10 improvement advisory:

1. **Eight concepts added to `ea-concepts.md`** (definitions, TOGAF/ArchiMate placement, distinctions, quick-reference rows): Service (SVC-NNN), Interface (IFC-NNN), Application/Technology Component (no new IDs — captured as ABB/SBB), Capability Increment, Plateau/Transition Architecture, Deliverable (vs Artifact vs Building Block), Architecture Partitioning (operationalised by `architectureLevel` + ADM tailoring), Enterprise Continuum (realised by the Architecture Repository). New ID prefixes **SVC-NNN** and **IFC-NNN** added to the ID Scheme and engagement-rules seed.
2. **TOGAF technique stubs:**
   - **Business Transformation Readiness Assessment** — new `templates/business-transformation-readiness.md` (12 readiness factors × readiness/urgency/difficulty, factor detail blocks, roadmap implications); Phase A artifact, reassessed at Phase E; registered in `artifact-descriptions.md`.
   - **Capability-Based Planning** — new `references/capability-based-planning.md` (capability as planning unit, increment quality tests, anti-patterns); wired into the `ea-roadmap` agent's work-candidate derivation.
   - **Interoperability Requirements** — new `skills/ea-requirements-management/references/interoperability-requirements.md` (business/information/technical categories, degrees 1–4, discovery checklist, REQ/IFC/STD capture conventions); wired into the Requirements-phase functional questions.
   - **Risk appetite & tolerance** — Risk Register template gains a `## Risk Appetite & Tolerance` section (appetite statement + per-rating tolerance/authority/escalation table); `/ea-risks accept` enforces the acceptance-authority column and warns when accepting outside appetite.
3. **Schema versioning** — `engagement.json` gains `schemaVersion` (integer, current 1) and `migrations[]` (audit trail appended by every `/ea-migrate` run); seed updated; migration-gap-catalogue detects their absence; `engagement-schema.md` adds a Source of Truth declaration (engagement.json masters direction/phases/artifact registry; generated registers are rendered views; file-mastered exceptions named).

---

### 5.53 Framework Lenses, Security F/H Completion, ADM Tailoring, Phase H Change Guide (v0.9.58)

P3 of the 2026-06-10 improvement advisory:

1. **Framework lenses** — new `skills/ea-framework-lenses/` skill: a pluggable mechanism mapping external prescriptive frameworks onto the ADM via a fixed lens-file contract (Pillars → ADM Mapping → Review Checklist → Interview Questions → Tagging Conventions). First lens: **AWS Well-Architected** (`references/aws-well-architected.md`, all 6 pillars). Consumed via `/ea-grill --skill waf` (pillar-by-pillar artifact review) and offered in Phase C-Data/C-App/D/E interviews when the engagement has cloud scope. Azure CAF / GCP frameworks are drop-in reference files. Lens findings land in existing registers (REQ/RIS/GAP/PAD) — never framework-specific stores; lenses do not participate in T1–T4 compliance.
2. **Security interview coverage completed** — Phase F (migration security: cutover protection, coexistence windows, secrets rotation, secure decommissioning, third-party access) and Phase H (ACR security impact, control drift, policy review cycles, incident-learning feedback) sections added to `security-interview-questions.md` and wired into the phase question bank. All 10 phases now have optional security sections.
3. **ADM tailoring** — `/ea-new` proposes a phase set from `architectureLevel` (e.g. Solution-level suggests opting out of Preliminary and Phase H), user-adjustable; opted-out phases get status `Not Applicable` + `optOutReason` in `phases{}` (reusing the existing status that `/ea-status` already excludes from progress), and their folders are not seeded. `/ea-phase` offers re-inclusion. Requirements and cross-cutting can never be opted out.
4. **Phase H change guide** — new `skills/ea-engagement-lifecycle/references/phase-h-change-guide.md`: change drivers, ACR triage flow, TOGAF three-way classification (Simplification / Incremental / Re-architecting) with tests, escalation rules with timeboxes, ADM re-entry mapping, and a per-ACR outputs checklist. Wired into `/ea-changes` (timebox flagging) and the Phase H interview facilitation notes.

---

### 5.52 Surface-Area Consolidation — Register Protocol, Review Lanes, Continuous Requirements (v0.9.57)

P2 of the 2026-06-10 improvement advisory:

1. **Register protocol** — the shared list/add/update/trace/generate mechanics of the five direction-register commands (`/ea-drivers`, `/ea-goals`, `/ea-issues`, `/ea-problems`, `/ea-gaps`) now live once in `skills/ea-engagement-lifecycle/references/register-protocol.md`. Each command shrank to a declarative Register Spec (prefix, storage, fields, link fields, trace chain, groupings, status transitions) plus its register-specific checks (Two-Layers, Issue↔Problem disambiguation, systemic/specificity warnings, gap severity escalation, `/ea-gaps promote`). Net ~915 lines removed; behavior unchanged. Concept definitions now point at `ea-concepts.md` instead of being restated inline.
2. **Review lane boundary** — `/ea-engage-review` explicitly composes `/ea-consistency` for its Consistency dimension (logic never restated); `--quick` now reports Consistency as `⏭ Skipped` instead of omitting it silently. (`/ea-consistency` is retained as the focused mechanical lane rather than folded — it owns `--ids`/`--details`/`--quality`/artifact modes and is referenced by seeded engagement rules in live engagements.)
3. **Continuous requirements** — `/ea-phase` runs a requirements check-in on every phase entry (open REQ-NNN items whose `phase` field matches, with an unaddressed-High warning), and completing the Requirements phase bridges directly into Phase A with the register carried as interview context.

---

### 5.51 Consumable Deliverables — Layered Publish, Reading Guide, Register Snapshots, On-demand Details (v0.9.56)

Four changes from the 2026-06-10 improvement advisory (`docs/reviews/improvement-advisory-2026-06-10.md`) targeting deliverable consumability and ceremony reduction:

1. **Layered publish (default)** — `/ea-publish` now defaults to a layered report: 3–5 page executive brief → per-artifact summaries (1–2 pages each, with links to full artifacts) → appendix index. Full-text embedding moved behind `--full`. Output: `artifacts/architecture-report-{date}.md`. All modes strip HTML guidance comments and treat `TBD`/`TODO` markers as blocking quality issues.
2. **Stakeholder reading guide** — every `/ea-publish` run writes `artifacts/index.md`: a one-screen "start here" map pointing to the latest report, executive summary, Architecture Vision, current-phase artifacts, and live registers.
3. **Register snapshot convention** — generated registers use stable, undated filenames (e.g. `risk-register.md`); regeneration archives the prior version to a `snapshots/` subfolder. Single `artifacts[]` entry per register. Convention: `skills/ea-artifact-templates/references/register-snapshot-convention.md`. Applies to all 14 register-generating commands.
4. **On-demand detail files** — `/ea-migrate` gap 3g is report-only and never bulk-creates empty detail stubs; detail files are created only when content is supplied (per-item selection + at least a Summary). Always excluded from `--auto`.

Review-command discoverability: `/ea-help` gains a "Which Review Command?" decision table; `/ea-grill` and `/ea-review` preambles state their lane and cross-reference the others.

---

### 5.50 Architecture Repository, Vendor/Horizon/Standards Registers, and Cross-cutting Sub-folders (v0.9.54)

**Architecture Repository** — shared org-wide store spanning multiple EA engagements and IT projects.

**Workspace structure:**
```
EA-Workspace/
├── workspace.json                     # workspace registry (projects[], repoPath, projectsPath)
├── Architecture-Repository/
│   ├── repo.json                      # repository config + ID counters
│   ├── vendor-landscape/              # VDR-NNN entries + vendor-index.md
│   ├── technology-horizon/            # THR-NNN entries + horizon-index.md
│   └── sib/standards/                 # STD-NNN entries + sib-index.md
└── EA-Projects/
    └── {slug}/                        # engagement folders
```

**New ID prefixes:** `VDR-NNN` (Vendor Landscape), `THR-NNN` (Technology Horizon), `STD-NNN` (Standards Information Base)

**New commands:**
- `/ea-repo [init|link|status|open]` — initialize workspace, link engagements to the repository, view repo status
- `/ea-vendors [list|add|update|link-sbb|archive]` — manage Vendor Landscape Register entries (VDR-NNN)
- `/ea-horizon [list|add|update|surface|link-adr]` — manage Technology Horizon Register with ring model (Adopt/Trial/Assess/Hold)
- `/ea-standards [list|add|link-constraint|surface]` — manage Standards Information Base (STD-NNN)

**Vendor/Horizon integration:**
- `/ea-sbbs new` — checks vendor-index.md for Architecture Repository match; warns on Sunset/EoL vendors; offers VDR link
- `/ea-adrs new` — for technology/vendor ADRs, checks THR (ring/rationale) and VDR (roadmap/lock-in); offers pre-population of §4/§6; back-links ADR-NNN into THR/VDR

**Cross-cutting sub-folders** — `artifacts/cross-cutting/` reorganized into three purpose-based sub-folders:
- `governance/` — ADR Register, Decision Register, Constraints Register, Policies Register
- `operations/` — Risk Register, Change Register, Concerns Register
- `context/` — Zachman Diagram, Role Catalogue
- `cross-cutting-index.md` — navigation hub (auto-maintained by register commands)

**Migration:** `/ea-migrate` gap check 3h detects flat cross-cutting files; `--reorganize` moves them to sub-folders and updates `engagement.json` paths.

---

## 6. Data Model

### Folder Structure

```
EA-projects/
└── {slug}/
    ├── .claude/
    │   └── rules/
    │       └── ea-engagement.md  # persistent session guardrails (session start, ID scheme, concept SST)
    ├── engagement.json           # all state: phases, artifacts, sessions, direction, metrics, optOuts
    ├── CLAUDE.md                 # pointer doc — identity + counts + locations; refreshed on /ea-open
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
| `/ea-status` | `[--next] [--direction]` | Portfolio dashboard — all engagements with progress, research count, opt-outs, non-standard flags; `--next` for next-action recommendation; `--direction` for Direction Register |
| `/ea-phase` | `[phase name]` | Start, navigate to, or resume an ADM phase |
| `/ea-interview` | `[web|voice|text|display]` | Run stakeholder interview; ADR threshold scoring; defaults to Web mode |
| `/ea-artifact` | `[create|view|list|summary]` | Create, view, or list artifacts; compliance check on view; `summary [refresh\|status]` for executive summary management |
| `/ea-brainstorm` | `[phase]` | Capture freeform thoughts before or during interviews |
| `/ea-generate` | `[artifact] [docx|pptx|mermaid|png|svg] [--theme] [--bg] [--all]` | Export artifact; embeds diagrams by default in docx/pptx; renders Mermaid to images via mmdc |
| `/ea-review` | `[artifact]` | Open artifact for review; runs compliance check; update review status |
| `/ea-grill` | `[artifact\|all] [--skill name]` | Deep-review artifact using a grill-me skill; auto-selects skill by type; apply findings with y/n/edit; `all` runs non-interactive batch review across all artifacts |
| `/ea-requirements` | `[list|add|edit|waive]` | Manage architecture requirements; corporate (read-only) and project scope |
| `/ea-constraints` | `[list|add|update|trace|impact] [--type] [--status] [--priority] [--owner] [--phase]` | Manage architecture constraints (CST-NNN); trace to artifacts and SBBs; assess impact |
| `/ea-policies` | `[list|add|update|trace|impact] [--type] [--scope] [--status]` | Manage architecture policies (POL-NNN); trace to constraints and principles; assess impact through linked constraints |
| `/ea-principles` | `[list|add|update|trace] [--type Business|Data|Application|Technology] [--status Active|Draft|Deprecated]` | Architecture Principles Register — manage BP/DP/AP/TP-NNN entries; `trace` detects ADR and constraint violations |
| `/ea-abbs` | `[generate|status|new|update ABB-NNN <field> <value>]` | Architecture Building Block Register — generate, view, create, or update ABB-NNN entries |
| `/ea-sbbs` | `[generate|status|new|update SBB-NNN <field> <value>]` | Solution Building Block Register — generate, view, create, or update SBB-NNN entries |
| `/ea-stories` | `[generate|status|new|update STY-NNN <field> <value>]` | User Story Register — generate, view, create, or update STY-NNN entries |
| `/ea-trace` | `[--gaps]` | Interactive traceability views — motivation chain from drivers to work packages; `--gaps` for consolidated gap report only |
| `/ea-decisions` | `[generate|status|rationale] [--audience] [--owner] [--domain] [--status] [--cost] [--impact] [--risk] [--artifact] [--authority]` | Generate Decision Register from all A3 logs; `rationale` mode backfills missing A3.N reasoning blocks |
| `/ea-adrs` | `[generate|status|new|update ADR-NNN <field> <value>]` | Manage Architecture Decision Records; auto-suggested by interviewer at 2+ threshold indicators |
| `/ea-risks` | `[generate|status|update RIS-NNN <field> <value>]` | Generate and maintain Risk Register by scanning all artifacts |
| `/ea-changes` | `[generate|status|update <ACR-ID> <field> <value>]` | Generate Change Register aggregating all Phase H ACR artifacts |
| `/ea-concerns` | — | Manage CON-NNN stakeholder concerns (Appendix A4) |
| `/ea-roles` | `[ROLE-ID] [--domain] [--generate] [--update ROLE-ID]` | Canonical 15-role catalogue — list, filter by domain, generate Role Catalogue artifact, assign named individuals |
| `/ea-zachman` | `[generate|review|gap|interview|classify <artifact>]` | Manage Zachman 6×6 classification diagram |
| `/ea-research` | `[add|note|link|list|view <item>|apply [artifact-id]]` | Manage research library; synthesise research against deliverables |
| `/ea-notes` | `[list|view|edit|delete]` | List, view, edit, or delete interview notes, brainstorm notes, and review files |
| `/ea-note` | `[text] [--artifact <id>] \| resolve <path>` | Quick-capture an ad-hoc note with Open/Resolved lifecycle; `resolve` records resolution with rationale and impact |
| `/ea-detail` | `[new|view|list|sync|link|check|note resolve|index]` | Create, view, list, sync, cross-link, and integrity-check item detail files; generate index; add and resolve inline notes |
| `/ea-consistency` | `[artifact <id>] [--ids] [--report]` | Focused consistency check — cross-artifact, within-artifact section contradictions, or ID reference scan only |
| `/ea-engage-review` | — | Full-scope engagement consistency, alignment, governance, and quality review |
| `/ea-migrate` | `[--report] [--reorganize]` | Align legacy engagement to current plugin version conventions; `--reorganize` moves flat-path artifacts into correct phase subfolders |
| `/ea-publish` | `[markdown|word|both] [--full|--executive]` | Layered stakeholder report (default) or full consolidated document (`--full`) via Pandoc; pre-publish compliance check; writes `artifacts/index.md` reading guide |
| `/ea-brief` | `[--focus decisions\|risks\|gaps\|strategy] [--save]` | Synthesised one-page engagement brief — ranked decisions, gaps, risks, open concerns |
| `/ea-workshop` | `[start|resume|export|list]` | Facilitated multi-stakeholder workshops — WS-NNN minutes, agenda, decisions, actions |
| `/ea-arb` | `[new|list|view|close]` | ARB meeting minutes — ARB-NNN, quorum, decisions, propagate to ADR register |
| `/ea-config` | `[section]` | Configure plugin settings, engagement rules, opt-outs, and refresh CLAUDE.md |
| `/ea-security-review` | `[artifact-id] [--report]` | Security audit — SABSA ADM mapping, ISO 27001 Annex A, and NIST CSF 2.0 coverage; full engagement or single artifact |
| `/ea-help` | — | Command reference, interview shortcuts, research agent guide |

---

## 8. Agents

| Agent | Role | Invoked by |
|---|---|---|
| `ea-facilitator` | Guides users through ADM phases; reads facilitatorStyle config | `/ea-phase`, `/ea-open` |
| `ea-interviewer` | Conducts structured interviews; all 4 modes, question preview, brainstorm, cross-topic detection, ADR threshold scoring | `/ea-interview` |
| `ea-roadmap` | Creates and manages the Architecture Roadmap in Review / Artifact-informed / Clean-slate mode | Ask Claude: "Let's build the roadmap" or "Review the roadmap" |
| `ea-requirements-analyst` | Extracts structured requirements from uploaded documents | `/ea-requirements` |
| `ea-consistency-checker` | Cross-artifact contradictions, naming consistency, traceability, phase alignment, ID reference validation | `/ea-consistency`, `/ea-engage-review` |
| `ea-document-analyst` | EA mapping layer — extracts content from uploaded documents and maps to artifacts; delegates format conversion to `ea-document-converter` (no dedicated command) | Ask Claude: "Analyse the uploaded documents" |
| `ea-document-converter` | Format conversion — normalises uploaded files (.docx, .xlsx, .drawio, .pdf) to Markdown or Mermaid before EA mapping; invoked automatically by `ea-document-analyst` (no dedicated command) | Ask Claude: "Convert this uploaded document" |
| `ea-advisor` | Answers EA methodology questions — TOGAF, Zachman, ArchiMate (no dedicated command) | Ask any methodology question in chat |
| `ea-diagram` | Creates, edits, and interprets architecture diagrams (Mermaid, Graphviz, Draw.io, ArchiMate); standard diagram catalogue per artifact type; offers mmdc render after saving | `/ea-generate mermaid|png|svg`, ask Claude: "Create a diagram for..." |
| `ea-research` | EA-aware research support — quick lookup (1-2 searches), deep 4-phase investigation (planning → execution → analysis → synthesis), phase research planning, multi-source synthesis, research quality audit, impact tracing | Ask: "Quick research: ...", "Deep research: ...", "What should I research for Phase X?", "Synthesise the vendor reports", "Quality check our research" |
| `ea-security-advisor` | Answers security architecture Q&A in engagement context; supports SABSA/ISO 27001/NIST CSF decisions and ADR threshold scoring | Ask any security architecture question in chat |
| `ea-security-auditor` | Security control gap detection; maps artifacts to SABSA, ISO 27001 Annex A, NIST CSF 2.0; produces prioritised remediation report | `/ea-security-review` |

---

## 9. Quality Gates

| Gate | When | Mechanism |
|---|---|---|
| Artifact compliance | Every artifact open (interview, review, view) | 3-tier check: T1 frontmatter → T2 template structure → T3 artifact-specific (A3/A5 presence, Strategic Alignment, Scope column, Two-section structure) |
| Pre-publish compliance | Before `/ea-publish` assembles | All selected artifacts scanned; user chooses proceed or remediate; non-compliant items flagged in output |
| Content policy | Throughout interview | No AI content without `🤖` marker; no overwrite of Approved fields without confirmation |
| Opt-out audit | Ongoing | Every exclusion tracked with reason + timestamp in `engagement.json → optOuts[]`; surfaced in `/ea-status` and published reports |
| ADR threshold | During interview (post-answer) | After each answer, `ea-interviewer` scores 8 indicators; if 2+ match → suggest `/ea-adrs new` with pre-populated metadata; adds ADR-NNN to A3 Notes |
| A3.N rationale coverage (T3-RATIONALE) | On `/ea-artifact view`, `/ea-engage-review`, `/ea-grill` | Any A3 row with `Authority = Strategic` and no A3.N block (and no sentinel) surfaces as a T2 warning; remediated via `/ea-decisions rationale` |
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
