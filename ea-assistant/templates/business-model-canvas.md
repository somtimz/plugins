---
artifactId: business-model-canvas
artifact: Business Model Canvas
engagement: {{engagement_name}}
phase: B
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Business
  category: Strategy
  audience: Executive
  layer: Motivation
  sensitivity: Confidential
  tags: [business-model, value-proposition, phase-b]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Linked to Business Architecture | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** The Business Model Canvas (BMC) describes how the organisation creates, delivers, and captures value. It is used in Phase B to ground the Business Architecture in the actual operating model before layering in capabilities, processes, and services. It makes business model assumptions explicit, enabling architects to identify which assumptions the target architecture is making.

**What to include:** All nine building blocks — Customer Segments, Value Propositions, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, Cost Structure. Populate for both baseline (current state) and target (where significant business model change is involved). Note interdependencies between blocks as you populate them.

**Quality indicators:**
- Value Propositions are stated from the customer's perspective — "reduces order processing time from 3 days to same-day" not "we have a fast order processing system"
- Revenue Streams and Cost Structure are quantified where possible — a BMC without financial grounding is strategic speculation
- The nine blocks are internally consistent — Customer Segments match Channels match Customer Relationships; the canvas should read as a coherent business story

**Common mistakes:**
- Completing the BMC as a standalone exercise without connecting it to the Business Architecture capability model — the BMC describes *what* the business does; the capability model describes *how* it is organised to do it
- Using the BMC for Assessment-only engagements without populating the current state — a target-only BMC has no baseline to measure gaps against
- Leaving Revenue Streams and Cost Structure blank — these are often the most contested sections and the most important for investment decisions

**TOGAF reference:** TOGAF 10 Phase B — the Business Model Canvas is a complementary tool to the Business Architecture; it is not a TOGAF-mandated artifact but provides the business model foundation that the Phase B capability model and operating model build upon.

</details>

# Business Model Canvas

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of the business model and how the architecture engagement supports or transforms it.
Diagram: Business Model Canvas visual
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## 1. Customer Segments

<details>
<summary>📋 Guidance</summary>

Who are the organisation's most important customers?
Segment customers into groups with distinct needs, behaviours, or characteristics.
Examples of segment types: Mass market, Niche market, Segmented, Diversified, Multi-sided platform.
List each segment on a separate line. Add a brief descriptor (size, need, or characteristic).

</details>

{{customer_segments}}

---

## 2. Value Propositions

<details>
<summary>📋 Guidance</summary>

What value does the organisation deliver to each customer segment?
A value proposition solves a customer problem or satisfies a customer need.
Map each value proposition to the segment(s) it serves.
Examples: newness, performance, customisation, price, risk reduction, accessibility, convenience.

</details>

{{value_propositions}}

---

## 3. Channels

<details>
<summary>📋 Guidance</summary>

Through which channels does the organisation reach its Customer Segments to deliver the
Value Proposition?
Include both communication channels (how you make customers aware) and distribution channels
(how the product or service is delivered).
Map channels to the segments they serve where relevant.

</details>

{{channels}}

---

## 4. Customer Relationships

<details>
<summary>📋 Guidance</summary>

What type of relationship does the organisation have with each Customer Segment?
Examples: Personal assistance, Dedicated personal assistance, Self-service, Automated services,
Communities, Co-creation.
Describe the relationship objective (acquire, retain, upsell) and the mechanism used.

</details>

{{customer_relationships}}

---

## 5. Revenue Streams

<details>
<summary>📋 Guidance</summary>

For what value are customers willing to pay, and how do they pay?
List all revenue streams. For each, note the pricing mechanism:
Fixed pricing (list price, product-feature dependent, customer-segment dependent, volume-based)
or Dynamic pricing (negotiation, yield management, real-time market, auction).
Include any relevant revenue volume or proportion where known.

</details>

{{revenue_streams}}

---

## 6. Key Resources

<details>
<summary>📋 Guidance</summary>

What key resources does the Value Proposition require?
Resources can be: Physical (facilities, equipment), Intellectual (brand, patents, data, IP),
Human (people, knowledge), Financial (credit lines, cash reserves).
Note which resources are owned vs. leased vs. sourced through partners.

</details>

{{key_resources}}

---

## 7. Key Activities

<details>
<summary>📋 Guidance</summary>

What key activities does the Value Proposition require?
Activities can be: Production (design, manufacture, deliver), Problem solving (consulting,
bespoke services, knowledge work), Platform/network (managing platforms, provisioning, promoting).
Focus on the activities the organisation must perform well to make the model work.

</details>

{{key_activities}}

---

## 8. Key Partnerships

<details>
<summary>📋 Guidance</summary>

Who are the organisation's key partners and suppliers?
Describe the motivation for the partnership:
- Optimisation and economy of scale (outsourcing non-core activities)
- Reduction of risk and uncertainty (joint ventures, alliances)
- Acquisition of particular resources and activities (licensing, strategic alliances)
List each partner and the role they play in the business model.

</details>

{{key_partnerships}}

---

## 9. Cost Structure

<details>
<summary>📋 Guidance</summary>

What are the most important costs inherent in the business model?
Classify the cost structure orientation:
- Cost-driven: lean, low-cost, automated, highly outsourced
- Value-driven: premium value creation, personalised service
Note whether costs are: Fixed costs (remain the same regardless of volume),
Variable costs (vary proportionally with volume), Economies of scale, Economies of scope.

</details>

{{cost_structure}}

---

## 10. Business Model Summary

<details>
<summary>📋 Guidance</summary>

Provide a one-paragraph narrative that ties together the nine blocks into a coherent
description of the business model. This is used in executive presentations and as the
opening context in the Business Architecture document.
Do not populate this with AI-generated content without clearly marking it as a draft.

</details>

{{business_model_summary}}

---

## 11. Linkage to Business Architecture

<details>
<summary>📋 Guidance</summary>

Map the BMC blocks to Business Architecture elements that will be defined in Phase B.
This ensures the Business Architecture is anchored to the actual business model rather than
being an abstract capability exercise disconnected from commercial reality.

</details>

| BMC Block | Business Architecture Element | Notes |
|---|---|---|
| Customer Segments | Business Services, Stakeholder Map | {{segment_arch_link}} |
| Value Propositions | Business Capabilities, Business Services | {{value_prop_arch_link}} |
| Channels | Business Processes, Application Architecture (Phase C) | {{channel_arch_link}} |
| Customer Relationships | Business Processes, Business Services | {{relationship_arch_link}} |
| Revenue Streams | Business Functions, Data Architecture (Phase C) | {{revenue_arch_link}} |
| Key Resources | Key Resources, Technology Architecture (Phase D) | {{resource_arch_link}} |
| Key Activities | Business Capabilities, Business Processes | {{activity_arch_link}} |
| Key Partnerships | Organisation Model, Architecture Contracts (Phase G) | {{partnership_arch_link}} |
| Cost Structure | Business Functions, Architecture Roadmap (Phase E) | {{cost_arch_link}} |

---

## 12. Requirements Addressed

<details>
<summary>📋 Guidance</summary>

List requirements from the Requirements Register that this artifact addresses.

</details>

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

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
