# Migration Gap Catalogue

Reference for `/ea-migrate`. Defines all gap checks, severity levels, and remediation actions.

## 3a — engagement.json Schema Gaps

| Check | Gap if… | Severity |
|---|---|---|
| `pluginVersion` field present | Field absent | Low |
| `lastMigratedVersion` field present | Field absent | Low |
| `direction` field present | Absent (pre-0.4.0) | Medium |
| **`direction` is concept-keyed** | `direction` is **domain-keyed** — has keys `Business`/`Data`/`Application`/`Technology`/`Motivation` instead of `vision`/`mission`/`drivers`/`goals`/… (legacy pre-0.9.x structure) | **Medium** |
| `direction.opportunities` field present | Absent (pre-0.9.77) | Low |
| `direction.gaps` field present | Absent | Low |
| `metrics` field present | Absent (pre-0.5.0) | Low |
| **`metrics` is a flat array** | `metrics` is a **domain-keyed object** (`{Business:[],Data:[],…}`) instead of a top-level array (legacy) | **Medium** |
| `engagementType` field present | Absent (pre-0.2.0) | Low |
| `architectureDomains` field present | Absent (pre-0.2.0) | Low |
| `optOuts` field present | Absent (pre-0.8.0) | Low |
| `architectureLevel` field present | Absent (pre-0.9.28) | Low |
| `schemaVersion` field present | Absent (pre-0.9.59) | Low |
| `migrations` field present | Absent (pre-0.9.59) | Low |
| `policies` field present (top-level) | Absent | Low |
| `finance` field present (top-level) | Absent (pre-0.9.66) | Low |
| `adoptedRAs` field present | Absent (pre-0.9.54) | Low |
| `localRA` field present | Absent (pre-0.9.54) | Low |
| `constraintsRepoPath` field present | Absent | Low |
| `requirements-index.json` scope values use Enterprise/Program | `scope: "Corporate"` or `"Project"` found (pre-0.9.35) | Low |

**Field locations (canonical):** `direction` is **concept-keyed** (`vision`, `mission`, `drivers[]`, `goals[]`, `objectives[]`, `strategies[]`, `issues[]`, `problems[]`, `opportunities[]`, `gaps[]`). `metrics[]`, `policies[]`, and `finance[]` are **top-level** arrays (siblings of `direction`, not inside it) — this matches the read paths in the register commands (`/ea-goals` reads `direction.goals[]`; `/ea-policies` reads top-level `policies[]`; `/ea-finance` reads top-level `finance[]`).

**Remediations:**
- `pluginVersion` absent → add `"pluginVersion": "{current_version}"`
- `lastMigratedVersion` absent → add `"lastMigratedVersion": "0.0.0"`
- `direction` absent → add concept-keyed object: `{ "vision": "", "mission": "", "drivers": [], "goals": [], "objectives": [], "strategies": [], "issues": [], "problems": [], "opportunities": [], "gaps": [] }`
- **`direction` domain-keyed → flatten to concept-keyed** (lossless): collect `goals`/`objectives`/`strategies` from every domain bucket (`Business`/`Data`/`Application`/`Technology`) **and** from `Motivation`; take `vision`/`mission`/`drivers`/`issues`/`problems` from `Motivation`. Each item already carries its own `domain` field, so the bucket key is redundant — discard it. **Guard:** before writing, assert all IDs are unique across buckets and that no bucket holds keys other than the known ones (`goals`/`objectives`/`strategies` per domain; `vision`/`mission`/`drivers`/`issues`/`problems`/`goals`/`objectives`/`strategies` for `Motivation`). If either check fails, **abort and report** — do not write. Snapshot `engagement.json` first (per "Snapshot Before Restructure").
- `direction.opportunities`/`direction.gaps` absent → add `[]` to `direction`
- `metrics` absent → add top-level `"metrics": []` (a **flat array**, not an object)
- **`metrics` domain-keyed object → flatten to top-level array** (lossless): concatenate every domain bucket's entries into one `metrics[]`; each entry already carries `domain`. Same uniqueness guard and snapshot as above.
- `engagementType` absent → add `"engagementType": null`
- `architectureDomains` absent → add `"architectureDomains": ["Business","Data","Application","Technology"]`
- `optOuts` absent → add `"optOuts": []`
- `architectureLevel` absent → add `"architectureLevel": null`; inform: "Set this via `/ea-details edit` (or `/ea-config metadata`) — allowed values: Strategic, Segment, Capability, Solution. Defaults to Segment until set."
- `schemaVersion` absent → add `"schemaVersion": 1` (current schema version per `engagement-schema.md`)
- `migrations` absent → add `"migrations": []` (the current run appends its audit entry in Step 7)
- `policies` absent → add top-level `"policies": []`
- `finance` absent → add top-level `"finance": []`
- `adoptedRAs` absent → add `"adoptedRAs": []`
- `localRA` absent → add `"localRA": { "nextId": 1 }`
- `constraintsRepoPath` absent → add `"constraintsRepoPath": ""`
- Legacy scope values (`Corporate`/`Project`) → rename all `"Corporate"` → `"Enterprise"` and `"Project"` → `"Program"` in `requirements-index.json`. Non-destructive; no content change.

