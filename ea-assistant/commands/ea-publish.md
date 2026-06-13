---
name: ea-publish
description: Publish selected EA artifacts as a layered, stakeholder-consumable report — executive brief, per-artifact summaries, and links to full artifacts — or a full consolidated document with --full; --persona <role> scopes the pack to a stakeholder role; --matrices inlines each artifact's linked relationship matrices
argument-hint: "[markdown|word|both] [--full | --executive] [--persona <role>] [--matrices]"
allowed-tools: [Read, Write, Bash]
---

Publish selected artifacts for the active engagement as a stakeholder-consumable report.

**Modes:**

| Mode | Invocation | Output |
|---|---|---|
| **Layered** (default) | `/ea-publish` | Executive brief + per-artifact summaries + appendix of links to full artifacts. Readable in one sitting; full detail one click away. |
| **Full** | `/ea-publish --full` | Single consolidated document embedding the full text of every selected artifact. Use for archival or contractual submission, not stakeholder reading. |
| **Executive** | `/ea-publish --executive` | Executive Architecture Pack — executive summaries and first diagrams only. |

**`--persona <role>` modifier** (combines with any mode above): scopes the pack to a stakeholder role from `skills/ea-engagement-lifecycle/references/persona-registry.md`. Resolve `<role>` against each persona's Key/Aliases (case-insensitive); if no match, list available personas and stop. The persona's **Audience** set pre-filters the artifact selection (Step 1) and its **Report bundle** is pre-ticked; the output is titled "{Persona} Pack". The user can still adjust the selection. Default layered mode applies unless `--full`/`--executive` is also given.

Every mode also writes/refreshes a stakeholder reading guide at `artifacts/index.md` (Step 6b).

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

### Step 1: List Available Artifacts

**If `--persona <role>` was passed** (or `defaultPersona:` is set in `.claude/rules/ea-local-config.md`): read the persona registry, resolve the role, and read each artifact's `taxonomy.audience` frontmatter. Pre-select artifacts whose `audience` is in the persona's **Audience** set or `All`; show the others in the list but un-ticked. Note at the top: "Scoped to {Persona} — audience: {tags}. Pre-selected {N} artifacts; adjust as needed." Then pre-tick the persona's **Report bundle** items where they correspond to generatable artifacts.

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

### Step 2c: Detail File Inclusion

After the artifact selection is confirmed, collect all detail files linked from the selected artifacts:
- Glob `EA-projects/{slug}/artifacts/details/*.md`
- Cross-check each file's `parentArtifact` frontmatter against the selected artifact list

If any detail files are found for the selected artifacts, ask:

```
Include item detail files in the published document?

  {N} detail file(s) found across the selected artifacts:
    G-001 — Reduce operational costs (Goal · Architecture Vision)
    WP-003 — CRM Platform Replacement (Work Package · Architecture Roadmap)
    ...

Options:
  (y) Inline — embed detail content after the relevant table section in each artifact
  (a) Appendix only — add a "Supplementary Item Detail" appendix at the end of the document
  (n) Exclude — do not include detail files (default)
```

- **Inline:** For each selected artifact, insert each linked detail file's content as a collapsible or indented subsection immediately after the table row it belongs to. Use a clear heading: `#### {ID} — {title} (Item Detail)`.
- **Appendix only:** Append a new top-level section at the end of the consolidated document: `## Supplementary Item Detail` — one subsection per detail file ordered by ID.
- **Exclude:** Skip detail files entirely (backward-compatible default).

If no detail files exist for the selected artifacts, skip this step silently.

### Step 2d: Matrix Inclusion

Relationship matrices are standalone artifacts (`{key}-matrix.md`), not embedded in the domain documents. By default they are **not** inlined and the author-facing `## Related Matrices` pointer is stripped (see Step "Each Artifact Section"). Offer to inline them:

For each selected artifact, resolve its linked matrices: read `skills/ea-artifact-templates/references/matrix-catalogue.md`, take the matrix keys whose **Folder** is the artifact's phase folder plus any keys named in the artifact's `## Related Matrices` pointer, and keep those where `{folder}/{key}-matrix.md` exists with a **populated** grid (≥1 non-placeholder data row).

If `--matrices` was passed, include all of them without prompting. Otherwise, if any populated matrices were found, ask:

```
Include linked relationship matrices in the published document?

  {N} populated matrix/matrices found across the selected artifacts:
    Actor / Role Matrix            (Business Architecture · phase-b)
    Application / Data Matrix       (Data Architecture · phase-c-data)
    ...

Options:
  (y) Inline — embed each matrix grid after its parent artifact, under a "Related Matrices" heading
  (a) Appendix only — add a "Relationship Matrices" appendix at the end of the document
  (n) Exclude — do not include matrices (default)
```

