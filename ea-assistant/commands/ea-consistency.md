---
name: ea-consistency
description: Focused consistency check — cross-artifact contradictions, ID reference validation, and within-artifact section consistency. Faster and more targeted than /ea-engage-review.
argument-hint: "[artifact <id>] [--ids] [--report]"
allowed-tools: [Read, Bash, Glob, Grep]
---

You are executing the `/ea-consistency` command.

## Overview

Runs a focused consistency check on the active engagement. Unlike `/ea-engage-review`, this command does not cover governance, quality scores, or alignment — it checks only consistency and ID integrity. All modes are **read-only**: no files are modified.

**Modes:**

| Args | Mode | What it checks |
|---|---|---|
| (none) | Full | Cross-artifact contradictions, naming consistency, requirement traceability, phase alignment, ID reference validation, detail file link integrity, detail/A4 content sync |
| `artifact <id>` | Artifact | Within-artifact section consistency + ID refs scoped to that file |
| `--ids` | IDs only | Fast scan — ID definition registry, broken references, orphaned IDs |
| `--details` | Detail links + sync | Fast scan — broken detail file links, frontmatter mismatches, cross-artifact link consistency, detail/A4 content sync |
| `--quality` | Quality | Readability + content completeness scan across all artifacts |
| `--report` (added to any mode) | Report | Suppresses interactive menu; prints full report inline |

---

## Step 1 — Resolve Active Engagement

> Resolve the active engagement per `skills/ea-engagement-lifecycle/references/engagement-resolution.md`.

---

## Step 2 — Mode Dispatch

Parse the arguments passed to this command and route to the appropriate mode below.

---

### Full Mode (no args)

Before dispatching to the agent, load full engagement context using **Scope C** from `skills/ea-engagement-lifecycle/references/context-loading.md`. Announce the loaded context.

Invoke the `ea-consistency-checker` agent. Pass the engagement slug, artifact root path, and all loaded file paths (notes and research). Instruct the agent to run all steps including the ID reference validation step (step 5b), and to additionally check:

- Whether artifact claims are consistent with interview notes for that phase (e.g. a goal stated in the artifact that contradicts what was captured in an interview session)
- Whether brainstorm notes raised concerns that remain unaddressed in any artifact
- Whether research items in `ResearchAndReferences/` contain findings that contradict artifact content

The agent must report these in a separate section titled **"Notes & Research Contradictions"** at the end of the full report.

After the agent produces its report, unless `--report` was specified, offer:

```
What would you like to do?

  1. View full ID reference report
  2. View detail file link report    →  /ea-consistency --details
  3. Deep-review an artifact         →  /ea-grill [artifact]
  4. Full engagement review          →  /ea-engage-review
  Enter a number or press Enter to close.
```

---

### Artifact Mode (`artifact <id>`)

**1. Locate the artifact**

Use Glob to find `EA-projects/{slug}/artifacts/**/{id}.md`. If not found, list available artifact IDs and ask the user to confirm.

**1b. Load artifact-scoped context**

Load context using **Scope A** from `skills/ea-engagement-lifecycle/references/context-loading.md`. Use the loaded notes and research in steps 2 and 3 below to extend the consistency check beyond artifact-only content.

**2. Within-artifact section consistency**

Read the artifact. For each top-level section heading (`## ...`), collect all ID tokens matching `(G|OBJ|DRV|STR|ISS|PRB|MET|REQ|RIS|ADR|WP|GAP|CON)-\d{3}` and the label or description text immediately associated with each token (the same table row, or the inline text surrounding it).

Build a map: `{ id → [ { section, label_text } ] }`

Flag any ID that appears in two or more sections with **differing label text**. Example:
```
⚠️  G-001 labelled inconsistently within this artifact:
    §3 Goals:              "Reduce operational costs"
    §14 Strategic Alignment: "Reduce supply chain costs"
    → Standardise the label across all sections
```

**3. ID reference validation (scoped to this artifact)**

Scan all other artifacts in `EA-projects/{slug}/artifacts/**/*.md` to build the engagement-wide ID definition registry (see step 5b in `ea-consistency-checker` for the definition rules).

Then check every ID referenced in the current artifact against the registry. Report any broken references (ID used in this artifact but not defined anywhere in the engagement).

**3b. Notes and research consistency (artifact mode)**

Using the loaded Scope A context:
- **Interview notes:** For each interview note matching this artifact, check whether any captured answer contradicts the current artifact field value. Flag divergence: `⚠️ Field '{field}' says '{artifact value}' — interview {date} captured '{note value}'`
- **Brainstorm notes:** Check whether any concern or assumption from the phase brainstorm notes is addressed somewhere in the artifact. Flag unaddressed concerns: `ℹ️ Brainstorm session N noted: '{concern}' — no corresponding artifact content found`
- **Research items:** For each loaded research item, check whether any finding contradicts a claim in the artifact. Flag: `⚠️ Research '{title}' states '{finding}' — conflicts with artifact §{section}`

**4. Output**

```
Consistency check: {artifact-name}
──────────────────────────────────
Within-artifact label inconsistencies: {N}
Broken ID references: {N}
Notes & research contradictions: {N}

[findings listed]

✅ No further issues found.
```

Unless `--report`, offer:
```
  1. Run a full engagement consistency check  →  /ea-consistency
  2. Deep-review this artifact                →  /ea-grill {id}
  3. Continue
```

---

### Detail Link Integrity Check (`--details` or included in Full Mode)

**Check D — Detail file link integrity**

