---
artifact: Principles Register
artifactId: architecture-principles
engagement: "{{engagement_name}}"
phase: Preliminary
status: Draft
reviewStatus: Not Reviewed
version: 0.1
templateVersion: 0.9.49
lastModified: "{{date}}"
taxonomy:
  domain: Cross-cutting
  category: Governance
  audience: All
  layer: Governance
  sensitivity: Internal
  tags: [principles, governance, preliminary]
relatedArtifacts: []
diagrams: []
links: []
---

<details>
<summary>🔒 TOGAF/ADM Compliance Status (author only — collapses on export)</summary>

## Compliance Checklist

| Requirement | Status | Notes |
|---|---|---|
| Minimum one principle per active domain | ⚠️ Pending | Required |
| All principles have all 4 TOGAF fields (Name/Statement/Rationale/Implications) | ⚠️ Pending | Required |
| Statements use modal verb (must/shall/will/should) | ⚠️ Pending | Required |
| T3-A3: Appendix A3 — Decision Log present | ⚠️ Pending | Required |
| T3-ADR: Appendix A5 — Related Architecture Decisions present | ⚠️ Pending | Required |
| Summary counts up-to-date | ⚠️ Pending | Refresh with `/ea-principles list` |

*This section is for author guidance only. Run `/ea-grill` to validate compliance.*

</details>

<details>
<summary>📋 Guidance</summary>

**Purpose:** Architecture Principles are the non-negotiable rules that govern all architecture decisions across the engagement. Established in the Preliminary phase, they remain stable throughout. Every ADR, constraint, and solution choice must be reconcilable with this active principle set.

**What to include:** Principles in each of the four TOGAF domains (Business, Data, Application, Technology) that are active in this engagement. Each principle requires all four standard fields: Name, Statement, Rationale, and Implications.

**Quality indicators:**
- Statement starts with a modal verb (must/shall/will) and can be read as a testable rule
- Rationale cites a business risk, policy (POL-NNN), or driver (DRV-NNN) — not just "good practice"
- Implications include at least one thing the principle *prohibits* (not just what it requires)
- Domain coverage: at least one active principle per domain actively in scope for this engagement

**Common mistakes:**
- Principles that describe *how* something should be built rather than a *rule* about design decisions (those belong in Constraints: CST-NNN)
- More than 12 principles per domain — quality over quantity; too many principles are never enforced
- Duplicate principles across domains that could be unified
- Implications that are too vague to detect violations in an ADR or design review

**TOGAF reference:** TOGAF 10 Part II §3 — Architecture Principles. The four-domain structure (BP/DP/AP/TP) follows TOGAF standard; the ID scheme is an engagement-wide convention.

**ID scheme:** BP-NNN (Business), DP-NNN (Data), AP-NNN (Application), TP-NNN (Technology) — all zero-padded 3-digit. Manage with `/ea-principles list|add|update|trace`.

</details>

# Architecture Principles — {{engagement_name}}

---

## Summary

<details>
<summary>📋 Guidance</summary>

**Purpose:** Shows the count of principles by domain and lifecycle status at a glance. Update this table after every `/ea-principles add` or `/ea-principles update` action.

**What to include:** Active principles (in force), Draft principles (proposed but not yet ratified), Deprecated principles (retired — kept for traceability).

**Quality indicator:** A well-governed engagement has 5–12 active principles per active domain. If Total Active = 0, principles have not been established — this is a governance gap.

**Common mistake:** Leaving all values as `—` after adding principles. Run `/ea-principles list` to refresh.

</details>

| Type | Active | Draft | Deprecated | Total |
|---|---|---|---|---|
| Business | — | — | — | — |
| Data | — | — | — | — |
| Application | — | — | — | — |
| Technology | — | — | — | — |
| **Total** | — | — | — | — |

---

## Business Principles

<details>
<summary>📋 Guidance</summary>

**Purpose:** Principles that govern Business Architecture decisions — capabilities, operating model, value streams, and strategic direction. These are the rules the business must live by regardless of which systems or technologies are used.

**What to include:** Principles about business capability design, operating model constraints, service delivery philosophy, and business data ownership. Do NOT include IT or technology decisions here — those belong in Application or Technology principles.

**Quality indicators:**
- A business principle should remain true even if all current technology were replaced
- Each principle should be traceable to a business driver (DRV-NNN) or business policy (POL-NNN)
- Implications should describe concrete business consequences — e.g. "This means the organisation cannot outsource the [capability] function without ARB approval"

**Common mistakes:**
- "All systems must be cloud-native" — this is a Technology Principle, not a Business Principle
- Principles that reflect current practice rather than a normative rule for future decisions
- Vague implications like "all teams must consider this" with no specific constraint

**TOGAF reference:** TOGAF 10 §3.5 — Business Principles govern the business strategy and operating model layer.

</details>

### BP-001 — {{Name}}

| Field | Value |
|---|---|
| **ID** | BP-001 |
| **Status** | Active |
| **Source Policy** | — |

**Statement:** {{One sentence, starting with a modal verb — e.g. "Business capabilities must be designed to function independently of any single technology vendor."}}

