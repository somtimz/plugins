# Advanced Practitioner Questions by Phase


These questions probe economic reasoning, decision quality, failure mode symptoms, and maturity level. Use them when the engagement is at L3+ or when the stakeholder is a senior practitioner. Mark each as `[ADVANCED]` when presenting.

### Preliminary Phase — Advanced
1. **[ADVANCED]** How is the architecture capability funded — as a persistent operating cost or as project overhead? (Tests Failure Mode 2: Centralized Bottleneck)
2. **[ADVANCED]** What percentage of architecture team time is spent on conversations vs. document production? (Elite habit: 70/30 rule)
3. **[ADVANCED]** What is the average decision latency for architecture questions — and what is the target? (Tests maturity L3+ indicator)
4. **[ADVANCED]** How are architecture standards maintained — as a static document or as a product with owners, consumers, and adoption metrics? (Tests advanced pattern: Architecture as Product)
5. **[ADVANCED]** What happens to a project that does not comply with architecture standards? (Tests Failure Mode 3: Fake Governance)

### Phase A — Advanced
1. **[ADVANCED]** Can you quantify the gap between current and desired state in economic terms (cost, risk, revenue)? (Deep tactic: strategic tension)
2. **[ADVANCED]** Have you built multiple candidate visions and evaluated trade-offs between them? (Deep tactic: multiple visions)
3. **[ADVANCED]** What are the success metrics that must be met before this vision is approved to proceed to Phase B? (Deep tactic: success metrics before B)
4. **[ADVANCED]** Who has co-created this vision with business leaders — and who has not been consulted? (Hidden mechanic: vision as negotiation tool)
5. **[ADVANCED]** If the full vision cannot be delivered, what is the minimum viable vision that still justifies the investment? (Pattern: Option Architecture)

### Phase B — Advanced
1. **[ADVANCED]** For each capability: is it differentiating (competitive advantage) or commodity (should be standardized)? (Deep tactic: differentiate vs commodity)
2. **[ADVANCED]** How is each capability linked to a value stream and a KPI or revenue/cost driver? (Deep tactic: capability-value stream-KPI linkage)
3. **[ADVANCED]** Does the current org design support the target capability model — or does the org need to change? (Deep tactic: challenge org design)
4. **[ADVANCED]** Where is the business ambiguous — and how does this architecture compress that ambiguity into coherent constraints? (Hidden mechanic: compression function)
5. **[ADVANCED]** Have you identified "where to play" and "how to win" — or only mapped processes? (Deep tactic: strategic focus)

### Phase C — Advanced
1. **[ADVANCED]** Is data treated as a product with ownership, quality SLAs, and lifecycle governance? (Deep tactic: data as product)
2. **[ADVANCED]** Are API contracts and event schemas defined before tools are selected? (Deep tactic: interoperability early)
3. **[ADVANCED]** What measurable criteria will be used to rationalize applications — cost, risk, duplication, or just age? (Deep tactic: rationalize with metrics)
4. **[ADVANCED]** Do data and application boundaries align with business domains? (Pattern: Fracture Planes)
5. **[ADVANCED]** Who owns each critical data domain — and what happens when ownership is ambiguous? (Hidden mechanic: data as power structure)
6. **[ADVANCED]** Are ABBs defined before any vendor or product is named? (Tests vendor-first anti-pattern)
7. **[ADVANCED]** Can every ABB trace to at least one REQ-NNN and one CAP-NNN? (Tests ABB validation)

