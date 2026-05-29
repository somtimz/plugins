---
artifactId: architecture-definition-document
artifact: Architecture Definition Document
engagement: {{engagement_name}}
phase: A
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.55
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
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| T3-A3 | ⚠️ Pending | |
| T3-A4 | ⚠️ Pending | |
| T3-ADR | ⚠️ Pending | |
| T3-RATIONALE | ⚠️ Pending | |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

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

## Executive Summary

<details>
<summary>📋 Guidance</summary>

**Purpose:** A decision-maker-level summary of what changed architecturally, why, and what the key cross-domain decisions were. This section is the primary entry point for sponsors, governance boards, and stakeholders who do not read the full document.

**What to include:** A brief narrative covering (a) the scope and intent of this engagement, (b) the key differences between baseline and target across all domains, (c) the two or three most significant architecture decisions, and (d) a note on critical risks or open issues. Include or reference the multi-domain overview diagram.

**Quality indicators:**
- A reader with no prior context can understand what changed and why after reading this section alone
- Key decisions reference ADR IDs (e.g. "The choice to adopt an API-first integration layer — see ADR-007 — eliminates the direct database coupling that created the current data quality issues")
- Baseline and target are compared concretely — not "the target is more modern" but "the monolith is decomposed into 4 bounded services with independent release pipelines"

**Common mistakes:**
- Restating what the ADD contains rather than what the architecture decided (a table of contents is not a summary)
- Omitting the baseline — readers need to understand what is changing *from*, not just what the target is
- Writing this section before the domain chapters are complete; use `/ea-summary refresh` to regenerate from populated content

**TOGAF reference:** TOGAF 10 §24 — the ADD Executive Summary corresponds to the Architecture Vision summary but at the detailed, post-analysis level, not the aspirational Phase A level.

</details>

{{executive_summary}}

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

**Purpose:** Establishes the bounded scope of this engagement so that every reader understands what the architecture covers and, critically, what it does not cover. Scope ambiguity is the most common cause of stakeholder misalignment at Phase G reviews.

**What to include:** Business units or organisational divisions in scope; systems and applications in scope (name them); geographies or legal entities if relevant; architecture domains active for this engagement (not all engagements span all four TOGAF domains); explicit out-of-scope exclusions. Reference the Statement of Architecture Work for the ratified scope statement.

**Quality indicators:**
- Out-of-scope items are explicitly listed — "out of scope: retail channel, legacy mainframe batch processes" is better than silence
- Domain scope is specified — "this engagement covers Business and Application architecture only; Data and Technology domains will be addressed in the Phase C extension"
- The scope statement matches the ratified SAoW; deviations are noted with justification

**Common mistakes:**
- Repeating the Architecture Vision scope verbatim without noting any changes or refinements since Phase A
- Vague scope like "the enterprise" — name the specific units, systems, and geographies
- Missing explicit out-of-scope list, which allows scope creep to go unnoticed

**TOGAF reference:** TOGAF 10 §24.3 — Scope and Context corresponds to the ADD's initial delimitation of the engagement boundary, derived from the SAoW (§23).

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

**Purpose:** Surfaces the active constraints on every architecture decision in this engagement. This section is read by reviewers at ADR time — they check whether a proposed decision is compatible with the governing principles before approving it.

**What to include:** The subset of principles from the Architecture Principles register that are actively applicable to this engagement's scope and domains. Do not restate the full register — link to it and call out the 3–5 principles most likely to be invoked during design reviews. Note any principles that were waived for this engagement, with the authority that granted the waiver.

**Quality indicators:**
- The selected principles are genuinely constraining — a reader could use them to challenge a technology choice or design decision
- Waivers are documented with a reference to the A3 decision or governance body that approved them
- The link to the full Principles register is accurate and resolves to the correct artifact

**Common mistakes:**
- Restating all principles verbatim — this bloats the ADD and duplicates the register; summarise and link instead
- Selecting principles that are too abstract to use as review criteria ("all architecture must be high quality")
- Omitting waivers — if a principle was suspended for this engagement, the ADD must record it

