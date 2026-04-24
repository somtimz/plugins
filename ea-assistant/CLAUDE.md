# EA Assistant — Developer Context

Plugin for managing Enterprise Architecture engagements end-to-end. TOGAF 10 process backbone, Zachman classification, ArchiMate 3.x notation.

**Current version:** 0.9.27 (plugin.json · docs/PRD.md)

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

| Command | Primary Agent | Purpose |
|---|---|---|
| `/ea-new` | ea-facilitator | Create a new engagement project |
| `/ea-open` | ea-facilitator | Open or switch between engagements |
| `/ea-status` | ea-facilitator | Dashboard: all engagements and progress |
| `/ea-phase` | ea-facilitator | Start, edit, or resume an ADM phase |
| `/ea-migrate` | ea-facilitator | Detect and resolve version alignment gaps |
| `/ea-config` | ea-facilitator | Configure plugin settings, engagement rules, opt-outs, and refresh CLAUDE.md |
| `/ea-help` | ea-facilitator | List commands and getting-started guide |
| `/ea-interview` | ea-interviewer | Structured Q&A for any artifact / ADM phase |
| `/ea-brainstorm` | ea-facilitator | Capture freeform thoughts for current phase |
| `/ea-research` | ea-research | Add/apply research documents and links; proactive phase research planning and synthesis |
| `/ea-artifact` | ea-facilitator | Create, view, or list artifacts |
| `/ea-review` | ea-facilitator | Open artifact for review; track review state |
| `/ea-grill` | ea-interviewer | Deep-review artifact (9 grill-me skills) |
| `/ea-next` | ea-facilitator | Suggest the single most valuable next action based on engagement state |
| `/ea-notes` | ea-facilitator | List, view, edit, or delete interview notes, brainstorm notes, and review files |
| `/ea-consistency` | ea-consistency-checker | Focused consistency check: cross-artifact contradictions, within-artifact section inconsistencies, ID reference validation |
| `/ea-engage-review` | ea-consistency-checker | Full engagement: consistency + traceability |
| `/ea-security-review` | ea-security-auditor | Full engagement or single-artifact security audit — SABSA, ISO 27001, NIST CSF 2.0 coverage |
| `/ea-publish` | ea-facilitator | Publish artifacts into a consolidated document |
| `/ea-decisions` | ea-facilitator | Decision Register — aggregates all A3 rows |
| `/ea-adrs` | ea-facilitator | ADR Register — create, update, track ADRs |
| `/ea-risks` | ea-facilitator | Risk Register — aggregate, rate, track RIS-NNN |
| `/ea-changes` | ea-facilitator | Change Register — aggregate all ACR artifacts |
| `/ea-concerns` | ea-facilitator | Concerns Register — aggregate all A4 rows |
| `/ea-roles` | ea-facilitator | Role Catalogue — list, filter, generate, and update role assignments |
| `/ea-direction` | ea-facilitator | Direction Register — Goals, Objectives, Strategies aggregated from artifacts |
| `/ea-requirements` | ea-facilitator | Requirement management and artifact sync |
| `/ea-zachman` | ea-facilitator | Zachman Diagram — generate, review, gap, classify |
| `/ea-generate` | ea-facilitator | Generate .docx / .pptx / .mmd / .png / .svg |

---

## Plugin Structure

```
agents/          12 agents (ea-facilitator, ea-interviewer, ea-roadmap, ea-document-analyst, ea-research, ...)
commands/        30 commands (see Command Reference above)
skills/          9 skill directories (ea-artifact-templates, ea-engagement-lifecycle, zachman-framework, ...)
templates/       31 TOGAF artifact templates (.md)
scripts/         Python scripts for Word/PPTX generation
docs/PRD.md      Authoritative product requirements (v0.9.12)
hooks/hooks.json Plugin lifecycle hooks
```

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

## Key Reference Files

