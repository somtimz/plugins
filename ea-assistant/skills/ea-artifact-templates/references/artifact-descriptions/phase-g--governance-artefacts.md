# Phase G — Governance Artefacts


### Architecture Compliance Assessment

**Purpose:** A formal review of a project's deliverables or a solution design against the approved architecture. Documents the degree of conformance and any approved variances.

**Audience:** Architecture review board, project managers, delivery leads.

**Contents:**
- Project name and scope
- Architecture principles assessment (conformant / partial / non-conformant for each principle)
- Architecture standards assessment (conformant / exception approved / non-conformant)
- Approved variances with justification
- Outstanding risks
- Assessment outcome (Fully Conformant / Conditionally Conformant / Non-Conformant)
- Reviewer and date

**When to Create:** Phase G, at defined project milestones (design review, pre-build, pre-deploy).

**Who Reviews:** Architecture Review Board.

**Phase:** G.

---

### Implementation Governance Plan

**Purpose:** Translates the Architecture Governance Framework into a concrete, engagement-specific schedule of reviews, checkpoints, and ownership assignments tied to this programme's work packages. Where the Governance Framework defines permanent enterprise governance structures, the Implementation Governance Plan defines how governance will be executed for this specific delivery.

**Audience:** Programme managers, delivery leads, project EA liaisons, governance authority.

**Contents:**
- Governance scope and objectives
- Named governance contacts for each role (no anonymous roles)
- Review schedule tied to delivery milestones per work package
- Compliance checkpoint process (preparation, review, gate decision)
- Waiver and exception process
- Change request process and volume thresholds
- Escalation paths
- Reporting metrics and governance calendar

**When to Create:** At the start of Phase G, before the first architecture review gate. Update when the delivery schedule changes significantly or new work packages enter scope.

**Who Reviews:** Governance Authority, Lead Architect, Programme Manager.

**Phase:** G.

**Template:** `implementation-governance-plan.md` — create with `/ea-artifact create implementation-governance-plan`.

---

### Architecture Requirements Specification

**Purpose:** The definitive, consolidated specification of all architecture requirements for the engagement: functional, non-functional, constraints, principles, and assumptions.

**Audience:** Delivery teams, solution architects, QA leads, project managers.

**Contents:**
- Functional requirements register
- Non-functional requirements register
- Constraints register
- Assumptions register
- Traceability to business goals and architectural decisions

**When to Create:** Initiated in Phase A, populated and refined in Phases B, C, and D. Baseline is signed off before Phase G.

**Who Reviews:** Business stakeholders (functional requirements), technical leads (NFRs), programme sponsor (constraints and assumptions).

**Phase:** A–D (populated), G (baselined for compliance checking).

---
