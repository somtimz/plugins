---
artifact: Implementation Governance Plan
engagement: {{engagement_name}}
phase: G
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Governance
  layer: Governance
  sensitivity: Internal
  tags: [governance, review-schedule, checkpoints, phase-g]
---

<details>
<summary>📋 Guidance</summary>

The Implementation Governance Plan is a Phase G artifact. It translates the Architecture
Governance Framework (Preliminary Phase) into a concrete schedule of reviews, checkpoints,
and ownership assignments tied to this programme's work packages.

**What Phase G governs — and what it does not:**

Phase G is architecture's *contribution to* programme governance. Its central question is:

> **"Is the implementation conforming to the approved architecture?"**

Phase G governs:
- architecture compliance reviews at delivery gates (design, pre-build, pre-deployment)
- handling of deviations and dispensations from the approved architecture
- architecture change requests raised by delivery teams
- monitoring of solution realisation fidelity against the target architecture
- architecture contracts between the architecture function and delivery projects

Phase G does **not** replace programme governance. The programme's own governance
structures — steering committees, PMO, investment committees, delivery stage gates,
risk and issue management, benefits tracking — continue to operate independently.
This plan adds the architectural lens to those structures.

**The two governance questions at Phase G:**

| Governance layer | Central question | Owner |
|---|---|---|
| Architecture governance (this plan) | "Is the solution being built conformant with the approved architecture?" | Lead Architect / ARB |
| Programme governance | "Is the programme delivering the change effectively, on time, and within budget?" | Programme Sponsor / PMO |

Both questions must be answered at each delivery gate. This plan covers only the first.

**How this plan relates to the Architecture Governance Framework:**

The Governance Framework (Preliminary) defines the permanent governance structures, decision
rights, and compliance approach. This plan applies those structures to the specific work
packages and delivery timeline of this engagement. It does not redefine governance —
it schedules and operationalises it.

Create this artifact at the start of Phase G and keep it updated as the delivery schedule
evolves. Without this plan, Phase G governance becomes ad-hoc — architects are called into
reviews at the wrong time, non-conformances are discovered too late, and change requests
pile up with no agreed process.

</details>

