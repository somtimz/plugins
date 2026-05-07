# Direction Quality Rules

Reference for `/ea-direction --quality`, `/ea-grill --skill direction`, and `/ea-interview` Part 3 inline challenge.

Defines quality checks for all direction item types: categorization correctness, phrasing quality, evidence requirements, and isolation (missing links).

---

## Role

Senior Architecture Strategist reviewing the quality of direction statements. Does not rewrite content — flags, challenges, and notes items for remediation. All findings are advisory or warnings; none block engagement progress unless the user chooses to address them before Phase A.

---

## Output Format

For each item with findings:

```
Direction Quality: {ID} — {item type}
  Statement: "{statement}"
  ⚠️ [Miscategorization] {explanation — what it reads as instead, and why}
  ⚠️ [Missing evidence] {field name} — {guidance on what evidence to add}
  ⚠️ [Isolated] Not linked to any {goal/driver/objective}
  ℹ️ [Ambiguous phrasing] "{vague element}" — suggest making more specific
```

- `⚠️` — Warning (should be addressed before Phase A review)
- `ℹ️` — Advisory (can proceed, but worth revisiting)
- Items with no findings: include in the clean count only

---

## Quality Rules by Item Type

### Vision

| Check | Flag when… | Severity |
|---|---|---|
| Aspirational, not current-state | Vision describes what the organisation is today, not a 3–5 year destination | Warning |
| Not a wish list | Vision is a long enumeration of desired attributes with no unifying statement | Advisory |
| Not empty | Vision is blank, placeholder, or `—` | Blocking |

**Categorization guide:** Vision = long-term aspirational destination; present-tense framing of the future state ("We are the leading…" not "We will become…"). If the statement is purely about current purpose → likely Mission.

---

### Mission

| Check | Flag when… | Severity |
|---|---|---|
| Present-scope, not future-state | Mission describes what the organisation aspires to become rather than what it does today | Warning |
| Not empty | Mission is blank, placeholder, or `—` | Blocking |

---

### Driver (DRV-NNN)

| Check | Flag when… | Severity |
|---|---|---|
| Factual force, not aspirational response | Statement begins with "We need…", "We should…", "We want…", "We must…" — describes a desired response, not the forcing condition | Warning — Miscategorization (likely a Goal) |
| Evidence present | `evidence` field is empty, `—`, or whitespace | Warning |
| Links to at least one goal | `linkedGoals` is empty | Warning — Isolated |
| Type classified | `type` field is not "External" or "Internal" | Warning |

**Categorization guide:** A Driver is the external or internal force that makes the engagement necessary — a market shift, regulatory change, competitive pressure, or internal dysfunction. If the statement describes what the organisation wants to achieve in response → it is a Goal, not a Driver.

**Challenge questions (for interactive grill mode):**
- "Is this a force acting on the organisation, or the organisation's desired response to a force? If the latter, what is the underlying force?"
- "What evidence supports this driver? Is it a documented fact, a market analysis, a regulatory publication, or an assumption?"
- "Which goals does this driver motivate? If none are yet defined, this driver is currently isolated."

---

### Goal (G-NNN)

| Check | Flag when… | Severity |
|---|---|---|
| Qualitative, no built-in deadline or metric | Statement contains a specific measure + deadline (e.g. "by Q3 2026", "to 99.9%", "reduce by 30%") | Warning — Miscategorization (likely an Objective) |
| WHERE, not HOW | Statement describes a course of action ("Adopt…", "Invest in…", "Partner with…", "Migrate to…") | Warning — Miscategorization (likely a Strategy) |
| Not vague | Statement is generic with no qualifying context ("Improve performance", "Enhance customer experience", "Be more agile") | Advisory — Ambiguous |
| Links to at least one driver | `drivers` field is empty | Warning — Isolated |

**Categorization guide:** A Goal describes WHERE the organisation wants to be — a qualitative destination with no built-in deadline. If it is measurable with a specific target and deadline → it is an Objective. If it describes a course of action chosen to reach a destination → it is a Strategy.

**Challenge questions:**
- "Is this a destination or a path? 'Become a data-driven organisation' is a destination. 'Adopt a data platform' is a path."
- "Could this goal exist without any specific technology or approach? If removing the technology mention makes it meaningless, it may be a Strategy."
- "What driver motivates this goal? If there is no driver, what forces this to be a priority now?"

---

### Objective (OBJ-NNN)

| Check | Flag when… | Severity |
|---|---|---|
| Has measure | `measure` field is empty or `—` | Blocking |
| Has target | `target` field is empty or `—` | Blocking |
| Has deadline | `deadline` field is empty or `—` | Blocking |
| Links to a parent goal | `linkedGoal` is empty | Warning — Isolated |
| Describes outcome, not action | Statement describes a course of action rather than a measurable result | Warning — Miscategorization (likely a Strategy) |
| Contains a measurable component | Statement has no metric, threshold, or measurable element — it is qualitative | Warning — Miscategorization (likely a Goal) |

