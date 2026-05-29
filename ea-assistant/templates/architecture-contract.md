---
artifactId: architecture-contract
artifact: Architecture Contract
engagement: {{engagement_name}}
phase: G
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Governance
  layer: Governance
  sensitivity: Confidential
  tags: [contract, conformance, commitment, phase-g]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Linked to Compliance Assessment | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** An Architecture Contract is the joint agreement between the architecture team and the implementation team on what will be built, to what architecture standards, and how conformance will be verified. It gives the architecture team formal standing to review and challenge implementation decisions — without a contract, architecture reviews are advisory only and can be ignored.

**What to include:** Reference to the approved Architecture Definition Document and relevant architecture domain artifacts, the specific principles and standards the implementation must conform to, the conformance verification approach (how and when reviews will occur), a deviation/dispensation process, and the acceptance criteria that must be met before the solution is approved for deployment.

**Quality indicators:**
- Conformance criteria are specific and testable — "the solution must expose all capabilities through versioned REST APIs conformant to the API Design Standard v2.1" is testable; "the solution must follow good practices" is not
- The deviation process is documented — the contract should specify how the delivery team can request a formal dispensation, not just prohibit deviations
- The contract is signed by both the architecture authority and the delivery team lead — unsigned contracts have no governance weight

**Common mistakes:**
- Contracts that list all architecture principles without identifying which ones are actively enforceable for this specific solution — this overwhelms delivery teams
- No conformance schedule — "architecture will review at appropriate times" is not governance; define the gates upfront
- Contracts created once and never revisited when the delivery team raises change requests

**TOGAF reference:** TOGAF 10 Part III, Phase G (§31) — Architecture Contracts. The Architecture Contract is the primary governance instrument of Phase G; it operationalises the Architecture Governance Framework for a specific delivery project.

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

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of agreed architecture commitments, compliance obligations, and governance approach for the implementation programme.
Diagram: Governance and compliance summary table
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

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
| [ACR-001](../details/ACR-001.md) | {{requirement}} | {{source_artifact}} | Design review / Test / Inspection |
| [ACR-002](../details/ACR-002.md) | {{requirement}} | {{source_artifact}} | Design review / Test / Inspection |

### Advisory Guidance
<details>
<summary>📋 Guidance</summary>

Advisory guidance represents preferred approaches. Deviation should be documented and
justified but does not require formal approval.

</details>

| Guidance ID | Guidance | Rationale |
|---|---|---|
| [ACG-001](../details/ACG-001.md) | {{guidance}} | {{rationale}} |

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