- **Inline:** after each artifact's content, add `### Related Matrices` with each matrix as a `#### {Matrix Name}` subsection (grid + any populated Observations). Strip each matrix file's own frontmatter, `<details>` blocks, and comments first.
- **Appendix only:** append a top-level `## Relationship Matrices` section ordered by phase then matrix name.
- **Exclude:** default; matrices are not inlined.

If no populated matrices exist for the selected artifacts, skip this step silently.

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

**Note on generation tools:** `/ea-publish` uses **pandoc** to convert the consolidated Markdown report to DOCX — this is appropriate for a flat narrative document. Individual artifact Word files (generated by `/ea-generate`) use the **python-docx scripts** (`generate-docx.py`, `generate-pptx.py`) which provide richer structured formatting. Do not use pandoc for individual artifacts.

### Step 4: Derive Document-Level Status

Compute the overall document status from the included artifacts:

| Included artifact statuses         | Document status         |
|------------------------------------|-------------------------|
| All Approved                       | `Approved`              |
| All Draft                          | `Draft`                 |
| Mix of Approved + anything else    | `Mixed — see artifact status table` |
| Any Needs Revision                 | `Mixed — contains sections requiring revision` |

### Step 5L: Build Layered Report (default mode)

Skip this step if `--full` or `--executive` was given.

Assemble a three-layer document — summary first, detail by reference:

```markdown
# {Engagement Name} — Architecture Report

{Cover page table — same format as Step 5}

## Artifact Status Summary
{Same table and warnings as Step 5}

---

## 1. Executive Brief

{3–5 pages maximum. Synthesize — do not concatenate:}
- Situation and strategic intent (from Architecture Vision §Strategic Intent or its Executive Summary)
- Top drivers and goals (from direction register — top 5–7 by priority, one line each)
- Key decisions made (Strategic-authority A3 rows + Completed ADRs — one line each with ID)
- Top risks and open issues (Critical/High only — one line each with ID)
- Roadmap headline (waves and timeline from Architecture Roadmap, if present)

---

## 2. Artifact Summaries

{One subsection per selected artifact, in ADM order, 1–2 pages each:}

### {Artifact Name}
> **Phase {phase}  ·  {status badge}  ·  Last modified: {date}**

{The artifact's `## Executive Summary` section. If absent, synthesize a 3–5 paragraph summary from the artifact's main sections — do not embed the full artifact. If `diagrams[]` is non-empty, include the first diagram.}

**Full artifact:** [{relative path}]({relative path})

---

## 3. Appendix — Full Artifact Index

| Artifact | Phase | Status | File |
|---|---|---|---|
{One row per selected artifact linking to its source file. Add rows for key registers (risk, decision, requirements, gap) whether or not selected, so readers can reach them.}
```

Rules:
- **Never embed full artifact text in layered mode** — that is what `--full` is for.
- Detail files (Step 2c) are always excluded in layered mode.
- Apply the link-rewrite table from Step 5 to summary content (links to included artifacts point at their summary anchors; links to excluded artifacts keep display text with a relative file link).

Then continue at Step 5b (Readability Pass).

### Step 5: Build Consolidated Document (`--full` mode only)

Assemble included artifacts in standard TOGAF ADM order (skip any not selected):

1. Cover page
2. Artifact Status Summary table
3. Table of Contents (selected artifacts only)
4. Artifact sections (in ADM order)
5. Appendices

**ADM order for sorting:**
Prelim → Requirements → A → B → C-Data → C-App → D → E → F → G → H

#### Table of Contents

Generate the ToC immediately after the Artifact Status Summary table and before the first artifact section. Use this exact format:

```markdown
## Table of Contents