**TOGAF reference:** TOGAF 10 §3 — Architecture Principles are established in the Preliminary phase; the ADD references the active subset in context, not as a primary catalogue.

</details>

See [Architecture Principles](../preliminary/architecture-principles.md) for the full catalogue.

**Key principles applicable to this engagement:**

{{key_principles_summary}}

---

## 3. Business Architecture

<details>
<summary>📋 Guidance</summary>

**Purpose:** Provides a decision-maker-level snapshot of business architecture changes — what capabilities exist today, what the target operating model looks like, and what the critical business gaps are. This chapter is where business sponsors confirm the ADD reflects their intended outcomes.

**What to include:** Baseline: current key capabilities (named, not generic), operating model structure, and the 2–3 most significant business pain points. Target: the capability additions or restructuring, the intended operating model changes, and the business outcomes delivered. Reference the full Business Architecture artifact for the detail; this chapter is a synthesis.

**Quality indicators:**
- Baseline and target are compared in concrete terms — capability by capability, not "current state is fragmented, target is integrated"
- Business gaps are named and traced to requirements (REQ-NNN) or drivers (DRV-NNN)
- The summary matches the full Business Architecture artifact — if they diverge, the ADD is stale

**Common mistakes:**
- Describing IT systems in the Business Architecture chapter — this chapter covers capabilities and operating model, not systems (those belong in §5 Application Architecture)
- Placeholder content like "Business Architecture to be populated in Phase B" with no update after Phase B completes
- Omitting the baseline — the target architecture only makes sense in contrast to what exists today

**TOGAF reference:** TOGAF 10 Part III, Phase B — Business Architecture. The ADD §3 is a summary view; the detail lives in the standalone Business Architecture artifact.

</details>

**Baseline:** {{business_baseline_summary}}

**Target:** {{business_target_summary}}

**Full detail:** [Business Architecture](../phase-b/business-architecture.md)

---

## 4. Data Architecture

<details>
<summary>📋 Guidance</summary>

**Purpose:** Summarises what data assets exist, who owns them, and how ownership, quality, and flows change in the target. Data architecture decisions have long lifespans — this chapter records the decisions that will constrain application and technology choices throughout the engagement.

**What to include:** Baseline: key data domains (named), current ownership model, known quality issues, and any regulatory or sovereignty constraints. Target: revised data ownership assignments, new or decommissioned data domains, data sharing patterns, and how quality and lineage requirements are addressed. Reference the full Data Architecture artifact for entity models and lineage diagrams.

**Quality indicators:**
- Data domains are named, not generic ("Customer, Product, Order" not "operational data")
- Ownership changes between baseline and target are explicit — "Ownership of the Customer master moves from CRM to the new MDM platform"
- Regulatory constraints (GDPR, sovereignty) are surfaced here if they affect architecture decisions

**Common mistakes:**
- Describing database technologies or tools in this chapter — those belong in §6 Technology Architecture
- Omitting data ownership changes, which are often the most contentious data architecture decisions
- Leaving the chapter empty because "the data model is in the Data Architecture artifact" — this chapter must provide a useful summary, not just a link

**TOGAF reference:** TOGAF 10 Part III, Phase C (Information Systems Architecture — Data) — the ADD §4 summarises the data layer decisions with a focus on ownership, quality, and flow.

</details>

**Baseline:** {{data_baseline_summary}}

**Target:** {{data_target_summary}}

**Full detail:** [Data Architecture](../phase-c-data/data-architecture.md)

---

## 5. Application Architecture

<details>
<summary>📋 Guidance</summary>

**Purpose:** Records the application landscape changes — which systems are retained, decommissioned, replaced, or newly introduced — and the integration patterns that connect them. Application architecture decisions are the most directly visible to delivery teams, so this chapter must be precise enough to guide solution design.

**What to include:** Baseline: the current application map (named systems, their roles, key integrations, and the coupling or duplication problems that motivate change). Target: the application portfolio changes (what is added, removed, consolidated), the integration pattern choices, and the key quality attribute decisions (e.g. event-driven vs synchronous, API-first, strangler-fig migration pattern).

