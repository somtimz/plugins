# Phase A — Architecture Vision Artefacts


### Architecture Vision

**Purpose:** Provides a high-level, stakeholder-oriented description of the target architecture and the value it will deliver. It is the primary communication document for executive and business stakeholders, and the **strategic index** for the engagement: §4–§11 summarise the motivation chain and link to the dedicated registers (Drivers/Goals/Objectives/Strategy/Issues/Problems) rather than embedding their full tables. Sign-off reviews the Vision together with its linked registers.

**Audience:** Executive sponsors, programme sponsors, senior business and IT stakeholders.

**Contents:**
- Executive summary of the problem being solved
- **Direction summaries (§4–§11)** — concise prose/summary per motivation concept drawn from `engagement.json direction`, each with a **"Full register" link** to its dedicated register ([[drivers-register]], [[goals-register]], [[objectives-register]], [[issues-register]], [[problems-register]], [[strategy-register]]). The Vision does not embed the full item tables — those live in the registers. Opportunities (§9) and Key Metrics (within §11) have no dedicated register and keep a lean Vision table.
- **Metrics Summary** — cross-domain table drawn from `engagement.json metrics`, listing all metrics grouped by type (Outcome / Performance / Activity), showing name, measure, baseline → target, deadline, frequency, source, linked direction ID, and current status. Metrics with no `name` or `measure` are excluded.
- Business goals and strategic drivers
- Scope of the architecture engagement
- High-level description of the target state (narrative, not technical)
- Key stakeholder concerns and how the architecture addresses them
- Preliminary risk and constraint identification
- Solution Concept Diagram (high-level visual)
- Proposed approach and timeline summary

**When to Create:** Phase A. Produced before detailed architecture work begins; used to obtain sponsorship approval to proceed.

**Who Reviews:** Programme sponsor, key business stakeholders, Architecture Review Board.

**Phase:** A.

---

### Statement of Architecture Work

**Purpose:** A formal agreement between the architecture team and the commissioning organisation that defines the scope, schedule, deliverables, resources, and acceptance criteria for the architecture engagement.

**Audience:** Programme sponsor, architecture team, project management, governance body.

**Contents:**
- Organisation and project sponsors
- Architecture engagement scope (business domains, systems, geographies in/out of scope)
- Constraints and assumptions
- Architecture deliverables list with due dates
- Resource requirements
- Review and acceptance process
- Risks

**When to Create:** Phase A, concurrent with the Architecture Vision. Signed off by the sponsor before Phase B begins.

**Who Reviews:** Programme sponsor, architecture team lead, project manager.

**Phase:** A.

---

### Stakeholder Map and Matrix

**Purpose:** Identifies all stakeholders relevant to the architecture engagement, their concerns, interest, and influence, and defines the engagement strategy for each.

**Audience:** Architecture team (internal reference); summary versions shared with programme management.

**Contents:**
- Stakeholder name and role
- Organisation / business unit
- Interest in the architecture (what they care about)
- Concerns (specific worries or questions)
- Influence level (High / Medium / Low)
- Engagement approach (inform, consult, collaborate, empower)
- Communication plan notes

**When to Create:** Phase A. Updated throughout the engagement as new stakeholders are identified.

**Who Reviews:** Architecture team, programme manager.

**Phase:** A (updated throughout).

---

### Business Case

**Purpose:** The economic and political instrument that secures the mandate and funding for the architecture engagement. States the problem, compares the realistic options on cost, value, and risk, and recommends one — backed by architecture-grade Cost Entries (FIN-NNN) from the Cost Model Register, not hand-waving. It is the artifact a sponsor reads before committing money.

**Audience:** Sponsor, executive leadership, investment/steering committee, programme management.

**Contents:**
- Problem / opportunity tied to drivers (DRV-NNN), goals (G-NNN), and objectives (OBJ-NNN), with the cost of inaction
- Options Considered table — genuinely distinct options including "do nothing", each referencing its FIN-NNN entries (Capex, Opex, 3-Year TCO, annual benefit, payback, confidence, trade-off)
- Recommended option with rationale framed in cost, risk, AND value terms (T4-ECON)
- Cost-Benefit Summary drawn from the recommended option's Cost Entries
- Assumptions with confidence; key risks (linked to RIS-NNN)
- Funding & timing aligned to Architecture Roadmap waves and annual funding cycles
- Benefits Realisation — each benefit assigned a `benefit`-type metric and an owner, reviewed in Phase G

