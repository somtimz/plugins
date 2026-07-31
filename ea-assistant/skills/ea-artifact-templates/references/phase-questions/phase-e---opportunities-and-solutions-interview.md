# Phase E — Opportunities and Solutions Interview


**Goal:** Prioritise work packages and build the initial architecture roadmap, grounded in the Goals, Objectives, and Strategies established in Phase A.

**Pre-session preparation:** Load the Architecture Vision and read §5 Goals (G-NNN), §10 Objectives (OBJ-NNN), §9 Opportunities (OPP-NNN), and §11 Strategic Direction Summary (STR-NNN) before starting. Present this list to participants so work package prioritisation is anchored to stated intent.

**Key questions:**

*Strategic alignment (ask first — establishes the anchor for all prioritisation)*
1. Looking at the Goals and Strategies defined in Phase A, which are the most critical to advance in the next 12 months? (Reference G-NNN and STR-NNN IDs by name.)
2. For each proposed work package, which Goal, Objective, or Strategy does it directly advance? Are there Goals or Strategies that no work package addresses — and is that intentional?

*Opportunity and gap coverage*
3. Which capability gaps identified in earlier phases are the highest priority to close?
4. For each high-priority gap — does it represent an Opportunity (OPP-NNN) to capture, not just a problem to fix? Assign an OPP-NNN if so, and link it to the work package it will be addressed by.
   - If an OPP-NNN was already recorded in Phase A, link the WP to it now.
   - If no OPP-NNN exists yet, create one and add it to Architecture Vision §9.
5. What projects are already in flight that this roadmap must align with or avoid conflicting with?

*Resources and capacity*
6. For each proposed work package: what roles and skills are needed to deliver it? Estimate FTE required and identify any skill gaps or vendor/partner dependencies.
   - Record: Roles, FTE estimate, skill dependencies, vendor/partner — in the WP's `Resources Required` field in the Architecture Roadmap.
   - Flag any WP where required resources are not confirmed as a delivery risk.

*Constraints and sequencing*
7. What is the available investment budget and target delivery timeline?
6. What sequencing dependencies exist — which changes must happen before others can begin?
8. What sequencing dependencies exist — which changes must happen before others can begin?
9. What are acceptable transition states — what does "good enough for now" look like at each stage?
10. If the budget were halved, which Goals and work packages would you protect, and which would you defer?

*Risk*
11. What are the biggest risks to delivering this roadmap — and do any of those risks directly threaten a Goal or Strategy?

**User Story (STY-NNN) questions:**
> Ask these when decomposing work packages into delivery items. Stories translate SBBs into actor-centred work.

12. For each SBB-NNN selected in Phase D: what user stories are needed to implement it?
    - Who is the actor? (user, operator, customer, system)
    - What does the actor want to accomplish? (goal)
    - Why does it matter? (benefit)
    - Format: "As a {actor}, I want {goal} so that {benefit}."
    - Assign a STY-NNN ID and capture in the Requirements Register Stories subsection or Architecture Roadmap.

13. For each story: what acceptance criteria confirm it is done?
    - Measurable outcomes: "Given X, when Y, then Z"
    - Link each criterion to a REQ-NNN measurable target where possible.

14. Are there enabler stories — infrastructure, security, compliance scaffolding — with no direct user-facing outcome?
    - Tag as `[Enabler]` and link to the SBB they support.
    - Ensure enabler stories still trace to at least one REQ-NNN (e.g. a security requirement).

15. For each story: what are the atomic implementation tasks?
    - Tasks have no IDs; they are bullet points under the story.
    - Example tasks: "Configure backup schedule", "Test restore procedure", "Write runbook"
    - **Anti-pattern check:** If a story reads like a task ("Configure X", "Run Y"), it is not a story — rewrite as actor-goal-benefit or move to Tasks.

### Decision Quality Questions
> Ask these after completing the standard Phase E questions. Phase E converts gaps and decisions into work packages — evidence-gating and PAD resolution are critical here.

