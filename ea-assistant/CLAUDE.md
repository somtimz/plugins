# EA Assistant — Developer Context

Plugin for managing Enterprise Architecture engagements end-to-end. TOGAF 10 process backbone, Zachman classification, ArchiMate 3.x notation.

**Current version:** 0.9.9 (plugin.json)
**Branch:** `feat/risk-management`

---

## Plugin Structure

```
agents/          8 agents (ea-facilitator, ea-interviewer, ea-roadmap, ea-document-analyst, ...)
commands/        20 commands (/ea-new, /ea-open, /ea-phase, /ea-interview, /ea-grill, /ea-changes, /ea-migrate, /ea-adrs, /ea-zachman, ...)
skills/          8 skill directories (ea-artifact-templates, ea-engagement-lifecycle, zachman-framework, ...)
templates/       23 TOGAF artifact templates (.md)
scripts/         Python scripts for Word/PPTX generation
docs/PRD.md      Authoritative product requirements (v0.9.4)
hooks/hooks.json Plugin lifecycle hooks
```

## Key Reference Files

| File | Purpose |
|---|---|
| `skills/ea-artifact-templates/references/ea-concepts.md` | Canonical definitions for all 13 EA concepts — **the single source of truth**; do not redefine concepts inline in agents or skills |
| `skills/ea-artifact-templates/references/compliance-check.md` | Three-tier artifact compliance rules (T1/T2/T3); all artifact-loading operations run this |
| `skills/ea-artifact-templates/references/phase-interview-questions.md` | Full question bank for every ADM phase with output routing tables |
| `skills/ea-artifact-templates/references/cross-topic-detection.md` | 10-row signal map for detecting answers that belong in a different artifact |
| `skills/ea-artifact-templates/references/artifact-descriptions.md` | Purpose, audience, contents, and phase for every artifact type |
| `skills/ea-engagement-lifecycle/SKILL.md` | ID scheme (DRV/G/OBJ/STR/MET/ISS/PRB), facilitator style behaviour, opt-out rules |
| `skills/ea-artifact-templates/SKILL.md` | A3 governance reference (states, transition rules) |
| `docs/PRD.md` | Full feature spec, data model, agent table, quality gates, success metrics |

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

## Agent Boundaries

| Agent | Owns | Does NOT do |
|---|---|---|
| `ea-facilitator` | Phase navigation, next-action decisions | Q&A, writing artifact fields |
| `ea-interviewer` | Structured Q&A, all interview modes | Phase navigation decisions |
| `ea-roadmap` | Roadmap creation/review (3 modes) | Other artifact types |
| `ea-document-analyst` | EA mapping layer — what to extract, where it goes | Format extraction (owns: ea-document-ingestion skill) |
| `ea-document-ingestion` (skill) | Format layer — how to read each file type | EA mapping decisions |
| `ea-consistency-checker` | Cross-artifact consistency | Artifact creation |

## Architecture Roadmap — 3 Modes

The `ea-roadmap` agent auto-selects based on engagement state:
- **Review** — existing roadmap artifact found → check completeness, traceability, wave logic
- **Artifact-informed** — source artifacts exist, no roadmap → read Vision G/OBJ/STR, Gap Analysis, Requirements Register; build goal/strategy coverage register; derive work packages; each WP anchored to at least one G/OBJ/STR
- **Clean-slate** — no artifacts → 7-question elicitation sequence

## /ea-grill Workflow

Steps 1–6: load artifact → select skill → brief → run grill → produce output → offer to save review file
**Step 7 (apply findings):** walk through each recommended revision with `y/n/edit` per revision; applied revisions bump artifact version (patch) and update `lastModified`; sets `reviewStatus: Revised`; Approved artifacts warn before write.

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
SCRIPT=$(find "$HOME/.claude" -name "generate-docx.py" -path "*/ea-assistant/scripts/*" | head -1)

