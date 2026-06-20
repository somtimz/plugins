---
name: ea-risks
description: Generate or view the Risk Register by aggregating all risks from across all artifacts in the active engagement. Use `add` to capture a new risk interactively, `accept RIS-NNN` to record a formal acceptance decision, and `update RIS-NNN` to edit any field.
argument-hint: "[generate|status|add|update|accept] [--status open|monitoring|accepted|closed|all] [--severity critical|high|medium|low] [--owner \"name\"] [--phase A|B|C|D|E|F|G|H] [--artifact \"name\"] [RIS-NNN field value] [--reason \"text\"]"
allowed-tools: [Read, Write, Bash, Glob]
---

You are executing the `/ea-risks` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

The Risk Register aggregates all architecture risks from every artifact in the active engagement into a single cross-cutting view. It tracks likelihood, impact, mitigation, ownership, and status for every risk identified during the engagement.

**Risk sources scanned:**
- Architecture Vision — §16 Key Risks (summary; full detail in Risk Register)
- Statement of Architecture Work — Risk section
- Business Architecture, Data Architecture, Application Architecture, Technology Architecture — any `Risk` or `Key Risks` section
- Gap Analysis — unresolved GAP-NNN entries (gaps with no closed mitigation path)
- Migration Plan — §4 Risk Register table
- Architecture Compliance Assessment — Outstanding Risks section
- Appendix A4 tables (all artifacts) — rows where `Category = Risk`
- Any existing `risk-register*.md` artifact (for previously curated RIS-NNN entries)

---

## Step 1 — Resolve Active Engagement

> Resolve the active engagement per `skills/ea-engagement-lifecycle/references/engagement-resolution.md`.

---

## Step 2 — Parse Arguments

**Mode selection** (first positional argument, defaults to `generate`):

| Mode | Invocation | Effect |
|---|---|---|
| `generate` | `/ea-risks` or `/ea-risks generate` | Scan all artifacts, aggregate risks, write register file |
| `status` | `/ea-risks status` | Inline summary only — no file written |
| `add` | `/ea-risks add` | Interactively capture a new risk and write it to the register |
| `update` | `/ea-risks update RIS-NNN <field> <value>` | Update a single field on an existing risk |
| `accept` | `/ea-risks accept RIS-NNN [--reason "text"]` | Record a formal acceptance decision with mandatory reason |

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

3. Check for **stale reviews**: for each Critical or High risk with `Status: Open` or `Monitoring`, compare `Last Reviewed` to today. If >30 days ago (or `Last Reviewed` is blank), list them:
   ```
   ⚠️ Stale reviews ({N} Critical/High risks not reviewed in >30 days):
     RIS-001 — {title} (last reviewed: {date or never})
     RIS-004 — {title} (last reviewed: {date})
   ```

4. Offer: "Run `/ea-risks` to generate the full register, or `/ea-risks --severity critical` to focus on critical risks."

---

## Mode: `update`

Invoked as: `/ea-risks update RIS-NNN <field> <value>`

1. Locate the existing risk register file in `EA-projects/{slug}/artifacts/cross-cutting/operations/risk-register*.md`.
   - If multiple versions exist, use the most recent.
   - If none exists, prompt: "No risk register found. Run `/ea-risks` to generate one first."
2. Find the `RIS-NNN` section in the file.
3. Accepted fields for update:
   - `status` → `Open` / `Monitoring` / `Accepted` / `Closed`
   - `title` → updated risk title (one line)
   - `description` → updated risk description
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

## Mode: `add`

Invoked as: `/ea-risks add`

Captures a new risk interactively and writes it to the existing risk register. Does not regenerate the full register.

