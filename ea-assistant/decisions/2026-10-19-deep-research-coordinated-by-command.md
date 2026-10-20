# Decision: Deep research is coordinated by `/ea-research deep`, not the `ea-research` agent

**Date:** 2026-10-19
**Status:** Decided / Implemented (v0.9.90)
**Scope:** `ea-assistant` plugin — `commands/ea-research.md`, `agents/ea-research.md`, new `agents/ea-researcher.md` and `agents/ea-research-writer.md`

---

## Decision

Deep research runs as the `deep` mode of `/ea-research`. The command plans the research, dispatches one `ea-researcher` subagent per subtopic in parallel, allows at most one gap round, and dispatches one `ea-research-writer` to produce the report. The report is saved to the research library as a new `report` item type, with the researchers' notes kept beside it in `ResearchAndReferences/research-notes/{slug}/`.

The `ea-research` agent keeps its quick, plan, synthesise, quality and impact modes. Asked for deep research, it returns a plan and hands off to the command.

---

## Context

Until 0.9.90 the `ea-research` agent ran deep research itself, in four phases, in one context: every search result, every fetched page and the report shared one window. It could not parallelise, because a subagent cannot dispatch subagents. It also set no bound on searches, and nothing stopped it citing a claim from memory.

The coordinator pattern from the `anthropic-skills:deep-research` skill fixes all three problems. The coordinator's context holds only the plan and the researchers' short summaries. Researchers work in parallel within a tool-call budget, each writing notes in which every finding carries a URL, and a separate writer drops any claim without one. Because the coordinator has to be the main conversation, it belongs in a command.

What we kept from the skill: clarify only when the answer changes the research; subtopics that do not overlap and together cover the question, with the researcher-count table; foreground parallel dispatch in one message; at most one extra round; notes on disk with Takeaway / Cited Findings / Inferences / Gaps; source evaluation (primary over aggregator, speculation flagged, conflicts stated); a BLUF report with signpost headers and inline citations; follow-up requests that build on an earlier report without overwriting it.

What we changed for EA: researchers carry the engagement's phase, target artifact and constraints; notes gain an EA Relevance section; the report adds engagement implications, a confidence table and next steps that name registers and commands; the plan is confirmed before dispatch, as the old deep mode did; the report lands in `research-index.md` so `apply`, Quality mode and Impact mode can use it.

---

## Consequences

- `/ea-research` needs `Agent`/`Task` and `AskUserQuestion` in `allowed-tools`. It does no searching itself.
- `apply` now writes the `📎 Source: ResearchAndReferences/{file}.md` marker that Impact mode already looked for and that nothing used to write.
- Engagements with no `report` items are unaffected. The index's `Type` column gains one value.
