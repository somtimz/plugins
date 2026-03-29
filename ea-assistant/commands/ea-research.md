---
name: ea-research
description: Manage research documents, notes, and external links in the ResearchAndReferences folder; apply findings to engagement deliverables
argument-hint: "[add|note|link|list|view <item>|apply [artifact-id]]"
allowed-tools: [Read, Write, Bash, Glob]
---

Manage research inputs for the active engagement and apply them to EA deliverables.

## Overview

The `ResearchAndReferences/` folder is the engagement's library for external context: whitepapers, reference architectures, analyst reports, standards documents, repository links, and ad-hoc research notes. Everything in this folder can be referenced during interviews, artifact creation, and `/ea-grill` reviews.

**Research item types:**
- **Document** — an uploaded or pasted document (stored as `.md` with original content)
- **Note** — a freeform research note or observation written directly in the conversation
- **Link** — a URL with title, summary, and relevance tags

All items are indexed in `ResearchAndReferences/research-index.md`.

---

## Instructions

If no engagement is active in context, display:

```
No engagement is currently open.

Run /ea-open to open an existing engagement first.
```

Then stop.

---

### Mode: list (default when no argument provided)

Display all research items for the active engagement.

Read `ResearchAndReferences/research-index.md`. If it does not exist (legacy engagement), create it with an empty index (see **Index File Format** below) and display:

```
📚 Research & References — {engagement name}
Folder: EA-projects/{slug}/ResearchAndReferences/

No research items yet.

Add research with:
  /ea-research add      — paste or describe a document
  /ea-research note     — write a research note
  /ea-research link     — add a URL reference
```

If items exist, display:

```
📚 Research & References — {engagement name}
Folder: EA-projects/{slug}/ResearchAndReferences/
Items: {N total} ({n} documents, {n} notes, {n} links)

  #  | Type     | Title                              | Added       | Tags
  ---|----------|------------------------------------|-------------|--------------------
  1  | document | Gartner EA Maturity Model 2024     | 2026-03-10  | capability, maturity
  2  | note     | Vendor positioning from RFI         | 2026-03-11  | vendor, app
  3  | link     | TOGAF 10 Reference Library         | 2026-03-12  | togaf, standard

Options:
  1. Add a document  (/ea-research add)
  2. Write a note    (/ea-research note)
  3. Add a link      (/ea-research link)
  4. View an item    (/ea-research view <#>)
  5. Apply to an artifact  (/ea-research apply)
```

---

### Mode: add

Add an uploaded document or pasted content to the research library.

1. Ask:
   ```
   Paste the document content (or describe the document if you cannot paste it directly):
   ```
2. Ask for a **title** (required) and **relevance tags** (optional, comma-separated).
3. Generate a filename slug from the title: lowercase, spaces to hyphens, remove special chars.
4. Write the content to `ResearchAndReferences/{slug}.md` with this frontmatter:

   ```yaml
   ---
   researchType: document
   title: "{title}"
   source: "{source or 'Pasted content'}"
   addedDate: "{ISO 8601 date}"
   tags: [{tag1}, {tag2}]
   ---
   ```

5. Update `research-index.md` (add a row to the Items table).
6. Confirm:
   ```
   ✅ Document added: {title}
      File: ResearchAndReferences/{slug}.md
      Tags: {tags}

   Run /ea-research apply to use this research to inform an artifact.
   ```

---

### Mode: note

Write a research note directly in the conversation.

1. Ask:
   ```
   Research note title:
   ```
2. Ask:
   ```
   Write your research note (observations, findings, vendor notes, anything relevant to the engagement):
   ```
3. Ask for **relevance tags** (optional).
4. Write to `ResearchAndReferences/{slug}.md` with frontmatter:

   ```yaml
   ---
   researchType: note
   title: "{title}"
   addedDate: "{ISO 8601 date}"
   tags: [{tag1}, {tag2}]
   ---
   ```

5. Update `research-index.md`.
6. Confirm with file path and offer to apply immediately.

---

### Mode: link

Add a URL reference with title and summary.

1. Ask:
   ```
   URL:
   Title (short description):
   Summary (what this link contains and why it is relevant):
   Tags (optional, comma-separated):
   ```
2. Write to `ResearchAndReferences/{slug}.md`:

   ```yaml
   ---
   researchType: link
   title: "{title}"
   url: "{url}"
   addedDate: "{ISO 8601 date}"
   tags: [{tag1}, {tag2}]
   ---

   ## Summary

   {summary}

   ## Relevance

   {how this resource relates to the engagement}
   ```

3. Update `research-index.md`.
4. Confirm with title, URL, and offer to apply immediately.

---

### Mode: view \<item\>

Display the full content of a research item.

