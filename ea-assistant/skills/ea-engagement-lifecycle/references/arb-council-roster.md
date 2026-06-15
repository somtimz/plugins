# ARB Council Roster

The **ARB Council** is an advisory review panel: a set of independent specialist viewpoints that each examine an in-scope subject (an artifact, a phase, an ADR, or the whole engagement) through one mandate, then cast a recorded vote. The consolidated tally and conditions feed the Architecture Review Board's formal decision (`/ea-arb`).

This file is the **single source of truth** for the council's membership. It drives the `ea-arb-council` skill (invoked by `/ea-council` and `/ea-arb council`), which reads this file at runtime — **adding, removing, or re-mandating a member is a data edit here; no command or skill logic changes.**

> **Not personas, not roles.** Council members are *evaluative voting viewpoints*. Keep them separate from `persona-registry.md` (audience/reporting lenses that drive `/ea-help` and `/ea-publish` — adding a council member there would corrupt the `audience` taxonomy filtering) and from `role-catalogue.md` (named RACI engagement participants). The three registries are independent.

## Member schema

Each member is a `### {Name}` block with these fields:

- **Key** — unique kebab-case identifier (matched case-insensitively against `--member`/alias).
- **Aliases** — alternative names for matching.
- **Mandate** — the single concern this member reviews for. A member judges *only* through this mandate.
- **Examines** — the in-scope subject aspects and artifacts it focuses on.
- **Reads / Reuses** — existing skills, references, registers, and compliance rules the member grounds its assessment in (do not invent new evaluation engines).
- **Evaluation questions** — the 3–5 questions the member asks of the subject.
- **Vote criteria** — what earns `Approve` vs `Approve-with-conditions` vs `Reject` vs `Abstain`.
- **Voting** — `yes` (counts in the tally) or `no` (advisory only).

## Resolution

1. The skill reads every `### {Name}` block below, in order.
2. `/ea-council --member <key>` (repeatable) runs only the named members; otherwise the full roster runs.
3. A member whose anchored reference/register is absent still votes from available context (it notes the missing input), mirroring the load-if-present convention in `ea-architect-lens`.

---

## Members

### Planner
- **Key:** `planner` · **Aliases:** delivery, feasibility, programme
- **Mandate:** Is the plan actually deliverable? Scrutinise sequencing, dependencies, timelines, and readiness.
- **Examines:** Architecture Roadmap (work-package waves & ordering), Migration Plan, Business Transformation Readiness Assessment, cross-WP dependencies, `engagement.json → direction.gaps[]`, metric deadlines.
- **Reads / Reuses:** `skills/ea-grill-skills/SKILL.md` (premortem mode — assume delivery fails, surface why); `references/capability-based-planning.md` (readiness ceiling); roadmap `Strategic Alignment` table.
- **Evaluation questions:**
  1. Is the work sequenced so each wave's prerequisites are actually in place, or are there ordering/dependency breaks?
  2. Are timelines and resourcing realistic against the readiness ceiling, or is the plan assuming a maturity the organisation lacks?
  3. Which single dependency or assumption, if it slips, collapses the schedule — and is it being managed?
  4. Are Critical/High gaps tied to scheduled work packages, or unowned?
- **Vote criteria:** `Approve` — feasible, dependencies managed. `Approve-with-conditions` — feasible if specific sequencing/resourcing fixes are made (list them). `Reject` — the plan is not deliverable as drawn (broken critical path, unstaffed Wave 1, readiness gap with no mitigation). `Abstain` — no roadmap/plan in scope yet.
- **Voting:** yes

### Security Analyst
- **Key:** `security-analyst` · **Aliases:** security, ciso, sec
- **Mandate:** Where are the security vulnerabilities and unmanaged risks?
- **Examines:** Architecture artifacts (data/app/tech), trust boundaries, authN/Z, data handling, constraints (CST), policies (POL), and the Risk Register.
- **Reads / Reuses:** `skills/ea-security/` + `/ea-security-review` + the `ea-security-auditor` agent; existing `CST-NNN`/`POL-NNN`/`RIS-NNN`. Surfaced vulnerabilities are proposed as `RIS-NNN` entries (confirm-before-apply).
- **Evaluation questions:**
  1. What are the highest-impact attack surfaces or data-exposure paths in the subject, and are they mitigated?
  2. Are security-relevant decisions backed by constraints/policies, or merely assumed?
  3. Which identified weakness is not yet a tracked `RIS-NNN`?
  4. Does the design meet the engagement's stated compliance obligations?
- **Vote criteria:** `Approve` — no material unmitigated exposure. `Approve-with-conditions` — acceptable once named controls/mitigations are added. `Reject` (**blocking**) — a material unmitigated vulnerability or compliance breach. `Abstain` — subject has no security surface.
- **Voting:** yes

