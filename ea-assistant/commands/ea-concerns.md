---
name: ea-concerns
description: Generate or view the Concerns Register by aggregating all stakeholder concerns and objections from Appendix A4 across all artifacts in the active engagement. Use `close CON-NNN` to interactively resolve a concern and update its source artifact.
argument-hint: "[generate|status|close CON-NNN] [--status addressed|partial|attention|all] [--category ...] [--partial] [--response \"text\"]"
allowed-tools: [Read, Write, Glob]
---

You are executing the `/ea-concerns` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

The Concerns Register aggregates all rows from every `## Appendix A4 — Stakeholder Concerns & Objections` section across all artifacts in the active engagement. It provides a single cross-artifact view of open concerns, objections, and tough questions — and surfaces items that require escalation to the Risk Register.

---

## Step 1 — Resolve Active Engagement

> Resolve the active engagement per `skills/ea-engagement-lifecycle/references/engagement-resolution.md`.

---

## Step 2 — Parse Arguments

**Mode selection** (first positional argument, defaults to `generate`):

| Mode | Invocation | Effect |
|---|---|---|
| `generate` | `/ea-concerns` or `/ea-concerns generate` | Scan all artifacts, aggregate concerns, write register file |
| `status` | `/ea-concerns status` | Inline summary only — no file written |
| `close` | `/ea-concerns close CON-NNN` | Interactively resolve a concern and write the update to its source artifact |

**Filter flags:**

| Flag | Values | Effect |
|---|---|---|
| `--status` | `addressed` / `partial` / `attention` / `all` | Filter by concern status. Default for `generate`: `all`. Default for `status`: `attention` |
| `--category` | `scope` / `goal` / `approach` / `feasibility` / `risk` / `stakeholder` / `other` | Filter by concern category |
| `--source "name"` | Any string | Case-insensitive partial match on the Raised By field |
| `--artifact "name"` | Any string | Case-insensitive partial match on source artifact name |

---

## Mode: `status`

1. Scan all A4 appendices (same as `generate`, Step 3 below).
2. Output inline summary — **do not write any file**:

```
Concerns Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Addressed: {N}  |  Partially Addressed: {N}  |  Requires Attention: {N}

By Category:  Scope {N}  |  Goal {N}  |  Approach {N}  |  Feasibility {N}  |  Risk {N}  |  Stakeholder {N}  |  Other {N}
Risk-eligible: {N} concern(s) flagged as Risk category — consider adding to Risk Register
Sources:      {N} artifacts scanned, {N} had A4 rows
```

3. Offer: "Run `/ea-concerns` to generate the full register, or `/ea-concerns --status attention` to focus on unresolved items."

---

## Mode: `generate` (default)

### Step 3 — Scan Artifacts for A4 Tables

1. List all files in `EA-projects/{slug}/artifacts/` matching `*.md` (exclude `*.review.md` and `concerns-register*.md`).
2. For each file, search for a section matching `## Appendix A4` or `### Appendix A4 — Stakeholder Concerns`.
3. Parse each table row (skip header rows and placeholder rows containing `*(no concerns recorded)*`).
4. Collect into a unified concern list with an added `sourceArtifact` field (the artifact file name, prettified).
5. Count: total artifacts scanned, artifacts with A4 rows, total rows collected.

**Parsing rules:**
- Column order: ID | Concern | Raised By | Category | Status | Response | Action / Owner
- If a row has fewer columns (partial entry), populate missing fields as `—`
- Skip rows where ID is empty or starts with `*(no`

### Step 4 — Apply Filters

Apply flags from Step 2. For `--status attention`, match rows where Status is `Requires Attention`. For partial-match flags (`--source`, `--artifact`), use case-insensitive substring matching.

If filtering results in zero rows, output: "No concerns match the applied filters." followed by the filter summary, then stop without writing a file.

### Step 5 — Flag Risk-Eligible Concerns

For each concern where `Category = Risk` or `Status = Requires Attention`:
- Check whether a RIS-NNN entry already exists in `EA-projects/{slug}/artifacts/cross-cutting/operations/risk-register*.md` that corresponds to this concern (match by keyword in description).
- If no matching risk found, flag the concern as **Risk-eligible** — note in the register output: "⚠️ No RIS-NNN — consider adding to Risk Register via `/ea-risks`"

### Step 6 — Render the Concerns Register

Build the register document with this structure:

```markdown
---
artifact: Concerns Register
artifactId: concerns-register
engagement: {name}
phase: All
status: Draft
generated: {YYYY-MM-DD}
filters: {filter summary or "none"}
---

# Concerns Register

**Engagement:** {name}
**Organisation:** {organisation}
**Generated:** {YYYY-MM-DD}

---

## Summary

| Total | Addressed | Partially Addressed | Requires Attention |
|---|---|---|---|
| {N} | {N} | {N} | {N} |

---

## Requires Attention

| ID | Concern | Raised By | Category | Source Artifact | Action / Owner | Risk-Eligible |
|---|---|---|---|---|---|---|
| CON-NNN | {concern} | {source} | {category} | {artifact} | {action} | ⚠️ Yes / — |

---

## Partially Addressed

| ID | Concern | Raised By | Category | Source Artifact | Response | Action / Owner |
|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... |

---

## Addressed

| ID | Concern | Raised By | Category | Source Artifact | Response |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

---

## Source Artifact Cross-Reference

| Artifact | Concerns | Requires Attention |
|---|---|---|
| Architecture Vision | {N} | {N} |
| ... | ... | ... |
```

