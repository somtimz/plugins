---
name: ea-arb-council
description: This skill should be used when the user asks to "convene the ARB council", "council review", "panel review", "review this through the council", or invokes /ea-council or /ea-arb council. Convenes a multi-member architecture review council — each member examines the in-scope subject through one mandate (feasibility, security, budget, design quality, innovation, prudence) and casts a recorded vote, then the skill synthesises a consolidated verdict.
version: 0.9.86
---

# EA ARB Council

You are rigorous and specific: every assessment cites concrete IDs, artifact names, and sections as evidence — never generic praise or vague concern.

The council membership is **data-driven**: read `skills/ea-engagement-lifecycle/references/arb-council-roster.md` and run exactly the members defined there, in order. Do not hardcode the roster. If the caller passed `--member <key>` (repeatable), run only the matching members; otherwise run all.

## Inputs (passed by the caller)

- **Subject / scope** — what is under review: a single artifact, a phase, a specific `ADR-NNN`, or the whole engagement.
- **Context** — `engagement.json` fields (name, currentPhase, full `direction`, metrics, artifacts list) plus the in-scope artifact content the caller loaded.
- **Mode** — full or `--quick`.
- **Member filter** — optional `--member` keys.

## Step 1 — Seat the council

Read the roster. For each member, note its **Mandate**, **Reads/Reuses** anchors, **Evaluation questions**, and **Vote criteria**. Load each member's anchored references/skills/registers **if present**; if an anchor is missing, the member still votes from available context and notes the missing input (load-if-present convention, as in `ea-architect-lens`).

## Step 2 — Run each member (one H2 section per member)

For each member, in roster order, produce a concise H2 section `## {Member} — {Vote}` containing:

- **2–5 sentences (or a tight list)** answering that member's Evaluation questions against the subject, each point citing specific evidence (IDs / artifact / section). Judge **only** through this member's mandate — do not stray into another member's concern.
- **Vote:** one of `Approve` · `Approve-with-conditions` · `Reject` · `Abstain`, chosen strictly by the member's Vote criteria. A `Reject` from a member whose roster entry marks it **blocking** (Security Analyst, Budget Analyst) is a blocking reject.
- **Top concern:** the single most important issue, in one sentence (or "None").
- **Conditions:** for `Approve-with-conditions` (or a `Reject` with a remedy), the specific change(s) that would move the vote to Approve. Each condition is concrete and actionable.

Do not pad. Do not restate the subject. Do not have members agree for the sake of agreement — the **Innovator** and **Conservative** are designed to pull in opposite directions on technology choices; let them.

## Step 3 — Synthesise the verdict

Produce a `## Council Verdict` section:

1. **Panel table** — one row per member:

   | Member | Vote | Top Concern | Conditions |
   |---|---|---|---|

2. **Tally** — count Approve / Approve-with-conditions / Reject / Abstain (voting members only; Abstain does not count for or against).

3. **Consensus** — the points the panel agrees on (strengths and shared concerns).

4. **Points of Contention** — where members split, with the trade-off stated for the board to adjudicate. **Always** reconcile the Innovator ⇄ Conservative split explicitly when both voted (e.g. "Innovator wants {X}; Conservative warns {Y} is unproven — the board must weigh future-proofing against delivery risk"). Surface any other split the same way.

5. **Conditions register** — the de-duplicated union of all members' conditions, each tagged with the member(s) that raised it. These become ARB Actions / decision conditions.

6. **Consolidated recommendation** — exactly one of:
   - **Endorse** — no Rejects; conditions (if any) are minor.
   - **Endorse with conditions** — no blocking Rejects; material conditions must be met. List them.
   - **Do not endorse** — one or more **blocking** Rejects (Security/Budget), or a majority of voting members Reject.
   - **Defer** — the subject is too incomplete for the panel to judge (multiple Abstains for "nothing in scope yet"); state what must exist first.

   State the rule that produced the recommendation in one line (e.g. "Blocking Reject from Security ⇒ Do not endorse").

## Step 4 — Hand back

Return the full report (member sections + verdict) to the caller. The caller (`/ea-council` or `/ea-arb council`) handles saving the report, writing back into ARB minutes, and proposing `RIS-NNN`/`CON-NNN`/Critiques — this skill does not write files.

## Quick mode

When `--quick` is set, run only the **Planner** and **Architect** members plus the **Council Verdict** synthesis (tally, contention, recommendation) from `engagement.json` state and the artifact list — no deep per-artifact read. Label the output: "(Quick mode — Planner + Architect only; run `/ea-council` for the full panel)".

## Reference files

The roster anchors each member to existing machinery — load these if available, proceed without them if not found:

- `skills/ea-engagement-lifecycle/references/arb-council-roster.md` — **required**; the membership and per-member mandates/criteria.
- `skills/ea-grill-skills/SKILL.md` — load **only** the `## Mode:` section(s) needed by the running member(s): `premortem` (Planner), `design`/`software-design`/`infra-design` (Architect), `finance` (Budget Analyst). Do not load the full file.
- `skills/ea-engagement-lifecycle/references/grill-scoring-rubric.md` — Quality dimension (Architect).
- `skills/ea-engagement-lifecycle/references/capability-based-planning.md` — readiness ceiling (Planner).
- `skills/ea-engagement-lifecycle/references/practitioner-tips.md`, `advanced-patterns.md` — Innovator framing.
- `skills/ea-engagement-lifecycle/references/failure-modes.md` — Conservative pattern-matching.
- `skills/ea-security/SKILL.md` — Security Analyst protocol (or defer to `/ea-security-review` / the `ea-security-auditor` agent for a deep pass).

Compliance rules the members apply (defined in `ea-assistant/CLAUDE.md`): **T4-TCO**, **T4-ECON** (Budget), **T4-OPTION** (Innovator), **T4-PREMAT** (Conservative).
