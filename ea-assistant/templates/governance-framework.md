---
artifact: Architecture Governance Framework
engagement: {{engagement_name}}
phase: Prelim
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Strategy
  audience: Governance
  layer: Governance
  sensitivity: Internal
  tags: [governance, arb, decision-rights, preliminary]
---

<details>
<summary>📋 Guidance</summary>

The Architecture Governance Framework is a Preliminary Phase artifact that defines how
architecture decisions are made, enforced, and communicated across the enterprise. It
establishes the structures and processes that all subsequent ADM work operates within.
Without a governance framework, architecture decisions become inconsistent, compliance
checking is informal, and the architecture programme loses credibility with delivery teams.

Create this artifact before beginning Phase A. It should be reviewed and updated whenever
the governance structure changes or the programme scope expands significantly.

</details>

# Architecture Governance Framework

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Prepared By:** {{prepared_by}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}

---

## 1. Purpose & Scope

<details>
<summary>📋 Guidance</summary>

State the purpose of this governance framework and the scope of architecture work it governs.
Be explicit: does it cover the whole enterprise, a programme, a division, or a specific set
of domains? Scope ambiguity is the most common governance failure mode.

</details>

**Purpose:** {{governance_purpose}}

**Scope of Governance:**
{{governance_scope}}

**Out of Scope:**
{{governance_out_of_scope}}

**Relationship to existing governance frameworks (corporate, project, IT):**
{{relationship_to_existing_governance}}

---

## 2. Governance Objectives

<details>
<summary>📋 Guidance</summary>

