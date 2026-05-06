# Architecture Failure Modes at Scale

Six recurring failure modes that undermine TOGAF effectiveness in real organizations. Each includes: **symptoms** (how to spot it), **root cause** (why it happens), **fix** (how to recover), **prevention** (how to avoid it), and **related tips/tactics/moves**.

These are not academic concerns — they are observed patterns in organizations ranging from mid-market to Fortune 50. Use this reference during engagement health checks (`/ea-engage-review`), grill-me sessions (`/ea-grill failure-mode`), and Phase H retrospectives.

---

## Failure Mode 1: The Documentation Trap

### Symptoms
- Architecture repository contains hundreds of artifacts; few are referenced after creation
- Teams produce catalogs, matrices, and viewpoints because they are "required"
- New architects spend weeks reading existing documents before contributing
- Stakeholders cannot name the last architecture document that influenced a decision
- Artifact completeness is celebrated; decision quality is not measured

### Root Cause
The organization confuses *documentation* with *decision support*. Architecture content is produced to satisfy process requirements rather than to shape choices. There is no feedback loop between artifact creation and decision impact.

### Fix
1. **Kill 70% of artifacts:** Audit the repository. Retire anything not referenced in a decision in the last 12 months.
2. **Focus on decisions:** For each remaining artifact, ask: "What decision does this support?" If none, archive it.
3. **Introduce decision logs:** Replace verbose descriptions with A3 Decision Logs that capture who decided what and why.
4. **Measure by decision speed:** Track how long it takes to resolve architecture questions, not how many documents were produced.
5. **Run a "documentation cemetery" purge:** Quarterly, remove obsolete artifacts and notify stakeholders.

### Prevention
- In Preliminary, define a "minimum viable artifact set" for each engagement type
- In `architecture-vision.md`, require every artifact to trace to at least one decision
- In governance, reward decision quality, not document volume
- In Phase H, ask: "Which artifacts actually influenced change?"

### Related Content
- Tips: #2 (decision-support, not documentation), #12 (timebox), #20 (viewpoints deliberately)
- Tactics: P4 (minimal standards catalog), A5 (success metrics before Phase B)
- Moves: #4 (knowledge graph, not document store)

---

## Failure Mode 2: Centralized Bottleneck

### Symptoms
- EA team is overloaded with review requests
- Delivery teams wait weeks for architecture approvals
- Shadow IT emerges as teams bypass architecture to meet deadlines
- Architecture decisions are made by a small group with limited bandwidth
- Domain teams feel architecture is "imposed from above"

### Root Cause
Architecture governance is over-centralized. All meaningful decisions flow through a small architecture authority. The EA team acts as a gatekeeper rather than a decision-support function. There is no distributed decision-making model.

### Fix
1. **Federate decisions:** Define which decisions are enterprise-level (cross-domain, high-cost, irreversible) vs domain-level (local, reversible, low-cost). Push domain decisions to domain architects.
2. **Create guardrails:** Replace approval gates with pre-approved patterns, reference architectures, and automated checks.
3. **Embed architects:** Assign enterprise architects to product teams, not a central pool.
4. **Delegate authority:** Give solution architects authority to approve designs within guardrails.
5. **Track bypasses:** Measure how often teams bypass architecture. If high, your governance is too heavy.

### Prevention
- In Preliminary, define decision rights and escalation paths in `governance-framework.md`
- In `governance-framework.md`, use RACI for architecture decisions
- In Phase G, measure governance by decision speed, not control coverage
- In Phase H, assess whether centralized governance caused delays

### Related Content
- Tips: #21 (lightweight governance), #23 (clear decision rights), #24 (guardrails over gates), #41 (embed architects)
- Tactics: P1 (Architecture Board as marketplace), G1 (embedded guidance)
- Moves: #1 (federated architecture), #2 (interaction models)

---

## Failure Mode 3: Fake Governance

### Symptoms
- Checklists are passed but systems still diverge from architecture
- Compliance assessments find no issues, but post-implementation audits reveal significant gaps
- Architecture Board meetings are performative — decisions are pre-ordained
- Deviations are documented but never remediated
- Governance is seen as "covering ourselves" rather than improving outcomes

### Root Cause
Governance is not tied to consequences. There is no enforcement mechanism, no feedback loop, and no accountability for deviations. Governance activities are designed to produce evidence of compliance, not to ensure actual alignment.

### Fix
1. **Tie governance to funding:** Non-compliant projects lose budget priority. Compliant projects get fast-tracked.
2. **Tie governance to deployment:** Use automated checks in CI/CD to block non-compliant deployments.
3. **Tie governance to risk acceptance:** Deviations require explicit risk acceptance by a named executive.
4. **Make governance visible:** Publish conformance metrics and deviation logs openly.
5. **Replace checklists with outcomes:** Measure whether governance improved delivery outcomes, not whether checklists were completed.

### Prevention
- In `governance-framework.md`, define consequences for non-compliance
- In `implementation-governance-plan.md`, specify automated enforcement mechanisms
- In Phase G, track deviations explicitly and decide: accept or remediate
- In Phase H, assess whether governance actually prevented misalignment

### Related Content
- Tips: #21 (lightweight governance), #27 (DevSecOps), #28 (decision speed), #40 (conformance by outcomes)
- Tactics: G2 (automated checks), G4 (track deviations), G5 (measure by outcomes)
- Moves: #9 (track decision outcomes), #10 (irreversible vs reversible)

---

## Failure Mode 4: Misalignment with Finance

### Symptoms
- "Great architecture" proposals are never funded
- Roadmaps are ignored by portfolio management
- Architecture cannot articulate value in financial terms
- Business cases for architecture initiatives are weaker than competing projects
- CFO views architecture as a cost center, not an investment

