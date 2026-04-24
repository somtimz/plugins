---
artifact: Role Catalogue
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.27
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: Governance
  layer: Reference
  sensitivity: Confidential
  tags: [roles, raci, governance, stakeholders, calendar, triggers]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>📋 Guidance</summary>

The Role Catalogue maps every role active in this engagement to a named individual, organisation, and RACI position. It supplements the Stakeholder Map (which tracks interests and influence) with governance-focused role assignments, triggering events, and meeting cadence.

Role IDs (ROLE-NNN) refer to the canonical definitions in `skills/ea-engagement-lifecycle/references/role-catalogue.md`. Remove rows for roles not active in this engagement. Add a RACI Override only when this engagement's governance structure differs from the canonical default.

</details>

# Role Catalogue

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Date:** {{YYYY-MM-DD}}

---

## Active Roles

<details>
<summary>📋 Guidance</summary>

List all roles active in this engagement. Assign a named individual and their organisation unit. Use the RACI Override column only when the engagement-specific RACI differs from the canonical default in `role-catalogue.md`. Leave blank if the default applies.

Remove unused role rows. If a role is shared across multiple individuals (e.g., multiple Application Owners), duplicate the row and append a domain qualifier in the Notes column (e.g., "CRM domain").

</details>

| Role ID | Role | Named Individual | Organisation Unit | RACI Override | Notes |
|---------|------|-----------------|-------------------|---------------|-------|
| ROLE-001 | Stakeholder | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-002 | Stakeholder Agent | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-003 | Subject Matter Expert (SME) | ⚠️ Not answered | ⚠️ Not answered | — | Multiple SMEs may be listed |
| ROLE-004 | Auditor | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-005 | Implementer | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-006 | Enterprise Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-007 | Business Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-008 | Data Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-009 | Application Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-010 | Technology Architect | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-011 | Business Analyst | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-012 | Delivery Lead | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-013 | Project Manager | ⚠️ Not answered | ⚠️ Not answered | — | |
| ROLE-014 | Data Owner | ⚠️ Not answered | ⚠️ Not answered | — | Specify data domain in Notes |
| ROLE-015 | Application Owner | ⚠️ Not answered | ⚠️ Not answered | — | Specify application in Notes |

---

## Triggering Events Summary

<details>
<summary>📋 Guidance</summary>

List the key events that activate role involvement in this engagement. Map each trigger to the roles it activates and the action required. Add engagement-specific triggers as needed.

</details>

| Trigger | Roles Activated | Action Required |
|---------|----------------|-----------------|
| New engagement initiated | ROLE-006, ROLE-013, ROLE-011 | Kick off interviews, schedule sessions, produce SAoW |
| Phase gate reached | ROLE-001, ROLE-006, ROLE-004 | Architecture review, compliance check, phase sign-off |
| Architecture Vision presented | ROLE-001, ROLE-002, ROLE-006 | Stakeholder review and approval |
| Architecture Contract raised | ROLE-001, ROLE-012, ROLE-006 | Review, negotiate, and sign |
| ACR raised (standard) | ROLE-006, ROLE-004, ROLE-001 | Impact assessment, governance decision, update Change Register |
| ACR raised (waiver required) | ROLE-001, ROLE-006, ROLE-004 | Waiver approval via IGP §6 process |
| Delivery gate approaching | ROLE-012, ROLE-004, ROLE-005 | Prepare compliance evidence, conduct gate review |
| Non-conformance identified | ROLE-004, ROLE-006, ROLE-005 | Raise non-conformance, agree remediation, track to closure |
| Data Architecture phase initiated | ROLE-008, ROLE-014, ROLE-003 | Data Architecture interviews, data model validation |
| Application Architecture phase initiated | ROLE-009, ROLE-015, ROLE-003 | Application Architecture interviews, portfolio review |
| ⚠️ Not answered | ⚠️ Not answered | ⚠️ Not answered |

---

## Engagement Calendar

<details>
<summary>📋 Guidance</summary>

Define the recurring meetings and governance activities for this engagement. Assign the roles expected to attend each. Add or remove rows to match the engagement's governance structure.

</details>

| Cadence | Meeting / Activity | Roles Present | Notes |
|---------|-------------------|---------------|-------|
| Weekly | Architecture Working Group | ROLE-006, ROLE-007, ROLE-008, ROLE-009, ROLE-010, ROLE-011 | Core architecture team |
| Weekly | Delivery Status Review | ROLE-012, ROLE-005, ROLE-006 | Phase G onwards |
| Fortnightly | Stakeholder Briefing | ROLE-001, ROLE-002, ROLE-006 | Progress update and decisions |
| Monthly | Steering Committee | ROLE-001, ROLE-006, ROLE-013 | Governance and escalations |
| Per phase | Phase Gate Review | ROLE-001, ROLE-004, ROLE-006, ROLE-012 | Phase sign-off |
| Per work package | Delivery Gate Review | ROLE-004, ROLE-005, ROLE-012 | Compliance assessment |
| Per ADR | ADR Review | ROLE-006, relevant Domain Architect, ROLE-001 | Decision capture |
| As needed | Emergency ACR Review | ROLE-001, ROLE-006, ROLE-004 | Waiver or dispensation |
| ⚠️ Not answered | ⚠️ Not answered | ⚠️ Not answered | |

---

## Escalation Paths

<details>
<summary>📋 Guidance</summary>

Summarise the escalation structure for this engagement. Confirm or override the canonical paths from `role-catalogue.md` based on the engagement's organisational context.

</details>

| Role | Escalates To | Receives From |
|------|-------------|---------------|
| ROLE-001 Stakeholder | Board / C-suite | Enterprise Architect (ROLE-006), Delivery Lead (ROLE-012) |
| ROLE-006 Enterprise Architect | Stakeholder (ROLE-001) | All Domain Architects, Business Analyst, Delivery Lead, Auditor |
| ROLE-012 Delivery Lead | Stakeholder (ROLE-001), Enterprise Architect (ROLE-006) | Implementer (ROLE-005) |
| ROLE-004 Auditor | Enterprise Architect (ROLE-006) | Implementer (ROLE-005), Delivery Lead (ROLE-012) |
| ROLE-011 Business Analyst | Enterprise Architect (ROLE-006), Delivery Lead (ROLE-012) | Stakeholder (ROLE-001), SMEs (ROLE-003) |
| ROLE-014 Data Owner | Data Architect (ROLE-008), Stakeholder (ROLE-001) | Data Architect (ROLE-008) |
| ROLE-015 Application Owner | Application Architect (ROLE-009), Stakeholder (ROLE-001) | Application Architect (ROLE-009) |

---

## Appendix A3 — Decision Log

| ID | Decision | State | Authority | Domain | Cost | Impact | Risk | Subject | Owner | Date |
|----|----------|-------|-----------|--------|------|--------|------|---------|-------|------|
| — | | | | | | | | | | |

---

## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status | Relevance |
|--------|-------|--------|-----------|
| — | | | |