"$HOME/.ea-assistant-venv/bin/python" "$SCRIPT" \
  --type {script-type} \
  --engagement-dir EA-projects/{slug} \
  --content @/tmp/ea-gen-{artifact-id}.json \
  --output EA-projects/{slug}/artifacts/{artifact-id}.docx
```

`--type` values: `vision`, `gap-analysis`, `app-portfolio`, `requirements-register`, `roadmap`, `stakeholder-map` — must match script's `ARTIFACT_SECTIONS` keys.
Content JSON must be extracted from the artifact markdown by Claude before calling the script; it is passed via `--content @file`, not via a non-existent `--input` flag.

## Compliance Rules (Tier 3 — Artifact-specific)

| Rule | Artifact | Requirement |
|---|---|---|
| T3-A3 | Architecture Vision, Business/Data/App/Tech Architecture | `## Appendix A3 — Decision Log` section present |
| T3-ROAD-SA | Architecture Roadmap | `## Strategic Alignment` section with at least one non-placeholder row |
| T3-ROAD-WP | Architecture Roadmap | At least one WP has non-empty `Advances Goals/Objectives` or `Executes Strategies` |
| T3-REQ | Requirements Register | Scope column present (Corporate / Project) |
| T3-TRACE | Traceability Matrix | Two-section structure (Corporate / Project) |

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

The Zachman Diagram is a cross-cutting classification artifact that maps all engagement content across the 6×6 grid (rows: Contextual → Functioning; columns: What / How / Where / Who / When / Why).

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

**Template:** `zachman-diagram.md` (created/updated by `/ea-zachman`)

---

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

**Templates:** `architecture-decision-record.md` (individual ADR), `adr-register.md` (aggregate, generated by `/ea-adrs generate`)

---

## Governance Artifacts

Three new governance templates covering Preliminary through Phase H:

| Template | Phase | Purpose | Command |
|---|---|---|---|
| `governance-framework.md` | Prelim | Enterprise governance structure: ARB ToR, decision rights, ADM tailoring, compliance process | `/ea-artifact create governance-framework` |
| `implementation-governance-plan.md` | G | Engagement-specific governance: review schedule, checkpoints, waiver process, escalation | `/ea-artifact create implementation-governance-plan` |
| `change-register.md` | H | Aggregated view of all ACR artifacts | `/ea-changes` (generated) |

**`/ea-changes` modes:** `generate` (default, writes change-register file), `status` (inline summary), `update <ACR-ID> <field> <value>` (single field update)

---

## Development Conventions

- **Validate frontmatter before every commit:** `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`
- **Agent frontmatter required:** `name`, `description`, `model`, `color`
- **Skill frontmatter required:** `name`, `description`, `version`
- **Command frontmatter required:** `name`, `description`
- **Do not redefine concepts inline** — always reference `ea-concepts.md`; do not redefine style rules inline — reference `ea-engagement-lifecycle/SKILL.md`
- **Do not duplicate logic across agents** — cross-topic detection lives in `cross-topic-detection.md`; A3 governance rules live in `ea-artifact-templates/SKILL.md`; concept definitions live in `ea-concepts.md`
- **Feature branches + PRs** for multi-file changes; direct commits to `main` for single-file fixes

## Engagement Storage Layout (Runtime)

```
EA-projects/{slug}/
├── engagement.json        # all state: phases, artifacts, sessions, direction, metrics, optOuts
├── CLAUDE.md              # auto-generated per-engagement context (overwritten on /ea-open)
├── artifacts/             # .md artifacts + .review.md review files
├── reviews/               # /ea-grill output files
├── interviews/            # session-log.md + dated interview notes
├── brainstorm/            # brainstorm-notes.md
├── diagrams/              # .mmd, .dot, .drawio
├── uploads/               # source documents for ingestion
└── ui/                    # generated HTML interview/brainstorm forms
```

The `CLAUDE.md` inside each engagement folder is auto-generated and **will be overwritten** on every `/ea-open`. Do not edit it manually; use `brainstorm/brainstorm-notes.md` for persistent notes within an engagement.
