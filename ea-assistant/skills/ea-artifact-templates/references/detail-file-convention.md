# Detail File Convention

Reference for the optional item-level detail file pattern in EA engagements.

---

## What is a Detail File?

A detail file is an optional companion Markdown file for a single row in an EA artifact table. It provides extended narrative, rationale, risks, costs, issues, concerns, impact, and alternatives that would make the source table unreadable if included inline.

Detail files are **opt-in** — not every row requires one. Create them for:
- High-priority or high-impact items
- Decisions that were contested or required significant deliberation
- Items raised or challenged during a grill or review session
- Any item where a stakeholder asks "why?" or "what about X?"
- Items with non-trivial cost, risk, or dependency implications

---

## File Location

All detail files for an engagement live in a single directory:

```
EA-projects/{slug}/artifacts/details/{ID}.md
```

**Examples:**
- `artifacts/details/G-001.md` — detail for Goal G-001
- `artifacts/details/CAP-003.md` — detail for Capability CAP-003
- `artifacts/details/WP-007.md` — detail for Work Package WP-007

**Key property:** The directory is engagement-wide — not per-phase. This ensures that when the same ID is referenced from multiple artifacts, all references point to the same canonical detail file.

---

## Linking from Artifact Tables

Add a `Details` column as the **rightmost column** in any ID-bearing table. The column value is:

- `[→](../details/{ID}.md)` — when a detail file exists
- `—` — when no detail file exists (default placeholder)

**Example (Goals table in Architecture Vision):**

```markdown
| ID | Goal | Business Driver(s) | Linked Strategies | Rationale | Details |
|---|---|---|---|---|---|
| [G-001](../details/G-001.md) | Reduce operational costs | DRV-001 | STR-001 | Cost pressure from competitive market | [→](../details/G-001.md) |
| G-002 | Improve customer satisfaction | DRV-002 | STR-002 | Customer NPS declining | — |
```

Note: The ID cell may also be linked directly (e.g. `[G-001](../details/G-001.md)`) as an alternative to the Details column — use whichever pattern the template defines.

---

## Relative Path from Artifacts

The relative path from any artifact to a detail file is:

| Artifact location | Path to detail file |
|---|---|
| `artifacts/phase-a/architecture-vision.md` | `../details/{ID}.md` |
| `artifacts/phase-b/business-architecture.md` | `../details/{ID}.md` |
| `artifacts/cross-cutting/risk-register.md` | `../details/{ID}.md` |
| `artifacts/requirements/requirements-register.md` | `../details/{ID}.md` |

All phase folders are one level under `artifacts/`, so the path is always `../details/{ID}.md`.

---

## Frontmatter Fields

Required fields in each detail file's YAML frontmatter:

| Field | Description |
|---|---|
| `item` | The ID (e.g. `G-001`) — must match the filename |
| `type` | The item type (e.g. `Goal`, `Capability`, `Work Package`) |
| `title` | Short title matching the item's label in the source table |
| `engagement` | Engagement name from `engagement.json` |
| `parentArtifact` | Relative path to the parent artifact (e.g. `phase-a/architecture-vision.md`) |
| `created` | Date created (`YYYY-MM-DD`) |
| `lastModified` | Date last updated (`YYYY-MM-DD`) |

---

## Standard Sections

Each detail file has nine standard sections. All sections are optional — omit those that don't apply.

| Section | Contents |
|---|---|
| **Summary** | 1–2 sentences: what this item is and why it exists |
| **Narrative** | Backstory: origin, context, organisational background |
| **Rationale** | Why it was defined this way; decisions made; A3/ADR references |
| **Risks** | Risks specific to this item (flag critical ones for `/ea-risks`) |
| **Costs** | Budget, resource, time, or opportunity cost implications |
| **Issues** | Known issues affecting or caused by this item (link ISS-NNN) |
| **Concerns** | Stakeholder concerns raised (link CON-NNN from Appendix A4) |
| **Impact** | What this item affects — both enabling and constraining |
| **Alternatives** | Options considered and why they were not chosen |

---

## How Skills Load Detail Files

### Scope A (ea-grill, ea-review, ea-interview)

After loading the focal artifact, Scope A includes a detail file loading step:

1. Scan all tables in the artifact for `[→](../details/{ID}.md)` links
2. For each linked file that exists on disk: read it and include as supplementary context for that item
3. During Q&A or comment generation, cite content as `[detail: {ID}]`

### ea-brainstorm

After step 3c (pulling pre-existing answers), also load any detail files linked from the artifact being brainstormed. Treat detail file content as additional context — surfaced as prefilled entries with `source: "detail: {ID}"`.

### ea-consistency Check D

