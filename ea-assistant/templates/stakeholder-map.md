---
artifact: Stakeholder Map
engagement: {{engagement_name}}
phase: Prelim/A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Stakeholder Map identifies all stakeholders, their interests, influence, and required
  level of engagement. It is used to plan communications and ensure architecture decisions
  address the right concerns. Update throughout the engagement as new stakeholders are identified.
-->

# Stakeholder Map

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Stakeholder Register

<!-- GUIDANCE:
  List every stakeholder who has an interest in or influence over the architecture.
  Include both supporters and potential resistors.
-->

| ID | Name | Role / Title | Organisation Unit | Interest | Influence | Engagement |
|---|---|---|---|---|---|---|
| S001 | {{name}} | {{role}} | {{unit}} | {{interest}} | High/Med/Low | Sponsor/Responsible/Consulted/Informed |

---

## Stakeholder Concerns

<!-- GUIDANCE:
  For each key stakeholder, describe their primary architecture concerns.
  These become the basis for architecture viewpoints and artifact selection.
-->

### {{stakeholder_name}}
- **Primary concern:** {{concern}}
- **Key questions:** {{questions}}
- **Artifacts addressing this concern:** {{artifact_refs}}

---

## Influence / Interest Matrix

<!-- GUIDANCE:
  Plot stakeholders on a 2x2 matrix: Influence (y-axis) vs Interest (x-axis).
  - High influence, high interest: Manage closely
  - High influence, low interest: Keep satisfied
  - Low influence, high interest: Keep informed
  - Low influence, low interest: Monitor
-->

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

<!-- GUIDANCE:
  Define how and when each stakeholder group will be engaged.
-->

| Stakeholder Group | Communication Method | Frequency | Owner |
|---|---|---|---|
| {{group}} | {{method}} | {{frequency}} | {{owner}} |

---

*This document was created using the EA Assistant plugin.*
