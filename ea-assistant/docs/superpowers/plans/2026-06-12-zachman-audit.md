# Zachman Diagram Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add completeness/consistency auditing for the Zachman Diagram — six check categories defined once, invoked from both a new `/ea-zachman audit` mode and a `/ea-grill` routing block.

**Architecture:** A checklist reference in the `zachman-framework` skill is the single source of truth for checks, severity, and report format. The 6×6 expected-model table (framework knowledge) goes into the existing `zachman-cell-descriptions.md` as a per-cell `Expected Model:` line; the checklist's perspective-purity category references it. Two thin entry points execute the checklist by reference.

**Tech Stack:** Markdown instruction files (Claude Code plugin framework). Verification = `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/` + grep checks per task.

**Spec:** `ea-assistant/docs/superpowers/specs/2026-06-12-zachman-audit-design.md`

**Working directory:** paths relative to `ea-assistant/` unless prefixed `../`. Commands run from repo root `/mnt/d/dev/claude-sandbox/plugins/`.

---

### Task 1: Audit Checklist Reference

**Files:**
- Create: `skills/zachman-framework/references/zachman-audit-checklist.md`

- [ ] **Step 1: Write the checklist file**

Create `skills/zachman-framework/references/zachman-audit-checklist.md` with exactly this content:

````markdown
# Zachman Diagram Audit Checklist

Single source of truth for Zachman Diagram quality auditing. Consumed by:
- `/ea-zachman audit` — standalone audit mode
- `/ea-grill` — Zachman Diagram grilling block in `skills/ea-grill-skills/SKILL.md`

Neither entry point restates these checks — both execute this checklist by reference.

The audit targets the most recent `artifacts/cross-cutting/context/zachman-diagram-*.md`. It complements (does not replace) `/ea-zachman review` and `gap`, which measure cell *presence*; this checklist measures cell *quality* — honesty, coherence, currency, scope, and perspective purity.

Every check yields one of: ✅ pass · ⚠ fail · ❓ unverifiable (insufficient information to confirm or deny).

---

## Check Categories

### 1. Cell honesty

For every cell marked ✅ in the Coverage Summary:
- The cell section has at least 2 substantive bullets (a bullet restating the cell name or containing only an ID is not substantive).
- The cell cites at least one source reference (artifact name or path).
- Overstated coverage: a ✅ cell failing either test is flagged — "Coverage overstated: R{N},C{N} marked ✅ but {reason}."

For every cell marked ⚠️: the cell text states what is missing (not just partial content with no annotation).

For every non-❌ cell: no placeholder text — `TBD`, `TODO`, `⚠️ Not answered`, `⊘`.

### 2. Row refinement

For each column with two or more vertically adjacent populated cells, R(N) content must be a traceable refinement of R(N−1). Verify by opening the contributing source artifacts (per `references/cell-extraction-map.md`), not just the grid text:
- R3,C1 logical entities trace to R2,C1 conceptual entities (compare against Data Architecture conceptual vs logical model sections).
- R3,C2 application components/services trace to R2,C2 capabilities or processes (compare against Application Architecture and Business Architecture).
- R4,Cx technology content traces to R3,Cx logical content (compare against Technology Architecture vs Application/Data Architecture).
- Flag: "Refinement break: R{N},C{N} introduces {element} with no antecedent in R{N−1},C{N}."

### 3. Column consistency

- Every ID cited in any cell (CAP-NNN, REQ-NNN, ROLE-NNN, ABB-NNN, SBB-NNN, VS-NNN, G-NNN, …) exists in its register or source artifact. Dangling IDs are flagged High.
- The same element is named identically wherever it appears across cells (e.g. a capability named "Order Management" in R2,C2 must not appear as "Order Mgmt Service" in R3,C2 without an explicit mapping note).
- No two cells claim contradictory facts about the same element (e.g. an application listed as retired in one cell and as target-state in another).

### 4. Staleness

- Read the diagram's generation date (filename `zachman-diagram-{YYYY-MM-DD}.md` or frontmatter).
- For each contributing artifact in `references/cell-extraction-map.md`, compare its `lastModified` (frontmatter; file mtime as fallback) against the diagram date.
- Flag each cell whose sources changed after generation: "Stale: R{N},C{N} — {artifact} modified {date}, after diagram generation."
- If stale cells exceed one third of populated cells, the overall verdict becomes **Stale** and the primary recommendation is `/ea-zachman generate` before any cell-level fixes.