**Rationale:** {{Why this principle exists — reference a DRV-NNN, POL-NNN, or specific business risk.}}

**Implications:**
- {{What this principle requires in practice}}
- {{What this principle prohibits in practice}}

---

## Data Principles

<details>
<summary>📋 Guidance</summary>

**Purpose:** Principles that govern Data Architecture decisions — ownership, quality, classification, privacy, and lifecycle. These ensure data is treated as a managed asset across the enterprise.

**What to include:** Principles about data ownership (who is authoritative), quality standards, classification and sensitivity handling, retention and disposal, and cross-domain data sharing.

**Quality indicators:**
- Each principle identifies who is accountable (a role, not a system) for the rule
- Implications specify what is prohibited — e.g. "No system may store a duplicate master record for Customer without ARB approval"
- Data sovereignty, privacy regulation, and classification constraints are reflected as principles where they impose design rules

**Common mistakes:**
- Principles that specify a particular database technology or tool (those are CST-NNN constraints or SBB-NNN choices)
- Omitting data sovereignty or regulatory principles where they exist
- "Data must be high quality" without specifying what quality means or how it is measured

**TOGAF reference:** TOGAF 10 §3.6 — Data Principles govern the data/information architecture layer.

</details>

<!-- Add DP-NNN entries below using the same structure as BP-001 above -->

---

## Application Principles

<details>
<summary>📋 Guidance</summary>

**Purpose:** Principles that govern Application Architecture decisions — component design, integration patterns, coupling, service contracts, and lifecycle. These prevent common anti-patterns like tight coupling and vendor lock-in at the application layer.

**What to include:** Principles about modularity (loose coupling, high cohesion), API-first design, reuse over rebuild, event-driven vs synchronous integration, and application lifecycle management.

**Quality indicators:**
- A principle like "Applications must expose capabilities through versioned APIs" is testable in an architecture review
- Implications describe concrete design constraints — e.g. "No application may call another application's database directly"
- Common integration and coupling anti-patterns are ruled out explicitly

**Common mistakes:**
- Principles that specify specific middleware products or frameworks (those belong in SBB-NNN / CST-NNN)
- "All applications must be maintainable" — too vague to use as a review criterion
- Omitting principles about integration — integration is the most common source of coupling violations

**TOGAF reference:** TOGAF 10 §3.7 — Application Principles govern application design and integration decisions.

</details>

<!-- Add AP-NNN entries below using the same structure as BP-001 above -->

---

## Technology Principles

<details>
<summary>📋 Guidance</summary>

**Purpose:** Principles that govern Technology Architecture decisions — platform selection, infrastructure design, vendor relationships, security posture, and operational standards. These are the rules that constrain technology choices and prevent lock-in.

**What to include:** Principles about vendor neutrality, cloud strategy, security-by-design, automation, resilience patterns, and platform standardisation.

**Quality indicators:**
- Technology principles should survive changes in vendor landscape — "must avoid single-vendor lock-in" outlasts any specific vendor's product roadmap
- Implications specify what is prohibited at design review time — e.g. "No SBB may be selected that lacks a documented exit strategy"
- Security, compliance, and operational principles are all represented

**Common mistakes:**
- Principles that mandate a specific vendor or product ("All infrastructure must run on AWS") — those belong in SBB-NNN decisions or CST-NNN constraints
- Omitting a security-by-design principle — this creates a governance gap visible in ARB reviews
- Principles at such a high level of generality that they cannot be used to challenge a technology choice

**TOGAF reference:** TOGAF 10 §3.8 — Technology Principles govern infrastructure, platform, and vendor selection decisions.

</details>

<!-- Add TP-NNN entries below using the same structure as BP-001 above -->

---

## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>

**Purpose:** Tracks significant governance decisions about the principles themselves — adopting a new principle, retiring an existing one, granting an exception, or resolving a conflict between two principles.

**What to include:** Each significant decision about the principle register. Minor wording changes do not need A3 entries; adoption, retirement, and formal exception grants do.

**Quality indicator:** If principles have been established but no A3 entries exist, governance decisions were made informally — document them retrospectively.

</details>

| # | Decision | Authority | Owner | Date | Status | Notes |
|---|---|---|---|---|---|---|
| A3.1 | *(record significant principle governance decisions here — e.g. adopting or retiring a principle)* | Strategic | — | — | Provisional | — |

---

## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>

Record concerns about specific principles — stakeholders who believe a principle is too restrictive, too vague, or conflicts with a business need. Also record challenges to the completeness of the principle set.

Use `/ea-concerns` to aggregate unresolved items across all artifacts.

</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |

---

## Appendix A5 — Related Architecture Decisions

<details>
<summary>📋 Guidance</summary>

List ADRs that are governed by, or informed the development of, the principles in this register. Each principle should eventually have at least one ADR that cites it — principles without ADR references may not be actively shaping decisions.

Use `/ea-principles trace` to find all ADRs and constraints referencing each principle.

</details>

| ADR-NNN | Title | Governed by Principle |
|---|---|---|
| — | — | — |

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

- [ ] *(Add tasks — e.g. "Establish at least one principle per active domain before Phase A sign-off")*
