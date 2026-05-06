# Advanced Architecture Patterns

Seven patterns that consistently appear in high-performing architecture functions. These are not standard TOGAF patterns — they are practitioner-developed approaches for scaling architecture impact.

Each pattern includes: **what it is**, **when to use it**, **how to implement**, **risks**, and **related tips/tactics/moves**.

---

## Pattern 1: Dual Operating System (Run vs Change)

### What It Is
Separate architecture into two distinct but aligned systems:
- **Run architecture:** Stability, cost optimization, reliability, operational excellence
- **Change architecture:** Innovation, speed, experimentation, transformation

Each has different governance, risk tolerance, metrics, and decision rights.

### When to Use It
- Organization has both legacy systems (must not break) and innovation initiatives (must move fast)
- Governance conflicts arise because "run" and "change" have incompatible risk profiles
- Architecture team is pulled between "keep the lights on" and "drive transformation"
- Common in: large enterprises, regulated industries, organizations with 15+ year legacy estates

### How to Implement
1. **Define the boundary:** Which systems are "run" (stable, low-risk, cost-optimized) vs "change" (innovating, higher-risk, speed-optimized)
2. **Separate governance:** Run governance = strict compliance, change governance = guardrails + autonomy
3. **Separate metrics:** Run = uptime, cost per transaction, MTTR; Change = time-to-market, experiment velocity, adoption rate
4. **Shared principles:** Both systems align on enterprise principles (security, data sovereignty) but interpret them differently
5. **Transition rules:** Define how a system moves from "change" to "run" (stabilization criteria)

### Risks
- **Silo creation:** Run and change teams stop communicating
- **Resource contention:** Both systems compete for the same architects and budget
- **Boundary ambiguity:** Systems in the middle are neglected
- **Cultural divide:** "Run" teams seen as conservative, "change" teams as reckless

### Related Content
- Tips: #21 (lightweight governance), #24 (guardrails), #41 (embed architects)
- Tactics: P2 (architecture services with SLAs), D2 (golden paths)
- Moves: #1 (federated architecture), #3 (reusable assets)

---

## Pattern 2: Architecture as Product

### What It Is
Treat architecture assets (capability maps, standards, reference architectures, roadmaps) as products with:
- Owners (product managers)
- Consumers (delivery teams, executives, compliance)
- Backlogs (enhancements, feedback, defects)
- Adoption metrics (usage, satisfaction, time-to-value)
- Lifecycle (create → launch → maintain → retire)

### When to Use It
- Architecture assets exist but are rarely used or referenced
- Delivery teams bypass architecture because assets are hard to find or understand
- Architecture team produces outputs but has no feedback loop
- Common in: mature EA functions, organizations with large architecture repositories

### How to Implement
1. **Catalog assets:** List all architecture assets (maps, standards, patterns, roadmaps)
2. **Identify consumers:** For each asset, define who uses it and for what purpose
3. **Assign owners:** Each asset has a named owner responsible for currency and usability
4. **Define adoption metrics:** Usage rate, time saved, decision quality improvement
5. **Create feedback channels:** Teams can suggest improvements, report outdated content, request new assets
6. **Prune ruthlessly:** Retire assets with low adoption; invest in high-value ones

### Risks
- **Product overhead:** Architecture team spends more time managing products than doing architecture
- **Consumer confusion:** Too many "products" fragments the architecture message
- **Quality degradation:** Rush to launch assets before they are robust enough
- **Measurement gaming:** Optimizing adoption metrics rather than decision quality

### Related Content
- Tips: #43 (reference architectures accelerate), #47 (co-create with engineers)
- Tactics: P2 (architecture services with SLAs), B2 (differentiate vs commodity)
- Moves: #3 (reusable assets), #4 (knowledge graph)

---

## Pattern 3: Intent-Based Architecture

### What It Is
Instead of prescribing exact solutions, define **intent + constraints**:
- **Intent:** What the system must achieve (performance, resilience, security posture)
- **Constraints:** Non-negotiable boundaries (compliance, interoperability, data ownership)
- **Freedom:** Teams choose how to satisfy intent within constraints

### When to Use It
- Organization wants to enable team autonomy without sacrificing enterprise coherence
- Technology landscape is too diverse for one-size-fits-all standards
- Innovation is suppressed by overly prescriptive architecture
- Common in: cloud-native organizations, microservices environments, platform teams

