# Phase B — Business Architecture Interview


**Goal:** Define business capabilities, processes, gaps, and business goals

**Key questions:**
1. What are the primary business functions performed by the organisation or the area in scope?
2. Walk me through the key end-to-end business processes — from customer/trigger to outcome.

   *2a. For each key process: walk me through the steps.*
   - Who performs each step (actor / role / system)?
   - Which application or system is used at each step?
   - Where are the key decision points or business rules applied?
   - What are the named exception paths — what can go wrong, and what happens next?
   - Is there an SLA or performance expectation for this process end-to-end?

   *2b. For each process: which value stream (from Q3a) is it part of, and which capabilities does it exercise?*
   (This builds the capability-to-process cross-reference that links §4 Processes to §3 Capabilities.)

3. Where are the biggest pain points or inefficiencies in current business operations?

3a. What are the end-to-end chains of activity that deliver value to your key stakeholders or customers?
   - For each value stream: what is the trigger that starts it, what is the end outcome the stakeholder receives, and who benefits?
   - Which value streams are most critical to the organisation's strategic goals (G-NNN)?
   - Assign each a VS-NNN ID.

   *3b. For each value stream: which business capabilities are exercised along the path?*
   - Are there steps in the value stream where no existing capability covers the need?
   - Flag any uncovered steps as capability gaps — these will become GAP-NNN entries.

4. Let's build the capability model systematically — this is the core Phase B deliverable. Capabilities are mastered in the Business Architecture capability table and managed with **`/ea-capabilities`** (which can also seed from the Architecture Repository's canonical capability map via `adopt`). A capability is an *ability to achieve an outcome* — a noun ("Order Management"), not a process ("Process Orders").

   a. **Level 1 — Domains:** What are the major capability domains relevant to this engagement?
      (e.g. Customer Management, Operations, Finance, Technology, Compliance — agree 4–8 domains)
      Assign each a CAP-NNN ID starting at CAP-001.

   b. **Level 2 — Capabilities:** For each domain, what specific capabilities must the organisation have to deliver value in that domain?
      Assign sequential CAP-NNN IDs continuing from the L1 IDs.

   c. **Level 3 — Sub-capabilities:** For any L2 capability where detail matters for gap analysis, what sub-capabilities exist beneath it?
      Only elicit L3 where there is a known gap or a Phase B deliverable that requires it.

   c2. **Value / Outcome:** For each capability, what business outcome does it enable — the value of being able to do it? ("What do we gain by being able to do this?") A capability with no articulated value and no strategic anchor is **capability inflation** — flag it for removal or as commodity overhead. Distinguish **differentiating** capabilities (where you compete — invest) from **commodity** ones (table stakes — make efficient). Recorded in the Value / Outcome column.

   d. **Maturity Assessment:** For each L2 and L3 capability, rate the current maturity:
      - **Absent** — this capability does not exist today
      - **Immature** — exists but ad hoc, inconsistent, or person-dependent
      - **Developing** — repeatable and documented but not optimised
      - **Mature** — optimised, governed, and performing well

   e. **Target Maturity:** What maturity level does each capability need to reach to support the engagement's strategies and goals?

   f. **Strategic Alignment:** Which STR-NNN or G-NNN does each capability support?
      Any capability with no strategic anchor should be flagged for removal or reclassification.

4a. Who are the primary actors that interact with this business domain?
    (Actors are roles, not individuals — examples: Customer, Supplier, Finance Officer, External Regulator, Internal System)

4b. For each actor: what are the 3–5 most important things they need to accomplish in this domain?
    - Capture each as a use case: "{Actor} needs to {goal}" — e.g. "Customer needs to submit a warranty claim"
    - **Layer test:** If the use case subject is "how we govern" or "how we standardize" (e.g., "Define governance process for AI projects") rather than "what the actor needs" (e.g., "Auto-triage cases with AI"), it is an **EA Capability Use Case** — route it to the Governance Framework or Architecture Principles, not the Business Architecture Use Case Catalog.
    - Assign each a UC-NNN ID sequentially.

