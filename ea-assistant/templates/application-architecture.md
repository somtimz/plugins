---
artifact: Application Architecture
artifactId: application-architecture
engagement: {{engagement_name}}
phase: C-App
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Application
  category: Design
  audience: Architecture
  layer: Target
  sensitivity: Internal
  tags: [applications, integration, portfolio, phase-c-app]
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

**Purpose:** The Application Architecture describes the current and target application portfolio, the interactions between applications, and how applications deliver the capabilities identified in the Business Architecture. It sits between the Business Architecture (what the business needs) and the Technology Architecture (what hosts it) — it is the primary artifact for rationalisation decisions, integration pattern choices, and build/buy/retire decisions.

**What to include:** Baseline application portfolio (named systems with their capability coverage and integration points), target application portfolio (what is retained, decommissioned, replaced, or introduced), integration patterns chosen (with ADR references for significant choices), component diagrams, and the capability-to-application mapping from the Business Architecture. Identify coupling risks and rationalisation opportunities.

**Quality indicators:**
- Applications are named, not generic — "the CRM system" becomes "Salesforce Sales Cloud (v52)"
- Every application in the target portfolio has a disposition: retain, extend, replace, decommission, or introduce
- Integration patterns are justified — a direct point-to-point integration between 10+ systems should trigger a question about integration platform; document why or why not

**Common mistakes:**
- Including infrastructure (servers, cloud services, databases) in the Application Architecture — those belong in Technology Architecture
- Application maps that show systems but not the flows between them — the flows reveal the coupling problems that motivate the architecture
- Omitting the disposition of legacy systems — "retain" is a valid and important architectural decision, not an oversight

**TOGAF reference:** TOGAF 10 Part III, Phase C (§27) — Information Systems Architecture, Application component. Produced in Phase C alongside Data Architecture; both are inputs to Phase D Technology Architecture.

</details>

# Application Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Related Matrices

> **TOGAF relationship matrices for this domain** (manage with `/ea-matrix`; definitions in `matrix-catalogue.md`): Application/Organization (`app-organization`), Role/Application (`role-application`), Application/Function (`app-function`), Application Interaction (`app-interaction`), Capability/Application (`capability-application`). Run `/ea-matrix list` for status.

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Overview of the application portfolio: what is being retired, consolidated, or introduced, and why.
Diagram: Application landscape heat map (domain × lifecycle state)
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Application Context

<details>
<summary>📋 Guidance</summary>

Describe the application landscape context: the business capabilities being supported, any
strategic direction for the application portfolio (cloud-first, SaaS migration, rationalisation),
and the key pain points with the current application estate (duplication, integration complexity,
technical debt, unsupported systems). Reference the Business Architecture.

</details>

{{application_context}}

---

## 1a. User Journeys & Use Cases

<details>
<summary>📋 Guidance</summary>

Map the key user journeys this application landscape must support. Trace from the Business Architecture Use Case Catalog (UC-NNN). Every architecturally significant use case should resolve to at least one application component that owns its execution.

- **Supported By** — list the APP-NNN IDs of the application components that jointly deliver this use case.
- **Key Interaction Points** — the named touchpoints where the actor interacts with the application (e.g. "web portal checkout page", "mobile push notification", "batch import API").
- **NFR Sensitivity** — the non-functional characteristic most at risk for this use case: Performance (latency / throughput), Availability (uptime / failover), Security (auth / data protection), or None (low sensitivity).

Gaps: any UC-NNN from the Business Architecture that maps to no application component is an application architecture gap — add it to §6.

</details>

| UC-NNN | Use Case | Primary Actor | Supported By (APP-NNN) | Key Interaction Points | NFR Sensitivity |
|---|---|---|---|---|---|
| [[UC-001]] | {{use_case}} | {{actor}} | {{app_ids}} | {{interaction_points}} | Performance / Availability / Security / None |

---

## 2. Current Application Portfolio

<details>
<summary>📋 Guidance</summary>

Catalogue the applications currently in scope. For each application, capture its function,
technology stack, lifecycle status, and the business capabilities it supports. This forms
the baseline. Flag applications that are end-of-life, unsupported, or candidates for retirement.

</details>

| App ID | Application Name | Function | Technology | Lifecycle Status | Capabilities Supported |
|---|---|---|---|---|---|
| [[APP-001]] | {{app_name}} | {{function}} | {{technology}} | Current / Aging / EOL / Retiring | {{capabilities}} |
| [[APP-002]] | {{app_name}} | {{function}} | {{technology}} | Current / Aging / EOL / Retiring | {{capabilities}} |

