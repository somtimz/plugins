---
artifact: Business Scenario
artifactId: business-scenario-{{BS-NNN}}
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.53
lastModified: {{YYYY-MM-DD}}
scenarioId: "{{BS-NNN}}"
taxonomy:
  domain: Cross-cutting
  category: Strategy
  audience: Executive
  layer: Motivation
  tags: [business-scenario, phase-a, requirements-elicitation]
relatedArtifacts: ["architecture-vision"]
diagrams: []
links: []
---

<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Problem Statement present | ⚠️ Pending | |
| ≥1 SMART Objective linked | ⚠️ Pending | |
| Environment documented (internal + external) | ⚠️ Pending | |
| ≥1 stakeholder with named concern | ⚠️ Pending | |
| Actors defined (human and/or computing) | ⚠️ Pending | |
| ≥1 Requirement captured | ⚠️ Pending | |
| Current State narrative present | ⚠️ Pending | |
| Target State narrative present | ⚠️ Pending | |

*Run `/ea-grill business-scenario-{{BS-NNN}}` to review completeness.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** A Business Scenario is a TOGAF Phase A technique that bridges business stakeholders and architects by framing architecture needs as a narrative. It describes the problem in terms stakeholders recognise, then derives the technical and business requirements needed to fix it. Scenarios validate the Architecture Vision by grounding it in concrete, lived experience rather than abstract frameworks.

**Key principle:** Focus on **the change** — "What happens today vs. what will happen in the target state." Do not model the current state in exhaustive detail; model the delta that the architecture must enable.

**When to use:**
- Multiple distinct problem domains are in scope — each gets its own scenario
- Stakeholders struggle to engage with abstract driver/goal tables — scenarios make it concrete
- Requirements are contested — scenarios provide a shared narrative that all parties can verify
- Phase A Executive Sponsor sign-off requires a plain-language business case

**TOGAF reference:** TOGAF 10 Part III, Phase A (§25.3.3) — Business Scenarios. Optional but strongly recommended when stakeholder alignment is needed before Phase B.

</details>

---

# Business Scenario: {{BS-NNN}} — {{title}}

**Engagement:** {{engagement_name}}
**Phase:** A — Architecture Vision
**Status:** {{Draft | In Review | Approved}}
**Author:** {{author}}
**Date:** {{YYYY-MM-DD}}

---

## 1. Problem Statement

*A clear description of the business problem or pain point this scenario addresses. Answer: "What is broken, and why does it matter?"*

{{problem_statement}}

**Links to:**
- Issues: {{ISS-NNN, ISS-NNN or —}}
- Problems: {{PRB-NNN, PRB-NNN or —}}
- Drivers: {{DRV-NNN, DRV-NNN or —}}

---

## 2. Objectives

*SMART goals the architecture must meet to resolve this scenario. Each objective must have a measure, target, and deadline.*

| OBJ-NNN | Objective | Measure | Target | Deadline | Priority |
|---|---|---|---|---|---|
| {{OBJ-001}} | {{objective}} | {{unit}} | {{target value}} | {{YYYY-MM-DD}} | High / Medium / Low |

> **SMART check:** Each objective should be Specific (names what changes), Measurable (has a unit and target), Achievable (realistic given constraints), Relevant (directly addresses the problem), and Time-bound (has a deadline). If an entry fails this check, it may be a Goal rather than an Objective.

---

## 3. Environment and Context

*The business and technology context within which this scenario occurs.*

### 3.1 Internal Environment

{{internal_environment}}

*Examples: organisational structure, existing capabilities, current platforms, budget envelope, regulatory mandate.*

### 3.2 External Environment

{{external_environment}}

*Examples: market pressures, regulatory changes, partner/customer expectations, competitive landscape.*

### 3.3 Technology Context — Current State

{{technology_context_current}}

*The specific systems, platforms, and integration points relevant to this scenario today. Focus on what constrains or enables the target state.*

---

