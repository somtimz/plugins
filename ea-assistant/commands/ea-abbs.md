---
name: ea-abbs
description: Generate or view the Architecture Building Block (ABB) Register. Scan all artifacts for ABB-NNN entries, aggregate them into a consolidated register, and surface orphan or unlinked ABBs.
argument-hint: "[generate | status | new | update ABB-NNN <field> <value>] [--domain Business|Data|Application|Technology] [--phase C|D] [--req REQ-NNN]"
allowed-tools: [Read, Write, Bash, Glob, Grep]
---

You are executing the `/ea-abbs` command.

## Overview

Architecture Building Blocks (ABBs) are logical, vendor-neutral components defined in Phase C (Application/Data) and Phase D (Technology) architecture. This command aggregates all ABB-NNN entries from across the engagement into a single register, surfaces orphans (ABBs with no linked requirement or SBB), and supports creating or updating individual ABB records.

**Modes:**
- `generate` (default) — scan all artifacts for ABB tables and write `abb-register.md`
- `status` — inline summary of ABBs without writing a file
- `new` — create a new ABB record interactively
- `update ABB-NNN <field> <value>` — update a single field on an existing ABB

**Naming Convention:**
- Use a **noun phrase** describing the logical function (e.g. "Immutable Log Store", not "Back up logs")
- Must be **vendor-neutral and technology-agnostic** — no product names, brands, versions, or cloud-provider terms
- If a vendor name appears in the Name or Description, it is SBB content — redirect to `/ea-sbbs new`

**Filters:**
- `--domain` — filter by architecture domain
- `--phase` — filter by ADM phase where ABB was defined
- `--req REQ-NNN` — filter ABBs that satisfy a specific requirement

---

## Step 1 — Resolve Active Engagement

> Resolve the active engagement per `skills/ea-engagement-lifecycle/references/engagement-resolution.md`.

---

## Mode: `generate` (default)

### Step 2 — Scan for ABB Entries

Scan all `.md` files in `EA-projects/{slug}/artifacts/` for ABB tables:

| Artifact Pattern | Section to Scan | Row Format |
|---|---|---|
| `business-architecture*.md` | `#### ABBs for CAP-NNN` subsections | `ABB-NNN | Name | Description | Satisfies (REQ-NNN) | Implemented by (SBB-NNN)` |
| `application-architecture*.md` | ABB Register or ABB sections | `ABB-NNN | Name | Description | Satisfies (REQ-NNN) | Implemented by (SBB-NNN)` |
| `data-architecture*.md` | ABB Register or ABB sections | Same |
| `technology-architecture*.md` | ABB Register section | `ABB-NNN | Name | Description | Satisfies (REQ-NNN) | Implemented by (SBB-NNN) | Domain` |

For each ABB row found:
- Extract: ID, Name, Description, Satisfies (REQ-NNN list), Implemented by (SBB-NNN list), Domain
- Record source artifact filename and phase
- If the same ABB-NNN appears in multiple artifacts, merge fields (take the most complete version)

### Step 3 — Detect Orphans and Gaps

For each ABB-NNN:
- **Orphan (Critical):** No `Satisfies` REQ-NNN — an ABB with no requirement is unvalidated
- **Orphan (Warning):** No `Implemented by` SBB-NNN — an ABB without an SBB may be premature (OK in Phase C, flag in Phase D+)
- **Leakage:** Name or Description contains a vendor name, version, or product → flag as "SBB content in ABB"

### Step 4 — Compile ABB Register

Using the ABB register template (`templates/abb-register.md`):

1. Populate Summary table: counts by domain, orphan status
2. Populate ABB Detail table: all ABBs with fields
3. Populate Orphan ABBs table: ABBs missing REQ or SBB links
4. Populate Leakage Report: ABBs with vendor/product names
5. Populate Requirement Coverage map: which REQs are satisfied by which ABBs

### Step 5 — Write the Register File

Write to: `EA-projects/{slug}/artifacts/abb-register.md`. If the file already exists, archive it to `snapshots/` first per `skills/ea-artifact-templates/references/register-snapshot-convention.md`.

Register in `engagement.json → artifacts[]` if not already present (single entry at the stable path).

