---
name: ea-sbbs
description: Generate or view the Solution Building Block (SBB) Register. Scan all artifacts for SBB-NNN entries, aggregate them into a consolidated register, and surface vendor-first selections or unlinked SBBs.
argument-hint: "[generate | status | new | update SBB-NNN <field> <value>] [--vendor <vendor>] [--phase D|E|F] [--abb ABB-NNN]"
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

You are executing the `/ea-sbbs` command.

## Overview

Solution Building Blocks (SBBs) are concrete, vendor-specific implementations of Architecture Building Blocks. This command aggregates all SBB-NNN entries from across the engagement into a single register, surfaces vendor-first selections (SBBs without an ABB), and tracks lock-in constraints.

**Modes:**
- `generate` (default) — scan all artifacts for SBB tables and write `sbb-register.md`
- `status` — inline summary of SBBs without writing a file
- `new` — create a new SBB record interactively
- `update SBB-NNN <field> <value>` — update a single field on an existing SBB

**Filters:**
- `--vendor` — filter by vendor name (partial match)
- `--phase` — filter by ADM phase where SBB was defined
- `--abb ABB-NNN` — filter SBBs that implement a specific ABB

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, artifacts.

---

## Mode: `generate` (default)

### Step 2 — Scan for SBB Entries

Scan all `.md` files in `EA-projects/{slug}/artifacts/` for SBB tables:

| Artifact Pattern | Section to Scan | Row Format |
|---|---|---|
| `technology-architecture*.md` | Solution Building Blocks Register | `SBB-NNN | Name | Implements (ABB-NNN) | Vendor / Source | Version | Referenced Constraints: [CST-NNN] | Constraints / Lock-in Risk` |
| `application-architecture*.md` | SBB Register or implementation sections | Same |
| `gap-analysis*.md` | SBB comparison tables | Same |

For each SBB row found:
- Extract: ID, Name, Implements (ABB-NNN), Vendor/Source, Version, Constraints/Lock-in Risk
- Record source artifact filename and phase
- Merge duplicates (most complete version wins)

### Step 3 — Detect Orphans and Anti-patterns

For each SBB-NNN:
- **Orphan (Critical):** No `Implements` ABB-NNN — vendor-first selection; flag as anti-pattern
- **Lock-in Risk:** Constraints field contains strong language ("proprietary API", "egress costs", "custom schema", "no migration path")
- **Version Drift:** Same SBB name with different versions in different artifacts

### Step 4 — Compile SBB Register

Using the SBB register template (`templates/sbb-register.md`):

1. Populate Summary table: counts by vendor, orphan status, lock-in risk level
2. Populate SBB Detail table: all SBBs with fields
3. Populate Orphan SBBs table: SBBs with no ABB link (vendor-first selections)
4. Populate Lock-in Risk table: SBBs with high lock-in constraints
5. Populate ABB Coverage map: which ABBs are implemented by which SBBs
6. Populate Vendor Portfolio: all vendors used, with SBB counts

### Step 5 — Write the Register File

Write to: `EA-projects/{slug}/artifacts/sbb-register.md`. If the file already exists, archive it to `snapshots/` first per `skills/ea-artifact-templates/references/register-snapshot-convention.md`.

Register in `engagement.json → artifacts[]` if not already present (single entry at the stable path).

Confirm: `"SBB Register written: {N} SBBs ({N} orphans flagged, {N} lock-in risks)"`

---

## Mode: `status`

Display inline summary:

```
SBB Status — {engagement name}
Generated: {YYYY-MM-DD}

Total SBBs:     {N}
By Vendor:      {vendor} ×{N} | {vendor} ×{N} | ...
Orphans:        {N} SBB(s) with no ABB link  ← vendor-first anti-pattern
Lock-in Risks:  {N} High | {N} Medium | {N} Low
Version Drift:  {N} SBB(s) with version conflicts across artifacts
Coverage:       {N} ABB(s) implemented by {N} SBB(s)

{if N > 0 orphans}: Use '/ea-sbbs generate' to write the full register with remediation notes.
{if N > 0 lock-in}: Consider running '/ea-grill phase-d --skill lock-in' to review constraints.
```

---

## Mode: `new`

Create a new SBB record.

### Step 2 — Determine Next SBB Number

Find highest existing SBB-NNN. Assign next: `SBB-{NNN+1}` (zero-padded).

### Step 3 — Collect SBB Metadata