*Reference diagram:* `../diagrams/{{current_app_landscape_diagram}}`

---

## 3. Target Application Landscape

<details>
<summary>📋 Guidance</summary>

Describe the target state: which applications are retained, replaced, retired, or introduced.
Explain the rationale for significant decisions (e.g. why a particular SaaS product was chosen,
why a legacy system is being retained). Include a target landscape diagram.

</details>

{{target_application_description}}

| App ID | Application Name | Status | Replaces | Rationale |
|---|---|---|---|---|
| {{app_id}} | {{app_name}} | Retain / Replace / Retire / New | {{replaced_app}} | {{rationale}} |

*Reference diagram:* `../diagrams/{{target_app_landscape_diagram}}`

---

## 4. Application Components

<details>
<summary>📋 Guidance</summary>

For each significant target application or component, describe its responsibilities, boundaries, internal structure, and service contracts. Use ArchiMate Application Component notation where applicable. Focus on components that are new, changed, or architecturally significant.

- **Architecture Pattern** — the dominant structural style for this component.
- **Internal Modules / Layers** — major internal divisions. Common layers: Presentation (UI / API surface), Business Logic (rules, workflows), Data Access (persistence, caching), Integration Adapter (outbound connectors). Only document layers that are architecturally distinct — don't invent layers that don't exist.
- **Service Contracts** — the services this component exposes to other components or external consumers. Each service contract is a commitment — it implies versioning, SLA, and governance.

</details>

### {{component_name_1}}

| Field | Value |
|---|---|
| **Responsibility** | {{responsibility}} |
| **Owner** | {{owner}} |
| **Architecture Pattern** | Microservices / Modular Monolith / Serverless / Event-driven / COTS / Hybrid |
| **Deployment Model** | On-premise / SaaS / PaaS / IaaS |
| **Data Managed** | {{data_managed}} |
| **Replaces / Consolidates** | {{predecessor}} |

**Internal Modules / Layers:**

| Layer | Module | Responsibility |
|---|---|---|
| Presentation | {{module}} | {{responsibility}} |
| Business Logic | {{module}} | {{responsibility}} |
| Data Access | {{module}} | {{responsibility}} |
| Integration Adapter | {{module}} | {{responsibility}} |

**Service Contracts:**

| Service / API | Type | Consumers | SLA |
|---|---|---|---|
| {{service_name}} | REST / GraphQL / Event / gRPC | {{consumers}} | {{response_time, availability}} |

#### ABBs for {{component_name_1}}

<!-- GUIDANCE: List the logical, vendor-neutral components (ABB-NNN) that realise requirements for this application component. Each ABB is implemented by one or more SBBs in the Technology Architecture. Use `/ea-detail new ABB-NNN` to create a detail file for complex ABBs.

Naming Convention:
- Use a noun phrase describing the logical function (e.g. "Immutable Log Store", not "Back up logs")
- Must be vendor-neutral and technology-agnostic — no product names, brands, versions, or cloud-provider terms
- If a vendor name appears in the Name or Description, it is SBB content — redirect to /ea-sbbs new
- See `skills/ea-artifact-templates/references/abb-catalogue.md` for standard reusable ABB names
- **AI/ML engagements:** If the engagement includes AI/ML, reference the AI Systems & Applications domain in the catalogue. Common Phase C ABBs for AI applications: RAG Orchestrator, Prompt Management Service, Model Serving Endpoint, AI Application Front-End, Human-in-the-Loop Review Service.
-->

| ABB-NNN | Name | Description | Satisfies (REQ-NNN) | Implemented by (SBB-NNN) |
|---|---|---|---|---|
| *(none captured)* | — | — | — | — |

---

### {{component_name_2}}

| Field | Value |
|---|---|
| **Responsibility** | {{responsibility}} |
| **Owner** | {{owner}} |
| **Architecture Pattern** | Microservices / Modular Monolith / Serverless / Event-driven / COTS / Hybrid |
| **Deployment Model** | On-premise / SaaS / PaaS / IaaS |
| **Data Managed** | {{data_managed}} |
| **Replaces / Consolidates** | {{predecessor}} |

**Internal Modules / Layers:**

| Layer | Module | Responsibility |
|---|---|---|
| Presentation | {{module}} | {{responsibility}} |
| Business Logic | {{module}} | {{responsibility}} |
| Data Access | {{module}} | {{responsibility}} |

**Service Contracts:**

