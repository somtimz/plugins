# Part III: Cross-Cutting Expert Moves


### Operating Model & Scaling (Moves 1–5)

**Move 1:** Move from centralized EA to federated architecture (enterprise + domain architects).  
**Move 2:** Define clear interaction models between EA, solution architects, and teams.  
**Move 3:** Scale via reusable assets (reference architectures, patterns, playbooks).  
**Move 4:** Treat architecture repository as a knowledge graph, not a document store.  
**Move 5:** Invest in internal enablement (training, communities of practice).

### Decision Science (Moves 6–10)

**Move 6:** Use decision frameworks (e.g., cost of delay, real options) to guide trade-offs.  
**Move 7:** Quantify uncertainty — don’t hide it behind diagrams.  
**Move 8:** Prefer reversible decisions when uncertainty is high.  
**Move 9:** Track decision outcomes to improve future judgment.  
**Move 10:** Separate irreversible vs reversible decisions in governance.

### Economics & Value Realization (Moves 11–15)

**Move 11:** Tie architecture to unit economics (cost per transaction, cost per feature).  
**Move 12:** Make technical debt visible in financial terms.  
**Move 13:** Use FinOps practices to influence architecture choices.  
**Move 14:** Optimize for total cost of ownership, not just build cost.  
**Move 15:** Continuously validate that benefits are actually realized post-implementation.

### Risk & Complexity Management (Moves 16–20)

**Move 16:** Reduce complexity as a primary goal — complexity is the real enemy.  
**Move 17:** Use architecture to actively manage systemic risk (not just document it).  
**Move 18:** Identify "fragile" components and prioritize their redesign.  
**Move 19:** Limit integration points — each one is a risk multiplier.  
**Move 20:** Design for graceful degradation, not just peak performance.

### Culture & Influence (Moves 21–25)

**Move 21:** Build credibility through delivery impact, not authority.  
**Move 22:** Use informal networks to drive adoption faster than formal governance.  
**Move 23:** Reward teams for alignment with architecture, not just delivery speed.  
**Move 24:** Make architecture visible and accessible — democratize it.  
**Move 25:** Continuously refine your influencing skills — architecture is a social discipline.

**Move 26:** Use the Decide vs Defer Matrix — Evidence × Reversibility × Impact × Urgency × Capability — to time every architecture decision correctly.

- **Evidence:** What data, experiment, or proof supports this choice? (Sufficient / Partial / Insufficient)
- **Reversibility:** Can it be undone within 6 months without major cost? (High / Medium / Low)
- **Impact:** If wrong, how many teams or systems are affected? (High / Medium / Low)
- **Urgency:** Is there a real deadline forcing commitment now? (High / Medium / Low)
- **Capability:** Does the team have the skills to implement and operate? (Yes / Partial / No)

Guidance:
- Evidence + Reversibility = High → Safe to decide now
- Evidence + Reversibility = Low → Defer to PAD-NNN
- Urgency = High + Capability = No → Decide with guardrails and learning plan
- Impact = High + Evidence = Insufficient → Do not commit without POC or spike

**Move 27:** Convert premature decisions to constraint-boundary PADs instead of committed choices.

When a stakeholder insists on a technology or pattern before the right phase:
1. Capture the constraint boundary (what MUST be true, what MUST NOT happen)
2. Document candidate options with preliminary assessment
3. Set an expiry date and resolution path
4. Create the PAD-NNN and link it to the relevant gap or work package
5. Communicate the boundary to delivery teams so they can design within it

This preserves political alignment while protecting architecture integrity.

---
