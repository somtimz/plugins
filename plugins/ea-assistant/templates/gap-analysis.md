---
artifact: Gap Analysis
engagement: {{engagement_name}}
phase: {{phase}}
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  Gap Analysis documents the differences between the Baseline (current) and Target architectures.
  A separate Gap Analysis is typically produced for each architecture domain (B, C-Data, C-App, D).
  Gaps feed directly into the Architecture Roadmap in Phase E.
-->

# Gap Analysis — {{domain}} Architecture

**Engagement:** {{engagement_name}}
**Domain:** {{domain}} (Business / Data / Application / Technology)
**Date:** {{YYYY-MM-DD}}

---

## Baseline Architecture Summary

<!-- GUIDANCE:
  Brief description of the current state architecture for this domain.
  Reference the relevant baseline artifact if it exists.
-->

{{baseline_summary}}

---

## Target Architecture Summary

<!-- GUIDANCE:
  Brief description of the target state architecture for this domain.
  Reference the target architecture document.
-->

{{target_summary}}

---

## Gap Register

<!-- GUIDANCE:
  List each gap between baseline and target.
  Categories: Missing capability, Retiring component, Consolidation, New requirement, Enhancement
-->

| Gap ID | Description | Category | Priority | Baseline State | Target State | Effort |
|---|---|---|---|---|---|---|
| GAP-001 | {{description}} | Missing capability | High/Med/Low | {{baseline}} | {{target}} | High/Med/Low |

---

## Zachman Coverage Analysis

<!-- GUIDANCE:
  Assess Zachman cell coverage for this domain. Identify which cells have gaps.
-->

| | What (Data) | How (Function) | Where (Network) | Who (People) | When (Time) | Why (Motivation) |
|---|---|---|---|---|---|---|
| **Executive** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **Business** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **Architect** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| **Engineer** | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

Legend: ✅ Covered | ⚠️ Partial | ⬜ Gap

---

## Recommended Actions

| Gap ID | Recommended Action | Phase | Owner |
|---|---|---|---|
| GAP-001 | {{action}} | E / F | {{owner}} |

---

*This document was created using the EA Assistant plugin.*
