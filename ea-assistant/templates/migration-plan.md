---
artifactId: migration-plan
artifact: Migration Plan
artifactId: migration-plan
engagement: {{engagement_name}}
phase: F
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Planning
  audience: Delivery
  layer: Transition
  sensitivity: Internal
  tags: [migration, waves, cutover, phase-f]
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
| Linked to Architecture Roadmap | ⚠️ Pending | |
| Benefits realisation tracked | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Migration Plan converts the Architecture Roadmap's work packages into a sequenced, funded, risk-assessed execution plan. It answers how and when the transition from baseline to target architecture will occur — including wave structure, dependencies, rollback provisions, and the business benefits expected at each milestone.

**What to include:** Wave structure (which WPs execute in each wave), sequencing rationale, inter-wave dependencies, resource and funding overview, migration risks with mitigations, rollback strategy per wave, and a benefits realisation tracker. The Migration Plan takes the Architecture Roadmap as its primary input and is the primary input to Programme and Project Management.

**Quality indicators:**
- Each wave delivers identifiable business value independently — a wave that only delivers infrastructure with no business benefit needs justification
- Rollback strategy is defined per wave before the wave begins, not after a failure — architects who define rollback after go-live are not doing architecture
- Benefits are tracked against the Architecture Vision goals (G-NNN) — if a wave completes but no goal advances, ask why

**Common mistakes:**
- Migration Plan that is a project plan — the Migration Plan is an architecture artifact describing the migration *architecture* (sequencing, dependencies, transition states); the project schedule lives in the PMO tooling
- No rollback strategy — "we won't need to roll back" is not a plan
- Wave sequencing driven by team availability rather than business value delivery — this is the most common cause of stakeholder disengagement with the roadmap

**TOGAF reference:** TOGAF 10 Part III, Phase F (§30) — Migration Planning. The primary Phase F deliverable; produced alongside the finalised Architecture Roadmap and Transition Architectures.

</details>

<details>
<summary>💡 Practitioner Tip — Migration</summary>