1. Locate the existing risk register in `EA-projects/{slug}/artifacts/cross-cutting/operations/risk-register.md`. If none exists, create a minimal register file using the template with this risk as the first entry.
2. Assign the next available RIS-NNN ID (increment from the highest existing ID).
3. Prompt for each field in sequence (all required unless noted):
   ```
   Title (one-line risk name):
   Description (what could happen and why):
   Likelihood (High / Medium / Low):
   Impact (High / Medium / Low):
   Mitigation (action to reduce likelihood or impact):
   Contingency (what to do if risk materialises) [optional — press Enter to skip]:
   Owner (name and role):
   Phase identified (A / B / C / D / E / F / G / H / Prelim):
   ```
4. Derive Rating from Likelihood × Impact using the standard matrix.
5. Show a confirmation preview:
   ```
   New risk — RIS-NNN: {title}
   Rating: {rating}  |  Likelihood: {L}  |  Impact: {I}
   Owner: {owner}  |  Phase: {phase}
   Mitigation: {mitigation}
   
   Add to register? (y/n)
   ```
6. On confirm: insert the new risk entry into the correct section (Critical / High / Medium / Low) of the register file. Set `Status: Open`, `Last Reviewed: {today}`.
7. Update `lastModified` in the register's YAML frontmatter.
8. Confirm: `"Added RIS-NNN: {title} ({rating}) to risk register."`

---

## Mode: `accept`

Invoked as: `/ea-risks accept RIS-NNN [--reason "text"]`

Records a formal acceptance decision for a risk — sets `Status: Accepted` and captures the mandatory reason in the risk entry. An accepted risk must have a documented rationale for governance purposes.

1. Locate the risk register and find the `RIS-NNN` entry.
1b. **Tolerance check:** if the register has a `## Risk Appetite & Tolerance` section, look up the acceptance authority for this risk's rating. If the authority is above lead-architect level (Sponsor / ARB), require it: prompt "This is a {rating} risk — acceptance authority is {authority}. Who is accepting it on their behalf? (name and role)" and record it as `Accepted By`. If the section marks the rating outside appetite (e.g. Critical: "must be mitigated or escalated"), warn before proceeding: "⚠️ {rating} risks are outside the stated risk appetite. Acceptance requires {authority} sign-off and should be exceptional. Continue? (y/n)"
2. If `--reason` flag is not provided, prompt:
   ```
   Acceptance reason (why is this risk being accepted without mitigation?):
   (e.g. "Cost of mitigation exceeds risk impact — accepted by sponsor",
   "Risk is inherent to the domain and cannot be mitigated",
   "Accepted pending Phase G review — revisit at contract gate")
   ```
   Reason is required. Empty input re-prompts once, then stops: `"Cancelled — risk not updated."`
3. Show confirmation:
   ```
   Accept RIS-NNN? (y/n)
   
   {Title}
   Status:  {current}  →  Accepted
   Reason:  {reason text}
   ```
4. On confirm:
   - Set `Status: Accepted`
   - Append to the risk entry: `**Acceptance Reason:** {reason}  ·  **Accepted:** {today}  ·  **Accepted By:** {facilitator}`
   - Update `Last Reviewed` to today
   - Move the risk row to the **Closed / Accepted Risks** table
5. Update `lastModified` in frontmatter.
6. Confirm: `"RIS-NNN accepted. Reason recorded. Moved to Closed / Accepted Risks."`

Note: if the risk is `Closed` rather than accepted (fully mitigated or expired), use `/ea-risks update RIS-NNN status Closed` instead.

---

## Mode: `generate` (default)

### Step 3 — Scan Artifacts for Risk Content

1. List all files in `EA-projects/{slug}/artifacts/` matching `*.md` (exclude `*.review.md` and `risk-register*.md`).
2. For each file, scan for risk content in these locations:

