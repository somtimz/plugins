# Detail File Cross-Linking and Organisation Design

**Version:** 0.9.46
**Date:** 2026-05-09
**Scope:** ea-assistant plugin — detail file system

---

## Problem

Detail files (`artifacts/details/{ID}.md`) have two gaps:

1. **No cross-linking** — a requirement detail has no way to reference the goal or capability it relates to, and vice versa.
2. **No organisation** — the flat `details/` directory mixes all types (goals, capabilities, requirements, work packages) with no grouping or index.
3. **No inline notes** — there is no way to annotate a specific detail file with an observation or flag it for follow-up without creating a separate file.

---

## Approach

Keep the flat `artifacts/details/` folder structure (no migration of existing links). Solve organisation through a generated index and type-grouped list view. Add cross-linking via frontmatter + `## Related Items` section. Add inline notes via `## Notes` section with Open/Resolved lifecycle.

---

## Data Model Changes

### `templates/item-detail.md`

Add two new frontmatter fields:

```yaml
relatedItems: []    # array of related item IDs e.g. ["G-001", "CAP-003"]
```

Add two new sections immediately after the header metadata block (before `## Summary`):

```markdown
## Notes

<!-- GUIDANCE: Inline notes and flags. Add via /ea-note --detail {ID} or n: during sessions.
     Resolve via /ea-detail note resolve {ID}. -->

## Related Items

| ID | Type | Title | Relationship |
|---|---|---|---|
```

`## Notes` is empty by default. `## Related Items` has an empty table with headers.

### Note format (inline in `## Notes`)

Open:
```markdown
> 📌 **{YYYY-MM-DD}:** {note text} — **Open**
```

Resolved:
```markdown
> 📌 **{YYYY-MM-DD}:** {note text} — ~~**Open**~~ ✅ **Resolved {YYYY-MM-DD}:** {resolution text}
```

### Related Items table (inline in `## Related Items`)

Links use same-directory relative paths — all detail files share `artifacts/details/`, so `G-001.md` links to `./G-001.md` (or just `G-001.md`):

```markdown
| [G-001](G-001.md) | Goal | Reduce operational costs | supports |
| [CAP-003](CAP-003.md) | Capability | Customer Data Management | implemented by |
```

---

## Relationship Labels

Relationship labels are free text. Suggested vocabulary and their automatic inverses:

| Forward | Inverse |
|---|---|
| `supports` | `supported by` |
| `implements` | `implemented by` |
| `constrains` | `constrained by` |
| `derived from` | `source of` |
| `related` | `related` |

If a label is not in this table, the inverse defaults to `related`.

---

## Command Changes

### New mode: `link {ID1} {ID2} [relationship]`

Creates a bidirectional link between two detail files.

1. Verify both `details/{ID1}.md` and `details/{ID2}.md` exist — stop with error if either is missing.
2. Check if `{ID2}` is already in `{ID1}`'s `relatedItems[]` — skip duplicate silently.
3. Add `{ID2}` to `{ID1}`'s `relatedItems[]` frontmatter.
4. Append a row to `{ID1}`'s `## Related Items` table: `| [{ID2}](ID2.md) | {type} | {title} | {relationship} |`
5. Mirror: add `{ID1}` to `{ID2}`'s `relatedItems[]` and a row to its `## Related Items` table using the inverse label.
6. Update `lastModified` in both files.
7. Confirm: `✅ Linked {ID1} ↔ {ID2} ({relationship} / {inverse})`

`relationship` defaults to `related` if omitted.

### New mode: `check [ID]`

Runs four integrity checks. With no argument, checks all detail files. With an ID, checks only that file.

**Check 1 — Link integrity:** For every ID in `relatedItems[]`, verify `details/{ID}.md` exists. Report missing files as broken links.

**Check 2 — Back-link symmetry:** For every ID in `relatedItems[]`, verify the linked file also contains the current ID in its own `relatedItems[]`. Report one-way links. Offer to add the missing back-link.

**Check 3 — Table/frontmatter sync:** Verify every ID in `relatedItems[]` has a row in `## Related Items` and every row in `## Related Items` has a corresponding entry in `relatedItems[]`. Report mismatches. Offer to sync.

