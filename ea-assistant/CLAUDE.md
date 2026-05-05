# EA Assistant — Developer Context

Plugin for managing Enterprise Architecture engagements end-to-end. TOGAF 10 process backbone, Zachman classification, ArchiMate 3.x notation.

**Current version:** 0.9.28 (plugin.json · docs/PRD.md)

---

## Critical Constraints

These rules prevent the most common errors. Check them before writing any agent or skill logic.

- **No inline concept definitions** — never define Capability, Work Package, Goal, etc. in prompts or inline text; always read `ea-concepts.md`
- **No invented ID prefixes** — use only the prefixes in the ID Scheme table; never create domain-prefixed IDs (BG-/DG-/AG-/TG- etc.)
- **Relative paths only** — all artifact paths are relative to `EA-projects/{slug}/`; never assume an absolute path
- **State changes require engagement.json** — every phase transition, artifact registration, and opt-out must update `engagement.json`
- **No duplicated logic** — cross-topic detection lives in `cross-topic-detection.md`; A3 governance rules live in `ea-artifact-templates/SKILL.md`; concept definitions live in `ea-concepts.md`; do not restate these inline

---

## Standard Engagement Flow

```
1. /ea-new          → creates EA-projects/{slug}/ layout; sets Phase: Preliminary
2. /ea-interview    → structured Q&A; populates interviews/; drafts artifact markdown
3. /ea-grill        → T3 compliance check + deep review; bumps artifact version on apply
4. /ea-adrs new     → captures significant architecture decisions; updates Appendix A3/A5
5. /ea-generate     → invokes Python scripts with extracted JSON → .docx / .pptx
```

For cross-engagement or end-of-phase validation: `/ea-engage-review` (consistency + motivation traceability + open items).

---

## Command Reference

30 commands available — run `/ea-help` for the full table with agent assignments.
Key entry points: `/ea-new` · `/ea-open` · `/ea-interview` · `/ea-grill` · `/ea-generate` · `/ea-status`

---

## Engagement Storage Layout

```
EA-projects/{slug}/
├── engagement.json           # all state: phases, artifacts, sessions, direction, metrics, optOuts
├── CLAUDE.md                 # stable pointer doc — identity, context, folder map (overwritten on /ea-open; no transitory state)
├── .claude/rules/
│   ├── ea-engagement.md      # persistent session guardrails (concept SST, ID scheme, rules) — auto-generated
│   └── ea-local-config.md    # user-editable local config (stakeholders, domain terms, preferences) — never overwritten
├── artifacts/                # phase-organized artifact files
│   ├── preliminary/          # Prelim: Architecture Principles, Engagement Charter
│   ├── requirements/         # Requirements: Register, Traceability Matrix
│   ├── phase-a/              # Phase A: Architecture Vision, SAoW, Stakeholder Map
│   ├── phase-b/              # Phase B: Business Architecture, Business Model Canvas
│   ├── phase-c-data/         # Phase C: Data Architecture
│   ├── phase-c-app/          # Phase C: Application Architecture
│   ├── phase-d/              # Phase D: Technology Architecture
│   ├── phase-e/              # Phase E: Gap Analysis, Architecture Roadmap
│   ├── phase-f/              # Phase F: Migration Plan
│   ├── phase-g/              # Phase G: Architecture Contract, Compliance Assessment
│   │   └── notes/            # interviews/, brainstorm/, reviews/ for this phase
│   ├── phase-h/              # Phase H: Change Request
│   │   └── notes/
│   └── cross-cutting/        # Risk Register, Decision Register, ADR Register, Zachman
│       └── notes/            # unscoped notes (no active phase)
├── diagrams/                 # .mmd, .dot, .drawio, .png, .svg
├── uploads/                  # source documents for ingestion
├── ResearchAndReferences/    # research documents, notes, links; research-index.md
└── ui/                       # generated HTML interview/brainstorm forms
```

> The `CLAUDE.md` inside each engagement folder is a **stable pointer document** (identity, context, folder map) — it contains no transitory state (no current phase, status counts, or commands). It is overwritten on every `/ea-open`. Do not edit it manually; use `brainstorm/brainstorm-notes.md` for persistent notes. For current phase and artifact state, run `/ea-open` or `/ea-status`.

### Artifact Link Conventions

All links in artifact markdown use paths relative to the artifact file at `artifacts/{phase}/`:

| Target | Relative path |
|---|---|
| Diagram | `../../diagrams/{name}.{ext}` |
| Same-phase artifact | `./{artifact-id}.md` |
| Different-phase artifact | `../{phase-folder}/{artifact-id}.md` |
| Upload | `../../uploads/{filename}` |
| Research document | `../../ResearchAndReferences/{filename}.md` |

### Artifact Metadata Fields

All artifact frontmatter includes three cross-reference fields (populated during authoring):
```yaml
relatedArtifacts: []   # artifact IDs referenced (e.g. ["architecture-vision"])
diagrams: []           # diagram paths from engagement root (e.g. ["diagrams/context.png"])
links: []              # named refs: [{label: "Context Diagram", path: "../../diagrams/context.png"}]
```

