---
name: ea-changes
description: Generate or view a Change Register by aggregating all Architecture Change Request artifacts in the active engagement. Supports filtering by status, type, domain, risk, owner, and phase.
---

You are executing the `/ea-changes` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

The Change Register aggregates all `change-request-*.md` (and `change-request.md`) artifacts in `EA-projects/{slug}/artifacts/` into a single cross-engagement view. It provides a consolidated picture of proposed, approved, rejected, and deferred architecture changes.

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` (excluding `.archive/`) and ask the user to select one.
3. Load `engagement.json` to confirm the slug and engagement name.

---

## Step 2 — Parse Arguments

Accepted flags (all optional, combinable):

| Flag | Values | Effect |
|---|---|---|
| `--status` | `open` / `approved` / `rejected` / `deferred` / `all` | `open` = Draft + Under Review; `approved` = Approved + Approved with Conditions; `all` = all states (default) |
| `--type` | `new-capability` / `substitution` / `process` / `correction` / `decommission` / `other` | Filter by Type of Change |
| `--domain` | `business` / `data` / `app` / `tech` | Filter by Affected Architecture Domains |
| `--risk` | `high` / `med` / `low` | Filter by Overall Risk Level |
| `--owner "name"` | Any string | Case-insensitive partial match on Assigned To or Decision Authority |
| `--phase "phase"` | Any phase identifier | Filter by phase in which the ACR was raised |

If no arguments given, default to `generate` mode with no filters.

---

## Mode: `status`

Invoked as: `/ea-changes status`

1. Scan all `change-request*.md` files (same as generate, below).
2. Output an inline summary table — **do not write any file**:

```
Change Register — {engagement name}
═══════════════════════════════════════════════════════════
Under Review : {N} change requests
Approved     : {N} ({N} with conditions)
Rejected     : {N}
Deferred     : {N}
─────────────────────────────────────────────────────────
Total        : {N}

Open change requests:
  {ACR ID} — {summary} [{risk level}] — raised by {raised_by}
  …
═══════════════════════════════════════════════════════════
```

---

## Mode: `update <ACR-ID> <field> <value>`

Invoked as: `/ea-changes update ACR-001 status "Approved"`

1. Locate the source `change-request-*.md` file containing the specified ACR ID (match on `**Change Request ID:**` field).
2. Update the specified field in the document:
   - `status` → update the **Status:** line
   - `decision` → update § 5 Disposition **Decision:** line
   - `decision-authority` → update **Decision Authority:** line
   - `owner` → update the Assigned To or Decision Authority field
3. Update `lastModified` in the artifact's YAML frontmatter.
4. Confirm: "Updated: {ACR ID} {field} → '{value}'."

---

## Mode: `generate` (default)

### Step 3 — Scan Change Request Artifacts

Find all files matching:
- `EA-projects/{slug}/artifacts/change-request-*.md`
- `EA-projects/{slug}/artifacts/change-request.md`

For each file, extract:
- **ACR ID** — from `**Change Request ID:**` field
- **Summary** — from `**Summary:**` field in § 1
- **Type of Change** — from `**Type of Change:**` in § 1
- **Affected Domains** — from `**Affected Architecture Domains:**` in § 1
- **Raised By** — from header `**Raised By:**`
- **Date Raised** — from header `**Date Raised:**`
- **Overall Risk Level** — from `**Overall Risk Level:**` in § 4
- **Status** — from header `**Status:**` line
- **Decision** — from `**Decision:**` in § 5 (if populated)
- **Decision Date** — from `**Decision Date:**` in § 5
- **Decision Authority** — from `**Decision Authority:**` in § 5
- **Conditions** — from `**Conditions:**` in § 5 (if applicable)
- **Deferral Reason** — from `**Deferral Reason:**` in § 5 (if applicable)
- **Artifacts to Update** — from table in § 6

If no files are found, inform the user:
> "No Architecture Change Request artifacts found in this engagement. Create one with `/ea-artifact create change-request`."

---

### Step 4 — Apply Filters

Apply all active filter flags to the collected ACR data. Filtering rules:
- `--status open` → include only Draft and Under Review entries
- `--status approved` → include only Approved and Approved with Conditions entries
- `--domain` → include only entries where the Affected Architecture Domains field contains the specified domain
- `--risk high` → include only entries where Overall Risk Level = High
- `--owner "name"` → case-insensitive partial match on Raised By, Decision Authority, or any owner field

If filters result in zero entries, report: "No change requests match the specified filters. {N} total exist — run without filters to see all."

---

### Step 5 — Build the Register

Organise the filtered ACRs into sections:

1. **Summary** — counts by status and by type
2. **Open — Under Review** — entries with status Draft or Under Review
3. **Approved** — entries with status Approved (no conditions)
4. **Approved with Conditions** — entries with status Approved with Conditions; include conditions and whether they have been met
5. **Rejected** — entries with status Rejected; include rationale
6. **Deferred** — entries with status Deferred; include trigger and review date
7. **Change Impact Summary** — list artifacts referenced in § 6 of ACRs across all approved and open entries, sorted by frequency
8. **Source Cross-Reference** — one row per source file with ACR ID, status, and lastModified

**Edge cases:**
- If an ACR has no ID (`{{change_request_id}}` still present), assign a provisional label `ACR-UNID-{N}` and flag: "⚠️ This change request has no ID assigned."
- If a single file contains multiple change requests (non-standard), treat each as a separate entry and note the shared file.

---

### Step 6 — Write the Register File

Write the register to:
```
EA-projects/{slug}/artifacts/change-register-{YYYY-MM-DD}.md
```

Use the `change-register.md` template. Populate all sections from the collected data. Set:
- `generated: {today}`
- `filters: {applied filters or "None"}`
- `lastModified: {today}`

Add an entry to `engagement.json → artifacts[]`:
```json
{
  "name": "Change Register",
  "file": "change-register-{YYYY-MM-DD}.md",
  "phase": "H",
  "status": "Draft",
  "reviewStatus": "Not Reviewed"
}
```
If a change register already exists, overwrite it (registers are regenerated, not versioned) and update the existing `artifacts[]` entry.

---

### Step 7 — Report

Confirm: "Change Register written to `artifacts/change-register-{YYYY-MM-DD}.md`. {N} change requests — {N} open, {N} approved, {N} rejected, {N} deferred."

Offer:
```
Options:
  1. View open change requests in detail
  2. Update a change request status
  3. View change impact summary
  4. Run /ea-risks to cross-check risk items raised in ACRs
```
