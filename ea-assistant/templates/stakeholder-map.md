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

The Stakeholder Map identifies all stakeholders, their interests, influence, and required
level of engagement. It is used to plan communications and ensure architecture decisions
address the right concerns. Update throughout the engagement as new stakeholders are identified.

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

*This document was created using the EA Assistant plugin.*
