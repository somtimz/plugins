---
name: ea-principles
description: Manage architecture principles — capture, view, trace to artifacts, and detect violations
argument-hint: "[list|add|update|trace] [--type Business|Data|Application|Technology] [--status Active|Draft|Deprecated] [BP-NNN|DP-NNN|AP-NNN|TP-NNN <field> <value>]"
allowed-tools: [Read, Write, Bash, Glob, Grep]
---

Manage architecture principles for the active engagement. Principles are the non-negotiable rules that govern all architecture decisions — every constraint, ADR, and solution choice must be reconcilable with the active principle set.

**Modes:**
- `list` (default) — show all principles grouped by type; flag any ADR or constraint that may contradict a principle
- `add` — interactively capture a new principle (Name, Statement, Rationale, Implications); auto-assign next ID within its type
- `update {ID} <field> <value>` — update a single field on an existing principle
- `trace [ID]` — show all artifacts, decisions (ADR-NNN), and constraints (CST-NNN) that reference or are governed by this principle; flag potential violations

**Filters (list and trace):**
- `--type Business|Data|Application|Technology` — filter by principle type
- `--status Active|Draft|Deprecated` — filter by status

**ID assignment:**
- Business Principles: BP-001, BP-002, ...
- Data Principles: DP-001, DP-002, ...
- Application Principles: AP-001, AP-002, ...
- Technology Principles: TP-001, TP-002, ...

## Step 1 — Resolve Active Engagement

Check `CLAUDE.md` or `engagement.json` context. If no engagement is open, scan `EA-projects/*/engagement.json` for the most recently modified active engagement. Ask the user to confirm if ambiguous.

## Step 2 — Locate or Create Principles Artifact

Look for `artifacts/preliminary/architecture-principles.md` in the active engagement folder.

- If the file exists: proceed with the requested mode.
- If the file does not exist and mode is `list`: display "No Architecture Principles artifact found. Run `/ea-artifact create architecture-principles` to create it, or use `/ea-principles add` to start capturing principles now."
- If the file does not exist and mode is `add`: offer to create the artifact scaffold before adding the first principle. Use `templates/principles-register.md` as the scaffold.

## Mode: `list` (default)

Read `artifacts/preliminary/architecture-principles.md`. Render a summary view:

```
## Architecture Principles — {engagement_name}

| Type       | Active | Draft | Deprecated | Total |
|---|---|---|---|---|
| Business   | N      | N     | N          | N     |
| Data       | N      | N     | N          | N     |
| Application| N      | N     | N          | N     |
| Technology | N      | N     | N          | N     |
| **Total**  | N      | N     | N          | N     |

### Business Principles
| ID     | Name | Status | Statement (first 80 chars) | Linked Constraints | Linked ADRs |
|---|---|---|---|---|---|
| BP-001 | ...  | Active | ...                        | CST-001            | ADR-002     |

### Data Principles
...

### Application Principles
...

### Technology Principles
...
```

After the table, scan `artifacts/cross-cutting/` for constraint and ADR register files. Check each constraint's `Source` field and each ADR's body for any principle ID reference. Flag any principle with zero references as "⚠️ Unreferenced — no constraints or ADRs cite this principle yet."

Load `skills/ea-principles-management/SKILL.md` for violation detection logic (Section 4).

## Mode: `add`

1. Prompt: "Which type of principle? (1) Business  (2) Data  (3) Application  (4) Technology"
2. Assign next sequential ID for that type by scanning the existing entries (e.g. if BP-001 and BP-002 exist, assign BP-003).
3. Prompt for each field — show an example of a good answer beside each prompt:
   - **Name** — short label, 2–5 words (e.g. "Technology Independence")
   - **Statement** — the normative rule in one sentence, starting with a modal verb (e.g. "Technology choices must not create dependency on a single vendor.")
   - **Rationale** — why this principle exists, 1–3 sentences
   - **Implications** — what following this principle requires or prohibits in practice (bullet points)
   - **Status** — Active / Draft / Deprecated (default: Active)
   - **Source Policy** — POL-NNN if this principle operationalises a policy (optional; press Enter to skip)
4. Show a preview of the formatted principle block. Ask "Apply? (y/edit/cancel)"
5. On confirm: append the principle block to the correct type section in `artifacts/preliminary/architecture-principles.md`. Update `lastModified` in frontmatter.
6. Offer: "Would you like to add a corresponding constraint (CST-NNN) to enforce this principle in the solution? Run `/ea-constraints add` when ready."

## Mode: `update {ID} <field> <value>`

1. Locate the principle by ID (e.g. `BP-002`) in `artifacts/preliminary/architecture-principles.md`.
2. Validate the field name against the allowed set: `name`, `statement`, `rationale`, `implications`, `status`, `sourcePolicy`.
3. Show the current value and the proposed new value. Ask "Apply? (y/n)"
4. On confirm: update the field in place. Update `lastModified` in frontmatter.
5. If `status` is being set to `Deprecated`: warn "Deprecating {ID} — any constraints or ADRs citing this principle will show a stale reference. Run `/ea-principles trace {ID}` to review downstream impact."

## Mode: `trace [ID]`

If an ID is provided, trace that specific principle. If no ID is given, trace all principles and produce a full linkage report.

For each principle being traced:

1. Grep all files under `artifacts/` for the principle ID (e.g. `BP-001`).
2. Report results in three categories:
   - **Constraints sourced from this principle** — CST-NNN entries with `Source` matching this ID or name
   - **Decisions that cite this principle** — ADR-NNN files referencing the ID in body or metadata
   - **Artifacts that reference this principle** — phase artifact files mentioning the ID
3. Load `skills/ea-principles-management/SKILL.md` Section 4 (Violation Detection) to scan completed ADRs for decisions that may contradict the principle's Statement. Flag with "⚠️ Possible violation — review ADR-NNN."
4. If no references found: "⚠️ {ID} has no constraints, ADRs, or artifact references. Consider adding an enforcing constraint via `/ea-constraints add`."

## Edge Cases

| Scenario | Handling |
|---|---|
| Duplicate principle name | Warn: "A principle named '{name}' may already exist ({ID}). Add anyway? (y/n)" |
| Deprecated principle cited in active ADR | Flag in `trace` output as stale reference |
| Principles artifact missing | Offer to scaffold from `templates/principles-register.md`; do not fail silently |
| No engagement open | Display: "No active engagement. Run `/ea-open` to open one." |
| --type filter with no matching principles | Display: "No {type} principles found. Use `/ea-principles add --type {type}` to create the first one." |