### Phase D — Advanced
1. **[ADVANCED]** Are technology standards core (mandatory enterprise-wide) or flexible (domain-specific)? Is there a defined flexible zone? (Deep tactic: standardize for leverage)
2. **[ADVANCED]** Are there pre-approved golden paths that teams can adopt without central review? (Deep tactic: golden paths)
3. **[ADVANCED]** Is observability and resilience embedded in technology standards from day one? (Deep tactic: design for failure)
4. **[ADVANCED]** How is cloud adoption changing team structures, funding, and decision rights — not just hosting? (Deep tactic: cloud as operating model)
5. **[ADVANCED]** Do standards have consumers, owners, and adoption metrics — or are they static documents? (Hidden mechanic: standards as product)
6. **[ADVANCED]** Is every SBB selected against a defined ABB, or are products chosen before logical components are named? (Tests vendor-first anti-pattern)
7. **[ADVANCED]** For each SBB: what is the exit cost and timeline if the vendor relationship fails? (Tests lock-in awareness)
8. **[ADVANCED]** Are fitness functions or conformance tests defined for each SBB before procurement? (Tests T4-FITNESS compliance)

### Phase E — Advanced
1. **[ADVANCED]** Does every work package deliver measurable business value, not just close a technical gap? (Deep tactic: value increments)
2. **[ADVANCED]** How are work packages prioritized — by impact, by feasibility, or by loudest voice? (Deep tactic: impact × feasibility)
3. **[ADVANCED]** What are the realistic transition architectures between baseline and target — not just the ideal end state? (Deep tactic: transition architectures)
4. **[ADVANCED]** What trade-offs are explicit in the roadmap — what is deferred and what is the risk of deferral? (Deep tactic: expose trade-offs)
5. **[ADVANCED]** If the budget were halved, which goals and work packages would you protect? (Tests economic reasoning)
6. **[ADVANCED]** Does every story trace to at least one REQ-NNN and one SBB-NNN? (Tests story traceability)
7. **[ADVANCED]** Are enabler stories explicitly tagged and linked to architectural runway requirements? (Tests architectural runway visibility)
8. **[ADVANCED]** Is each story decomposable into 2–5 tasks, or are stories too large (epic-sized) or too small (task-level)? (Tests story sizing)

### Phase F — Advanced
1. **[ADVANCED]** Is benefits realization tracked per wave — and how is it measured? (Deep tactic: optimize for value delivery)
2. **[ADVANCED]** What is the risk exposure per migration wave — what breaks if a wave fails? (Deep tactic: risk exposure)
3. **[ADVANCED]** Are there clear exit criteria for legacy systems — without which they will live forever? (Deep tactic: legacy exit criteria)
4. **[ADVANCED]** Does the plan include rollback paths and off-ramps — or is it all-or-nothing? (Deep tactic: maintain flexibility)
5. **[ADVANCED]** Can the migration plan articulate value in financial terms (TCO, cost of change, risk reduction) to finance? (Tests Failure Mode 4: Misalignment with Finance)

### Phase G — Advanced
1. **[ADVANCED]** Is governance provided through embedded guidance or remote review? (Deep tactic: embedded guidance)
2. **[ADVANCED]** Are conformance checks automated in CI/CD, or does every deployment wait for manual approval? (Deep tactic: automated checks)
3. **[ADVANCED]** Is governance effort focused on high-risk, irreversible decisions — or does it review everything? (Deep tactic: focus on high-risk)
4. **[ADVANCED]** Are deviations accepted (with risk sign-off) or remediated — not just documented? (Deep tactic: track deviations)
5. **[ADVANCED]** How is governance measured — by decision speed and delivery outcomes, or by checklist coverage? (Deep tactic: measure by outcomes)

### Phase H — Advanced
1. **[ADVANCED]** Is the target architecture updated continuously, or only during major projects? (Deep tactic: living system)
2. **[ADVANCED]** What leading indicators are tracked to trigger mini-ADM cycles before crises emerge? (Deep tactic: leading indicators)
3. **[ADVANCED]** Are obsolete architectures retired explicitly, or do they linger indefinitely? (Deep tactic: retire obsolete)
4. **[ADVANCED]** Are implementation learnings fed back into principles, standards, and reference architectures? (Deep tactic: feed learnings back)
5. **[ADVANCED]** How often does the architecture team run mini-ADM cycles for incremental change? (Tests maturity L5 indicator)