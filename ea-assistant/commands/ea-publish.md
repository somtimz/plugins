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
- ⊘ Opted out — explicitly excluded by user (included in list but flagged)
- ⬜ Not created — excluded automatically

**Opt-out flagging:** Read `engagement.json` → `optOuts[]`. If any artifact-level opt-outs exist, add them to the selection list with an `⊘ Opted out` marker and a note: `"{reason}"`. They are excluded from the consolidated document by default — the user may choose to include a placeholder section for each. If any question-level opt-outs exist within included artifacts, they appear inline in the artifact content as `⊘ Opted out — {reason}`.

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

### Step 2b: Pre-Publish Compliance Check

For each selected artifact, run a quick compliance scan (the same three-tier check used by artifact load: frontmatter fields, template structure, artifact-specific rules). Present a summary:

```
Pre-publish compliance check:

  #  Artifact                        Compliance
  ─────────────────────────────────────────────────
  1  Architecture Principles         ✅ Compliant
  2  Requirements Register           ⚠️ 2 issues (missing Motivation field on REQ-003, REQ-007)
  3  Architecture Vision             ✅ Compliant
  4  Business Architecture           ⚠️ 1 issue (empty §4 Capability Gaps)
```

If any artifact has compliance issues:
- List the specific issues per artifact
- Ask: "Proceed with publication anyway, or address compliance issues first?"
- If the user proceeds, add a `complianceNote` to the Artifact Status Summary table: `⚠️ Published with known compliance issues — see individual artifact headers`

If all artifacts are compliant, proceed silently to Step 3.

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

If any opt-outs exist (artifact or question level), add:
> ⊘ This document contains opted-out items. Fields or artifacts marked ⊘ were explicitly excluded by the engagement team. See `engagement.json → optOuts[]` for the full audit trail with reasons and timestamps.

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
# Bootstrap: install pandoc if not present
if ! command -v pandoc &>/dev/null; then
  echo "Installing pandoc..."
  if command -v brew &>/dev/null; then
    brew install pandoc
  elif command -v apt-get &>/dev/null; then
    sudo apt-get install -y pandoc
  else
    echo "Cannot auto-install pandoc. Please install it manually: https://pandoc.org/installing.html"
    exit 1
  fi
fi

pandoc artifacts/consolidated-report-{date}.md \
  --reference-doc=templates/consolidated-report.docx \
  -o artifacts/consolidated-report-{date}.docx
```

If a `.docx` reference template does not exist, run pandoc without `--reference-doc`.

### Step 7: Confirm

Report:
- Output file path(s) and sizes
- Number of artifacts included
- Any artifacts excluded and why (not created, deselected, or opted out)
- If opted-out artifacts were excluded: "⊘ {N} artifact(s) opted out and excluded: {names}. Run `/ea-open` to review or reverse opt-outs."
- If opted-out questions appear in included artifacts: "⊘ {N} question(s) opted out within included artifacts — marked inline."
- Overall document status
