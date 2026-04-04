---
artifact: Architecture Definition Document
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.13
lastModified: {{YYYY-MM-DD}}
taxonomy:
  domain: Cross-cutting
  category: Design
  audience: Architecture
  layer: Target
  sensitivity: Internal
  tags: [add, architecture-definition, cross-phase, phase-a]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>📋 Guidance</summary>

The Architecture Definition Document (ADD) is the primary container for all architecture
descriptions produced across the ADM cycle. It evolves progressively:

- Phase A: skeleton created — structure established, high-level content from Architecture Vision
- Phase B: Business Architecture chapter populated
- Phase C: Data and Application Architecture chapters populated
- Phase D: Technology Architecture chapter populated
- Phase E: refined and internally consistent across all chapters
- Phase F: finalised, approved, and baselined

The ADD does not replace the individual domain architecture artifacts. It provides a
single navigable document that brings the domain artifacts together into a coherent whole,
adding cross-domain alignment sections and the consolidated baseline/target narrative.

Update `relatedArtifacts` in this document's frontmatter as domain artifacts are produced.

</details>

# Architecture Definition Document

**Engagement:** {{engagement_name}}
**Organisation:** {{organisation}}
**Sponsor:** {{sponsor}}
**Date:** {{YYYY-MM-DD}}
**ADD Version:** 0.1 (skeleton)

---

## Document Status

| Chapter | Status | Source Artifact | Last Updated |
|---|---|---|---|
| 1. Scope and Context | ⚠️ Not answered | — | — |
| 2. Architecture Principles | ⚠️ Not answered | [Architecture Principles](../preliminary/architecture-principles.md) | — |
| 3. Business Architecture | ⚠️ Not answered | [Business Architecture](../phase-b/business-architecture.md) | — |
| 4. Data Architecture | ⚠️ Not answered | [Data Architecture](../phase-c-data/data-architecture.md) | — |
| 5. Application Architecture | ⚠️ Not answered | [Application Architecture](../phase-c-app/application-architecture.md) | — |
| 6. Technology Architecture | ⚠️ Not answered | [Technology Architecture](../phase-d/technology-architecture.md) | — |
| 7. Cross-Domain Alignment | ⚠️ Not answered | — | — |
| 8. Baseline Architecture Summary | ⚠️ Not answered | — | — |
| 9. Target Architecture Summary | ⚠️ Not answered | — | — |

---

## 1. Scope and Context

<details>
<summary>📋 Guidance</summary>

Define the scope of this architecture engagement — which business units, systems,
geographies, and architecture domains are in scope. Reference the Statement of Architecture
Work and Architecture Vision for the full context.

</details>

**Architecture scope:** {{scope}}

**Domains in scope:** {{architecture_domains}}

**Reference documents:**
- [Statement of Architecture Work](./statement-of-architecture-work.md)
- [Architecture Vision](./architecture-vision.md)

---

## 2. Architecture Principles

<details>
<summary>📋 Guidance</summary>

Summarise the governing architecture principles. Reference the full Principles Catalogue
rather than restating it here.

</details>

See [Architecture Principles](../preliminary/architecture-principles.md) for the full catalogue.

**Key principles applicable to this engagement:**

{{key_principles_summary}}

---

## 3. Business Architecture

<details>
<summary>📋 Guidance</summary>

Summarise the baseline and target business architecture. Reference the full Business
Architecture artifact for detail. In the skeleton phase, record the high-level intent
from the Architecture Vision.

</details>

**Baseline:** {{business_baseline_summary}}

**Target:** {{business_target_summary}}

**Full detail:** [Business Architecture](../phase-b/business-architecture.md)

---

## 4. Data Architecture

<details>
<summary>📋 Guidance</summary>

Summarise the baseline and target data architecture.

</details>

**Baseline:** {{data_baseline_summary}}

**Target:** {{data_target_summary}}

**Full detail:** [Data Architecture](../phase-c-data/data-architecture.md)

---

## 5. Application Architecture

<details>
<summary>📋 Guidance</summary>

Summarise the baseline and target application architecture.

</details>

**Baseline:** {{application_baseline_summary}}

**Target:** {{application_target_summary}}

**Full detail:** [Application Architecture](../phase-c-app/application-architecture.md)

---

## 6. Technology Architecture

<details>
<summary>📋 Guidance</summary>

Summarise the baseline and target technology architecture.

</details>

**Baseline:** {{technology_baseline_summary}}

**Target:** {{technology_target_summary}}

**Full detail:** [Technology Architecture](../phase-d/technology-architecture.md)

---

## 7. Cross-Domain Alignment

<details>
<summary>📋 Guidance</summary>

Identify and document points where domain architectures interact, depend on each other,
or must be kept consistent. This section is the value-add of the ADD over individual domain
artifacts — it is where cross-cutting dependencies and conflicts are surfaced and resolved.

</details>

| Interaction | Domains | Description | Resolution |
|---|---|---|---|
| {{interaction}} | Business ↔ Data | {{description}} | {{resolution}} |

---

## 8. Baseline Architecture Summary

<details>
<summary>📋 Guidance</summary>

A cross-domain summary of the current-state architecture. Derived from the baseline
sections of the domain architecture artifacts.

</details>

{{baseline_summary}}

---

## 9. Target Architecture Summary

<details>
<summary>📋 Guidance</summary>

A cross-domain summary of the target architecture. Derived from the target sections
of the domain architecture artifacts and validated against the Architecture Vision.

</details>

{{target_summary}}

---

## Appendix A3 — Decision Log

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |

---

*This document was created using the EA Assistant plugin.*
