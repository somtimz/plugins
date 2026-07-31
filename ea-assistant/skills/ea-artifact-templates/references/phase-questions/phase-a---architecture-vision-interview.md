# Phase A — Architecture Vision Interview


**Goal:** Define scope, concerns, high-level target, and cross-domain goals

**ID Scheme Reference:**

| Prefix | Concept | Example | Linked To |
|---|---|---|---|
| DRV-NNN | Business Driver | DRV-001 | — (root cause of engagement) |
| G-NNN | Goal | G-001 | DRV-NNN (responds to driver) |
| OBJ-NNN | Objective | OBJ-001 | G-NNN (operationalises goal) |
| ISS-NNN | Issue | ISS-001 | G-NNN (threatens goal) |
| PRB-NNN | Problem | PRB-001 | OBJ-NNN (blocks objective) |
| STR-NNN | Strategy | STR-001 | G-NNN (approach to achieve goal) |
| MET-NNN | Metric | MET-001 | OBJ-NNN (measures objective) |
| OPP-NNN | Opportunity | OPP-001 | DRV-NNN + G-NNN (specific possibility to exploit) |

Assign IDs sequentially within each prefix as responses are confirmed. Record IDs in the Architecture Vision template and in `engagement.json` where applicable.

**Key questions:**

*§2 Business Drivers — the forces making this engagement necessary:*
1. What external forces (market shifts, regulatory changes, competitive pressure, technology change) are creating pressure to act now?
2. What internal forces (cost pressure, strategic mandate, leadership change, capability gap) are pushing this engagement forward?
3. For each driver: is it an opportunity to exploit, a threat to respond to, or a mandate to comply with?