- Accept `<item>` as either an index number (from `list`) or a filename stem.
- Read the file and display its full content.
- After displaying, offer:
  ```
  Options:
  1. Apply this research to an artifact  (/ea-research apply {slug})
  2. Edit this research item
  3. Delete this research item
  4. Return to list  (/ea-research)
  ```

---

### Mode: apply \[artifact-id\]

Synthesise one or more research items against an engagement artifact and propose revisions.

**Step 1 — Select research items**

If `/ea-research apply` was run without a specific item, display the list and ask:

```
Which research items should inform this synthesis?

  1. Gartner EA Maturity Model 2024   [document]
  2. Vendor positioning from RFI      [note]
  3. TOGAF 10 Reference Library       [link]
  A. All items

Enter numbers (comma-separated) or A for all:
```

**Step 2 — Select target artifact**

If no `artifact-id` argument was provided, list artifacts in the active engagement and ask the user to select one. Show only artifacts that exist on disk.

```
Select the artifact to review against this research:

  1. Architecture Vision        (Phase A)  [Draft]
  2. Business Architecture      (Phase B)  [Draft]
  3. Gap Analysis               (Phase B)  [Approved]
  ...
```

**Step 3 — Load and synthesise**

Read:
- All selected research item files from `ResearchAndReferences/`
- The target artifact file from `artifacts/{artifact-id}.md`

Synthesise: compare the research content against the artifact section by section and identify:
- **Gaps** — information in the research that should be reflected in the artifact but is not
- **Contradictions** — claims in the artifact that the research calls into question
- **Enhancements** — specific additions or revisions the research supports
- **References** — links or citations worth adding to the artifact's reference list or decision log

**Step 4 — Present findings**

Display findings in this format:

```
## Research Synthesis — {artifact name}
Sources: {research item titles}

### Gaps
1. [§{section}] The research highlights {finding} but the artifact does not address it.
   → Suggested addition: "{proposed text}"

### Contradictions
1. [§{section}] Artifact states "{claim}" but {research title} indicates "{counter-evidence}".
   → Suggested revision: "{revised text}"

### Enhancements
1. [§{section}] "{current text}" — can be strengthened with evidence from {research title}.
   → Suggested revision: "{enhanced text}"

### Suggested References
1. Add to Appendix A5 or A3 Notes: "{research title}" — {brief relevance}
```

**Step 5 — Apply revisions**

After showing all findings, ask:

```
Apply findings to {artifact name}?

Walk through each suggestion (y/n/edit per item), or:
  A — apply all automatically
  S — skip all (save findings only)
  Q — quit without saving
```

For `y/n/edit` per item:
- **y** — apply the suggested revision to the artifact
- **n** — skip this revision
- **edit** — ask the user to provide the revised text before applying

For `A` (apply all): apply every suggested revision without prompting per item.

For `S` (skip all): write a synthesis report to `ResearchAndReferences/synthesis-{artifact-id}-{date}.md` without modifying the artifact.

**Step 6 — Update artifact**

After applying at least one revision:
- Bump the artifact's `version` field (patch increment: `0.2` → `0.3`)
- Update `lastModified` to now
- Set `reviewStatus` to `Revised`
- Write updated artifact file

Also write the synthesis report to `ResearchAndReferences/synthesis-{artifact-id}-{date}.md` regardless of whether revisions were applied, so findings are preserved.

**Step 7 — Confirm**

```
✅ Research applied to: {artifact name}
   Revisions applied: {N of M}
   Artifact version: {old} → {new}
   Synthesis report: ResearchAndReferences/synthesis-{artifact-id}-{date}.md

Options:
1. Apply to another artifact
2. View updated artifact  (/ea-artifact view {artifact-id})
3. Return to engagement  (/ea-status)
```

---

## Index File Format

`ResearchAndReferences/research-index.md` tracks all items. Created automatically if missing.

```markdown
---
indexType: research
engagementSlug: {slug}
lastUpdated: {ISO 8601}
---

# Research & References — {engagement name}

| # | Type | Title | File | Added | Tags |
|---|------|-------|------|-------|------|
| 1 | document | Gartner EA Maturity Model 2024 | gartner-ea-maturity-model-2024.md | 2026-03-10 | capability, maturity |
| 2 | note | Vendor positioning from RFI | vendor-positioning-from-rfi.md | 2026-03-11 | vendor, app |
| 3 | link | TOGAF 10 Reference Library | togaf-10-reference-library.md | 2026-03-12 | togaf, standard |
```

Rules:
- Append a new row when an item is added
- Remove the row when an item is deleted (also delete the item file)
- Do not renumber existing rows after deletion — use the next available number for new items
- Update `lastUpdated` on every write