### 5. Scope honesty

- Every 🚫 cell must be justified by `engagement.json → architectureDomains` or a recorded scope decision (Engagement Charter scope section, or an A3 entry). Unjustified 🚫 in an in-scope domain is flagged High.
- An in-scope domain with an entire row or column marked 🚫 is flagged High: "Whole {row/column} excluded but domain {name} is in scope."

### 6. Perspective purity (primitive model fit)

One cell = one primitive model. For each populated cell, compare its content against the `Expected Model:` line for that cell in `references/zachman-cell-descriptions.md`:
- Content belonging to a lower row's perspective in an upper row is flagged (e.g. physical schema details in R2,C1; vendor product names in R2,C2).
- Content belonging to an upper row in a lower row is flagged (e.g. business goal prose in R4,C6).
- A bundle artifact (e.g. Architecture Definition Document) cited as a source is acceptable only if the cell's extracted content is the separable primitive model — citing the bundle with no extracted model content is flagged.
- Flag: "Perspective mix: R{N},C{N} contains {description} which belongs to R{M} ({expected model})."

---

## Severity Assignment

| Severity | Findings |
|---|---|
| High | Overstated ✅ cells; contradictory claims; dangling IDs; unjustified 🚫 in in-scope domains; whole in-scope row/column excluded |
| Medium | Missing source references; refinement breaks; stale cells; perspective mixing; bundle cited without separable model |
| Low | Naming drift without contradiction; thin ⚠️ annotations |

All findings in R5/R6 default to Low regardless of category — those rows describe implementation and operational reality usually outside documentation scope (consistent with `/ea-zachman gap` severity rules).

---

## Report Format

Both entry points render this structure (grill additionally feeds findings into its own scorecard and verdict):

```
ZACHMAN AUDIT — {engagement name}
Diagram: {filename} (generated {date})  |  Audited: {YYYY-MM-DD}
════════════════════════════════════════════════════

Category scorecard
──────────────────────────────────────────────────
1. Cell honesty          ✅ {n}  ⚠ {n}  ❓ {n}
2. Row refinement        ✅ {n}  ⚠ {n}  ❓ {n}
3. Column consistency    ✅ {n}  ⚠ {n}  ❓ {n}
4. Staleness             ✅ {n}  ⚠ {n}  ❓ {n}
5. Scope honesty         ✅ {n}  ⚠ {n}  ❓ {n}
6. Perspective purity    ✅ {n}  ⚠ {n}  ❓ {n}

Findings — High
──────────────────────────────────────────────────
{cell ref} — {finding} → {action}

Findings — Medium
──────────────────────────────────────────────────
{cell ref} — {finding} → {action}

Findings — Low
──────────────────────────────────────────────────
{cell ref} — {finding} → {action}

Verdict: {Ready | Needs revision | Stale}
```

**Verdict rules:** **Ready** — no High findings. **Needs revision** — one or more High findings. **Stale** — stale cells exceed one third of populated cells (overrides the other two; fix currency first).
````

- [ ] **Step 2: Verify**

```bash
grep -c "^### " ea-assistant/skills/zachman-framework/references/zachman-audit-checklist.md
```
Expected: `6`

```bash
grep -n "Verdict rules" ea-assistant/skills/zachman-framework/references/zachman-audit-checklist.md
```
Expected: one match.

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/skills/zachman-framework/references/zachman-audit-checklist.md
git commit -m "feat(ea-assistant): add Zachman audit checklist reference (6 check categories)"
```

---

### Task 2: Expected Model Lines in Cell Descriptions

**Files:**
- Modify: `skills/zachman-framework/references/zachman-cell-descriptions.md`

The file has 36 cell blocks under `## Cell-by-Cell Descriptions`, each shaped:

```markdown
#### Cell {R},{C} — {Name}
**Purpose:** ...
**Example Content:** ...
**Example Artefacts:** ...
```

- [ ] **Step 1: Add an `**Expected Model:**` line to every cell block**

Insert the line immediately AFTER the `**Purpose:**` line of each cell, using this mapping (row, column → text):