**Quality indicators:**
- Named systems appear in both baseline and target — it is clear which systems survive, which are retired, and which are new
- Integration pattern choices reference ADRs (e.g. "API gateway pattern — see ADR-012")
- The target application map is consistent with the Technology Architecture chapter (§6) — the same systems appear in both

**Common mistakes:**
- Describing infrastructure (servers, cloud services) in this chapter — those belong in §6 Technology Architecture
- Omitting the integration model — a list of applications with no integration description misses the most common source of architectural risk
- The application list contradicts the full Application Architecture artifact — always reconcile before the ADD is published

**TOGAF reference:** TOGAF 10 Part III, Phase C (Information Systems Architecture — Application) — the ADD §5 is the synthesis view; the full artifact holds the component diagrams and interface specifications.

</details>

**Baseline:** {{application_baseline_summary}}

**Target:** {{application_target_summary}}

**Full detail:** [Application Architecture](../phase-c-app/application-architecture.md)

---

## 6. Technology Architecture

<details>
<summary>📋 Guidance</summary>

**Purpose:** Records the infrastructure, platform, and vendor decisions that underpin the target application architecture. Technology architecture decisions are often the most capital-intensive and hardest to reverse, so this chapter must capture the governance context — not just the choices made, but why they are constrained.

**What to include:** Baseline: current infrastructure landscape (platform, hosting model, key vendors), known technical debt or end-of-life risks. Target: the platform strategy (cloud/hybrid/on-prem), the key infrastructure decisions (SBB-NNN references), vendor selections with rationale, and the decommission plan for baseline components being retired. Security and operational principles that constrain platform choices should be noted here.

**Quality indicators:**
- Key technology decisions reference ADRs or SBB-NNN entries — not free-text vendor names with no rationale
- Baseline technical debt is quantified where possible (e.g. "two on-premises servers reach end-of-life in Q3 2027")
- Target platform choices are traceable to Technology Principles (TP-NNN) — a platform choice that cannot be justified by any governing principle is a governance gap

**Common mistakes:**
- Naming specific products or vendors without rationale — the ADD should record the decision, not just the outcome
- Omitting the decommission plan for baseline components — without it, the target architecture is incomplete
- Technology choices in this chapter that contradict Application Architecture §5 (e.g. a different integration platform from what §5 describes)

**TOGAF reference:** TOGAF 10 Part III, Phase D — Technology Architecture. The ADD §6 is the management view; the full artifact contains the infrastructure diagrams, platform specifications, and SBB mapping.

</details>

**Baseline:** {{technology_baseline_summary}}

**Target:** {{technology_target_summary}}

**Full detail:** [Technology Architecture](../phase-d/technology-architecture.md)

---

## 7. Cross-Domain Alignment

<details>
<summary>📋 Guidance</summary>

**Purpose:** This is the ADD's primary value-add over the individual domain artifacts. The domain chapters (§3–§6) summarise each domain in isolation; this chapter documents where those domains intersect, depend on each other, or must be kept mutually consistent. Cross-domain alignment failures are the most common cause of architecture delivery breakdowns.

**What to include:** Explicit interaction points — e.g. "The Customer capability (Business) depends on the MDM platform (Technology) being operational before the CRM replacement (Application) can go live." Key constraints that one domain imposes on another. Conflicts that were identified and the resolution approach (with ADR reference if a significant decision was required). Any shared patterns or ABBs that span multiple domains.

**Quality indicators:**
- At least one cross-domain interaction identified per pair of active domains (Business↔Application, Application↔Data, Data↔Technology, etc.)
- Interactions describe concrete dependencies — not "Business and Technology must be aligned" but "the operating model change (Business) requires the event-driven messaging platform (Technology) to be live first"
- Conflicts are resolved, not just listed — if a conflict is noted with no resolution, it is an open risk, not a cross-domain alignment entry

