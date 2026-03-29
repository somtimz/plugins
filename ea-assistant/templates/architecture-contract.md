---
artifact: Architecture Contract
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
  sensitivity: Confidential
  tags: [contract, conformance, commitment, phase-g]
---

<details>
<summary>📋 Guidance</summary>

An Architecture Contract is a Phase G artifact representing the joint agreement between the
architecture team and the implementation team on the deliverables, quality, and fitness-for-purpose
of the solution. It is the primary governance instrument during implementation. Contracts should
be established with each major delivery team or project implementing work packages from the
Architecture Roadmap. They give the architecture team standing to review and challenge
implementation decisions that may deviate from the agreed architecture.

</details>

# Architecture Contract

**Engagement:** {{engagement_name}}
**Contract Reference:** {{contract_reference}}
**Organisation:** {{organisation}}
**Architecture Authority:** {{architecture_authority}}
**Implementation Team / Project:** {{implementation_team}}
**Date:** {{YYYY-MM-DD}}
**Version:** {{version}}
**Status:** {{status}}

---

## 1. Contract Purpose

<details>
<summary>📋 Guidance</summary>

State the purpose and scope of this contract. Identify which work packages from the Architecture
Roadmap are covered, and what the implementation team is being authorised to deliver.
The contract creates a mutual obligation: the implementation team commits to conformance;
the architecture team commits to providing timely guidance and decisions.

</details>

{{contract_purpose}}

**Work Packages Covered:** {{work_package_ids}}
**Authorised Deliverables:** {{authorised_deliverables}}

---

## 2. Architecture Conformance Requirements

<details>
<summary>📋 Guidance</summary>

Define the specific architecture conformance requirements that the implementation must satisfy.
These are derived from the target architecture documents (Phase C and D artifacts) and
Architecture Principles. Be precise: vague requirements cannot be assessed objectively.
Distinguish between mandatory conformance requirements and advisory guidance.

</details>

### Mandatory Requirements
<details>
<summary>📋 Guidance</summary>

Mandatory requirements are non-negotiable. Deviation requires formal change request and
Architecture Board approval before implementation proceeds.

</details>

| Req ID | Requirement | Source Artifact | Verification Method |
|---|---|---|---|
| ACR-001 | {{requirement}} | {{source_artifact}} | Design review / Test / Inspection |
| ACR-002 | {{requirement}} | {{source_artifact}} | Design review / Test / Inspection |

### Advisory Guidance
<details>
<summary>📋 Guidance</summary>

Advisory guidance represents preferred approaches. Deviation should be documented and
justified but does not require formal approval.

</details>

| Guidance ID | Guidance | Rationale |
|---|---|---|
| ACG-001 | {{guidance}} | {{rationale}} |

---

## 3. Agreed Standards

<details>
<summary>📋 Guidance</summary>

List the specific technology and design standards the implementation team agrees to follow.
Reference the Technology Architecture standards table. Include versioning requirements where
relevant (e.g. minimum TLS version, approved language runtimes, API specification format).

</details>

| Category | Standard | Version / Specification | Mandatory / Preferred |
|---|---|---|---|
| API Design | {{standard}} | {{version}} | Mandatory / Preferred |
| Security | {{standard}} | {{version}} | Mandatory / Preferred |
| Logging & Observability | {{standard}} | {{version}} | Mandatory / Preferred |
| {{category}} | {{standard}} | {{version}} | Mandatory / Preferred |

---

## 4. Implementation Constraints

<details>
<summary>📋 Guidance</summary>

Document constraints the implementation team must respect. These may be architectural
(do not introduce new data stores outside the approved pattern), operational (no changes
during business-critical periods), commercial (approved vendor list), or regulatory
(data residency, security clearance for personnel). Constraints differ from requirements:
they bound the solution space rather than specifying a desired outcome.

</details>

| Constraint | Type | Rationale |
|---|---|---|
| {{constraint_1}} | Architectural / Operational / Commercial / Regulatory | {{rationale_1}} |
| {{constraint_2}} | Architectural / Operational / Commercial / Regulatory | {{rationale_2}} |

---

## 5. Review Schedule

<details>
<summary>📋 Guidance</summary>

Define when architecture reviews will occur during implementation. Include both scheduled
checkpoints (e.g. design review before build, pre-deployment review) and the process for
requesting ad-hoc architecture guidance. Specify what evidence the implementation team
must provide at each review (e.g. updated design documents, test results, ADRs).

</details>

| Review | Trigger / Date | Required Evidence | Reviewer | Outcome |
|---|---|---|---|---|
| Solution Design Review | Before build commences | Solution design document | {{reviewer}} | Approve / Approve with conditions / Reject |
| Pre-deployment Review | Before production deployment | Test results, updated docs | {{reviewer}} | Approve / Approve with conditions / Reject |
| {{review_name}} | {{trigger}} | {{evidence}} | {{reviewer}} | Approve / Approve with conditions / Reject |

### Ad-hoc Guidance Process
{{adhoc_guidance_process}}

---

## 6. Sign-off

<details>
<summary>📋 Guidance</summary>

Both the architecture authority and the implementation team lead must sign to indicate
agreement. Retain the signed contract as part of the engagement record. The contract
should be re-signed if material changes are made to the scope of the work package
or the conformance requirements.

</details>

By signing below, the named parties confirm they have read, understood, and agree to the
terms of this Architecture Contract.

| Role | Name | Organisation | Signature | Date |
|---|---|---|---|---|
| Architecture Authority | {{architecture_authority}} | {{arch_organisation}} | | |
| Implementation Lead | {{implementation_lead}} | {{impl_organisation}} | | |
| {{approver_role}} | {{approver_name}} | {{approver_org}} | | |

---

*This document was created using the EA Assistant plugin.*