### Step 7 — Output Format

Ask the user:

> Output as:
> **1.** Markdown (in-chat)
> **2.** Summary + Requires Attention only (inline, no file)
>
> Press Enter or type **1** for Markdown.

- **Option 1** — Write to `EA-projects/{slug}/artifacts/cross-cutting/operations/concerns-register.md`. If the file already exists, archive it to `snapshots/` first per `skills/ea-artifact-templates/references/register-snapshot-convention.md`. Register in `engagement.json` with `phase: "All"`, `status: "Draft"` (single entry at the stable path).
- **Option 2** — Output the Summary and Requires Attention table only, inline. Do not write any file.

After generating, if any Risk-eligible concerns were flagged, offer:
> "⚠️ {N} concern(s) are risk-eligible with no matching Risk Register entry. Run `/ea-risks` to review and register them."

---

## Mode: `close CON-NNN`

Invoked as: `/ea-concerns close CON-NNN [--partial] [--response "text"]`

Resolves a concern by updating its Status, Response, and Action/Owner fields in the source artifact's A4 table.

**Flags:**

| Flag | Effect |
|---|---|
| `--partial` | Sets Status to `Partially Addressed` instead of `Addressed` |
| `--response "text"` | Pre-fills the Response field; skips the response prompt |

### Step A — Resolve Active Engagement

Same as `generate` Step 1.

### Step B — Locate CON-NNN

1. Scan all `*.md` files in `EA-projects/{slug}/artifacts/` (exclude `*.review.md` and `concerns-register*.md`) for an A4 table row whose ID column matches `CON-NNN` (exact, case-insensitive).
2. Record the source artifact file path and the full row content.
3. If not found: `"CON-NNN not found in any A4 appendix. Run /ea-concerns status to list all concern IDs."` — stop.
4. If found in multiple artifacts: list all matches and ask the user to select which to update.

### Step C — Show Current State

```
Concern found in: {Artifact Name}

  ID:         CON-NNN
  Concern:    {concern text}
  Raised By:  {source}
  Category:   {category}
  Status:     {current status}
  Response:   {current response or —}
  Action:     {current action / owner or —}
```

If `Status` is already `Addressed`: warn before continuing:
```
⚠️ CON-NNN is already Addressed. Update anyway? (y/n)
```
If user answers `n`: stop without changes.

### Step D — Prompt for Response

Skip this step if `--response` flag was provided.

```
Response — where or how is this concern addressed?
(e.g. "§5 Constraints — added as a hard constraint", "ADR-007 addresses this",
"Accepted by sponsor — out of scope for this engagement")
```

Response is required. If the user provides an empty input, re-prompt once. On second empty input: `"Cancelled — concern not updated."` — stop.

### Step E — Confirm the Change

```
Apply this change? (y/n)

  CON-NNN in {Artifact Name}:
  Status:   {current}  →  {Addressed | Partially Addressed}
  Response: {response text}
  Action:   {current action}  →  —
```

For `Partially Addressed`: leave existing Action/Owner unchanged (or prompt if currently `—`).

If the user answers `n`: stop without changes.

### Step F — Write Update to Source Artifact

1. Find the A4 table row matching `CON-NNN` in the source artifact file.
2. Update the row in place:
   - `Status` → `Addressed` (default) or `Partially Addressed` (if `--partial`)
   - `Response` → response text
   - `Action / Owner` → `—` (for Addressed); preserve existing value for Partially Addressed
3. Update `lastModified` in the artifact's YAML frontmatter to the current ISO 8601 timestamp.

### Step G — Update engagement.json

Find the entry in `engagement.json → artifacts[]` whose `file` matches the source artifact path. Update its `lastModified` to the current ISO 8601 timestamp.

### Step H — Confirm and Offer Next Steps

```
Closed CON-NNN in {Artifact Name} — Status: {Addressed | Partially Addressed}
Response: "{response text}"
```

If `Category = Risk` and no matching RIS-NNN was found in any `risk-register*.md`:
```
⚠️ This concern is categorised as Risk. If a corresponding RIS-NNN exists in the
Risk Register, run `/ea-risks update RIS-NNN status Closed` to mark it resolved.
```

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No A4 section found in any artifact | Report "No A4 appendices found." Offer: "Run `/ea-grill` on key artifacts to generate concerns, or add them manually to each artifact's A4 appendix." |
| A4 row with missing fields | Include with missing fields as `—`; flag in Summary: "N rows with missing fields" |
| Concern already in Risk Register | Note in the register: `✓ Registered as {RIS-NNN}` in the Risk-Eligible column |
| Duplicate CON-NNN across artifacts | Keep both; note: "Duplicate ID — re-numbering applied in this register: CON-NNN (from {artifact})" |
| All concerns are Addressed | Still write register; celebrate: "All {N} concerns have documented responses." |
| `close`: CON-NNN not found | `"CON-NNN not found in any A4 appendix."` — stop |
| `close`: CON-NNN in multiple artifacts | List matches with source artifact name; prompt user to select one |
| `close`: concern already Addressed | Warn: "CON-NNN is already Addressed. Update anyway? (y/n)" |
| `close`: response prompt left empty twice | `"Cancelled — concern not updated."` — stop without writes |
| `close`: source artifact is Approved | Warn before write: "This artifact is Approved. Updating it will not change reviewStatus. Proceed? (y/n)" |
| `close --partial`: Action/Owner is empty | Prompt: "Action / Owner for this partially addressed concern:" before confirming |