| Service / API | Type | Consumers | SLA |
|---|---|---|---|
| {{service_name}} | REST / GraphQL / Event / gRPC | {{consumers}} | {{response_time, availability}} |

#### ABBs for {{component_name_2}}

<!-- GUIDANCE: List the logical, vendor-neutral components (ABB-NNN) that realise requirements for this application component. Each ABB is implemented by one or more SBBs in the Technology Architecture. Use `/ea-detail new ABB-NNN` to create a detail file for complex ABBs.

Naming Convention:
- Use a noun phrase describing the logical function (e.g. "Immutable Log Store", not "Back up logs")
- Must be vendor-neutral and technology-agnostic — no product names, brands, versions, or cloud-provider terms
- If a vendor name appears in the Name or Description, it is SBB content — redirect to /ea-sbbs new
- See `skills/ea-artifact-templates/references/abb-catalogue.md` for standard reusable ABB names
- **AI/ML engagements:** If the engagement includes AI/ML, reference the AI Systems & Applications domain in the catalogue. Common Phase C ABBs for AI applications: RAG Orchestrator, Prompt Management Service, Model Serving Endpoint, AI Application Front-End, Human-in-the-Loop Review Service.
-->

| ABB-NNN | Name | Description | Satisfies (REQ-NNN) | Implemented by (SBB-NNN) |
|---|---|---|---|---|
| *(none captured)* | — | — | — | — |

---

## 5. Integration Architecture

<details>
<summary>📋 Guidance</summary>

Describe how applications communicate and exchange data. Specify the integration patterns
adopted (event-driven, API-first, ESB, point-to-point) and the rationale. Identify any
integration platform or middleware in the target state. Highlight integrations with external
parties. Include an integration diagram.

</details>

### Integration Principles
{{integration_principles}}

### Integration Pattern
{{integration_pattern}}

*Reference diagram:* `../diagrams/{{integration_diagram}}`

| Integration ID | Source App | Target App | Pattern | Protocol | Data Exchanged |
|---|---|---|---|---|---|
| [[INT-001]] | {{source}} | {{target}} | Sync API / Async Event / Batch | {{protocol}} | {{data}} |
| [[INT-002]] | {{source}} | {{target}} | Sync API / Async Event / Batch | {{protocol}} | {{data}} |

### API Catalog

<details>
<summary>📋 Guidance</summary>

List all APIs exposed by application components to other components or external consumers. This catalog is the authoritative reference for integration teams and is the input to API gateway configuration. Include both internal (component-to-component) and external (partner / public) APIs. Omit database-level or internal library calls — only document service boundaries.

</details>

| API ID | Name | Provider (APP-NNN) | Consumers | Type | Protocol | Auth Method | SLA |
|---|---|---|---|---|---|---|---|
| [[API-001]] | {{api_name}} | {{provider_app}} | {{consumers}} | REST / GraphQL / Event / gRPC | {{protocol}} | OAuth2 / mTLS / API Key / None | {{response_time, availability}} |

---

## 6. Gap Analysis

<details>
<summary>📋 Guidance</summary>

Summarise the key application architecture gaps between current and target state.
Typical gaps: missing capabilities, duplicated applications, unsupported integrations,
shadow IT, applications without a clear owner. Reference the full Gap Analysis artifact.

</details>

*See Gap Analysis artifact for full detail:* `gap-analysis.md`

| Gap ID | Description | Priority | Impact |
|---|---|---|---|
| [[GAP-001]] | {{description}} | High / Med / Low | {{impact}} |

---

## 7. Requirements Addressed

<details>
<summary>📋 Guidance</summary>

Map this artifact to requirements from the Requirements Register to demonstrate traceability.
Every significant architectural decision should be traceable to at least one requirement.

</details>

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

## 8. Diagrams

<details>
<summary>📋 Guidance</summary>

Standard diagrams for the Application Architecture. Diagrams are stored in `diagrams/` relative to the engagement root and embedded in exported documents via `/ea-generate`. Use `/ea-diagram` to create or edit. See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

</details>

| Diagram | File | Status |
|---|---|---|
| Application Cooperation View | `../../diagrams/application-architecture-cooperation.mmd` | ❌ Missing |
| Application Component Map | `../../diagrams/application-architecture-component-map.mmd` | ❌ Missing |

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
*Use `/ea-decisions` to generate a cross-artifact Decision Register from all A3 tables.*
*Use `/ea-concerns` to generate a cross-artifact Concerns Register from all A4 tables.*
