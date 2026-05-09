---
name: ea-stories
description: Generate or view the User Story Register. Scan all artifacts for STY-NNN entries, aggregate them into a consolidated register, and surface orphan stories or stories without acceptance criteria.
argument-hint: "[generate | status | new | update STY-NNN <field> <value>] [--actor <actor>] [--sbb SBB-NNN] [--req REQ-NNN] [--enabler]"
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

You are executing the `/ea-stories` command.

## Overview

User Stories (STY-NNN) are lightweight, actor-centred delivery items that translate SBBs into executable work. This command aggregates all STY-NNN entries from across the engagement into a single register, surfaces orphan stories (no REQ or SBB link), and tracks enabler stories.

**Modes:**
- `generate` (default) — scan all artifacts for STY tables and write `story-register-{YYYY-MM-DD}.md`
- `status` — inline summary of stories without writing a file
- `new` — create a new story record interactively
- `update STY-NNN <field> <value>` — update a single field on an existing story

**Filters:**
- `--actor` — filter by actor name (partial match)
- `--sbb SBB-NNN` — filter stories that implement a specific SBB
- `--req REQ-NNN` — filter stories that satisfy a specific requirement
- `--enabler` — show only enabler stories (tagged `[Enabler]`)

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, artifacts.

---

## Mode: `generate` (default)

### Step 2 — Scan for Story Entries

Scan all `.md` files in `EA-projects/{slug}/artifacts/` for STY tables:

| Artifact Pattern | Section to Scan | Row Format |
|---|---|---|
| `requirements-register*.md` | Stories subsections under each REQ | `STY-NNN | Story | Implements (SBB-NNN) | Tasks` |
| `architecture-roadmap*.md` | Work package decomposition tables | `STY-NNN | Story | Implements (SBB-NNN) | Tasks` |
| `migration-plan*.md` | Delivery item tables | Same |

For each STY row found:
- Extract: ID, Story text, Implements (SBB-NNN), Tasks, Acceptance criteria (if present)
- Record source artifact filename and phase
- Detect enabler stories: text contains `[Enabler]` or no actor benefit pattern
- Merge duplicates (most complete version wins)

### Step 3 — Detect Orphans and Quality Issues

For each STY-NNN:
- **Orphan (Warning):** No `Satisfies` REQ-NNN — story not traced to a requirement
- **Orphan (Info):** No `Implements` SBB-NNN — may be an enabler story; flag if not tagged `[Enabler]`
- **No Acceptance Criteria:** Story has no acceptance criteria listed
- **Task-level Story:** Story text reads like a task ("configure X", "write Y", "run Z") rather than an actor goal

### Step 4 — Compile Story Register

Using the Story register template (`templates/story-register.md`):

1. Populate Summary table: counts by actor, orphan status, enabler status
2. Populate Story Detail table: all stories with fields
3. Populate Orphan Stories table: stories missing REQ or SBB links
4. Populate Quality Issues table: stories without acceptance criteria or task-level text
5. Populate Requirement Coverage map: which REQs are implemented by which stories
6. Populate SBB Coverage map: which SBBs are delivered by which stories

### Step 5 — Write the Register File

Write to: `EA-projects/{slug}/artifacts/story-register-{YYYY-MM-DD}.md`

Register in `engagement.json → artifacts[]` if not already present.

Confirm: `"Story Register written: {N} stories ({N} orphans flagged, {N} enablers)"`

---

## Mode: `status`

Display inline summary:

```
Story Status — {engagement name}
Generated: {YYYY-MM-DD}

Total Stories:     {N}
By Actor:         {actor} ×{N} | {actor} ×{N} | ...
Enablers:         {N} ({N}% of total)
Orphans:          {N} story(ies) with no REQ link  |  {N} story(ies) with no SBB link
Quality Issues:   {N} without acceptance criteria  |  {N} task-level items
Coverage:         {N} REQ(s) → {N} story(ies)  |  {N} SBB(s) → {N} story(ies)

{if N > 0 orphans}: Use '/ea-stories generate' to write the full register with remediation notes.
{if N > 0 quality}: Consider running '/ea-grill phase-e --skill story-quality' to review.
```

---

## Mode: `new`

Create a new story record.

### Step 2 — Determine Next Story Number

Find highest existing STY-NNN. Assign next: `STY-{NNN+1}` (zero-padded).

### Step 3 — Collect Story Metadata

```
Creating new Story — STY-{NNN}

1. Story (follow "As a {actor}, I want {goal} so that {benefit}"):
2. Implements (SBB-NNN this story delivers — optional, press Enter):
3. Satisfies (REQ-NNN this story addresses — optional, press Enter):
4. Acceptance criteria (how we know it's done — bullet list, optional):
5. Enabler story? (y/n — no direct user-facing outcome, e.g. infrastructure setup):
```

### Step 4 — Validate

- Story must follow actor-goal-benefit pattern. If not, warn: "⚠️ This looks like a task, not a story. Use bullet points under a story instead? (y/n)"
- If enabler = n and no SBB link → info: "Consider linking to an SBB for traceability."
- If enabler = y → tag as `[Enabler]` in story text

### Step 5 — Create File

Write to: `EA-projects/{slug}/artifacts/sty-{NNN}-{kebab-slug}.md`

Register in `engagement.json → artifacts[]`.

Confirm: `"STY-{NNN} created. Link to REQ and SBB for full traceability."`

---

## Mode: `update STY-NNN <field> <value>`

Update a single field.

**Valid fields:**

| Field | Valid values |
|---|---|
| `story` | any string (actor-goal-benefit format preferred) |
| `implements` | SBB-NNN (single) |
| `satisfies` | REQ-NNN (single or comma-separated) |
| `acceptanceCriteria` | bullet list string |
| `enabler` | `true` / `false` |

**Validation rules:**
- Setting `story` to task-level text → warn about story-vs-task distinction
- Setting `enabler: true` → append `[Enabler]` tag if not present
- Setting `enabler: false` → remove `[Enabler]` tag if present

**Procedure:**
1. Find the story file matching `sty-{NNN}*.md` or the STY row in the register
2. Show proposed change: `"STY-NNN: {field} — '{old}' → '{new}'"`
3. Ask: `"Apply? (y/n)"`
4. On confirm: update the file and `engagement.json`

Confirm: `"Updated STY-NNN: {field} set to '{new_value}'"`

---

## Edge Cases

| Scenario | Handling |
|---|---|
| No stories found | Report "No stories found. Define stories in Requirements Register Stories subsections or Architecture Roadmap." |
| Story appears in multiple artifacts | Merge fields; prefer Requirements Register version; list all sources |
| Story with no REQ link | Flag as orphan; suggest linking via `/ea-requirements` or `/ea-interview` |
| Story with task-level text | Flag as quality issue; suggest rewriting as actor-goal-benefit or moving to Tasks |
| Enabler story without [Enabler] tag | Auto-tag if detected (infrastructure, compliance, security scaffolding language) |
