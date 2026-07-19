# Preliminary Phase Interview


**Goal:** Establish the Engagement Charter, Architecture Principles, and Governance Framework

**Deliverables:** Engagement Charter, Architecture Principles, Governance Framework

---

### Preliminary — Part 1: Organisation & Engagement Context

*Routes to: Engagement Charter §1 (Organisation Background), §2 (Purpose & Mandate), §3 (Scope)*

1. Describe the organisation: industry, operating model, scale, and the key aspects of the current technology landscape that are relevant to this engagement.
2. What has changed recently — strategically, competitively, or operationally — that is making this engagement necessary now?
3. Who has authorised this engagement and what is the formal mandate? (Board resolution, executive decision, regulatory directive, programme board approval)
4. How would you classify this engagement type?
   - [ ] Greenfield implementation — building new capability where none exists
   - [ ] Legacy modernisation — replacing or upgrading existing systems
   - [ ] Cloud migration — moving workloads to cloud platforms
   - [ ] Capability assessment — understanding current state before committing to direction
   - [ ] Regulatory compliance — mandated by a regulation or external body
   - [ ] Merger / acquisition integration — consolidating organisations or systems
   - [ ] Post-acquisition rationalisation — reducing duplication after a merger
   - [ ] Other: ___
5. What is explicitly in scope for this engagement? What is explicitly out of scope?
6. What assumptions are you making that, if wrong, would significantly change the scope or approach?
7. What constraints apply to this engagement? (select all that apply)
   - [ ] Regulatory — compliance obligations, legal requirements, data residency rules
   - [ ] Financial — budget cap or envelope
   - [ ] Technical — existing platform lock-in, skills gap, mandated standards
   - [ ] Organisational — headcount limits, change capacity, political constraints
   - [ ] Time — fixed deadline, regulatory timeline, or programme dependency
   - [ ] Other: ___

---

### Preliminary — Part 2: Relationships & Affected Organisations

*Routes to: Engagement Charter §4 (Related Engagements), §5 (Organisations Affected)*

8. What other programmes or projects is this engagement related to — as a predecessor, successor, or peer? What does this engagement depend on from them, and what do they depend on from this engagement?
9. Which internal divisions or business units will be significantly affected by this engagement?
10. Which external organisations — customers, partners, suppliers, regulators — are affected?
11. Are there regulatory or compliance bodies whose requirements this engagement must satisfy?

---

### Preliminary — Part 3: Motivation Framework

*Routes to: Engagement Charter §6, engagement.json → direction (rendered in the motivation registers), Architecture Vision §4–§5/§7–§8/§10 summaries*

12. What external forces (market shifts, regulatory changes, competitive pressure, technology change) are creating pressure to act now? Assign each a DRV-NNN ID.
13. What internal forces (cost pressure, strategic mandate, leadership change, capability gap) are pushing this engagement forward? Assign each a DRV-NNN ID.
   - For each driver: what evidence, event, or data point confirms this is real pressure on the organisation right now? Note the source (report, incident, regulatory instrument, stakeholder statement). A driver without a verifiable source is an assumption — flag it.
14. Given those drivers, what are the high-level outcomes this engagement must achieve? Capture each as a goal (G-NNN) — a qualitative statement of a desired future state.
15. For each goal: what specific, measurable result would prove this goal is being achieved, and by when? Capture each as an objective (OBJ-NNN) with a measure and deadline.
16. How does the organisation intend to achieve its goals? Capture the key approaches as strategies (STR-NNN), each linked to the goals it supports.
17. What is currently getting in the way? Capture strategic threats as issues (ISS-NNN, linked to goals) and operational blockers as problems (PRB-NNN, linked to objectives).

---

### Preliminary — Part 4: Programme Structure

*Routes to: Engagement Charter §7 (Programme Structure)*

18. How is this engagement structured as a programme? What major phases of delivery do you anticipate?
   - Common phase types: Planning, Preparation, Procurement, Pilot, Implementation (one or more waves), Post-Implementation / Benefits Realisation
   - Not all types are required — phases may be merged or omitted
19. For each programme phase: what are the key deliverables, linked goals, estimated duration, and prerequisites?
20. What is driving the phasing decision? (e.g. regulatory deadline, risk management, change capacity, budget approval cycles, technology dependencies)

---

### Preliminary — Part 5: Outcomes, Benefits, Costs & Risks

*Routes to: Engagement Charter §8 (Outcomes), §9 (Benefits), §10 (Costs), §11 (Risk Profile)*

21. When this engagement is complete, what will be different? Describe the outputs (what will be delivered), outcomes (how the organisation will operate differently), and impacts (strategic effects).
22. What financial benefits do you expect? (cost reduction, cost avoidance, revenue growth, efficiency gains — quantify where possible)
23. What non-financial benefits do you expect? (risk reduction, compliance, capability, resilience, customer experience)
24. What is the budget envelope for this engagement? What are the major cost categories?
25. What are the top risks to this engagement succeeding? For each: what is the likelihood, impact, and proposed mitigation?
26. What level of residual risk is the sponsor willing to accept? Under what circumstances would the engagement be paused or stopped?

---

### Preliminary — Part 6: Governance & Principles

*Routes to: Architecture Principles, Governance Framework*

27. Who are the key decision-makers for IT investment in your organisation?
28. Does an existing architecture governance body or process exist? If so, how does it operate?
29. What are the top three strategic goals for your organisation over the next three years?
30. What does good architecture practice look like in your organisation?
31. What existing frameworks, standards, or methodologies does the organisation follow?
32. How would you describe your organisation's risk appetite for technology change?

