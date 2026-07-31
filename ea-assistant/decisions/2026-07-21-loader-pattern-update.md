# Decision: Redirect EA-assistant loaders to specific subfile paths

**Date:** 2026-07-21
**Status:** Decided / Implementing
**Scope:** `ea-assistant` plugin — loaders in `commands/`, `agents/`, and `skills/` that point at the post-split reference files

---

## Decision

For each loader that names one of the seven reference files split on 2026-07-18 (decision: `decisions/2026-07-18-reference-file-efficiency.md`), route the load to one of two targets:

| Loader kind | Target |
|---|---|
| **Discovery load** (no phase / no concept named) | The **index** (e.g. `ea-concepts.md`, `adm-phase-guide.md`) — the index is the right surface for "show me the map" |
| **Scoped load** (specific phase, concept family, or numbered tip named in the same line) | The **specific subfile** (e.g. `concept-families/motivation-concepts.md`, `phase-questions/phase-a---architecture-vision-interview.md`, `practitioner-tips/part-i-...md`) |

Reject the rule "always load the index and discover from there." That rule kept the index-Read in every prompt and put the agent through an unnecessary second load (the subfile) for the actual content.

---

## Context

The 2026-07-18 split created seven sets of index + subfile pairs totalling 65 new files. The split's stated goal was reducing per-prompt context cost — agents load only the relevant subfile. The decision journal explicitly left a `[ ] Cross-references in remaining agent/command files reviewed and updated where a specific concept is named` checkbox unchecked.

A subsequent `/simplify` review on 2026-07-21 confirmed that ~50 call sites in `commands/`, `agents/`, and `skills/` still pointed at the old monolithic paths. Many were scoped loads — e.g. `commands/ea-goals.md` line 8 says "For the Goal concept and its distinctions from Driver/Objective/Strategy, read `ea-concepts.md`" — and loaded the 124-line index plus the model's inference of "where is Goal?" instead of the 429-line `concept-families/motivation-concepts.md` that carries the Goal definition.

The split had also surfaced the limitation that the loader rule was never made explicit; the absence of a rule meant that the original 2,030-line monolithic file was replaced by a 124-line index plus 6 family files, but the call-site pattern still routed every concept through the index, so the only saving was the 1,906 lines that moved out of the index — none of the saving that came from agents loading *only* the relevant concept.

---

## Alternatives considered

1. **Leave the call sites as-is** — smallest change, but the context-cost reduction promised by the 2026-07-18 split is only partially realised. The decision's stated goal (smaller per-prompt loads) is not met for scoped tasks.
2. **Always load the index** (option rejected below in the rejection note) — even smaller change, but never narrower than #1 and strictly worse for scoped loads.
3. **Route every call site through a single `loader.json` data file** — programmatic consumers can resolve paths; but the existing pattern is prose-based ("read `ea-concepts.md`"), and converting loaders to consume JSON is a much larger refactor with no immediate payoff (no programmatic consumer reads `engagement-schema.json` either).
4. **Scoped-load rule + index-only for discovery (chosen)** — every existing call site can be classified into one of the two categories; the file path is in the same line as the concept/phase name it just referenced, so the redirect is mechanical.

---

## Reasoning

- **The routing is in the prose already.** `ea-goals.md` says "the **Goal** concept"; it already names Goal — it doesn't need the index to discover Goal.
- **Subfiles are smaller and single-purpose.** `concept-families/motivation-concepts.md` is the canonical source for Goal, Objective, Strategy, etc. Loading it directly saves the ~6-step look-up ("is Goal in business-layer? in motivation? let me scan the index…").
- **Discoverers stay cheap.** Pure discovery (no concept named, e.g. "show me what's in the concept map") keeps the index — that's what the index is for.
- **Mechanical, reviewable change.** Each redirect is one Edit. A reviewer can scan the diff and confirm intent matches content.

---

## Trade-offs accepted

- **More precise file lists in loader prose** — a future split that introduces a new concept family will need to update every command/agent that names a concept in that family. The 2026-07-18 split already had this property; the loader-pattern update makes the dependency explicit.
- **Service straddles families.** `commands/ea-services.md` and `ea-business-services-management/SKILL.md` need to load two family subfiles (Service is defined in both `architecture-products-concepts.md` and `governance-and-rules-concepts.md`). Pre-existing; not in scope to fix here.
- **Per-prompt context cost is harder to reason about from grep alone.** A loose rule ("use the index") was easy to enforce with grep; the scoped rule needs the model to read the loader language. Accepted because the model already does that — the rule changes where the pointer lands, not whether the model reads the prose.

---

## Updates / supersedes

- Marks the `[ ] Cross-references in remaining agent/command files reviewed and updated where a specific concept is named` checkbox in `decisions/2026-07-18-reference-file-efficiency.md` as done. Decision file's verification block should be updated in the same commit.
- Does **not** change the file structure created by the 2026-07-18 decision — only the loaders that consume those files.

---

## Verification

- [x] Frontmatter validation: 104 files, 0 errors, 0 warnings.
- [x] `engagement-schema.json` parses as valid JSON.
- [x] `grep -rn "<seven monolithic paths>" --include="*.md" commands/ agents/ skills/` returns no scoped loads — every match is either a discovery load or a reference inside a decision/plan/PRD doc (historical, kept verbatim).
- [x] Decision journal updated; new entry dated 2026-07-21.
- [ ] Manual spot-check of `/ea-goals`, `/ea-processes`, `/ea-services`, `/ea-capabilities`, `/ea-operatingmodel`, `/ea-interview phase preliminary`, `/ea-brainstorm`, `/ea-grill --skill practitioner`: each fires the loader pattern and reaches the same artifact state (no behaviour change — only context cost reduced).

---

## Categorisation table (per call site)

See the implementation plan at `/home/somtimz/.claude/plans/linked-waddling-boot.md` for the full per-file change list. Each redirect follows the discovery / scoped rule above. Three categories of "do not change" also recorded:

1. **Discovery loads** — kept on the index.
2. **Historical/docs** — `decisions/`, `docs/plans/`, `docs/PRD.md` reference the old paths; left verbatim for accuracy.
3. **Top-level prose** — `CLAUDE.md`, `README.md`, `docs/IMPLEMENTATION.md` rules rewritten to describe the new layout, not the old file.