### Root Cause
Architecture proposals are framed in technical and framework terms rather than economic terms. The architecture team does not speak the language of finance (cost, risk, return, TCO). Portfolio management cannot compare architecture proposals to other investments.

### Fix
1. **Translate everything into economics:** Every architecture proposal must include cost, risk, and expected return.
2. **Make technical debt visible:** Quantify technical debt in financial terms (interest payments, principal reduction).
3. **Use FinOps practices:** Collaborate with finance to attribute cloud and infrastructure costs to architecture decisions.
4. **Optimize for TCO:** Frame architecture choices in terms of total cost of ownership, not just build cost.
5. **Validate benefits realization:** After implementation, verify that promised benefits were actually achieved.

### Prevention
- In `architecture-vision.md`, quantify business driver impact where possible
- In `architecture-roadmap.md`, show cost/benefit per work package
- In `migration-plan.md`, include benefits realization tracking
- In governance, require economic justification for all architecture decisions

### Related Content
- Tips: #3 (portfolio alignment), #32 (financial language), #45 (migration as product), #50 (delivery outcomes)
- Tactics: B4 (link to KPIs/revenue), F3 (funding cycles), F4 (exit criteria for legacy)
- Moves: #11 (unit economics), #12 (technical debt), #13 (FinOps), #14 (TCO), #15 (benefits realization)

---

## Failure Mode 5: Over-Standardization

### Symptoms
- Innovation slows because teams cannot experiment outside approved technologies
- Teams bypass standards because they are too rigid for domain-specific needs
- "Standard" platforms are forced on teams where they create more problems than they solve
- Architecture team is seen as a barrier to legitimate experimentation
- Standards catalog grows but adoption decreases

### Root Cause
Standards are treated as universally mandatory rather than as guidance with zones of flexibility. The organization has not defined which standards are core (mandatory) vs which are flexible (experimental).

### Fix
1. **Define zones:** Core standards (mandatory, enterprise-wide) vs Flexible zones (domain-specific, experimental)
2. **Create exception processes:** Teams can request exceptions with economic justification
3. **Review standards regularly:** Retire standards that are obsolete or counterproductive
4. **Measure standard value:** Track whether standards actually reduced cost/risk or just created overhead
5. **Promote experimentation:** Allow controlled experiments outside standards with defined success criteria

### Prevention
- In `architecture-principles.md`, distinguish principles (universal) from standards (contextual)
- In `governance-framework.md`, define "flexible zones" explicitly
- In Phase H, feed implementation learnings back into standards pruning
- In `governance-framework.md`, measure standard adoption rate and satisfaction

### Related Content
- Tips: #22 (principles as constraints), #24 (guardrails), #30 (prune obsolete), #49 (balance intentional/emergent)
- Tactics: D1 (standardize for leverage), D2 (golden paths)
- Moves: #8 (reversible decisions), #10 (irreversible vs reversible)

---

## Failure Mode 6: Static Target Architecture Illusion

### Symptoms
- "Future state" architecture is never reached
- Roadmaps are perpetually out of date
- Target architecture becomes a fantasy that nobody believes
- Implementation drifts further from target with each release
- Architecture team spends more time updating target diagrams than guiding delivery

### Root Cause
The organization treats target architecture as a fixed destination rather than a directional instrument. The assumption is that once the target is defined, the organization will converge to it. In reality, enterprises are dynamic systems — market shifts, regulatory changes, and implementation learnings continuously reshape what "target" means.

### Fix
1. **Treat target as directional:** The target is a compass, not a destination. Update it continuously.
2. **Invest in transition architectures:** The path matters more than the destination. Design realistic intermediate states.
3. **Use mini-ADM cycles:** Run lightweight architecture reviews for incremental changes without full phase overhead.
4. **Monitor leading indicators:** Track tech debt, delivery friction, and capability maturity as early warning signals.
5. **Retire obsolete architectures:** When a target is no longer relevant, retire it explicitly rather than letting it linger.

### Prevention
- In `architecture-vision.md`, frame the vision as "directional" not "fixed"
- In `architecture-roadmap.md`, update quarterly, not annually
- In `migration-plan.md`, design for flexibility and include rollback/off-ramp options
- In Phase H, run continuous "mini-ADM cycles" for incremental changes
- In governance, monitor leading indicators rather than just end-state compliance

### Related Content
- Tips: #10 (right problem), #44 (continuous validation), #49 (balance intentional/emergent)
- Tactics: E4 (transition architectures), F5 (maintain flexibility), H1 (living system), H3 (mini-ADM cycles)
- Moves: #4 (knowledge graph), #15 (benefits realization)

---

## Failure Mode Detection Checklist

Use this during `/ea-engage-review` or `/ea-grill failure-mode`:

| Failure Mode | Detection Question | Severity |
|---|---|---|
| Documentation Trap | Can stakeholders name the last architecture document that changed a decision? | Critical if "no" |
| Centralized Bottleneck | How long is the architecture review queue? | Critical if >2 weeks |
| Fake Governance | Are deviations remediated or just documented? | Critical if "just documented" |
| Misalignment with Finance | Can architecture articulate value in $ terms? | Critical if "no" |
| Over-Standardization | Are teams bypassing standards? | Warning if >20% bypass |
| Static Target Illusion | When was target architecture last updated? | Warning if >6 months |

---

*See also: `practitioner-tips.md` for the 50 tips and 70 deep tactics, `adm-maturity-model.md` for maturity assessment, `advanced-patterns.md` for recovery patterns.*