| Cell | Expected Model text |
|---|---|
| 1,1 | High-level subject list — things important to the business; vocabulary, not a data model |
| 1,2 | Business capability list — high-level functions in scope |
| 1,3 | Location/site list — regions, sites, business locations |
| 1,4 | Organization list — business units and external parties in scope |
| 1,5 | Major business events and cycles list |
| 1,6 | Goals/objectives list — strategy intent, not detailed motivation modelling |
| 2,1 | Conceptual data model — business concepts and relationships |
| 2,2 | Business process model — value streams, BPMN L2/L3 |
| 2,3 | Business logistics/location model — business nodes and connections |
| 2,4 | Organization model — roles and responsibilities, business-level RACI |
| 2,5 | Business event model — business cycles and event lifecycles |
| 2,6 | Business motivation model — ends/means: goals, strategies, policies, rules |
| 3,1 | Logical data model — normalised entities and attributes |
| 3,2 | Application/function architecture — logical services and use cases |
| 3,3 | Logical network/distribution architecture — system nodes and integrations |
| 3,4 | Logical identity and access / role model — actors and permissions model |
| 3,5 | Logical state/sequence model — state machines, sequence diagrams |
| 3,6 | Business rules specification — decision tables, rule catalogue |
| 4,1 | Physical data design — schemas, tables, storage structures |
| 4,2 | Component design — modules, APIs, programs, microservices design |
| 4,3 | Technology network architecture — environments, zones, routing |
| 4,4 | Workforce/ops design — job designs, runbook ownership, support model |
| 4,5 | Job schedules and orchestration design — batch windows, triggers |
| 4,6 | Rule implementation design — rules engines/configs, control design |
| 5,1 | DDL / database build scripts — indexes, constraints |
| 5,2 | Program specs / code — detailed algorithms |
| 5,3 | Network configs — firewalls, DNS, IaC templates |
| 5,4 | Security configs — IAM policies, groups, entitlements |
| 5,5 | Scheduler configs — cron, pipelines, event triggers |
| 5,6 | Policy-as-code / rules tables — configured policies and rules |
| 6,1 | Actual data — records in production |
| 6,2 | Running processes and applications |
| 6,3 | Live network as operated |
| 6,4 | Real people executing roles |
| 6,5 | Actual timing and performance — logs, metrics, SLA results |
| 6,6 | Operational outcomes — KPI attainment, actual decisions made |

Each inserted line has the form (example for Cell 1,1):

```markdown
**Expected Model:** High-level subject list — things important to the business; vocabulary, not a data model
```

Also add one sentence to the file's intro paragraph (after "with purpose, example content, and example artefacts for each."):

```markdown
Each cell also carries an **Expected Model** line — the primitive model that belongs in that cell (one cell = one primitive model; mixing perspectives across rows is an audit finding per `zachman-audit-checklist.md`).
```

- [ ] **Step 2: Verify**

```bash
grep -c "\*\*Expected Model:\*\*" ea-assistant/skills/zachman-framework/references/zachman-cell-descriptions.md
```
Expected: `36`

```bash
grep -c "^#### Cell" ea-assistant/skills/zachman-framework/references/zachman-cell-descriptions.md
```
Expected: `36` (unchanged — no cells added or removed)

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/skills/zachman-framework/references/zachman-cell-descriptions.md
git commit -m "feat(ea-assistant): add Expected Model line to all 36 Zachman cell descriptions"
```

---

### Task 3: `/ea-zachman audit` Mode

**Files:**
- Modify: `commands/ea-zachman.md`

- [ ] **Step 1: Update frontmatter**

Change:
```yaml
description: Create, populate, and review the Zachman Diagram for an EA engagement — generate from existing artifacts, interview to fill gaps, produce coverage analysis, and classify any artifact against the 6×6 grid
argument-hint: "[generate | review | gap | interview | classify <artifact-name>]"
```
to:
```yaml
description: Create, populate, review, and audit the Zachman Diagram for an EA engagement — generate from existing artifacts, interview to fill gaps, produce coverage analysis, audit completeness and consistency, and classify any artifact against the 6×6 grid
argument-hint: "[generate | review | gap | interview | audit | classify <artifact-name>]"
```

- [ ] **Step 2: Update the Overview modes line**

Change:
```markdown
**Modes:** `generate` (default), `review`, `gap`, `interview`, `classify <artifact-name>`
```
to:
```markdown
**Modes:** `generate` (default), `review`, `gap`, `interview`, `audit`, `classify <artifact-name>`
```

And in the **Reference files** list, add this line after the `zachman-cell-descriptions.md` entry:
```markdown
- `skills/zachman-framework/references/zachman-audit-checklist.md` — six audit check categories, severity model, report format (used by `audit` mode and `/ea-grill`)
```

- [ ] **Step 3: Add the audit mode section**

Insert the following AFTER the `## Mode: classify <artifact-name>` section (at the end of the file):