### Budget Analyst
- **Key:** `budget-analyst` · **Aliases:** budget, finance, cost
- **Mandate:** Account for every penny — is the spend justified, costed, and affordable?
- **Examines:** Cost Model Register (`FIN-NNN`), Business Case (options, TCO, payback), Roadmap/Migration cost estimates, benefit metrics.
- **Reads / Reuses:** `/ea-finance` + `FIN-NNN`; compliance rules **T4-TCO** (numeric cost with confidence on strategic options / Wave-1 WPs) and **T4-ECON** (cost/risk/value framing in rationale).
- **Evaluation questions:**
  1. Does every strategic option and Wave-1 work package carry a costed estimate (Capex/Opex or 3-yr TCO) with stated confidence?
  2. Is the recommended option the best value on cost·risk·value, or is a cheaper credible option dismissed without rationale?
  3. Where is money committed without a `FIN-NNN` entry or a benefit it traces to?
  4. Does the payback/benefits case hold, or is ROI asserted without numbers?
- **Vote criteria:** `Approve` — fully costed, defensible value. `Approve-with-conditions` — sound once specified costs/estimates are supplied. `Reject` (**blocking**) — major uncosted commitment, or value not justified. `Abstain` — no financial content in scope.
- **Voting:** yes

### Architect
- **Key:** `architect` · **Aliases:** design, quality, chief-architect
- **Mandate:** Is this a high-quality design — coherent, traceable, and sound?
- **Examines:** Design quality across the subject — coupling/cohesion, patterns, interfaces, data ownership, and motivation-chain traceability (DRV→G→OBJ→STR→WP).
- **Reads / Reuses:** `skills/ea-grill-skills/SKILL.md` (design / software-design / infra-design modes); `references/grill-scoring-rubric.md` (the **Quality** dimension — definition-correctness, guidance adherence, evidence & rigour, readability).
- **Evaluation questions:**
  1. Is the design coherent and at the right abstraction level for its phase, or are concerns tangled / over-specified?
  2. Does every significant element trace to a driver/goal, or is there orphaned work?
  3. Where are the brittle coupling points, unowned interfaces, or anti-patterns?
  4. Do the load-bearing decisions carry captured rationale (A3.N / ADR)?
- **Vote criteria:** `Approve` — sound, traceable, well-reasoned. `Approve-with-conditions` — good with specific design corrections. `Reject` — structurally weak, untraceable, or undocumented in load-bearing places. `Abstain` — subject is non-design (e.g. a pure governance record).
- **Voting:** yes

### Innovator
- **Key:** `innovator` · **Aliases:** modernise, innovation
- **Mandate:** Push for the most modern, future-proof choice — challenge dated thinking and preserve optionality.
- **Examines:** Technology and pattern choices, the Technology Horizon Register (`THR`), and whether the design leaves room to adopt better options later.
- **Reads / Reuses:** `references/practitioner-tips.md`, `references/advanced-patterns.md`; Technology Horizon Register (`THR-NNN`); compliance rule **T4-OPTION** (hard-to-reverse choices carry an optionality note).
- **Evaluation questions:**
  1. Is the subject reaching for the best available approach, or defaulting to the familiar where a stronger modern option exists?
  2. Does it preserve optionality on hard-to-reverse choices, or lock in early?
  3. Which emerging capability (in the horizon register or industry) is being ignored to the engagement's cost?
- **Vote criteria:** `Approve` — appropriately forward-looking with preserved optionality. `Approve-with-conditions` — adopt a named modern option / add an optionality note. `Reject` — needlessly dated or self-limiting choice that will age badly. `Abstain` — no technology/approach choice in scope. *(Deliberately opposes the Conservative — the split is a feature.)*
- **Voting:** yes

### Conservative
- **Key:** `conservative` · **Aliases:** prudent, proven, traditional
- **Mandate:** Adopt only tried-and-true products and processes — resist hype and premature commitment.
- **Examines:** Technology/vendor specificity vs phase, maturity of proposed products, and reliance on proven standards.
- **Reads / Reuses:** compliance rule **T4-PREMAT** (no specific tech/vendor choices in directional phases — flag and convert to `PAD-NNN`); `references/failure-modes.md`; Standards Information Base (`STD-NNN`).
- **Evaluation questions:**
  1. Is any choice premature for its phase (vendor/product named where only direction belongs)? Should it become a `PAD-NNN`?
  2. Are proposed products/processes proven and supportable, or bleeding-edge with thin operational evidence?
  3. Which choice matches a known failure-mode pattern, and what is the proven alternative?
- **Vote criteria:** `Approve` — proven, phase-appropriate, low-surprise. `Approve-with-conditions` — defer the premature choice to a `PAD-NNN` / substitute a proven option. `Reject` — unproven/hype-driven choice carrying avoidable delivery risk. `Abstain` — no maturity-relevant choice in scope. *(Deliberately opposes the Innovator — the split is a feature.)*
- **Voting:** yes

---

## Extending the council

Add a member as a new `### {Name}` block with the same fields (Key · Aliases · Mandate · Examines · Reads/Reuses · Evaluation questions · Vote criteria · Voting). Anchor it to existing skills/references/compliance rules rather than inventing a new evaluation engine. Set **Voting: no** for an advisory-only viewpoint that should not affect the tally. No command or skill edits are required — `ea-arb-council` reads this file at runtime.
