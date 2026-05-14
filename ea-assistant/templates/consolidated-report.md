---
artifact: Consolidated Architecture Document
engagement: {{engagement_name}}
date: {{YYYY-MM-DD}}
version: {{version}}
templateVersion: 0.9.5
status: {{document_status}}
taxonomy:
  domain: Cross-cutting
  category: Planning
  audience: Executive
  layer: Reference
  sensitivity: Internal
  tags: [summary, executive, portfolio, cross-cutting]
relatedArtifacts: []
diagrams: []
links: []
---
<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Cross-artifact consistency verified | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** A publication-ready consolidated view of the engagement's architecture artifacts, assembled for external distribution (stakeholders, governance boards, client delivery). This document is a snapshot — it reflects the state of the source artifacts at publication time and is not a primary authoring surface.

**What to include:** Only artifacts that are in `Approved` or `Review` status should be included in a published consolidated report; `Draft` artifacts may be included with an explicit caveat. The artifact selection should be agreed with the engagement sponsor before `/ea-publish` is run. Include only the artifacts relevant to the publication audience — an executive briefing does not include all technical artifacts.

**Quality indicators:**
- The Artifact Status Summary table is complete and current — every included artifact is listed with its status and last-modified date
- The ⚠️ draft warning banner is present if any included artifact is not `Approved`
- Source artifacts have been refreshed from their current state before publication — stale content is the primary risk with consolidated reports

**Common mistakes:**
- Editing the consolidated report directly — changes will be overwritten on the next `/ea-publish` run; all changes must be made in source artifacts first
- Publishing a report with `Draft` artifacts without the warning banner — this misrepresents the governance status to external stakeholders
- Including all artifacts regardless of audience — tailor the artifact selection to the publication audience and purpose

**TOGAF reference:** TOGAF 10 §19 — the Consolidated Architecture Document corresponds to the ADM's concept of an Architecture Repository view, assembled for stakeholder consumption at phase gates or governance reviews.

</details>

# {{engagement_name}} — Architecture Document

| Field           | Value                    |
|-----------------|--------------------------|
| **Engagement**  | {{engagement_name}}      |
| **Organisation**| {{organisation}}         |
| **Sponsor**     | {{sponsor}}              |
| **Version**     | {{version}}              |
| **Published**   | {{YYYY-MM-DD}}           |
| **Document Status** | {{document_status}}  |
| **Scope**       | {{n}} of {{m}} artifacts |

---

## Artifact Status Summary

| # | Artifact | Phase | Status | Last Modified |
|---|----------|-------|--------|---------------|
| {{n}} | {{artifact_name}} | {{phase}} | {{status_badge}} | {{last_modified}} |

<!-- Repeat row per included artifact -->

<!-- If any artifact is not Approved, include the following warning: -->
> ⚠️ This document contains sections that have not been approved. Review each section's status header before distributing.

---

## Table of Contents

<!-- List only included artifacts in ADM order -->
1. {{artifact_name}}

---

<!-- ═══════════════════════════════════════════════════════
     ARTIFACT SECTIONS — one block per included artifact
     ═══════════════════════════════════════════════════════ -->

---

## {{artifact_name}}

> **Phase {{phase}}  ·  {{status_badge}}  ·  Last modified: {{last_modified}}**

{{artifact_content}}

<!-- If open review comments exist, append: -->
### Open Review Comments

{{review_comments}}

---

<!-- Repeat section block per included artifact in ADM order -->

---

## Appendices

### A. Source Documents

| Document | Date | Location |
|----------|------|----------|
| {{document}} | {{date}} | `uploads/{{filename}}` |

---

*Published by EA Assistant on {{generation_date}}*

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