````markdown
---

## Mode: `audit`

Quality audit of the Zachman Diagram — completeness honesty, consistency, currency, scope, and perspective purity. Complements `review`/`gap` (presence) with quality checks.

1. **Locate the diagram.** Find the most recent `EA-projects/{slug}/artifacts/cross-cutting/context/zachman-diagram-*.md`. If none exists, error: "No Zachman Diagram found — run `/ea-zachman generate` first."
2. **Run the checklist.** Load `skills/zachman-framework/references/zachman-audit-checklist.md` and execute all six categories with cross-artifact verification: open contributing artifacts per `cell-extraction-map.md`, verify cited IDs against their registers, compare modification dates, and compare cell content against each cell's `Expected Model:` line in `zachman-cell-descriptions.md`. The check definitions live in the checklist — do not restate them here.
3. **Render the report inline** using the checklist's Report Format: category scorecard, findings grouped High / Medium / Low (each with cell reference, evidence, and concrete action), and the verdict (Ready / Needs revision / Stale, per the checklist's verdict rules).
4. **Save the report** to `EA-projects/{slug}/artifacts/cross-cutting/notes/reviews/zachman-audit-{YYYY-MM-DD}.md` (create the folder if needed).
5. **Offer next actions:**
   - Verdict Stale → "Re-run `/ea-zachman generate` to refresh from current artifacts? (y/n)"
   - Otherwise → "Run `/ea-zachman interview` jumping to the failing cells? (y/n)"
   - Then ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md (the --next flag section)` and output the recommendation.
````

- [ ] **Step 4: Verify**

```bash
grep -n "Mode: \`audit\`" ea-assistant/commands/ea-zachman.md
grep -c "audit" ea-assistant/commands/ea-zachman.md
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```
Expected: audit mode section present; multiple `audit` matches (frontmatter, modes line, reference list, mode section); validation 0 errors.

- [ ] **Step 5: Commit**

```bash
git add ea-assistant/commands/ea-zachman.md
git commit -m "feat(ea-assistant): add audit mode to /ea-zachman"
```

---

### Task 4: `/ea-grill` Zachman Routing Block

**Files:**
- Modify: `skills/ea-grill-skills/SKILL.md` (after the Matrix artifact grilling block at line ~358)

- [ ] **Step 1: Insert the block**

Find:

```markdown
**Matrix artifact grilling:**
If the artifact under review is itself a matrix (frontmatter contains a `matrixKey` field):
- Look up the key in `skills/ea-artifact-templates/references/matrix-catalogue.md` and run the full check set defined by `/ea-matrix check` mode in `commands/ea-matrix.md` (axes check, marker check, orphan check, catalogue grill checks, approval check) — the check definitions live in the catalogue; do not restate them.
- Report each as ✅ / ⚠ / ❓ in the scorecard, and treat ⚠ marker or axes failures as Inconsistent sections in the verdict.
```

Immediately AFTER it (before the `---` preceding "At the end, provide:"), insert a blank line followed by:

```markdown
**Zachman Diagram grilling:**
If the artifact under review is a Zachman Diagram (artifact id or filename matches `zachman-diagram*`):
- Run the audit checklist from `skills/zachman-framework/references/zachman-audit-checklist.md` — all six categories with cross-artifact verification (contributing artifacts per the cell-extraction-map; cited IDs against registers; modification dates; cell content against each cell's `Expected Model:` line in `zachman-cell-descriptions.md`). The check definitions live in the checklist; do not restate them.
- Feed findings into the standard grill output: High findings map to Inconsistent sections in the verdict; the checklist's Stale verdict maps to "Needs revision" with re-generation (`/ea-zachman generate`) as the top prioritised revision.
- Grill's standard apply flow holds — applying fixes bumps the diagram artifact version and saves the review file per grill's convention.
```

- [ ] **Step 2: Verify**

```bash
grep -n "Zachman Diagram grilling" ea-assistant/skills/ea-grill-skills/SKILL.md
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
```
Expected: one match, located after the Matrix artifact grilling block and before "At the end, provide:"; validation 0 errors.

- [ ] **Step 3: Commit**

```bash
git add ea-assistant/skills/ea-grill-skills/SKILL.md
git commit -m "feat(ea-assistant): add Zachman Diagram grilling block to grill skill"
```

---

### Task 5: Docs and Version Bump (0.9.63)

**Files:**
- Modify: `commands/ea-help.md`, `CLAUDE.md`, `.claude-plugin/plugin.json`, `../.claude-plugin/marketplace.json`, `docs/PRD.md`, `README.md`
- Modify (frontmatter version only): `skills/zachman-framework/SKILL.md`, `skills/ea-grill-skills/SKILL.md`

- [ ] **Step 1: ea-help.md**

Line 112, change:
```markdown
| `/ea-zachman [mode]` | Manage the Zachman 6×6 classification diagram (generate, review, gap, interview, classify) |
```
to:
```markdown
| `/ea-zachman [mode]` | Manage the Zachman 6×6 classification diagram (generate, review, gap, interview, audit, classify) |
```
Do NOT change any command count — no new command was added.

- [ ] **Step 2: README.md**

Line 56, change:
```markdown
- **Zachman Diagram** — `/ea-zachman` auto-populates and manages the 6×6 classification grid; generate, review, gap, interview, and classify modes
```
to:
```markdown
- **Zachman Diagram** — `/ea-zachman` auto-populates and manages the 6×6 classification grid; generate, review, gap, interview, audit, and classify modes — audit checks completeness honesty, row/column consistency, staleness, scope, and perspective purity
```

Line 201, change:
```markdown
| `/ea-zachman [mode]` | Manage the Zachman 6×6 classification diagram — generate, review, gap, interview, classify |
```
to:
```markdown
| `/ea-zachman [mode]` | Manage the Zachman 6×6 classification diagram — generate, review, gap, interview, audit, classify |
```

- [ ] **Step 3: Version bumps**

- `CLAUDE.md`: `**Current version:** 0.9.62` → `**Current version:** 0.9.63` (command count stays 55 — do not change it)
- `.claude-plugin/plugin.json`: `"version": "0.9.62"` → `"version": "0.9.63"`
- `../.claude-plugin/marketplace.json`: ea-assistant entry `"version": "0.9.62"` → `"version": "0.9.63"`
- `skills/zachman-framework/SKILL.md` and `skills/ea-grill-skills/SKILL.md`: frontmatter `version:` → `0.9.63`

Verify JSON parses:
```bash
python3 -c "import json; json.load(open('ea-assistant/.claude-plugin/plugin.json')); json.load(open('.claude-plugin/marketplace.json')); print('OK')"
```

- [ ] **Step 4: PRD.md**

Add a `## v0.9.63 — Zachman Diagram Audit` section above the v0.9.62 section (match its format), covering: the six-category audit checklist (cell honesty, row refinement, column consistency, staleness, scope honesty, perspective purity), the `Expected Model:` line on all 36 cell descriptions, `/ea-zachman audit` mode (inline report + saved review file, Ready/Needs revision/Stale verdict), and the `/ea-grill` Zachman routing block. Update the version line at the top of the PRD to 0.9.63.

- [ ] **Step 5: Verify**

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/
grep -rn "0.9.62" ea-assistant/CLAUDE.md ea-assistant/.claude-plugin/plugin.json .claude-plugin/marketplace.json
grep -n "audit" ea-assistant/commands/ea-help.md | head -2
```
Expected: 0 errors; no remaining `0.9.62` in those three files; ea-help shows audit in the /ea-zachman row.

- [ ] **Step 6: Commit**

```bash
git add ea-assistant/commands/ea-help.md ea-assistant/README.md ea-assistant/CLAUDE.md ea-assistant/.claude-plugin/plugin.json .claude-plugin/marketplace.json ea-assistant/docs/PRD.md ea-assistant/skills/zachman-framework/SKILL.md ea-assistant/skills/ea-grill-skills/SKILL.md
git commit -m "feat(ea-assistant): v0.9.63 — Zachman Diagram audit"
```

---

## Final Verification

```bash
~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/                                  # 0 errors
grep -c "^### " ea-assistant/skills/zachman-framework/references/zachman-audit-checklist.md           # 6
grep -c "\*\*Expected Model:\*\*" ea-assistant/skills/zachman-framework/references/zachman-cell-descriptions.md  # 36
grep -n "zachman-audit-checklist.md" ea-assistant/commands/ea-zachman.md ea-assistant/skills/ea-grill-skills/SKILL.md  # both consumers reference the checklist
```
