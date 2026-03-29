---
artifact: Engagement Charter
engagement: {{engagement_name}}
phase: Prelim
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Strategy
  audience: Executive
  layer: Motivation
  sensitivity: Confidential
  tags: [charter, engagement, programme, motivation, preliminary]
---

<details>
<summary>📋 Guidance</summary>

The Engagement Charter is the foundational Preliminary Phase artifact. It establishes the
authoritative record of *why* the engagement exists, *what* it covers, *who* it affects,
*how* it is structured, and *what* it is expected to deliver.

The Charter differs from the Architecture Vision (Phase A):
- The **Engagement Charter** covers the engagement or programme as a whole — it is the
  business case and mandate document. It exists before any architecture work begins.
- The **Architecture Vision** (Phase A) defines the target architecture and the strategy
  for achieving it. It builds on the Charter's foundation.

In large programmes, the Charter covers the entire programme lifecycle; individual
Architecture Visions may then be created for specific sub-programmes or delivery phases.

Once approved, the Charter is the baseline reference for scope management, benefits
realisation, and governance throughout the engagement. Significant changes to scope,
objectives, or programme structure require a formal Charter revision.

</details>

# Engagement Charter

**Engagement:** {{engagement_name}}
**Programme / Project Reference:** {{programme_reference}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Lead Architect:** {{lead_architect}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** Draft / Under Review / Approved

---

## 1. Organisation Background

<details>
<summary>📋 Guidance</summary>

Provide context about the organisation that this engagement serves. Describe the industry,
operating model, scale, and relevant history. Focus on what a new stakeholder needs to
understand the organisation's situation — not a generic company profile. Include details
that explain *why this engagement is happening now* (e.g. recent growth, regulatory change,
merger, strategy shift).

</details>

### 1.1 Organisation Profile

**Industry / Sector:** {{industry_sector}}

**Operating Model:** {{operating_model}}
*(e.g. centralised / federated / holding company / franchise / government department)*

**Scale:** {{organisation_scale}}
*(e.g. headcount, revenue band, geographic footprint, number of business units)*

**Technology Landscape Summary:** {{technology_landscape}}
*(e.g. predominantly on-premises, mixed cloud, heavily outsourced — highlight characteristics relevant to this engagement)*

### 1.2 Relevant History & Context

{{organisation_history_context}}
*(Describe recent events, strategic shifts, or prior programmes that explain why this engagement is needed now. Reference prior architectures, failed attempts, or known constraints.)*

### 1.3 Current State Summary

| Dimension | Current State | Relevance to Engagement |
|---|---|---|
| Business Capability | {{current_state}} | {{relevance}} |
| Technology Platform | {{current_state}} | {{relevance}} |
| Data & Information | {{current_state}} | {{relevance}} |
| People & Process | {{current_state}} | {{relevance}} |
| Governance & Compliance | {{current_state}} | {{relevance}} |

---

## 2. Engagement Purpose & Mandate

<details>
<summary>📋 Guidance</summary>

State clearly why this engagement exists and who has authorised it. The mandate is the
formal justification for spending time, money, and organisational attention on this work.
A weak or vague mandate is a governance risk — it allows scope to drift and makes it
difficult to close the engagement when done.

Be specific: what problem is being solved, what opportunity is being captured, or what
obligation is being met?

</details>

### 2.1 Purpose Statement

{{engagement_purpose}}
*(One clear paragraph: what this engagement exists to achieve and why it is needed now.)*

### 2.2 Mandate

**Authorised By:** {{authorised_by}}
**Authorisation Reference:** {{authorisation_reference}}
*(e.g. Board resolution, Executive decision, Programme Board approval, Regulatory directive)*
**Date Authorised:** {{YYYY-MM-DD}}

**Engagement Type:** {{engagement_type}}
*(e.g. Greenfield implementation, Legacy modernisation, Capability assessment, Cloud migration, Regulatory compliance, Merger integration, Post-acquisition rationalisation)*

### 2.3 Strategic Alignment

| Strategic Initiative / Plan | Alignment |
|---|---|
| {{strategic_initiative}} | {{how_this_engagement_contributes}} |
| {{strategic_initiative}} | {{how_this_engagement_contributes}} |

---

## 3. Scope & Boundaries

<details>
<summary>📋 Guidance</summary>

Define precisely what is in scope and what is explicitly out of scope. Explicit out-of-scope
statements are as important as in-scope definitions — they prevent scope creep and manage
stakeholder expectations. If something is deferred (in scope for a future phase), say so.

Use the architecture domain rows to communicate clearly with technical stakeholders.
Use the business domain rows to communicate with business stakeholders.

</details>

### 3.1 In Scope

| # | Scope Item | Domain | Phase(s) |
|---|---|---|---|
| 1 | {{scope_item}} | Business / Data / Application / Technology | {{phases}} |
| 2 | {{scope_item}} | Business / Data / Application / Technology | {{phases}} |
| 3 | {{scope_item}} | Business / Data / Application / Technology | {{phases}} |

### 3.2 Out of Scope

| # | Excluded Item | Reason | Future Consideration? |
|---|---|---|---|
| 1 | {{excluded_item}} | {{reason}} | Yes — Phase {N} / No / Under review |
| 2 | {{excluded_item}} | {{reason}} | Yes — Phase {N} / No / Under review |

### 3.3 Scope Boundaries

**Geographic scope:** {{geographic_scope}}

**Organisational units in scope:** {{organisational_units}}

**Systems and applications explicitly in scope:** {{systems_in_scope}}

**Systems and applications explicitly out of scope:** {{systems_out_of_scope}}

**Data domains in scope:** {{data_domains}}

### 3.4 Assumptions

| # | Assumption | Owner | Impact if Wrong |
|---|---|---|---|
| 1 | {{assumption}} | {{owner}} | {{impact}} |
| 2 | {{assumption}} | {{owner}} | {{impact}} |

### 3.5 Constraints

| # | Constraint | Type | Impact |
|---|---|---|---|
| 1 | {{constraint}} | Regulatory / Financial / Technical / Organisational / Time | {{impact}} |
| 2 | {{constraint}} | Regulatory / Financial / Technical / Organisational / Time | {{impact}} |

---

## 4. Relationship to Other Engagements & Programmes

<details>
<summary>📋 Guidance</summary>

Most architecture engagements do not exist in isolation. Document how this engagement
relates to other programmes, projects, and architecture initiatives. Dependencies are
a major source of delivery risk — undefined dependencies become blocked deliverables.

For each related engagement, be clear about the direction of dependency: does this
engagement depend on the other, does the other depend on this, or is it a peer
relationship with shared assumptions?

</details>

| Related Programme / Engagement | Relationship Type | Dependency Direction | Key Interface | Status |
|---|---|---|---|---|
| {{programme_name}} | Predecessor / Successor / Peer / Dependent / Feeds-into | This depends on it / It depends on this / Mutual | {{interface_description}} | {{status}} |
| {{programme_name}} | Predecessor / Successor / Peer / Dependent / Feeds-into | This depends on it / It depends on this / Mutual | {{interface_description}} | {{status}} |

**Architecture repository / standards this engagement inherits:** {{inherited_standards}}

**Architecture outputs this engagement will produce for others:** {{outputs_for_others}}

---

## 5. Organisations Affected

<details>
<summary>📋 Guidance</summary>

List all organisations — internal divisions, subsidiaries, external partners, customers,
regulators — that will be affected by this engagement. "Affected" includes organisations
that will change how they operate, organisations that consume outputs from affected systems,
and organisations with a governance or compliance interest.

This section informs the Stakeholder Map (Phase A) and the Communications Plan.

</details>

### 5.1 Internal Organisations

| Division / Business Unit | Nature of Impact | Level of Involvement | Primary Contact |
|---|---|---|---|
| {{division}} | {{nature_of_impact}} | High / Medium / Low | {{contact}} |
| {{division}} | {{nature_of_impact}} | High / Medium / Low | {{contact}} |

### 5.2 External Organisations

| Organisation | Type | Nature of Impact | Engagement Required |
|---|---|---|---|
| {{organisation}} | Customer / Partner / Supplier / Regulator / Joint Venture | {{nature}} | Yes — {how} / No |
| {{organisation}} | Customer / Partner / Supplier / Regulator / Joint Venture | {{nature}} | Yes — {how} / No |

### 5.3 Regulatory & Compliance Bodies

| Body / Framework | Obligation | Relevant Scope | Key Contact |
|---|---|---|---|
| {{body}} | {{obligation}} | {{scope}} | {{contact}} |

---

## 6. Motivation Framework

<details>
<summary>📋 Guidance</summary>

The motivation framework captures the full chain from what is causing pressure to act
(Drivers) through to what the organisation wants to achieve (Goals), how it will measure
progress (Objectives), how it will act (Strategies), and what is standing in the way
(Issues and Problems).

Populate this section using the DRV/G/OBJ/STR/ISS/PRB ID scheme. IDs assigned here
are the canonical IDs for this engagement — use them consistently in all subsequent
artifacts and in engagement.json.

Motivation chain: DRV → G → OBJ ← STR; ISS threatens G; PRB blocks OBJ.

This section is the source of truth for engagement.json → direction. Run /ea-interview
to populate engagement.json simultaneously.

</details>

### 6.1 Vision & Mission

**Vision:** {{vision_statement}}
*(The future state the organisation aspires to — long-term, aspirational, and qualitative)*

**Mission:** {{mission_statement}}
*(The enduring purpose of the organisation that this engagement serves)*

### 6.2 Business Drivers

*Forces — external or internal — making this engagement necessary now.*

| ID | Driver | Type | Priority | Notes |
|---|---|---|---|---|
| DRV-001 | {{driver_description}} | External / Internal / Regulatory / Strategic | High / Medium / Low | {{notes}} |
| DRV-002 | {{driver_description}} | External / Internal / Regulatory / Strategic | High / Medium / Low | {{notes}} |
| DRV-003 | {{driver_description}} | External / Internal / Regulatory / Strategic | High / Medium / Low | {{notes}} |

### 6.3 Goals

*Broad, qualitative outcomes the engagement must achieve. Each goal responds to one or more drivers.*

| ID | Goal Statement | Linked Drivers | Owner | Priority |
|---|---|---|---|---|
| G-001 | {{goal_statement}} | DRV-NNN | {{owner}} | High / Medium / Low |
| G-002 | {{goal_statement}} | DRV-NNN | {{owner}} | High / Medium / Low |
| G-003 | {{goal_statement}} | DRV-NNN | {{owner}} | High / Medium / Low |

### 6.4 Objectives

*Specific, measurable, time-bound results that operationalise each goal. Each objective links to a goal and should have at least one metric.*

| ID | Objective | Measure | Target | Deadline | Linked Goal |
|---|---|---|---|---|---|
| OBJ-001 | {{objective_statement}} | {{measure}} | {{target_value}} | {{YYYY-MM-DD}} | G-NNN |
| OBJ-002 | {{objective_statement}} | {{measure}} | {{target_value}} | {{YYYY-MM-DD}} | G-NNN |
| OBJ-003 | {{objective_statement}} | {{measure}} | {{target_value}} | {{YYYY-MM-DD}} | G-NNN |

### 6.5 Strategies

*How the organisation intends to achieve its goals. Each strategy supports one or more goals and produces work packages.*

| ID | Strategy | Supports Goals | Approach Summary |
|---|---|---|---|
| STR-001 | {{strategy_statement}} | G-NNN | {{approach}} |
| STR-002 | {{strategy_statement}} | G-NNN | {{approach}} |

### 6.6 Issues & Problems

*Issues threaten goals (strategic risks); Problems block objectives (operational blockers).*

| ID | Type | Statement | Threatens / Blocks | Owner | Status |
|---|---|---|---|---|---|
| ISS-001 | Issue | {{issue_statement}} | G-NNN | {{owner}} | Open / Being Addressed / Resolved |
| PRB-001 | Problem | {{problem_statement}} | OBJ-NNN | {{owner}} | Open / Being Addressed / Resolved |

---

## 7. Programme Structure

<details>
<summary>📋 Guidance</summary>

Define the delivery phases for this engagement — the major stages of work with their
objectives, deliverables, and sequencing. Keep this section focused on *what will be
delivered and when*. Governance arrangements (who decides what, ARB structure, decision
rights, compliance process) are defined in the **Architecture Governance Framework**;
do not duplicate them here.

Phase types:
- **Planning** — scope definition, resource planning, architecture work
- **Preparation** — environment setup, team onboarding, data migration readiness, tooling
- **Procurement** — vendor selection, contract negotiation, partner engagement
- **Pilot** — limited or time-boxed deployment to validate approach before full rollout
- **Implementation** — actual delivery; multiple waves are common for large programmes
- **Post-Implementation** — stabilisation, hypercare, benefits realisation, lessons learned
- **Other** — any phase type not covered above (name it explicitly)

Each phase should link to the goals and objectives it primarily delivers against.

</details>

| # | Phase Name | Type | Description | Key Deliverables | Linked Goals | Prerequisites | Est. Duration | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | {{phase_name}} | Planning | {{description}} | {{deliverables}} | G-NNN | None | {{duration}} | Planned / In Progress / Complete / On Hold / Not Required |
| 2 | {{phase_name}} | Preparation | {{description}} | {{deliverables}} | G-NNN | Phase 1 | {{duration}} | Planned |
| 3 | {{phase_name}} | Procurement | {{description}} | {{deliverables}} | G-NNN | Phase 1 | {{duration}} | Planned |
| 4 | {{phase_name}} | Pilot | {{description}} | {{deliverables}} | G-NNN | Phase 2, 3 | {{duration}} | Planned |
| 5 | {{phase_name}} | Implementation | {{description}} | {{deliverables}} | G-NNN | Phase 4 | {{duration}} | Planned |
| 6 | {{phase_name}} | Post-Implementation | {{description}} | {{deliverables}} | G-NNN | Phase 5 | {{duration}} | Planned |

**Programme Timeline Summary:**
- **Estimated Start Date:** {{YYYY-MM-DD}}
- **Estimated End Date:** {{YYYY-MM-DD}}
- **Total Duration:** {{total_duration}}
- **Key Milestones:** {{key_milestones}}

**Phasing Rationale:**
{{phasing_rationale}}
*(Explain why the programme is structured this way — e.g. regulatory deadline drives Phase 1 timeline; Pilot reduces risk before full rollout; Implementation split across two waves to manage change capacity)*

**Governance Reference:**
Architecture governance for this engagement is defined in the Architecture Governance Framework (Preliminary phase artifact). That document covers: governance bodies and their Terms of Reference, decision rights and escalation thresholds, ADM compliance process, waiver procedures, and the Architecture Review Board structure.

> See: `artifacts/governance-framework.md`

---

## 8. Expected Outcomes

<details>
<summary>📋 Guidance</summary>

Describe what the engagement will have produced when it is complete. Distinguish between:
- **Outputs** — tangible deliverables (systems, platforms, processes, documents)
- **Outcomes** — changes in how the organisation operates or performs
- **Impacts** — broader strategic or organisational effects

A successful engagement delivers all three. Outputs without outcomes are sunk costs.

</details>

### 8.1 Outputs — What Will Be Delivered

| # | Output | Produced By Phase | Owner |
|---|---|---|---|
| 1 | {{output}} | Phase {N} | {{owner}} |
| 2 | {{output}} | Phase {N} | {{owner}} |

### 8.2 Outcomes — How the Organisation Will Operate Differently

| # | Outcome | Linked Objectives | Measurable? |
|---|---|---|---|
| 1 | {{outcome}} | OBJ-NNN | {{how_measured}} |
| 2 | {{outcome}} | OBJ-NNN | {{how_measured}} |

### 8.3 Impacts — Strategic & Organisational Effects

{{strategic_impacts}}

---

## 9. Benefits

<details>
<summary>📋 Guidance</summary>

Capture the expected benefits at the level of detail available at this stage. Where
financial quantification is not yet possible, describe the benefit qualitatively and
note when quantification will be available. Benefits without owners are rarely realised —
assign an owner for every benefit.

Distinguish between financial benefits (cost reduction, revenue growth, cost avoidance)
and non-financial benefits (risk reduction, compliance, capability, resilience, reputation).
Both categories matter for the investment decision.

</details>

### 9.1 Financial Benefits

| # | Benefit | Type | Estimated Value | Realisation Phase | Owner | Confidence |
|---|---|---|---|---|---|---|
| 1 | {{benefit}} | Cost reduction / Cost avoidance / Revenue growth / Efficiency gain | {{value_or_TBD}} | Phase {N} | {{owner}} | High / Medium / Low |
| 2 | {{benefit}} | Cost reduction / Cost avoidance / Revenue growth / Efficiency gain | {{value_or_TBD}} | Phase {N} | {{owner}} | High / Medium / Low |

**Total estimated financial benefit:** {{total_benefit_or_TBD}}

### 9.2 Non-Financial Benefits

| # | Benefit | Category | Linked Objective | Owner |
|---|---|---|---|---|
| 1 | {{benefit}} | Risk reduction / Compliance / Capability / Resilience / Reputation / Customer experience | OBJ-NNN | {{owner}} |
| 2 | {{benefit}} | Risk reduction / Compliance / Capability / Resilience / Reputation / Customer experience | OBJ-NNN | {{owner}} |

### 9.3 Benefits Realisation

**Earliest benefit realisation expected:** {{earliest_benefit_date}}

**How benefits will be tracked:** {{benefits_tracking_approach}}

---

## 10. Costs

<details>
<summary>📋 Guidance</summary>

Document the cost envelope at the level of detail available at Charter stage. Full cost
breakdown will be developed during the Planning/Preparation phase. At this stage, capture
the categories and order-of-magnitude estimates. Unbudgeted costs discovered after
Charter approval are a governance risk.

Include both one-time costs (implementation) and ongoing costs (run costs, licences,
support). Many organisations underestimate run costs — call them out explicitly.

</details>

### 10.1 Cost Summary

| Category | One-Time Cost | Annual Ongoing Cost | Phase | Confidence |
|---|---|---|---|---|
| Internal staffing / EA resources | {{cost_or_TBD}} | {{cost_or_TBD}} | All phases | High / Medium / Low |
| External consulting / SI partner | {{cost_or_TBD}} | — | Phases {N} | High / Medium / Low |
| Software licences / SaaS | {{cost_or_TBD}} | {{cost_or_TBD}} | Phase {N}+ | High / Medium / Low |
| Infrastructure / cloud | {{cost_or_TBD}} | {{cost_or_TBD}} | Phase {N}+ | High / Medium / Low |
| Data migration | {{cost_or_TBD}} | — | Phase {N} | High / Medium / Low |
| Training & change management | {{cost_or_TBD}} | {{cost_or_TBD}} | Phase {N} | High / Medium / Low |
| Procurement / vendor management | {{cost_or_TBD}} | — | Phase {N} | High / Medium / Low |
| Contingency (recommended 15–20%) | {{cost_or_TBD}} | — | All phases | — |
| **Total** | **{{total_one_time}}** | **{{total_ongoing}}** | — | — |

### 10.2 Funding Approach

**Budget approved:** {{budget_approved_amount}}
**Budget reference:** {{budget_reference}}
**Funding source:** {{funding_source}}
**Budget owner:** {{budget_owner}}

**Unfunded cost items (if any):** {{unfunded_items}}

---

## 11. Initial Risk Profile

<details>
<summary>📋 Guidance</summary>

Capture the high-level risks known at Charter stage. This is not the full risk register
— that is produced by `/ea-risks`. The purpose here is to surface the risks that are
significant enough to influence whether or how to proceed with the engagement.

For each risk, consider: delivery risks (will we be able to build this?), adoption risks
(will people use it?), dependency risks (what if the other programme is delayed?), and
strategic risks (could this deliver harm instead of benefit?).

This section feeds into the Risk Register generated by `/ea-risks`.

</details>

| ID | Risk | Likelihood | Impact | Rating | Mitigation | Owner |
|---|---|---|---|---|---|---|
| RIS-001 | {{risk_description}} | High / Med / Low | High / Med / Low | Critical / High / Med / Low | {{mitigation}} | {{owner}} |
| RIS-002 | {{risk_description}} | High / Med / Low | High / Med / Low | Critical / High / Med / Low | {{mitigation}} | {{owner}} |
| RIS-003 | {{risk_description}} | High / Med / Low | High / Med / Low | Critical / High / Med / Low | {{mitigation}} | {{owner}} |

**Overall risk level:** High / Medium / Low

**Risk acceptance statement:**
{{risk_acceptance_statement}}
*(State what level of residual risk the sponsor is willing to accept and under what conditions the engagement would be paused or stopped)*

---

## 12. Key Stakeholders

<details>
<summary>📋 Guidance</summary>

List the key stakeholders at Charter stage. This is the seed of the Stakeholder Map
(Phase A). Include sponsors, decision-makers, and anyone whose active engagement is
required for the programme to succeed — not everyone who has a passive interest.

</details>

| Name | Role / Title | Organisation | Interest | Influence | Engagement Approach |
|---|---|---|---|---|---|
| {{name}} | {{role}} | {{organisation}} | High / Medium / Low | High / Medium / Low | {{approach}} |
| {{name}} | {{role}} | {{organisation}} | High / Medium / Low | High / Medium / Low | {{approach}} |

**Programme Sponsor (accountable):** {{sponsor}}
**Programme Director (responsible):** {{programme_director}}
**Lead Architect:** {{lead_architect}}
**Business Owner:** {{business_owner}}

---

## 13. Approval & Sign-off

<details>
<summary>📋 Guidance</summary>

Record the formal approval of the Charter by the business and programme parties who own
the mandate and budget. An unsigned Charter is a statement of intent, not a mandate.

Note: Architecture governance approval (ARB sign-off on architecture compliance) is a
separate concern managed through the Architecture Governance Framework and the
Implementation Governance Plan — do not conflate business programme approval with
architecture governance approval.

</details>

| Role | Name | Signature / Approval Reference | Date |
|---|---|---|---|
| Programme Sponsor | {{sponsor}} | {{reference}} | {{YYYY-MM-DD}} |
| Programme Director | {{programme_director}} | {{reference}} | {{YYYY-MM-DD}} |
| Lead Architect | {{lead_architect}} | {{reference}} | {{YYYY-MM-DD}} |
| Business Owner | {{business_owner}} | {{reference}} | {{YYYY-MM-DD}} |
| {{other_approver}} | {{name}} | {{reference}} | {{YYYY-MM-DD}} |

**Next Review Date:** {{YYYY-MM-DD}}
*(Charter should be reviewed when: scope changes materially, key assumptions are invalidated, programme structure is revised, or sponsor/programme director changes)*

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
Record governance decisions made during the development or execution of this Charter. Use `/ea-decisions` to generate a cross-artifact Decision Register.
</details>

| ID | Decision | State | Authority | Domain | Cost | Impact | Risk | Subject | Captured By | Owner | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>
Record all stakeholder concerns, objections, and tough questions raised about this Charter. Use `/ea-concerns` to generate a cross-artifact Concerns Register.
</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

*This document was created using the EA Assistant plugin. Use `/ea-decisions` to manage decisions, `/ea-concerns` to manage concerns, and `/ea-risks` to manage the full risk register.*