**Common mistakes:**
- Leaving this section as a single placeholder row when multiple domain chapters are populated — this signals no cross-domain analysis was done
- Listing the same interaction table as the domain architecture artifacts without adding synthesis
- Omitting the sequence dependency: "Application depends on Data which depends on Technology" — the ordering of these dependencies drives the transition architecture and migration plan

**TOGAF reference:** TOGAF 10 §24 — the ADD Cross-Domain Alignment section is the integration mechanism that ensures the four domain architecture chapters (Phase B, C, D) are internally consistent and form a coherent whole.

</details>

| Interaction | Domains | Description | Resolution |
|---|---|---|---|
| {{interaction}} | Business ↔ Data | {{description}} | {{resolution}} |

---

## 8. Baseline Architecture Summary

<details>
<summary>📋 Guidance</summary>

**Purpose:** Provides the consolidated current-state picture across all active domains in a single coherent view. Stakeholders and delivery teams use this as the authoritative "where we are starting from" reference — it must be stable and agreed before transition planning begins.

**What to include:** A brief narrative that characterises the current architecture across domains — the key capabilities, systems, data assets, and infrastructure in place today. Highlight the pain points, technical debt, or capability gaps that motivate this engagement. Where possible, quantify: number of applications, age of key systems, volume of integration points, known end-of-life dates.

**Quality indicators:**
- The baseline is specific enough that a new team member could understand the current state without reading all four domain chapters
- Pain points are tied to named business drivers (DRV-NNN) or requirements (REQ-NNN)
- The content is confirmed by stakeholder review — not synthesised from documentation alone without validation

**Common mistakes:**
- Describing the target instead of the baseline (a surprisingly common error when documents are edited in target-first order)
- Overly technical baseline that does not connect to business impact — the ADD audience includes business sponsors
- Stale baseline content — if the engagement has been running for 6+ months and the baseline has changed, update it

**TOGAF reference:** TOGAF 10 §24 — the Baseline Architecture Summary corresponds to the Architecture Landscape description established in the Preliminary phase and refined during Phase A, consolidated across domains as Phases B–D complete.

</details>

{{baseline_summary}}

---

## 9. Target Architecture Summary

<details>
<summary>📋 Guidance</summary>

**Purpose:** The definitive statement of what the architecture will look like when the engagement objectives are met. This is the reference point for all gap analysis, transition planning, and compliance assessment work — every downstream artifact is validated against this section.

**What to include:** A narrative of the target state across all active domains — the capabilities added, systems introduced or retired, data ownership model established, and infrastructure platform selected. Describe what business outcomes this architecture enables. Reference the Architecture Vision for alignment with the original intent, and note any divergences from the Phase A target description (with rationale).

**Quality indicators:**
- The target is consistent with the Architecture Vision — if there are divergences, they are explained with ADR or A3 references
- The target is specific enough to drive gap analysis — each domain gap in the Gap Analysis artifact should be traceable to a delta between the baseline (§8) and this section
- Business outcomes are stated alongside the technical target — "the target enables real-time inventory visibility across all channels" not just "event-driven messaging platform"

**Common mistakes:**
- Describing an aspirational target that has not been validated against constraints — the target in the ADD is the ratified, feasibility-checked target, not the Architecture Vision aspiration
- Target that contradicts the individual domain architecture artifacts — always reconcile before publishing
- Missing the connection back to the Architecture Vision: if the target has evolved since Phase A, document why

**TOGAF reference:** TOGAF 10 §24 — the Target Architecture Summary is the ADD's consolidated, cross-domain, post-analysis target. It supersedes the Architecture Vision target description once Phases B–D are complete.

</details>

{{target_summary}}

---

<details>
<summary>Appendix A3 — Decision Log</summary>

| Item | Value | State | Captured By | Owner | Authority | Domain | Cost | Impact | Risk | Subject | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |

</details>

<details>
<summary>Appendix A4 — Stakeholder Concerns & Objections</summary>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

</details>

<details>
<summary>Appendix A5 — Related Architecture Decisions</summary>

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |

</details>

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