**Check 4 — Open notes:** Flag detail files that contain unresolved `📌` notes (lines matching `— **Open**`).

Output format:
```
/ea-detail check — {Engagement Name}
────────────────────────────────────────
G-001   ✅ 2 links · 0 open notes
REQ-003 ⚠️ broken link: CAP-009 (file not found)
CAP-003 ⚠️ one-way link: G-001 links here but CAP-003 does not link back
WP-007  ⚠️ 1 open note (2026-05-09)

3 issue(s). Run /ea-detail check {ID} to fix interactively.
```

Interactive fix per issue: offer to remove the broken link, add the missing back-link, or navigate to the open note.

### New mode: `note resolve {ID}`

Lists all open `📌` notes in `details/{ID}.md` (numbered). User selects one. Prompts for resolution text. Updates the selected blockquote in-place: appends `— ~~**Open**~~ ✅ **Resolved {today}:** {text}`. Updates `lastModified`.

### New mode: `index`

Generates `EA-projects/{slug}/artifacts/details/_index.md`. Overwrites any previous index.

Structure:
```markdown
# Detail File Index — {Engagement Name}
_Generated: {date} · {N} detail files · {M} cross-links_

## {Type Group}   ← one section per type that has at least one detail file, in ID-prefix alphabetical order

| ID | Title | Related Items | Open Notes | Parent Artifact |
|---|---|---|---|---|
| [{ID}]({ID}.md) | {title} | [{ID2}](ID2.md), ... | — or 📌 N open | [{artifact name}](../artifacts/{parentArtifact}) |
```

- Related Items column: comma-separated links using same-directory relative paths
- Open Notes column: `—` if none, `📌 N open` if any open notes present
- `_index.md` is excluded from all `check` operations (it is derived, not authoritative)

### Updated mode: `list [phase]`

- Default output groups rows by type (one header per type, rows beneath)
- New `--type {type}` filter: `ea-detail list --type requirement` — shows only matching type
- Add Open Notes column to the table
- Footer: `{N} detail file(s) · {M} cross-links · {K} open notes`

### Updated mode: `view {ID}`

After displaying file content, if `relatedItems[]` is non-empty, show navigation prompt:
```
Related: G-001 (Goal), CAP-003 (Capability) — /ea-detail view {ID} to open
```

Consistency action (option 3) extended to run all four check types from the new `check` mode against this single file.

---

## `/ea-note` integration

`/ea-note --detail {ID}` is a valid invocation. It appends a new open `📌` blockquote to the `## Notes` section of `details/{ID}.md`, following the same save-and-confirm flow as `--artifact`.

`n: {text}` during any session where a detail file is the focal context saves inline to `## Notes` (source set to the active session type: `interview`, `grill`, etc.).

---

## `detail-file-convention.md` additions

Add two new sections:
- **Cross-Linking** — explains `relatedItems[]`, relationship vocabulary, `link` and `check` commands
- **Inline Notes** — explains the `## Notes` section format, add and resolve flows

---

## Files Changed

| File | Change |
|---|---|
| `ea-assistant/templates/item-detail.md` | Add `relatedItems: []` frontmatter; add `## Notes` and `## Related Items` sections |
| `ea-assistant/commands/ea-detail.md` | Add `link`, `check`, `note resolve`, `index` modes; update `view` and `list` |
| `ea-assistant/commands/ea-note.md` | Add `--detail {ID}` as a valid target |
| `ea-assistant/skills/ea-artifact-templates/references/detail-file-convention.md` | Add Cross-Linking and Inline Notes sections |
| `ea-assistant/.claude-plugin/plugin.json` | Version 0.9.45 → 0.9.46 |
| `.claude-plugin/marketplace.json` | Version 0.9.45 → 0.9.46 |
| `ea-assistant/CLAUDE.md` | Version bump |
| `ea-assistant/commands/ea-help.md` | Update `/ea-detail` argument-hint and description |
| `ea-assistant/docs/PRD.md` | Version + new section |
| `ea-assistant/README.md` | Feature bullets |