---

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Organisation profile | Engagement Charter | `§1.1 Organisation Profile` |
| History & context | Engagement Charter | `§1.2 Relevant History & Context` |
| Engagement purpose & mandate | Engagement Charter | `§2 Purpose & Mandate` |
| Engagement type | Engagement Charter | `§2.2 Mandate` + `engagement.json → engagementType` |
| Scope in/out | Engagement Charter | `§3 Scope & Boundaries` |
| Assumptions | Engagement Charter | `§3.4 Assumptions` |
| Constraints | Engagement Charter / Constraints Register | `§3.5 Constraints` + `CST-NNN` entries via `/ea-constraints` |
| Related engagements | Engagement Charter | `§4` |
| Organisations affected | Engagement Charter | `§5` |
| Business drivers (DRV-NNN) | Engagement Charter `§6.2` + Architecture Vision `§4` + `engagement.json → direction.drivers` | — |
| Goals (G-NNN) | Engagement Charter `§6.3` + Architecture Vision `§5` + `engagement.json → direction.goals` | — |
| Objectives (OBJ-NNN) | Engagement Charter `§6.4` + Architecture Vision `§10` + `engagement.json → direction.objectives` | — |
| Strategies (STR-NNN) | Engagement Charter `§6.5` + Architecture Vision `§11` + `engagement.json → direction.strategies` | — |
| Issues / Problems | Engagement Charter `§6.6` + Architecture Vision `§7` + `§8` | — |
| Programme structure | Engagement Charter | `§7 Programme Structure` |
| Expected outcomes | Engagement Charter | `§8` |
| Benefits | Engagement Charter | `§9` |
| Costs | Engagement Charter | `§10` |
| Risk profile | Engagement Charter `§11` + Risk Register (via `/ea-risks`) | — |
| Key stakeholders | Engagement Charter `§12` + Stakeholder Map `{{stakeholder_table}}` | — |
| IT decision-makers | Architecture Principles | `{{existing_governance}}` |
| Strategic goals (principles context) | Architecture Principles | `{{strategic_goals}}` |
| Good architecture definition | Architecture Principles | `{{architecture_definition}}` |
| Existing frameworks/standards | Architecture Principles | `{{existing_frameworks}}` |
| Risk appetite | Architecture Principles | `{{risk_appetite}}` |
| Governance body | Governance Framework | `§3 Governance Structure` |

**Facilitation Notes:**
- Run the context and motivation questions (Parts 1–3) as a structured workshop with senior leadership and the sponsor — competing priorities and scope disagreements surface quickly in a group setting.
- Run the programme structure and risk questions (Parts 4–5) with the programme director and key delivery leads.
- Run the governance and principles questions (Part 6) with the EA team, CTO/CIO, and ARB members.
- Ask for written documentation of existing principles, strategies, or standards before the session — gaps between stated and documented practice are significant findings.
- If no governance body exists, note this as a gap and flag it as a deliverable (Governance Framework) rather than leaving it unaddressed.
- The motivation framework (Part 3) produces IDs used in all subsequent artifacts — agree them in this session and record in engagement.json before moving to Phase A.
- Dual-route all DRV/G/OBJ/STR/ISS/PRB responses: write to the Engagement Charter AND to engagement.json → direction simultaneously.

**§D Diagrams — ask at close of session:**
> "Two standard diagrams help communicate the engagement scope and structure. Would you like to create either of these now, or describe what they should show?"
- **Context Diagram** — engagement boundary, key external organisations and relationships (`engagement-charter-context.mmd`)
- **Organisation Chart** — structure and units in scope (`engagement-charter-org-chart.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filename added to Engagement Charter frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for the Preliminary Phase? (y/n)"

**SABSA focus:** Contextual — governance, obligations, and existing security posture

1. What security governance model applies to this organisation? (e.g., CISO-led, committee-based, outsourced)
2. Who holds security decision authority — who can approve exceptions, set policy, and sign off on architecture security sections?
3. What security policies already exist? Are they current and enforced?
4. What compliance obligations apply? (e.g., GDPR, PCI-DSS, ISO 27001, HIPAA, sector regulation)
5. Is there an existing ISMS or security programme this engagement must align with?
6. What is the current security maturity tier? (NIST CSF: Partial / Risk Informed / Repeatable / Adaptive)

**Output routing:**
| Answer | Output |
|---|---|
| Governance model and decision authority | Architecture Principles (security governance section) |
| Existing policies and compliance obligations | Governance Framework (security notes), DRV-NNN type:security |
| Current maturity tier | Architecture Vision (security baseline section) |

### Decision Quality Questions
> Ask these after completing the standard Preliminary Phase questions. They probe whether decisions are being made at the right time with sufficient evidence.

1. **[DECISION]** Which decisions must be made in the Preliminary Phase, and which should be deferred to later phases? (Principles should be decided now; technology choices should not.)
2. **[DECISION]** Are the architecture principles evidence-based — grounded in known constraints, regulatory requirements, or proven practice — or are they aspirational statements?
3. **[DECISION]** Is there strong pressure to make specific technology or vendor commitments before Phase A? If so, how will you handle it? (Convert to PAD-NNN with constraint boundaries.)
4. **[DECISION]** What evidence would change the principles you've defined? If none, the principles are assumptions — flag them.

---