Validates detail file link integrity across all artifacts:
- Scan all `[→](../details/{ID}.md)` and `../details/{ID}.md` links
- Verify target file exists
- Verify `item` frontmatter field matches filename ID
- Report broken links as warnings

---

## Creating Detail Files

Use `/ea-detail new {ID} [{artifact-id}]` to create a detail file. The command:

1. Detects the ID type from the prefix
2. Locates the parent artifact (from the optional argument or by scanning all artifacts)
3. Extracts the matching table row to pre-fill `title`, `type`, and `parentArtifact`
4. Creates `artifacts/details/{ID}.md` from `templates/cross-cutting/item-detail.md`
5. Opens the file for editing

---

## Consistency Rules

- **One canonical file per ID** — if G-001 appears in Architecture Vision and is referenced in Business Architecture, both tables link to the same `artifacts/details/G-001.md`
- **Filename must match the `item` frontmatter field** — `G-001.md` must have `item: G-001`
- **Title should match source table** — update `title` in the detail file when the source table label changes
- **Path is always `../details/{ID}.md`** from any artifact — never use absolute paths or phase-relative paths

---

## ID Type to Parent Artifact Mapping

When `/ea-detail new {ID}` is called without an artifact argument, use this table to locate the likely parent artifact:

| ID Prefix | Type | Typical Parent Artifact |
|---|---|---|
| `DRV` | Business Driver | `phase-a/architecture-vision.md` |
| `G` | Goal | `phase-a/architecture-vision.md` |
| `OBJ` | Objective | `phase-a/architecture-vision.md` |
| `STR` | Strategy | `phase-a/architecture-vision.md` |
| `ISS` | Issue | `phase-a/architecture-vision.md` |
| `PRB` | Problem | `phase-a/architecture-vision.md` |
| `OPP` | Opportunity | `phase-a/architecture-vision.md` |
| `MET` | Metric | `phase-a/architecture-vision.md` |
| `CAP` | Capability | `phase-b/business-architecture.md` |
| `VS` | Value Stream | `phase-b/business-architecture.md` |
| `UC` | Use Case | `phase-b/business-architecture.md` |
| `GAP` | Gap | Scan all `gap-analysis.md` files |
| `WP` | Work Package | `phase-e/architecture-roadmap.md` |
| `REQ` | Requirement | `requirements/requirements-register.md` |
| `RIS` | Risk | `cross-cutting/risk-register.md` |
| `CON` | Stakeholder Concern | Scan all Appendix A4 tables |
| `ADR` | Architecture Decision Record | Scan `adr-*.md` files |
| `OPP` | Opportunity | `phase-a/architecture-vision.md` |
| `PAD` | Pending Architecture Decision | Scan all artifacts |

If the parent artifact cannot be determined automatically, prompt the user to specify `{artifact-id}`.

---

## Session Recording

When interview, review, brainstorm, or grill sessions surface concerns or issues related to a specific engagement item, those items may be recorded directly into the detail file's **Concerns** or **Issues** sections. This keeps item-level context in one canonical place rather than scattered across session notes.

### Entry formats by session type

| Session | Section | Format |
|---|---|---|
| Interview (A3 capture, ISS/PRB assignment) | Issues or Concerns | `- [interview: {YYYY-MM-DD}] {captured text} — {ISS-NNN / PRB-NNN / A3 ref}` |
| Review (comment) | Concerns | `- [review: {YYYY-MM-DD}] {comment text} — {reviewer}` |
| Brainstorm (`[ISS?]` / `[PRB?]` entries) | Issues | `- [brainstorm: {YYYY-MM-DD}] {entry text}` (retaining `[ISS?]`/`[PRB?]` marker) |
| Grill (CON-NNN from A4) | Concerns | `- CON-NNN: {concern text} — {grill skill}, {YYYY-MM-DD}` |

**Rules:**
- Session recording is always **offer-based** — the user confirms before any write.
- If a detail file does not exist when recording is accepted, create a stub from `templates/cross-cutting/item-detail.md` first.
- Do not overwrite existing entries — always append.
- Update `lastModified` in the detail file frontmatter after every write.

---

## Sync Rules

Detail file Concerns and Issues sections must stay in sync with the parent artifact's Appendix A4 table. Sync gaps occur when:

1. **Detail file → A4 gap:** A `CON-NNN` referenced in a detail file's Concerns section has no matching row in the parent artifact's A4 table.
2. **A4 → Detail file gap:** An A4 table row associated with an item (linkable via the Details column) is not referenced in that item's detail file Concerns section.