4c. For each use case: what triggers it, what must be true before it starts (preconditions), and what does success look like for the actor?
    - Summarise the main success scenario in one sentence — the normal path from trigger to outcome.
    - Are there named alternate paths or exception scenarios worth noting at architecture level?

4d. For each use case: which capabilities (CAP-NNN) must the business have to support it?
    - Any use case where no existing capability covers the need is a capability gap — flag it in §7 Gap Analysis.
    - Link each UC-NNN to the value stream (VS-NNN) it contributes to.

5. How is the organisation structured — what divisions, teams, or geographies are involved?
6. What are the priority business outcomes this architecture must support?
7. What does the business need to look like in three to five years?
8. How is performance measured today — what KPIs or metrics matter most?
9. *(If Business direction not yet defined or needs refinement)* Let's capture Business direction. Remind the user of the distinction:
   - **Goal** = where the business wants to be (qualitative; no number required)
   - **Objective** = how far and by when (must have a measure, a target, and a deadline)
   - **Strategy** = how you'll get there (a chosen approach, not an outcome)

   Ask for goals first, then objectives for each goal, then strategies. If a response has a target number or deadline, classify it as an objective. If it describes an approach (e.g. "use agile delivery"), classify it as a strategy.
10. For each Business objective captured, ask: "How will you measure this — what is the unit of measure, and where does the data come from? What is the current baseline?" Capture as a `performance` metric (`BM-`) linked to the objective. For goals, ask for a leading indicator — capture as an `outcome` metric. For strategies, ask for an activity measure — capture as an `activity` metric.

### Decision Quality Questions
> Ask these after completing the standard Phase B questions. Phase B is where capability gaps are identified — decisions on how to close them should be evidence-based.

1. **[DECISION]** For each capability gap identified: what POC, benchmark, or reference implementation is required before committing to a closure approach?
2. **[DECISION]** When a make-vs-buy or build-vs-configure choice is proposed, what evidence supports each option? Has a weighted scorecard been applied?
3. **[DECISION]** What optionality is preserved in the target capability model? If a vendor or pattern is chosen, how hard is it to reverse or swap later?
4. **[DECISION]** Are any decisions being made under strong stakeholder pressure? What is the defensible evidence-based position?
5. **[DECISION]** Which capability gaps should be logged as PAD-NNN rather than committed decisions? (Gaps with weak evidence, high reversibility cost, or unclear impact.)

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Primary business functions | Business Architecture | `{{business_functions}}` |
| Key end-to-end processes | Business Architecture | `§4 Business Processes` |
| Process steps, actors, systems, decisions | Business Architecture | `§4 Business Processes — Steps table` |
| Process exceptions | Business Architecture | `§4 Business Processes — Exceptions` |
| Process SLA / performance | Business Architecture | `§4 Business Processes — SLA / Performance` |
| Pain points/inefficiencies | Gap Analysis | `{{current_state_gaps}}` |
| Value streams (VS-NNN) | Business Architecture | `§3a Value Streams` |
| Capability-to-value-stream linkage | Business Architecture | `§3a Key Capabilities column` + `§3 Supports column` |
| Capability domains (L1, CAP-NNN) | Business Architecture | `§3 Business Capabilities` (Level L1) |
| Capabilities (L2, CAP-NNN) | Business Architecture | `§3 Business Capabilities` (Level L2) |
| Sub-capabilities (L3, CAP-NNN) | Business Architecture | `§3 Business Capabilities` (Level L3) |
| Capability maturity assessments | Business Architecture + Gap Analysis | `§3` maturity columns + `§7 Gap Analysis` |
| Capability-to-strategy links | Business Architecture | `Supports (STR-NNN / G-NNN)` column |
| Actors | Business Architecture | `§4a Use Case Catalog — Primary Actor` |
| Use cases (UC-NNN) | Business Architecture | `§4a Use Case Catalog` |
| Use case capability linkage | Business Architecture | `§4a Capabilities Used (CAP-NNN)` |
| Use case value stream linkage | Business Architecture | `§4a` → `§3a VS-NNN` cross-reference |
| Gap Analysis | Gap Analysis | `{{business_gaps}}` |
| Organisation structure | Business Architecture | `{{org_structure}}` |
| Priority business outcomes | Business Architecture | `{{business_outcomes}}` |
| Future state description | Business Architecture | `{{future_state}}` |
| KPIs and metrics | Business Architecture | `{{performance_metrics}}` |
| Business direction (goals, objectives, strategies) | engagement.json + Business Capability Map | `direction.Business` + `{{business_direction}}` |
| Business metrics | engagement.json + Business Capability Map | `metrics.Business` + `{{business_metrics}}` |

