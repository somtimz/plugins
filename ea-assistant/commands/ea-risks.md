---
name: ea-risks
description: Generate or view the Risk Register by aggregating all risks from across all artifacts in the active engagement. Supports filtering by status, severity, owner, domain, phase, or source artifact.
argument-hint: "[generate|status|update] [--status open|monitoring|accepted|closed|all] [--severity critical|high|medium|low] [--owner \"name\"] [--phase A|B|C|D|E|F|G|H] [--artifact \"name\"] [RIS-NNN field value]"
allowed-tools: [Read, Write, Bash, Glob]
---

You are executing the `/ea-risks` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

The Risk Register aggregates all architecture risks from every artifact in the active engagement into a single cross-cutting view. It tracks likelihood, impact, mitigation, ownership, and status for every risk identified during the engagement.

**Risk sources scanned:**
- Architecture Vision — §14 Key Risks table
- Statement of Architecture Work — Risk section
- Migration Plan — §4 Risk Register table
- Architecture Compliance Assessment — Outstanding Risks section
- Any existing `risk-register-*.md` artifact (for previously curated RIS-NNN entries)

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` (excluding `.archive/`) and ask the user to select one.
3. Load `engagement.json` to confirm the slug and engagement name.

---

## Step 2 — Parse Arguments

**Mode selection** (first positional argument, defaults to `generate`):

| Mode | Invocation | Effect |
|---|---|---|
| `generate` | `/ea-risks` or `/ea-risks generate` | Scan all artifacts, aggregate risks, write register file |
| `status` | `/ea-risks status` | Inline summary only — no file written |
| `update` | `/ea-risks update RIS-NNN <field> <value>` | Update a single field on an existing risk |

**Filter flags** (apply to `generate` and `status` modes):

| Flag | Values | Effect |
|---|---|---|
| `--status` | `open` / `monitoring` / `accepted` / `closed` / `all` | Filter by risk status. Default for `generate`: `all`. Default for `status`: `open` |
| `--severity` | `critical` / `high` / `medium` / `low` | Filter by derived risk rating |
| `--owner "name"` | Any string | Case-insensitive partial match on Owner |
| `--phase` | `A` / `B` / `C` / `D` / `E` / `F` / `G` / `H` | Filter by phase where risk was identified |
| `--artifact "name"` | Any string | Filter by source artifact (partial match) |

---

## Mode: `status`

1. Scan all risk sources (same as `generate`, Step 3 below).
2. Output inline summary — **do not write any file**:

```
Risk Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Open: {N}  |  Monitoring: {N}  |  Accepted: {N}  |  Closed: {N}

By Rating:    Critical {N}  |  High {N}  |  Medium {N}  |  Low {N}
By Source:    Arch Vision {N}  |  SoAW {N}  |  Migration Plan {N}  |  Compliance {N}  |  Register {N}
Open owners:  {name} ×{N}  |  {name} ×{N}  |  Unassigned ×{N}
Sources:      {N} artifacts scanned, {N} contained risks
```

3. Offer: "Run `/ea-risks` to generate the full register, or `/ea-risks --severity critical` to focus on critical risks."

---

## Mode: `update`

Invoked as: `/ea-risks update RIS-NNN <field> <value>`

1. Locate the existing risk register file in `EA-projects/{slug}/artifacts/risk-register-*.md`.
   - If multiple versions exist, use the most recent.
   - If none exists, prompt: "No risk register found. Run `/ea-risks` to generate one first."
2. Find the `RIS-NNN` section in the file.
3. Accepted fields for update:
   - `status` → `Open` / `Monitoring` / `Accepted` / `Closed`
   - `owner` → name and role string
   - `mitigation` → updated mitigation text
   - `contingency` → updated contingency text
   - `likelihood` → `High` / `Medium` / `Low`
   - `impact` → `High` / `Medium` / `Low`
4. If `likelihood` or `impact` changes, recalculate the `Rating` field using the rating matrix (see template guidance).
5. Update the `Last Reviewed` field to today's date.
6. If status is set to `Closed` or `Accepted`, move the risk row to the **Closed / Accepted Risks** table and record the resolution.
7. Write the updated file and confirm: "Updated RIS-NNN: {field} → {new value}."

---

## Mode: `generate` (default)

### Step 3 — Scan Artifacts for Risk Content

1. List all files in `EA-projects/{slug}/artifacts/` matching `*.md` (exclude `*.review.md` and `risk-register-*.md`).
2. For each file, scan for risk content in these locations:

| Artifact Pattern | Section to Scan | Row Format |
|---|---|---|
| `architecture-vision*.md` | `## 14. Key Risks` or `## Key Risks` | `Risk \| Likelihood \| Impact \| Mitigation` table |
| `statement-of-architecture-work*.md` | Any `Risk` section | `Risk \| Likelihood \| Impact \| Mitigation` table |
| `migration-plan*.md` | `## 4. Risk Register` | `Risk ID \| Description \| Likelihood \| Impact \| Mitigation \| Owner` table |
| `compliance-assessment*.md` | `Outstanding Risks` section | Any risk table or bullet list |
| `risk-register-*.md` | All `RIS-NNN:` sections | Existing curated risk entries (highest fidelity — use as-is) |

