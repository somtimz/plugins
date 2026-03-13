---
artifact: Application Architecture
engagement: {{engagement_name}}
phase: C
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Application Architecture is a Phase C artifact that describes the current and target
  application portfolio, the interactions between applications, and how applications deliver
  the capabilities identified in the Business Architecture. It sits between the Business
  Architecture (what the business needs) and the Technology Architecture (what infrastructure
  hosts it). Application Architecture drives integration decisions, rationalisation opportunities,
  and build/buy/retire choices.
-->

# Application Architecture

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## 1. Application Context

<!-- GUIDANCE:
  Describe the application landscape context: the business capabilities being supported, any
  strategic direction for the application portfolio (cloud-first, SaaS migration, rationalisation),
  and the key pain points with the current application estate (duplication, integration complexity,
  technical debt, unsupported systems). Reference the Business Architecture.
-->

{{application_context}}

---

## 2. Current Application Portfolio

<!-- GUIDANCE:
  Catalogue the applications currently in scope. For each application, capture its function,
  technology stack, lifecycle status, and the business capabilities it supports. This forms
  the baseline. Flag applications that are end-of-life, unsupported, or candidates for retirement.
-->

| App ID | Application Name | Function | Technology | Lifecycle Status | Capabilities Supported |
|---|---|---|---|---|---|
| APP-001 | {{app_name}} | {{function}} | {{technology}} | Current / Aging / EOL / Retiring | {{capabilities}} |
| APP-002 | {{app_name}} | {{function}} | {{technology}} | Current / Aging / EOL / Retiring | {{capabilities}} |

*Reference diagram:* `../diagrams/{{current_app_landscape_diagram}}`

---

## 3. Target Application Landscape

<!-- GUIDANCE:
  Describe the target state: which applications are retained, replaced, retired, or introduced.
  Explain the rationale for significant decisions (e.g. why a particular SaaS product was chosen,
  why a legacy system is being retained). Include a target landscape diagram.
-->

{{target_application_description}}

| App ID | Application Name | Status | Replaces | Rationale |
|---|---|---|---|---|
| {{app_id}} | {{app_name}} | Retain / Replace / Retire / New | {{replaced_app}} | {{rationale}} |

*Reference diagram:* `../diagrams/{{target_app_landscape_diagram}}`

---

## 4. Application Components

<!-- GUIDANCE:
  For each significant target application or component, describe its responsibilities,
  boundaries, and key interfaces. Use ArchiMate Application Component notation where applicable.
  Focus on the components that are new, changed, or architecturally significant.
-->

### {{component_name_1}}

| Field | Value |
|---|---|
| **Responsibility** | {{responsibility}} |
| **Owner** | {{owner}} |
| **Deployment Model** | On-premise / SaaS / PaaS / IaaS |
| **Key Interfaces** | {{interfaces}} |
| **Data Managed** | {{data_managed}} |
| **Replaces / Consolidates** | {{predecessor}} |

### {{component_name_2}}

| Field | Value |
|---|---|
| **Responsibility** | {{responsibility}} |
| **Owner** | {{owner}} |
| **Deployment Model** | On-premise / SaaS / PaaS / IaaS |
| **Key Interfaces** | {{interfaces}} |
| **Data Managed** | {{data_managed}} |
| **Replaces / Consolidates** | {{predecessor}} |

---

## 5. Integration Architecture

<!-- GUIDANCE:
  Describe how applications communicate and exchange data. Specify the integration patterns
  adopted (event-driven, API-first, ESB, point-to-point) and the rationale. Identify any
  integration platform or middleware in the target state. Highlight integrations with external
  parties. Include an integration diagram.
-->

### Integration Principles
{{integration_principles}}

### Integration Pattern
{{integration_pattern}}

*Reference diagram:* `../diagrams/{{integration_diagram}}`

| Integration ID | Source App | Target App | Pattern | Protocol | Data Exchanged |
|---|---|---|---|---|---|
| INT-001 | {{source}} | {{target}} | Sync API / Async Event / Batch | {{protocol}} | {{data}} |
| INT-002 | {{source}} | {{target}} | Sync API / Async Event / Batch | {{protocol}} | {{data}} |

---

## 6. Gap Analysis

<!-- GUIDANCE:
  Summarise the key application architecture gaps between current and target state.
  Typical gaps: missing capabilities, duplicated applications, unsupported integrations,
  shadow IT, applications without a clear owner. Reference the full Gap Analysis artifact.
-->

*See Gap Analysis artifact for full detail:* `gap-analysis.md`

| Gap ID | Description | Priority | Impact |
|---|---|---|---|
| GAP-001 | {{description}} | High / Med / Low | {{impact}} |

---

## 7. Requirements Addressed

<!-- GUIDANCE:
  Map this artifact to requirements from the Requirements Register to demonstrate traceability.
  Every significant architectural decision should be traceable to at least one requirement.
-->

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

*This document was created using the EA Assistant plugin.*
