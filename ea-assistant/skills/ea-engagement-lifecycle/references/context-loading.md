# Full Engagement Context Loading

Reference protocol for loading complete engagement context before performing analysis.
Used by `ea-grill`, `ea-review`, `ea-consistency`, `ea-interview`, and `ea-brainstorm`.

All paths are relative to `EA-projects/{slug}/`.

---

## Scope A — Artifact-scoped context

**Used by:** `ea-grill`, `ea-review`, `ea-interview` (artifact mode)

For a given `artifactId` and its `phase`:

1. Read the focal artifact (`artifacts/{phase-folder}/{artifact-id}.md`)
2. Read all artifacts listed in the focal artifact's `relatedArtifacts` frontmatter field (resolve each to its file path)
3. Read all artifacts in `artifacts/cross-cutting/` (Risk Register, Decision Register, ADR Register, Zachman)
4. Read `artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md` if it exists
5. Read all files in `artifacts/{phase-folder}/notes/interviews/` matching `interview-{artifact-id}-*.md`
6. Read all files in `artifacts/{phase-folder}/notes/reviews/` matching `grill-{artifact-id}-*.md`
7. Read `ResearchAndReferences/research-index.md`; for each item tagged with this phase or a topic matching the artifact type, read the full item file
8. **Load detail files:** Scan all tables in the focal artifact for `[→](../details/{ID}.md)` links. For each linked file that exists at `artifacts/details/{ID}.md`, read it and include its content as supplementary context for that item.

Announce the loaded context before proceeding:
```
Context loaded: {N} related artifacts · {N} interview notes · {N} brainstorm sessions · {N} review files · {N} research items · {N} detail files
```

If none of a category exist, omit it from the announcement (e.g. "Context loaded: 2 related artifacts · 1 research item").

---

## Scope B — Phase-scoped context

**Used by:** `ea-interview` (phase mode), `ea-brainstorm`

For a given `phase`:

1. Read all artifacts in `artifacts/{phase-folder}/*.md` (exclude any path containing `/notes/`)
2. Read all artifacts in `artifacts/cross-cutting/` (excluding `notes/`)
3. Read `artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md` if it exists
4. Read all files in `artifacts/{phase-folder}/notes/interviews/`
5. Read `ResearchAndReferences/research-index.md`; read full content for items tagged with this phase

Announce:
```
Context loaded: {N} phase artifacts · {N} interview notes · {N} brainstorm sessions · {N} research items
```

---

## Scope C — Full engagement context

**Used by:** `ea-consistency` (Full mode)

1. Glob `artifacts/**/*.md`; exclude paths containing `/notes/`
2. Glob `artifacts/**/notes/interviews/*.md`
3. Glob `artifacts/**/notes/brainstorm/brainstorm-notes.md`
4. Glob `artifacts/**/notes/reviews/*.md`
5. Read `ResearchAndReferences/research-index.md` and all linked item files
6. Glob `artifacts/details/*.md` — read all detail files

Announce:
```
Full context loaded: {N} artifacts · {N} note files · {N} research items
```

---

## Using loaded context

Apply loaded context as follows — do not surface it passively; use it to inform questions, flag gaps, and surface contradictions:

| Document type | How to use |
|---|---|
| Related artifacts | Cross-reference ID labels, goal text, and decisions — flag inconsistencies (e.g. G-001 labelled differently across artifacts) |
| Brainstorm notes | Concerns or assumptions the user surfaced — check whether they are addressed in the artifact; if not, flag the gap |
| Interview notes | Prior captured answers — flag divergence when artifact content contradicts what was answered in an interview session |
| Review / grill files | Prior critique findings — check whether recommended revisions from earlier grills were actually applied |
| Research items | External evidence — surface findings that support or contradict artifact claims; cite the item title and the specific claim |
| Detail files | Extended narrative, rationale, risks, costs, issues, concerns, impact, and alternatives for individual items — use when asking deep questions about an item or when a stakeholder raises a concern about it; cite as `[detail: {ID}]` |

**Citation format:** When referencing loaded context in output, use short inline citations:
- `[interview {date}]` — from a dated interview notes file
- `[brainstorm session {N}]` — from a brainstorm notes session block
- `[review {date}]` — from a grill review file
- `[research: {item-title}]` — from a research library item
- `[detail: {ID}]` — from a detail file for a specific engagement item
