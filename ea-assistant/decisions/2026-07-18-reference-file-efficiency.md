# Decision: Split long skill/reference files for efficiency

**Date:** 2026-07-18
**Status:** Decided / Implementing
**Scope:** `ea-assistant` plugin skill/reference files

---

## Decision

Split the longest skill/reference markdown files into focused sub-references with lightweight index pages, instead of keeping everything in monolithic files.

Files split:

| Original file | Lines | New structure |
|---|---|---|
| `skills/ea-artifact-templates/references/ea-concepts.md` | 2,030 | Index + 6 family files under `concept-families/` |
| `skills/ea-artifact-templates/references/phase-interview-questions.md` | 1,491 | Index + 13 phase files under `phase-questions/` |
| `skills/ea-engagement-lifecycle/references/adm-phase-guide.md` | 615 | Index + 10 phase files under `adm-phases/` |
| `skills/ea-artifact-templates/references/diagram-catalogue.md` | 522 | Index + 12 files under `diagram-catalogue/` |
| `skills/ea-artifact-templates/references/artifact-descriptions.md` | 787 | Compact table index + 10 phase files under `artifact-descriptions/` |
| `skills/ea-engagement-lifecycle/references/engagement-schema.md` | 489 | Annotated markdown index + `engagement-schema.json` |
| `skills/ea-engagement-lifecycle/references/practitioner-tips.md` | 526 | Index + 5 files under `practitioner-tips/` |

---

## Context

Prior work had already identified that `ea-concepts.md`, `phase-interview-questions.md`, `artifact-descriptions.md`, `adm-phase-guide.md`, `practitioner-tips.md`, `diagram-catalogue.md`, and `engagement-schema.md` were each several hundred to >2,000 lines. The repeated structure inside each file made it hard for agents and users to load only the relevant section, and every context window paid the cost of unused material.

---

## Alternatives considered

1. **Leave files as-is** — lowest risk, but no efficiency gain and context-window pressure remains.
2. **Convert to YAML/JSON data + renderer** — most compact for highly repeated patterns (e.g., practitioner tips), but introduces a rendering dependency and is overkill for prose-heavy reference material.
3. **Pure markdown split (chosen)** — keeps the existing toolchain (no new dependencies), preserves searchability, and is the same pattern already used for artifact templates and registers. Index pages restore the original lookup experience.

---

## Reasoning

- **Markdown split is the smallest step** that meaningfully reduces per-prompt context size.
- **Index pages** keep the original files useful as entry points; nothing needs to change in commands/agents that load the index.
- **JSON extraction for `engagement-schema`** gives programmatic consumers a canonical schema file while keeping human commentary in markdown.
- **Per-phase files** mirror the engagement `artifacts/` layout, making paths predictable.
- **No frontmatter changes** were required, so the existing CI validator passes unchanged.

---

## Trade-offs accepted

- Some agent/command references still point to the old `ea-concepts.md` and `practitioner-tips.md` paths. Where a specific concept is named, references were updated to the sub-file; generic "load canonical concepts" prompts intentionally remain on the index so they can discover the full concept family map.
- Slightly more files to maintain, but each file is smaller and single-purpose.
- The split was done on top of existing uncommitted work; the branch also carries the business-context/BMC concept updates and Operating Model promotion.

---

## Supersedes

- No prior decision on reference-file structure.

---

## Verification

- [x] Frontmatter validation: `~/.bun/bin/bun /mnt/d/dev/claude-sandbox/plugins/.github/scripts/validate-frontmatter.ts /mnt/d/dev/claude-sandbox/plugins/ea-assistant/` — 104 files, 0 errors, 0 warnings.
- [x] `engagement-schema.json` parses as valid JSON.
- [x] New index pages contain links to all sub-files.
- [ ] Cross-references in remaining agent/command files reviewed and updated where a specific concept is named.
