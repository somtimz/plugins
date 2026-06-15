---
name: ea-council
description: Convene the ARB council — a multi-member review panel (planner, security, budget, architect, innovator, conservative) that each examine a subject through one mandate and vote, producing a consolidated verdict for the Architecture Review Board
argument-hint: "[artifact-id | phase <X> | adr ADR-NNN | --all] [--quick] [--member <key>]"
allowed-tools: [Read, Write, Bash, Glob, Grep]
---

You are executing the `/ea-council` command. Load the `ea-arb-council` skill for the panel logic; the council membership is data in `skills/ea-engagement-lifecycle/references/arb-council-roster.md`.

## Overview

`/ea-council` convenes a multi-viewpoint review **panel**. Unlike `/ea-grill` (one deep critique of one artifact) or `/ea-lens` (one practitioner's eight lenses), the council runs several independent specialist members — each judging the subject through a single mandate — and **synthesises their votes into a consolidated verdict** with points of contention and conditions. It is the analytic engine behind an ARB review; `/ea-arb council` records its output into the meeting minutes.

This command resolves the engagement, scope, and context, runs the skill, presents the verdict, and offers to persist it. The skill owns the member logic and the synthesis (no duplicated logic — see `CLAUDE.md`).

---

## Step 1 — Resolve Active Engagement

> Resolve the active engagement per `skills/ea-engagement-lifecycle/references/engagement-resolution.md`.

## Step 2 — Resolve Scope

Parse the argument into the **subject** under review:

| Argument | Subject |
|---|---|
| `{artifact-id}` (e.g. `architecture-vision`) | that single artifact |
| `phase <X>` (e.g. `phase A`) | all artifacts whose `phase` is X |
| `adr ADR-NNN` | that ADR plus the artifacts it is referenced by |
| `--all` or no argument | the whole engagement |

## Step 3 — Load Context

If `--quick` is set: **skip the deep read** and pass `engagement.json` state + the artifact list only.

Otherwise read the in-scope artifact `.md` files under `EA-projects/{slug}/artifacts/`, excluding `*.review.md` and generated registers (`decision-register*.md`, `risk-register*.md`, `concerns-register*.md`, `adr-register*.md`, `change-register*.md`, `gap-register*.md`, `*-register*.md`). Also scan each in-scope artifact's `## Appendix A3`, `## Appendix A4`, and any `RIS-NNN`/`CST-NNN`/`POL-NNN`/`FIN-NNN`/`THR-NNN`/`PAD-NNN` tokens so members have their anchors. For the whole-engagement scope, use the same load+exclusions list as `/ea-lens` Step 2.

## Step 4 — Run the Council

Load the `ea-arb-council` skill. Pass the subject, the loaded context, the mode (full or `--quick`), and any `--member` filters. The skill runs each roster member (one section + vote each) and produces the `## Council Verdict` (panel table, tally, consensus, points of contention, conditions, consolidated recommendation).

## Step 5 — Present and Persist

Present the full report. Then offer:

```
What next?
  1. Save the council report to file
  2. Push findings to the reviewed artifact(s) and registers
  3. Record this council review in an ARB meeting
  4. Done
```

- **1 — Save:** write to `EA-projects/{slug}/artifacts/cross-cutting/notes/reviews/council-review-{scope}-{YYYY-MM-DD}.md` (scope = `engagement`, the artifact id, `phase-{X}`, or the ADR id), with frontmatter `artifact`, `scope`, `date`, `reviewer: ea-council`.
- **2 — Push findings (confirm-before-apply, one finding at a time):**
  - For each reviewed artifact, add unresolved member findings to its **Artifact Working Notes → Critiques** table — `| {#} | {section} | {finding} | ea-council / {member} | {YYYY-MM-DD} | Open |`.
  - Add stakeholder-facing concerns to **Appendix A4** as `CON-NNN` rows (Category, Status, Action/Owner). Before adding, read the existing A4 rows and skip any concern already present (matched by source `ea-council` or the same member name and finding text) to avoid duplicates if Option 3 is also selected.
  - For each **Security Analyst** or **Budget Analyst** finding flagged as a risk, offer to create a `RIS-NNN` entry via `/ea-risks add` (prefill statement from the finding, severity from the member's concern). Walk one finding at a time with `y/n/edit`.
- **3 — Record in ARB:** invoke the `/ea-arb council` write-back (Mode: Council in `commands/ea-arb.md`) — pick or create the target `ARB-NNN`, then write the `## Council Review` section, a Decisions row (Vote tally + Outcome), and conditions into the Actions Register.

## Handling `--quick`

When invoked with `--quick`: skip Step 3's deep read, run the skill in quick mode (Planner + Architect + verdict only), and label the output "(Quick mode — Planner + Architect only; run `/ea-council` for the full panel)".

## Handling `--member`

`--member <key>` (repeatable; matches a roster Key or Alias) runs only the named members and notes in the verdict that the panel was partial.