## 3b — Expected Artifacts Missing

| Artifact | Introduced in | Severity if absent |
|---|---|---|
| Engagement Charter (`engagement-charter`) | 0.9.5 | Medium |
| Governance Framework (`governance-framework`) | 0.9.4 | Low |

**Remediation:** Do NOT auto-create artifacts — they require interview input. Offer: "Would you like to create this artifact now? (`/ea-artifact create {artifact-id}`)"

## 3c — Artifact Frontmatter Gaps

For each artifact `.md` in `EA-projects/{slug}/artifacts/` and phase subdirectories (excluding `*.review.md`, registers, session logs):

| Check | Gap if… | Introduced in | Severity |
|---|---|---|---|
| `taxonomy:` block present with all 5 sub-fields | Block absent or incomplete | 0.9.4 | Medium |
| `templateVersion:` field present | Field absent | 0.9.5 | Low |
| `complianceNote` not set to `accepted-non-standard` | Flag for review only | — | Info |

**Taxonomy remediation:**
1. Look up artifact type from `artifact:` frontmatter field
2. Find canonical taxonomy from `skills/ea-artifact-templates/references/taxonomy.md`
3. If found: present canonical values for confirmation; inject `taxonomy:` block after `templateVersion:` (or after `version:` if `templateVersion` also absent)
4. If not found: present blank taxonomy block; ask user to fill in values

**templateVersion remediation:** Inject `templateVersion: 0.0.0` to signal pre-versioning origin.

## 3d — Phase-Organized Artifact Structure

| Check | Gap if… | Introduced in | Severity | Remediated by |
|---|---|---|---|---|
| Artifact files in `artifacts/{phase-folder}/` | Any `artifacts[]` entry has file path directly in `artifacts/` (flat) | 1.0.0 | Medium | `/ea-migrate --reorganize` |
| `relatedArtifacts:` field present | Field absent | 1.0.0 | Low | `/ea-migrate` |
| `diagrams:` field present | Field absent | 1.0.0 | Low | `/ea-migrate` |
| `links:` field present | Field absent | 1.0.0 | Low | `/ea-migrate` |

**Flat-path detection (GAP-M-015):** Count artifacts with flat paths and report the total. Do **not** offer to move them here — direct the user to `/ea-migrate --reorganize` for all file moves.

**Missing fields remediation (GAP-M-016):** Inject `relatedArtifacts: []`, `diagrams: []`, `links: []` after the `tags:` line in the taxonomy block. Non-destructive — safe to auto-apply.

## 3e — Rules File Gap

| Check | Gap if… | Introduced in | Severity |
|---|---|---|---|
| `.claude/rules/ea-engagement.md` exists | File absent | 0.9.12 | Low |
| `CLAUDE.md` contains `## Where to Find Content` | Section absent (old-format fat CLAUDE.md) | 0.9.12 | Medium |

**Rules file remediation:** Create `.claude/rules/ea-engagement.md` from `templates/seeds/engagement-rules.md` with current engagement name and slug.

**CLAUDE.md remediation:** Regenerate `CLAUDE.md` from `templates/seeds/engagement-claude-md.md` using current `engagement.json` state. Full strategic data is not lost — it remains in `engagement.json → direction` and artifact files.

## 3f — Artifact Content Gaps

| Check | Artifact Types | Gap if… | Introduced in | Severity |
|---|---|---|---|---|
| `## Appendix A3 — Decision Log` present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Roadmap, SAoW, Migration Plan | Section absent | 0.7.0 | Medium |
| `## Appendix A4 — Stakeholder Concerns & Objections` present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Roadmap, SAoW, Migration Plan, Engagement Charter, Governance Framework, Implementation Governance Plan | Section absent | 0.9.3 | Medium |
| `## Appendix A5 — Related Architecture Decisions` present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Architecture Roadmap, SAoW, Migration Plan, Compliance Assessment, Requirements Register, Engagement Charter, Governance Framework, Implementation Governance Plan | Section absent | 0.9.7 | Low |