**When to Create:** Phase A with directional estimates (the funding/mandate instrument supporting the Request for Architecture Work and Architecture Vision). Refined in Phase F once the Architecture Roadmap and Cost Entries are firm.

**Who Reviews:** Sponsor, investment/steering committee, architecture review board.

**Phase:** A (draft), F (refined).

**Template:** `business-case.md` — create with `/ea-artifact create business-case`. Populate costs via `/ea-finance`.

---

### Communications Plan

**Purpose:** Defines how architecture information will be communicated to each stakeholder group throughout the ADM cycle — what they need to know, how often, through what channel, and who is responsible. Complements the Stakeholder Map by converting stakeholder engagement strategies into a concrete communication schedule.

**Audience:** Architecture team, programme manager, communications leads.

**Contents:**
- Communication objectives for the engagement
- Stakeholder communication matrix (group, information need, frequency, channel, owner, ADM phases)
- Communication schedule mapped to ADM phase milestones and gate reviews
- Communication channels and formats
- Escalation and feedback process

**When to Create:** Phase A, alongside the Stakeholder Map. Updated when stakeholder landscape changes or a new phase gate is added.

**Who Reviews:** Architecture team lead, programme manager.

**Phase:** A (updated throughout).

**Template:** `communications-plan.md` — create with `/ea-artifact create communications-plan`.

---

### Business Transformation Readiness Assessment

**Purpose:** Rates the organisation's readiness to absorb the transformation across twelve TOGAF readiness factors (vision clarity, desire, need, business case, funding, sponsorship, governance, accountability, workable approach, IT capacity, enterprise capacity, ability to implement and operate) — each with a readiness rating, urgency, and difficulty to fix. Low-readiness factors become risks (RIS-NNN) and readiness work packages, and cap how much concurrent change the roadmap may schedule.

**Audience:** Sponsor, programme leadership, architecture team.

**Contents:**
- Readiness factor table (12 factors × readiness/urgency/difficulty/evidence)
- Factor detail blocks for Low/None factors with readiness actions
- Roadmap implications (change-capacity ceiling, readiness work packages)

**When to Create:** Phase A (first assessment); reassessed at Phase E before wave sequencing — the roadmap must respect readiness, not assume it.

**Who Reviews:** Sponsor, programme manager, architecture team lead.

**Phase:** A (refined in E).

**Template:** `business-transformation-readiness.md` — create with `/ea-artifact create business-transformation-readiness`.

---

### Architecture Definition Document

**Purpose:** The primary container for all architecture descriptions produced across the ADM cycle. Brings together the Business, Data, Application, and Technology architecture chapters into a single coherent document with cross-domain alignment and baseline/target narratives. Evolves from a skeleton in Phase A to a finalised, approved baseline in Phase F.

**Audience:** Architecture Review Board, governance authority, delivery teams, programme sponsor.

**Contents:**
- Document status table (chapter by chapter, with source artifact links)
- Scope and context
- Architecture Principles summary (references the Principles Catalogue)
- Business Architecture chapter (summarised, linking to full artifact)
- Data Architecture chapter (summarised, linking to full artifact)
- Application Architecture chapter (summarised, linking to full artifact)
- Technology Architecture chapter (summarised, linking to full artifact)
- Cross-domain alignment (interactions, dependencies, conflicts and resolutions)
- Baseline Architecture summary (cross-domain)
- Target Architecture summary (cross-domain)

**When to Create:** Phase A (skeleton — structure and high-level content from Architecture Vision). Populated chapter by chapter as domain architectures are completed in Phases B, C, and D. Refined in Phase E; finalised and approved in Phase F.

**Who Reviews:** Lead Architect (each phase); Architecture Review Board (Phase F finalisation).

**Phase:** A (skeleton), B–D (populated), E (refined), F (finalised).

**Template:** `architecture-definition-document.md` — create with `/ea-artifact create architecture-definition-document`.

---