---

## ID Scheme

| Prefix | Concept | Example |
|---|---|---|
| DRV-NNN | Business Driver | DRV-001 |
| G-NNN | Goal | G-001 |
| OBJ-NNN | Objective | OBJ-001 |
| STR-NNN | Strategy | STR-001 |
| MET-NNN | Metric | MET-001 |
| ISS-NNN | Issue | ISS-001 |
| PRB-NNN | Problem | PRB-001 |
| WP-NNN | Work Package (roadmap) | WP-001 |
| GAP-NNN | Gap (Gap Analysis) | GAP-001 |
| REQ-NNN | Requirement | REQ-001 |
| RIS-NNN | Risk | RIS-001 |
| CON-NNN | Stakeholder Concern / Objection | CON-001 |
| ADR-NNN | Architecture Decision Record | ADR-001 |
| OPP-NNN | Opportunity | OPP-001 |
| CAP-NNN | Capability (Capability Model) | CAP-001 |
| VS-NNN | Value Stream | VS-001 |
| UC-NNN | Use Case | UC-001 |

**Do not use domain-prefixed IDs** (BG-/DG-/AG-/TG- etc.) — the scheme is unified and domain-agnostic.

---

## Agent Boundaries

`ea-facilitator` → phase navigation and next-action decisions only (not Q&A, not artifact writing).
`ea-interviewer` → all structured Q&A only (not phase navigation).
`ea-document-analyst` → EA mapping layer; delegates format conversion to `ea-document-converter`.
For full ownership table, see individual agent definition files in `agents/`.

---

## Architecture Decision Records

ADRs are standalone documents capturing significant architecture decisions — technology/vendor selection, pattern choices, make-vs-buy, data governance, security architecture, or any decision that is hard to reverse.

**ADR lifecycle:** `Candidate → In Progress → Completed → Superseded (by ADR-NNN) | Deprecated`

**ADR vs A3 Decision Log:**
- **A3** = governance state tracking inside an artifact (who decided what, at what authority, verified or not)
- **A3.N** = rationale detail block below the A3 table — one per decision, captures Rationale, Alternatives, Tradeoffs, Implications inline; created by `ea-interviewer` after `a: {text}` capture, or backfilled via `/ea-decisions rationale`
- **ADR** = standalone full-context document (situation, options analysis, rationale, consequences)
- Link them: A3 row `Notes` column should reference the ADR-NNN ID

**`/ea-adrs` modes:** `generate` (default, writes register), `status` (inline summary), `new` (create ADR from template), `update ADR-NNN <field> <value>` (single field update)

**ADR threshold:** `ea-interviewer` suggests an ADR when 2+ indicators apply (tech/vendor selection, high cost/risk, hard to reverse, make-vs-buy, contested by stakeholder, affects data governance/security/compliance/principles)

**`## Appendix A5 — Related Architecture Decisions` section** is required (T3-ADR) on: Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Architecture Roadmap, SAoW, Migration Plan, Compliance Assessment, Requirements Register, Engagement Charter, Governance Framework, Implementation Governance Plan

---

## Compliance Rules (Tier 3 — Artifact-specific)

| Rule | Artifact | Requirement |
|---|---|---|
| T3-A3 | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Consolidated Gap Analysis, Architecture Roadmap, Statement of Architecture Work, Migration Plan, Engagement Charter, Governance Framework, Implementation Governance Plan, Communications Plan, Architecture Definition Document, Transition Architectures | `## Appendix A3 — Decision Log` section present |
| T3-A5-ADR | Same artifact list as T3-A3 | `## Appendix A5 — Related Architecture Decisions` section present |
| T3-RATIONALE | Same artifact list as T3-A3 | Any A3 row with `Authority = Strategic` has no `#### A3.N — {Item}` block and no sentinel `*(rationale not captured)*` — surfaces in `/ea-artifact view`, `/ea-engage-review`, `/ea-grill` |
| T3-ROAD-SA | Architecture Roadmap | `## Strategic Alignment` section with at least one non-placeholder row |
| T3-ROAD-WP | Architecture Roadmap | At least one WP has non-empty `Advances Goals/Objectives` or `Executes Strategies` |
| T3-REQ | Requirements Register | Scope column present (Corporate / Project) |
| T3-TRACE | Traceability Matrix | Two-section structure (Corporate / Project) |

---

## Documentation Update Checklist

Before bumping `plugin.json` version, update all six files:

| File | What to update |
|---|---|
| `.claude-plugin/plugin.json` | Version; description if changed |
| `../.claude-plugin/marketplace.json` | Version + description — **must exactly match `plugin.json`** |
| `docs/PRD.md` | Version; new feature sections; revised counts |
| `commands/ea-help.md` | Commands table; tips |
| `README.md` | Feature bullets; commands table |
| `CLAUDE.md` (this file) | Version; Command Reference; ID scheme additions; new compliance rules |
