---
artifact: cross-cutting-index
artifactId: cross-cutting-index
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DDTHH:MM:SSZ}}
taxonomy:
templateVersion: 0.9.55
  domain: Cross-cutting
  category: Governance
  audience: Architecture
  layer: Governance
  sensitivity: Internal
  tags: [cross-cutting, index, navigation]
---

# Cross-cutting Artifacts — {{engagement_name}}

Navigation hub for all artifacts that apply across ADM phases. Maintained automatically by `/ea-adrs`, `/ea-decisions`, `/ea-risks`, `/ea-concerns`, `/ea-changes`, `/ea-constraints`, `/ea-zachman`, and `/ea-roles`.

---

## Governance

Architecture decisions, decision log, constraints, and policies.

| Artifact | File | Status | Last Modified |
|---|---|---|---|
| ADR Register | [adr-register-{YYYY-MM-DD}.md](governance/adr-register-{YYYY-MM-DD}.md) | ⚠️ Not generated | — |
| Decision Register | [decision-register-{YYYY-MM-DD}.md](governance/decision-register-{YYYY-MM-DD}.md) | ⚠️ Not generated | — |
| Constraints Register | [constraints-register-{YYYY-MM-DD}.md](governance/constraints-register-{YYYY-MM-DD}.md) | ⚠️ Not generated | — |
| Policies Register | [policies-register-{YYYY-MM-DD}.md](governance/policies-register-{YYYY-MM-DD}.md) | ⚠️ Not generated | — |

> Use `/ea-adrs generate`, `/ea-decisions generate`, `/ea-constraints generate`, `/ea-policies generate` to create or refresh these registers.

---

## Operations

Risk tracking, change requests, and stakeholder concerns.

| Artifact | File | Status | Last Modified |
|---|---|---|---|
| Risk Register | [risk-register-{YYYY-MM-DD}.md](operations/risk-register-{YYYY-MM-DD}.md) | ⚠️ Not generated | — |
| Change Register | [change-register-{YYYY-MM-DD}.md](operations/change-register-{YYYY-MM-DD}.md) | ⚠️ Not generated | — |
| Stakeholder Concerns | [concerns-register-{YYYY-MM-DD}.md](operations/concerns-register-{YYYY-MM-DD}.md) | ⚠️ Not generated | — |

> Use `/ea-risks generate`, `/ea-changes generate`, `/ea-concerns generate` to create or refresh these registers.

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
