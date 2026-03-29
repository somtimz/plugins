---
artifact: Migration Plan
engagement: {{engagement_name}}
phase: F
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Planning
  audience: Delivery
  layer: Transition
  sensitivity: Internal
  tags: [migration, waves, cutover, phase-f]
---

<details>
<summary>📋 Guidance</summary>

The Migration Plan is the primary Phase F artifact. It takes the work packages from the
Architecture Roadmap (Phase E) and defines how they will be sequenced and executed to
transition from the baseline to the target architecture. Phase F focuses on the practical
"how and when" of migration: sequencing, dependency management, wave planning, risk, and
rollback. It is an input to implementation planning and must be kept current as delivery proceeds.

</details>

# Migration Plan

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}

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

### Wave 2: {{wave_2_name}}

| Field | Value |
|---|---|
| **Target Date** | {{wave_2_date}} |
| **Work Packages** | {{wave_2_work_packages}} |
| **Transition Architecture** | {{plateau_2}} |
| **Entry Criteria** | {{wave_2_entry_criteria}} |
| **Exit Criteria** | {{wave_2_exit_criteria}} |
| **Key Dependencies** | {{wave_2_dependencies}} |

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

## Related Architecture Decisions

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
