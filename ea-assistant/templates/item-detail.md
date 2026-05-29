---
artifact: Item Detail
phase: All
taxonomy: cross-cutting
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
engagement: "{{engagement_name}}"
item: "{{ID}}"
type: "{{item_type}}"
title: "{{item_title}}"
parentArtifact: "{{parent_artifact_path}}"
created: "{{YYYY-MM-DD}}"
lastModified: "{{YYYY-MM-DD}}"
relatedItems: "{{related_items}}"
relatedArtifacts: []
diagrams: []
links: []
---

<!-- GUIDANCE:
  This is a detail file for a single engagement item (e.g. G-001, CAP-003, WP-007).
  It lives at artifacts/details/{ID}.md and is linked from a table row in the parent artifact.
  Fill in the sections that are relevant — not all sections apply to every item type.
  Sections left as placeholders will remain as-is; they do not block the engagement.
  Use /ea-detail view {ID} to open and /ea-detail new {ID} to create for a new item.

  Item-type guidance:
  - For CAP-NNN: include capability maturity rationale and value stream coverage (which VS-NNN exercises this capability).
  - For VS-NNN: include trigger-to-outcome flow and capability exercise map (which CAP-NNN are exercised at each step).
  - For UC-NNN: include actor analysis, process consumption trace, and requirement generation trace (which REQ-NNN were generated).
-->

# {{ID}}: {{item_title}}

**Type:** {{item_type}}
**Parent Artifact:** [{{parent_artifact_name}}](../{{parent_artifact_path}})
**Last Updated:** {{YYYY-MM-DD}}

---

## Notes

<!-- GUIDANCE: Inline notes and flags for this item.
     Add via /ea-note --detail {ID} or n: during sessions.
     Resolve via /ea-detail note resolve {ID}. -->

---

## Related Items

<!-- GUIDANCE: Cross-links to related detail files.
     Auto-populated from the parent artifact table row on creation.
     Managed via /ea-detail link {ID1} {ID2}.
     The relatedItems frontmatter field is the source of truth; this table is derived from it. -->

| ID | Type | Title | Relationship |
|---|---|---|---|
{{related_items_table}}

---

## Summary

<!-- GUIDANCE: 1–2 sentences. What is this item and why does it exist? -->

{{item_summary}}

---

## Narrative

<!-- GUIDANCE:
  The backstory. Where did this item come from? What context is needed to understand it fully?
  Include business context, history, organisational pressures, or stakeholder background.
-->

{{narrative}}

---

## Rationale

<!-- GUIDANCE:
  Why was this item defined this way? What decisions were made in arriving at this formulation?
  Reference A3 decision rows or ADR-NNN entries where applicable.
-->

{{rationale}}

---

## Risks

<!-- GUIDANCE:
  Risks specifically associated with this item — not the engagement-wide risk register.
  What could go wrong if this item is wrong, incomplete, or not delivered?
  Flag critical risks for promotion to the Risk Register via /ea-risks.
-->

{{risks}}

---

## Costs

<!-- GUIDANCE:
  Cost implications of this item — budget, resource, time, or opportunity cost.
  Include estimates where known; use High / Medium / Low if no figures are available.
-->

{{costs}}

---

## Issues

<!-- GUIDANCE:
  Known issues that affect or are caused by this item.
  Link to ISS-NNN entries in the parent artifact where applicable.
-->

{{issues}}

---

## Concerns

<!-- GUIDANCE:
  Stakeholder concerns raised about this item.
  Link to CON-NNN entries from Appendix A4 of the parent artifact where applicable.
-->

{{concerns}}

---

## Impact

<!-- GUIDANCE:
  What does this item affect? Other architecture items, capabilities, timelines, or stakeholders.
  Include both positive impact (what this item enables) and negative impact (what it constrains).
  Reference dependent IDs (OBJ-NNN, WP-NNN, GAP-NNN, etc.) where applicable.
-->

{{impact}}

---

## Alternatives

<!-- GUIDANCE:
  What alternatives were considered and why were they not chosen?
  Use the same format as A3.N rationale blocks for consistency.
  If no alternatives were formally considered, record that explicitly.
-->

{{alternatives}}

---

*Detail file for {{ID}} · Engagement: {{engagement_name}} · Use `/ea-detail view {{ID}}` to open.*
