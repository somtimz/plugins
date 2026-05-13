---
artifact: Architecture Policies Register
artifactId: policies-register
engagement: {{engagement_name}}
phase: All
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.5
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Register
  audience: All
  layer: Reference
  sensitivity: Internal
  tags: [policies, traceability, governance]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-POL | ⚠️ Pending | Title and Type columns present |
| T3-POL-AUTHORITY | ⚠️ Pending | Every Enacted policy has a named Issuing Authority |
| T3-POL-REVIEW | ⚠️ Pending | Every Active policy has a Review Cycle |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

The Architecture Policies Register captures all formal governance documents and mandates that authorise constraints for this engagement.

Policies are distinct from principles (internal decision filters), constraints (binding restrictions), and requirements (verifiable outcomes). Every policy must have:
  - an **Issuing Authority** (who enacted it)
  - an **Effective Date** (when it became binding)
  - a **Review Cycle** (when it expires or is reassessed)

Policies are grouped by Type: Security, Procurement, Data Governance, Technology, Compliance, HR, Operational.

**Scope:**
  - Enterprise 🔒: organisation-wide policies enacted by board, regulator, or enterprise governance. Content fields (title, type, authority, statement) are read-only — only status, linked constraints, review cycle, and document reference may be updated locally.
  - Divisional / Geographic: policies enacted by divisional or regional authorities. Fully editable.

**Traceability:**
  - Every policy should generate at least one CST-NNN constraint. A policy with no linked constraints is an orphan — it has not been operationalised into architecture rules.
  - Every CST-NNN should ideally trace to a POL-NNN. Constraints with free-text Source values are traceability gaps.
  - Use `/ea-policies trace` to verify policy-to-constraint linkage.
  - Use `/ea-policies impact` to assess which capabilities or work packages are bounded by a policy's derived constraints.

**⚠️ Stale policy check:** Policies with Review Cycle past due may invalidate linked constraints. Run `/ea-policies list` to flag stale policies.

**⚠️ Two Layers check:** Distinguish `Business Policies` (what the business must comply with, e.g. "GDPR Data Protection Policy") from `Architecture Policies` (how the EA function governs solution design, e.g. "Cloud-First Technology Policy"). Both belong in the Policies Register; the distinction is in Type and Issuing Authority.

</details>

# Architecture Policies Register

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Last Synced from Repo:** {{last_sync_date}}
**Version:** {{version}}

---

## Executive Summary

<details>
<summary>📋 Guidance</summary>

Summary of the policy landscape: total count, type distribution, and key enterprise policies driving this engagement.
Diagram: Policies summary chart (count by type/scope)
Run `/ea-summary refresh` to regenerate this section from current artifact content.

</details>

{{executive_summary}}

---

## Policies Summary

| Total | Enterprise 🔒 | Divisional | Geographic | Enacted | Under Review | Draft | Retired | Stale | Orphan |
|---|---|---|---|---|---|---|---|---|---|
| {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} | {{N}} |

---

## Security Policies

| POL-NNN | Title | Issuing Authority | Effective Date | Review Cycle | Scope | Status | Linked Constraints |
|---|---|---|---|---|---|---|---|
| POL-001 | {{title}} | {{authority}} | {{date}} | {{review}} | {{scope}} | {{status}} | {{constraints}} |

---

## Procurement Policies

| POL-NNN | Title | Issuing Authority | Effective Date | Review Cycle | Scope | Status | Linked Constraints |
|---|---|---|---|---|---|---|---|
| POL-001 | {{title}} | {{authority}} | {{date}} | {{review}} | {{scope}} | {{status}} | {{constraints}} |

---

## Data Governance Policies

| POL-NNN | Title | Issuing Authority | Effective Date | Review Cycle | Scope | Status | Linked Constraints |
|---|---|---|---|---|---|---|---|
| POL-001 | {{title}} | {{authority}} | {{date}} | {{review}} | {{scope}} | {{status}} | {{constraints}} |

---

## Technology Policies

| POL-NNN | Title | Issuing Authority | Effective Date | Review Cycle | Scope | Status | Linked Constraints |
|---|---|---|---|---|---|---|---|
| POL-001 | {{title}} | {{authority}} | {{date}} | {{review}} | {{scope}} | {{status}} | {{constraints}} |

---

## Compliance Policies

| POL-NNN | Title | Issuing Authority | Effective Date | Review Cycle | Scope | Status | Linked Constraints |
|---|---|---|---|---|---|---|---|
| POL-001 | {{title}} | {{authority}} | {{date}} | {{review}} | {{scope}} | {{status}} | {{constraints}} |

---

## HR Policies

| POL-NNN | Title | Issuing Authority | Effective Date | Review Cycle | Scope | Status | Linked Constraints |
|---|---|---|---|---|---|---|---|
| POL-001 | {{title}} | {{authority}} | {{date}} | {{review}} | {{scope}} | {{status}} | {{constraints}} |

---

## Operational Policies

| POL-NNN | Title | Issuing Authority | Effective Date | Review Cycle | Scope | Status | Linked Constraints |
|---|---|---|---|---|---|---|---|
| POL-001 | {{title}} | {{authority}} | {{date}} | {{review}} | {{scope}} | {{status}} | {{constraints}} |

---

## Orphan Policies

⚠️ The following policies have no linked constraints:

| POL-NNN | Title | Type | Issuing Authority | Action |
|---|---|---|---|---|
| POL-NNN | {{title}} | {{type}} | {{authority}} | Link to CST-NNN or document why no constraint is needed |

---

## Stale Policies

⚠️ The following policies have Review Cycle past due:

| POL-NNN | Title | Review Cycle | Status | Action |
|---|---|---|---|---|
| POL-NNN | {{title}} | {{review}} | {{status}} | Update status to Under Review or extend Review Cycle |

---

## Appendix A3 — Decision Log

| # | Decision | Rationale | Authority | Date | Verified |
|---|---|---|---|---|---|
| 1 | | | | | |

---

## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status |
|---|---|---|
| | | |
