---
artifact: Stakeholder Map
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Analysis
  audience: Architecture
  layer: Reference
  sensitivity: Confidential
  tags: [stakeholders, concerns, influence, phase-a]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Segmentation complete | ⚠️ Pending | |
| Power/interest grid populated | ⚠️ Pending | |
| Communication strategy defined | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Stakeholder Map identifies all stakeholders, their architectural concerns, level of influence, and the engagement strategy required for each. It ensures that architecture decisions address the concerns of the right people and that communications are targeted to the right audience. This is a living artifact — update it as new stakeholders are identified or influence patterns change.

**What to include:** Stakeholder identification (name/role), architectural concerns (CON-NNN references), power/interest classification, required engagement level (inform/consult/collaborate/decide), communication channel preference, and the current engagement status. The power/interest grid visualises priority stakeholders at a glance.

**Quality indicators:**
- Every identified concern (CON-NNN) is owned by a named stakeholder in this map — orphan concerns without owners are not managed
- High-power/high-interest stakeholders have explicit engagement strategies, not just "keep informed"
- The map is updated when significant stakeholder changes occur (new sponsor, team restructure, key stakeholder departure)

**Common mistakes:**
- Stakeholder map that only lists the obvious named contacts — the most influential stakeholders are sometimes informal (a technical lead, a long-tenured SME, a politically connected manager)
- "Keep informed" as a strategy for all stakeholders — this homogenises engagement and fails to secure active support from decision-makers
- Creating the stakeholder map once in Phase A and never revisiting it — stakeholder influence shifts significantly as the engagement progresses into delivery

**TOGAF reference:** TOGAF 10 Part III, Phase A (§25.3) — Stakeholder Management. Stakeholder identification and concern management is a core Phase A activity; the Stakeholder Map is the primary artifact.

</details>

<details>
<summary>💡 Practitioner Tip — Stakeholder Engagement</summary>

- **Co-create the vision with business leaders** — stakeholders who help build the vision own it; those who receive it resist it. (Tip #33)
- Map stakeholders by **power and interest**, not just by title — a senior executive with no interest in your scope is less relevant than a mid-level manager who controls a critical resource. (Tip #31)
- **Speak the language of the audience** — executives want outcomes and risks; delivery teams want constraints and patterns. (Tip #32)
- Build **informal networks** to drive adoption — lunch-and-learns, pairing with engineers, Slack channels for quick advice. (Deep tactic #46)
- Make architecture **visible and accessible** — a new engineer should find and understand standards in under 30 minutes. (Deep tactic #47)
- Influence team structures, not just system structures — **Conway's Law is a lever**, not a constraint. (Deep tactic #48)
- Reward alignment with architecture, not just delivery speed. (Deep tactic #49)
- **Use strategic tension** to drive urgency — quantify the gap between current and desired state. (Deep tactic #50)

</details>

# Stakeholder Map

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Overview of the stakeholder landscape, key relationships, and engagement approach for this architecture programme.
Diagram: Influence/interest grid or RACI summary
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Stakeholder Register

<details>
<summary>📋 Guidance</summary>

List every stakeholder who has an interest in or influence over the architecture.
Include both supporters and potential resistors.

</details>

| ID | Name | Role / Title (ROLE-NNN) | Organisation Unit | Interest | Influence | Engagement | Details |
|---|---|---|---|---|---|---|---|
| S001 | {{name}} | {{role}} (ROLE-NNN) | {{unit}} | {{interest}} | High/Med/Low | Sponsor/Responsible/Consulted/Informed | — |

---

## Stakeholder Concerns

<details>
<summary>📋 Guidance</summary>

For each key stakeholder, describe their primary architecture concerns.
These become the basis for architecture viewpoints and artifact selection.

</details>

### {{stakeholder_name}}
- **Primary concern:** {{concern}}
- **Key questions:** {{questions}}
- **Artifacts addressing this concern:** {{artifact_refs}}

---

## Influence / Interest Matrix

<details>
<summary>📋 Guidance</summary>

Plot stakeholders on a 2x2 matrix: Influence (y-axis) vs Interest (x-axis).
- High influence, high interest: Manage closely
- High influence, low interest: Keep satisfied
- Low influence, high interest: Keep informed
- Low influence, low interest: Monitor

</details>

```
High Influence │ Keep Satisfied  │ Manage Closely
               │                 │
               │ {{stakeholder}} │ {{stakeholder}}
───────────────┼─────────────────┼────────────────
Low Influence  │ Monitor         │ Keep Informed
               │                 │
               │ {{stakeholder}} │ {{stakeholder}}
               └─────────────────┴────────────────
                    Low Interest      High Interest
```

---

## Communication Plan

<details>
<summary>📋 Guidance</summary>

Define how and when each stakeholder group will be engaged.

</details>

| Stakeholder Group | Communication Method | Frequency | Owner |
|---|---|---|---|
| {{group}} | {{method}} | {{frequency}} | {{owner}} |

---

## Artifact Working Notes

> Working-layer: persists across reviews. Populated by `/ea-grill` (Critiques), `/ea-review` (Comments), and manually. Never exported to Word/PPTX — stripped by `/ea-generate`.

### Comments

*Ad-hoc notes from architects, reviewers, or stakeholders.*

| Date | Author | Note |
|---|---|---|
| — | — | — |

### Critiques

*Formal findings from `/ea-grill` or `/ea-review` that require a response before this artifact can be approved.*

| # | Section | Finding | Source | Date | Status |
|---|---|---|---|---|---|
| — | — | — | — | — | Open |

### Exceptions

*Formal exceptions granted to a standard, principle, or compliance rule — each must have a rationale and approver.*

| # | Rule / Principle Waived | Rationale | Approver | Date |
|---|---|---|---|---|
| — | — | — | — | — |

### Outstanding Tasks

*Things that must be completed before this artifact can move to Approved status.*

- [ ] *(Add tasks — e.g. "Populate §3 Assumptions before Phase B sign-off")*

*This document was created using the EA Assistant plugin.*
