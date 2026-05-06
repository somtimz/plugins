---
artifact: Transition Architectures
engagement: {{engagement_name}}
phase: E/F
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.13
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Design
  audience: Architecture
  layer: Transition
  sensitivity: Internal
  tags: [transition, intermediate-state, phase-e, phase-f]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-A3 | ⚠️ Pending | |
| T3-A4 | ⚠️ Pending | |
| T3-ADR | ⚠️ Pending | |
| T3-RATIONALE | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

Transition Architectures define the intermediate architecture states between the Baseline
and the Target Architecture. Each Transition Architecture represents a coherent, deliverable
state of the enterprise that provides business value on its own — it is not merely a partial
target, but a stable and viable intermediate configuration.

Produced in Phase E (initial) and refined in Phase F (finalised with the Migration Plan).
Each transition state should correspond to one or more work packages in the Architecture Roadmap.

</details>

# Transition Architectures

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of the transition states between baseline and target: how many steps, and what is achieved at each.
Diagram: State-progression diagram: T0 → T1 → T2 → Target
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Overview

<details>
<summary>📋 Guidance</summary>

Describe the overall migration path: how many transition states are planned, the rationale
for the number and sequencing, and the key business drivers that shape the transition approach.

</details>

{{transition_overview}}

**Number of transition states:** {{transition_count}}

---

## Transition State Summary

| State | Name | Target Date | Key Capability Delivered | Supporting Work Packages |
|---|---|---|---|---|
| Baseline | Current State | — | {{baseline_description}} | — |
| T1 | {{t1_name}} | {{t1_date}} | {{t1_capability}} | {{t1_work_packages}} |
| T2 | {{t2_name}} | {{t2_date}} | {{t2_capability}} | {{t2_work_packages}} |
| Target | Target Architecture | {{target_date}} | {{target_capability}} | — |

---

## Transition State Detail

<details>
<summary>📋 Guidance</summary>

For each transition state, describe the architecture at that point in time across all
applicable domains. Reference the domain architecture artifacts for detailed specifications.
Focus on what has changed from the previous state and what business value is delivered.

</details>

### Transition State 1 — {{t1_name}}

**Target Date:** {{t1_date}}
**Description:** {{t1_description}}

**Changes from Baseline:**

| Domain | Change Description | Impact |
|---|---|---|
| Business | {{b_change}} | {{b_impact}} |
| Data | {{d_change}} | {{d_impact}} |
| Application | {{a_change}} | {{a_impact}} |
| Technology | {{t_change}} | {{t_impact}} |

**Business Value Delivered:** {{t1_business_value}}

**Dependencies and Prerequisites:** {{t1_dependencies}}

**Risks:** {{t1_risks}}

---

### Transition State 2 — {{t2_name}}

**Target Date:** {{t2_date}}
**Description:** {{t2_description}}

**Changes from T1:**

| Domain | Change Description | Impact |
|---|---|---|
| Business | {{b_change}} | {{b_impact}} |
| Data | {{d_change}} | {{d_impact}} |
| Application | {{a_change}} | {{a_impact}} |
| Technology | {{t_change}} | {{t_impact}} |

**Business Value Delivered:** {{t2_business_value}}

**Dependencies and Prerequisites:** {{t2_dependencies}}

**Risks:** {{t2_risks}}

---

## Traceability to Roadmap Work Packages

<details>
<summary>📋 Guidance</summary>

Each transition state should be directly traceable to one or more work packages in the
Architecture Roadmap. This table confirms that every WP contributes to a specific transition.

</details>

| Work Package | WP-NNN | Contributes to Transition | Description |
|---|---|---|---|
| {{wp_name}} | WP-001 | T1 | {{wp_description}} |

---

## Appendix A3 — Decision Log

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |

---

*This document was created using the EA Assistant plugin.*
