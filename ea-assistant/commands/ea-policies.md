---
name: ea-policies
description: Manage architecture policies — capture governance documents, trace to constraints, and assess policy impact
argument-hint: "[list|add|update|trace|impact] [--type Security|Procurement|Data Governance|Technology|Compliance|HR|Operational] [--scope Enterprise|Divisional|Geographic] [--status Draft|Enacted|Under Review|Superseded|Retired]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-policies` command. Load the `ea-policies-management` skill for detailed logic.

## Overview

Architecture policies are **formal governance documents or mandates** enacted by an authority (board, regulator, CISO, governance body) that create binding boundaries on architecture and implementation choices. Policies are the **authorising source** for constraints — they do not directly restrict solution space, but they **generate** constraints (CST-NNN) that do.

Policies are distinct from:
- **Principles** — internal normative decision filters, not external mandates
- **Constraints** — binding restrictions *derived from* policies, not the policies themselves
- **Requirements** — verifiable outcomes with measurable targets

This command aggregates all `POL-NNN` entries into a single Policies Register, supports creating or updating individual policy records, traces policies to the constraints they generate, and assesses which capabilities, ABBs, and work packages are ultimately bounded by a policy's derived constraints.

**Modes:**
- `list` (default) — read the Policies Register, render a table grouped by Type
- `add` — interactively capture a new policy and write it to the register
- `update` — update a single field on an existing policy (`/ea-policies update POL-NNN <field> <value>`)
- `trace` — show which constraints, principles, and SBBs reference this policy
- `impact` — assess which capabilities, ABBs, and work packages are bounded by constraints sourced from this policy

**Filters:**
- `--type` — filter by policy type
- `--scope` — filter by scope of authority
- `--status` — filter by status

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, artifacts.

---

## Mode: `list` (default)

1. Read `EA-projects/{slug}/artifacts/policies-register-{YYYY-MM-DD}.md` (human-readable register).
2. Render a summary table grouped by Type:

```
Policies Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Enacted: {N}  |  Under Review: {N}  |  Draft: {N}  |  Retired: {N}

By Type:       Security {N}  |  Procurement {N}  |  Data Governance {N}  |  Technology {N}  |  Compliance {N}  |  HR {N}  |  Operational {N}
By Scope:      Enterprise 🔒 {N}  |  Divisional {N}  |  Geographic {N}
Orphans:       {N} policy(ies) with no linked constraint
Stale:         {N} policy(ies) with Review Cycle past due
Detail Files:  {N} POL-NNN(s) with detail files  |  {N} open issues across all policy detail files
```

3. If any policies have `Status: Enacted` but no linked constraints, flag: "⚠️ {N} enacted policy(ies) with no linked constraints — run `/ea-policies trace` to bind them."
4. If any policies have `Review Cycle` past due, flag: "⚠️ {N} policy(ies) with overdue review — may invalidate linked constraints. Run `/ea-policies trace` to assess impact."

---

## Mode: `add`

Invoked as: `/ea-policies add`

1. Locate the existing register in `EA-projects/{slug}/artifacts/policies-register-*.md`. If none exists, create a minimal register from the template with this policy as the first entry.
2. Assign the next available `POL-NNN` ID (increment from the highest existing ID).
3. Prompt for each field in sequence (all required unless noted):

```
Creating new policy — POL-{NNN}

1. Title (e.g. "Cloud-First Procurement Policy v4.2"):
2. Type (Security / Procurement / Data Governance / Technology / Compliance / HR / Operational):
3. Issuing Authority (who enacted it, e.g. "CISO", "Procurement Board", "Legal"):
4. Effective Date (YYYY-MM-DD):
5. Review Cycle / Expiry (YYYY-MM-DD, or "Annual", "Biennial"):
6. Scope of Authority (Enterprise 🔒 / Divisional / Geographic):
7. Document Reference / URL (link to policy document, or press Enter) [optional]:
8. Statement (summary of what the policy mandates):
9. Linked Constraints (CST-NNN IDs, comma-separated, or press Enter) [optional]:
```

4. If `Scope = Enterprise 🔒` and `Issuing Authority` is blank, warn: "⚠️ Enterprise policies require an Issuing Authority. Provide one or change Scope to Divisional."
5. If `Issuing Authority` is blank, re-prompt once. On second empty input: "Cancelled — Issuing Authority is mandatory for all policies." — stop.
6. Show confirmation preview:

```
New policy — POL-NNN: {title}
Type: {type}  |  Authority: {issuingAuthority}  |  Effective: {effectiveDate}
Scope: {scope}  |  Review: {reviewCycle}
Linked Constraints: {linkedConstraints or "—"}

Add to register? (y/n)
```

