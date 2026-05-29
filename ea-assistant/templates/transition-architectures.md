---
artifact: Transition Architectures
artifactId: transition-architectures
engagement: {{engagement_name}}
phase: E/F
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
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

**Purpose:** Transition Architectures define the sequence of stable, deliverable intermediate states between the Baseline and Target Architecture. Each state must be viable on its own — providing real business value and leaving the enterprise in a better position — not merely a partial target that cannot stand alone.

**What to include:** For each transition state: the specific capabilities delivered, the systems added or retired, the data flows changed, and the business outcomes enabled. Include the state-progression diagram (T0 → T1 → T2 → Target) and the traceability to work packages in the Architecture Roadmap.

**Quality indicators:**
- Each transition state is self-contained and delivers business value independently — a reader could describe what the enterprise looks like at T1 without reference to T2 or Target
- The number of transition states reflects the complexity and risk profile of the engagement — too few (one big-bang) signals risk; too many signals insufficient planning
- Each transition state maps to one or more WP-NNN entries in the Architecture Roadmap

**Common mistakes:**
- Defining transition states that are technically convenient but deliver no business value until the final state is reached — this is phased delivery, not a Transition Architecture
- Omitting the business value delivered at each state — delivery teams use this to justify incremental investment
- Producing this artifact in Phase E without revisiting it in Phase F when the Migration Plan is finalised

**TOGAF reference:** TOGAF 10 §31 (Phase E) and §32 (Phase F) — Transition Architectures are a Phase E deliverable, refined in Phase F. Each state should correspond to a migration increment in the Migration Plan.

</details>

# Transition Architectures

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

**Purpose:** Decision-maker summary of the migration path — how many transition states are planned, what is delivered at each, and why this sequencing was chosen. This is the section sponsors read to validate that the transition approach balances speed of value delivery with risk management.

**What to include:** The total number of transition states, one sentence per state describing the headline capability delivered, and the state-progression diagram (T0 → T1 → T2 → Target). Note the timeline from baseline to target. If the sequencing was constrained by a dependency or risk decision, note it here with an ADR reference.

**Quality indicators:**
- The diagram is present and current — state labels match the section headings below
- Each state delivers a named business capability, not just a technical milestone
- The executive summary is refreshed after the detail sections are populated — run `/ea-summary refresh`

**Common mistakes:**
- Writing the executive summary before the detail sections are complete — this section should be the last written
- State-progression diagram that conflicts with the Transition State Summary table below
- Describing the migration approach in technical terms only, without the business outcome each state delivers

**TOGAF reference:** TOGAF 10 §31 — the executive summary of Transition Architectures aligns with the Phase E outputs that present the migration path to stakeholders for endorsement.

</details>

{{executive_summary}}

---

## Overview

<details>
<summary>📋 Guidance</summary>

**Purpose:** Explains the migration strategy — the logic behind the chosen number of states and their sequencing — so that delivery teams and governance boards understand the architectural thinking, not just the plan.

**What to include:** The rationale for the number of transition states chosen (e.g. "three states were chosen to deliver customer-facing value in T1 while deferring the technically complex MDM consolidation to T2"). Key business drivers (DRV-NNN) that constrain the sequencing. Dependencies that force a specific ordering. Risk appetite decisions that led to phasing a particular change incrementally rather than in one step.

**Quality indicators:**
- The number of states is justified by concrete reasoning — not "we chose three because it felt right" but "T1 was driven by the regulatory deadline for Q3; T2 aligns with the next budget cycle"
- Dependency constraints are named explicitly — "T2 cannot start until the MDM platform from T1 is operational"
- The overview aligns with the Transition State Summary table — no states appear in one but not the other

**Common mistakes:**
- Omitting the rationale for the sequencing — stakeholders will ask why T1 delivers X before Y; document the answer here
- Transition states that are defined by project sprints or resource availability rather than architectural coherence
- Overview that does not reference the Architecture Roadmap work packages driving each state

**TOGAF reference:** TOGAF 10 §31 — the transition architecture overview is the architect's explanation of the migration sequencing strategy, not a project plan. The project plan lives in the Migration Plan artifact.

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

**Purpose:** The detailed specification of each intermediate architecture state — what the enterprise looks like at that point in time, what changed since the previous state, and what business value is delivered. This section is used by delivery teams to understand what they are building toward, and by governance to confirm each increment is coherent and valuable.

**What to include:** For each transition state: the target date, a prose description of the architecture at that state, a domain-by-domain change table, the business value delivered (named outcomes, not generic benefits), dependencies that must be met before this state can be reached, and the principal risks. Add or remove state blocks (T1, T2, T3...) to match the actual number of transition states planned.

**Quality indicators:**
- The "Changes from previous state" table covers all active domains — a blank cell in the table is a red flag, not a valid entry
- Business value is named and measurable — "enables online order tracking for all customers" not "improves customer experience"
- Dependencies are specific and owned — "requires MDM platform WP-003 to be completed and accepted-tested, owned by Data Architecture team"
- Risks are specific to this transition state, not generic project risks — "risk that T1 go-live coincides with peak trading period May–June; mitigation: defer to July"

**Common mistakes:**
- Describing changes in technical implementation terms only — each change must connect to a business outcome
- Transition states where the "Changes from previous state" table is identical to the target architecture — this means there is only one state, not a true transition architecture
- Missing the dependency on preceding states — T2 cannot be planned without explicitly noting what T1 must have delivered first

**TOGAF reference:** TOGAF 10 §31 — each transition state detail block corresponds to a discrete migration increment, traceable to one or more work packages in the Architecture Roadmap and one or more migration increments in the Migration Plan.

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

**Purpose:** Confirms bidirectional traceability between Transition Architectures and the Architecture Roadmap. Every work package must contribute to a specific transition state; every transition state must be supported by at least one work package. Gaps in either direction are governance findings.

**What to include:** One row per work package (WP-NNN), noting which transition state it contributes to and a brief description of what it delivers. If a work package spans multiple transition states, add a row for each. Add a reverse-traceability check: confirm that every transition state in the Transition State Summary above has at least one WP entry in this table.

**Quality indicators:**
- Every WP-NNN referenced here also appears in the Architecture Roadmap — no phantom work packages
- Every transition state (T1, T2, etc.) has at least one WP in this table — an unanchored transition state has no delivery mechanism
- Work package descriptions are specific enough to distinguish between WPs — not all described as "implements the target architecture"

**Common mistakes:**
- Populating this table after the roadmap is finalised without checking backward — mismatches between roadmap WPs and transition states discovered late are expensive to resolve
- Leaving the placeholder row with WP-001 when multiple work packages exist — this table should reflect the actual roadmap
- Missing transition state assignments for infrastructure or platform WPs (often omitted because they support multiple states rather than one)

**TOGAF reference:** TOGAF 10 §31 and §32 — traceability between Transition Architectures and work packages is the mechanism that ensures the Migration Plan is grounded in architectural intent. Run `/ea-roadmap trace` to verify completeness.

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
