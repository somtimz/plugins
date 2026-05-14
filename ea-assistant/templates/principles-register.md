---
artifact: Architecture Principles
artifactId: architecture-principles
engagement: "{{engagement_name}}"
phase: Preliminary
status: Draft
reviewStatus: Not Reviewed
version: 0.1.0
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

# Architecture Principles — {{engagement_name}}

> **Purpose:** Architecture Principles are the non-negotiable rules that govern all architecture decisions across the engagement. Established in the Preliminary phase, they remain stable throughout. Every ADR, constraint, and solution choice must be reconcilable with this set.
>
> **ID scheme:** BP-NNN (Business), DP-NNN (Data), AP-NNN (Application), TP-NNN (Technology)
>
> **Manage with:** `/ea-principles list|add|update|trace`

<!-- GUIDANCE
Each principle requires four fields (TOGAF standard):
- Name: short label (2–5 words)
- Statement: the normative rule — one sentence, modal verb (must/shall/will/should)
- Rationale: why this rule exists (1–3 sentences)
- Implications: what following this rule requires or prohibits in practice

Aim for 5–12 principles per active domain. Avoid implementation detail in statements — that belongs in constraints (CST-NNN).
-->

## Summary

| Type | Active | Draft | Deprecated | Total |
|---|---|---|---|---|
| Business | — | — | — | — |
| Data | — | — | — | — |
| Application | — | — | — | — |
| Technology | — | — | — | — |
| **Total** | — | — | — | — |

---

## Business Principles

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

<!-- Add DP-NNN entries below using the same structure as BP-001 above -->

---

## Application Principles

<!-- Add AP-NNN entries below using the same structure as BP-001 above -->

---

## Technology Principles

<!-- Add TP-NNN entries below using the same structure as BP-001 above -->

---

## Appendix A3 — Decision Log

| # | Decision | Authority | Owner | Date | Status | Notes |
|---|---|---|---|---|---|---|
| A3.1 | *(record significant principle governance decisions here — e.g. adopting or retiring a principle)* | Strategic | — | — | Provisional | — |

## Appendix A5 — Related Architecture Decisions

| ADR-NNN | Title | Governed by Principle |
|---|---|---|
| — | — | — |
