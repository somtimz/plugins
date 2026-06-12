# EA Engagement Rules Reference

## Purpose

This document is the canonical reference for the 12 engagement discipline rules that govern every EA project created by ea-assistant. These rules are adapted from software-engineering discipline to enterprise architecture artifact management. They are seeded into every engagement as `.claude/rules/ea-engagement.md` on `/ea-new` and backfilled on `/ea-open`.

Agents and commands should cite specific rules by number when surfacing guidance, review findings, or compliance gaps.

---

## Rule 1 — Think Before Artifacting

State assumptions explicitly. If uncertain about a concept classification, ask rather than guess.
- Present multiple interpretations when ambiguity exists (e.g., is this a Goal or a Strategy?).
- Push back when a simpler artifact structure exists.
- Stop when confused. Name what's unclear and cite `skills/ea-artifact-templates/references/ea-concepts.md`.

**When to cite:** During `/ea-interview` when the user describes something ambiguous; during `/ea-grill` when a concept is misclassified; during `/ea-artifact` authoring when the template is unclear.

---

## Rule 2 — Simplicity First

Minimum artifact content that solves the need. Nothing speculative.
- No sections beyond what the artifact template requires.
- No abstractions for single-use artifacts.
- Test: would a senior architect say this artifact is overcomplicated? If yes, simplify.

**When to cite:** When an artifact draft includes unnecessary sections; when a user asks for "just in case" content; during `/ea-grill` conciseness review.

---

## Rule 3 — Surgical Changes

Touch only the artifact or engagement files you must. Clean up only your own mess.
- Don't "improve" adjacent artifacts, comments, or formatting.
- Don't refactor artifacts that aren't broken.
- Match existing style, frontmatter structure, and section ordering — even if you'd do it differently.

**When to cite:** During `/ea-grill` when a review finding touches multiple artifacts; when a user asks to "clean up" unrelated files; during consistency checks.

---

## Rule 4 — Goal-Driven Execution

Define success criteria before authoring. Loop until verified.
- "Add a constraint" → "Write CST-NNN entry, verify it appears in Constraints Register, confirm traceability to at least one artifact."
- "Fix the gap analysis" → "Write test that reproduces the missing GAP-NNN link, then make it pass."
- "Refactor the Architecture Vision" → "Ensure T3-A3 and T3-A5-ADR compliance pass before and after."

**When to cite:** At the start of any multi-step artifact operation; when the user says "make it work" without defining done; during `/ea-grill` when success criteria are absent.

---

## Rule 5 — Use the model only for judgment calls

Use me for: classification, drafting, summarization, extraction, disambiguation.
Do NOT use me for: ID assignment, compliance scoring, link validation, deterministic transforms.
- If `engagement.json` or a register file can answer, read it — don't ask.
- If the compliance-check reference defines the rule, apply it — don't interpret.

**When to cite:** When an agent is about to generate IDs from scratch instead of reading the engagement register; when compliance is being eyeballed instead of checked against `compliance-check.md`.

---

## Rule 6 — Scope budgets are not advisory

Per-artifact: 4 sections or 4,000 tokens of net new content. Per-session: 30,000 tokens across all artifacts.
- If approaching budget, summarize and offer to continue in a fresh session.
- Surface the breach. Do not silently overrun.

**When to cite:** When an artifact is ballooning beyond its template scope; when a session has produced multiple large artifacts without checkpointing.

---

## Rule 7 — Surface conflicts, don't average them

If two artifacts contradict, pick one (more recent / more tested / higher reviewStatus).
- Explain why. Flag the other for cleanup via `/ea-consistency` or `/ea-engage-review`.
- Don't blend conflicting patterns into a muddled compromise.

**When to cite:** During `/ea-consistency` when contradictions are found; during `/ea-grill` when an artifact contains blended or contradictory statements.

---

## Rule 8 — Read before you write

Before adding an artifact or section, read:
- Existing artifacts in the same phase (to avoid duplication)
- `engagement.json` direction (to align with current goals, objectives, strategies)
- `skills/ea-artifact-templates/references/ea-concepts.md` (to use canonical definitions)
- `skills/ea-engagement-lifecycle/references/adm-phase-guide.md` (to confirm phase placement)
- `skills/ea-artifact-templates/references/compliance-check.md` (to know T3/T4 requirements upfront)

> "Looks orthogonal" is dangerous. If unsure why an artifact is structured a certain way, ask.

**When to cite:** When an agent creates an artifact without checking for existing ones; when a concept is defined inline instead of read from `ea-concepts.md`.

---

## Rule 9 — Compliance checks verify intent, not just structure

Tier 3 and Tier 4 checks must encode WHY the artifact matters, not just WHAT it contains.
- A compliance check that can't fail when business logic changes is wrong.
- T3-A3 checks that the Decision Log captures *who decided what and why*, not just that a section exists.
- T4-EVID checks that Evidence Assessment tables contain *sufficient* evidence, not just *any* evidence.

**When to cite:** During `/ea-grill` when a T3/T4 check is superficial (section exists but content is placeholder); during compliance remediation when structure is fixed but intent is still missing.

---

## Rule 10 — Checkpoint after every significant step

Summarize what was done, what's verified (against `engagement.json`, compliance rules, engagement direction), and what's left.
- Don't continue from a state you can't describe back.
- If you lose track, stop and restate.

**When to cite:** After any multi-step command (`/ea-interview`, `/ea-grill`, `/ea-generate`) to enforce a summary; when the conversation context has grown large.

---

## Rule 11 — Match engagement conventions, even if you disagree

Conformance > taste inside the engagement.
- Use the unified ID scheme (DRV-NNN, G-NNN, OBJ-NNN, RA-NNN, etc.) — never invent domain-prefixed variants.
- Follow the artifact frontmatter format: `relatedArtifacts`, `diagrams`, `links`.
- Use relative paths per the Artifact Link Conventions table.
- If you genuinely think a convention is harmful, surface it via `/ea-grill` or `/ea-engage-review`. Don't fork silently.

**When to cite:** When an artifact uses non-standard IDs, paths, or frontmatter; when a user asks to deviate from the established format.

---

## Rule 12 — Fail loud

"Completed" is wrong if anything was skipped silently.
"Compliance passes" is wrong if any T3/T4 checks were skipped.
- Default to surfacing uncertainty, not hiding it.
- If an artifact has unresolved concerns, flag it — don't mark it Approved.

**When to cite:** When an agent reports "done" but compliance checks were bypassed; when a review finding is marked resolved but the fix was incomplete; when an artifact is about to be marked Approved with open concerns.

---

## Quick Reference

| Rule | Key discipline | Violation smell |
|---|---|---|
| 1 | Ask, don't guess on concepts | Inline concept definitions; ambiguous classifications |
| 2 | Minimum viable artifact | Speculative sections; "just in case" content |
| 3 | Touch only what you must | Adjacent artifact "improvements"; style changes |
| 4 | Define done before starting | "Make it work"; no compliance target |
| 5 | Read registers, don't generate | Inventing IDs; guessing compliance |
| 6 | Budget is a hard limit | Ballooning artifacts; silent overrun |
| 7 | Pick one, explain why | Blended compromises; unresolved contradictions |
| 8 | Read before writing | Inline definitions; duplicate artifacts |
| 9 | Checks must test intent | Placeholder sections; structural only compliance |
| 10 | Summarize every step | Lost context; indescribable state |
| 11 | Follow conventions | Non-standard IDs; custom frontmatter |
| 12 | Surface every gap | "Done" with skipped checks; silent bypass |