*§3 Goals — the broad outcomes the strategy must achieve:*
4. Given those drivers, what are the high-level outcomes this engagement must achieve? Capture each as a goal: a qualitative statement of a desired future state — no numbers or deadlines required at this level. (e.g. "Become a trusted custodian of customer data", "Achieve highly reliable platform operations")
   - If a response includes a specific number or deadline, it is an **Objective** — note it and handle in the next step.
   - If it describes an approach ("adopt cloud-first"), it is a **Strategy** — note it and record separately.
   - **Layer test:** If the stated goal is about governance, standards, or EA capability (e.g., "Establish AI governance", "Define architecture review process"), it is likely an **EA Goal** — capture it separately for the Governance Framework or Architecture Principles, not as a Business Goal in the Architecture Vision. See [Two Layers of Intent](../two-layers-of-intent.md).
   - Assign each confirmed goal a G-NNN ID and note which driver(s) it responds to.
   - For each goal: in one sentence, why is achieving it important for this engagement specifically? What happens if it is not achieved? (This is the goal's Rationale — captures the consequence of failure.)

*§4 Objectives — the measurable, time-bound results that operationalise each goal:*
5. For each goal captured: what is the specific, measurable result that would prove this goal is being achieved — and by when? (e.g. for "Achieve highly reliable platform operations" → "Reduce unplanned downtime to under 4 hours per quarter by Q4 2026")
   - Each objective must have: a unit of measure, a target value, and a deadline. Push back on any that lack all three.
   - Assign each confirmed objective an OBJ-NNN ID and link it to its parent goal.
6. For each objective: how will you measure progress? What is the current baseline, and where does the data come from? Capture as a performance metric linked to the objective.
   - For goals without a single measure, ask for a leading indicator — capture as an outcome metric.

*§5 Issues — the systemic barriers that threaten goals:*
7. For each goal: what broader, systemic concerns are currently preventing or threatening its achievement? (Patterns of dysfunction, capability gaps, unresolved conflicts — not single broken things.) (e.g. "Weak stakeholder alignment across business units", "Inconsistent data quality across operational systems")
   - Assign each confirmed issue an ISS-NNN ID and link it to the goal(s) it threatens.
   - If a response is too specific and fixable ("error rate is 30%"), it is a **Problem** — note it and handle in the next step.
   - For each issue: what observable signal or event confirms this issue exists? Who raised or first identified it? (Evidence and source — an issue without evidence is an assumption.)

*§6 Problems — the specific, observable symptoms that block objectives:*
8. For each objective: what specific, measurable symptoms are actively blocking or undermining its delivery today? (e.g. "The monthly close process takes 15 days due to manual reconciliation", "Mobile checkout abandonment is 68% — 2× the industry benchmark")
   - Assign each confirmed problem a PRB-NNN ID and link it to the objective(s) it blocks.
   - If a response is too broad and unfixable directly ("we have poor data culture"), it is an **Issue** — move it up.
   - For each problem: what data point, incident, or measurement confirms this symptom is currently active? Who raised or first identified it? (Evidence and source — a problem without evidence cannot be prioritised or verified later.)

*Inter-element connections — run after Issues and Problems are captured:*
> **After Issues:** "Do any of these issues, if resolved, unlock something the organisation could not do before — beyond just removing the barrier? If so, that's an Opportunity — capture it as OPP-NNN."
> **After Problems:** "Does each problem link clearly to an objective it's blocking? Could resolving any of them create a new capability or market possibility worth tracking as an Opportunity?"

*§7 Opportunities — specific, actionable possibilities to exploit:*
9. Given the drivers, goals, and gaps identified: what specific things could this engagement make possible that the organisation cannot currently do? (e.g. "Real-time personalisation using our existing data platform", "Self-service supplier onboarding — currently takes 3 weeks manually")
   - Classify each as: **Exploit** (capitalise on existing advantage), **Enhance** (amplify current capability), or **Emerge** (something not previously in scope).
   - Assign each confirmed opportunity an OPP-NNN ID and link it to the driver(s) and goal(s) it advances.
   - An opportunity must advance at least one goal. If it advances no goal, either a goal is missing or the item is not architecture-relevant.

*Inter-element connections — run after Risks are captured (§15 Key Risks):*
> **After Risks:** "For each Critical or High risk — which goal does it threaten? Link it now (G-NNN). And: does this risk also suggest a defensive opportunity worth capturing as OPP-NNN?"
> **After Metrics:** "For each metric — what is the current baseline? If unknown, flag it as a data gap. An unmeasured baseline is itself a benefits realisation risk."

*§1 Executive Summary / §9 Scope / §10–§16 — scope, constraints, and risks:*
10. What does success look like at the end of this engagement? → §1 Executive Summary
11. Who are the key stakeholders and what are their primary concerns? → §10 Stakeholders + Stakeholder Map
12. What is explicitly in scope and out of scope for this engagement? → §9 Scope
13. What known constraints or assumptions should be documented upfront? → §12 Constraints + §13 Assumptions
14. What existing architecture assets, decisions, or documents are relevant? → Statement of Architecture Work §3
15. What is the desired timeline for completing this work? → §9 Scope (Time Horizon) + SoAW
16. What are the biggest risks that could derail this engagement? → §15 Key Risks

### Decision Quality Questions
> Ask these after completing the standard Phase A questions. Phase A is for directional choices only — any specific technology or pattern commitment is premature.

1. **[DECISION]** Have any specific technology choices, vendor selections, or implementation patterns been proposed in this phase? If yes, flag as premature and convert to PAD-NNN with constraint boundaries.
2. **[DECISION]** For each strategy (STR-NNN): what evidence would be required before it can be treated as a committed decision rather than a directional hypothesis?
3. **[DECISION]** Is there stakeholder pressure to make specific technology commitments now? What is the defensible governance position if challenged?
4. **[DECISION]** Which decisions made in Phase A should be revisited after Phase B–D analysis? (All technology-specific choices; directional strategies with weak evidence.)

**Output Routing:**

| Response Topic | Target Artifact | Target Field |
|---|---|---|
| External business drivers | Drivers Register (+ engagement.json) | `direction.drivers[]`; Vision §4 summary |
| Internal business drivers | Drivers Register (+ engagement.json) | `direction.drivers[]`; Vision §4 summary |
| Goals | Goals Register + engagement.json | `direction.goals[]`; Vision §5 summary |
| Objectives | Objectives Register + engagement.json | `direction.objectives[]`; Vision §10 summary |
| Systemic issues | Issues Register (+ engagement.json) | `direction.issues[]`; Vision §7 summary |
| Specific problems | Problems Register (+ engagement.json) | `direction.problems[]`; Vision §8 summary |
| Opportunities | Architecture Vision | `§9 Opportunities` (OPP-NNN rows) |
| Performance metrics | engagement.json | `metrics[]` linked to OBJ-NNN |
| Success criteria | Architecture Vision | `§1 Executive Summary` + `§5 Goals` |
| Key stakeholders | Stakeholder Map | `{{stakeholder_list}}` |
| Stakeholder concerns | Stakeholder Map | `{{stakeholder_concerns}}` |
| Strategies | Strategy Register + engagement.json | `direction.strategies[]`; Vision §11 summary |
| Metrics | engagement.json | `§11 Strategic Direction Summary` (MET-NNN rows) + `metrics[]` |
| In-scope items | Architecture Vision | `§2 Scope — {{scope_in}}` |
| Out-of-scope items | Architecture Vision | `§2 Scope — {{scope_out}}` |
| Constraints | Statement of Architecture Work / Constraints Register | `{{constraints}}` + `CST-NNN` via `/ea-constraints` |
| Assumptions | Statement of Architecture Work | `{{assumptions}}` |
| Existing architecture assets | Statement of Architecture Work | `§3 Approach` (reference existing assets as inputs) |
| Timeline | Statement of Architecture Work | `{{timeline}}` |
| Key risks | Architecture Vision | `§16 Key Risks` (summary; full detail in Risk Register) |
| Strategies | engagement.json | `direction.strategies[]` |

**Facilitation Notes:**
- Follow the sequence: Drivers → Goals → Objectives → Issues → Problems. Each layer is easier to articulate once the layer above is established.
- Goals come before objectives. Do not ask for measures until you have a confirmed, classified goal — premature measurement pressure collapses goals into objectives and loses the qualitative anchor.
- When classifying responses: numbers or deadlines → Objective; approaches or choices → Strategy; broad dysfunction → Issue; specific observable symptom → Problem. Reclassify explicitly and confirm with the stakeholder before recording.
- For every Issue, ask "which goal does this threaten?" — if it threatens no goal, either the goal list is incomplete or the issue is not architecture-relevant.
- For every Problem, ask "which objective does this block?" — if it blocks no objective, either the objectives list is incomplete or the problem is out of scope.
- Scope boundary questions often generate the most debate; document disagreements explicitly rather than forcing premature consensus.
- A brief stakeholder RACI draft during this session prevents scope and accountability conflicts later.
- If a driver, issue, or problem needs external validation or deeper investigation, pause and invoke `@research-agent` before recording it as fact. Example: "I'll check the regulatory landscape on that before we lock in DRV-002." Research findings can be pasted directly into brainstorm notes or artifact fields.

**§D Diagrams — ask at close of session:**
> "Two diagrams can make the Architecture Vision immediately clearer for executive stakeholders. Would you like to create either now, or describe what they should show?"
- **Motivation Map** — shows the full DRV → Goal → Strategy chain in one visual (`architecture-vision-motivation-map.mmd`)
- **Stakeholder Power/Interest Grid** — positions each stakeholder by influence and engagement level (`architecture-vision-stakeholder-grid.mmd`)

If the user describes content, offer to launch `/ea-diagram` immediately. Output routing: diagram files → `diagrams/`, filenames added to Architecture Vision frontmatter `diagrams: []`.
See `skills/ea-artifact-templates/references/diagram-catalogue.md` for Mermaid starters.

### Security Questions (optional)
> Offer this section after completing the standard phase questions. Ask: "Would you like to address security concerns for Phase A? (y/n)"

**SABSA focus:** Contextual — security vision, drivers, and top-level risk

1. What are the primary security drivers for this engagement? Are they regulatory, contractual, or risk-driven?
2. Who are the security stakeholders? (CISO, DPO, compliance officer, risk committee, board audit committee)
3. What are the top 3 security risks at the engagement level? What keeps the CISO awake at night?
4. What security principles should constrain all downstream architecture decisions?
5. Is there an existing security architecture or security reference model that this engagement must align with?
6. Are there any known security incidents or breaches in this organisation's recent history that should inform the architecture?

**Output routing:**
| Answer | Output |
|---|---|
| Security drivers | DRV-NNN type:security in Requirements Register |
| Security stakeholders | Stakeholder Map (security authority roles) |
| Top-level security risks | RIS-NNN type:security, category:security in Risk Register |
| Security principles | Architecture Principles (security section) |

---
