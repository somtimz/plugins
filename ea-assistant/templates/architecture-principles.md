---
artifact: Architecture Principles
engagement: {{engagement_name}}
phase: Prelim
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
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
<summary>📋 Guidance</summary>

Architecture Principles define the rules and guidelines that govern architecture decisions.
They should be agreed with the sponsor and key stakeholders before Phase A begins.
Each principle has a Name, Statement, Rationale, and Implications.
TOGAF recommends 9-15 principles. Too few lack guidance; too many become unmanageable.

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

</details>

# Architecture Principles

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Date:** {{YYYY-MM-DD}}

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

---

## Data Principles

### DP-01: {{principle_name}}

| Field | Value |
|---|---|
| **Statement** | {{principle_statement}} |
| **Rationale** | {{rationale}} |
| **Implications** | {{implications}} |

---

## Application Principles

### AP-01: {{principle_name}}

| Field | Value |
|---|---|
| **Statement** | {{principle_statement}} |
| **Rationale** | {{rationale}} |
| **Implications** | {{implications}} |

---

## Technology Principles

### TP-01: {{principle_name}}

| Field | Value |
|---|---|
| **Statement** | {{principle_statement}} |
| **Rationale** | {{rationale}} |
| **Implications** | {{implications}} |

---

## Principles Summary

| ID | Category | Principle | Status |
|---|---|---|---|
| BP-01 | Business | {{name}} | Draft/Approved |
| DP-01 | Data | {{name}} | Draft/Approved |

---

*This document was created using the EA Assistant plugin.*