1. **[DECISION]** Are all PAD-NNN entries from earlier phases either resolved or linked to a work package? List any open PADs with expired target dates.
2. **[DECISION]** For each work package: what evidence must be gathered before it starts? Is the evidence status sufficient, partial, or insufficient?
3. **[DECISION]** Are work packages with insufficient evidence scheduled in Wave 1? If yes, flag as high-risk and require executive sign-off or guardrails.
4. **[DECISION]** What is the decision reversibility of each work package? (High = can reverse with minimal cost; Low = irreversible or expensive.)
5. **[DECISION]** Does every work package advance at least one goal or execute at least one strategy? Orphan work packages create delivery risk — flag them.
6. **[DECISION]** Which transition architectures are deliberate value increments vs. temporary compromises? Document the value delivery mode for each.

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| Goals/strategies addressed by the roadmap | Architecture Roadmap | Strategic Alignment table (G-NNN / OBJ-NNN / STR-NNN / OPP-NNN column) |
| Goals/strategies with no covering WP | Architecture Roadmap | `{{unaddressed_items}}` |
| Goals/strategies per work package | Architecture Roadmap | WP table `{{g_obj_ids}}` / `{{str_ids}}` per WP |
| Opportunities per work package | Architecture Roadmap | WP table Strategic Alignment (OPP-NNN) |
| Priority capability gaps | Architecture Roadmap | `{{priority_gaps}}` |
| WP resource requirements | Architecture Roadmap | WP `Resources Required` + `Capacity note` fields |
| In-flight projects | Architecture Roadmap | `{{existing_projects}}` |
| Investment budget | Architecture Roadmap | `{{investment_budget}}` |
| Target timeline | Architecture Roadmap | `{{delivery_timeline}}` |
| Sequencing dependencies | Architecture Roadmap | `{{sequencing_dependencies}}` |
| Acceptable transition states | Architecture Roadmap | `{{transition_states}}` |
| Minimum viable delivery | Architecture Roadmap | `{{minimum_viable_scope}}` |
| Delivery risks | Architecture Roadmap | `{{delivery_risks}}` |

**Facilitation Notes:**
- **Always anchor to Phase A Goals first.** Without this, prioritisation defaults to loudest voice or easiest wins rather than strategic intent. If the Architecture Vision is incomplete or has no Goals defined, flag this as a blocker and recommend completing §5–§10 before proceeding.
- The Strategic Alignment table in the roadmap must have every G-NNN and STR-NNN from Phase A appear at least once. Anything missing is an explicit coverage gap.
- The "halved budget" question is the most powerful prioritisation tool — framing it as "which Goals do we protect?" makes the trade-off explicit and strategic rather than tactical.
- In-flight project alignment is frequently underestimated; request a project portfolio list before the session and map conflicts in advance.
- Sequencing questions work well as a group exercise where participants physically order work packages — disagreements in the room are better surfaced now than during delivery.
- Acceptable transition states define architecture checkpoints; if the organisation cannot articulate them, the roadmap will lack governance anchors.

**§D Diagrams — ask at close of session:**
> "One diagram is essential for Phase E. Would you like to create it now?"
- **Architecture Roadmap (Gantt)** — work packages sequenced into delivery waves with timeline (`architecture-roadmap-gantt.mmd`)
- **Gap Heat Map** *(optional)* — visual prioritisation of gaps by impact and effort (`gap-analysis-heat-map.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Architecture Roadmap frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase E? (y/n)"

**SABSA focus:** Component — security gap analysis and work package sequencing

1. What security gaps have been identified against the target architecture?
2. Which security work packages are highest priority — what cannot go live without being addressed?
3. Are there security dependencies that constrain the roadmap sequence? (e.g., IAM must be in place before application migration)
4. What security products or tools are being selected to implement the Physical layer controls?
5. Are any security capabilities being deferred to a later iteration, and is that risk-accepted?

**Output routing:**
| Answer | Output |
|---|---|
| Security gaps | Gap Analysis (security gaps section) |
| Security work packages | Architecture Roadmap (WP-NNN type:security) |
| Security dependencies | Architecture Roadmap (sequencing notes) |

---
