---
name: ea-actions
description: Generate and manage the Stakeholder Action Plan — a consolidated per-approver action view seeded from the SAoW and Target State Declaration, suitable for governance forums and ARB
argument-hint: "[generate|view|update <approver> <row#> <field> <value>|status]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-actions` command.

## Overview

The Stakeholder Action Plan provides a consolidated, per-approver view of what each stakeholder with approval authority must do to progress this engagement. It is seeded from the SAoW acceptance criteria and sign-off table, enriched with success criteria from the Target State Declaration, and suitable for distribution to a governance forum or ARB.

**Modes:**
- `generate` — seed from SAoW + Target State Declaration; show draft for confirmation before writing
- `view` — display the current Stakeholder Action Plan
- `update <approver> <row#> <field> <value>` — update a single action row
- `status` — summary of pending, complete, and overdue actions

---

## Step 1 — Resolve Active Engagement

> Resolve the active engagement per `skills/ea-engagement-lifecycle/references/engagement-resolution.md`.

---

## Mode: `generate`

Invoked as: `/ea-actions generate`

### Pre-check

Check whether `artifacts/cross-cutting/governance/stakeholder-action-plan.md` already exists.

- If it exists: "Stakeholder Action Plan already exists. Regenerate (replaces content) or view existing? (regenerate/view)" — stop unless user selects regenerate.

### Data Collection

**Step A — Read SAoW:**

Check for `artifacts/phase-a/statement-of-architecture-work.md` in the engagement folder.

- If not found: "No SAoW found. Create one via `/ea-interview start phase A` before generating the action plan." Stop.
- If found, read and extract:
  - §6 Acceptance Criteria table rows: `Deliverable | Acceptance Criteria | Accepted By`
  - §7 Sign-off table rows: `Role | Name`
  - §4 Schedule table rows: `Milestone | Description | Target Date | Owner`

Flag if §6 or §7 are empty/placeholder-only: "⚠️ SAoW §6 or §7 is unpopulated — the action plan will be a stub. Continue? (y/n)"

**Step B — Read Target State Declaration:**

Check for `artifacts/phase-a/target-state-declaration.md`.

- If found: extract §3 Success Criteria table rows (`Criterion | Measurable Condition | Linked Deliverable | Accepted By`) and §1 Overall Target State summary.
- If not found: warn "No Target State Declaration found — success criteria will come from the SAoW only. Run `/ea-target new` to create one." Continue.

**Step C — Build approver map:**

1. Extract all unique names from SAoW §6 `Accepted By` column.
2. Match each name against SAoW §7 `Name` column to find their `Role`.
3. For names in §6 not present in §7: include them with role `⚠️ Role not in SAoW §7 — verify`.
4. Merge Target State Declaration §3 `Accepted By` values into the approver map — deduplicate by name.

**Step D — Build per-approver action rows:**

For each approver:
1. Collect all SAoW §6 rows where `Accepted By` = this approver.
2. Collect all Target State §3 rows where `Accepted By` = this approver (skip duplicates already from SAoW).
3. For each row, find a matching milestone in SAoW §4 `Milestone` text — use `Target Date` as `Due Date`. If no match: leave `Due Date` as `{{due_date}}`.
4. Set all statuses to `Pending`.

**Step E — Build target state summary:**

- If Target State Declaration exists: use §1 Overall Target State text.
- Otherwise: use `engagement.json → direction.vision` if populated, else `{{target_state_summary}}`.

### Draft and Confirm

Present the full draft to the user:

```
Stakeholder Action Plan — {engagement name}
══════════════════════════════════════════════
Approvers: {N}
Total actions: {N}

{Per-approver summary table}

---
Per-Approver Detail:

{For each approver: name, role, action table}

---
Governance Schedule:
{SAoW §4 milestones relevant to sign-off}

Write this action plan? (y/n/edit)
```

If user selects `edit`: prompt for which approver or section to modify before writing.

### Writing the Artifact

1. Substitute all collected data into `templates/cross-cutting/stakeholder-action-plan.md`.
2. Populate `engagement_name`, `organisation` from `engagement.json`.
3. Compute action summary counts (all Pending at generation time).
4. Set `lastModified` to today.
5. Write to `EA-projects/{slug}/artifacts/cross-cutting/governance/stakeholder-action-plan.md`.
6. Register in `engagement.json → artifacts[]`:
```json
{
  "id": "stakeholder-action-plan",
  "name": "Stakeholder Action Plan",
  "phase": "All",
  "file": "artifacts/cross-cutting/governance/stakeholder-action-plan.md",
  "reviewFile": "artifacts/cross-cutting/governance/stakeholder-action-plan.review.md",
  "status": "Draft",
  "createdAt": "{ISO 8601 timestamp}",
  "lastModified": "{ISO 8601 timestamp}",
  "reviewStatus": "Not Reviewed"
}
```
7. Update `engagement.json → lastModified`.
8. Confirm: "Stakeholder Action Plan written to `artifacts/cross-cutting/governance/stakeholder-action-plan.md` — {N} approvers, {N} actions. Use `/ea-actions status` for a summary."

---

## Mode: `view`

Invoked as: `/ea-actions view`

1. Read `EA-projects/{slug}/artifacts/cross-cutting/governance/stakeholder-action-plan.md`.
2. If the file does not exist: "No Stakeholder Action Plan found. Run `/ea-actions generate` to create one."
3. Display the full artifact content inline.

---

## Mode: `update`

Invoked as: `/ea-actions update <approver> <row#> <field> <value>`

`<approver>` — partial name match (case-insensitive) against the H3 section headers.
`<row#>` — 1-based row number in that approver's action table.
`<field>` — one of: `action`, `deliverable`, `acceptance-criteria`, `due-date`, `status`
`<value>` — new value. For `status`: must be one of `Pending | In Review | Approved | Deferred`.

1. Read the artifact.
2. Find the approver section (H3 matching `<approver>`). If ambiguous (multiple matches): list matches and ask user to be more specific.
3. Find row `<row#>` in that approver's action table.
4. Show: `"Row {N} — {field}: '{current}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update the cell, update `lastModified`, write back.
7. Recompute action summary counts in the Executive Summary table and update them.

---

## Mode: `status`

Invoked as: `/ea-actions status`

1. Read `EA-projects/{slug}/artifacts/cross-cutting/governance/stakeholder-action-plan.md`.
2. If not found: "No Stakeholder Action Plan found. Run `/ea-actions generate` to create one."
3. Parse all action table rows across all per-approver sections.
4. Compute counts: Total | Pending | In Review | Approved | Deferred | Overdue (Due Date < today and status ≠ Approved).
5. Output:

```
Stakeholder Action Plan — {engagement name}
══════════════════════════════════════════════
Total: {N}  |  Pending: {N}  |  In Review: {N}  |  Approved: {N}  |  Deferred: {N}
Overdue: {N}

| Approver | Role | Pending | Approved | Overdue | Next Due |
|---|---|---|---|---|---|
| {name} | {role} | {N} | {N} | {N} | {date or —} |
```

6. Flag overdue items: "⚠️ {N} overdue action(s) — update status with `/ea-actions update <approver> <row#> status <value>`."

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No SAoW found | Abort with message directing to `/ea-interview start phase A` |
| SAoW §6/§7 empty | Warn; offer to generate stub or stop |
| Approver in §6 not in §7 | Include with flagged role; warn |
| Target State Declaration absent | Continue without it; warn |
| Artifact already exists on `generate` | Ask: regenerate or view |
| Ambiguous approver name in `update` | List matches; ask user to be specific |
| `status` value not in allowed set | List valid values and stop |
