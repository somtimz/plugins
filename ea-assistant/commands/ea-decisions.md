---
name: ea-decisions
description: Generate or view a Decision Register by aggregating all Appendix A3 decision rows from across all artifacts in the active engagement. Supports filtering by audience, owner, domain, authority, cost, impact, risk, subject, status, or source artifact.
---

You are executing the `/ea-decisions` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

The Decision Register aggregates all `Appendix A3 — Decision Log` rows from every artifact in the active engagement into a single cross-artifact view. It is tailorable to any audience, decision maker, domain, or status filter.

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
| `--audience` | `executive` / `architect` / `business` / `technical` | Preset filter combination (see Audience Profiles below) |
| `--owner "name"` | Any string | Case-insensitive partial match on the Owner column |
| `--domain` | `business` / `data` / `app` / `tech` / `cross` | Filter by Domain column |
| `--authority` | `strategic` / `tactical` / `operational` | Filter by Authority column |
| `--cost` | `high` / `med` / `low` / `tbd` | Filter by Cost column |
| `--impact` | `high` / `med` / `low` / `tbd` | Filter by Impact column |
| `--risk` | `high` / `med` / `low` / `tbd` | Filter by Risk column |
| `--subject "tag"` | Any string | Case-insensitive partial match on the Subject column |
| `--status` | `open` / `verified` / `all` | `open` = Provisional + Awaiting Verification + Returned; `verified` = Verified + Voted + Fiat; `all` = all states |
| `--artifact "name"` | Artifact name or partial | Show only decisions from matching artifact |

**Audience Profiles (preset filter combinations):**

| Audience | Filters Applied | Sections Rendered |
|---|---|---|
| `executive` | Authority = Strategic; Impact = High | Open Decisions, By Authority (Strategic only), By Impact (High only) |
| `architect` | None (all) | Full register — all sections |
| `business` | Domain = Business or Cross | Open Decisions, By Domain (Business + Cross), By Impact |
| `technical` | Domain = Application or Technology | Open Decisions, By Domain (App + Tech), By Cost, By Risk |

If `--audience` is combined with other flags, the explicit flags further narrow the audience preset (intersection, not union).

If no arguments given, default to `generate` mode with no filters and audience = All.

---

## Mode: `status`

Invoked as: `/ea-decisions status`

1. Scan A3 tables (same as generate, below).
2. Output an inline summary table — **do not write any file**:

```
Decision Register — {engagement name}
══════════════════════════════════════════
Total: {N}  |  Open: {N}  |  Verified: {N}  |  Voted: {N}  |  Fiat: {N}  |  Returned: {N}

By Authority:   Strategic {N}  |  Tactical {N}  |  Operational {N}
By Domain:      Business {N}  |  Data {N}  |  App {N}  |  Tech {N}  |  Cross {N}
Open owners:    {name} ({role}) ×{N}  |  {name} ×{N}  |  Unassigned ×{N}
Source files:   {N} artifacts scanned, {N} had A3 rows
```

3. Ask: "Run `/ea-decisions` to generate the full register, or `/ea-decisions --audience executive` for an executive view."

---

## Mode: `generate` (default)

### Step 3 — Scan Artifacts for A3 Tables

1. List all files in `EA-projects/{slug}/artifacts/` matching `*.md` (exclude `*.review.md` and `decision-register-*.md`).
2. For each file, read its content and search for a section matching `## Appendix A3` or `### Appendix A3 — Decision Log`.
3. Parse each table row (skip header rows and placeholder rows containing `*(no decisions recorded)*`).
4. Collect into a unified decision list with an added `sourceArtifact` field (the artifact file name, prettified).
5. Count: total artifacts scanned, artifacts with A3 rows, total rows collected.

**Parsing rules:**
- Column order: Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date
- If a row has fewer columns than expected (legacy format), populate missing fields as `—`
- Skip rows where Item is empty or starts with `*(`

### Step 4 — Apply Filters

Apply any flags parsed in Step 2 to the unified decision list. For partial-match flags (`--owner`, `--subject`, `--artifact`), use case-insensitive substring matching.

If filtering results in zero rows, output: "No decisions match the applied filters." followed by the filter summary, then stop (do not write a file).

### Step 5 — Render the Decision Register

Populate the `decision-register.md` template with the filtered data:

- Omit any section whose subsection table would be empty after filtering (do not render empty subsections)
- Populate the Summary table counts from the filtered dataset
- If `--audience` was set to a preset, note the preset name in the frontmatter `audience:` field
- Record applied filters in `filters:` frontmatter field (e.g. `authority=strategic, impact=high`)
- Set `generated:` to today's date
- The **Full Decision Index** always shows all rows in the filtered set regardless of audience preset

### Step 6 — Output Format

Ask the user:

> Output as:
> **1.** Markdown (in-chat)
> **2.** Word document (.docx)
> **3.** Summary table only (inline, no file)
>
> Press Enter or type **1** for Markdown.

- **Option 1** — Write to `EA-projects/{slug}/artifacts/decision-register-{YYYY-MM-DD}.md`. Register the artifact in `engagement.json` with `phase: "All"`, `status: "Draft"`. If a decision register for today already exists, append `-v2`, `-v3` etc. Display a brief confirmation with counts.
- **Option 2** — Write the `.md` file first (same as Option 1), then load the `ea-generate` skill and export to `.docx`.
- **Option 3** — Output the Summary section and Open Decisions table inline only. Do not write any file.

---

## Edge Cases

| Scenario | Handling |
|---|---|
| Artifact has no A3 section | Skip silently; include in "scanned" count but not "with A3 rows" count |
| A3 row missing classification fields (legacy) | Include in register with missing fields shown as `—`; flag in Summary: "N rows with missing classification fields" |
| Multiple decision registers already exist | Each is dated/versioned; all listed in `engagement.json`; `/ea-decisions status` uses latest |
| Filter returns zero results | Show "No decisions match the applied filters." with filter summary; do not write a file |
| Owner partial match returns multiple owners | Show all matching owners; include in results |
| `--audience` combined with conflicting flags | Apply intersection; note in filter summary: "executive preset + domain=Data applied" |
