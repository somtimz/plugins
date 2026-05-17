---
name: ea-constraints
description: Manage architecture constraints — capture, view, trace to artifacts, and assess impact on solution space
argument-hint: "[list|add|update|trace|impact] [--type Technology|Regulatory|Budget|Timeline|Organisational|Interoperability] [--status Active|Waived|Proposed] [--priority High|Medium|Low] [--owner name] [--phase A|B|C|D|E|F|G|H]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-constraints` command. Load the `ea-constraints-management` skill for detailed logic.

## Overview

Architecture constraints are non-negotiable restrictions on the solution space. They are distinct from requirements (which define what the architecture must achieve) and from risks (which are uncertain). Every constraint has a **Source** (policy, regulation, contract, or mandate) and an **Owner** (accountable person or role).

This command aggregates all `CST-NNN` entries from across the engagement into a single Constraints Register, supports creating or updating individual constraint records, and traces constraints to the artifacts and SBBs they bound.

**Modes:**
- `list` (default) — read the Constraints Register, render a table grouped by Type
- `add` — interactively capture a new constraint and write it to the register
- `update` — update a single field on an existing constraint (`/ea-constraints update CST-NNN <field> <value>`)
- `trace` — show which artifacts acknowledge or work around each constraint
- `impact` — assess which ADM phases, capabilities, ABBs, or work packages are bounded by a given constraint

**Filters:**
- `--type` — filter by constraint type
- `--status` — filter by status
- `--priority` — filter by priority
- `--owner` — case-insensitive partial match on Owner
- `--phase` — filter by ADM phase where identified

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, artifacts.

---

## Mode: `list` (default)

1. Read `EA-projects/{slug}/artifacts/cross-cutting/governance/constraints-register.md` (human-readable register) and `constraints-index.json`.
2. Render a summary table grouped by Type:

```
Constraints Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Active: {N}  |  Waived: {N}  |  Proposed: {N}

By Type:       Technology {N}  |  Regulatory {N}  |  Budget {N}  |  Timeline {N}  |  Organisational {N}  |  Interoperability {N}
By Priority:   High {N}  |  Medium {N}  |  Low {N}
Orphans:       {N} constraint(s) with no linked artifact
SBB Coverage:  {N} SBB(s) referencing CST-NNN  |  {N} SBB(s) with free-text only
Detail Files:  {N} CST-NNN(s) with detail files  |  {N} open issues across all constraint detail files
```

3. If any constraints have `Status: Active` but no linked artifacts, flag: "⚠️ {N} active constraint(s) with no artifact linkage — run `/ea-constraints trace` to bind them."
4. If any SBBs have free-text constraints but no `Referenced Constraints: [CST-NNN]` field, flag: "⚠️ {N} SBB(s) with untraced constraints — run `/ea-constraints trace --sbb` to link them."
5. If any detail files have open issues, flag: "⚠️ {N} open issue(s) in constraint detail files — run `/ea-detail check CST-NNN` to review."

---

## Mode: `add`

Invoked as: `/ea-constraints add`

1. Locate the existing register in `EA-projects/{slug}/artifacts/cross-cutting/governance/constraints-register.md`. If none exists, create a minimal register from the template with this constraint as the first entry.
2. Assign the next available `CST-NNN` ID (increment from the highest existing ID).
3. Prompt for each field in sequence (all required unless noted):

```
Creating new constraint — CST-{NNN}

1. Type (Technology / Regulatory / Budget / Timeline / Organisational / Interoperability):
2. Statement (the binding restriction, e.g. "Must deploy within existing AWS account"):
3. Source (POL-NNN ID preferred, or policy/regulation/contract/mandate free-text):
4. Owner (name and role — mandatory):
5. Scope (Enterprise 🔒 / Program):
6. Priority (High / Medium / Low):
7. ADM Phase (Prelim / A / B / C / D / E / F / G / H):
8. Linked Artifacts (artifact IDs, comma-separated, or press Enter) [optional]:
```

4. If `Scope = Enterprise 🔒` and `Source` is blank, warn: "⚠️ Enterprise constraints require a Source. Provide one or change Scope to Program."
5. If `Owner` is blank, re-prompt once. On second empty input: "Cancelled — Owner is mandatory for all constraints." — stop.
6. Show confirmation preview:

