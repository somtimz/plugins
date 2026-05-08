---
artifact: Business Architecture
engagement: {{engagement_name}}
phase: B
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.6
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Business
  category: Design
  audience: Business
  layer: Target
  sensitivity: Internal
  tags: [capabilities, processes, organisation, phase-b]
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
| Linked to Architecture Vision | ⚠️ Pending | |
| Traces to Requirements Register | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

The Business Architecture describes the business strategy, governance, organisation, and
key business processes. It is the foundation for the Application and Technology architectures.
Phase B takes Architecture Vision as its primary input.

</details>

<details>
<summary>💡 Practitioner Tip — Phase B</summary>

- **Map capabilities to value streams** — don't model capabilities in isolation. A capability without a value stream is a theory, not architecture. (Deep tactic #11)
- Identify **differentiating vs commodity capabilities** — optimize investment accordingly; don't over-invest in commodity. (Deep tactic #12)
- Use business architecture to **challenge org design**, not just reflect it. If the org structure prevents the target state, say so. (Deep tactic #13)
- Link capabilities directly to **KPIs and revenue/cost drivers** — business architecture is a compression function that turns ambiguity into constraints. (Deep tactic #14)
- Focus on **"where to play" and "how to win"** — not just process diagrams. (Deep tactic #15)
- Gaps are **opportunities disguised as problems** — frame them as investments, not deficiencies. (Tip #18)
- **Two Layers check** — ensure Use Cases, Requirements, and Goals in this artifact describe *business operations* (what the business does), not *EA governance* (how architecture is governed). If a Use Case subject is "governance process," "review board," or "standard," it belongs in the EA / TOGAF layer (Governance Framework, Architecture Principles) — not here. See `ea-concepts.md` → **Two Layers of Intent**.

</details>

# Business Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Overview of the business model, key capabilities, and structural changes required. Written for an executive or business sponsor audience.
Diagram: Capability map or value chain diagram showing current vs. target capability maturity
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Business Context

<details>
<summary>📋 Guidance</summary>

Describe the business context: industry, operating model, strategic direction.
Reference the Architecture Vision for strategic goals.

</details>

{{business_context}}

---

## 2. Organisation Model

<details>
<summary>📋 Guidance</summary>

Describe the organisational structure relevant to this architecture.
Include a diagram reference if available.

</details>

{{organisation_model}}

*Reference diagram:* `../diagrams/{{org_diagram}}`

---

## 3. Business Capabilities

<details>
<summary>📋 Guidance</summary>

Define capabilities using a three-level hierarchy. Each capability gets a CAP-NNN ID.

- **L1** — capability domain (broadest grouping, e.g. Customer Management, Operations, Finance)
- **L2** — capability within a domain (the primary unit of analysis)
- **L3** — sub-capability (only add where a known gap or deliverable requires it)

**Maturity scale:**
- **Absent** — capability does not exist today
- **Immature** — exists but ad hoc, inconsistent, or person-dependent
- **Developing** — repeatable and documented but not optimised
- **Mature** — optimised, governed, and performing well

**Supports column:** link each capability to the STR-NNN strategy or G-NNN goal it enables.
A capability with no strategic anchor should be flagged for removal or reclassification.

**A capability with no value stream exercising it is an orphan — flag it.** Every capability should be traceable to at least one value stream or one use case.

</details>

| CAP-NNN | Level | Capability | Description | Current Maturity | Target Maturity | Supports (STR-NNN / G-NNN) | Details |
|---|---|---|---|---|---|---|---|
| CAP-001 | L1 | {{domain_name}} | {{domain_description}} | Absent / Immature / Developing / Mature | {{target}} | {{STR-NNN or G-NNN}} | — |
| CAP-002 | L2 | {{capability_name}} | {{description}} | Absent / Immature / Developing / Mature | {{target}} | {{STR-NNN or G-NNN}} | — |
| CAP-003 | L3 | {{sub_capability_name}} | {{description}} | Absent / Immature / Developing / Mature | {{target}} | {{STR-NNN or G-NNN}} | — |

---

## 3a. Value Streams

<details>
<summary>📋 Guidance</summary>

A value stream is an end-to-end set of activities that delivers a result of value to a stakeholder (customer, partner, regulator, or internal consumer). Value streams sit above processes — a single value stream typically spans multiple business processes and exercises several capabilities.

Populate this section before detailing processes in §4 — value streams provide the organising context for process decomposition.

- Every value stream must have a named trigger (what initiates it) and a named end outcome (what the stakeholder receives).
- Map each value stream to the capabilities it exercises — this reveals which capabilities are strategically load-bearing.
- Any step in a value stream with no covering capability is a capability gap — flag it for §7 Gap Analysis.
- Any value stream with no linked Goal or Strategy is an orphan — flag it.

</details>

| VS-NNN | Value Stream | Description | Trigger | End Outcome | Key Capabilities (CAP-NNN) | Strategic Link (G-NNN / STR-NNN) | Details |
|---|---|---|---|---|---|---|---|
| VS-001 | {{value_stream_name}} | {{description}} | {{trigger}} | {{end_outcome}} | {{cap_ids}} | {{strategic_link}} | — |

---

## 4. Business Processes

<details>
<summary>📋 Guidance</summary>

Describe the key business processes in scope. Map each process to the value stream it contributes to (§3a) and the capabilities it exercises (§3).

For each process, capture the step-by-step flow using the Steps table — this is the primary architecture deliverable. Actors should be roles (not individuals). System/App column should reference APP-NNN IDs from the Application Architecture once available; use system names if IDs are not yet assigned.

Decision / Rule column captures the business logic applied at each step — this is often where integration complexity, compliance requirements, and system boundaries emerge.

</details>

### {{process_name}}

- **Purpose:** {{purpose}}
- **Value Stream:** {{VS-NNN — value stream this process contributes to}}
- **Trigger:** {{trigger}}
- **Inputs:** {{inputs}}
- **Outputs:** {{outputs}}
- **Actors:** {{actors}}
- **SLA / Performance:** {{e.g. "Complete within 2 business days"}}
- **Diagram:** `../diagrams/{{process_diagram}}`

**Steps:**

| Step | Description | Actor / Role | System / App | Decision / Business Rule |
|---|---|---|---|---|
| 1 | {{step_description}} | {{actor}} | {{system}} | {{decision_or_rule}} |
| 2 | {{step_description}} | {{actor}} | {{system}} | {{decision_or_rule}} |

**Exceptions:**
- {{exception_name}}: {{what triggers it and what happens}}

---

## 4a. Use Case Catalog

<details>
<summary>📋 Guidance</summary>

A use case captures what an actor needs to accomplish, not how the system implements it. Use cases bridge the business architecture (what capabilities are needed) and the application architecture (which components must support the actor's goal).

- **Actors** are roles, not individuals: Customer, Supplier, Finance Officer, Regulator, External System.
- **Goal** is the outcome the actor wants — stated from the actor's perspective.
- **Main Success Scenario** — one sentence summarising the normal path to success. Detailed step-by-step flows belong in functional specifications, not here.
- **Capabilities Used** — links to CAP-NNN entries. Any use case with no covering capability is a capability gap; flag it in §7.
- **Requirements generation** — every use case must generate at least one REQ-NNN requirement. A use case with no requirements is a modeling gap — flag it.

**⚠️ Two Layers check:** If the use case subject is "how we govern" or "how we standardize solutions" (e.g., "Define governance process for AI projects") rather than "what the actor needs" (e.g., "Auto-triage cases with AI"), it is an **EA Capability Use Case** — route it to the Governance Framework or Architecture Principles, not the Business Architecture. See `ea-concepts.md` → **Two Layers of Intent**.

Assign UC-NNN IDs sequentially. These IDs are referenced in the Application Architecture (§1a) to trace which application components support each use case.

</details>

| UC-NNN | Use Case | Primary Actor | Goal | Trigger | Preconditions | Main Success Scenario | Capabilities Used (CAP-NNN) | Details |
|---|---|---|---|---|---|---|---|---|
| UC-001 | {{use_case_name}} | {{actor}} | {{goal}} | {{trigger}} | {{preconditions}} | {{one-sentence summary}} | {{cap_ids}} | — |

---

## 5. Business Services

<details>
<summary>📋 Guidance</summary>

List the business services delivered by the organisation.
A business service is an explicitly defined exposed behaviour.

</details>

| Service | Description | Consumer | Provider |
|---|---|---|---|
| {{service_1}} | {{description}} | {{consumer}} | {{provider}} |

---

## 6. Business Information / Data Objects

<details>
<summary>📋 Guidance</summary>

Key business information objects used and produced by the business processes.
These feed into the Data Architecture in Phase C.

</details>

| Information Object | Description | Owner | Sensitivity |
|---|---|---|---|
| {{object_1}} | {{description}} | {{owner}} | Public/Internal/Confidential |

---

## 7. Gap Analysis

<details>
<summary>📋 Guidance</summary>

Compare the current state business architecture with the target state.
Identify gaps that need to be addressed in the solution architecture.

</details>

| Gap | Current State | Target State | Impact |
|---|---|---|---|
| {{gap_1}} | {{current}} | {{target}} | High/Med/Low |

---

## 8. Requirements Addressed

<details>
<summary>📋 Guidance</summary>

List requirements from the Requirements Register that this artifact addresses.

</details>

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

## 8a. Traceability Summary

<details>
<summary>📋 Guidance</summary>

The Business Architecture is the bridge between strategic intent and execution. Every element in this artifact must trace forward to requirements and backward to direction. Use this summary to validate completeness:

- **Every CAP-NNN** links to at least one G-NNN or STR-NNN (via the Supports column). A capability with no strategic anchor is an orphan.
- **Every VS-NNN** exercises CAP-NNN capabilities and links to G-NNN/STR-NNN (via the Strategic Link column). A value stream with no linked Goal or Strategy is an orphan.
- **Every Business Process** contributes to a VS-NNN value stream. A process with no parent value stream is an orphan.
- **Every UC-NNN** consumes processes and generates REQ-NNN requirements. A use case with no requirements is a modeling gap.
- **Every REQ-NNN** traces back through UC/CAP/VS to G-NNN/OBJ-NNN. A requirement with no upstream trace is an orphan.

```
G-NNN / STR-NNN ──► CAP-NNN ──► VS-NNN ──► Process ──► UC-NNN ──► REQ-NNN
```

Flag any orphan or gap in §7 Gap Analysis.

</details>

---

## 9. Diagrams

<details>
<summary>📋 Guidance</summary>

Standard diagrams for the Business Architecture. Diagrams are stored in `diagrams/` relative to the engagement root and embedded in exported documents via `/ea-generate`. Use `/ea-diagram` to create or edit. See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

</details>

| Diagram | File | Status |
|---|---|---|
| Capability Map | `../../diagrams/business-architecture-capability-map.mmd` | ❌ Missing |
| Business Process Flow | `../../diagrams/business-architecture-process-flow.mmd` | ❌ Missing |
| Organisation Map | `../../diagrams/business-architecture-org-map.mmd` | ❌ Missing |

*Use `/ea-diagram` to create. Run `/ea-generate png` to render for export.*

---

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

Record all decisions made during the development of this artifact.
Use /ea-decisions to aggregate this table across all artifacts into a Decision Register.

</details>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
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

*This document was created using the EA Assistant plugin.*
*Use `/ea-decisions` to generate a cross-artifact Decision Register from all A3 tables.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
