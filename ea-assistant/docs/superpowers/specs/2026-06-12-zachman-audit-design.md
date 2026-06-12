# Zachman Diagram Audit Feature Design

**Date:** 2026-06-12
**Status:** Approved
**Scope:** ea-assistant plugin

---

## Overview

Add a quality audit for the Zachman Diagram — completeness and consistency checks that go beyond the existing presence-based modes (`/ea-zachman review` and `gap` measure whether cells are filled; nothing checks whether the content is honest, internally consistent, current, or correctly scoped).

One checklist reference is the single source of truth. Two entry points invoke it: a new `/ea-zachman audit` mode and a Zachman routing block in `/ea-grill`.

---

## 1. Audit Checklist Reference

New file: `skills/zachman-framework/references/zachman-audit-checklist.md` (alongside the existing four zachman references).

Six check categories. Each check yields ✅ pass / ⚠ fail / ❓ unverifiable (the grill-standard trio). Severity per finding reuses `/ea-zachman gap`'s model: High / Medium / Low.

| # | Category | Checks |
|---|---|---|
| 1 | **Cell honesty** | Every ✅ cell has ≥2 substantive bullets and ≥1 source reference; every ⚠️ cell states what is missing; no placeholder text (`TBD`, `TODO`, `⚠️ Not answered`, `⊘`) appears in any non-❌ cell; coverage symbols match content (a ✅ cell with one thin bullet is flagged as overstated) |
| 2 | **Row refinement** | For each populated column, R(N) content is a traceable refinement of R(N−1): R3/What logical entities trace to R2/What conceptual entities; R3/How application components trace to R2/How capabilities or processes; R4 technology components trace to R3 application components. Verified by opening the contributing source artifacts (Business / Data / Application / Technology Architecture per the cell-extraction-map), not just the grid text |
| 3 | **Column consistency** | Every ID cited in a cell (CAP-NNN, REQ-NNN, ROLE-NNN, ABB-NNN, SBB-NNN, …) exists in its register or source artifact; the same element is named identically across cells; no two cells claim contradictory facts about the same element |
| 4 | **Staleness** | Compare the diagram file's date against the `lastModified` (frontmatter or file mtime) of each contributing artifact listed in `skills/zachman-framework/references/cell-extraction-map.md`; flag every cell whose sources changed after the diagram was generated; suggest re-running `/ea-zachman generate` when stale cells exceed a third of populated cells |
| 5 | **Scope honesty** | Every 🚫 cell is justified by `engagement.json → architectureDomains` or a recorded scope decision (Engagement Charter scope section or A3 entry); an in-scope domain with an entire row or column marked 🚫 is flagged High |
| 6 | **Perspective purity (primitive model fit)** | One cell = one primitive model. Each populated cell's content matches the expected model type for that cell per the 6×6 expected-model table in `skills/zachman-framework/references/zachman-cell-descriptions.md` — e.g., physical schema details in R2/What (Owner row) flagged; business goals prose in R4/Why flagged. A bundle artifact (e.g., Architecture Definition Document) cited as a source is acceptable only if the cell's extract is the separable primitive model, not the whole document |

