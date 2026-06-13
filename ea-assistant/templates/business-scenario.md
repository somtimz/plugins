---
artifact: Business Scenario
artifactId: business-scenario-{{BS-NNN}}
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
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

<details>
<summary>📋 Guidance</summary>

A clear description of the business problem or pain point this scenario addresses. Answer: "What is broken, and why does it matter?" Write it in the stakeholder's language, not the architect's. Link it to the Issues, Problems, and Drivers it stems from so the scenario is anchored in the motivation chain.

</details>

{{problem_statement}}

**Links to:**
- Issues: {{ISS-NNN, ISS-NNN or —}}
- Problems: {{PRB-NNN, PRB-NNN or —}}
- Drivers: {{DRV-NNN, DRV-NNN or —}}

---

## 2. Objectives

<details>
<summary>📋 Guidance</summary>

SMART goals the architecture must meet to resolve this scenario — each with a measure, target, and deadline. An objective that fails the SMART check (no unit, no target, no date) is probably a Goal; move it or sharpen it. Every objective should trace back to the problem in §1.

</details>

| OBJ-NNN | Objective | Measure | Target | Deadline | Priority |
|---|---|---|---|---|---|
| {{OBJ-001}} | {{objective}} | {{unit}} | {{target value}} | {{YYYY-MM-DD}} | High / Medium / Low |

> **SMART check:** Each objective should be Specific (names what changes), Measurable (has a unit and target), Achievable (realistic given constraints), Relevant (directly addresses the problem), and Time-bound (has a deadline). If an entry fails this check, it may be a Goal rather than an Objective.

---

## 3. Environment and Context

<details>
<summary>📋 Guidance</summary>

The business and technology context within which this scenario occurs — internal (structure, capabilities, platforms, budget, mandate), external (market, regulation, partner/customer expectations, competition), and the current technology touchpoints. Capture only what constrains or enables the target state; this is context, not a full baseline architecture.

</details>

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

<details>
<summary>📋 Guidance</summary>

Who is involved in or affected by this scenario, and what they care about most. Capture only the stakeholders directly in this scenario — the full engagement register lives in the Stakeholder Map. Each named concern is a candidate CON-NNN and a test the target state must satisfy.

</details>

| Stakeholder | Role | Primary Concern | Engagement Level |
|---|---|---|---|
| {{stakeholder_1}} | {{role}} | {{concern}} | Informed / Consulted / Responsible / Accountable |
| {{stakeholder_2}} | {{role}} | {{concern}} | Informed / Consulted / Responsible / Accountable |

> Link to Stakeholder Map (`../stakeholder-map.md`) for the full engagement register. This table captures only the stakeholders directly involved in this scenario.

---

## 5. Actors

<details>
<summary>📋 Guidance</summary>

The specific people and systems that participate in this scenario. Actors are not stakeholders — actors take or receive actions in the scenario flow. A **human actor** is a person or role who initiates, approves, or receives outcomes; a **computing actor** is a system, application, service, or device that processes, stores, or transmits information. Mark each computing actor's current state (Existing / To Be Built / To Be Modified) — that feeds the change delta in §9.

</details>

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

<details>
<summary>📋 Guidance</summary>

The specific capabilities the architecture must deliver to resolve this scenario, grouped by domain (Business / Data / Application / Technology) with a MoSCoW priority. Each requirement should trace to an actor, problem, or issue in this scenario. Register each formally with `/ea-requirements add` and set `sourceScenario` so traceability from scenario to requirement is maintained.

</details>

| REQ-NNN | Domain | Statement | Priority | Source (Actor / Problem) |
|---|---|---|---|---|
| {{REQ-001}} | Business / Data / Application / Technology | {{requirement statement}} | Must / Should / Could | {{Actor or PRB-NNN or ISS-NNN}} |

> Run `/ea-requirements add` to formally register each requirement. Set `sourceScenario: {{BS-NNN}}` to maintain traceability from scenario to requirement.

---

## 7. Current State Narrative

<details>
<summary>📋 Guidance</summary>

A plain-language description of what happens today — the "before" picture, written as a stakeholder would describe it, not as an architect would model it. Name the friction points explicitly; they are what the target state must remove and what makes the case for change concrete.

</details>

{{current_state_narrative}}

**Friction points in the current state:**
- {{friction_1}}
- {{friction_2}}

---

## 8. Target State Narrative

<details>
<summary>📋 Guidance</summary>

What will happen after the architecture is delivered — the "after" picture. Write it to be verifiable: stakeholders should be able to confirm whether the target has been reached. The success signals here should map back to the objectives in §2 and the friction points in §7.

</details>

{{target_state_narrative}}

**Success signals in the target state:**
- {{signal_1}}
- {{signal_2}}

---

## 9. Change Delta

<details>
<summary>📋 Guidance</summary>

What specifically changes between current and target state across process, data, application, and technology — and the architecture action each change requires. This is the minimum the architecture must enable; it is the bridge from narrative to work packages, so keep each row concrete and actionable.

</details>

| Dimension | Current State | Target State | Architecture Action Required |
|---|---|---|---|
| Process | {{current process}} | {{target process}} | {{what must be designed/built/changed}} |
| Data | {{current data state}} | {{target data state}} | {{what must be designed/built/changed}} |
| Application | {{current systems}} | {{target systems}} | {{what must be designed/built/changed}} |
| Technology | {{current tech}} | {{target tech}} | {{what must be designed/built/changed}} |

---

## 10. Scenario Diagram (optional)

<details>
<summary>📋 Guidance</summary>

A simple flow or sequence diagram showing the scenario in the target state — Actor → Action → System notation is sufficient. The diagram should match the actors in §5 and the target flow in §8; generate it with `/ea-generate business-scenario-{{BS-NNN}} mermaid`.

</details>

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