### How to Implement
1. **Replace "shall use X" with "shall achieve Y":**
   - Bad: "Use Kafka for all event-driven systems"
   - Good: "Event-driven systems must handle >10k events/sec with <200ms latency and decoupled producers/consumers"
2. **Define constraint categories:** Security, data, compliance, observability, resilience
3. **Create "fitness functions":** Automated checks that verify intent is met (see Pattern #5)
4. **Document exemplars:** Show how teams have satisfied intent in different ways
5. **Review exceptions:** Track and learn from teams that needed different solutions

### Risks
- **Ambiguity:** Teams interpret intent differently, leading to inconsistency
- **Constraint gaps:** Important boundaries are missed, creating downstream integration pain
- **Fitness function complexity:** Automated checks become so complex they constrain creativity
- **Governance erosion:** Without clear accountability, teams ignore intent entirely

### Related Content
- Tips: #22 (principles as constraints), #49 (balance intentional/emergent)
- Tactics: D1 (standardize for leverage), D2 (golden paths)
- Moves: #6 (decision frameworks), #8 (reversible decisions)

---

## Pattern 4: Option Architecture (Real Options Thinking)

### What It Is
Design architectures that preserve future flexibility by:
- Abstracting vendor lock-in behind interfaces
- Using modular domain boundaries
- Delaying irreversible commitments until uncertainty is reduced
- Treating future flexibility as an asset with value

### When to Use It
- Technology or market uncertainty is high
- Long-term commitments (vendor selection, platform choice) have high switching costs
- Organization needs to experiment before committing
- Common in: emerging technology adoption, M&A integration, multi-cloud strategies

### How to Implement
1. **Identify irreversible decisions:** Which choices are hard or expensive to undo?
2. **Abstract behind interfaces:** Use APIs, adapters, and abstraction layers to decouple from specific implementations
3. **Define "option points":** Explicit decision points where the organization can choose a different path
4. **Quantify option value:** Use real options valuation (or simpler cost-of-delay) to justify flexibility investments
5. **Review options regularly:** At each phase gate, reassess whether options are still valuable

### Risks
- **Over-engineering:** Excessive abstraction adds complexity without proportional value
- **Analysis paralysis:** Teams avoid committing because they want to preserve options
- **Interface drift:** Abstractions become outdated and create their own lock-in
- **Cost of flexibility:** Preserving options has a real cost (development, maintenance, performance)

### Related Content
- Tips: #14 (ABB to SBB), #19 (independently valuable increments)
- Tactics: E5 (expose trade-offs), F5 (maintain flexibility)
- Moves: #6 (decision frameworks), #8 (reversible decisions), #10 (irreversible vs reversible)

---

## Pattern 5: Architecture Fitness Functions

### What It Is
Borrowed from evolutionary architecture: define automated checks that verify architectural intent is preserved as the system evolves. Examples:
- Latency thresholds (e.g., API response <200ms p99)
- Coupling limits (e.g., no more than 5 downstream dependencies per service)
- Security constraints (e.g., all APIs authenticated, no secrets in code)
- Resilience checks (e.g., circuit breaker present, retry logic configured)
- Data ownership rules (e.g., each domain owns its master data)

### When to Use It
- Organization has defined architecture intent but struggles to maintain it over time
- Manual architecture reviews do not scale
- Delivery velocity creates "architecture drift" (teams bypass standards under pressure)
- Common in: high-velocity delivery environments, microservices, CI/CD-heavy organizations

### How to Implement
1. **Codify architecture intent:** Convert principles and standards into measurable thresholds
2. **Embed in pipelines:** Add fitness function checks to build, test, and deployment pipelines
3. **Start small:** Begin with 3–5 high-impact checks, then expand
4. **Make visible:** Dashboard fitness function results so teams can see architectural health
5. **Evolve:** Update thresholds as architecture intent evolves (do not let them become static)

### Risks
- **False security:** Teams assume fitness functions catch everything; they do not
- **Threshold gaming:** Teams optimize for passing checks rather than architectural quality
- **Maintenance burden:** Fitness functions require ongoing engineering investment
- **Brittleness:** Overly rigid thresholds block legitimate exceptions

### Related Content
- Tips: #21 (lightweight governance), #27 (DevSecOps), #48 (fitness functions)
- Tactics: G2 (automated checks), D3 (observability)
- Moves: #15 (benefits realization), #17 (systemic risk)

---

## Pattern 6: Capability Heatmap → Investment Engine

### What It Is
Use the Capability Model and Gap Analysis not just to document what exists, but to **drive investment prioritization**:
- Heatmap capabilities by maturity (Absent → Immature → Developing → Mature)
- Overlay strategic importance (differentiating vs commodity)
- Identify high-importance, low-maturity capabilities as priority investment targets
- Feed directly into Architecture Roadmap work packages and funding requests

### When to Use It
- Architecture has a capability map but it is not used to influence budgets
- Investment decisions are made without reference to capability gaps
- Multiple initiatives compete for funding without a clear prioritization framework
- Common in: organizations with large transformation budgets, portfolio management offices

### How to Implement
1. **Create the heatmap:** Map all L1/L2 capabilities with maturity + strategic importance
2. **Define "must-fix" zones:** High importance + low maturity = immediate investment
3. **Link to work packages:** Each priority capability gap becomes one or more WP-NNN entries
4. **Align to funding:** Present heatmap in portfolio review meetings as evidence for investment
5. **Track over time:** Update maturity scores quarterly to show progress

### Risks
- **Measurement subjectivity:** Maturity scores are often judgment-based and politically sensitive
- **Static heatmap:** Teams create the heatmap once and never update it
- **Investment gaming:** Business units inflate capability importance to attract funding
- **Narrow focus:** Heatmap prioritization ignores non-capability drivers (regulatory, market)

### Related Content
- Tips: #4 (capability-based planning), #8 (value streams), #33 (visuals)
- Tactics: B1 (capabilities to value streams), B2 (differentiate vs commodity)
- Moves: #11 (unit economics), #14 (TCO optimization)

---

## Pattern 7: Fracture Plane Design

### What It Is
Design systems along natural "break lines" that align with:
- Business domains (bounded contexts)
- Team boundaries (Conway's Law)
- Data ownership (master data per domain)
- Deployment independence (each plane can be released separately)

If architecture and org structure misalign, you get friction, duplication, and delays.

### When to Use It
- Monolithic systems are being decomposed
- Multiple teams are contributing to the same codebase
- Deployment coordination is a major bottleneck
- Common in: microservices adoption, platform engineering, org restructuring

### How to Implement
1. **Map business domains:** Identify bounded contexts using domain-driven design techniques
2. **Align teams to domains:** Each team owns one domain end-to-end (data, logic, API)
3. **Define interfaces:** Contracts between domains (APIs, events, data schemas)
4. **Enforce boundaries:** Use fitness functions to prevent cross-domain coupling
5. **Evolve planes:** As business domains change, re-evaluate fracture plane boundaries

### Risks
- **Over-decomposition:** Too many small services creates operational overhead
- **Interface brittleness:** Contracts between domains become hard to change
- **Org resistance:** Teams do not want to give up ownership of shared components
- **Performance:** Cross-domain calls introduce latency

### Related Content
- Tips: #20 (viewpoints deliberately), #43 (reference architectures), #47 (co-create with engineers)
- Tactics: C4 (domain-oriented architectures), C5 (clear boundaries)
- Moves: #18 (fragile components), #19 (limit integration points)

---

## Pattern Selection Guide

| Problem | Pattern | Quick Test |
|---|---|---|
| Governance is too slow and bottlenecks delivery | #1 Dual OS | Do "run" and "change" systems have incompatible risk profiles? |
| Architecture assets are produced but not used | #2 Architecture as Product | Can you name the top 3 most-used architecture assets? |
| Standards are too prescriptive and stifle innovation | #3 Intent-Based | Are standards framed as "achieve Y" or "use X"? |
| Technology uncertainty is high; commitments are premature | #4 Option Architecture | Which decisions are irreversible and when must they be made? |
| Architecture intent erodes over time despite reviews | #5 Fitness Functions | Are architecture constraints checked automatically in pipelines? |
| Capability map exists but does not influence investment | #6 Capability Heatmap | Did the last portfolio review reference capability maturity scores? |
| Monolithic systems create coordination bottlenecks | #7 Fracture Planes | Can teams deploy independently without cross-team coordination? |

---

*See also: `practitioner-tips.md` for the 50 tips and 70 deep tactics, `adm-maturity-model.md` for maturity assessment, `failure-modes.md` for common traps.*
