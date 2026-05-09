---
name: ea-notes
description: List, view, edit, delete, or resolve notes for the active engagement
argument-hint: "[list [phase] | view <path> | edit <path> | delete <path>]"
allowed-tools: [Read, Write, Glob, Bash]
---

Browse, view, edit, or delete notes for the active EA engagement.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

Read `engagement.json` and extract the `slug` field. All paths in this command are relative to `EA-projects/{slug}/`.

---

### Mode: `list [phase]` (default)

1. Glob `artifacts/**/notes/**/*.md` and `notes/adhoc/**/*.md` from the engagement root to discover all note files.

2. Classify each file by type from its path segment:
   - `.../notes/interviews/...` → Interview Note
   - `.../notes/brainstorm/...` → Brainstorm Note
   - `.../notes/reviews/...` → Review Note
   - `.../notes/adhoc/...` → Ad-hoc Note

3. Resolve the phase label from the path segment (e.g. `phase-a` → `Phase A`, `preliminary` → `Preliminary`, `cross-cutting` → `Cross-cutting`).

4. If a `[phase]` argument was provided (e.g. `/ea-notes list phase-a` or `/ea-notes list A`), filter to that phase only.

5. Display grouped by type:

```
## Interview Notes
| Phase        | Artifact / Scope            | Date       | Ver | File path |
|--------------|-----------------------------|------------|-----|-----------|
| Phase A      | architecture-vision         | 2026-04-05 | v1  | artifacts/phase-a/notes/interviews/interview-architecture-vision-2026-04-05-v1.md |

## Brainstorm Notes
| Phase        | Sessions | Last Updated | File path |
|--------------|----------|--------------|-----------|
| Phase A      | 2        | 2026-04-05   | artifacts/phase-a/notes/brainstorm/brainstorm-notes.md |

## Review Notes
| Phase        | Artifact                    | Skill      | Date       | File path |
|--------------|-----------------------------|------------|------------|-----------|
| Phase A      | architecture-vision         | boardroom  | 2026-04-05 | artifacts/phase-a/notes/reviews/grill-architecture-vision-boardroom-2026-04-05.md |

## Ad-hoc Notes
| Phase        | Status   | Date       | Source     | File path |
|--------------|----------|------------|------------|-----------|
| Phase A      | Open     | 2026-05-09 | interview  | artifacts/phase-a/notes/adhoc/note-2026-05-09-1.md |
| Cross-cutting| Resolved | 2026-05-08 | standalone | artifacts/cross-cutting/notes/adhoc/note-2026-05-08-1.md |
```

For brainstorm notes, read the `sessions` and `lastUpdated` fields from frontmatter to populate the table.

For ad-hoc notes, read the `status` and `source` fields from frontmatter to populate the table. Sort Open notes before Resolved ones.

If no notes are found, show: "No notes found for this engagement yet. Run `/ea-note`, `/ea-brainstorm`, `/ea-interview`, or `/ea-grill` to create notes."

After displaying, offer a next-actions menu:
```
What would you like to do?
  v) View a note       e) Edit a note       d) Delete a note       r) Resolve a note       q) Quit
```

When `r` is selected:
- Prompt: "Enter the file path of the note to resolve (relative to `EA-projects/{slug}/`):"
- Follow the resolve flow from `/ea-note resolve <path>`:
  1. Read the note file. If `status` is already `Resolved`, display the current resolution section and ask: "Update resolution? (y/n)" If no, end cleanly.
  2. Prompt in sequence (wait for each response before asking the next):
     - **Resolved by:** "What resolved this note? Enter artifact IDs or item IDs (comma-separated, e.g. `STR-003, phase-b/business-architecture`):"
     - **Description:** For each ID provided, ask: "What changed in {id}?" (one line each)
     - **Rationale:** "Why was this the right resolution?"
     - **Impact:** "What changed in the engagement as a result?"
     - **Residual impacts:** "Any outstanding impacts still unresolved? (press Enter to skip)"
  3. Update the note's frontmatter: `status: Resolved`, `resolvedDate: {today ISO 8601}`, `resolvedBy: [{ids}]`
  4. Replace `*(not yet resolved)*` in the `## Resolution` section with the full populated resolution block (Status, Resolved By, Rationale, Impact, Residual Impacts).
  5. Write the updated file.
  6. Confirm: `✅ Note resolved — {path}`

---

### Mode: `view <path>`

1. Read the file at the given path (relative to `EA-projects/{slug}/`).
2. Display the full content inline with a header showing the file type, phase, and date.
3. After displaying, offer: "Edit this note? (y/n)"

---

### Mode: `edit <path>`

1. Read the file at the given path.
2. Display the current content.
3. Ask: "What would you like to change? Describe the edit or paste the replacement content."
4. Apply the described edit to the file.
5. Confirm: "Note updated — `{path}`"

---

### Mode: `delete <path>`

1. Read the file at the given path.
2. Show the filename and first line of content.
3. Ask for confirmation: "Type the filename (without path) to confirm deletion:"
4. If confirmed, delete the file.
5. Confirm: "Deleted — `{path}`"
6. If the `notes/brainstorm/` or `notes/interviews/` or `notes/reviews/` folder is now empty after deletion, leave the folder in place (do not remove it).