- [Artifact Status Summary](#artifact-status-summary)
- [Architecture Principles](#architecture-principles)
- [Architecture Vision](#architecture-vision)
- [Business Architecture](#business-architecture)
```

**Rules:**

1. First entry is always `[Artifact Status Summary](#artifact-status-summary)`.
2. One entry per selected artifact, in ADM order (same order as document body).
3. If appendices are present, add a final entry: `[Appendices](#appendices)`.
4. Do NOT include the cover page or Table of Contents itself as entries.

**Anchor derivation** — apply to every artifact display name to produce the link target:
- Take the artifact's display name exactly as it appears in the `## {Artifact Name}` heading
- Lowercase all characters
- Replace every space with a hyphen `-`
- Remove all characters that are not alphanumeric or hyphens (strip punctuation, special characters, emoji)
- Collapse consecutive hyphens into one

Examples:
| Heading | Anchor |
|---|---|
| `## Architecture Vision` | `#architecture-vision` |
| `## Business Architecture` | `#business-architecture` |
| `## Phase C — Data Architecture` | `#phase-c--data-architecture` |
| `## Requirements Register` | `#requirements-register` |
| `## Artifact Status Summary` | `#artifact-status-summary` |

The `## {Artifact Name}` heading in the document body **must use the same display name as the entry in the ToC** — do not add phase labels, status badges, or numbering to the `##` heading line itself (these go in the `> **Phase · status · date**` blockquote on the line immediately after).

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

**Strip plugin scaffolding before insertion (all modes):** remove all HTML comments (`<!-- GUIDANCE: ... -->` and any other `<!-- ... -->` blocks) **and all author-only `<details>...</details>` blocks** (Compliance Status, 📋 Guidance, 💡 Practitioner Tip, 📊 Scorecard, and any other collapsible) from artifact content, plus the `## Artifact Working Notes` section, and the author-facing **`## Related Matrices`** pointer blockquote (it references `/ea-matrix` — when matrices are inlined per Step 2d, the real grids replace it; otherwise it is dropped). Published output must contain no authoring guidance, compliance scaffolding, scores, or tool-command pointers.

Before inserting each artifact's content, rewrite its links for the consolidated document context:

| Link type | Example | Action |
|---|---|---|
| External URL | `[TOGAF](https://...)` | Keep as-is — pandoc preserves clickable hyperlinks |
| Same-document section anchor | `[Goals](#3-goals)` | Keep as-is |
| Relative link to an **included** artifact | `[Arch Vision](../phase-a/architecture-vision.md)` | Rewrite to internal anchor: `[Arch Vision](#architecture-vision)` |
| Relative link to an **included** artifact + section | `[Goals](../phase-a/architecture-vision.md#3-goals)` | Rewrite to section anchor: `[Goals](#3-goals)` |
| Relative link to an artifact **not included** | `[Tech Architecture](../phase-d/technology-architecture.md)` | Strip link, keep display text: `Technology Architecture` |
| Relative image | `![diagram](../../diagrams/context.png)` | Resolve to absolute path |
| Wikilink to an **included** artifact | `[[architecture-vision\|Arch Vision]]` | Rewrite to internal anchor: `[Arch Vision](#architecture-vision)` |
| Wikilink to anything else | `[[G-001]]`, `[[tech-radar\|Radar]]` | Strip — keep alias text, or the target if no alias: `G-001`, `Radar` |
| Wikilink embed | `![[context.png]]` | Treat as the image at `diagrams/context.png` — resolve to absolute path |

Anchor derivation: the consolidated document uses `## {Artifact Name}` as each artifact's heading. The corresponding anchor is the heading text lowercased with spaces replaced by hyphens (e.g., `## Architecture Vision` → `#architecture-vision`).

Open each artifact section with a status header:

```markdown
---

## {Artifact Name}

> **Phase {phase}  ·  {status badge}  ·  Last modified: {lastModified date}**

{artifact content with links rewritten per table above}
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

### Step 5b: Readability Pass

Load `skills/ea-artifact-templates/references/publish-quality.md`.

Scan the assembled document against all rules in that file. Produce a readability report:

```
Readability Pass
────────────────────────────────────────
Tables too wide (>8 cols):     {N}  [list artifact/section]
Tables too long (>10 rows):    {N}  [list]
Header-only tables:            {N}  [list]
Placeholder text found:        {N}  [list]
Broken image paths:            {N}  [list]
Sections missing narrative:    {N}  [list]
Terminology inconsistencies:   {N}  [list]
```

If any **Blocking** issues exist (placeholder text, `TBD` / `TODO` markers, `⚠️ Not answered` fields, broken image paths):
- List each occurrence explicitly (artifact section + text snippet).
- Ask: "These issues should be resolved before publishing. Choose an option:"
  - **(f) Fix now** — walk through each issue interactively; patch the source artifact and re-assemble the affected section.
  - **(m) Mark and continue** — insert `<!-- ⚠️ PUBLISH QUALITY ISSUE: {description} -->` inline at each occurrence; add a `## Publication Quality Notes` section immediately after the cover page listing all issues with locations.
  - **(a) Abort** — stop; do not write output files.

Non-blocking issues (Warning, Advisory): Add each to the `## Publication Quality Notes` section without blocking. If there are no blocking issues and at least one non-blocking issue, create the Publication Quality Notes section automatically.

If all checks pass, continue silently.

### Step 5c: Rewrite Pass

Ask the user:

```
Run a readability rewrite? This will:
  - Add brief narrative introductions to sections that open directly with a table
  - Add transition sentences between back-to-back sections with no prose
  - Standardise terminology flagged as inconsistent

  (y) Yes — apply rewrite   (n) No — skip   (p) Preview first
```

- **(y) Yes:** Apply the rewrite to the assembled document in-memory. Each inserted passage is tagged `<!-- ai-inserted -->` so it is identifiable in the source.
- **(p) Preview:** Show the first 3 proposed insertions with before/after context; ask to confirm before applying all.
- **(n) No:** Skip; proceed to Step 6.

**Executive Mode (`--executive`):** Step 5b runs in reduced scope — blocking checks only (placeholder text and broken image paths; skip narrative and terminology checks). Step 5c is skipped entirely.

---

### Step 6: Write Output

- Layered mode (default) — Markdown: `artifacts/architecture-report-{YYYY-MM-DD}.md`, Word: `artifacts/architecture-report-{YYYY-MM-DD}.docx`
- Full mode (`--full`) — Markdown: `artifacts/consolidated-report-{YYYY-MM-DD}.md`, Word: `artifacts/consolidated-report-{YYYY-MM-DD}.docx`

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

### Step 6b: Write the Stakeholder Reading Guide

After writing the report (every mode), write/overwrite `EA-projects/{slug}/artifacts/index.md`:

```markdown
# {Engagement Name} — Start Here

_Updated: {YYYY-MM-DD} by /ea-publish_

**New to this engagement? Read in this order:**

1. **[Latest published report]({report filename from Step 6})** — the layered architecture report ({date})
2. **Executive summary** — [{path}] (if an executive-summary artifact exists)
3. **Architecture Vision** — [{path}] (the why and the target)
4. **Current phase artifacts** — {links to artifacts of engagement.json → currentPhase}

**Registers (current state):**

| Register | File |
|---|---|
| Risks | [risk-register.md](cross-cutting/operations/risk-register.md) |
| Decisions | [decision-register.md](cross-cutting/governance/decision-register.md) |
| Requirements | [{path}] |
| Gaps | [gap-register.md](cross-cutting/gap-register.md) |

{Only list registers whose files exist.}

**Everything else:** [Cross-cutting index](cross-cutting/cross-cutting-index.md) · [Diagrams](../diagrams/) · full artifact list in the report appendix.
```

Keep the guide to one screen — it is a map, not a summary.

### Step 7: Confirm

Report:
- Output file path(s) and sizes
- Number of artifacts included
- Any artifacts excluded and why (not created, deselected, or opted out)
- If opted-out artifacts were excluded: "⊘ {N} artifact(s) opted out and excluded: {names}. Run `/ea-open` to review or reverse opt-outs."
- If opted-out questions appear in included artifacts: "⊘ {N} question(s) opted out within included artifacts — marked inline."
- Overall document status

---

### Executive Mode (`--executive` flag)

Triggered by `/ea-publish --executive` or `/ea-publish --executive word`.

Produces an **Executive Architecture Pack** — one section per artifact containing only its Executive Summary and first diagram. Intended for sponsor briefings, board updates, and programme steering committees.

**Steps 1–2 run as normal** (list and select artifacts), with this variation:
- Default selection prompt: "Select artifacts for the Executive Architecture Pack (press Enter for all created artifacts)."

**Step 2b (compliance check) is skipped.**

**Step 3 (format):** Default is `both` (markdown + docx). Override with `word` or `markdown` argument.

**Step 4 (document status):** Computed the same way — use the highest-severity status across selected artifacts.

**Assembly — replaces Step 5:**

Build the document using this structure:

```markdown
# {Engagement Name} — Executive Architecture Pack

| Field        | Value                     |
|--------------|---------------------------|
| Organisation | {organisation}            |
| Sponsor      | {sponsor}                 |
| Published    | {today YYYY-MM-DD}        |
| Status       | {derived document status} |
| Scope        | {N} artifacts summarised  |

---

## Artifact Summaries

---

### {Artifact Name}

> **Phase {phase}  ·  {status badge}  ·  Last modified: {date}**

{content of the ## Executive Summary section from this artifact}

{If the artifact frontmatter diagrams[] is non-empty: include the first entry as an image reference}

---
```

For each artifact:
- Extract the content of the `## Executive Summary` section (everything between the `## Executive Summary` heading and the next `##` heading or `---`).
- If no `## Executive Summary` section exists: substitute `*No executive summary available for this artifact. Run \`/ea-artifact summary refresh {artifact-name}\` to add one.*`
- Include diagrams: if `diagrams[]` in frontmatter is non-empty, resolve the first path to an absolute path and include as `![{artifact-name} diagram]({absolute-path})`.

**Step 6 — Write output:**
- Markdown: `artifacts/executive-pack-{YYYY-MM-DD}.md`
- Word: `artifacts/executive-pack-{YYYY-MM-DD}.docx` (using same pandoc step as Step 6)

**Step 7 — Confirm:**
```
Executive Architecture Pack published.
  Artifacts summarised:  {N}
  Missing summaries:     {N} ({names, if any})
  Output: artifacts/executive-pack-{date}.md
          artifacts/executive-pack-{date}.docx
```