```
New constraint — CST-NNN: {type}
Statement: {statement}
Source: {source}  |  Owner: {owner}  |  Priority: {priority}
Scope: {scope}  |  Phase: {phase}

Add to register? (y/n)
```

7. On confirm: insert into the register, update `constraints-index.json`, set `Status: Active`, `lastModified: today`.
8. Confirm: `"CST-NNN added to Constraints Register. Use '/ea-constraints trace' to link it to artifacts."`

---

## Mode: `update`

Invoked as: `/ea-constraints update CST-NNN <field> <value>`

1. Locate the register and find the `CST-NNN` entry.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `statement` | any string |
| `type` | Technology / Regulatory / Budget / Timeline / Organisational / Interoperability |
| `source` | any string |
| `owner` | any string |
| `priority` | High / Medium / Low |
| `status` | Active / Waived / Proposed |
| `scope` | Enterprise / Program |
| `linkedArtifacts` | comma-separated artifact IDs |

3. Validation rules:
   - Setting `status` to `Waived` → `waiverJustification` must be non-empty
   - Setting `owner` to blank → warn: "Owner is mandatory. Keep existing? (y/n)"
   - Removing all `linkedArtifacts` → warn: "This constraint will have no artifact linkage. Continue? (y/n)"
4. Show proposed change: `"CST-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update `artifacts/cross-cutting/governance/constraints-register.md` and `constraints-index.json`, set `lastModified: today`.
7. Confirm: `"Updated CST-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-constraints trace [CST-NNN] [--sbb]`

**Without CST-NNN:**
1. For every `CST-NNN` in the register, scan all artifacts for acknowledgment:
   - Artifact frontmatter `relatedArtifacts` or body text references to `CST-NNN`
   - SBB files with `Referenced Constraints: [CST-NNN]`
   - Requirements Register rows with `category: Constraint` that match this constraint text
   - Detail files: `artifacts/details/CST-NNN.md` — if present, note the file and count open issues/concerns
2. Output a traceability matrix:

```
| CST-NNN | Statement | Type | Linked Artifacts | SBB References | Detail File | Untraced? |
|---|---|---|---|---|---|---|
```

3. Flag untraced constraints (no artifact, SBB, or detail file reference) in red.

**With `--sbb`:**
1. Scan all SBB files for free-text constraint language in the "Constraints / Lock-in Risk" field.
2. For each SBB with untraced constraints, suggest a `CST-NNN` match or offer to create one.

---

## Mode: `impact`

Invoked as: `/ea-constraints impact CST-NNN`

1. Load the constraint entry.
2. Scan engagement artifacts for references to `CST-NNN` or constraint text:
   - Architecture Vision — does it bound scope?
   - Business Architecture — which capabilities are affected?
   - Application/Data/Tech Architecture — which ABBs/SBBs are constrained?
   - Gap Analysis — which gaps are caused by this constraint?
   - Architecture Roadmap — which work packages must respect it?
   - Detail file: `artifacts/details/CST-NNN.md` — if present, include open issues, concerns, and impact assessment from the detail file
3. Render impact summary:

```
Impact Assessment — CST-NNN: {statement}

Affected Artifacts:   {N} ({list})
Affected ABBs:        {N} ({list or —})
Affected SBBs:        {N} ({list or —})
Affected Work Packages: {N} ({list or —})
Detail File:          {path or —}  |  Open Issues: {N}  |  Open Concerns: {N}
Constraint Type:      {type}  |  Priority: {priority}  |  Owner: {owner}

If this constraint were waived: {impact_description}
```

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No constraints found | Report "No constraints found. Capture constraints during Phase A interviews or /ea-brainstorm." |
| Constraint appears in multiple artifacts | Merge fields; prefer the most complete version; list all sources |
| Constraint with no Owner | Flag as governance gap; cannot be set to Active without Owner |
| `add`: blank Source for Enterprise scope | Warn and require source; or downgrade to Program scope |
| `update`: status Waived with no justification | Reject; prompt for waiver justification |
| Duplicate CST-NNN across artifacts | Keep both; note: "Duplicate ID — re-numbering applied: CST-NNN (from {artifact})" |