| File | Purpose |
|---|---|
| `skills/ea-artifact-templates/references/ea-concepts.md` | Canonical definitions for all 14 EA concepts — **single source of truth**; do not redefine inline |
| `skills/ea-artifact-templates/references/compliance-check.md` | Three-tier artifact compliance rules (T1/T2/T3); run on every artifact load |
| `skills/ea-artifact-templates/references/phase-interview-questions.md` | Full question bank for every ADM phase with output routing tables |
| `skills/ea-artifact-templates/references/cross-topic-detection.md` | 10-row signal map for detecting answers belonging in a different artifact |
| `skills/ea-artifact-templates/references/diagram-catalogue.md` | Expected diagrams per artifact type, Mermaid starters, naming conventions — used by ea-interviewer (§D prompts), ea-brainstorm (step 7), ea-grill (Step 8) |
| `skills/ea-artifact-templates/references/artifact-descriptions.md` | Purpose, audience, contents, and phase for every artifact type |
| `skills/ea-engagement-lifecycle/SKILL.md` | ID scheme, facilitator style, opt-out rules |
| `skills/ea-engagement-lifecycle/references/phase-constraints.md` | Per-phase runtime constraints: required artifacts, ID rules, traceability rules, blocking gates — read by ea-facilitator on phase entry, ea-interviewer at session start, ea-consistency-checker during validation |
| `skills/ea-engagement-lifecycle/references/context-loading.md` | Context loading protocol — Scope A (artifact), Scope B (phase), Scope C (full) — used by ea-grill, ea-review, ea-consistency, ea-interview, ea-brainstorm |
| `skills/ea-artifact-templates/SKILL.md` | A3 governance reference (states, transition rules) |
| `docs/PRD.md` | Full feature spec, data model, agent table, quality gates, success metrics |

## Skill Dependency Map

| Skill | Provides | Primary consumers |
|---|---|---|
| `ea-artifact-templates` | Templates, compliance rules, A3/A4/A5 governance, concept definitions | ea-interviewer, /ea-artifact, /ea-grill |
| `ea-engagement-lifecycle` | ID scheme, facilitator style, opt-out rules, session tracking | ea-facilitator, ea-interviewer |
| `zachman-framework` | Zachman 6×6 classification methods and source mappings | ea-facilitator, /ea-zachman |
| `ea-requirements-management` | REQ taxonomy, scope rules, sync protocol | /ea-requirements |
| `ea-interview-ui` | React artifact UI for Web/Display interview mode | /ea-interview |
| `ea-generation` | .docx/.pptx generation workflow, JSON extraction protocol | /ea-generate |
| `ea-document-ingestion` | Format layer — how to read each file type (PDF, DOCX, PPTX, etc.) | ea-document-analyst |
| `archimate-notation` | ArchiMate 3.x element types, notation rules | ea-facilitator |
| `ea-security` | SABSA ADM mapping, ISO 27001 controls, NIST CSF functions, artifact security checklists, security interview questions | ea-security-advisor, ea-security-auditor, ea-interviewer |

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
| CAP-NNN | Capability (Capability Model) | CAP-001 |

**Do not use domain-prefixed IDs** (BG-/DG-/AG-/TG- etc.) — the scheme is unified and domain-agnostic.

## Motivation Framework Chain

```
Vision → Mission → Business Drivers → Goals ← Strategies
                                          ↓
                              Issues (threaten)    Objectives ← Problems (block)
                                                       ↓
                                               Capability Model
                                                       ↓
                                                Operating Model
                                                       ↓
                                                   Metrics (leading/lagging)
                                                       ↓
                                             Requirements Register (traces all layers)
```

Capability Gaps (missing/immature capabilities) prevent Goals and trigger Phase E work packages.

---

## Agent Boundaries

