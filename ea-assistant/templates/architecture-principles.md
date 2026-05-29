---
artifactId: architecture-principles
artifact: Architecture Principles
artifactId: architecture-principles
engagement: {{engagement_name}}
phase: Preliminary
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Strategy
  audience: Architecture
  layer: Reference
  sensitivity: Internal
  tags: [principles, standards, governance, preliminary]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Principles have rationale and implications | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** Architecture Principles define the rules and guidelines that govern all architecture decisions in this engagement. They are established in the Preliminary Phase and remain stable across the ADM cycle — every design decision, ADR, and constraint must be reconcilable with the active principle set.

**What to include:** Principles in each of the four TOGAF domains (Business, Data, Application, Technology) that are in scope for this engagement. Each principle requires four standard fields: Name, Statement (with modal verb — must/shall/will), Rationale (citing a business risk, policy, or driver), and Implications (what the principle requires AND what it prohibits). TOGAF recommends 9–15 principles; too few lack guidance, too many become unmanageable.

**Quality indicators:**
- Each principle statement can be used as a test: given a proposed design decision, you can say "this decision is/is not consistent with [principle]"
- Implications include at least one thing the principle *prohibits* — principles that only describe what is required without stating what is ruled out are often ignored at review time
- At least one principle per active architecture domain

**Numbering:** If principles are numbered (P01, P02 …), the sequence must be gapless. A jump
from P10 to P12 means P11 is missing — not deferred. Check the final catalogue before
publishing.

**Activation governance:** Any principle describing how AI systems are enabled (activated,
switched on, or expanded in scope) must specify the approval path, not just a notification
obligation. A "notify the CoE" clause is a governance bypass if the engagement's operating
model requires CoE approval for Tier 2 and Governance Council approval for Tier 1 systems.
Align activation language to the tier-based decision authority defined in the governance model.

**Governance bypass anti-pattern:** Avoid "non-response within N days is treated as approval
to proceed." This converts inaction into a governance gate clearance. Use escalation instead:
if no response is received within the defined timeframe, the requesting party escalates to the
next authority tier who must decide within a stated period.

**Employee impact language:** Absolute formulations ("roles are enhanced, not eliminated") are
harder to defend under legal challenge than qualified ones ("no employee will be laid off
*solely* because of AI automation"). Use the qualified form in formal governance documents.

**Regulatory status:** If a principle's rationale references pending legislation, describe it
as anticipated or pending — not as enacted. Include a "basis for planning" clause that explains
the principle remains valid if the legislation stalls (because it reflects best practice
regardless). Consistent framing across all artifacts prevents contradiction.

**Citizen recourse:** In AI-heavy engagements, consider whether a principle is needed to
address citizen data rights and recourse — the right to know when AI influenced a decision,
to access an explanation, and to request human review. This is distinct from operational
privacy principles (which govern how the organisation handles data) and from accountability
principles (which govern human oversight of decisions). A citizen recourse principle addresses
the citizen's rights directly.

**Common mistakes:**
- Principles that describe how something should be built ("all services must be deployed in containers") rather than a rule about design decisions — those belong in Constraints (CST-NNN) or SBB-NNN choices
- More than 15 principles — quality over quantity; a long principle list is rarely enforced; consolidate where possible
- Implications that are too vague to detect violations ("all teams must consider this") — implications should be specific enough to use in an architecture review

**TOGAF reference:** TOGAF 10 Part III §3 — Architecture Principles. The four-domain structure (Business, Data, Application, Technology) and the four-field format (Name/Statement/Rationale/Implications) follow the TOGAF standard. For the structured register with BP/DP/AP/TP-NNN IDs, see the Principles Register artifact.

</details>

# Architecture Principles

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of the guiding principles adopted and why they matter for decision-making.
Diagram: Principles poster: 2-column card layout (principle name + statement)
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Principle Categories

<details>
<summary>📋 Guidance</summary>

Organise principles into categories: Business, Data, Application, Technology.
Add or remove categories as appropriate.

</details>

---

## Business Principles

### BP-01: {{principle_name}}

| Field | Value |
|---|---|
| **Statement** | {{principle_statement}} |
| **Rationale** | {{rationale}} |
| **Implications** | {{implications}} |
| **Source Policy** | {{POL-NNN or policy name, if derived from an enterprise policy}} |
| **Details** | — |

---

## Data Principles

### DP-01: {{principle_name}}

| Field | Value |
|---|---|
| **Statement** | {{principle_statement}} |
| **Rationale** | {{rationale}} |
| **Implications** | {{implications}} |
| **Source Policy** | {{POL-NNN or policy name, if derived from an enterprise policy}} |
| **Details** | — |

---

## Application Principles

### AP-01: {{principle_name}}

| Field | Value |
|---|---|
| **Statement** | {{principle_statement}} |
| **Rationale** | {{rationale}} |
| **Implications** | {{implications}} |
| **Source Policy** | {{POL-NNN or policy name, if derived from an enterprise policy}} |
| **Details** | — |

---

## Technology Principles

### TP-01: {{principle_name}}

| Field | Value |
|---|---|
| **Statement** | {{principle_statement}} |
| **Rationale** | {{rationale}} |
| **Implications** | {{implications}} |
| **Source Policy** | {{POL-NNN or policy name, if derived from an enterprise policy}} |
| **Details** | — |

---

## Principles Summary

| ID | Category | Principle | Status | Details |
|---|---|---|---|---|
| [BP-01](../details/BP-01.md) | Business | {{name}} | Draft/Approved | [→](../details/BP-01.md) |
| [DP-01](../details/DP-01.md) | Data | {{name}} | Draft/Approved | [→](../details/DP-01.md) |

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
