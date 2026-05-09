---
name: ea-note
description: Quick-capture a note, concern, or annotation — saved immediately with routing suggestions
argument-hint: "[text] [--artifact <id>] [--detail <id>] | resolve <path>"
allowed-tools: [Read, Write, Glob, Bash]
---

Quick-capture a note for the active EA engagement, optionally linked to a specific artifact.

## Instructions

### Step 1 — Require an active engagement

Check for `engagement.json` in context. If no engagement is active, prompt: "No engagement is currently active. Run `/ea-open` to open one first."

Read `engagement.json` and extract `slug`, `name`, and `currentPhase`. All paths in this command are relative to `EA-projects/{slug}/`.

**If the argument begins with `resolve`, skip immediately to the [Mode: `resolve <path>`](#mode-resolve-path) section below.** Do not proceed to Step 2.

---

### Step 2 — Capture text

If inline text was provided as an argument (excluding flags), use it as the note text.

If no text was provided, prompt: "What's on your mind?"

---

### Step 3 — Determine mode

**Resolve the phase folder** from `currentPhase` using this lookup table:

| `currentPhase` value | Phase folder |
|---|---|
| `Prelim` | `preliminary` |
| `A` | `phase-a` |
| `B` | `phase-b` |
| `C` or `C-Data` | `phase-c-data` |
| `C-App` | `phase-c-app` |
| `D` | `phase-d` |
| `E` | `phase-e` |
| `F` | `phase-f` |
| `G` | `phase-g` |
| `H` | `phase-h` |
| (null or not set) | `cross-cutting` |

**Resolve the phase label** from `currentPhase`:

| `currentPhase` | Phase label |
|---|---|
| `Prelim` | `Preliminary` |
| `A` | `Phase A — Architecture Vision` |
| `B` | `Phase B — Business Architecture` |
| `C` or `C-Data` | `Phase C — Information Systems Architecture (Data)` |
| `C-App` | `Phase C — Information Systems Architecture (Application)` |
| `D` | `Phase D — Technology Architecture` |
| `E` | `Phase E — Opportunities & Solutions` |
| `F` | `Phase F — Migration Planning` |
| `G` | `Phase G — Implementation Governance` |
| `H` | `Phase H — Architecture Change Management` |
| (null or not set) | `Cross-cutting` |

---

#### Detail mode (when `--detail {ID}` is provided)

1. Check whether `EA-projects/{slug}/artifacts/details/{ID}.md` exists. If not: "No detail file found for `{ID}`. Create it first with `/ea-detail new {ID}`." — stop.
2. Read the detail file.
3. If a `## Notes` section exists, locate its end: the `---` separator or next `##` heading that follows the section. If `## Notes` does not exist (legacy file created before this feature), append `\n\n## Notes\n` before the first `##` section after the header metadata block.
4. Insert a new blockquote at the end of the `## Notes` section content, immediately before the closing `---` or next `##`:
   `> 📌 **{YYYY-MM-DD}:** {text} — **Open**`
5. Set `lastModified` in frontmatter to today's date.
6. Write the file.
7. Skip to Step 4 (confirm save), using path `artifacts/details/{ID}.md`.

The routing suggestions in Step 5 still apply after the confirm.

---

#### Artifact mode (when `--artifact <id>` is provided)

1. Glob `artifacts/**/{id}.md` to locate the artifact file.
2. If not found, show: "No artifact found with id `{id}`. Check the id and try again."
3. Ask: "Save as (i) inline annotation or (l) linked note?"

**Inline annotation (i):**

1. Read the artifact file.
2. List its `##` section headers (ignore `###` and deeper).
3. Ask: "Which section should this annotation appear under?"
4. Insert `\n> **Note ({YYYY-MM-DD}):** {text}` at the end of that section's content, immediately before the next `##` heading (or at end of file if it is the last section).
5. Write the updated artifact file.
6. Confirm: `✅ Annotation saved — {artifact path}`
7. Skip to Step 5 (routing suggestions).

**Linked note (l):**

1. Determine the next sequential `N` for today by globbing `artifacts/{phase-folder}/notes/adhoc/note-{artifact-id}-{YYYY-MM-DD}-*.md` in that folder, counting existing files, and adding 1 (e.g. if 3 files exist, N = 4).
2. Build the note path: `artifacts/{phase-folder}/notes/adhoc/note-{artifact-id}-{YYYY-MM-DD}-{N}.md` — use the phase folder resolved from `currentPhase` in Step 1, not the artifact's own location.
3. Write the note file with artifact-note frontmatter and body (see templates below).
4. Read the artifact file's `links:` frontmatter array. Append `{note path}` to it and write the updated artifact file.
5. Skip to Step 4.

---

#### Phase / cross-cutting mode (no `--artifact`)

1. Determine the next sequential `N` for today by globbing `artifacts/{phase-folder}/notes/adhoc/note-{YYYY-MM-DD}-*.md`, counting existing files, and adding 1 (e.g. if 3 files exist, N = 4).
2. Build the note path: `artifacts/{phase-folder}/notes/adhoc/note-{YYYY-MM-DD}-{N}.md`
3. Write the note file with adhoc frontmatter and body (see templates below).
4. Continue to Step 4.

---

### Note file templates

**Ad-hoc note frontmatter** (phase / cross-cutting mode):

```yaml
---
type: adhoc
engagement: {name}
phase: {phase label or "Cross-cutting"}
date: {YYYY-MM-DD}
source: standalone
parentArtifact: null
status: Open
resolvedDate: null
resolvedBy: []
crossPhase: false
---
```

**Linked artifact note frontmatter** (artifact mode — linked):

```yaml
---
type: artifact-note
engagement: {name}
phase: {phase label}
date: {YYYY-MM-DD}
source: standalone
parentArtifact: {artifact-id}
status: Open
resolvedDate: null
resolvedBy: []
crossPhase: false
---
```

**Note body** (both types):

```markdown
{note text}

## Resolution

*(not yet resolved)*
```

---

### Step 4 — Confirm save

Display the save confirmation, adapting the path and resolution shortcut by mode:

**`--detail` mode:**
```
✅ Note saved — artifacts/details/{ID}.md

_Shortcuts: `n: {text}` to capture during interviews/grill · `/ea-detail note resolve {ID}` to resolve_
```

**All other modes:**
```
✅ Note saved — artifacts/{phase-folder}/notes/adhoc/note-{YYYY-MM-DD}-{N}.md

_Shortcuts: `n: {text}` to capture during interviews/grill · `/ea-note resolve {path}` to record resolution_
```

---

### Step 5 — Routing suggestions

Classify the note text against the signals below. Offer **one** relevant follow-up action — the first signal that matches. Do not show a wall of options.

| Signal in text | Routing offer |
|---|---|
| Contains `must`, `shall`, `should`, or `need to` | "Add to requirements register? (`/ea-requirements add`)" |
| Sounds like a concern or objection | "Capture as a stakeholder concern? (`/ea-interview`)" |
| Contains a technology or vendor name, `vs`, or `make vs buy` | "Create an ADR? (`/ea-adrs new`)" |
| References a different phase (e.g. "in Phase B") | "Flag for that phase? (adds cross-phase marker)" |
| No signal matches | "View all notes: `/ea-notes list`" |

If the user selects the cross-phase marker offer, set `crossPhase: true` in the note's frontmatter (updating the existing field) and confirm.

If no routing is selected, end cleanly — the note is already saved.

---

## Mode: `resolve <path>`

Invoked as `/ea-note resolve <path>` where `<path>` is relative to `EA-projects/{slug}/`.

1. Read the note file at the given path.
2. If `status` is already `Resolved`, display the current resolution section and ask: "Update resolution? (y/n)" If no, end cleanly.

3. Prompt in sequence — wait for each response before asking the next:

   **Resolved by:** "What resolved this note? Enter artifact IDs or item IDs (comma-separated, e.g. `STR-003, phase-b/business-architecture`):"

   **Description:** For each ID provided, ask: "What changed in {id}?" (one line each)

   **Rationale:** "Why was this the right resolution?"

   **Impact:** "What changed in the engagement as a result?"

   **Residual impacts:** "Any outstanding impacts still unresolved? (press Enter to skip)"

4. Update the note's frontmatter:
   - `status: Resolved`
   - `resolvedDate: {today ISO 8601}`
   - `resolvedBy: [{ids}]`

5. Replace `*(not yet resolved)*` in the `## Resolution` section with:

```markdown
**Status:** Resolved — {YYYY-MM-DD}

### Resolved By
- {artifact-id or item-id}: {description of what changed}

### Rationale
{why this resolution was chosen}

### Impact
{what changed in the engagement as a result}

### Residual Impacts
- {any outstanding impact that is still unresolved — or "None identified"}
```

6. Write the updated file.

7. Confirm: `✅ Note resolved — {path}`