**Appendix remediation:** See `skills/ea-artifact-templates/references/appendix-templates.md` for the markdown blocks to inject. Ordering: A3 → A4 → A5. Place each missing appendix after any existing lower-numbered appendix, or before any existing higher-numbered one. If none exist, append at the document end.

## 3i — Template Body Section & Guidance Gaps

Backfills body **sections** and `<details>📋 Guidance</details>` **blocks** that the artifact's current template defines but the existing artifact is missing — without ever modifying populated content. This is how artifacts created under an older template pick up sections and guidance added by later releases (e.g. a Related Matrices pointer, a new roll-up section, or guidance blocks the interview/grill/brainstorm skills consume).

**Strictly insertion-only.** 3i never edits, reorders, or deletes existing content. It only adds missing scaffolding (heading + guidance + empty placeholders) or a missing guidance block above an already-present heading. **Always excluded from `--auto`** — every insertion requires interactive per-section confirmation.

### Scope and exclusions

- **Applies to:** authored artifacts only. Resolve the template via the artifact's frontmatter `artifactId` → `templates/{artifactId}.md`. If no matching template exists, skip with `[Info]` (per the Non-standard artifacts rule below).
- **Skip entirely (command-generated bodies — refresh by re-running the generating command, not by backfilling):** any artifact with a `generated:` frontmatter field, or whose `artifactId` matches `*-register`, `*-matrix`, `decision-register`, `cost-model-register`, `traceability-matrix`, `zachman-diagram`, `role-catalogue`, `consolidated-report`, or `cross-cutting-index`. For these, structure is owned by the generating command (`/ea-risks`, `/ea-matrix`, `/ea-strategies generate`, etc.).
- **Out of scope (handled elsewhere):** the author-only `## Compliance Checklist` block, the `# Title` H1, and Appendices A3/A4/A5 (covered by 3f).

### Detection

| Check | Gap if… | Severity |
|---|---|---|
| Template body section present in artifact | A `## {Section}` heading in the template body is absent from the artifact | Low |
| Section guidance present | A section exists in both, but the template's copy has a `<details>📋 Guidance</details>` block and the artifact's does not | Info |

Heading match is case-insensitive on the heading text after the `## ` marker, ignoring trailing punctuation. A section the user renamed counts as present (do not flag a rename as missing — when unsure, flag `[Info]`, never auto-insert a duplicate).

### Remediation (per-section confirmation, insertion-only)

- **Missing section:** copy the template's full section verbatim (heading + guidance block + placeholders/tables). Insert it at the position that preserves template order — immediately **before** the first later template-section that *does* exist in the artifact; if none exist, immediately before the first Appendix (`## Appendix A3`) or `## Artifact Working Notes`; otherwise append at the document end. Preview the heading + first ~5 lines; confirm `y / n / skip / view` (view shows the full block).
- **Missing guidance block:** insert the template's `<details>📋 Guidance</details>` block immediately after the artifact's existing heading line, before any existing content. Confirm per block.
- **Never** touch populated content. If a heading exists with content beneath it, only the missing-guidance insertion (above the content) is permitted — the content itself is never read for replacement or edited.

### Approved artifacts

Warn before any 3i insertion on an `Approved` artifact:
```
⚠️ {artifact name} is Approved. 3i adds empty template scaffolding (headings, guidance, blank
placeholders) — populated content is never changed and reviewStatus stays Approved. New empty
sections may warrant re-review. Proceed with this insertion? (y/n)
```

## Snapshot Before Restructure (applies to 3j and 3k)

Unlike 3a–3i, the **3j and 3k** remediations relocate **populated** content — they can lose or misfile authored work if they go wrong. Before applying **any** 3j reorder or 3k move, snapshot every artifact that will be modified:

1. Copy the artifact to a `snapshots/` subfolder in its own directory, named `{artifact-id}-{YYYY-MM-DD}-pre-restructure.md` (append `-v2`, `-v3` if the name exists), per `skills/ea-artifact-templates/references/register-snapshot-convention.md`. Create `snapshots/` if needed.
2. Announce it: `"Snapshot saved: {path} — revert with a copy-back if needed."`
3. Only then apply the change.

**Content-preservation verification (mandatory):** after a 3j reorder, the multiset of section blocks (heading + body, verbatim) must be identical before and after — only their order changes. After a 3k move, the moved block must appear in exactly one place across the source and destination (never zero, never duplicated). If verification fails, restore from the snapshot and report the failure — never leave a half-applied move.

## 3j — Section Ordering Gaps

Reorders **existing** sections of an artifact to match the order its current template defines. Runs only on sections present in both the artifact and the template (3i handles missing ones — run 3i first). **Whole-section atomic moves only:** a section is its `## {heading}` line plus everything until the next `## ` heading; the block moves verbatim. Severity **Low**. **Excluded from `--auto`.** Same authored-artifact scope and command-generated exclusions as 3i.

