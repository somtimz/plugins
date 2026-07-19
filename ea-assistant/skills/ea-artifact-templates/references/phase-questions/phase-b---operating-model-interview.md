# Phase B — Operating Model Interview


**Goal:** Design the execution system that will run the Business Architecture day after day — organisation, roles, decision rights, controls, processes, workforce, sourcing, technology enablement, and performance management.

**When to run:** Run this interview after the Business Architecture capability/value-stream model is at least draft-stable. The OM executes the blueprint; designing it before the BA is stable risks an operating model that does not deliver the target capabilities.

**Key questions:**

### Operating Model Context
*Routes to: Operating Model §1*

1. What is the scope of this Operating Model — enterprise-wide, divisional, programme-level, or for a specific value stream?
2. Which Business Architecture capabilities (CAP-NNN) and value streams (VS-NNN) does this OM need to operationalise? Link each OM section back to at least one CAP-NNN or VS-NNN.
3. What Business Model Canvas changes (new segments, channels, revenue streams, partnerships) drive changes in how the organisation must operate?

### Organisation Design
*Routes to: Operating Model §2*

4. What operating units, teams, or forums are needed to deliver the target capabilities? Do not reproduce the whole enterprise org chart — focus on the operating structure required by this architecture.
5. For each operating unit: what capabilities (CAP-NNN) and value streams (VS-NNN) does it support?
6. How does the target operating structure differ from today's organisation? What units are new, merged, or retired?

### Roles, Decision Rights & Accountability
*Routes to: Operating Model §3*

7. For the key decisions this OM must make (e.g. pricing exceptions, capacity allocation, vendor selection, risk acceptance, hiring): who is accountable, who is consulted, who is informed, and what is the escalation path?
8. Which business operating roles are required that do not exist today? How do they differ from EA engagement roles (ROLE-NNN, managed via `/ea-roles`)?
9. Where are decision rights unclear or contested today? How will the OM resolve them?

### Governance, Controls & SLAs
*Routes to: Operating Model §4*

10. What business controls, checkpoints, or service-level expectations keep the operating model on track? (e.g. monthly capacity review, fraud control, customer complaint SLA)
11. Which policies (POL-NNN), constraints (CST-NNN), or business rules (BR-NNN) apply to each control?
12. Which controls are proportionate to risk, and which are overhead that should be challenged or removed?

### Business Processes Execution Model
*Routes to: Operating Model §5 + Business Processes Register*

13. Which end-to-end business processes are critical to this OM? For each: what value stream (VS-NNN) and capabilities (CAP-NNN) does it serve?
14. For each critical process: what is its OM role — core, supporting, exception handling, governance? Which operating role owns it?
15. Are the detailed process steps already captured as PROC-NNN entries, or do they need to be created via `/ea-processes add`?
16. Where do processes hand off across operating units, channels, or partners? What integration or orchestration is required?

### Workforce, Locations & Channels
*Routes to: Operating Model §6*

17. What skills, headcount, or workforce mix changes are needed to operate the target model?
18. Which locations, regions, or sites are in scope? Will the target state centralise, distribute, or regionalise work?
19. What delivery channels (digital, physical, partner, self-service) does this OM use? Link each to the relevant business service (SVC-NNN) and value stream (VS-NNN).
20. What are the implications of workforce/location/channel choices for capabilities and processes?

### Sourcing & Partnership Model
*Routes to: Operating Model §7*

21. For each capability or service in scope: is it made internally, bought via COTS/SaaS, or delivered through a partner/shared-service arrangement?
22. Who are the strategic vendors, outsourcers, or ecosystem partners? Link to Vendor Landscape (VDR-NNN) entries where applicable.
23. What make-vs-buy or partner decisions are hard to reverse, high cost, or contested? Flag these for ADR-NNN capture.

### Information & Technology Enablement
*Routes to: Operating Model §8*

24. At a business level, what data, applications, or technology are essential to enable this OM? Do not design Phase C/D detail here — just identify the enabling dependencies.
25. For each enabling dependency: which Phase C/D artifact will contain the detailed design (Data Architecture, Application Architecture, Technology Architecture)?
26. What technology constraints (existing platforms, mandated standards, skills gaps) shape the OM design?

### Performance Management
*Routes to: Operating Model §9 + engagement.json → metrics*

27. How will the OM be measured? Identify metrics (MET-NNN) for capability performance, process performance, customer outcomes, and financial impact.
28. For each metric: what is the target, the review cadence, and the accountable owner?
29. How do these metrics close the loop back to goals (G-NNN), objectives (OBJ-NNN), and strategies (STR-NNN)?

### Gap Analysis
*Routes to: Operating Model §10 + Gap Analysis*

30. What gaps exist in the target operating model relative to current operations? (organisation, process, control, workforce, sourcing, enablement, performance)
31. Which of these are OM gaps (how work is run) versus capability gaps (what the business can do)? Route capability gaps to the Business Architecture / Gap Analysis; keep OM gaps here.
32. Link each OM gap to a GAP-NNN entry.

