---
id: RA-{{id}}
name: {{name}}
domain: {{domain}}
status: Draft
version: 1.0.0
source: {{source}}
industryBody: "{{industryBody}}"
linkedCAPs: []
linkedSTDs: []
linkedADRs: []
linkedSBBs: []
reviewCadence: ""
createdDate: {{date}}
lastModified: {{date}}
---

<details>
<summary>📋 Guidance</summary>

A reference architecture is a **governed, reusable blueprint** for a *class* of solutions — prescriptive enough that independent teams build interoperable, secure, aligned systems, but not so prescriptive it becomes a solution architecture. It sits between business strategy and implementation. See the **Reference Architecture (RA-NNN)** concept in `ea-concepts.md` for the full definition, failure modes, and the stress test.

**The boundaries are what give it governance value** — fill in Mandatory vs Optional Components, Integration Mechanisms, Security Trust Boundaries, Data Sovereignty, and Operational Responsibilities, or this devolves into "architecture by PowerPoint". Stay technology-neutral (name ABBs and standards; reference approved SBBs — don't bake in one vendor).

</details>

## Overview

<details>
<summary>📋 Guidance</summary>

What this architectural pattern is, the class of solutions it governs, and when to use it. 1–3 paragraphs. State the core consistency goal: what should look the same across every solution built from this RA.

</details>

<!-- Describe what this RA is and when to use it. -->

## Scope & Domain

<details>
<summary>📋 Guidance</summary>

The domain this RA governs (e.g. Customer Engagement, Integration, Data & Analytics, Cloud, IAM) and the boundary of the solution class. State explicitly what is in scope and what is out of scope — an RA without a boundary governs nothing.

</details>

| In scope | Out of scope |
|---|---|
| | |

## Capability Alignment

<details>
<summary>📋 Guidance</summary>

Which business capabilities (CAP-NNN) this RA serves — the start of capability→technology traceability. Every RA should trace to at least one capability, or its strategic purpose is unclear.

</details>

| CAP-NNN | Capability | How this RA enables it |
|---|---|---|
| | | |

## Architecture Layers

<details>
<summary>📋 Guidance</summary>

The logical service decomposition — the layers/services every conforming solution composes (e.g. presentation, API, identity & access, business services, data services, observability, security controls), expressed as ABB-NNN. Logical and vendor-neutral.

</details>

| Layer | ABB-NNN | ABB Name | Role in Pattern |
|---|---|---|---|
| | | | |

## Mandatory vs Optional Components

<details>
<summary>📋 Guidance</summary>

The single most important governance section. What **must** every conforming solution include, and what **may** it include? Mandatory components are checked at architecture review; optional ones preserve design freedom.

</details>

| Component (ABB-NNN) | Mandatory / Optional | Conformance note |
|---|---|---|
| | Mandatory | |
| | Optional | |

## Integration Patterns & Mechanisms

<details>
<summary>📋 Guidance</summary>

The approved ways components interact — e.g. "all external access goes through an API gateway", "applications publish events to the event bus", "authentication uses the central identity provider". Name the pattern and whether it is mandatory.

</details>

| Interaction | Approved pattern / mechanism | Mandatory? |
|---|---|---|
| | | Yes |

## Information Flows

<details>
<summary>📋 Guidance</summary>

How key data moves between the components/layers above — source → mechanism → destination. Reference a diagram if one exists.

</details>

| Flow | From | To | Mechanism | Notes |
|---|---|---|---|---|
| | | | | |

## Security Architecture & Trust Boundaries

<details>
<summary>📋 Guidance</summary>

Where trust crosses a boundary, and the controls at each crossing. Name the trust zones and the security patterns (authn/authz, encryption, segmentation) a conforming solution inherits.

</details>

| Trust boundary | Crossing | Required control / pattern |
|---|---|---|
| | | |

## Data Ownership & Sovereignty

<details>
<summary>📋 Guidance</summary>

Master-data services, data ownership boundaries, and residency/sovereignty requirements. Which component is the authoritative source for which data, and where may that data physically reside?

</details>

| Data domain | Authoritative source (master) | Ownership boundary | Residency / sovereignty requirement |
|---|---|---|---|

## Technology Standards

<details>
<summary>📋 Guidance</summary>

The STD-NNN standards this RA mandates — technology-neutral (protocols, formats, conformance specs), not product names. Vendor specifics live in approved SBBs, not here.

</details>

| STD-NNN | Standard | Mandatory? |
|---|---|---|
| | | Yes |

## Non-Functional Requirements

<details>
<summary>📋 Guidance</summary>

The NFR envelope every conforming solution inherits (availability, performance, scalability, security, observability…). Give measurable targets where possible — these become conformance criteria.

</details>

| NFR category | Target / envelope | Conformance check |
|---|---|---|
| | | |

## Key Decisions

<details>
<summary>📋 Guidance</summary>

The significant architectural decisions baked into this RA, each with a rationale summary and a candidate ADR. These are the choices a solution team inherits rather than re-litigates.

</details>

| Decision | Rationale Summary | Candidate ADR Title |
|---|---|---|
| | | |

## Constraints

<details>
<summary>📋 Guidance</summary>

Constraints this RA imposes on conforming solutions (CST-NNN candidates), each flagged Mandatory or flexible.

</details>

| Description | Candidate CST Title | Flexibility |
|---|---|---|
| | | Mandatory |

## Implied Principles

<details>
<summary>📋 Guidance</summary>

The architecture principles (BP/DP/AP/TP-NNN) this RA assumes and applies. An RA applies principles; it does not restate them as universal rules.

</details>

- <!-- e.g. AP-001: Loose Coupling -->

## Governance Checkpoints & Conformance

<details>
<summary>📋 Guidance</summary>

The measurable conformance criteria used when a solution is reviewed against this RA — and where in the lifecycle each is checked (typically Phase G). Without conformance criteria an RA has no governance teeth. Also note adoption metrics, if tracked.

</details>

| Checkpoint | Conformance criterion (measurable) | Checked at |
|---|---|---|
| | | Phase G review |

**Adoption metric:** <!-- e.g. % of new solutions in this domain conforming; reviewed quarterly -->

## Operational Responsibilities

<details>
<summary>📋 Guidance</summary>

Who runs and supports what — the operational ownership a conforming solution must arrange (shared services it consumes vs components it operates itself).

</details>

| Component / service | Operated by | Consumed as shared service? |
|---|---|---|

## Adoption Notes

<details>
<summary>📋 Guidance</summary>

What is mandatory vs flexible when adopting this RA, and known acceptable adaptations. Help a solution team understand where they have freedom.

</details>

<!-- What is mandatory vs. flexible when adopting this RA. Note known adaptations. -->

## Stress Test

<details>
<summary>📋 Guidance</summary>

Record the RA's answer to the consistency-vs-freedom stress test. A good RA survives: *"If three independent teams build three different systems from this RA, will their solutions exhibit consistent security, integration, data-management, operational, and governance characteristics without extensive coordination?"* If no → under-specified; if yes but the three are near-identical → over-constrained.

</details>

- **Three-teams test verdict:** <!-- Consistent without over-constraining? Where is guidance thin or too tight? -->

## Grill Checklist

<details>
<summary>📋 Guidance</summary>

Testable conformance statements (present tense) that `/ea-grill` runs when this RA is adopted by an engagement. Each should be objectively checkable against a solution.

</details>

1. <!-- Testable statement in present tense -->