| Artifact Pattern | Section to Scan | Row Format |
|---|---|---|
| `architecture-vision*.md` | `## 14. Key Risks` or `## Key Risks` | `Risk \| Likelihood \| Impact \| Mitigation` table |
| `statement-of-architecture-work*.md` | Any `Risk` section | `Risk \| Likelihood \| Impact \| Mitigation` table |
| `business-architecture*.md` | Any `Risk` or `Key Risks` section | `Risk \| Likelihood \| Impact \| Mitigation` table or bullet list |
| `data-architecture*.md` | Any `Risk` or `Key Risks` section | Same |
| `application-architecture*.md` | Any `Risk` or `Key Risks` section | Same |
| `technology-architecture*.md` | Any `Risk` or `Key Risks` section | Same |
| `gap-analysis*.md` | All `GAP-NNN` entries with `Status ≠ Closed` | Treat each open gap as a risk: Description = gap description; Likelihood = Medium (default); Impact = infer from gap severity if present, else Medium; Mitigation = gap mitigation field if populated |
| `migration-plan*.md` | `## 4. Risk Register` | `Risk ID \| Description \| Likelihood \| Impact \| Mitigation \| Owner` table |
| `compliance-assessment*.md` | `Outstanding Risks` section | Any risk table or bullet list |
| `risk-register*.md` | All `RIS-NNN:` sections | Existing curated risk entries (highest fidelity — use as-is) |

3a. **Scan A4 tables for Risk-category concerns:**
- For each artifact file, read `## Appendix A4` and parse rows where `Category = Risk`
- For each such row:
  - Check whether a RIS-NNN entry already exists in any `risk-register*.md` matching the concern text (keyword substring match)
  - If no match: include as a new risk candidate with `Description` = concern text, `Raised By` = concern source, `Likelihood: TBD`, `Impact: TBD`, `Source: {artifact name} (A4 CON-NNN)`
  - If a match exists: skip (already registered); note `✓ Registered as RIS-NNN` in the register output
- TBD likelihood/impact risks are assigned `Rating: Unrated` and flagged in the Summary (same as other unrated risks)

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

4. Deduplicate: if the same risk description appears in both an existing `risk-register*.md` and another source artifact, use the register version (it is more authoritative).

5. Count: total artifacts scanned, artifacts with risks, total risk rows.

### Step 4 — Apply Filters

Apply any flags from Step 2 to the risk list. Partial-match flags (`--owner`, `--artifact`) use case-insensitive substring matching.

If filtering results in zero rows, output: "No risks match the applied filters." with the filter summary, then stop without writing a file.

### Step 5 — Derive Traceability

For each Open or Monitoring risk, check whether its description references any G-NNN or OBJ-NNN IDs from `engagement.json`. If references are present, populate `Affected Objectives`. If no references are explicit, note `—` (do not infer).

### Step 6 — Render the Risk Register

Populate `templates/cross-cutting/risk-register.md` with the collected data:

- Group risks by rating: Critical → High → Medium → Low
- Within each group, sort by likelihood descending (High first)
- Populate the Summary table with counts (filtered dataset)
- Populate the Heatmap Summary table with RIS-NNN lists per cell
- Populate the Source Artifact Cross-Reference table dynamically from the actual sources that contributed risks (one row per source artifact; do not include hardcoded entries for artifacts that had no risks)
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

- **Option 1** — Write to `EA-projects/{slug}/artifacts/cross-cutting/operations/risk-register.md`. If the file already exists, archive it to `snapshots/` first per `skills/ea-artifact-templates/references/register-snapshot-convention.md`. Register in `engagement.json` with `phase: "All"`, `status: "Draft"` (single entry at the stable path). Display a brief confirmation with counts.
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
| Gap Analysis gap has no severity field | Default Likelihood and Impact to Medium; flag as Unrated for review |
| A4 Category=Risk concern already has a matching RIS-NNN | Skip; note `✓ Registered as RIS-NNN` in A4 scan output |
| `add`: no existing register | Create a minimal register from template with the new risk as the first entry |
| `accept`: risk is already Accepted | Warn: "RIS-NNN is already Accepted. Update the reason? (y/n)" |
| `accept`: reason prompt left empty twice | "Cancelled — risk not updated." — stop without writes |
| `accept`: risk is Closed | Inform: "RIS-NNN is Closed. Use `/ea-risks update RIS-NNN status Open` first if you want to reopen and accept it." |
