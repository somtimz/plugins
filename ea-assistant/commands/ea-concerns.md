---
name: ea-concerns
description: Generate or view the Concerns Register by aggregating all stakeholder concerns and objections from Appendix A4 across all artifacts in the active engagement. Supports filtering by status, category, source, and artifact.
argument-hint: "[generate|status] [--status addressed|partial|attention|all] [--category scope|goal|approach|feasibility|risk|stakeholder|other] [--source \"name\"] [--artifact \"name\"]"
allowed-tools: [Read, Write, Glob]
---

You are executing the `/ea-concerns` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

The Concerns Register aggregates all rows from every `## Appendix A4 — Stakeholder Concerns & Objections` section across all artifacts in the active engagement. It provides a single cross-artifact view of open concerns, objections, and tough questions — and surfaces items that require escalation to the Risk Register.

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
| `generate` | `/ea-concerns` or `/ea-concerns generate` | Scan all artifacts, aggregate concerns, write register file |
| `status` | `/ea-concerns status` | Inline summary only — no file written |

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

1. List all files in `EA-projects/{slug}/artifacts/` matching `*.md` (exclude `*.review.md` and `concerns-register-*.md`).
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
- Check whether a RIS-NNN entry already exists in `EA-projects/{slug}/artifacts/risk-register-*.md` that corresponds to this concern (match by keyword in description).
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

- **Option 1** — Write to `EA-projects/{slug}/artifacts/concerns-register-{YYYY-MM-DD}.md`. Register in `engagement.json` with `phase: "All"`, `status: "Draft"`. If a register for today already exists, append `-v2`, `-v3` etc.
- **Option 2** — Output the Summary and Requires Attention table only, inline. Do not write any file.

After generating, if any Risk-eligible concerns were flagged, offer:
> "⚠️ {N} concern(s) are risk-eligible with no matching Risk Register entry. Run `/ea-risks` to review and register them."

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No A4 section found in any artifact | Report "No A4 appendices found." Offer: "Run `/ea-grill` on key artifacts to generate concerns, or add them manually to each artifact's A4 appendix." |
| A4 row with missing fields | Include with missing fields as `—`; flag in Summary: "N rows with missing fields" |
| Concern already in Risk Register | Note in the register: `✓ Registered as {RIS-NNN}` in the Risk-Eligible column |
| Duplicate CON-NNN across artifacts | Keep both; note: "Duplicate ID — re-numbering applied in this register: CON-NNN (from {artifact})" |
| All concerns are Addressed | Still write register; celebrate: "All {N} concerns have documented responses." |