3. For each risk row found:
   - Extract: description, likelihood, impact, mitigation, owner (if present).
   - Derive rating from likelihood × impact:
     - `High` + `High` → **Critical**
     - `High` + `Medium` OR `Medium` + `High` → **High**
     - `Medium` + `Medium` OR `High` + `Low` OR `Low` + `High` → **Medium**
     - `Medium` + `Low` OR `Low` + `Medium` OR `Low` + `Low` → **Low**
     - Unknown or missing values → **Unrated**
   - Record source artifact filename (prettified) and ADM phase.
   - Assign a new `RIS-NNN` ID if not already assigned (increment from last used ID; preserve existing IDs from prior register).

4. Deduplicate: if the same risk description appears in both an existing `risk-register-*.md` and another source artifact, use the register version (it is more authoritative).

5. Count: total artifacts scanned, artifacts with risks, total risk rows.

### Step 4 — Apply Filters

Apply any flags from Step 2 to the risk list. Partial-match flags (`--owner`, `--artifact`) use case-insensitive substring matching.

If filtering results in zero rows, output: "No risks match the applied filters." with the filter summary, then stop without writing a file.

### Step 5 — Derive Traceability

For each Open or Monitoring risk, check whether its description references any G-NNN or OBJ-NNN IDs from `engagement.json`. If references are present, populate `Affected Objectives`. If no references are explicit, note `—` (do not infer).

### Step 6 — Render the Risk Register

Populate `templates/risk-register.md` with the collected data:

- Group risks by rating: Critical → High → Medium → Low
- Within each group, sort by likelihood descending (High first)
- Populate the Summary table with counts (filtered dataset)
- Populate the Heatmap Summary table with RIS-NNN lists per cell
- Populate the Source Artifact Cross-Reference table
- Populate the Closed / Accepted Risks table with any risks in those statuses
- Set `generated:` frontmatter to today's date
- If filters were applied, record in frontmatter: `filters: {filter summary}`

### Step 7 — Output Format

Ask the user:

> Output as:
> **1.** Markdown (in-chat)
> **2.** Word document (.docx)
> **3.** Summary table only (inline, no file)
>
> Press Enter or type **1** for Markdown.

- **Option 1** — Write to `EA-projects/{slug}/artifacts/risk-register-{YYYY-MM-DD}.md`. Register in `engagement.json` with `phase: "All"`, `status: "Draft"`. If a risk register for today already exists, append `-v2`, `-v3` etc. Display a brief confirmation with counts.
- **Option 2** — Write the `.md` file first (same as Option 1), then load the `ea-generation` skill and export to `.docx`.
- **Option 3** — Output the Summary and Critical + High risk tables inline only. Do not write any file.

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No artifacts contain risk content | Report "No risks found in any artifact." Offer to create a risk register from scratch using grill-me-premortem |
| Risk row has no likelihood or impact | Include with `Rating: Unrated`; flag in Summary: "N unrated risks — run `/ea-risks update RIS-NNN likelihood <value>` to complete" |
| Existing risk register found | Preserve all existing `RIS-NNN` IDs and curated content; only add new risks from re-scan; update summary counts |
| Same risk in multiple artifacts | Use the most detailed version; record all source artifacts in `Source` field (comma-separated) |
| Risk with no owner | Set `Owner: Unassigned`; flag in summary count |
| Migration Plan uses `MIG-RNNNN` IDs | Assign a canonical `RIS-NNN` and record the source ID in the `Source` field as `Migration Plan (MIG-R001)` |
