---
name: ea-rules
description: Manage business rules — capture declarative governance statements, trace to services, policies, constraints, and motivation elements
argument-hint: "[list|add|update|trace|impact] [--directive Must|Must Not|Should|Should Not] [--source Regulatory|Internal|Contractual|Market Practice|Policy-derived] [--scope Enterprise|Program] [--status Active|Draft|Under Review|Superseded|Retired]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-rules` command. Load the `ea-business-rules-management` skill for detailed logic and the `ea-artifact-templates` skill for concept definitions.

## Overview

This command manages `BR-NNN` entries. Read `skills/ea-artifact-templates/references/concept-families/governance-and-rules-concepts.md` (**Business Rule**) for the canonical definition before prompting or validating. The command aggregates all `BR-NNN` entries into a single Business Rules Register, supports creating or updating individual rules, traces rules to linked services and motivation, and assesses the impact of a rule across the service and capability landscape.

**Modes:**
- `list` (default) — read the Business Rules Register, render a table grouped by Source
- `add` — interactively capture a new business rule and write it to the register
- `update` — update a single field on an existing rule (`/ea-rules update BR-NNN <field> <value>`)
- `trace` — show which services, policies, constraints, and motivation elements reference this rule
- `impact` — assess which services, capabilities, ABBs, and SBBs are affected by a rule

**Filters:**
- `--directive` — filter by directive
- `--source` — filter by rule source
- `--scope` — filter by scope
- `--status` — filter by status

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, `rules[]`.

---

## Mode: `list` (default)

1. Read `EA-projects/{slug}/artifacts/cross-cutting/operations/business-rules-register.md` (human-readable register).
2. Render a summary table grouped by Source:

```
Business Rules Register — {engagement name}
══════════════════════════════════════════════════════════
Total: {N}  |  Active: {N}  |  Draft: {N}  |  Under Review: {N}  |  Superseded: {N}  |  Retired: {N}

By Source:     Regulatory {N}  |  Internal {N}  |  Contractual {N}  |  Market Practice {N}  |  Policy-derived {N}
By Directive:  Must {N}  |  Must Not {N}  |  Should {N}  |  Should Not {N}
By Scope:      Enterprise 🔒 {N}  |  Program {N}
Orphans:       {N} rule(s) with no linked service, policy, constraint, or motivation element
Untraced:      {N} rule(s) with broken link references
Detail Files:  {N} BR-NNN(s) with detail files  |  {N} open issues across all rule detail files
```

3. If any rules have `Status: Active` but no linked services, processes, use cases, or enforcement, flag: "⚠️ {N} active rule(s) with no operational linkage — run `/ea-rules trace` to bind them."
4. If any rules have `Source: Policy-derived` but no linked policy, flag: "⚠️ {N} policy-derived rule(s) with no POL-NNN linkage — run `/ea-rules update BR-NNN linkedPolicies` to bind them."

---

## Mode: `add`

Invoked as: `/ea-rules add`

1. Locate the existing register in `EA-projects/{slug}/artifacts/cross-cutting/operations/business-rules-register.md`. If none exists, create a minimal register from the template with this rule as the first entry.
2. Assign the next available `BR-NNN` ID (increment from the highest existing ID in `engagement.json → rules[]`).
3. Prompt for each field in sequence (all required unless noted):

