# Publish Quality Rules

Reference for `/ea-publish` (Steps 5b–5c), `/ea-review` (action f), and `/ea-consistency --quality`.

Defines all readability and content-quality checks with severity levels.

---

## Table Rules

| Check | Flag when… | Severity |
|---|---|---|
| Column count | Table has >8 columns | Warning |
| Row count | Table has >10 data rows | Advisory |
| Header-only table | Table has headers but zero data rows | Warning |

**Remediations:**
- Too many columns → split into two focused tables (e.g. identification fields + status fields) or convert to vertical key-value layout
- Too many rows → introduce sub-headings by category, or move detail rows to an annex
- Header-only → fill in data or remove the table (likely a placeholder)

---

## Diagram Rules

| Check | Flag when… | Severity |
|---|---|---|
| Broken image path | `![...](path)` or `![[file]]` where the resolved path / vault file does not exist | Blocking |
| Missing diagram | Artifact type is Architecture Vision, Business Architecture, Data Architecture, Application Architecture, or Technology Architecture and contains no `![...]` or `![[...]]` reference | Advisory |

**Remediations:**
- Broken path → fix the relative path or provide the diagram file
- Missing diagram → add a context or landscape diagram; use `../../diagrams/{name}.{ext}` convention

---

## Document Flow Rules

| Check | Flag when… | Severity |
|---|---|---|
| Section opens with table | A `## ...` heading is immediately followed by a table with no prose paragraph first | Advisory |
| Back-to-back sections | Two or more `## ...` headings appear with only a `---` separator and no prose between them | Advisory |
| Terminology inconsistency | A key term used as a table heading label or section title appears with different wording elsewhere in the same document | Advisory |

**Terminology consistency method:** Build a case-insensitive map of all distinct table column headers and section titles. Flag pairs where the edit distance is small (≤3) but the strings differ (e.g. "Cloud Platform" vs "Cloud Infrastructure"). Present both usages and ask which is canonical.

**Remediations:**
- Section opens with table → add one introductory sentence before the table explaining what the table covers
- Back-to-back sections → add a one-sentence transition at the end of the preceding section
- Terminology → standardise to one term; search-and-replace throughout the document

---

## Content Completeness Rules

| Check | Flag when… | Severity |
|---|---|---|
| Placeholder text | `{{...}}` patterns found in document body | Blocking |
| Unresolved markers | `TBD`, `TODO`, or `(TBD)` appears in document body (whole-word match) | Blocking |
| Not-answered fields | `⚠️ Not answered` appears in document body | Blocking |
| Guidance comments | Any HTML comment (`<!-- ... -->`) survives in the assembled output | Blocking |
| Empty appendix | A3, A4, or A5 appendix table contains only the row `*(no ... recorded)*` | Advisory |
| Missing Executive Summary | Artifact section contains no `## Executive Summary` heading | Advisory |

**Remediations:**
- Placeholder / TBD-TODO / Not-answered → resolve by editing the source artifact before re-publishing, or mark inline with `<!-- ⚠️ PUBLISH QUALITY ISSUE: placeholder not filled — {field description} -->`
- Guidance comments → stripped automatically during assembly (see `/ea-publish` "Strip plugin scaffolding"); flag only if any remain after stripping
- Empty appendix → advisory only; acceptable to publish if intentionally empty
- Missing Executive Summary → run `/ea-summary refresh {artifact-name}` to generate one

---

## Link Integrity Rules (publish-time)

| Check | Flag when… | Severity |
|---|---|---|
| Broken image path | Relative image path or `![[file]]` embed resolves to a non-existent file | Blocking |
| Broken internal anchor | After link rewriting, an `[text](#anchor)` target does not correspond to any heading in the consolidated document | Warning |
| External URLs | Any `[text](https://...)` | Not validated — skip |

**Anchor derivation:** heading text lowercased, spaces replaced by hyphens, punctuation stripped (e.g. `## Architecture Vision` → `#architecture-vision`).

---

## Severity Levels

| Level | Behaviour |
|---|---|
| **Blocking** | Must be resolved or explicitly deferred before the output file is written |
| **Warning** | Reported in Publication Quality Notes section; does not block output |
| **Advisory** | Reported inline in the quality scan; does not block output |