### Decision Quality Questions
> Ask these after completing the standard Operating Model questions. Operating Model decisions are often organisationally and politically charged — evidence and accountability matter.

1. **[DECISION]** For each new operating unit or role: what evidence supports the design — volume, capability coverage, decision load, or risk exposure?
2. **[DECISION]** For each sourcing choice (make/buy/partner): what evidence supports the option, and what would change the decision?
3. **[DECISION]** Which decisions in this OM are hard to reverse (org design, outsourcing, location strategy)? Have they been captured as ADR-NNN or PAD-NNN?
4. **[DECISION]** Where decision rights are contested, what is the defensible, governance-backed position?
5. **[DECISION]** How will the OM be validated before full rollout — pilot, simulation, staged cutover, or other test?

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| OM scope and context | Operating Model | `§1 Operating Model Context — {{operating_model_context}}` |
| BA links (CAP-NNN / VS-NNN) | Operating Model | §1–§7 traceability fields |
| Business-model drivers | Operating Model | `§1` + Business Model Canvas link |
| Operating units / forums | Operating Model | `§2 Organisation Design — {{organisation_design}}` |
| Unit-to-capability/value-stream links | Operating Model | `§2` table |
| Target org changes | Operating Model / Gap Analysis | `§2` + GAP-NNN entries |
| Decision / accountability matrix | Operating Model | `§3 Roles, Decision Rights & Accountability` |
| New business operating roles | Operating Model | `§3` + Role Catalogue note |
| Governance controls / SLAs | Operating Model | `§4 Governance, Controls & SLAs` |
| Linked policies / rules / constraints | Operating Model / registers | `§4` + POL/CST/BR-NNN |
| Critical process list and OM role | Operating Model | `§5 Business Processes Execution Model` |
| Process ownership and handoffs | Operating Model + Business Processes Register | `§5` + PROC-NNN owner/scope |
| Workforce / skills changes | Operating Model | `§6 Workforce, Locations & Channels` |
| Locations / channels | Operating Model + Business Services Register | `§6` + `deliveryChannel` on SVC-NNN |
| Sourcing choices | Operating Model | `§7 Sourcing & Partnership Model` |
| Strategic vendors / partners | Operating Model + Vendor Landscape | `§7` + VDR-NNN |
| Hard-to-reverse sourcing decisions | ADR Register | ADR-NNN via `/ea-adrs new` |
| Information / tech enablement dependencies | Operating Model | `§8 Information & Technology Enablement` |
| Performance metrics | Operating Model + engagement.json | `§9 Performance Management` + `metrics[]` |
| OM gaps | Gap Analysis + Operating Model | `§10 Gap Analysis` + GAP-NNN |
| Requirements emerging from OM | Requirements Register | REQ-NNN via `/ea-requirements add` |

**Facilitation Notes:**
- Run the Business Architecture interview and confirm the capability/value-stream model before this interview. If the BA is unstable, spend the first half of this session validating BA links rather than designing new org structures.
- Use the Business Architecture capability map as the organising anchor — every OM element should trace to a capability or value stream; otherwise it is untethered design.
- Distinguish **business operating roles** (owned by the OM) from **EA engagement roles** (ROLE-NNN in the Role Catalogue). Confusing the two is a common Phase B error.
- Decision-rights questions often surface political tension; document the defensible position and escalate unresolved disputes to the Architecture Review Board.
- Sourcing and location decisions are frequently hard to reverse — convert them to ADR-NNN at the point the choice is ratified, not afterwards.
- Keep process detail in the Business Processes Register; this interview should produce a summary-and-link index in OM §5, not duplicated step tables.
- Workforce/channel questions should surface delivery-model implications for business services — update `deliveryChannel` and `operatingModelNote` on SVC-NNN entries via `/ea-services update`.

**§D Diagrams — ask at close of session:**
> "Three diagrams are standard for the Operating Model. Which would you like to create or describe now?"
- **Operating Model Overview** — value chain + operating units + delivery channels (`operating-model-overview.mmd`)
- **Organisation Design** — target operating structure and decision fora (`operating-model-org-design.mmd`)
- **Process Execution Context** — critical processes mapped to operating units and capabilities (`operating-model-process-context.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Operating Model frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard Operating Model questions. Ask: "Would you like to address security concerns for the Operating Model? (y/n)"

**SABSA focus:** Operational — security roles, controls, and supply-chain assurance

1. Which business operating roles own security decisions for this domain?
2. What security controls are embedded in the operating processes (e.g. segregation of duties, access recertification, fraud checks)?
3. What SLAs or assurance requirements apply to outsourced or partner-delivered capabilities?
4. Which third parties introduce material security or compliance risk, and how are they governed?

**Output routing:**
| Answer | Output |
|---|---|
| Security roles and accountabilities | Operating Model §3 + Governance Framework |
| Process-embedded security controls | Operating Model §4 + RIS-NNN |
| Supplier security SLAs / assurance | Operating Model §7 + Constraints Register |
| High-risk third parties | Vendor Landscape (VDR-NNN) + Risk Register (RIS-NNN) |

---
