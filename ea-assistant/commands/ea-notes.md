---
name: ea-notes
description: List, view, edit, or delete interview notes, brainstorm notes, and review files for the active engagement
argument-hint: "[list [phase] | view <path> | edit <path> | delete <path>]"
allowed-tools: [Read, Write, Glob, Bash]
---

Browse, view, edit, or delete notes for the active EA engagement.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

Read `engagement.json` and extract the `slug` field. All paths in this command are relative to `EA-projects/{slug}/`.

---

### Mode: `list [phase]` (default)

1. Glob `artifacts/**/notes/**/*.md` from the engagement root to discover all note files.

2. Classify each file by type from its path segment:
   - `.../notes/interviews/...` → Interview Note
   - `.../notes/brainstorm/...` → Brainstorm Note
   - `.../notes/reviews/...` → Review Note

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
```

For brainstorm notes, read the `sessions` and `lastUpdated` fields from frontmatter to populate the table.

If no notes are found, show: "No notes found for this engagement yet. Run `/ea-brainstorm`, `/ea-interview`, or `/ea-grill` to create notes."

After displaying, offer a next-actions menu:
```
What would you like to do?
  v) View a note       e) Edit a note       d) Delete a note       q) Quit
```

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
