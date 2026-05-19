# Design: EA Target State Declaration + Stakeholder Action Plan

**Date:** 2026-05-18
**Plugin:** ea-assistant
**Status:** Approved

---

## Problem

There is no first-class concept of "target state" in an EA engagement. The desired end state is scattered across goals (G-NNN), objectives (OBJ-NNN), the Architecture Vision, and the SAoW acceptance criteria. There is also no artifact that surfaces what each stakeholder with approval authority needs to do — approvers must dig through the SAoW to find their obligations.

---

## Solution

Two new commands and two new artifact templates:

1. **`/ea-target`** — creates and manages a Target State Declaration artifact in `phase-a/`
2. **`/ea-actions`** — generates and manages a Stakeholder Action Plan artifact in `cross-cutting/governance/`

---

## Artifact: Target State Declaration

**Path:** `artifacts/phase-a/target-state-declaration.md`
**Template:** `templates/target-state-declaration.md`
**Artifact ID:** `target-state-declaration`
**Phase:** A
**Taxonomy:** domain=Cross-cutting, category=Strategy, audience=Executive, layer=Motivation

### Sections

1. Executive Summary
2. Target State Summary — overall end-state statement (what will be true when this engagement succeeds?)
3. Per-Domain Target States — one subsection per domain in `engagement.json → architectureDomains` (Business / Data / Application / Technology)
4. Success Criteria — table: `| Criterion | Measure | Linked Deliverable | Accepted By |` — pre-populated from SAoW §6 if SAoW exists
5. Key Assumptions — list
6. Traceability — table linking to G-NNN, OBJ-NNN, STR-NNN from `engagement.json → direction`
7. Appendix A3 — Decision Log (T3-A3)
8. Appendix A4 — Stakeholder Concerns & Objections
9. Appendix A5 — Related Architecture Decisions

### Compliance

- T3-A3 required
- T3-A4 required
- T3-A5-ADR required

---

## Command: `/ea-target`

**File:** `commands/ea-target.md`

### Modes

| Mode | Invocation | Description |
|---|---|---|
| `new` | `/ea-target new` | Interview-driven creation of the Target State Declaration |
| `view` | `/ea-target view` | Display the current Target State Declaration |
| `update` | `/ea-target update <section> <value>` | Update a specific field |

### `new` Interview Flow

1. Overall target state summary (1–3 sentences)
2. Per-domain target state for each domain in `architectureDomains`
3. Success criteria — if SAoW exists, pre-populate from SAoW §6 `Acceptance Criteria` + `Accepted By` columns and ask user to confirm/add; otherwise prompt directly
4. Key assumptions
5. Linked goals — select from existing G-NNN (optional)

On confirm: write artifact, register in `engagement.json → artifacts[]`, set `lastModified`.

### Edge Cases

- No SAoW exists → skip pre-population of success criteria; prompt directly
- Target State Declaration already exists → ask: "A Target State Declaration already exists. Overwrite, or open for editing? (overwrite/edit)"
- No goals in direction → skip traceability section; warn: "No goals found — add them via `/ea-goals add` and update traceability with `/ea-target update`"

---

## Artifact: Stakeholder Action Plan

**Path:** `artifacts/cross-cutting/governance/stakeholder-action-plan.md`
**Template:** `templates/stakeholder-action-plan.md`
**Artifact ID:** `stakeholder-action-plan`
**Phase:** All (cross-cutting)
**Taxonomy:** domain=Cross-cutting, category=Governance, audience=Governance, layer=Governance

### Sections

1. Executive Summary — engagement name, target state one-liner, total pending/complete/overdue counts
2. Approval Authority Register — summary table: `| Name | Role | Organisation | Pending | Complete | Next Due |`
3. Per-Approver Action Detail — one H3 section per approver:
   - Name, role, organisation
   - Action table: `| # | Action | Deliverable | Acceptance Criteria | Due Date | Status |`
   - Status values: `Pending | In Review | Approved | Deferred`
4. Governance Schedule — `| Gate | Description | Required Approvers | Target Date | Status |`
5. Working Notes — Comments, Critiques, Outstanding Tasks (standard block)

No new ID prefix — actions are numbered rows within the artifact, not cross-referenced from other artifacts.

---

## Command: `/ea-actions`

**File:** `commands/ea-actions.md`

### Modes

| Mode | Invocation | Description |
|---|---|---|
| `generate` | `/ea-actions generate` | Seed action plan from SAoW + Target State Declaration; show draft for confirmation before writing |
| `view` | `/ea-actions view` | Display the current Stakeholder Action Plan |
| `update` | `/ea-actions update <approver> <row#> <field> <value>` | Edit a single action row |
| `status` | `/ea-actions status` | Summary: N approvers, N pending / N complete / N overdue |

### `generate` Logic

1. Resolve active engagement; read `engagement.json`
2. Read SAoW at `artifacts/phase-a/statement-of-architecture-work.md`:
   - §6 acceptance criteria table (`Deliverable | Acceptance Criteria | Accepted By`)
   - §7 sign-off table (`Role | Name`)
3. Read Target State Declaration at `artifacts/phase-a/target-state-declaration.md` if present:
   - §4 success criteria table — merge with SAoW acceptance criteria, deduplicate by deliverable
4. Read `engagement.json → direction` for target state context (goals, strategies)
5. Group all actions by approver name (match SAoW §6 `Accepted By` to SAoW §7 `Name`)
6. Set all statuses to `Pending`; populate `Due Date` from SAoW §4 schedule where a matching milestone exists
7. Present full draft to user; ask: "Write this action plan? (y/n/edit)"
8. On confirm: write artifact, register in `engagement.json → artifacts[]`

### Edge Cases

- No SAoW exists → abort with: "No SAoW found. Create one via `/ea-interview start phase A` before generating the action plan."
- SAoW §6/§7 unpopulated → warn and generate stub with placeholder rows
- Action plan already exists → ask: "Stakeholder Action Plan already exists. Regenerate (replaces content) or view existing? (regenerate/view)"
- Approver in §6 `Accepted By` not in §7 sign-off table → include them anyway; flag: "⚠️ [Name] appears in acceptance criteria but not in sign-off table — verify role"

---

## Files to Create

| File | Action |
|---|---|
| `commands/ea-target.md` | Create |
| `commands/ea-actions.md` | Create |
| `templates/target-state-declaration.md` | Create |
| `templates/stakeholder-action-plan.md` | Create |

## Files to Modify

| File | Change |
|---|---|
| `commands/ea-help.md` | Add `/ea-target` and `/ea-actions` to commands table |
| `CLAUDE.md` | Add to Command Reference section |
| `skills/ea-artifact-templates/SKILL.md` | Register new artifact IDs and template paths |

## Out of Scope

- No `engagement.json` schema changes
- No changes to existing templates (SAoW, stakeholder map)
- No new ID prefix
- Version bump deferred to release commit