**Categorization guide:** An Objective is the measurable, time-bound operationalization of a Goal — HOW FAR and BY WHEN. All three fields (measure, target, deadline) are mandatory. If the statement is qualitative with no metric → it is a Goal. If it describes a chosen approach → it is a Strategy.

**Challenge questions:**
- "What would 'done' look like, and by when? If you cannot answer with a number and a date, this is a Goal, not an Objective."
- "What unit of measure are you using? Is this a leading indicator (predicts the outcome) or a lagging indicator (confirms it happened)?"
- "Which goal does this operationalize? An objective without a parent goal cannot be evaluated for strategic relevance."

---

### Strategy (STR-NNN)

| Check | Flag when… | Severity |
|---|---|---|
| Describes approach, not outcome | Statement describes a result to achieve ("Achieve…", "Reduce…", "Increase…", "Become…") | Warning — Miscategorization (likely a Goal) |
| Not a sequenced plan or set of steps | Statement contains numbered steps, timelines, or milestones — describes execution, not direction | Warning — Miscategorization (likely a Work Package or Migration Plan) |
| Not measurable/time-bound | Statement contains a specific metric + deadline | Advisory — possible Objective |
| Links to at least one goal | `supports` field is empty | Warning — Isolated |

**Categorization guide:** A Strategy is the chosen course of action — the HOW. It should be directional ("Adopt X", "Standardise on Y", "Partner with Z", "Invest in W") not an outcome statement. If the statement describes a destination → it is a Goal. If it contains sequenced steps → it belongs in a Migration Plan or Work Package.

**Challenge questions:**
- "Is this the approach you will take, or the result you want to achieve? Strategies answer 'how', not 'where'."
- "Could a different strategy achieve the same goal? If the strategy IS the goal, they may be conflated."
- "Which goal does this strategy support? If this strategy does not advance any stated goal, what motivates it?"

---

### Issue (ISS-NNN)

| Check | Flag when… | Severity |
|---|---|---|
| Systemic pattern, not a single event | Statement describes one specific observable event, a single metric, or a one-time failure | Warning — Miscategorization (likely a Problem) |
| Has evidence | `evidence` field is empty | Warning |
| Threatens at least one goal | `threatensGoals` field is empty | Warning — Isolated |

**Categorization guide:** An Issue is a strategic, systemic concern — a recurring pattern of dysfunction or a structural barrier that threatens goals. It has no single fix. If the statement is specific, measurable, and describes a single fixable event → it is a Problem.

**Challenge questions:**
- "Is this a pattern of dysfunction, or a single event? Issues are patterns; Problems are events."
- "Which goal does this issue threaten? If it does not threaten any stated goal, why is it captured here?"
- "What evidence supports this issue? A systemic claim without evidence is an assumption."

---

### Problem (PRB-NNN)

| Check | Flag when… | Severity |
|---|---|---|
| Specific and observable, not systemic | Statement describes a pattern-level or structural concern affecting a goal — no single fix | Warning — Miscategorization (likely an Issue) |
| Has evidence | `evidence` field is empty | Warning |
| Has stated symptom | `symptom` field is empty | Warning |
| Blocks at least one objective | `blocksObjectives` field is empty | Warning — Isolated |

**Categorization guide:** A Problem is a tactical, observable blocker — specific, measurable, and fixable. If the statement describes a systemic pattern threatening a goal → it is an Issue.

**Challenge questions:**
- "What is the observable symptom? Problems must have a measurable manifestation."
- "Which objective does this block? A problem that blocks no objective may be out of scope for this engagement."
- "What evidence supports this? A specific problem should be citable from data, incident logs, or stakeholder reports."

---

### Opportunity (OPP-NNN)

| Check | Flag when… | Severity |
|---|---|---|
| Type is Exploit / Enhance / Emerge | `type` field is blank or does not match one of the three values | Warning |
| Links to at least one driver | `drivers` field is empty | Warning — Isolated |
| Links to at least one goal | `linkedGoals` field is empty | Advisory |

**Type guide:**
- **Exploit** — leverages an existing strength or asset
- **Enhance** — improves an existing capability or process
- **Emerge** — creates a new capability that does not yet exist

**Challenge questions:**
- "Is this an opportunity or a strategy? Opportunities are possibilities — strategies are the choices made to act on them."
- "Which driver creates this opportunity? If no driver motivates it, why is it on the table now?"
- "Which goal does pursuing this opportunity advance? If none, it may be out of scope."

---

## Summary Format (used by /ea-direction --quality and interview Part 3)

```
Direction Quality Scan — {engagement name or 'Part 3 capture'}
──────────────────────────────────────────────────────────────
Items assessed: {N}   Issues found: {N}

⚠️ Warnings (address before Phase A)
  {ID}: {finding type} — {one-line description}
  ...

ℹ️ Advisory (can proceed, worth revisiting)
  {ID}: {finding type} — {one-line description}
  ...

✅ {N} items passed all checks.
```
