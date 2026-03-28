---
artifact: Architecture Roadmap
engagement: {{engagement_name}}
phase: E/F
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<details>
<summary>📋 Guidance</summary>

The Architecture Roadmap lists individual work packages in priority order that together
deliver the Target Architecture. It evolves from Phase E (initial) through Phase F (refined)
and is updated in Phase H as change requests are processed.

</details>

# Architecture Roadmap

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Horizon:** {{time_horizon}}

---

## Strategic Alignment

<details>
<summary>📋 Guidance</summary>

Map this roadmap to the Goals, Objectives, and Strategies defined in Phase A. Every Goal and Strategy in the Architecture Vision should be traceable to at least one Work Package. Gaps in coverage should be flagged explicitly.

</details>

| ID | Goal / Objective / Strategy | Type | Addressed by Work Packages |
|---|---|---|---|
| {{G-001}} | {{goal_description}} | Goal | {{WP-NNN}} |
| {{OBJ-001}} | {{objective_description}} | Objective | {{WP-NNN}} |
| {{STR-001}} | {{strategy_description}} | Strategy | {{WP-NNN}} |

**Unaddressed items:** {{list_any_goals_objectives_strategies_not_covered_or_None}}

---

## Roadmap Overview

<details>
<summary>📋 Guidance</summary>

Provide a high-level timeline view. Reference a diagram if available.

</details>

*Reference diagram:* `../diagrams/{{roadmap_diagram}}`

---

## Work Packages

<details>
<summary>📋 Guidance</summary>

Each work package is a discrete unit of change that can be planned and resourced.
Work packages close gaps identified in the Gap Analysis.

</details>

### WP-001: {{work_package_name}}

| Field | Value |
|---|---|
| **ID** | WP-001 |
| **Description** | {{description}} |
| **Advances Goals / Objectives** | {{g_obj_ids}} |
| **Executes Strategies** | {{str_ids}} |
| **Closes Gaps** | {{gap_ids}} |
| **Addresses Requirements** | {{req_ids}} |
| **Phase / Wave** | Wave 1 / Wave 2 / Wave 3 |
| **Estimated Effort** | {{effort}} |
| **Dependencies** | {{dependencies}} |
| **Owner** | {{owner}} |
| **Status** | Proposed / Approved / In Progress / Complete |

---

## Transition Architectures

<details>
<summary>📋 Guidance</summary>

Define the intermediate states (plateaus) between baseline and target.
Each plateau should be a stable, usable architecture state.

</details>

| Plateau | Description | Target Date | Work Packages |
|---|---|---|---|
| Plateau 1 | {{description}} | {{date}} | WP-001, WP-002 |
| Plateau 2 | {{description}} | {{date}} | WP-003 |
| Target | {{target_description}} | {{date}} | All |

---

## Prioritisation

<details>
<summary>📋 Guidance</summary>

Explain the prioritisation criteria used to sequence work packages.

</details>

{{prioritisation_rationale}}

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>

Record all stakeholder concerns, objections, and tough questions raised about this artifact.
Sources include grill-me sessions, Architecture Review Board feedback, executive challenge
sessions, and sponsor meetings. For each concern, record whether it is addressed in existing
documentation (Addressed / Partially Addressed) or requires further action (Requires Attention).
Use `/ea-concerns` to aggregate unresolved items across all artifacts. Concerns that represent
a material risk should also be raised as RIS-NNN entries via `/ea-risks`.

</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

*This document was created using the EA Assistant plugin.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
