# Elite Architect Day-to-Day Playbook

What distinguishes elite architects from framework-compliant practitioners is not knowledge of TOGAF phases — it is how they spend their time, make decisions, and influence outcomes.

This playbook captures observable behaviors, mental models, and daily habits of high-impact architects. Use it for self-assessment, team coaching, and interview preparation.

---

## Decision Habits

### Spend 70% of time on conversations, 30% on artifacts
Elite architects do not produce more documents — they produce better decisions. Their time is spent:
- Facilitating trade-off discussions
- Building coalitions and resolving conflicts
- Coaching teams on architectural thinking
- Reviewing high-blast-radius decisions

**Self-assessment:** Track your time for one week. If artifacts exceed 50%, you are likely operating at L1–L2 maturity.

### Focus on the 10% of decisions that drive 90% of outcomes
Not all architecture decisions are equal. Elite architects identify:
- **Irreversible decisions** (hard to undo: vendor lock-in, data model choices)
- **High-blast-radius decisions** (affect multiple teams or systems)
- **Cross-domain coupling points** (where boundaries are most fragile)

They invest disproportionate effort in these decisions and delegate the rest.

**Self-assessment:** For your last 20 decisions, which 2 would you redo if you had the chance? Those are your high-impact decisions.

### Make trade-offs visible, not hidden
Elite architects do not present "perfect" solutions. They explicitly state:
- What was traded away
- What risks were accepted
- What assumptions were made
- What would change the decision

**Self-assessment:** In your last architecture review, did you present trade-offs before stakeholders asked for them?

### Prefer reversible decisions when uncertainty is high
When facing uncertainty, elite architects:
- Delay irreversible commitments
- Abstract behind interfaces to preserve optionality
- Design modular boundaries so components can be replaced
- Quantify the cost of flexibility vs the cost of premature commitment

**Self-assessment:** Of your last 10 major decisions, how many are reversible within 6 months?

---

## Interface Control

### Control interfaces, not implementations
Elite architects focus their authority on:
- **API contracts** (what services promise to each other)
- **Data boundaries** (who owns what data, how it flows)
- **Integration patterns** (sync vs async, event-driven vs request-response)
- **Observability contracts** (what metrics and logs are required)

They let teams own implementation details within these boundaries.

**Self-assessment:** Can you draw the integration diagram for your domain from memory? If not, you do not control the interfaces.

### Design for graceful degradation, not just peak performance
Elite architects ask: "What happens when this component fails?" They design:
- Circuit breakers and bulkheads
- Fallback paths and degraded modes
- Clear failure signals and recovery procedures
- Resilience as a first-class concern, not an afterthought

**Self-assessment:** For your top 5 critical paths, have you documented the failure mode and recovery procedure?

---

## Systems Thinking

### Ask: "What does this decision do to the system as a whole?"
Elite architects constantly zoom out. Before approving a change, they trace:
- Which other systems are affected?
- Which teams need to coordinate?
- What assumptions are being made about other components?
- What happens if this assumption is wrong?

**Self-assessment:** For your last decision, did you identify all downstream dependencies before committing?

### Treat simplicity as a strategic objective
Elite architects aggressively:
- **Remove components** that do not justify their existence
- **Reduce dependencies** between systems
- **Eliminate duplication** across teams
- **Question complexity** rather than accepting it

Complexity is treated as a liability, not a sign of sophistication.

**Self-assessment:** In the last 6 months, have you retired or consolidated any systems? If not, complexity is likely growing unchecked.

### Monitor leading indicators, not just lagging outcomes
Elite architects track:
- **Decision latency** (how long to resolve architecture questions)
- **Technical debt velocity** (is debt growing or shrinking?)
- **Integration point count** (more points = more risk)
- **Pattern reuse rate** (are teams using reference architectures?)

They use these to trigger mini-ADM cycles before problems become crises.

**Self-assessment:** Do you have a dashboard showing at least 3 leading indicators of architecture health?

---

## Influence Without Authority