**Facilitation Notes:**
- Recommended sequence: value streams (Q3a) → capability model (Q4) → process decomposition (Q2a) → use cases (Q4a). Value streams provide the organising context before drilling into capability and process detail.
- Work top-down on capabilities: agree L1 domains first (with the group), then populate L2 capabilities for the domains most relevant to the engagement scope. Don't attempt to enumerate all L3 sub-capabilities — only go to L3 where there is a known gap or a Phase B deliverable that requires it.
- Run a capability mapping workshop using a whiteboard or collaborative tool — asking participants to place capabilities on a heat map (invest/maintain/retire) surfaces priorities faster than questions alone.
- Process walk-throughs are best done with operational staff, not just managers; the "how it actually works" often differs significantly from the "how it should work" described by leadership. The Steps table in §4 is most accurately populated in a session with process owners, not IT leadership.
- Decision / business rule capture (Q2a) frequently surfaces where compliance, exception handling, and system complexity live — these become inputs to application architecture component design.
- Use case elicitation (Q4a) works well after the capability model is agreed — actors often emerge naturally from capability discussions ("who uses this capability?").
- When identifying gaps, ask "what would you do if you had no constraints?" to surface aspirational capabilities before applying reality checks.
- Every L2/L3 capability where Current Maturity < Target Maturity is a Capability Gap — ensure it appears in the Gap Analysis Capability Gap Register with a Prevents (G-NNN/OBJ-NNN) link.
- Every use case with no covering capability is also a Capability Gap — flag it immediately in §7.
- The KPIs question links business architecture to measurable outcomes — use answers to define gap analysis criteria.

**§D Diagrams — ask at close of session:**
> "Four diagrams are standard for the Business Architecture. Which would you like to create or describe now?"
- **Capability Map** — hierarchical heat map of business capabilities with maturity colouring (`business-architecture-capability-map.mmd`)
- **Value Stream Map** — end-to-end chains of activity with capability overlays (`business-architecture-value-stream.mmd`)
- **Business Process Flow** — swimlane for the most critical end-to-end process (`business-architecture-process-flow.mmd`)
- **Organisation Map** — structure and roles in scope (`business-architecture-org-map.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Business Architecture frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase B? (y/n)"

**SABSA focus:** Conceptual — security policies, business security attributes, organisational model

1. What are the business security attributes required? (confidentiality, integrity, availability, auditability, accountability, non-repudiation — which matter most and why?)
2. What security policies govern this business domain? Are they documented and enforced?
3. How are security roles and responsibilities organised? Is there a clear RACI for security decisions?
4. What are the security-sensitive business processes — processes where a failure would cause regulatory, financial, or reputational harm?
5. What third-party or supply chain relationships introduce security risk?

**Output routing:**
| Answer | Output |
|---|---|
| Business security attributes | Business Architecture (security section), REQ-NNN type:security, source:business policy |
| Security roles and RACI | Business Architecture (security RACI), Governance Framework |
| Security-sensitive processes | Business Architecture (process security notes), RIS-NNN |

---