List 3–6 specific, measurable objectives this governance framework is designed to achieve.
Good governance objectives are outcomes ("Ensure all solution designs are reviewed before
build approval") not activities ("Hold ARB meetings"). Link each objective to a business
driver or strategic goal where possible.

</details>

| # | Objective | Linked Driver / Goal |
|---|---|---|
| 1 | {{objective}} | {{driver_or_goal}} |
| 2 | {{objective}} | {{driver_or_goal}} |
| 3 | {{objective}} | {{driver_or_goal}} |

---

## 3. Governance Structure

<details>
<summary>📋 Guidance</summary>

Describe all governance bodies and their relationships. A typical structure has three levels:
strategic (Architecture Review Board), operational (EA Team), and project-level (EA Liaisons).
Define what each body is authorised to decide without escalation.

</details>

### 3.1 Governance Bodies

| Body | Role | Chair | Members | Meeting Cadence |
|---|---|---|---|---|
| Architecture Review Board (ARB) | Strategic architecture decisions, principle approval, waiver authority | {{arb_chair}} | {{arb_members}} | {{arb_cadence}} |
| EA Working Group | Operational governance, standard setting, compliance review | {{ewg_chair}} | {{ewg_members}} | {{ewg_cadence}} |
| Project EA Liaison | Project-level conformance, local decisions | {{pel_role}} | {{pel_members}} | {{pel_cadence}} |

### 3.2 Roles & Responsibilities

| Role | Responsibilities | Named Individual |
|---|---|---|
| Chief / Lead Architect | Architecture strategy, principle ownership, ARB facilitation | {{lead_architect}} |
| ARB Chair | Meeting governance, tie-breaking, escalation authority | {{arb_chair}} |
| Domain Architects | Domain standards, review inputs, technical authority | {{domain_architects}} |
| Project EA Liaison | Project conformance tracking, waiver requests, local decisions | {{ea_liaison}} |
| Architecture Repository Owner | Artifact storage, version control, access management | {{repo_owner}} |

---

## 4. Architecture Review Board — Terms of Reference

<details>
<summary>📋 Guidance</summary>

The Terms of Reference (ToR) formally establishes the ARB as a governance body. Without a
ToR, the ARB has no agreed authority, quorum, or decision procedure — and its decisions
can be challenged. Keep the ToR brief and practical.

</details>

**Mandate:** {{arb_mandate}}

**Authority Level:** {{arb_authority_level}}
*(e.g., "The ARB is authorised to approve or reject all architecture decisions rated Strategic or Tactical authority and escalate to the CTO/CIO only those with budget implications > $X")*

**Quorum:** {{arb_quorum}}

**Decision Method:** {{arb_decision_method}}
*(e.g., consensus; majority; chair has casting vote)*

**Minutes & Record-Keeping:** {{arb_record_keeping}}

**Review & Renewal:** This ToR is reviewed annually or when governance structure changes.

---

## 5. Decision Rights Matrix

<details>
<summary>📋 Guidance</summary>

Define who can decide what without escalation. Three levels are typical: ARB approval required,
Lead Architect discretion, and Project-level discretion. Be specific — "technology choices"
is too vague; "selection of a new integration platform" is useful.

</details>

| Decision Type | Examples | Authority Level | Escalation Path |
|---|---|---|---|
| Strategic | Architecture principles changes, enterprise platform selection, domain strategy | ARB approval required | CTO / CIO |
| Tactical | Solution pattern selection, cross-domain integrations, significant NFR trade-offs | Lead Architect + ARB notification | ARB |
| Operational | Within-project technology choices within approved patterns, minor deviations | Project EA Liaison | Lead Architect |
| Emergency | Critical production issues requiring immediate deviation from architecture | Lead Architect approval + retrospective ARB review | ARB (next meeting) |

Additional decision types specific to this engagement:

| Decision Type | Examples | Authority Level | Escalation Path |
|---|---|---|---|
| {{decision_type}} | {{examples}} | {{authority}} | {{escalation}} |

---

## 6. ADM Tailoring Decisions

<details>
<summary>📋 Guidance</summary>

Document which ADM phases apply to this engagement, which artifacts are mandatory versus
optional, and any deliberate adaptations to the standard ADM process. Tailoring decisions
are themselves governance decisions and should be recorded here so they cannot be revisited
informally later.

</details>

### 6.1 Phase Applicability

| Phase | Applicable? | Rationale |
|---|---|---|
| Preliminary | Yes | — |
| Requirements | {{yes_no}} | {{rationale}} |
| A — Architecture Vision | Yes | — |
| B — Business Architecture | {{yes_no}} | {{rationale}} |
| C — Data Architecture | {{yes_no}} | {{rationale}} |
| C — Application Architecture | {{yes_no}} | {{rationale}} |
| D — Technology Architecture | {{yes_no}} | {{rationale}} |
| E — Opportunities & Solutions | {{yes_no}} | {{rationale}} |
| F — Migration Planning | {{yes_no}} | {{rationale}} |
| G — Implementation Governance | {{yes_no}} | {{rationale}} |
| H — Architecture Change Management | {{yes_no}} | {{rationale}} |

### 6.2 Mandatory vs Optional Artifacts

| Artifact | Phase | Mandatory / Optional | Rationale if Optional |
|---|---|---|---|
| Architecture Vision | A | Mandatory | — |
| Architecture Principles | Prelim | Mandatory | — |
| {{artifact}} | {{phase}} | {{mandatory_optional}} | {{rationale}} |

### 6.3 ADM Adaptations

{{adm_adaptations}}

---

## 7. Architecture Compliance Process

<details>
<summary>📋 Guidance</summary>

Define how compliance checking is triggered and conducted. Compliance is most effective when
it is scheduled (built into project gates) rather than reactive. The waiver process must be
simple enough that teams use it rather than ignore it — a complex waiver process encourages
silent non-conformance.

</details>

### 7.1 Compliance Checkpoints

| Checkpoint | Trigger | Assessor | Output |
|---|---|---|---|
| Design Review | Before build approval | Lead Architect | Compliance Assessment |
| Pre-Deployment | Before production deployment | Lead Architect + Domain Architect | Compliance Assessment (updated) |
| Post-Implementation | 30 days after go-live | EA Liaison | Conformance Confirmation |
| {{checkpoint}} | {{trigger}} | {{assessor}} | {{output}} |

### 7.2 Waiver & Exception Process

**When a waiver is required:** {{waiver_trigger}}
*(e.g., "Any deviation from an approved architecture principle or a pattern defined in the Technology Standards Catalogue")*

**Waiver Request Process:**
1. {{waiver_step_1}}
2. {{waiver_step_2}}
3. {{waiver_step_3}}

**Waiver Approval Authority:** {{waiver_authority}}

**Waiver Record:** All approved waivers are recorded in the relevant Compliance Assessment artifact and the Decision Register.

---

## 8. Architecture Repository

<details>
<summary>📋 Guidance</summary>

Define where architecture artifacts are stored, how they are versioned, and who has access.
The repository location is less important than the consistency of its use. A single well-known
location is better than a "correct" tool that nobody uses.

</details>

**Repository Location:** {{repository_location}}

**Version Control:** {{version_control_approach}}

**Access Levels:**

| Level | Who | Access |
|---|---|---|
| Author | EA Team | Read / Write / Publish |
| Reviewer | ARB Members, Domain Architects | Read / Comment |
| Consumer | Project Teams, Delivery Leads | Read |
| {{level}} | {{who}} | {{access}} |

**Naming Conventions:** {{naming_conventions}}

**Retention Policy:** {{retention_policy}}

---

## 9. Escalation & Dispute Resolution

<details>
<summary>📋 Guidance</summary>

Define what happens when governance decisions are disputed or when a project team refuses to
comply with an architecture decision. The existence of a clear escalation path — even one
rarely used — signals that governance has teeth.

</details>

**Escalation Triggers:** {{escalation_triggers}}

**Escalation Path:**

| Level | Body / Individual | Timeframe |
|---|---|---|
| 1 | Lead Architect | {{timeframe}} |
| 2 | ARB | {{timeframe}} |
| 3 | CTO / CIO | {{timeframe}} |
| 4 | {{body}} | {{timeframe}} |

**Dispute Resolution Process:** {{dispute_resolution}}

---

## 10. Governance Maturity & Review

<details>
<summary>📋 Guidance</summary>

Governance frameworks that are never reviewed become irrelevant. Define a review cadence and
the criteria for deciding when a major revision is needed (e.g., significant scope change,
governance failures, programme closure).

</details>

**Review Cadence:** {{review_cadence}}

**Review Trigger Conditions:**
- {{trigger_1}}
- {{trigger_2}}
- {{trigger_3}}

**Governance Effectiveness Metrics:**

| Metric | Target | How Measured |
|---|---|---|
| % of projects with ARB review before build approval | {{target}} | {{measurement}} |
| Average waiver decision time | {{target}} | {{measurement}} |
| Non-conformances identified post-deployment | {{target}} | {{measurement}} |
| {{metric}} | {{target}} | {{measurement}} |

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>
Record governance decisions made during the development of this framework. Use `/ea-decisions` to generate a cross-artifact Decision Register.
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

*This document was created using the EA Assistant plugin. Use `/ea-decisions` to manage decisions and `/ea-concerns` to manage concerns.*