### Build credibility through delivery impact, not job title
Elite architects earn influence by:
- Delivering measurable outcomes (speed, cost, quality improvements)
- Making teams' lives easier, not harder
- Being the person who resolves ambiguity, not creates it
- Showing up when things go wrong, not just when things are reviewed

**Self-assessment:** When was the last time a delivery team sought your input voluntarily?

### Use informal networks to drive adoption
Formal governance moves slowly. Elite architects also operate through:
- **Lunch-and-learns** and informal knowledge sharing
- **Pairing with engineers** on design decisions
- **Slack/Teams channels** for quick architecture advice
- **Communities of practice** for pattern dissemination

**Self-assessment:** Can you name 5 informal contacts who would champion your architecture decisions?

### Make architecture visible and accessible
Elite architects democratize architecture:
- Capability maps are interactive and searchable
- Standards are documented with "why" not just "what"
- Architecture decisions are published with rationale
- Diagrams are updated in real time, not annually

**Self-assessment:** Can a new engineer find and understand your architecture standards in under 30 minutes?

---

## Architecture Shaping Organization Design

### Influence team structures, not just system structures
Elite architects recognize that Conway's Law is not a constraint — it is a lever. They:
- Align team boundaries with system boundaries (fracture planes)
- Advocate for team restructuring when architecture and org misalign
- Design for the teams you have, not the teams you wish you had
- Co-evolve architecture and organizational design

**Self-assessment:** Have you ever proposed an organizational change (team split/merge) based on architecture needs?

### Reward alignment with architecture, not just delivery speed
Elite architects work with leadership to ensure:
- Performance reviews include architecture alignment
- Teams are recognized for reducing technical debt, not just shipping features
- Architecture champions are promoted and retained
- Shadow IT and bypass behavior has consequences

**Self-assessment:** Does your organization formally recognize teams that align with architecture?

---

## Daily Habits Checklist

| Habit | Elite Behavior | L1–L2 Behavior |
|---|---|---|
| Morning priority | Review decision queue; identify high-blast-radius items | Review document backlog; prioritize artifact completion |
| Meeting default | Facilitate trade-offs; coach teams; resolve ambiguity | Present documents; seek approvals; enforce standards |
| Response to resistance | "What concern are we not addressing?" | "This is the standard; comply or escalate" |
| Approach to new technology | "What optionality does this preserve or destroy?" | "Is this on the approved list?" |
| Review focus | Interfaces, contracts, blast radius | Implementation details, syntax, naming |
| Success metric | Decision quality, delivery outcomes | Artifact completeness, checklist compliance |
| Relationship with delivery | Embedded partner | External reviewer |
| Handling uncertainty | Preserve reversibility, abstract behind interfaces | Specify exact solutions prematurely |
| Communication style | Trade-offs explicit, visuals over prose, stories over frameworks | Framework-heavy, assumption-heavy, detail-heavy |
| Attitude to standards | Prune actively, justify each standard's existence | Accumulate standards, rarely retire |

---

## Self-Assessment: Are You Operating at Elite Level?

Score yourself 1–5 on each dimension:

1. **Decision Focus:** Do you spend more time on conversations than documents?
2. **Economic Literacy:** Can you articulate architecture value in financial terms?
3. **Systems Thinking:** Do you trace downstream effects before committing?
4. **Simplicity:** Have you removed or simplified something in the last quarter?
5. **Influence:** Do delivery teams seek your input voluntarily?
6. **Visibility:** Is your architecture discoverable and understandable?
7. **Org Design:** Have you influenced team structure based on architecture?
8. **Metrics:** Do you track leading indicators of architecture health?
9. **Feedback:** Do you know which of your past decisions were correct?
10. **Learning:** Are you continuously updating your mental models?

**Scoring:**
- 40–50: Elite practitioner (L4–L5)
- 30–39: Advanced practitioner (L3–L4)
- 20–29: Competent practitioner (L2–L3)
- 10–19: Framework-compliant (L1–L2)
- <10: Needs development focus

---

*See also: `practitioner-tips.md` for the 50 tips and 70 deep tactics, `adm-maturity-model.md` for team maturity assessment, `failure-modes.md` for common traps.*