```
Creating new business rule — BR-{NNN}

1. Subject (the business entity or process governed, e.g. "Customer eligibility for senior discount"):
2. Condition (when the rule applies, e.g. "Customer age is 65 or older AND purchase is made on a weekday"):
3. Directive (Must / Must Not / Should / Should Not):
4. Outcome (the business result or action, e.g. "A 10% discount is applied"):
5. Authority (who owns or enacted the rule, e.g. "Pricing Committee", or a POL-NNN ID):
6. Source (Regulatory / Internal / Contractual / Market Practice / Policy-derived):
7. Enforcement (Manual review / Automated check / Workflow approval / Audit sample / System validation):
8. Scope (Enterprise 🔒 / Program):
9. ADM Phase (Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements):
10. Linked Business Services (SVC-NNN IDs, comma-separated, or press Enter) [optional]:
11. Linked Business Processes (PROC-NNN IDs, comma-separated, or press Enter) [optional]:
12. Linked Use Cases (UC-NNN IDs, comma-separated, or press Enter) [optional]:
13. Linked Policies (POL-NNN IDs, comma-separated, or press Enter) [optional]:
14. Linked Constraints (CST-NNN IDs, comma-separated, or press Enter) [optional]:
15. Trace to Motivation (DRV-NNN / G-NNN / OBJ-NNN / STR-NNN IDs, comma-separated, or press Enter) [optional]:
```

4. If `Scope = Enterprise 🔒` and `Authority` is blank, warn: "⚠️ Enterprise rules require an Authority. Provide one or change Scope to Program."
5. If `Directive` is invalid, re-prompt with the allowed values.
6. If `Source = Policy-derived` and no linked policy is provided, suggest: "Consider linking this rule to the authorising POL-NNN."
7. Show confirmation preview:

```
New business rule — BR-NNN: {subject}
Condition: {condition}
Directive: {directive}  |  Outcome: {outcome}
Authority: {authority}  |  Source: {source}  |  Enforcement: {enforcement}
Scope: {scope}  |  Phase: {admPhase}
Linked Services: {linkedServices or "—"}
Linked Processes: {linkedProcesses or "—"}
Linked Use Cases: {linkedUseCases or "—"}
Linked Policies: {linkedPolicies or "—"}
Linked Constraints: {linkedConstraints or "—"}
Trace to Motivation: {linkedMotivation or "—"}

Add to register? (y/n)
```

8. On confirm:
   - Append the rule to `engagement.json → rules[]`.
   - Insert the rule into the register file.
   - Set `status: Draft` if not explicitly set otherwise, `lastModified: today`.
9. Confirm: `"BR-NNN added to Business Rules Register. Use '/ea-rules trace' to verify linkages."`

---

## Mode: `update`

Invoked as: `/ea-rules update BR-NNN <field> <value>`

1. Locate the register and find the `BR-NNN` entry.
2. Valid fields for update:

| Field | Valid values |
|---|---|
| `subject` | any string |
| `condition` | any string |
| `directive` | Must / Must Not / Should / Should Not |
| `outcome` | any string |
| `authority` | any string |
| `source` | Regulatory / Internal / Contractual / Market Practice / Policy-derived |
| `enforcement` | Manual review / Automated check / Workflow approval / Audit sample / System validation |
| `scope` | Enterprise / Program |
| `status` | Active / Draft / Under Review / Superseded / Retired |
| `supersededBy` | BR-NNN |
| `admPhase` | Prelim / A / B / C-Data / C-App / D / E / F / G / H / Requirements |
| `zachmanCell` | any string |
| `linkedServices` | comma-separated SVC-NNN list |
| `linkedProcesses` | comma-separated PROC-NNN list |
| `linkedUseCases` | comma-separated UC-NNN list |
| `linkedPolicies` | comma-separated POL-NNN list |
| `linkedConstraints` | comma-separated CST-NNN list |
| `linkedMotivation` | comma-separated DRV/G/OBJ/STR IDs |

3. Validation rules:
   - Setting `status` to `Superseded` → require `supersededBy: BR-NNN`
   - Setting `status` to `Retired` → warn: "Retiring a rule may leave services without governance. Continue? (y/n)"
   - Setting `authority` to blank → warn: "Authority is mandatory. Keep existing? (y/n)"
   - Removing all `linkedServices`, `linkedProcesses`, `linkedUseCases`, `linkedPolicies`, `linkedConstraints`, and `linkedMotivation` → warn: "This rule will have no linkages. Continue? (y/n)"
   - Link values must match existing IDs in the engagement; flag unknown IDs as broken references