### Detection

Build the template's canonical `## ` section order (body sections only — exclude the author-only `## Compliance Checklist`, the `# Title`, and the trailing Appendices A3/A4/A5 + `## Artifact Working Notes`, which are always last). Build the artifact's order of the same sections. If the artifact's relative order differs from the template's, flag `[Low]` with the specific out-of-order sections.

Appendices and Working Notes keep their fixed trailing order (A3 → A4 → A5 → Working Notes) and are never reordered into the body.

### Remediation (per-artifact confirmation)

1. Show the before/after **heading order** (headings only — not the full bodies):
   ```
   Reorder business-architecture.md sections to template order?
     current: Executive Summary · Organisation Model · Business Context · …
     template: Executive Summary · Business Context · Organisation Model · …
   Only the order of existing sections changes; all content is preserved. (y / n / skip)
   ```
2. Warn that the author may have reordered intentionally: "If this ordering was deliberate, skip."
3. On confirm: snapshot (above), move whole-section blocks to template order, run the preservation check.

**Approved artifacts:** 3j is permitted on an `Approved` artifact with explicit confirmation — it changes only section *order*, not content (the preservation check guarantees this), so `reviewStatus` stays `Approved`; offer re-review as optional. This is an explicit exception to the general "only metadata/appendix changes on Approved artifacts" rule, justified by the content-preservation guarantee.

## 3k — Misplaced Content (heuristic, user-confirmed moves)

Surfaces content that likely belongs in a **different section** (within the document) or a **different artifact**, and proposes a move. **Heuristic and advisory** — every move is user-confirmed; nothing is inferred-and-applied. Severity **Info**. **Excluded from `--auto`.** Conservative, high-precision patterns only — when unsure, do not suggest.

### Detection patterns

| Pattern | Suggested destination | Move type |
|---|---|---|
| A `Risk`-titled section/table, or A4 rows with `Category = Risk`, in a non-Risk artifact | Risk Register (`/ea-risks`) | register registration (not raw paste) |
| Requirement-shaped statements ("the system must/shall …") in narrative body | Requirements Register (`/ea-requirements`) | register registration |
| A populated section that belongs to a different artifact type per the templates (e.g. a `Work Packages` section authored inside Architecture Vision) | the owning artifact (e.g. Architecture Roadmap) | cross-document block move |
| A block clearly under the wrong heading within the same doc (e.g. constraints listed under `Assumptions`) | the correct section in the same doc | within-document block move |

### Remediation (per-move, user-confirmed)

For each suggestion, show: the source block (or its first lines), the proposed destination, the confidence, and the rationale. Then:

- **Register registration** (Risk/Requirements/Decision targets): do **not** paste raw markdown into a register — registers are command-owned. Instead offer to run the register's `add` flow seeded from the block (e.g. `/ea-risks add` pre-filled), and once registered, replace the source block with a one-line pointer (`*Registered as RIS-NNN — see [[risk-register]]*`) only on confirm.
- **Cross-document block move** (narrative → narrative): snapshot **both** artifacts; insert the block into the destination's correct section (use 3i positioning rules); remove it from the source; replace the source location with an optional pointer line if the user wants one; run the preservation check across both files; flag any `[[links]]`/IDs that referenced the moved block as needing update.
- **Within-document block move:** snapshot the artifact; move the block under the correct heading; preservation check.

Confirm options per move: `y / n / skip / edit-destination`. If the user declines, leave everything untouched.

### Approved artifacts

3k moves change populated content, so on an `Approved` artifact warn and require explicit confirmation; moving content out of an Approved artifact should set its `reviewStatus` back to `Needs Revision` (a moved block is a material change) — confirm this with the user before applying.

## Handling Special Cases

**Non-standard artifacts:** If `artifact:` field does not match a known template type, flag `[Info]` — not a migration error. Do not attempt canonical taxonomy. Suggest manual review or `/ea-grill artifact`.

**Approved artifacts:** Warn before writing:
```
⚠️ {artifact name} is Approved. This remediation only adds metadata (taxonomy/templateVersion) or appends
empty appendix tables — content sections are not changed. The reviewStatus will remain Approved. Proceed? (y/n)
```
Only structural metadata additions are permitted on Approved artifacts **by 3a–3i**. The body-restructure checks **3j and 3k define their own Approved handling** (see their sections): 3j reorders with content preserved (reviewStatus stays Approved); 3k moves populated content and sets reviewStatus to `Needs Revision`. Both require explicit confirmation and a snapshot.