**Severity assignment guidance** (stated in the checklist file):
- High — overstated ✅ cells, contradictory claims, dangling IDs, unjustified 🚫 in in-scope domains
- Medium — missing source references, broken row refinement, stale cells, perspective mixing
- Low — naming drift without contradiction, thin ⚠️ annotations; all R5/R6 findings default to Low (depth those rows describe is usually outside documentation scope — consistent with `/ea-zachman gap`'s severity rules)

The checklist file also defines the report format (see §2) so both entry points render identically.

### 6×6 Expected-Model Table

The expected primitive model per cell lives in `skills/zachman-framework/references/zachman-cell-descriptions.md` — each cell entry gains an `Expected model:` line. It is framework knowledge, not audit logic: the audit's category 6 references it, and `generate`/`interview` can reuse it later without duplication. Content (condensed; full prose in the reference):

| Row \ Col | What (Data) | How (Function) | Where (Network) | Who (People) | When (Time) | Why (Motivation) |
|---|---|---|---|---|---|---|
| R1 Planner / Scope | High-level subject list | Capability list | Location/site list | Organization list | Major business events/cycles | Goals/objectives list |
| R2 Owner / Conceptual | Conceptual data model | Business process model (value streams, BPMN L2/L3) | Business logistics/location model | Organization model (roles, business RACI) | Business event model | Business motivation model (ends/means: goals, strategies, policies, rules) |
| R3 Designer / Logical | Logical data model (entities, attributes) | Application/function architecture (logical services, use cases) | Logical network/distribution architecture | Logical identity & access / role model | Logical state/sequence model | Business rules specification (decision tables, rule catalog) |
| R4 Builder / Physical | Physical data design (schemas, storage) | Component design (modules, APIs, microservices) | Technology network architecture (environments, zones) | Workforce/ops design (job designs, runbooks, support model) | Job schedules & orchestration design | Rule implementation design (rules engines, control design) |
| R5 Subcontractor / Detailed | DDL / DB build scripts | Program specs / code | Network configs (firewalls, DNS, IaC) | Security configs (IAM policies, entitlements) | Scheduler configs (cron, pipelines, triggers) | Policy-as-code / rules tables |
| R6 Functioning Enterprise | Actual production data | Running processes/apps | Live network as operated | Real people executing roles | Actual timing/performance (logs, metrics, SLAs) | Operational outcomes (KPI attainment, actual decisions) |

---

## 2. Entry Point A — `/ea-zachman audit` Mode

Sixth mode added to `commands/ea-zachman.md` (after `classify`).

1. Locate the most recent `EA-projects/{slug}/artifacts/cross-cutting/context/zachman-diagram-*.md`. If none exists, error: "No Zachman Diagram found — run `/ea-zachman generate` first."
2. Load the checklist from `skills/zachman-framework/references/zachman-audit-checklist.md` and run all five categories with cross-artifact verification (open source artifacts per the cell-extraction-map; read registers to verify IDs; compare modification dates).
3. Render inline:
   - Per-category scorecard (✅/⚠/❓ counts per category)
   - Findings grouped High / Medium / Low, each with cell reference (R{N},C{N}), evidence, and a concrete action
   - Verdict: **Ready** (no High findings) / **Needs revision** (High findings present) / **Stale** (staleness dominates — re-generate before fixing cells)
4. Save the same report to `EA-projects/{slug}/artifacts/cross-cutting/notes/reviews/zachman-audit-{YYYY-MM-DD}.md`.
5. Offer next actions: run `/ea-zachman interview` jumping to failing cells; re-run `/ea-zachman generate` if verdict is Stale; done.

The mode defines no checks — it executes the checklist by reference.

---

## 3. Entry Point B — `/ea-grill` Routing

New block in `skills/ea-grill-skills/SKILL.md`, inserted after the **Matrix artifact grilling** block:

**Zachman Diagram grilling:** if the grill target is a Zachman Diagram (artifact id or filename matches `zachman-diagram*`):
- Run the audit checklist from `skills/zachman-framework/references/zachman-audit-checklist.md` (all five categories, cross-artifact verification) — the check definitions live in the checklist; do not restate them.
- Findings feed grill's standard output: scorecard entries, prioritised revisions, and verdict. High findings map to Inconsistent sections in the grill verdict.
- Grill's standard apply flow holds: applying fixes bumps the diagram artifact version; the review file saves per grill's convention.

Neither entry point duplicates check logic (plugin no-duplicated-logic rule).

---

## 4. Files to Create / Modify

### New files

| File | Purpose |
|---|---|
| `skills/zachman-framework/references/zachman-audit-checklist.md` | Six check categories, severity guidance, report format — single source of truth |

### Modified files

| File | Change |
|---|---|
| `skills/zachman-framework/references/zachman-cell-descriptions.md` | `Expected model:` line added to each of the 36 cell entries (from the 6×6 expected-model table) |
| `commands/ea-zachman.md` | `audit` mode added (frontmatter argument-hint + description updated; new mode section) |
| `skills/ea-grill-skills/SKILL.md` | Zachman Diagram grilling block after the matrix grilling block |
| `commands/ea-help.md` | `/ea-zachman` row updated to include `audit` |
| `CLAUDE.md` | Version 0.9.63 |
| `.claude-plugin/plugin.json` | Version 0.9.63 |
| `../.claude-plugin/marketplace.json` | Version 0.9.63 (must match plugin.json) |
| `docs/PRD.md` | v0.9.63 section |
| `README.md` | Zachman audit mention in the `/ea-zachman` row |

No new commands (count stays 55). No new ID prefixes.

---

## 5. Out of Scope

- Auto-fixing cells from within the audit (fixes go through `/ea-zachman interview` or `generate`)
- Re-generation triggered automatically by the audit
- Auditing historical diagram versions (only the most recent diagram is audited)
