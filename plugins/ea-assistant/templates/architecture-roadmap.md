---
artifact: Architecture Roadmap
engagement: {{engagement_name}}
phase: E/F
status: Draft
reviewStatus: Not Reviewed
version: 0.1
lastModified: {{YYYY-MM-DD}}
---

<!-- GUIDANCE:
  The Architecture Roadmap lists individual work packages in priority order that together
  deliver the Target Architecture. It evolves from Phase E (initial) through Phase F (refined)
  and is updated in Phase H as change requests are processed.
-->

# Architecture Roadmap

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}
**Horizon:** {{time_horizon}}

---

## Roadmap Overview

<!-- GUIDANCE:
  Provide a high-level timeline view. Reference a diagram if available.
-->

*Reference diagram:* `../diagrams/{{roadmap_diagram}}`

---

## Work Packages

<!-- GUIDANCE:
  Each work package is a discrete unit of change that can be planned and resourced.
  Work packages close gaps identified in the Gap Analysis.
-->

### WP-001: {{work_package_name}}

| Field | Value |
|---|---|
| **ID** | WP-001 |
| **Description** | {{description}} |
| **Closes Gaps** | {{gap_ids}} |
| **Addresses Requirements** | {{req_ids}} |
| **Phase / Wave** | Wave 1 / Wave 2 / Wave 3 |
| **Estimated Effort** | {{effort}} |
| **Dependencies** | {{dependencies}} |
| **Owner** | {{owner}} |
| **Status** | Proposed / Approved / In Progress / Complete |

---

## Transition Architectures

<!-- GUIDANCE:
  Define the intermediate states (plateaus) between baseline and target.
  Each plateau should be a stable, usable architecture state.
-->

| Plateau | Description | Target Date | Work Packages |
|---|---|---|---|
| Plateau 1 | {{description}} | {{date}} | WP-001, WP-002 |
| Plateau 2 | {{description}} | {{date}} | WP-003 |
| Target | {{target_description}} | {{date}} | All |

---

## Prioritisation

<!-- GUIDANCE:
  Explain the prioritisation criteria used to sequence work packages.
-->

{{prioritisation_rationale}}

---

*This document was created using the EA Assistant plugin.*
