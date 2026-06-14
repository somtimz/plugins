# EA Assistant

A Claude Code plugin for managing Enterprise Architecture engagements from start to finish.

## Overview

EA Assistant supports the full EA engagement lifecycle using **TOGAF 10** as the process backbone, **Zachman** as the classification framework, and **ArchiMate 3.x** as the notation language. It manages multiple concurrent engagements, generates and reviews artifacts, facilitates stakeholder interviews, and produces consolidated architecture reports.

## Platform Support

EA Assistant works on both **Windows** and **Ubuntu Linux** (including WSL). All plugin components — commands, skills, agents, and Python scripts — use cross-platform paths and standard libraries.

## Features

- **Multi-engagement management** — create, open, track, edit, archive, and delete EA projects with engagement type classification (Greenfield/Brownfield/Assessment-only/Migration)
- **Full ADM lifecycle** — start, edit, or resume any TOGAF ADM phase (Prelim, A–H)
- **Motivation framework** — structured Business Drivers (DRV), Goals (G), Objectives (OBJ), Issues (ISS), and Problems (PRB) with ID-based traceability chains in the Architecture Vision (15 sections including Strategic Direction Summary with Strategies and Key Metrics); `/ea-status --direction --quality` scans all direction items for miscategorization, missing evidence, isolated items, and ambiguous phrasing; `/ea-grill --skill direction` runs an interactive direction quality review; inline quality challenge during engagement interviews flags and summarises issues before proceeding
- **Business Model Canvas** — Phase B BMC template (9 building blocks) with 27-question interview bank and linkage table to Business Architecture elements
- **Architecture Requirements** — manage requirements with Enterprise (read-only, waiveable) and Program (editable) scope distinction; NFR sub-type classification (19 categories including Availability, Reliability, Performance, Security, Compliance, Governance, Resilience, Ethical, Legal, and more) with measurable target fields; optional `### Sample Tests` and `### Stories` subsections per requirement capture verifiable tests and STY-NNN delivery items inline; Motivation field links each requirement to its driver, issue, problem, goal, or objective; `/ea-grill --skill requirements` produces NFR coverage scorecard and traceability gap list
- **Capability management** — `/ea-capabilities` creates, edits, maps, and scores business capabilities (CAP-NNN) in the Business Architecture capability model (L1→L2→L3 hierarchy, Business vs Technology type, current/target maturity, **value/outcome**, strategic anchor); `map` renders the box-in-box capability map, `score` rates Completeness + Quality (value stated, strategically anchored, not a process, not inflated), `adopt` seeds from the Architecture Repository's **canonical capability map** (CAP-C-NNN). The Capability Model concept, Phase B interview, brainstorm, and scoring all test for the value a capability brings
- **ABB / SBB / User Story traceability** — end-to-end implementation chain from Capability (CAP-NNN) → Requirement (REQ-NNN) → Architecture Building Block (ABB-NNN) → Solution Building Block (SBB-NNN) → User Story (STY-NNN) → Task; ABBs are vendor-neutral logical components captured per application/technology component; SBBs are concrete product/vendor choices in the Technology Architecture Solution Building Blocks Register; concept disambiguation in `ea-concepts.md` and Layer 6 cross-topic probes in `/ea-grill` prevent capability/requirement/ABB/SBB/story misclassification
- **Artifact generation** — all TOGAF artifacts from templates, guided by interviews
- **Format export** — generate Word (.docx), PowerPoint (.pptx), Mermaid source, PNG, and SVG from any artifact; diagrams automatically embedded in docx/pptx deliverables
- **Phase interviews** — curated question bank for each ADM phase (Text, Web, or Display mode) with output routing to artifacts; ID scheme reference and section markers for Phase A
- **Interview shortcuts** — single-key shortcuts for defaults, skip, N/A, opt-out, brainstorm, research, A3 logging, and governance transitions; type `?` at any prompt for contextual help
- **Contextual help** — type `?` during any interview to see the artifact's purpose, value, current progress, and a link to the EA concepts reference
- **EA concepts reference** — canonical definitions of all 32 EA concepts (Vision, Mission, Business Driver, Principle, Direction, Goal, Objective, Strategy, Plan, Risk, Issue, Problem, Opportunity, Capability Model, Capability Gap, Work Package, Operating Model, Value Stream, Business Process, Use Case, Business Scenario, Requirement, Opportunity, Constraint, Metrics, Cost Entry, ADR, ABB, SBB, Reference Architecture, User Story, Stakeholder Concern) with full motivation chain model, TOGAF/ArchiMate alignment, and disambiguation checklist; grounded in *EA Strategic Context: Terms, Concepts, and Relationship Models*
- **Cross-topic detection** — flags answers that belong in a different artifact and offers to route them correctly or save for later
- **Session tracking** — records facilitator, participants, topics, and next recommended step for every interview session; prior session summary shown at session start
- **Brainstorming** — capture freeform thoughts before or during interviews; surfaced automatically as context during Q&A
- **Requirements analysis** — extract structured requirements from uploaded documents, map to ADM phases and Zachman cells
- **Stakeholder interviews** — chat-based or interactive web form; dated and versioned notes
- **Diagram support** — Mermaid, Graphviz (.dot), Draw.io (.drawio), ArchiMate notation
- **EA tool import** — ingest Sparx XMI, Archi tool `.archimate`, and LeanIX CSV/JSON exports; map elements to engagement artifacts
- **Decision Register** — cross-artifact decision tracking with governance states (Provisional → Verified/Voted/Fiat), owner attribution, and on-demand registers tailored by audience, domain, authority, cost, impact, or risk
- **Artifact grill** — deep-review any artifact using grill-me skills (stress-test, premortem, decision, design, software-design, infra-design, artifact, diagram, boardroom-strategy); auto-selects best skill by artifact type; apply findings back to the artifact one revision at a time with per-revision confirm/skip/edit
- **Artifact scoring** — `/ea-score` assigns two scores, **Completeness** and **Quality** (0–100 + band), **per section and overall**, using `grill-scoring-rubric.md` (grounded in the EA concept definitions, each section's guidance block, and the compliance tiers; Quality includes a readability dimension). Scores render into an author-only `<details>📊 Scorecard</details>` block in each artifact (per-section table + overall, stripped on export); `--all` scores the whole engagement and the overall pair is cached in `engagement.json` for tracking. `/ea-grill` emits the same two scores during a deep review. Command-generated artifacts (registers/matrices) are not scored
- **Opt-out tracking** — explicitly opt out of any question or artifact; reasons and timestamps recorded; surfaced in status reports and consolidated documents
- **Artifact compliance** — automatic compliance check when opening any artifact; offer to remediate missing fields/sections or accept as-is with sensible defaults
- **Pre-publish compliance** — `/ea-publish` runs compliance scan on all selected artifacts before assembly; non-compliant items flagged with option to proceed or remediate
- **Review & consistency** — per-artifact review workflow with quality check action (table sizes, placeholder text, broken images, narrative gaps — each finding addable as a review comment); cross-artifact consistency checking; `/ea-consistency --quality` scans all artifacts for readability and content completeness issues; ID reference registry (broken refs, orphaned IDs); within-artifact section contradiction detection; post-save compliance + consistency prompt after every artifact write
- **Security architecture** — `/ea-security-review` audits artifacts against SABSA layer coverage, ISO 27001:2022 control domains, and NIST CSF 2.0 functions; `/ea-grill security` provides interactive single-artifact security review with applied fixes; `ea-security-advisor` agent answers SABSA/ISO/NIST Q&A and security architecture decision trade-offs
- **Layered publishing** — `/ea-publish` produces a stakeholder-consumable layered report by default (executive brief → per-artifact summaries → appendix of links to full artifacts) and writes an `artifacts/index.md` reading guide; `--full` builds the classic full-text consolidated document; readability pass flags oversized tables, broken image paths, placeholder text, `TBD`/`TODO` markers, and sections lacking narrative; guidance comments are stripped from all published output; AI-assisted rewrite pass adds transitions and narrative intros (with `<!-- ai-inserted -->` markers); opted-out and non-standard items flagged inline
- **Research agent integration** — invoke `@research-agent` at any point during interviews for evidence-based validation of drivers, risks, technology choices, or assumptions; invoke `ea-research` agent for proactive phase research planning, multi-source synthesis, and research quality audits
- **Document ingestion** — upload existing docs and diagrams to inform artifacts; format extraction (docx, pdf, xlsx, csv, drawio, mmd) handled by `ea-document-ingestion` skill; EA content mapping handled by `ea-document-analyst` agent
- **External tool integration** — delegate to Claude Code MCP tools and agents (web search, browser automation, database queries, project management) from any interview, review, or research session
- **Architecture Roadmap agent** — three-mode roadmap creation: Review (existing artifact), Artifact-informed (reads Vision Goals/Strategies/Objectives + Gap Analysis + Requirements to seed work packages with strategic alignment), Clean-slate (direct elicitation with no prior artifacts); Strategic Alignment table in roadmap template links every G-NNN/OBJ-NNN/STR-NNN to covering work packages
- **Phase E strategic alignment** — roadmap work packages explicitly link to Goals and Strategies from Phase A; interview questions anchor prioritisation to G-NNN/STR-NNN before addressing gaps and constraints
- **ADM reference material** — detailed phase inputs/outputs, tailoring guidance for agile/programme/capability-based contexts
- **Constraints Register** — `/ea-constraints` manages architecture constraints (CST-NNN) as first-class objects with Type, Source, Owner, and Impact Assessment; distinguishes constraints from requirements and risks; traces constraints to SBBs, artifacts, and work packages
- **Policies Register** — `/ea-policies` manages architecture policies (POL-NNN) as first-class governance documents with Issuing Authority, Effective Date, Review Cycle, and Linked Constraints; distinguishes policies from principles and constraints; traces policies through linked CST-NNN constraints to capabilities, ABBs, and work packages
- **Business Drivers Register** — `/ea-drivers` manages business drivers (DRV-NNN) as first-class objects with type (External/Internal), priority, evidence, and linked goals; `trace` walks the full DRV→G→OBJ→STR→WP motivation chain; `generate` produces the Drivers Register
- **Architecture Gap Register** — `/ea-gaps` manages architecture gaps (GAP-NNN) as first-class objects with domain, severity, baseline/target state, phase, and status; `promote` formalises raw gap prose from `/ea-trace --gaps` into GAP-NNN entries; `trace` links upstream artifacts to downstream work packages; migration gaps use GAP-M-NNN
- **Seasoned Architect Lens** — `/ea-lens` reviews the whole engagement through eight practitioner lenses (Real Problem, Decision Quality, Real Risk, Stakeholder Reality, Motivation Chain Integrity, Architecture vs Implementation Blur, What to Do Next, The One Thing); `--quick` produces lenses 1, 7, 8 only from engagement.json without a full artifact scan
- **Phase-adaptive interviews and brainstorms** — `/ea-interview` and `/ea-brainstorm` now inject a phase intent preamble from `adm-phase-guide.md`, filter engagement direction items by phase relevance, and skip questions already answered in existing artifacts
- **Risk Register** — `/ea-risks` generates a cross-cutting Risk Register (RIS-NNN) by scanning all artifacts for risk content; Likelihood × Impact severity matrix
- **Financial modeling** — `/ea-finance` manages a Cost Model Register of FIN-NNN Cost Entries, each capturing the full architecture-grade cost picture of one work package, option, or capability (capex, opex, derived 3-year TCO, payback, confidence); `generate` writes the register and rolls up the Architecture Roadmap budget. A Business Case artifact (`/ea-artifact create business-case`) compares costed options and recommends one (T4-ECON/T4-TCO); `benefit`-type metrics track value realisation in Phase G
- **Architecture Decision Records** — `/ea-adrs` manages standalone ADRs (Candidate → Completed lifecycle); `ea-interviewer` auto-suggests ADRs at 2+ threshold indicators; Appendix A5 links artifacts to related ADRs
- **Zachman Diagram** — `/ea-zachman` auto-populates and manages the 6×6 classification grid; generate, review, gap, interview, audit, and classify modes — audit checks completeness honesty, row/column consistency, staleness, scope, and perspective purity
- **Governance artifacts** — Engagement Charter (Prelim), Governance Framework (Prelim), Implementation Governance Plan (G), Change Register (H)
- **Architecture Change Management** — `/ea-changes` generates Change Register from Phase H ACR artifacts; `/ea-concerns` manages CON-NNN stakeholder concerns (Appendix A4)
- **Engagement review** — `/ea-engage-review` produces a full health report covering coverage, traceability, governance, ADR status, and Zachman completeness
- **Item detail files** — optional per-item companion files (`artifacts/details/{ID}.md`) capture extended narrative, rationale, risks, costs, issues, concerns, impact, and alternatives for any ID-bearing table row; linked from source tables via `Details` column; loaded automatically as context by interview, grill, review, and brainstorm sessions
- **Obsidian wikilink support** — internal links (detail files, cross-artifact, diagrams, uploads, research) use `[[..]]` wikilink syntax by default for new engagements, making artifacts fully navigable in an Obsidian vault; per-engagement `linkStyle: wikilink|markdown` setting in `.claude/rules/ea-local-config.md`; commands parse both forms; `/ea-generate` and `/ea-publish` resolve wikilinks on export
- **Session capture to detail files** — interview, review, brainstorm, and grill sessions offer to record surfaced issues and concerns directly into the relevant item's detail file; grill cross-references new CON-NNN entries to item detail files after A4 population
- **Detail file sync** — `/ea-detail sync <ID>` bidirectionally syncs a detail file's Concerns/Issues with the parent artifact's A4 table; `/ea-consistency --details` validates link integrity (Check D) and A4 content sync (Check E) across all detail files
- **Detail file cross-linking** — `/ea-detail link {ID1} {ID2} [rel]` creates bidirectional links with automatic inverse labels; `relatedItems[]` frontmatter is the source of truth; `/ea-detail check` validates link integrity, back-link symmetry, table/frontmatter sync, and open notes
- **Inline detail notes** — `/ea-note --detail {ID}` appends open `📌` annotations to a detail file's `## Notes` section; `/ea-detail note resolve {ID}` resolves them in-place; visible in `check`, `list`, and `index` output
- **Detail file index** — `/ea-detail index` generates `artifacts/details/_index.md` grouped by type with cross-link and open-note columns
- **Generate and publish with detail files** — `/ea-generate --with-details` embeds detail file content in exported .docx/.pptx; `/ea-publish` offers inline, appendix-only, or exclude options for detail files in consolidated documents
- **Migration** — `/ea-migrate` aligns legacy engagements to the current plugin version; scan 3g flags high-priority items (Critical/High risks, High-priority requirements, Strategic decisions) lacking detail files (report-only — detail files are created on demand, never as bulk empty stubs); scan 3i backfills template body sections and `<details>📋 Guidance</details>` blocks the artifact predates (insertion-only, per-section confirmation, skips command-generated artifacts); scan 3j reorders existing sections to template order (whole-section atomic moves); scan 3k heuristically surfaces misplaced content and proposes user-confirmed moves within or across documents — 3j/3k snapshot the artifact before any change, run a content-preservation check, and are excluded from `--auto`; preview with `--report`
- **Register snapshots** — generated registers use stable filenames (e.g. `risk-register.md`); regenerating archives the previous version to a `snapshots/` subfolder, keeping one current register per folder
- **Register protocol** — the direction-register commands (`/ea-drivers`, `/ea-goals`, `/ea-objectives`, `/ea-strategies`, `/ea-issues`, `/ea-problems`, `/ea-gaps`) share one mode-mechanics reference (`register-protocol.md`); each command is a declarative spec plus its unique checks; `add`/`update` mirror changes into the artifact display view (e.g. Architecture Vision §2–§6) so stakeholder-facing tables never drift from `engagement.json`
- **Continuous requirements** — `/ea-phase` surfaces open requirements relevant to each phase on entry and bridges Requirements-phase completion directly into Phase A
- **Framework lenses** — pluggable overlay for external prescriptive frameworks (`ea-framework-lenses` skill) with all three cloud lenses available: AWS Well-Architected (`/ea-grill --skill waf`), Azure Cloud Adoption Framework (`--skill caf`, adoption-lifecycle shape covering Phase A/B/E/F strategy, five-Rs dispositions, landing zones, governance disciplines), and Google Cloud Architecture Framework (`--skill gcaf`, SLO-driven pillar review); phase interviews offer the lenses whose questions cover the current phase on cloud-scope engagements
- **ADM tailoring** — `/ea-new` proposes a phase set from the Architecture Level (Solution-level engagements can inherit Preliminary and Phase H from the enterprise); opted-out phases are excluded from picklists and progress but re-includable via `/ea-phase`
- **Phase H change management** — ACR triage guide with TOGAF Simplification/Incremental/Re-architecting classification, escalation timeboxes, and ADM re-entry mapping; security questions now cover all 10 phases including F (migration security) and H (change security)
- **Complete concept catalogue** — `ea-concepts.md` covers Service (SVC-NNN), Interface (IFC-NNN), Components, Capability Increment, Plateau, Deliverable, Architecture Partitioning, and Enterprise Continuum alongside the motivation and building-block concepts
- **TOGAF techniques** — Business Transformation Readiness Assessment template (12 factors, roadmap implications), Capability-Based Planning reference (wired into roadmap derivation), Interoperability Requirements checklist (categories, degrees 1–4, REQ/IFC capture), and risk appetite/tolerance enforcement in `/ea-risks accept`
- **Schema versioning** — `engagement.json` carries `schemaVersion` and a `migrations[]` audit trail appended by every `/ea-migrate` run; engagement.json is the declared single source of truth, generated registers are rendered views
- **Session rules** — each engagement folder is seeded with `.claude/rules/ea-engagement.md`: persistent guardrails loaded by Claude Code on every session (require `/ea-open`, protect Approved artifacts, enforce unified ID scheme, cite reference SSTs for concepts and phase guidance)
- **Slim engagement CLAUDE.md** — the per-engagement `CLAUDE.md` is a lightweight pointer document (identity + state counts + content locations); full strategic detail stays in `engagement.json → direction` and artifact files
- **TOGAF governance model** — two-layer governance reference (architecture governance vs programme governance) with phase-by-phase table; `ea-concepts.md` includes full motivation-concepts ADM lifecycle (where each concept is first captured, refined, realized, and adapted across Preliminary through Phase H)
- **Research & References** — `/ea-research` manages a per-engagement library (documents, notes, links); `apply` mode synthesises research against any artifact — gaps and contradictions surfaced with `y/n/edit` revision workflow; synthesis reports saved to `ResearchAndReferences/`
- **Diagram rendering** — render Mermaid (`.mmd`) files to PNG or SVG via mermaid-cli (`mmdc`); standard diagram catalogue per artifact type; batch render with `--all`
- **Advanced practitioner content** — 50 high-impact TOGAF tips, 70 phase-by-phase deep tactics, 25 cross-cutting expert moves, 5-level maturity model (L1–L5), 7 advanced operating patterns, 6 failure modes at scale, elite architect day-to-day playbook, and synthesized white paper
- **Practitioner grill modes** — `/ea-grill --skill practitioner` (economic framing + decision quality), `--skill maturity` (L1–L5 assessment), `--skill failure-mode` (symptom scan + pre-mortem)
- **Advanced brainstorm pauses** — during `/ea-brainstorm`, type `p:`, `f:`, `o:`, `m:`, or `e:` to trigger pattern discovery, failure-mode scan, optionality exploration, maturity assessment, or economic framing
- **Economic framing pause** — during `/ea-interview`, type `e: {statement}` to add cost/risk/value analysis to any answer; links to Tier 4 compliance (economic traceability)
- **Decide vs Defer Framework** — 5-factor decision quality assessment (Evidence, Reversibility, Impact, Urgency, Capability) triggered by `d: {statement}` during interviews; prevents premature commitments, converts weak-evidence decisions to PAD-NNN, and adds guardrails to reversible decisions
- **Pending Architecture Decision (PAD-NNN)** — lightweight deferred-decision artifact with constraint boundaries, candidate options, evidence requirements, resolution path, expiry date, and consequences of premature commitment; linked to GAP-NNN, WP-NNN, and ADR-NNN
- **Evidence-gated prioritisation** — work packages with insufficient evidence flagged as high-risk or deferred from Wave 1; prevents speculative scheduling
- **Political alignment documentation** — records stakeholder pressure and defensible evidence-based positions for high-impact decisions; surfaces in ADR and A3 assessments
- **Tier 4 compliance** — advanced compliance rules for L3+ engagements: economic traceability, decision latency documentation, optionality preservation, fitness function coverage, premature decision detection, evidence quality assessment, political alignment, PAD hygiene, and work package evidence gating; maturity-based enforcement expectations
- **Ad-hoc note capture** — `/ea-note [text] [--artifact <id>] | resolve <path>` quick-captures notes with Open/Resolved lifecycle from anywhere in the engagement; standalone notes routed to phase folder with classification suggestions; artifact annotations inserted inline or as linked files; `n:` interrupt prefix works during `/ea-interview` and `/ea-grill` without breaking session flow; `/ea-notes list` shows Ad-hoc Notes section with Status column
- **Git and GitHub integration** — `/ea-git` manages `EA-projects/` as a git repository; `init` creates the repo, `.gitignore`, and optional private GitHub remote via `gh` CLI; `commit` auto-generates contextual messages from changed artifact names; `push`/`sync`/`log`/`remote` for full GitHub workflow; `/ea-open` shows version control status inline
- **Motivation concept registers** — dedicated register commands for Goals (`/ea-goals`), Objectives (`/ea-objectives`), Strategies (`/ea-strategies`), Issues (`/ea-issues`), and Problems (`/ea-problems`); each with list/add/update/trace/generate modes; Domain/Type/Horizon classification; Strategy `trace` renders the Goals→Strategies→Work Packages map; Issue vs Problem and Goal vs Strategy disambiguation on `add`; trace walks the full upstream/downstream motivation chain
- **Persona-tailored menus and reports** — `/ea-help --persona <role>` renders a role-scoped command menu and suggested workflow; `/ea-publish --persona <role>` assembles a role-scoped report pack (filtered by the `audience` taxonomy). Built-in personas: Enterprise Architect, CIO, CISO, Chief Product Officer, Chief Privacy Officer, Business Architect, Data Architect. Definitions live in `persona-registry.md` (interests, command subset, report bundle, entry workflow); adding a persona is a data edit. `defaultPersona:` in `ea-local-config.md` sets the engagement default
- **Business Scenarios** — `/ea-scenarios` manages TOGAF Phase A Business Scenarios (BS-NNN) with guided `new` mode through all six TOGAF elements (Problem Statement, Objectives, Environment, Stakeholders, Actors, Requirements) plus Current/Target State narratives and Change Delta; `interview` mode completes existing scenarios; `trace` walks the full motivation chain from drivers/issues/problems through the scenario to goals, objectives, and generated requirements; generates a Scenarios Summary Register
- **Architecture Repository** — `/ea-repo` initializes a shared `EA-Workspace/` structure with `Architecture-Repository/` (VDR/THR/STD registers) and `EA-Projects/` as siblings; `link` connects an engagement to the repo; `/ea-open` (no args) discovers active projects via `workspace.json` walk-up
- **Vendor Landscape Register** — `/ea-vendors` manages org-wide vendor assessments (VDR-NNN) with roadmap status (Active/Sunset/EoL), lock-in risk, and SBB cross-links; `/ea-sbbs new` auto-checks the vendor index and warns on Sunset/EoL vendors
- **Technology Horizon Register** — `/ea-horizon` manages a technology radar (THR-NNN) with Adopt/Trial/Assess/Hold ring model, ring history, and PoC evidence; `/ea-adrs new` cross-references THR entries for technology/vendor selection decisions
- **Standards Information Base** — `/ea-standards` manages industry/regulatory standards (STD-NNN) with adoption status (Mandatory/Recommended/Informational/Deprecated) and CST-NNN constraint linkage; `surface` command shows standards relevant to the active ADM phase
- **Reference Architecture Register** — define reusable RA-NNN patterns with ABB/SBB layer catalogues, key decisions, and grill checklist integration; adopt patterns into engagements
- **TOGAF relationship matrices** — 20-matrix catalogue (Actor/Role, Application/Data CRUD, Capability/Application, Goal/Service, Data Entity/Data Component, System/Technology, Work Package/Dependency…) with /ea-matrix management, axis seeding from existing artifacts, and grill compliance checks; domain architecture templates carry a Related Matrices pointer
- **Cross-cutting sub-folders** — `artifacts/cross-cutting/` reorganized into `governance/` (ADR Register, Decision Register, Constraints, Policies), `operations/` (Risk Register, Change Register, Concerns), and `context/` (Zachman, Roles); auto-maintained `cross-cutting-index.md` navigation hub; `/ea-migrate --reorganize` migrates legacy flat paths

## Prerequisites

- Claude Code with plugin support
- `pandoc` (for Word document export)
  - **Linux/macOS:** `brew install pandoc` or `apt install pandoc`
  - **Windows:** `winget install pandoc` or download from [pandoc.org](https://pandoc.org/installing.html)
- Python 3.11+ with `python-docx` and `python-pptx` packages (for `/ea-generate` Word/PPTX export)
  - **Linux/macOS:** `pip3 install python-docx python-pptx`
  - **Windows:** `pip install python-docx python-pptx`
- `mermaid-cli` (for `/ea-generate png|svg` diagram rendering — optional)
  - `npm install -g @mermaid-js/mermaid-cli`
  - Falls back to `npx -y @mermaid-js/mermaid-cli` automatically if not globally installed

## Installation

```bash
/plugin install ea-assistant
```

## Configuration

Create `.claude/ea-assistant.local.md` in your working directory to configure EA Assistant behaviour:

```yaml
# Path to shared requirements folder
requirementsRepoPath: /path/to/shared/requirements-folder

# Facilitator tone: patient | direct | executive  (default: patient)
facilitatorStyle: patient

# Audience: executive | architect | technical | mixed  (default: mixed)
audienceLevel: mixed

# Confirm before writing each answer to an artifact  (default: false)
requireConfirmBeforeRecord: false

# Show @research-agent reminders on drivers, risks, assumptions  (default: true)
researchPrompts: true

# Show topic/theme summary at end of each interview session  (default: true)
sessionSummary: true

# UI delivery mode: artifact | html  (default: html)
# Use 'artifact' in Claude Code Desktop, Cowork Desktop, or claude.ai/code
# Use 'html' (or omit) in Claude Code CLI terminal
uiMode: html
```

**Style guide:**
- `patient` — explains each question, offers examples, probes short answers, pauses at section transitions
- `direct` — ask, record, move on; minimal preamble
- `executive` — business-outcome framing, no TOGAF jargon, checkpoints every 5–7 questions

> **CLI users:** Leave `uiMode` unset or set to `html` — the interview and brainstorm UIs will open as a standalone HTML file in your browser. **Desktop/Cowork/Web users:** Set `uiMode: artifact` to render UIs inline as React artifacts.

> `requirementsRepoPath` currently points to a local folder. SharePoint integration is planned for a future version.

## Commands

| Command | Description |
|---|---|
| `/ea-new` | Create a new EA engagement with guided setup, engagement type selection, domain scoping, and Preliminary phase scaffolding |
| `/ea-open` | Open an engagement with full details, edit metadata/phases/artifacts, archive or delete |
| `/ea-status` | Portfolio dashboard with type, domains, phase progress, artifact counts, opt-outs, and non-standard artifact flags; `--next` for next action; `--direction` for Direction Register |
| `/ea-phase [phase]` | Start, edit, or resume an ADM phase |
| `/ea-artifact [action]` | Create, view, or list artifacts; runs compliance check on view; `summary [refresh\|status]` for executive summary management |
| `/ea-brainstorm [phase]` | Capture freeform thoughts and context before or during interviews |
| `/ea-interview [mode]` | Start or resume a stakeholder interview (artifact or phase mode; Text/Web/Display) |
| `/ea-generate [artifact] [format]` | Export as docx, pptx, mermaid, png, or svg; diagrams embedded in docx/pptx by default; `--matrices` embeds linked relationship matrices |
| `/ea-notes [mode]` | List, view, edit, or delete interview notes, brainstorm notes, and review files |
| `/ea-note [text] [--artifact <id>] \| resolve <path>` | Quick-capture an ad-hoc note with Open/Resolved lifecycle; `resolve` records resolution with rationale and impact; `n:` prefix works mid-interview or mid-grill |
| `/ea-detail new\|view\|list\|sync\|link\|check\|note resolve\|index` | Create, view, list, sync, cross-link, and integrity-check item detail files; generate type-grouped index; add and resolve inline notes |
| `/ea-review [artifact]` | Open an artifact for review and assessment; runs compliance check on load |
| `/ea-requirements [action]` | Manage architecture requirements |
| `/ea-constraints [action]` | Manage architecture constraints — capture, view, trace to artifacts, and assess impact on solution space |
| `/ea-policies [mode]` | Manage architecture policies — capture governance documents, trace to constraints, and assess policy impact |
| `/ea-drivers [mode]` | Business Driver Register — list, add, update, trace DRV→G→OBJ→STR→WP chain, or generate register |
| `/ea-scenarios [mode]` | Business Scenario Register — list, create, interview, trace, and generate Phase A scenario artifacts (BS-NNN) |
| `/ea-repo [init\|link\|status\|open]` | Architecture Repository — initialize EA-Workspace, link engagements to the shared Architecture Repository |
| `/ea-vendors [list\|add\|update\|link-sbb\|archive]` | Vendor Landscape Register — org-wide VDR-NNN entries with roadmap status and lock-in tracking |
| `/ea-horizon [list\|add\|update\|surface\|link-adr]` | Technology Horizon Register — THR-NNN radar entries with Adopt/Trial/Assess/Hold rings |
| `/ea-standards [list\|add\|link-constraint\|surface]` | Standards Information Base — STD-NNN entries with adoption status and constraint linkage |
| `/ea-refarch [new\|list\|show\|edit\|adopt\|unadopt\|status]` | Reference Architecture Register — manage RA-NNN patterns with ABB/SBB layer catalogues, key decisions, and grill checklist integration |
| `/ea-matrix [list\|new\|show\|edit\|check] [key]` | TOGAF relationship matrices — 16 grid artifacts (Actor/Role, App/Data CRUD, Capability/Application, Goal/Service, Data Entity/Component, System/Technology…) with axis seeding and catalogue-driven checks |
| `/ea-gaps [mode]` | Architecture Gap Register — list, add, promote raw gaps to GAP-NNN, update, trace to work packages, or generate register |
| `/ea-principles [mode]` | Manage architecture principles (BP/DP/AP/TP-NNN) — list, add, update, or trace; violation detection flags ADRs that contradict active principles |
| `/ea-abbs [mode]` | Architecture Building Block Register — generate, view, create, or update ABB-NNN entries; modes: generate, status, new, update |
| `/ea-actions [generate\|view\|update\|status]` | Stakeholder Action Plan — consolidated per-approver action view seeded from SAoW and Target State Declaration |
| `/ea-sbbs [mode]` | Solution Building Block Register — generate, view, create, or update SBB-NNN entries; modes: generate, status, new, update |
| `/ea-stories [mode]` | User Story Register — generate, view, create, or update STY-NNN entries; modes: generate, status, new, update |
| `/ea-target [new\|view\|update]` | Target State Declaration — per-domain target states, success criteria, and traceability to goals and objectives |
| `/ea-trace [--gaps]` | Interactive traceability views — motivation chain from drivers to work packages; `--gaps` for consolidated gap report only |
| `/ea-decisions [options]` | Generate a Decision Register from all A3 decision logs; filter by audience, owner, domain, authority, cost, impact, risk, subject, or status |
| `/ea-adrs [mode]` | Manage Architecture Decision Records — generate register, create new ADR, update status |
| `/ea-risks [mode]` | Generate and maintain a cross-cutting Risk Register from all artifact risk sections |
| `/ea-finance [list\|add\|update\|trace\|generate]` | Cost Model Register — manage FIN-NNN Cost Entries (capex/opex/TCO/payback with confidence), trace to work packages/ADRs/goals, generate register and roll up the roadmap budget |
| `/ea-changes [mode]` | Generate Change Register aggregating Phase H ACR artifacts |
| `/ea-concerns` | Manage CON-NNN stakeholder concerns and objections (Appendix A4) |
| `/ea-roles [ROLE-ID\|--domain\|--generate\|--update]` | Role Catalogue — list, filter, and generate role assignments with RACI, triggers, and calendar |
| `/ea-zachman [mode]` | Manage the Zachman 6×6 classification diagram — generate, review, gap, interview, audit, classify |
| `/ea-research [mode]` | Research library — add documents, notes, links; apply findings to artifacts |
| `/ea-consistency [options]` | Focused consistency check — cross-artifact contradictions, ID reference validation (`--ids`), or single-artifact within-section check (`artifact <id>`) |
| `/ea-lens [--quick]` | Seasoned architect engagement review across eight practitioner lenses |
| `/ea-engage-review` | Full engagement health check — coverage, traceability, governance, ADR status, Zachman |
| `/ea-security-review [<artifact-id>] [--framework sabsa\|iso\|nist]` | Security audit — SABSA layer coverage, ISO 27001:2022 domain alignment, NIST CSF 2.0 function analysis; full engagement by default |
| `/ea-migrate [--report\|--reorganize]` | Align a legacy engagement to the current plugin version conventions; backfills template body sections/guidance (3i), reorders sections to template order (3j), and proposes user-confirmed moves of misplaced content within/across documents (3k) — body changes are snapshotted, confirmed per item, excluded from `--auto`; `--reorganize` moves flat-path artifacts into correct phase subfolders |
| `/ea-grill [artifact] [--skill]` | Deep-review an artifact using a grill-me skill; apply findings one revision at a time; `all` mode batch-reviews all artifacts |
| `/ea-score [artifact\|--all\|--status]` | Score artifacts on Completeness + Quality (0–100 + band), per section and overall; writes an author-only 📊 Scorecard block into each artifact (stripped on export); `--all` scores the engagement, `--status` shows the last scores |
| `/ea-brief [--focus decisions\|risks\|gaps\|strategy] [--save]` | Synthesised one-page engagement brief — ranked decisions, gaps, risks, open concerns |
| `/ea-workshop [start\|resume\|export\|list]` | Facilitated multi-stakeholder workshops — WS-NNN minutes, agenda, decisions, actions |
| `/ea-arb [new\|list\|view\|close]` | ARB meeting minutes — ARB-NNN, quorum, decisions, propagate to ADR register |
| `/ea-goals [mode]` | Goals Register — list, add, update, trace G→OBJ→STR→WP, or generate register; Domain + Type classification |
| `/ea-objectives [mode]` | Objectives Register — list, add, update, trace OBJ→G/PRB/MET/WP, or generate register; measurability checks (measure, target, deadline) |
| `/ea-strategies [mode]` | Strategy Register — list, add, update, trace the Goals→Strategies→Work Packages map, or generate register; Type + Horizon classification; `trace` renders the Strategy Map |
| `/ea-capabilities [list\|add\|update\|map\|score\|adopt]` | Manage business capabilities (CAP-NNN) in the Business Architecture capability model — hierarchy, capability map, Completeness+Quality scoring, and adopt from the canonical capability map |
| `/ea-issues [mode]` | Issues Register — list, add, update, trace ISS→G→GAP, or generate register; Domain (incl. Engagement) + Type classification |
| `/ea-problems [mode]` | Problems Register — list, add, update, trace PRB→OBJ→REQ, or generate register; Domain (incl. Engagement) + Type classification |
| `/ea-git [init\|status\|commit\|push\|sync\|log\|remote]` | Manage EA-projects/ as a git repository — init, commit, push to GitHub |
| `/ea-publish [--full\|--executive]` | Layered stakeholder report (default), full consolidated document (`--full`), or executive pack; `--matrices` inlines linked relationship matrices; writes `artifacts/index.md` reading guide; compliance pre-check |
| `/ea-config [section]` | Configure plugin settings, engagement rules, opt-outs, and refresh CLAUDE.md |
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
| `resume` / `done` | End brainstorm and return to the interview |
| `r: {query}` / `research: {query}` | Research a topic mid-interview; findings surfaced inline with option to save to ResearchAndReferences |
| `e: {statement}` | Economic framing pause — add cost/risk/value analysis to any answer |
| `d: {statement}` | Decide/Defer pause — 5-factor assessment; recommends: Decide now / Defer / Guardrails / Premature / Risky commit; offers to create PAD-NNN |
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
│   ├── .claude/
│   │   └── rules/
│   │       └── ea-engagement.md  # persistent session rules (auto-loaded by Claude Code)
│   ├── engagement.json           # metadata, ADM phases, settings, opt-outs
│   ├── CLAUDE.md                 # pointer doc — identity + state counts + locations
│   ├── requirements/             # local architecture requirements
│   ├── artifacts/                # generated artifacts + review files
│   ├── diagrams/                 # Mermaid, Graphviz, Draw.io, PNG, SVG files
│   ├── uploads/                  # source documents and diagrams
│   ├── reviews/                  # grill-me review outputs
│   ├── ResearchAndReferences/    # research docs, notes, links; research-index.md
│   └── interviews/
│       ├── session-log.md        # chronological session history (who, what, next step)
│       └── interview-*.md        # dated, versioned interview notes
└── .archive/                     # archived engagements (hidden)
    └── old-engagement/
        └── engagement.json
```

## Frameworks Supported

- **TOGAF 10** — ADM process backbone
- **Zachman Framework** — full 6×6 classification
- **ArchiMate 3.x** — architecture notation and modelling

## License

[MIT](./LICENSE)
