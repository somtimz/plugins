---
name: ea-publish
description: Publish selected EA artifacts into a single consolidated architecture document, with per-artifact status and date reflected throughout
argument-hint: "[markdown|word|both]"
allowed-tools: [Read, Write, Bash]
---

Publish selected artifacts for the active engagement into a single consolidated document.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

### Step 1: List Available Artifacts

Read `engagement.json` and present all artifacts as a numbered selection list. Show status, phase, and last modified date for each:

```
Available artifacts for: {Engagement Name}

  #  Artifact                        Phase   Status          Last Modified
  ─────────────────────────────────────────────────────────────────────────
  1  Architecture Principles         Prelim  ✅ Approved      2026-03-10
  2  Requirements Register           Req     ✅ Approved      2026-03-12
  3  Architecture Vision             A       ✅ Approved      2026-03-14
  4  Stakeholder Map                 A       🔄 In Review     2026-03-15
  5  Business Architecture           B       ✏️  Draft         2026-03-18
  6  Technology Architecture         D       ✏️  Draft         2026-03-19
     Application Architecture        C       ⬜ Not created   —
```

Status legend:
- ✅ Approved — signed off, ready for publication
- 🔄 In Review / Needs Revision — work in progress
- ✏️  Draft — early stage, not yet reviewed
- ⬜ Not created — excluded automatically

> **Tip:** To export a single artifact, use `/ea-generate [artifact-name] [format]` instead.

### Step 2: Prompt for Selection

Ask the user:

```
Which artifacts do you want to include?
Enter numbers separated by commas (e.g. 1,2,3), a range (e.g. 1-4), or "all" for all created artifacts.
```

- Accept: individual numbers, comma-separated, ranges (e.g. `2-5`), or `all`
- Only include artifacts that have been created (exclude "Not created" entries regardless of selection)
- If the selection includes Draft or In Review artifacts, warn: "⚠️ Your selection includes {N} artifact(s) that are not yet Approved. They will be included and marked accordingly."
- Confirm the final selection before proceeding

### Step 3: Determine Output Format

- If argument is `markdown` — Markdown only
- If argument is `word` — Word (.docx) only
- If argument is `both` or no argument — both formats
- If pandoc is not available and Word is requested, warn and offer Markdown only

### Step 4: Derive Document-Level Status

Compute the overall document status from the included artifacts:

| Included artifact statuses         | Document status         |
|------------------------------------|-------------------------|
| All Approved                       | `Approved`              |
| All Draft                          | `Draft`                 |
| Mix of Approved + anything else    | `Mixed — see artifact status table` |
| Any Needs Revision                 | `Mixed — contains sections requiring revision` |

### Step 5: Build Consolidated Document

Assemble included artifacts in standard TOGAF ADM order (skip any not selected):

1. Cover page
2. Artifact Status Summary table
3. Table of Contents (selected artifacts only)
4. Artifact sections (in ADM order)
5. Appendices

**ADM order for sorting:**
Prelim → Requirements → A → B → C-Data → C-App → D → E → F → G → H

#### Cover Page

```markdown
# {Engagement Name} — Architecture Document

| Field          | Value                           |
|----------------|---------------------------------|
| Organisation   | {organisation}                  |
| Sponsor        | {sponsor}                       |
| Version        | 1.0                             |
| Published      | {today's date YYYY-MM-DD}       |
| Document Status| {derived status from Step 4}    |
| Scope          | {N of M artifacts included}     |
```

#### Artifact Status Summary Table

Include immediately after the cover page metadata, before the Table of Contents:

```markdown
## Artifact Status Summary

| # | Artifact                  | Phase  | Status       | Last Modified |
|---|---------------------------|--------|--------------|---------------|
| 1 | Architecture Principles   | Prelim | ✅ Approved   | 2026-03-10    |
| 2 | Requirements Register     | Req    | ✅ Approved   | 2026-03-12    |
| 3 | Architecture Vision       | A      | ✅ Approved   | 2026-03-14    |
| 4 | Business Architecture     | B      | ✏️ Draft       | 2026-03-18    |
```

If any artifact is not Approved, add this note below the table:
> ⚠️ This document contains sections that have not been approved. Review each section's status header before distributing.

#### Each Artifact Section

Open each artifact section with a status header showing its individual status and date:

```markdown
---

## {Artifact Name}

> **Phase {phase}  ·  {status badge}  ·  Last modified: {lastModified date}**

{artifact content as-is — do NOT alter}
```

Status badges for section headers:
- `✅ Approved`
- `🔄 In Review`
- `⚠️ Needs Revision`
- `✏️ Draft`

If the artifact has open review comments (in its `.review.md` file), append:

```markdown
### Open Review Comments

{review comments content}
```

### Step 6: Write Output

- Markdown: `artifacts/consolidated-report-{YYYY-MM-DD}.md`
- Word: `artifacts/consolidated-report-{YYYY-MM-DD}.docx`

```bash
pandoc artifacts/consolidated-report-{date}.md \
  --reference-doc=templates/consolidated-report.docx \
  -o artifacts/consolidated-report-{date}.docx
```

If a `.docx` reference template does not exist, run pandoc without `--reference-doc`.

### Step 7: Confirm

Report:
- Output file path(s) and sizes
- Number of artifacts included
- Any artifacts excluded and why (not created, or deselected)
- Overall document status