## 4. Stakeholders and Concerns

*Who is involved in or affected by this scenario, and what they care about most.*

| Stakeholder | Role | Primary Concern | Engagement Level |
|---|---|---|---|
| {{stakeholder_1}} | {{role}} | {{concern}} | Informed / Consulted / Responsible / Accountable |
| {{stakeholder_2}} | {{role}} | {{concern}} | Informed / Consulted / Responsible / Accountable |

> Link to Stakeholder Map (`../stakeholder-map.md`) for the full engagement register. This table captures only the stakeholders directly involved in this scenario.

---

## 5. Actors

*The specific people and systems that participate in this scenario. Actors are not the same as stakeholders — actors are the ones who take actions or receive actions in the scenario flow.*

### 5.1 Human Actors

| Actor | Type | Role in Scenario |
|---|---|---|
| {{actor_name}} | Human | {{what they do in this scenario}} |

### 5.2 Computing Actors (Systems)

| System | Type | Role in Scenario | Current State |
|---|---|---|---|
| {{system_name}} | Application / Platform / Service / Device | {{what the system does in this scenario}} | Existing / To Be Built / To Be Modified |

> **Human vs Computing Actor:** A human actor is a person or role who initiates, approves, or receives outcomes. A computing actor is a system, application, service, or device that processes, stores, or transmits information in the scenario.

---

## 6. Requirements

*The specific capabilities the architecture must deliver to resolve this scenario. Grouped by domain. Each requirement should trace to this scenario.*

| REQ-NNN | Domain | Statement | Priority | Source (Actor / Problem) |
|---|---|---|---|---|
| {{REQ-001}} | Business / Data / Application / Technology | {{requirement statement}} | Must / Should / Could | {{Actor or PRB-NNN or ISS-NNN}} |

> Run `/ea-requirements add` to formally register each requirement. Set `sourceScenario: {{BS-NNN}}` to maintain traceability from scenario to requirement.

---

## 7. Current State Narrative

*A plain-language description of what happens today — the "before" picture. Written as a stakeholder would describe it, not as an architect would model it.*

{{current_state_narrative}}

**Friction points in the current state:**
- {{friction_1}}
- {{friction_2}}

---

## 8. Target State Narrative

*What will happen after the architecture is delivered — the "after" picture. Written to be verifiable: stakeholders should be able to confirm whether the target has been reached.*

{{target_state_narrative}}

**Success signals in the target state:**
- {{signal_1}}
- {{signal_2}}

---

## 9. Change Delta

*What specifically changes between current and target state. This is the minimum the architecture must enable.*

| Dimension | Current State | Target State | Architecture Action Required |
|---|---|---|---|
| Process | {{current process}} | {{target process}} | {{what must be designed/built/changed}} |
| Data | {{current data state}} | {{target data state}} | {{what must be designed/built/changed}} |
| Application | {{current systems}} | {{target systems}} | {{what must be designed/built/changed}} |
| Technology | {{current tech}} | {{target tech}} | {{what must be designed/built/changed}} |

---

## 10. Scenario Diagram (optional)

*A simple flow or sequence diagram showing the scenario in the target state. Actor → Action → System notation is sufficient.*

```
{{actor_1}} ──[action]──► {{system_1}} ──[result]──► {{actor_2}}
```

*Generate a Mermaid sequence diagram with `/ea-generate business-scenario-{{BS-NNN}} mermaid`.*

---

## Appendix — Traceability

| Element | ID | Notes |
|---|---|---|
| Business Drivers motivating this scenario | {{DRV-NNN}} | |
| Issues this scenario addresses | {{ISS-NNN}} | |
| Problems this scenario addresses | {{PRB-NNN}} | |
| Goals this scenario advances | {{G-NNN}} | |
| Objectives this scenario operationalises | {{OBJ-NNN}} | |
| Requirements generated by this scenario | {{REQ-NNN}} | |
| Architecture Vision section | Architecture Vision §1 / §14 | |