```
Creating new SBB — SBB-{NNN}

1. Name (specific product or technology, e.g. "AWS CloudTrail"):
2. Implements (ABB-NNN this SBB realises — required):
3. Vendor / Source (commercial vendor, open-source project, or internal build):
4. Version (specific version, release channel, or "managed"):
5. Referenced Constraints (CST-NNN IDs that bound this SBB selection, comma-separated, or press Enter):
6. Constraints / Lock-in Risk (vendor-specific detail: proprietary APIs, egress costs, licensing, data residency):
```

**Vendor Landscape context (if Architecture Repository linked):**

After the user provides the Vendor / Source value (field 3), check `engagement.json → repoPath`. If set:

1. Read `{repoPath}/vendor-landscape/vendor-index.md` and search for a partial match on the vendor name entered.
2. If a match is found, display:
   ```
   📋 Vendor Landscape match: {VDR-NNN} — {Vendor} / {Product}
      Roadmap Status : {roadmapStatus}
      Lock-in Risk   : {lockInRisk}
      Notes          : {notes (first line)}
   ```
3. If `roadmapStatus` is `Sunset` or `EoL`, warn:
   ```
   ⚠️  This vendor/product is marked {roadmapStatus} in the Architecture Repository.
       Consider selecting an alternative or documenting the exception in the Constraints Register.
   ```
4. Ask: `"Link this SBB to {VDR-NNN}? (y/n)"`. If yes, add `linkedVDR: VDR-NNN` to the SBB frontmatter when writing the file.
5. If no match is found, note: `"No Vendor Landscape entry for '{vendor}'. Use '/ea-vendors add' to register this vendor."`

### Step 4 — Validate

- `Implements` is required. If blank or ABB-NNN not found, warn: "⚠️ This SBB has no ABB. Create the ABB first with `/ea-abbs new`, or proceed as vendor-first? (y/n)"
- Scan `name` for vendor names; if none found, warn: "⚠️ This looks like an ABB (logical, no vendor). Use `/ea-abbs new` instead? (y/n)"

### Step 5 — Create File

Write to: `EA-projects/{slug}/artifacts/sbb-{NNN}-{kebab-name}.md`

Register in `engagement.json → artifacts[]`.

Confirm: `"SBB-{NNN} created. Lock-in constraints captured. Use '/ea-grill sbb-{NNN}' to stress-test vendor risk."`

---

## Mode: `update SBB-NNN <field> <value>`

Update a single field.

**Valid fields:**

| Field | Valid values |
|---|---|
| `name` | any string |
| `implements` | ABB-NNN (single) |
| `vendor` | any string |
| `version` | any string |
| `referencedConstraints` | comma-separated CST-NNN list |
| `constraints` | any string |

**Validation rules:**
- Setting `name` to a logical description (no vendor) → warn about ABB leakage
- Setting `implements` to a non-existent ABB → warn, allow as planned
- Setting `referencedConstraints` → verify each CST-NNN exists in the engagement Constraints Register; if not found, warn and offer to create via `/ea-constraints add`
- Setting `constraints` → scan for lock-in keywords; if high-risk terms found, flag. If `referencedConstraints` is empty, warn: "⚠️ This SBB has vendor lock-in detail but no referenced CST-NNN constraint. Link a constraint for traceability? (y/n)"
- Setting `vendor` → if Architecture Repository is linked, check `{repoPath}/vendor-landscape/vendor-index.md` for a match. If found, show roadmap/lock-in summary and offer to update `linkedVDR` on the SBB. If the matched entry is `Sunset` or `EoL`, warn before applying.

**Procedure:**
1. Find the SBB file matching `sbb-{NNN}*.md` or the SBB row in the register
2. Show proposed change: `"SBB-NNN: {field} — '{old}' → '{new}'"`
3. Ask: `"Apply? (y/n)"`
4. On confirm: update the file and `engagement.json`

Confirm: `"Updated SBB-NNN: {field} set to '{new_value}'"`

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No SBBs found | Report "No SBBs found. Define SBBs in Technology Architecture SBB Register." |
| SBB appears in multiple artifacts | Merge fields; prefer Technology Architecture version; list all sources |
| SBB with no ABB link | Flag as orphan/vendor-first; suggest creating ABB via `/ea-abbs new` |
| Same vendor used 5+ times | Flag vendor concentration risk in status summary |
| `new`: no vendor in name | Warn and offer redirect to `/ea-abbs new` |