7. On confirm: insert into the register, update `engagement.json` `policies[]`, set `Status: Enacted`, `lastModified: today`.
8. Confirm: `"POL-NNN added to Policies Register. Use '/ea-policies trace' to link it to constraints."`

---

## Mode: `update`

Invoked as: `/ea-policies update POL-NNN <field> <value>`

1. Locate the register and find the `POL-NNN` entry.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `title` | any string |
| `type` | Security / Procurement / Data Governance / Technology / Compliance / HR / Operational |
| `issuingAuthority` | any string |
| `effectiveDate` | YYYY-MM-DD |
| `reviewCycle` | YYYY-MM-DD, Annual, Biennial, or free-text |
| `scope` | Enterprise / Divisional / Geographic |
| `status` | Draft / Enacted / Under Review / Superseded / Retired |
| `documentReference` | any URL or string |
| `statement` | any string |
| `linkedConstraints` | comma-separated CST-NNN list |
| `linkedPrinciples` | comma-separated principle names or IDs |

3. Validation rules:
   - Setting `status` to `Superseded` → require `supersededBy: POL-NNN`
   - Setting `status` to `Retired` → warn: "Retiring a policy may invalidate linked constraints. Continue? (y/n)"
   - Setting `issuingAuthority` to blank → warn: "Issuing Authority is mandatory. Keep existing? (y/n)"
   - Removing all `linkedConstraints` → warn: "This policy will have no constraint linkage. Continue? (y/n)"
4. Show proposed change: `"POL-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update the register and `engagement.json`, set `lastModified: today`.
7. Confirm: `"Updated POL-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-policies trace [POL-NNN] [--constraints] [--principles] [--sbb]`

**Without POL-NNN:**
1. For every `POL-NNN` in the register, scan all artifacts for acknowledgment:
   - Constraints Register rows where `Source` matches `POL-NNN` or the policy title
   - Architecture Principles with a `Source Policy` field referencing `POL-NNN`
   - SBB files with `Referenced Constraints: [CST-NNN]` where the CST-NNN is linked to this policy
   - Detail files: `artifacts/details/POL-NNN.md` — if present, note the file and count open issues/concerns
2. Output a traceability matrix:

```
| POL-NNN | Title | Type | Linked Constraints | Principles | SBB References | Detail File | Untraced? |
|---|---|---|---|---|---|---|---|
```

3. Flag untraced policies (no linked constraint, principle, or SBB reference) in red.

**With `--constraints`:**
1. For each policy, list all CST-NNN constraints that trace to it.
2. Flag constraints whose Source is free-text and matches the policy title but is not formally linked.

**With `--principles`:**
1. Scan all principles for `Source Policy` or free-text references to policy names.
2. Flag principles aligned with a policy but without formal POL-NNN linkage.

**With `--sbb`:**
1. For each policy, trace through linked CST-NNN constraints to find affected SBBs.

---

## Mode: `impact`

Invoked as: `/ea-policies impact POL-NNN`

1. Load the policy entry.
2. Resolve all linked CST-NNN constraints.
3. For each linked constraint, scan engagement artifacts for references (same as `/ea-constraints impact CST-NNN`).
4. Aggregate impacts across all linked constraints:

```
Impact Assessment — POL-NNN: {title}

Policy:               {title} ({type}) — {status}
Authority:            {issuingAuthority}  |  Effective: {effectiveDate}  |  Review: {reviewCycle}

Linked Constraints:   {N} ({list})

Affected Artifacts:   {N} ({deduplicated list})
Affected Capabilities: {N} ({list or —})
Affected ABBs:        {N} ({list or —})
Affected SBBs:        {N} ({list or —})
Affected Work Packages: {N} ({list or —})
Detail File:          {path or —}  |  Open Issues: {N}  |  Open Concerns: {N}

If this policy were retired or superseded: {aggregated_impact_description}
```

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No policies found | Report "No policies found. Capture policies during Preliminary phase interviews or /ea-brainstorm." |
| Policy appears in multiple artifacts | Merge fields; prefer the most complete version; list all sources |
| Policy with no Issuing Authority | Flag as governance gap; cannot be set to Enacted without Issuing Authority |
| `add`: blank Issuing Authority for Enterprise scope | Warn and require authority; or downgrade scope |
| `update`: status Retired with linked constraints | Warn about impact on constraints; offer to waive linked CST-NNN entries |
| `update`: status Superseded with no `supersededBy` | Reject; prompt for superseding POL-NNN |
| Duplicate POL-NNN across artifacts | Keep both; note: "Duplicate ID — re-numbering applied: POL-NNN (from {artifact})" |
| Stale policy (Review Cycle past due) | Flag in `list` mode; suggest `/ea-policies update POL-NNN status Under Review` |