| Agent | Owns | Does NOT do |
|---|---|---|
| `ea-facilitator` | Phase navigation, next-action decisions | Q&A, writing artifact fields |
| `ea-interviewer` | Structured Q&A, all interview modes | Phase navigation decisions |
| `ea-roadmap` | Roadmap creation/review (3 modes) | Other artifact types |
| `ea-document-converter` | Format conversion — converts uploads to `.md`/`.mmd` intermediates in `uploads/converted/` | EA mapping, artifact writes |
| `ea-document-analyst` | EA mapping layer — what to extract, where it goes | Format conversion (delegates to ea-document-converter) |
| `ea-document-ingestion` (skill) | Pipeline protocol — orchestrates converter → analyst → artifact write sequence | EA mapping decisions, format conversion |
| `ea-consistency-checker` | Cross-artifact consistency | Artifact creation |
| `ea-advisor` | TOGAF/Zachman/ArchiMate advisory, framework Q&A | Phase navigation, artifact writing |
| `ea-diagram` | Architecture diagram creation/editing/interpretation (Mermaid, Graphviz, Draw.io, ArchiMate) | EA mapping, artifact writes |
| `ea-requirements-analyst` | Document parsing → structured requirements register (FR/NFR/CON/PRI/ASS/DRV), ADM phase coverage map, Zachman coverage matrix, `requirements-index.json` population | Phase navigation, interview facilitation |
| `ea-research` | Proactive research planning (what to study per phase), multi-source synthesis, research quality audit, research impact traceability | Applying individual research items to artifacts (that's `/ea-research apply`), format conversion |
| `ea-security-advisor` | SABSA/ISO 27001/NIST CSF Q&A, security architecture decisions | Phase navigation, artifact writing |
| `ea-security-auditor` | Security control gap detection, SABSA/ISO/NIST coverage audit | Artifact creation, security Q&A |

---

## Architecture Roadmap — 3 Modes

The `ea-roadmap` agent auto-selects based on engagement state:

- **Review** — existing roadmap artifact found → check completeness, traceability, wave logic
- **Artifact-informed** — source artifacts exist, no roadmap → read Vision G/OBJ/STR, Gap Analysis, Requirements Register; build goal/strategy coverage register; derive work packages; each WP anchored to at least one G/OBJ/STR
- **Clean-slate** — no artifacts → 7-question elicitation sequence

## /ea-grill Workflow

Steps 1–6: load artifact → select skill → brief → run grill → produce output → offer to save review file
**Step 7 (apply findings):** walk through each recommended revision with `y/n/edit` per revision; applied revisions bump artifact version (patch) and update `lastModified`; sets `reviewStatus: In Review` (if previously Not Reviewed or Needs Revision); Approved artifacts warn before write.

## /ea-generate — Mermaid Image Rendering

`/ea-generate png` and `/ea-generate svg` render `.mmd` files to images using mermaid-cli (`mmdc`).

**Prerequisite:** `npm install -g @mermaid-js/mermaid-cli`
Auto-fallback: `npx -y @mermaid-js/mermaid-cli` (downloads on first run if `mmdc` not on PATH)

**Render single file:** `/ea-generate png diagrams/my-diagram.mmd`
**Render all diagrams:** `/ea-generate png --all`
**Options:** `--theme default|dark|forest|neutral|base` `--bg white|transparent|#rrggbb`

**Batch script:** `scripts/render-mermaid.py` — direct Python invocation for bulk rendering
```bash
python3 ea-assistant/scripts/render-mermaid.py EA-projects/{slug}/diagrams/ --format png --theme default
```

**WSL2 note:** If Puppeteer/Chromium fails: `export PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable`

## /ea-generate — Script Invocation

Scripts: `scripts/generate-docx.py` and `scripts/generate-pptx.py`

```bash
# Locate script (CLAUDE_PLUGIN_ROOT is not set automatically)
# Scripts are at ../../scripts relative to EA-projects/{slug}/, or find via:
SCRIPT=$(find "$HOME/.claude" -name "generate-docx.py" -path "*/ea-assistant/scripts/*" | head -1)

"$HOME/.ea-assistant-venv/bin/python" "$SCRIPT" \
  --type {script-type} \
  --engagement-dir EA-projects/{slug} \
  --content @/tmp/ea-gen-{artifact-id}.json \
  --diagrams @/tmp/ea-diagrams-{artifact-id}.json \
  --output EA-projects/{slug}/artifacts/{artifact-id}.docx
```

**`--type` values:** `vision`, `gap-analysis`, `app-portfolio`, `requirements-register`, `roadmap`, `stakeholder-map` — must match script's `ARTIFACT_SECTIONS` keys.

**JSON extraction:** Before calling the script, extract structured content from the artifact markdown into JSON. Keys must match `ARTIFACT_SECTIONS`. Strip headings, table markers, and frontmatter — pass plain text per section. If a section is absent, omit the key. Content is passed via `--content @file`, not via a non-existent `--input` flag.

**`--diagrams`** is optional; pass `[{"title":"...", "path":"..."}]` or `@file.json`. Diagrams are embedded as a final appendix (docx) or appended as slides (pptx).

---

## Research & References

The `ResearchAndReferences/` folder is the engagement library for external context.

**`/ea-research` modes:** `add` (paste document), `note` (freeform note), `link` (URL + summary), `list` (default, shows index), `view <item>` (full content), `apply [artifact-id]` (synthesise against deliverable)

**Apply workflow:** loads selected research items + target artifact → identifies gaps, contradictions, enhancements → `y/n/edit` per revision → bumps artifact version (patch) → writes synthesis report to `ResearchAndReferences/synthesis-{artifact-id}-{date}.md`

**Index file:** `ResearchAndReferences/research-index.md` — auto-maintained, tracks type/title/file/date/tags for every item

## Risk Management

The Risk Register (`templates/risk-register.md`) is a cross-cutting artifact generated by `/ea-risks`. It aggregates risks from all artifacts into a single register with RIS-NNN IDs, severity ratings, ownership, and mitigation tracking.

**Risk sources scanned by `/ea-risks`:**
- Architecture Vision — §14 Key Risks
- Statement of Architecture Work — Risk section
- Migration Plan — §4 Risk Register
- Architecture Compliance Assessment — Outstanding Risks
- Existing `risk-register-*.md` (curated RIS-NNN entries)

**`/ea-risks` modes:** `generate` (default, writes file), `status` (inline summary), `update RIS-NNN <field> <value>` (single field update)

**Risk rating:** Derived from Likelihood × Impact → Critical / High / Medium / Low (see template guidance block for matrix)

## Zachman Diagram

Cross-cutting classification artifact mapping all engagement content across the 6×6 grid (rows: Contextual → Functioning; columns: What / How / Where / Who / When / Why).

**`/ea-zachman` modes:** `generate` (auto-populate from existing artifacts), `review` (inline coverage matrix), `gap` (prioritised gap list with remediation actions), `interview` (guided Q&A row by row), `classify <artifact>` (cell classification for any artifact)

**Coverage indicator:** ✅ Populated / ⚠️ Partial / ❌ Empty / 🚫 Out of scope

**Key source mappings:**
- Architecture Vision → R1,C6 + R2,C6 (goals, drivers, strategies)
- Business Architecture → R2,C2 + R2,C4 (processes, organisation)
- Data Architecture → R2,C1 + R3,C1 + R4,C1 (semantic → logical → physical data)
- Application Architecture → R3,C2 + R3,C3 + R3,C4 (functions, distribution, roles)
- Technology Architecture → R4,C3 + R4,C2 (infrastructure, system design)
- Requirements Register → R2,C6 + R3,C6 (motivation, business rules)

**Row 6** is always 🚫 — it represents the running enterprise, observed not modelled.

## Architecture Decision Records

ADRs are standalone documents capturing significant architecture decisions — technology/vendor selection, pattern choices, make-vs-buy, data governance, security architecture, or any decision that is hard to reverse.

**ADR lifecycle:** `Candidate → In Progress → Completed → Superseded (by ADR-NNN) | Deprecated`

**ADR vs A3 Decision Log:**
- **A3** = governance state tracking inside an artifact (who decided what, at what authority, verified or not)
- **ADR** = standalone full-context document (situation, options analysis, rationale, consequences)
- Link them: A3 row `Notes` column should reference the ADR-NNN ID

**`/ea-adrs` modes:** `generate` (default, writes register), `status` (inline summary), `new` (create ADR from template), `update ADR-NNN <field> <value>` (single field update)

**ADR threshold:** `ea-interviewer` suggests an ADR when 2+ indicators apply (tech/vendor selection, high cost/risk, hard to reverse, make-vs-buy, contested by stakeholder, affects data governance/security/compliance/principles)

**`## Appendix A5 — Related Architecture Decisions` section** is required (T3-ADR) on: Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Architecture Roadmap, SAoW, Migration Plan, Compliance Assessment, Requirements Register, Engagement Charter, Governance Framework, Implementation Governance Plan

## Governance Artifacts

| Template | Phase | Purpose | Command |
|---|---|---|---|
| `governance-framework.md` | Prelim | Enterprise governance structure: ARB ToR, decision rights, ADM tailoring, compliance process | `/ea-artifact create governance-framework` |
| `implementation-governance-plan.md` | G | Engagement-specific governance: review schedule, checkpoints, waiver process, escalation | `/ea-artifact create implementation-governance-plan` |
| `change-register.md` | H | Aggregated view of all ACR artifacts | `/ea-changes` (generated) |

---

## Compliance Rules (Tier 3 — Artifact-specific)

| Rule | Artifact | Requirement |
|---|---|---|
| T3-A3 | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Consolidated Gap Analysis, Architecture Roadmap, Statement of Architecture Work, Migration Plan, Engagement Charter, Governance Framework, Implementation Governance Plan, Communications Plan, Architecture Definition Document, Transition Architectures | `## Appendix A3 — Decision Log` section present |
| T3-A5-ADR | Same artifact list as T3-A3 | `## Appendix A5 — Related Architecture Decisions` section present |
| T3-ROAD-SA | Architecture Roadmap | `## Strategic Alignment` section with at least one non-placeholder row |
| T3-ROAD-WP | Architecture Roadmap | At least one WP has non-empty `Advances Goals/Objectives` or `Executes Strategies` |
| T3-REQ | Requirements Register | Scope column present (Corporate / Project) |
| T3-TRACE | Traceability Matrix | Two-section structure (Corporate / Project) |

---

## EA Plugin Workflows

When running any EA command, first check that at least one engagement exists in `EA-projects/`. If none exist, offer to create one with `/ea-new` rather than displaying an empty state.

## UI Generation

For browser-based UIs (brainstorm pads, interview forms), always write plain HTML files to `EA-projects/{slug}/ui/` rather than rendering React artifacts. Open via `file://` path or a simple HTTP server. The `ea-interview-ui` skill handles this automatically when `uiMode` is unset (defaults to HTML file mode).

## Development Conventions

- **Validate frontmatter before every commit:** `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`
- **Agent frontmatter required:** `name`, `description`, `model`, `color`
- **Skill frontmatter required:** `name`, `description`, `version`
- **Command frontmatter required:** `name`, `description`
- **Do not redefine concepts inline** — always reference `ea-concepts.md`
- **Feature branches + PRs** for multi-file changes; direct commits to `main` for single-file fixes

## Documentation Update Checklist

Before bumping `plugin.json` version and before pushing, always update these files to reflect new features, changed commands, or revised behaviour:

| File | What to update |
|---|---|
| `.claude-plugin/plugin.json` | Version number; description if feature set changed |
| `../.claude-plugin/marketplace.json` | Version and description — **must exactly match `plugin.json`** |
| `docs/PRD.md` | Version number; new sections for any new feature area; revised command/agent/template counts; quality gates if changed |
| `commands/ea-help.md` | Commands table (add/remove rows); tips section (add tips for new features) |
| `README.md` | Feature bullet list; commands table; prerequisite changes; project storage layout if changed |
| `CLAUDE.md` (this file) | Version number; Plugin Structure counts; Command Reference table; ID scheme additions; new compliance rules; Skill Dependency Map |

**`plugin.json` ↔ `marketplace.json` sync rule:** The `version` and `description` fields in `ea-assistant/.claude-plugin/plugin.json` and the corresponding entry in `.claude-plugin/marketplace.json` must always be identical. Update both in the same edit — never one without the other.

**When a version bump is the only change** (no new features), update the version number in all six files only — no other edits needed.

**When the docs are out of date**, bring them up to date before the next version bump — do not accumulate undocumented versions.