4. Show proposed change: `"BR-NNN: {field} — '{old}' → '{new}'"`
5. Ask: `"Apply? (y/n)"`
6. On confirm: update the register and `engagement.json`, set `lastModified: today`.
7. Confirm: `"Updated BR-NNN: {field} set to '{new_value}'."`

---

## Mode: `trace`

Invoked as: `/ea-rules trace [BR-NNN] [--services] [--policies] [--constraints] [--motivation]`

**Without BR-NNN:**
1. For every `BR-NNN` in `engagement.json → rules[]`, scan the register and related artifacts for acknowledgments:
   - Business Services Register entries where `Linked Business Rules` contains BR-NNN
   - Policies Register entries where `Linked Business Rules` contains BR-NNN
   - Constraints Register rows where the rule is cited
   - Motivation registers where the rule's `linkedMotivation` IDs exist
   - Detail files: `artifacts/details/BR-NNN.md`
2. Output a traceability matrix:

```
| BR-NNN | Subject | Directive | Linked Services | Linked Policies | Linked Constraints | Trace to Motivation | Detail File | Orphan? |
|---|---|---|---|---|---|---|---|---|
```

3. Flag orphan rules (no linked service, policy, constraint, or motivation element) in red.

**With `--services`:**
1. For each rule, list all linked SVC-NNN services and whether they are Business/Application/Technology level.
2. Flag services aligned with a rule but without formal BR-NNN linkage.

**With `--policies`:**
1. For each rule, list linked POL-NNN policies.
2. Flag `Source: Policy-derived` rules with no linked policy.

**With `--constraints`:**
1. For each rule, list linked CST-NNN constraints and the artifacts that reference them.

**With `--motivation`:**
1. For each rule, expand the `linkedMotivation` IDs into their statements and show the upstream/downstream chain.

---

## Mode: `impact`

Invoked as: `/ea-rules impact BR-NNN`

1. Load the rule entry from `engagement.json → rules[]`.
2. Resolve all linked services, capabilities, ABB, SBB, and constraints.
3. Scan engagement artifacts for references to those linked items.
4. Aggregate impacts:

```
Impact Assessment — BR-NNN: {subject}

Rule:                 {subject} ({directive}) — {status}
Condition:            {condition}
Outcome:              {outcome}
Authority:            {authority}  |  Source: {source}  |  Enforcement: {enforcement}

Linked Services:      {N} ({list or —})
Linked Policies:      {N} ({list or —})
Linked Constraints:   {N} ({list or —})
Linked Motivation:    {N} ({list or —})

Affected Services:    {N} ({deduplicated list or —})
Affected Capabilities: {N} ({list or —})
Affected ABBs:        {N} ({list or —})
Affected SBBs:        {N} ({list or —})
Affected Work Packages: {N} ({list or —})
Detail File:          {path or —}  |  Open Issues: {N}  |  Open Concerns: {N}

If this rule were retired or superseded: {aggregated_impact_description}
```

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No rules found | Report "No business rules found. Capture rules during Preliminary / Business Architecture phase interviews or /ea-brainstorm." |
| Rule appears in multiple artifacts | Merge fields; prefer the most complete version; list all sources |
| Rule with no Authority | Flag as governance gap; cannot be set to Active without Authority |
| `add`: blank Authority for Enterprise scope | Warn and require authority; or downgrade scope |
| `update`: status Retired with linked services | Warn about impact on services; offer to update linked services to remove the rule |
| `update`: status Superseded with no `supersededBy` | Reject; prompt for superseding BR-NNN |
| Duplicate BR-NNN across artifacts | Keep both; note: "Duplicate ID — re-numbering applied: BR-NNN (from {artifact})" |
| Broken link reference | Flag in `trace`; suggest `/ea-rules update BR-NNN <link-field>` |