**How to sync:**
- Run `/ea-detail sync {ID}` to bidirectionally sync a single item.
- Run `/ea-consistency --details` to scan all detail files for sync gaps (Check E) alongside link integrity (Check D).

**Sync rules:**
- A CON-NNN that exists only in a detail file is pushed to A4 with `Status: Requires Attention` and `Raised By: detail file`.
- A CON-NNN that exists only in A4 is pulled to the detail file Concerns section with format `- CON-NNN: {concern text} — {Raised By}, {date}`.
- ISS-NNN and PRB-NNN in the detail file Issues section are not synced to A4 — they are tracked in the engagement's Issues/Problems register via `/ea-interview`.

---

## Generation and Publishing

Detail file content can be included in exported and published documents.

### ea-generate (single artifact)

Use the `--with-details` flag:
```
/ea-generate architecture-vision docx --with-details
```

When set:
- All detail files linked from the artifact are read and passed to the Python generation script as a `detailFiles` JSON array.
- The script embeds each detail file's content as a subsection after its relevant table row, or as **Appendix D — Item Detail Files** at the end of the document.
- Without the flag: behaviour is identical to the pre-detail-file version (backward-compatible).

### ea-publish (consolidated document)

After selecting artifacts, choose how to include detail files:

| Option | Effect |
|---|---|
| **Inline** | Detail content embedded after the relevant table section in each artifact |
| **Appendix only** | `## Supplementary Item Detail` section at the end of the consolidated document |
| **Exclude** | Detail files not included (default) |

---

## Cross-Linking

### Data model

Each detail file carries a `relatedItems: []` frontmatter array — the machine-readable source of truth for cross-links:

```yaml
relatedItems: ["G-001", "CAP-003"]
```

The `## Related Items` section renders those links as a human-readable table:

```markdown
## Related Items

| ID | Type | Title | Relationship |
|---|---|---|---|
| [G-001](G-001.md) | Goal | Reduce operational costs | supports |
| [CAP-003](CAP-003.md) | Capability | Customer Data Management | implemented by |
```

Links use same-directory relative paths — all detail files share `artifacts/details/`, so `G-001.md` links to `./G-001.md`.

### Managing links

Use `/ea-detail link {ID1} {ID2} [relationship]` to create a bidirectional link:

1. Both files must exist — the command stops with an error if either is missing.
2. The link is added to both files: `{ID2}` in `{ID1}`'s list and `{ID1}` in `{ID2}`'s list.
3. The inverse label is applied automatically (see table below).
4. `lastModified` is updated in both files.

If a file was created before the `## Related Items` section existed, the command appends the section before the next `##` heading.

### Relationship labels

| Forward | Inverse |
|---|---|
| `supports` | `supported by` |
| `implements` | `implemented by` |
| `constrains` | `constrained by` |
| `derived from` | `source of` |
| `related` | `related` |

If a label is not in this table, the inverse defaults to `related`.

### Consistency rules

`/ea-detail check [ID]` runs four checks:

1. **Link integrity** — every ID in `relatedItems[]` maps to an existing `details/{ID}.md`.
2. **Back-link symmetry** — if A links to B, B must link back to A.
3. **Table/frontmatter sync** — every ID in `relatedItems[]` has a row in `## Related Items`, and every row has a matching `relatedItems[]` entry. Full-token matching: `G-001` must match `G-001` only, not `G-0010`.
4. **Open notes** — flags files with unresolved `📌` annotations.

With no argument, all detail files are checked. With an ID, only that file is checked with interactive fix options.

---

## Inline Notes

### Format

Notes live in the `## Notes` section of each detail file.

Open:
```markdown
> 📌 **{YYYY-MM-DD}:** {note text} — **Open**
```

Resolved:
```markdown
> 📌 **{YYYY-MM-DD}:** {note text} — ~~**Open**~~ ✅ **Resolved {YYYY-MM-DD}:** {resolution text}
```

### Adding notes

- `/ea-note --detail {ID}` — appends a new open `📌` blockquote to the `## Notes` section.
- `n: {text}` during any session where a detail file is the focal context — same effect; source is set to the active session type (`interview`, `grill`, etc.).

If a legacy file is missing the `## Notes` section, it is added before `## Summary`.

### Resolving notes

`/ea-detail note resolve {ID}` lists all open notes in the file (numbered). Select one, enter resolution text — the blockquote is updated in-place with the resolved format above. `lastModified` is updated.

### Visibility

- `/ea-detail check` — Check 4 flags files with open notes.
- `/ea-detail list` — Open Notes column shows `—` or `📌 N open`.
- `/ea-detail index` — Open Notes column in `_index.md` shows the same.
- `/ea-detail view {ID}` — Action menu includes "Resolve a note" when open notes are present.
