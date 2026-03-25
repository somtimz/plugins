---
artifact: Business Model Canvas
engagement: {{engagement_name}}
phase: B
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Business Model Canvas (BMC) describes how the organisation creates, delivers, and captures
  value. It is used in Phase B to ground the Business Architecture in the actual operating model
  of the business — before layering in capabilities, processes, and services.

  Use the BMC when the engagement involves significant business model change (Greenfield,
  Brownfield transformation), or when the current business model needs to be baselined before
  identifying gaps. For Assessment-only engagements, the BMC documents the current state.

  The nine building blocks form a coherent whole — changes to one block typically affect others.
  Draw out dependencies as you populate the canvas (e.g., which Key Resources support which
  Value Propositions; which Channels serve which Customer Segments).

  Based on the Business Model Canvas by Osterwalder & Pigneur (strategyzer.com).
-->

# Business Model Canvas

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## 1. Customer Segments

<!-- GUIDANCE:
  Who are the organisation's most important customers?
  Segment customers into groups with distinct needs, behaviours, or characteristics.
  Examples of segment types: Mass market, Niche market, Segmented, Diversified, Multi-sided platform.
  List each segment on a separate line. Add a brief descriptor (size, need, or characteristic).
-->

{{customer_segments}}

---

## 2. Value Propositions

<!-- GUIDANCE:
  What value does the organisation deliver to each customer segment?
  A value proposition solves a customer problem or satisfies a customer need.
  Map each value proposition to the segment(s) it serves.
  Examples: newness, performance, customisation, price, risk reduction, accessibility, convenience.
-->

{{value_propositions}}

---

## 3. Channels

<!-- GUIDANCE:
  Through which channels does the organisation reach its Customer Segments to deliver the
  Value Proposition?
  Include both communication channels (how you make customers aware) and distribution channels
  (how the product or service is delivered).
  Map channels to the segments they serve where relevant.
-->

{{channels}}

---

## 4. Customer Relationships

<!-- GUIDANCE:
  What type of relationship does the organisation have with each Customer Segment?
  Examples: Personal assistance, Dedicated personal assistance, Self-service, Automated services,
  Communities, Co-creation.
  Describe the relationship objective (acquire, retain, upsell) and the mechanism used.
-->

{{customer_relationships}}

---

## 5. Revenue Streams

<!-- GUIDANCE:
  For what value are customers willing to pay, and how do they pay?
  List all revenue streams. For each, note the pricing mechanism:
  Fixed pricing (list price, product-feature dependent, customer-segment dependent, volume-based)
  or Dynamic pricing (negotiation, yield management, real-time market, auction).
  Include any relevant revenue volume or proportion where known.
-->

{{revenue_streams}}

---

## 6. Key Resources

<!-- GUIDANCE:
  What key resources does the Value Proposition require?
  Resources can be: Physical (facilities, equipment), Intellectual (brand, patents, data, IP),
  Human (people, knowledge), Financial (credit lines, cash reserves).
  Note which resources are owned vs. leased vs. sourced through partners.
-->

{{key_resources}}

---

## 7. Key Activities

<!-- GUIDANCE:
  What key activities does the Value Proposition require?
  Activities can be: Production (design, manufacture, deliver), Problem solving (consulting,
  bespoke services, knowledge work), Platform/network (managing platforms, provisioning, promoting).
  Focus on the activities the organisation must perform well to make the model work.
-->

{{key_activities}}

---

## 8. Key Partnerships

<!-- GUIDANCE:
  Who are the organisation's key partners and suppliers?
  Describe the motivation for the partnership:
  - Optimisation and economy of scale (outsourcing non-core activities)
  - Reduction of risk and uncertainty (joint ventures, alliances)
  - Acquisition of particular resources and activities (licensing, strategic alliances)
  List each partner and the role they play in the business model.
-->

{{key_partnerships}}

---

## 9. Cost Structure

<!-- GUIDANCE:
  What are the most important costs inherent in the business model?
  Classify the cost structure orientation:
  - Cost-driven: lean, low-cost, automated, highly outsourced
  - Value-driven: premium value creation, personalised service
  Note whether costs are: Fixed costs (remain the same regardless of volume),
  Variable costs (vary proportionally with volume), Economies of scale, Economies of scope.
-->

{{cost_structure}}

---

## 10. Business Model Summary

<!-- GUIDANCE:
  Provide a one-paragraph narrative that ties together the nine blocks into a coherent
  description of the business model. This is used in executive presentations and as the
  opening context in the Business Architecture document.
  Do not populate this with AI-generated content without clearly marking it as a draft.
-->

{{business_model_summary}}

---

## 11. Linkage to Business Architecture

<!-- GUIDANCE:
  Map the BMC blocks to Business Architecture elements that will be defined in Phase B.
  This ensures the Business Architecture is anchored to the actual business model rather than
  being an abstract capability exercise disconnected from commercial reality.
-->

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

<!-- GUIDANCE:
  List requirements from the Requirements Register that this artifact addresses.
-->

| Req ID | Requirement | How Addressed |
|---|---|---|
| {{req_id}} | {{requirement}} | {{how}} |

---

*This document was created using the EA Assistant plugin.*
