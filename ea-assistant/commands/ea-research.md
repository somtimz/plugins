---
name: ea-research
description: Research a topic on the web (quick lookup or deep multi-researcher report) and manage research documents, notes, links and reports in the ResearchAndReferences folder; apply findings to engagement deliverables
argument-hint: "[quick <topic>|deep <topic>|add|note|link|list|view <item>|apply [artifact-id]]"
allowed-tools: [Read, Write, Bash, Glob, Grep, Agent, Task, AskUserQuestion]
---

Research external topics for the active engagement, manage the research library, and apply findings to EA deliverables.

## Overview

The `ResearchAndReferences/` folder is the engagement's library for external context: whitepapers, reference architectures, analyst reports, standards documents, repository links, and ad-hoc research notes. Everything in this folder can be referenced during interviews, artifact creation, and `/ea-grill` reviews.

**Research item types:**
- **Document** — an uploaded or pasted document (stored as `.md` with original content)
- **Note** — a freeform research note or observation written directly in the conversation
- **Link** — a URL with title, summary, and relevance tags
- **Report** — a cited research report produced by `/ea-research deep`; its researchers' notes sit beside it in `research-notes/{slug}/`

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
  /ea-research deep <topic>   — run a cited multi-source research report
  /ea-research quick <topic>  — fast lookup, 1-2 searches
  /ea-research add      — paste or describe a document
  /ea-research note     — write a research note
  /ea-research link     — add a URL reference
```

If items exist, display:

```
📚 Research & References — {engagement name}
Folder: EA-projects/{slug}/ResearchAndReferences/
Items: {N total} ({n} reports, {n} documents, {n} notes, {n} links)

  #  | Type     | Title                              | Added       | Tags
  ---|----------|------------------------------------|-------------|--------------------
  1  | document | Gartner EA Maturity Model 2024     | 2026-03-10  | capability, maturity
  2  | note     | Vendor positioning from RFI         | 2026-03-11  | vendor, app
  3  | link     | TOGAF 10 Reference Library         | 2026-03-12  | togaf, standard
  4  | report   | Zero trust adoption in banking     | 2026-03-14  | security, phase-d

