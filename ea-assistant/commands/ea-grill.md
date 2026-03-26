---
name: ea-grill
description: Deep-review an EA artifact using a grill-me skill — stress-test, boardroom simulation, pre-mortem, decision critique, or design critique
argument-hint: "[artifact-name] [--skill stress-test|boardroom|premortem|decision|design|boardroom-strategy]"
allowed-tools: [Read, Bash]
---

Deeply review an EA artifact using a grill-me skill.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

---

### Step 1 — Identify the artifact

If an artifact name was provided as an argument, locate it in `EA-projects/{slug}/artifacts/`. If not specified, list all artifacts in the engagement and ask the user to select one.

---

### Step 2 — Select the grill-me skill

If `--skill` was provided, use that skill. Otherwise, recommend a skill based on artifact type using this table:

| Artifact | Recommended Skill | Reason |
|---|---|---|
| Architecture Vision | `grill-me-boardroom-strategy` | Needs strategic depth + board pressure + pre-mortem — the most comprehensive review |
| Statement of Architecture Work | `grill-me-decision` | A formal commitment — review as a decision memo |
| Architecture Principles | `grill-me-stress-test` | Each principle needs to survive assumption testing |
| Business Architecture | `grill-me-design` | Reviews for user needs, incentives, edge cases, and unintended consequences |
| Application Architecture | `grill-me-design` | Reviews for scalability, failure points, and integration friction |
| Data Architecture | `grill-me-design` | Reviews for data needs, access patterns, quality, and governance gaps |
| Technology Architecture | `grill-me-design` | Reviews for vendor lock-in, resilience, and operational realism |
| Architecture Roadmap | `grill-me-premortem` | Assumes delivery failure — surfaces sequencing risks and missed dependencies |
| Migration Plan | `grill-me-premortem` | Red-teams the migration — finds failure modes before they occur |
| Gap Analysis | `grill-me-stress-test` | Tests whether gaps are correctly identified and prioritised |
| Architecture Contract | `grill-me-decision` | Reviews the commitment and its governance implications |
| Compliance Assessment | `grill-me-boardroom` | Simulates a board / audit panel reviewing compliance posture |
| Stakeholder Map | `grill-me-design` | Tests whether stakeholder concerns, incentives, and engagement levels are realistic |
| Requirements Register | `grill-me-stress-test` | Tests whether requirements are complete, traceable, and achievable |
| Decision Register | `grill-me-decision` | Reviews whether decisions are defensible, owned, and governed |
| Business Model Canvas | `grill-me-boardroom-strategy` | Needs full strategic + commercial + execution review |

Confirm the skill with the user before proceeding, and offer the full list as alternatives.
The `--skill` argument accepts these short names (mapped to the full `grill-me-*` skill IDs):

| Short name | Skill ID | What it does |
|---|---|---|
| `stress-test` | `grill-me-stress-test` | Tests assumptions, surfaces risks, forces execution realism |
| `boardroom` | `grill-me-boardroom` | Board panel simulation: finance, operations, risk, reputation, employee impact, strategic fit |
| `premortem` | `grill-me-premortem` | Red-team assuming failure in 12 months: failure modes, warning signs, safeguards |
| `decision` | `grill-me-decision` | Decision memo extractor: options, criteria, tradeoffs, recommendation, next steps |
| `design` | `grill-me-design` | Design critique: user needs, failure points, edge cases, incentives, scalability |
| `boardroom-strategy` | `grill-me-boardroom-strategy` | Hybrid: depth + board pressure + pre-mortem (most thorough) |

---

### Step 3 — Load the artifact

Read the artifact file. Extract:
- The artifact type and phase
- All populated sections (skip empty `{{placeholder}}` fields)
- Any A3 Decision Log entries
- The current status, version, and review status from frontmatter

---

### Step 4 — Brief the reviewer

Before starting the grill, present a one-paragraph framing to the user:

```
## Artifact Grill — [Artifact Name] using [skill-name]

**Artifact:** [name] | **Phase:** [phase] | **Status:** [status] | **Version:** [version]
**Skill:** [skill description — one line]

I've loaded the artifact. I'll now act as [role from skill] and review it one question at a time.
After each of your answers I'll push back, identify weaknesses, and suggest stronger positions.
When the review is complete I'll produce a structured critique.

Ready? Here is my first question.
```

---

### Step 5 — Run the grill

Apply the selected grill-me skill, using the artifact content as the "proposal" being reviewed. You have full context of every section. Ask questions that specifically challenge the content of this artifact — do not ask generic questions that ignore what is written.

For example:
- If reviewing an Architecture Vision and the Business Drivers section lists only internal drivers, challenge whether external forces have been overlooked.
- If reviewing a Migration Plan and Wave 1 has no rollback procedure, ask directly about that gap.
- If reviewing an Architecture Principles artifact and a principle lacks an Implications section, probe whether the team understands the practical consequences.

Follow the selected skill's interviewing protocol exactly: one question at a time, with the question framing, recommended answer, and what a board member / critic / red-teamer would worry about.

---

### Step 6 — Produce the output

When the review is complete (or the user types `done` or `finish`), produce the skill's structured output as specified:

- **stress-test** → refined strategy summary, top 5 unresolved risks, hardest objection, next decision required
- **boardroom** → 10 toughest questions, weakest answers, board-ready 2-minute summary
- **premortem** → top failure modes, early warning signs, safeguards, proceed/pause/redesign verdict
- **decision** → decision statement, options analysis, recommendation, risks, next steps
- **design** → strengths, design flaws, recommended revisions, unresolved design bets
- **boardroom-strategy** → executive summary, case for proceeding, case against, top unresolved risks, next decision required, 2-minute board-ready version

Offer to save the output as a review note:
```
Save this grill output as a review file? (y/n)
File would be saved to: EA-projects/{slug}/reviews/grill-{artifact-id}-{skill}-{YYYY-MM-DD}.md
```

If the user confirms, write the file with a frontmatter header:
```yaml
---
artifact: [artifact-name]
skill: [grill-me-skill-used]
date: [YYYY-MM-DD]
reviewer: ea-grill
---
```
