---
artifact: cross-cutting-index
artifactId: cross-cutting-index
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.86
lastModified: {{YYYY-MM-DDTHH:MM:SSZ}}
taxonomy:
  admPhases: [Preliminary, Requirements, A, B, C-Data, C-App, D, E, F, G, H]
  zachmanCell: ""
  domain: Cross-cutting
  category: Governance
  audience: Architecture
  layer: Governance
  sensitivity: Internal
  tags: [cross-cutting, index, navigation]
---

# Cross-cutting Artifacts — {{engagement_name}}

Navigation hub for all artifacts that apply across ADM phases. Maintained automatically by `/ea-adrs`, `/ea-decisions`, `/ea-risks`, `/ea-concerns`, `/ea-changes`, `/ea-constraints`, `/ea-policies`, `/ea-rules`, `/ea-services`, `/ea-valuestreams`, `/ea-processes`, `/ea-usecases`, `/ea-zachman`, and `/ea-roles`.

---

## Governance

Architecture decisions, decision log, constraints, and policies.

| Artifact | File | Status | Last Modified |
|---|---|---|---|
| ADR Register | [adr-register.md](governance/adr-register.md) | ⚠️ Not generated | — |
| Decision Register | [decision-register.md](governance/decision-register.md) | ⚠️ Not generated | — |
| Constraints Register | [constraints-register.md](governance/constraints-register.md) | ⚠️ Not generated | — |
| Policies Register | [policies-register.md](governance/policies-register.md) | ⚠️ Not generated | — |

> Use `/ea-adrs generate`, `/ea-decisions generate`, `/ea-constraints generate`, `/ea-policies generate` to create or refresh these registers.

---

## Operations

Risk tracking, change requests, stakeholder concerns, value streams, business processes, use cases, business rules, and services.

| Artifact | File | Status | Last Modified |
|---|---|---|---|
| Risk Register | [risk-register.md](operations/risk-register.md) | ⚠️ Not generated | — |
| Change Register | [change-register.md](operations/change-register.md) | ⚠️ Not generated | — |
| Stakeholder Concerns | [concerns-register.md](operations/concerns-register.md) | ⚠️ Not generated | — |
| Value Streams Register | [value-streams-register.md](operations/value-streams-register.md) | ⚠️ Not generated | — |
| Business Processes Register | [business-processes-register.md](operations/business-processes-register.md) | ⚠️ Not generated | — |
| Use Cases Register | [use-cases-register.md](operations/use-cases-register.md) | ⚠️ Not generated | — |
| Business Rules Register | [business-rules-register.md](operations/business-rules-register.md) | ⚠️ Not generated | — |
| Business Services Register | [business-services-register.md](operations/business-services-register.md) | ⚠️ Not generated | — |

> Use `/ea-risks generate`, `/ea-changes generate`, `/ea-concerns generate`, `/ea-valuestreams generate`, `/ea-processes generate`, `/ea-usecases generate`, `/ea-rules generate`, `/ea-services generate` to create or refresh these registers.

---

## Context

Classification and role reference artifacts.

| Artifact | File | Status | Last Modified |
|---|---|---|---|
| Zachman Diagram | [zachman-diagram.md](context/zachman-diagram.md) | ⚠️ Not generated | — |
| Role Catalogue | [role-catalogue.md](context/role-catalogue.md) | ⚠️ Not generated | — |

> Use `/ea-zachman generate` and `/ea-roles generate` to create or refresh these artifacts.

---

## Notes

Unscoped cross-cutting notes are stored in `notes/`. Use `/ea-notes cross-cutting` to view or create entries.