- **Optimize for value delivery** — sequence migration so that business benefits arrive early and compound over time. (Deep tactic #31)
- Quantify **risk exposure** per migration wave — know what breaks if a wave fails. (Deep tactic #32)
- Align to **funding cycles** — architecture that cannot fit into annual budget processes rarely gets executed. (Deep tactic #33)
- Define **exit criteria for legacy** — without clear retirement targets, old systems live forever. (Deep tactic #34)
- Maintain **flexibility** — build rollback paths and off-ramps into the plan; no migration survives first contact with reality unchanged. (Deep tactic #35)
- Treat transition architectures as **strategic instruments**, not temporary compromises. (Tip #45)
- The migration plan is a **contract between architecture and delivery** — it sets expectations that both sides must meet. (Tip #46)

</details>

# Migration Plan

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of migration waves, key dependencies, and risk areas to manage.
Diagram: Migration wave diagram or Gantt chart
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Migration Overview

<details>
<summary>📋 Guidance</summary>

Summarise the migration at a high level: what is being migrated, from what baseline, to what
target, and over what timeframe. State the overall migration strategy (e.g. big-bang,
phased, parallel run, strangler fig). Reference the Architecture Roadmap for the work packages
being executed.

</details>

{{migration_overview}}

**Migration Strategy:** {{migration_strategy}}
**Overall Timeline:** {{start_date}} to {{end_date}}
**Reference Roadmap:** `architecture-roadmap.md`

---

## 2. Migration Approach

<details>
<summary>📋 Guidance</summary>

Describe the approach in enough detail that a delivery team can plan from it. Address:
- How data will be migrated (ETL, replication, manual, dual-write)
- How cut-over will be managed (hard cut-over, phased, feature flags)
- How users will be transitioned (training, change management)
- How legacy systems will be decommissioned
- Any parallel running period and how reconciliation will be conducted

</details>

### Data Migration Approach
{{data_migration_approach}}

### Cut-over Approach
{{cutover_approach}}

### User Transition
{{user_transition_approach}}

### Legacy Decommissioning
{{decommissioning_approach}}

---

## 3. Wave Plan

<details>
<summary>📋 Guidance</summary>

Break the migration into discrete waves (tranches). Each wave should deliver a stable,
usable state (a transition architecture plateau). Sequence waves to manage dependency,
risk, and organisational change capacity. Each wave should have clear entry criteria
(what must be true before the wave begins) and exit criteria (what must be true before
the next wave starts).

</details>

### Wave 1: {{wave_1_name}}

| Field | Value |
|---|---|
| **Target Date** | {{wave_1_date}} |
| **Work Packages** | {{wave_1_work_packages}} |
| **Transition Architecture** | {{plateau_1}} |
| **Entry Criteria** | {{wave_1_entry_criteria}} |
| **Exit Criteria** | {{wave_1_exit_criteria}} |
| **Key Dependencies** | {{wave_1_dependencies}} |

#### Wave 1 Resource Summary

| Resource | Required | Available | Gap |
|---|---|---|---|
| {{role}} | {{fte_required}} | {{fte_available}} | None / ⚠️ {{gap_description}} |

### Wave 2: {{wave_2_name}}

| Field | Value |
|---|---|
| **Target Date** | {{wave_2_date}} |
| **Work Packages** | {{wave_2_work_packages}} |
| **Transition Architecture** | {{plateau_2}} |
| **Entry Criteria** | {{wave_2_entry_criteria}} |
| **Exit Criteria** | {{wave_2_exit_criteria}} |
| **Key Dependencies** | {{wave_2_dependencies}} |

#### Wave 2 Resource Summary

| Resource | Required | Available | Gap |
|---|---|---|---|
| {{role}} | {{fte_required}} | {{fte_available}} | None / ⚠️ {{gap_description}} |

*Reference diagram:* `../diagrams/{{wave_plan_diagram}}`

---

## 4. Risk Register

<details>
<summary>📋 Guidance</summary>

List the risks specific to migration execution. Migration risks differ from architecture
risks — they focus on execution: data loss, extended downtime, user disruption, integration
failure during cut-over, and regulatory issues during transition. Include likelihood,
impact, mitigation, and an owner for each risk.

</details>

| Risk ID | Description | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| MIG-R001 | {{description}} | High / Med / Low | High / Med / Low | {{mitigation}} | {{owner}} |
| MIG-R002 | {{description}} | High / Med / Low | High / Med / Low | {{mitigation}} | {{owner}} |

---

## 5. Rollback Plan

<details>
<summary>📋 Guidance</summary>

For each wave, define the rollback trigger, rollback procedure, and rollback decision authority.
A rollback plan should be tested before it is needed. Specify: what monitoring will detect
a need to roll back, who can authorise rollback, and how long the rollback window is open
after each cut-over.

</details>

| Wave | Rollback Trigger | Rollback Procedure | Decision Authority | Rollback Window |
|---|---|---|---|---|
| Wave 1 | {{trigger_1}} | {{procedure_1}} | {{authority_1}} | {{window_1}} |
| Wave 2 | {{trigger_2}} | {{procedure_2}} | {{authority_2}} | {{window_2}} |

### Rollback Constraints
{{rollback_constraints}}

---

## 6. Success Criteria

<details>
<summary>📋 Guidance</summary>

Define the measurable criteria that will confirm the migration has succeeded. Criteria should
be verifiable: system health checks, data reconciliation counts, performance benchmarks,
user acceptance sign-off. Include the testing approach used to validate each criterion.

</details>

| Criterion | Measure | Target | Validation Method | Owner |
|---|---|---|---|---|
| Data integrity | {{measure}} | {{target}} | {{validation}} | {{owner}} |
| System availability | {{measure}} | {{target}} | {{validation}} | {{owner}} |
| {{criterion}} | {{measure}} | {{target}} | {{validation}} | {{owner}} |

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.
Each row captures the decision item, agreed value, governance state, who captured it,
who owns or must verify it, and classification fields used by /ea-decisions.
Use /ea-decisions to aggregate this table across all artifacts into a Decision Register.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

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


## Appendix A5 — Related Architecture Decisions

<details>
<summary>📋 Guidance</summary>

List ADRs that informed, were informed by, or are otherwise relevant to this artifact.
Reference the ADR-NNN ID so readers can navigate to the full decision record.
Use `/ea-adrs` to manage the ADR Register and surface ADR summaries.

When a significant decision is made during an interview for this artifact, the
`ea-interviewer` will suggest creating an ADR if the decision meets the threshold
criteria (technology/vendor selection, high cost/risk, hard to reverse, etc.).

</details>

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
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
