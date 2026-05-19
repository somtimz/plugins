---
name: ea-target
description: Create and manage the Target State Declaration — captures per-domain target states, success criteria, and traceability to goals and objectives
argument-hint: "[new|view|update <section> <value>]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-target` command.

## Overview

The Target State Declaration is the engagement's authoritative statement of the desired end state — what will be true when this architecture work succeeds. It translates the Architecture Vision into a concrete, domain-by-domain description of the future state and defines the success criteria by which the engagement will be judged complete.

The Target State Declaration is defined by and must be consistent with:
1. The Statement of Architecture Work (SAoW) — scope, deliverables, and acceptance criteria
2. The Architecture Vision — strategic direction and justification

It feeds the Stakeholder Action Plan (`/ea-actions`) which surfaces per-approver actions for governance forums.

**Modes:**
- `new` (default if no artifact exists) — interview-driven creation
- `view` — display the current Target State Declaration
- `update <section> <value>` — update a specific section

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, organisation, sponsor, currentPhase, architectureDomains, direction (goals, objectives, strategies).

---

## Mode: `new`

Invoked as: `/ea-target new` or `/ea-target` when no Target State Declaration artifact exists.

### Pre-check

Check whether `artifacts/phase-a/target-state-declaration.md` already exists in the engagement folder.

- If it exists: "A Target State Declaration already exists. Open it for editing (`/ea-target view`) or overwrite it? (edit/overwrite)" — stop unless user selects overwrite.
- If SAoW exists at `artifacts/phase-a/statement-of-architecture-work.md`: read §6 acceptance criteria table — extract all rows into a buffer for use in Step 4.

### Interview

Conduct the following questions in sequence. Apply standard interview shortcuts (s = skip, n/a = not applicable, opt-out, a: = decision log). Use the template at `templates/target-state-declaration.md` for placeholder keys.

**Q1 — Overall target state:**
```
What will be true when this engagement succeeds?
(1–3 sentences — a testable description of the desired future state, not an aspiration)
```

**Q2 — Per-domain target states** (one question per domain in `engagement.json → architectureDomains`; skip domains not in scope):

For each domain in [Business, Data, Application, Technology]:
```
In the {domain} domain, what does the target state look like?
(Describe the future architecture — what will exist, what will be different, what will be possible)
```

If a domain is not in `architectureDomains`, pre-fill with `➖ Not applicable`.

**Q3 — Success criteria:**

If SAoW acceptance criteria were found in the pre-check buffer:
```
I found {N} acceptance criteria in the SAoW (§6). Here they are:

{table of SAoW acceptance criteria rows}

Do these cover all success criteria for this engagement, or are there additional architectural success criteria to add?
(Enter additional criteria one at a time, or press Enter to accept the SAoW criteria as-is)
```

If no SAoW exists:
```
What specific conditions must be met for this engagement to be considered complete?
(Enter each criterion as: [Condition] | [Measurable test] | [Deliverable] | [Accepted By])
```

Collect all criteria. For each criterion without an `Accepted By` value, prompt: "Who has authority to confirm this criterion is met?"

**Q4 — Key assumptions:**
```
What key assumptions does this target state depend on?
(List each assumption — flag any that could invalidate the target state if proven false)
```

**Q5 — Traceability:**
```
Which goals (G-NNN) does this target state realise?
```
Display available G-NNN entries from `engagement.json → direction.goals[]`. Allow multi-select.

If no goals exist: "No goals found — you can add goals later via `/ea-goals add` and link them with `/ea-target update traceability`."

### Writing the artifact

1. Substitute all collected answers into `templates/target-state-declaration.md`.
2. Pre-populate `engagement_name`, `organisation`, `sponsor` from `engagement.json`.
3. Set `lastModified` to today's date.
4. Write to `EA-projects/{slug}/artifacts/phase-a/target-state-declaration.md`.
5. Register in `engagement.json → artifacts[]`:
```json
{
  "id": "target-state-declaration",
  "name": "Target State Declaration",
  "phase": "A",
  "file": "artifacts/phase-a/target-state-declaration.md",
  "reviewFile": "artifacts/phase-a/target-state-declaration.review.md",
  "status": "Draft",
  "createdAt": "{ISO 8601 timestamp}",
  "lastModified": "{ISO 8601 timestamp}",
  "reviewStatus": "Not Reviewed"
}
```
6. Update `engagement.json → lastModified`.
7. Confirm: "Target State Declaration written to `artifacts/phase-a/target-state-declaration.md`. Use `/ea-actions generate` to produce a Stakeholder Action Plan from this artifact."

---

## Mode: `view`

Invoked as: `/ea-target view`

1. Read `EA-projects/{slug}/artifacts/phase-a/target-state-declaration.md`.
2. If the file does not exist: "No Target State Declaration found. Run `/ea-target new` to create one."
3. Display the full artifact content inline.

---

## Mode: `update`

Invoked as: `/ea-target update <section> <value>`

Valid section names and what they update:

| Section name | Updates |
|---|---|
| `summary` | §1 Overall Target State (`{{overall_target_state}}`) |
| `business` | §2 Business Domain (`{{target_state_business}}`) |
| `data` | §2 Data Domain (`{{target_state_data}}`) |
| `application` | §2 Application Domain (`{{target_state_application}}`) |
| `technology` | §2 Technology Domain (`{{target_state_technology}}`) |
| `assumptions` | §4 Key Assumptions (replace full list) |
| `traceability` | §5 Traceability table |

1. Read the current artifact.
2. Show the current value of the named section.
3. Ask: "Replace with: `{value}`? (y/n)"
4. On confirm: replace the placeholder/current value, update `lastModified`, write back.

---

## Edge Cases

| Scenario | Handling |
|---|---|
| Artifact already exists on `new` | Prompt: edit or overwrite |
| No SAoW found | Skip SAoW pre-population; prompt for success criteria directly |
| SAoW §6 is empty/placeholder | Warn: "SAoW §6 Acceptance Criteria is unpopulated — fill it in first via `/ea-interview` or enter success criteria directly" |
| No goals in direction | Skip traceability Q5; note in artifact; suggest `/ea-goals add` |
| Domain not in architectureDomains | Pre-fill that domain section with `➖ Not applicable` |
| Unknown section name in `update` | List valid section names and stop |