Confirm: `"ABB Register written: {N} ABBs ({N} orphans flagged)"`

---

## Mode: `status`

Display inline summary:

```
ABB Status — {engagement name}
Generated: {YYYY-MM-DD}

Total ABBs:     {N}
By Domain:      Business {N} | Data {N} | Application {N} | Technology {N}
By Phase:       C {N} | D {N}
Orphans:        {N} ABB(s) with no REQ link  |  {N} ABB(s) with no SBB link
Leakage:        {N} ABB(s) with vendor/product names
Coverage:       {N} REQ(s) satisfied by {N} ABB(s)

{if N > 0 orphans}: Use '/ea-abbs generate' to write the full register with remediation notes.
```

---

## Mode: `new`

Create a new ABB record.

**RA reference (if adopted RAs exist):**
Before starting the interview, check `engagement.json → adoptedRAs[]`. If non-empty:
- Load each adopted RA's `## Architecture Layers` table.
- If any RA has a row whose `Layer` matches the domain the user is creating an ABB in, display:
  ```
  Reference Architecture hint — {RA-NNN}: {RA name}
  The following ABBs are defined in this RA for the {domain} layer:
  | ABB-NNN | ABB Name | Role in Pattern |
  ...
  ```
  Then ask: "Are you implementing one of these, or defining a new ABB?"
  - If implementing an existing one: pre-fill the Name and Description from the RA row; let user confirm or override.
  - If new: continue with the standard interview.

### Step 2 — Determine Next ABB Number

Find highest existing ABB-NNN. Assign next: `ABB-{NNN+1}` (zero-padded).

### Step 3 — Collect ABB Metadata

```
Creating new ABB — ABB-{NNN}

1. Name (noun phrase describing logical function, e.g. "Immutable Log Store"):
   Tip: Check `skills/ea-artifact-templates/references/abb-catalogue.md` for standard ABB names to reuse.
2. Domain (Business / Data / Application / Technology):
3. Description (what it does, vendor-neutral):
4. Satisfies (REQ-NNN IDs, comma-separated, or press Enter):
5. Implemented by (SBB-NNN IDs, comma-separated, or press Enter — skip if Phase C):
```

### Step 4 — Validate

- Name must not contain vendor names or version numbers
- Description must be logical, not product-specific
- If vendor detected, warn: "⚠️ This looks like an SBB, not an ABB. Use `/ea-sbbs new` instead? (y/n)"

### Step 5 — Create File

Write to: `EA-projects/{slug}/artifacts/abb-{NNN}-{kebab-name}.md`

Using a lightweight ABB record template with the collected fields.

Register in `engagement.json → artifacts[]`.

Confirm: `"ABB-{NNN} created. Use '/ea-interview abb-{NNN}' to populate extended rationale."`

---

## Mode: `update ABB-NNN <field> <value>`

Update a single field.

**Valid fields:**

| Field | Valid values |
|---|---|
| `name` | any string |
| `description` | any string |
| `domain` | `Business` / `Data` / `Application` / `Technology` |
| `satisfies` | comma-separated REQ-NNN list |
| `implementedBy` | comma-separated SBB-NNN list |

**Validation rules:**
- Setting `name` or `description` — scan for vendor names; if found, warn about leakage
- Setting `implementedBy` — verify each SBB-NNN exists in the engagement (or note as planned)

**Procedure:**
1. Find the ABB file matching `abb-{NNN}*.md` or the ABB row in the register
2. Show proposed change: `"ABB-NNN: {field} — '{old}' → '{new}'"`
3. Ask: `"Apply? (y/n)"`
4. On confirm: update the file and `engagement.json`

Confirm: `"Updated ABB-NNN: {field} set to '{new_value}'"`

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No ABBs found in any artifact | Report "No ABBs found. Define ABBs in Application/Technology Architecture templates." |
| ABB appears in multiple artifacts | Merge fields; prefer the most complete version; list all sources |
| ABB with no REQ link | Flag as orphan; suggest linking via `/ea-requirements` or `/ea-interview` |
| ABB with vendor name in description | Flag as leakage; suggest moving to SBB or rewriting as logical description |
| `new`: name contains vendor | Warn and offer to redirect to `/ea-sbbs new` |