Options:
  1. Research a topic (/ea-research deep <topic> or quick <topic>)
  2. Add a document  (/ea-research add)
  3. Write a note    (/ea-research note)
  4. Add a link      (/ea-research link)
  5. View an item    (/ea-research view <#>)
  6. Apply to an artifact  (/ea-research apply)
```

---

### Mode: quick \<topic\>

A fast lookup: one or two searches and a short cited answer. Dispatch the `ea-research` agent with `Quick research: {topic}` and the active engagement slug, and show its answer. If the topic needs more than two searches, the agent says so; offer `/ea-research deep {topic}`.

---

### Mode: deep \<topic\>

A cited research report built by researchers working in parallel, saved to the library as a `report` item.

You are the **coordinator**. Plan the research, dispatch the researchers and the writer, and register the result. Do not search, fetch or write the report yourself, and do not read the `ea-researcher` or `ea-research-writer` agent files: keeping that material out of this conversation is what leaves room for the report. Track progress with a task list if one is available, naming steps by what they do ("Research regulation"), not by subagent.

**Step 1 — Load context**

Read `engagement.json` (current phase, open decisions, open PAD-NNN items) and `ResearchAndReferences/research-index.md` (create it from the seed if missing, as in `list`). From these, work out what the research informs: an artifact section, a pending decision, a register. If `{topic}` is empty, ask for it.

**Step 2 — Clarify, only if it changes the research**

Ask follow-up questions (AskUserQuestion) only where the answer would change what gets researched:
- Ambiguous terms: acronyms or jargon with several meanings across fields.
- Jurisdiction or region, when the answer varies by it and neither the topic nor the engagement says which.
- Ambiguous entities: vendor, product or standard names that refer to several things.
- What it informs, when Step 1 could not tell and the target changes the questions.

Do not ask otherwise; every question delays the report.

**Step 3 — Title, slug and earlier research**

Choose a title: 3-6 words, under 50 characters, sentence case, specific to this request. The slug is the title in lowercase with spaces as hyphens (rule as in `add`).

Check the index for `report` items and list `ResearchAndReferences/research-notes/`. Then:
- **New topic:** a fresh title.
- **Extends or updates an earlier report:** a title that names the topic and what this request adds ("Zero trust banking regulators"), or the earlier title plus the next number ("Zero trust adoption in banking 2"). Note the earlier report's file and notes folder; the writer builds on them.
- **Redo requested:** a new title as above, but pass no earlier material.

The slug must differ from every existing item and folder. Never rename, move or write into an earlier request's report or notes folder.

Create `ResearchAndReferences/research-notes/{slug}/`. Note the engagement's absolute path; subagents get absolute paths.

**Step 4 — Decompose**

Split the question into subtopics that do not overlap and together cover it. For each, consider whether it needs more than one independent point of view (for example vendor claims versus independent assessments). One researcher per subtopic and viewpoint:

| Researchers | When | EA example |
|---|---|---|
| 1 | One factual question | "When does DORA apply to our sector?" |
| 3 | A focused topic with a few angles (the default) | "Event-driven integration for core banking": patterns and products, adoption evidence, failure modes |
| 4 | Distinct evaluation criteria | "Compare iPaaS options": capability fit, cost model, ecosystem and skills, independent reviews |
| 5+ | Several jurisdictions, domains or entities | "Data residency rules": EU, UK, US federal, Canada, APAC |

When building on earlier research, decompose only what this request adds or needs re-checking.

Show the plan before dispatching:

```
🔎 Deep research: {title}
Informs: {artifact / decision}   Phase: {phase}
Builds on: {earlier report, or none}

Researchers:
  1. {subtopic} — {key questions, one line}
  2. ...

Proceed? (y / edit / cancel)
```

**Step 5 — Dispatch the researchers in parallel**

Dispatch every researcher in **one message** (multiple Agent calls), `subagent_type: ea-researcher`, foreground. Give each a precise, self-contained assignment, carrying the engagement's constraints into it:

```
Research {narrow subtopic}.

Objective: {what the notes must cover}

Key questions:
- {question 1}
- {question 2}

Suggested sources:
- {source types to prioritise: standards bodies, regulators, analyst research, vendor documentation, case studies, academic}

Engagement context:
- Phase: {phase}; informs: {artifact section or decision}
- Constraints: {sector, geography, time window, scope from engagement.json}

Save your notes to {absolute engagement path}/ResearchAndReferences/research-notes/{slug}/{subtopic-slug}.md
```

**Step 6 — One gap round, only if essential**

Read the researchers' returned summaries, not their notes. If a gap would leave the report unable to answer the question, dispatch researchers for it in parallel, once. Say "After these researchers finish, I will move directly to the report writer." when you do. Never run a third round: move on to Step 7 whatever comes back.

**Step 7 — Dispatch the writer**

Dispatch one `ea-research-writer`, foreground:

```
Read the notes in {absolute engagement path}/ResearchAndReferences/research-notes/{slug}/ and write a research report that answers: {the full research question; for an extension, the earlier question as amended by this request}.

Research title: {title}
Engagement context: phase {phase}; informs {artifact / decision}; tags {tags}
Earlier research to build on: {absolute paths of the earlier report and notes folder, or "none"}

Save the report to {absolute engagement path}/ResearchAndReferences/{slug}.md
```

**Step 8 — Register and deliver**

Add a row to `research-index.md` (type `report`, file `{slug}.md`, tags from the report frontmatter) and update `lastUpdated`. Read the report, then confirm:

```
✅ Research report: {title}
   File: ResearchAndReferences/{slug}.md  ({n} sources)
   Notes: ResearchAndReferences/research-notes/{slug}/

{3-5 sentence summary: the answer and what it means for the engagement}

Options:
  1. Apply to an artifact  (/ea-research apply {artifact-id})
  2. View the full report  (/ea-research view {slug})
  3. Extend this research  (/ea-research deep <follow-up>)
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
- **y** — apply the suggested revision to the artifact, followed on its own line by `📎 Source: ResearchAndReferences/{research-file}.md` naming the item that supports it (the marker `/ea-research`'s impact tracing and `ea-research` Impact mode look for)
- **n** — skip this revision
- **edit** — ask the user to provide the revised text before applying; add the same `📎 Source:` marker

For `A` (apply all): apply every suggested revision without prompting per item, each with its `📎 Source:` marker.

When the source is a `report`, cite the report, not its notes files: the report is what was reviewed and approved.

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

`ResearchAndReferences/research-index.md` tracks all items. Created automatically if missing — seed from `templates/seeds/research-index.md`.

Rules:
- Append a new row when an item is added
- Remove the row when an item is deleted (also delete the item file; for a `report`, confirm before also deleting its `research-notes/{slug}/` folder)
- `Type` is one of `document`, `note`, `link`, `report`
- Do not renumber existing rows after deletion — use the next available number for new items
- Update `lastUpdated` on every write