Scan all artifact files in `EA-projects/{slug}/artifacts/**/*.md` (excluding `/notes/`) for detail file links in all forms per `skills/ea-artifact-templates/references/link-conventions.md`: `[→](../details/{ID}.md)`, `[{ID}](../details/{ID}.md)`, `[[{ID}]]`, and `[[{ID}|...]]`.

For each link found:

1. **Verify target file exists:** Check whether `EA-projects/{slug}/artifacts/details/{ID}.md` exists.
   - If missing: report as a broken link: `⚠️ [artifact path] — link to ../details/{ID}.md but file does not exist`

2. **Verify `item` frontmatter matches filename:** For each detail file that does exist, read its frontmatter and check that `item: {ID}` matches the filename `{ID}.md`.
   - If mismatch: report: `⚠️ artifacts/details/{ID}.md — item frontmatter says '{actual}' but filename is '{ID}'`

3. **Check cross-artifact consistency:** If the same ID is linked from multiple artifacts, verify all links point to the same canonical file `../details/{ID}.md`.
   - If any artifact uses a different relative path or no link while another does: report: `ℹ️ {ID} is linked in {N} artifacts — verify the Details column is consistent across all references`

Report format:

```
Check D — Detail File Link Integrity
──────────────────────────────────────
Detail files found: {N}
Broken links: {N}
Frontmatter mismatches: {N}
Cross-artifact inconsistencies: {N}

[findings listed]

✅ All detail file links valid.
```

This check runs automatically in **Full Mode** and can be run in isolation with `--details`.

---

### Detail File Content Sync Check (`--details` or included in Full Mode)

**Check E — Detail File Content Sync**

For each detail file in `EA-projects/{slug}/artifacts/details/`:

1. **Extract concern references:** Scan the **Concerns** section for `CON-NNN` patterns. Scan the **Issues** section for `ISS-NNN` and `PRB-NNN` patterns.

2. **Verify concerns exist in parent A4:**
   - Read the parent artifact (from `parentArtifact` frontmatter).
   - For each `CON-NNN` in the detail file Concerns section: check whether a matching row exists in `## Appendix A4`. If not: report `⚠️ Sync gap: CON-NNN in {ID}.md Concerns but not in {parent artifact} A4 table — run ea-detail sync {ID}`.

3. **Verify A4 concerns are in detail file:**
   - For each A4 row whose text or subject references the item's ID: check whether the detail file's Concerns section contains a `CON-NNN` reference for that row. If not: report `⚠️ Sync gap: CON-NNN in {parent artifact} A4 is associated with {ID} but not referenced in {ID}.md Concerns section`.

Report format:

```
Check E — Detail File Content Sync
───────────────────────────────────
Detail files scanned: {N}
Detail → A4 gaps (concerns in detail file missing from A4): {N}
A4 → Detail gaps (A4 concerns associated with item but missing from detail file): {N}

[findings listed]

✅ All detail file content is in sync with parent A4 tables.
```

Offer for each gap: "Run `ea-detail sync {ID}` to resolve."

This check runs automatically in **Full Mode** and as part of the `--details` mode (alongside Check D).

---

### IDs-Only Mode (`--ids`)

Fast path — skips all entity/contradiction/traceability logic.

**1. Build ID definition registry**

Scan every `.md` file in `EA-projects/{slug}/artifacts/**/*.md`. An ID is **defined** when it appears as:
- First cell of a Markdown table row: `| G-001 | ...`
- A heading that begins with the ID token: `## G-001 — label`

Pattern: `(G|OBJ|DRV|STR|ISS|PRB|MET|REQ|RIS|ADR|WP|GAP|CON)-\d{3}`

**2. Scan for references**

Scan every artifact for any occurrence of the pattern. Occurrences that are NOT the definition source are references.

**3. Report**

```
ID Reference Scan — {engagement name}
──────────────────────────────────────
IDs defined:    {N}
IDs referenced: {N}

🔴 Broken references ({N})
| Artifact | Section | ID | Context |
|---|---|---|---|
| phase-a/architecture-vision.md | §14 Key Risks | RIS-007 | "linked to RIS-007" |

ℹ️  Orphaned IDs — defined but never referenced elsewhere ({N})
| Artifact | ID |
|---|---|
| phase-b/business-architecture.md | GAP-003 |

✅ All other IDs valid.
```

Unless `--report`, offer:
```
  1. Run full consistency check  →  /ea-consistency
  2. Continue
```

---

### Quality Mode (`--quality`)

Load `skills/ea-artifact-templates/references/publish-quality.md`.

Scan every artifact in `EA-projects/{slug}/artifacts/**/*.md`, excluding `*.review.md`, files in `notes/` subdirectories, and files in `details/`.

Apply all rules from publish-quality.md to each artifact. Aggregate findings:

```
Quality Scan — {engagement name}
──────────────────────────────────────────
Artifacts scanned: {N}
Artifacts with issues: {N}

{Artifact Name}
  ⚠️ Table too wide: §{section} — {N} columns (max 8)
  ⚠️ Placeholder text: §{section} — "{{requirement_statement}}"
  ℹ️ Section opens with table: §{section} — add narrative introduction

✅ {Artifact Name} — no issues found.
```

Severity display:
- `⚠️` — Blocking or Warning findings
- `ℹ️` — Advisory findings
- `✅` — artifact passed all checks

`--quality` can be combined with `--report` to print the full report inline without the interactive menu.

Unless `--report`, offer:
```
  1. Run a full consistency check  →  /ea-consistency
  2. Review an artifact            →  /ea-review {id}
  3. Continue
```