# Implementation Governance Plan

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Governance Authority:** {{governance_authority}}
**Lead Architect:** {{lead_architect}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## 1. Executive Summary

<details>
<summary>📋 Guidance</summary>

Summarise in 3–5 sentences: what is being governed, who is responsible, and the key governance
milestones. This section is the primary reference for executives and programme managers who
need to understand governance obligations without reading the full plan.

</details>

{{executive_summary}}

---

## 2. Governance Scope & Objectives

<details>
<summary>📋 Guidance</summary>

Define precisely what this plan governs. List the work packages, projects, or delivery streams
in scope. State the specific governance objectives — what conformance outcomes are expected
by programme completion.

</details>

**Governed Scope:** {{governed_scope}}

**Relationship to Programme Governance:**
This plan governs architecture conformance only. Programme delivery governance (scope, schedule, budget, benefits, risk, and issue management) is owned by {{programme_governance_owner}} and operates through {{programme_governance_mechanism}}. Architecture governance is one input to programme stage gates — it does not replace them.

**Work Packages / Projects in Scope:**

| Work Package | ID | Delivery Stream | Governance Owner |
|---|---|---|---|
| {{work_package}} | WP-NNN | {{stream}} | {{owner}} |

**Governance Objectives:**

| # | Objective | Success Criterion |
|---|---|---|
| 1 | {{objective}} | {{success_criterion}} |
| 2 | {{objective}} | {{success_criterion}} |
| 3 | {{objective}} | {{success_criterion}} |

---

## 3. Governance Structure

<details>
<summary>📋 Guidance</summary>

Identify the people who are responsible for governance activities in this engagement. These
roles may be filled by the standing Architecture Review Board or by engagement-specific
governance contacts. Always name individuals — "the architecture team" is not a governance contact.

</details>

| Role | Responsibility | Named Individual | Contact |
|---|---|---|---|
| Governance Authority | Final escalation, waiver approval | {{governance_authority}} | {{contact}} |
| Lead Architect | Architecture conformance, review scheduling | {{lead_architect}} | {{contact}} |
| Domain Architect — Business | Business architecture conformance | {{domain_architect}} | {{contact}} |
| Domain Architect — Data | Data architecture conformance | {{domain_architect}} | {{contact}} |
| Domain Architect — Application | Application architecture conformance | {{domain_architect}} | {{contact}} |
| Domain Architect — Technology | Technology architecture conformance | {{domain_architect}} | {{contact}} |
| Project EA Liaison | Day-to-day conformance tracking per project | {{ea_liaison}} | {{contact}} |
| Delivery Lead | Conformance gating within delivery | {{delivery_lead}} | {{contact}} |

---

## 4. Review Schedule

<details>
<summary>📋 Guidance</summary>

Define the architecture review schedule tied to the delivery timeline. Reviews should be
anchored to delivery milestones (design freeze, build start, UAT entry, go-live), not to
calendar months, so the schedule remains valid even when the programme slips. At minimum,
define one design review and one pre-deployment review per work package.

</details>

| Review Gate | Work Package | Delivery Milestone | Planned Date | Assessor | Output |
|---|---|---|---|---|---|
| Design Review | {{work_package}} | Design freeze | {{YYYY-MM-DD}} | {{assessor}} | Compliance Assessment |
| Pre-Build Review | {{work_package}} | Build approval | {{YYYY-MM-DD}} | {{assessor}} | Compliance Assessment (updated) |
| Pre-Deployment Review | {{work_package}} | Before production | {{YYYY-MM-DD}} | {{assessor}} | Compliance Assessment (final) |
| Post-Implementation Review | {{work_package}} | 30 days post go-live | {{YYYY-MM-DD}} | {{assessor}} | Conformance Confirmation |
| {{review_gate}} | {{work_package}} | {{milestone}} | {{YYYY-MM-DD}} | {{assessor}} | {{output}} |

**Standing Architecture Governance Meeting:**
- **Frequency:** {{meeting_frequency}}
- **Chair:** {{meeting_chair}}
- **Standing agenda:** Progress updates, open change requests, waiver decisions, risk review

---

## 5. Compliance Checkpoint Process

<details>
<summary>📋 Guidance</summary>

Define what happens at each review gate. The process must be repeatable: every delivery team
should know exactly what to prepare, who to involve, and what output to expect. A well-defined
checkpoint process is the difference between governance that prevents problems and governance
that just records them.

</details>

### 5.1 Standard Compliance Checkpoint Steps

1. **Pre-review preparation (T-5 working days):** Delivery team submits artefacts to Lead Architect (solution design, relevant architecture diagrams, traceability to approved patterns).
2. **Architecture review (T-2 working days):** Lead Architect and relevant Domain Architects review submitted artefacts against the Architecture Contract and approved patterns.
3. **Compliance Assessment issued (T-0):** Compliance Assessment document completed and shared with Delivery Lead.
4. **Gate decision:** {{gate_decision_process}}
5. **Non-conformance handling:** {{non_conformance_handling}}

### 5.2 Compliance Outcomes

| Outcome | Meaning | Required Action |
|---|---|---|
| Fully Conformant | Artefacts conform to approved architecture | None — proceed to next milestone |
| Conditionally Conformant | Minor deviations within approved patterns | Delivery team to remediate conditions before next gate |
| Waiver Granted | Known deviation approved by governance authority | Waiver recorded in Compliance Assessment and Decision Register |
| Non-Conformant | Significant deviation from approved architecture | Design must be revised and re-reviewed before gate can pass |

---

## 6. Waiver & Exception Process

<details>
<summary>📋 Guidance</summary>

Define how delivery teams request a formal waiver when they cannot conform to an architecture
requirement. The process must be fast enough to avoid becoming a bottleneck — ideally a
5-working-day turnaround for standard waivers. Distinguish between waivers (approved deviations
for valid reasons) and non-conformances (unapproved deviations that must be remediated).

</details>

**When a Waiver is Required:** {{waiver_trigger}}

**Standard Waiver Process:**

| Step | Action | Owner | Timeframe |
|---|---|---|---|
| 1 | Delivery team submits Waiver Request (impact, justification, alternatives considered) | Project EA Liaison | Day 1 |
| 2 | Lead Architect reviews and provides recommendation | Lead Architect | Day 1–3 |
| 3 | Governance Authority issues decision | {{governance_authority}} | Day 3–5 |
| 4 | Decision recorded in Compliance Assessment and Decision Register | Lead Architect | Day 5 |

**Waiver Request Template Fields:**
- Architecture requirement being waived
- Reason the requirement cannot be met
- Alternatives considered and why rejected
- Impact of the waiver on other architecture elements
- Proposed compensating controls (if applicable)
- Expiry / review date for the waiver

**Emergency Waiver Process:** {{emergency_waiver_process}}
*(For critical path situations requiring a decision within 24 hours)*

---

## 7. Change Request Process

<details>
<summary>📋 Guidance</summary>

Define how changes to the agreed architecture are raised, assessed, and approved. Changes
are different from waivers: a change proposes to update the approved architecture itself,
while a waiver is a permitted deviation from it. Link to the Architecture Change Request
template for the actual request artefact.

</details>

**Types of Change in Scope:**
- {{change_type_1}}
- {{change_type_2}}
- {{change_type_3}}

**Change Request Process:**

| Step | Action | Owner | Timeframe |
|---|---|---|---|
| 1 | Raise Architecture Change Request (ACR) using the ACR template | Requestor | — |
| 2 | Lead Architect performs initial impact assessment | Lead Architect | {{timeframe}} |
| 3 | Governance Authority reviews and decides | {{governance_authority}} | {{timeframe}} |
| 4 | If approved: affected artifacts updated, Change Register updated | Lead Architect | {{timeframe}} |
| 5 | If rejected / deferred: rationale recorded in ACR | Lead Architect | {{timeframe}} |

**Change Volume Threshold:** If more than {{threshold}} ACRs are raised in any 4-week period, trigger a governance health review.

---

## 8. Escalation Paths

| Trigger | Escalation Path | Timeframe | Decision Maker |
|---|---|---|---|
| Delivery team disputes compliance assessment | Lead Architect → Governance Authority | {{timeframe}} | {{decision_maker}} |
| Waiver not decided within 5 working days | Governance Authority | Immediate | {{decision_maker}} |
| Non-conformance not remediated by next gate | Lead Architect → Programme Director | {{timeframe}} | {{decision_maker}} |
| Systemic non-conformance across multiple projects | Governance Authority → CTO / CIO | {{timeframe}} | {{decision_maker}} |
| {{trigger}} | {{escalation_path}} | {{timeframe}} | {{decision_maker}} |

---

## 9. Reporting & Metrics

<details>
<summary>📋 Guidance</summary>

Define how governance health is reported to stakeholders. Keep the governance report simple
— one page of metrics is more useful than a detailed narrative. Report at every standing
governance meeting.

</details>

**Reporting Frequency:** {{reporting_frequency}}

**Report Audience:** {{report_audience}}

**Governance Metrics Dashboard:**

| Metric | Target | Reporting Source |
|---|---|---|
| Compliance Assessments completed on schedule | ≥ 90% | Review schedule log |
| Waiver decisions within 5 working days | ≥ 95% | Waiver register |
| Open non-conformances older than 30 days | 0 | Compliance Assessment register |
| Change requests decided within SLA | ≥ 90% | Change Register |
| {{metric}} | {{target}} | {{source}} |

---

## 10. Governance Calendar

<details>
<summary>📋 Guidance</summary>

Provide a high-level calendar of key governance activities for the engagement. This gives
delivery teams visibility of when they need to prepare for architecture reviews, and ensures
governance activities are budgeted and resourced.

</details>

| Month / Period | Activity | Work Packages | Owner |
|---|---|---|---|
| {{period}} | {{activity}} | {{work_packages}} | {{owner}} |

---

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

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>
Record governance decisions made during the development or execution of this plan. Use `/ea-decisions` to generate a cross-artifact Decision Register.
</details>

| ID | Decision | State | Authority | Domain | Cost | Impact | Risk | Subject | Captured By | Owner | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>
Record all stakeholder concerns, objections, and tough questions raised about this artifact. Use `/ea-concerns` to generate a cross-artifact Concerns Register.
</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

*This document was created using the EA Assistant plugin. Use `/ea-decisions` to manage decisions, `/ea-concerns` to manage concerns, and `/ea-changes` to manage change requests.*
