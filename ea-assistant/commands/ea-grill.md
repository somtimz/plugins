---
name: ea-grill
description: Deep-review an EA artifact using a grill-me skill — stress-test, boardroom simulation, pre-mortem, decision critique, or design critique
argument-hint: "[artifact-name] [--skill stress-test|premortem|decision|design|software-design|infra-design|artifact|diagram|boardroom-strategy] | security <artifact-id> | all [--skill <name>]"
allowed-tools: [Read, Bash, Glob]
---

Deeply review an EA artifact using a grill-me skill.

**Lane:** deep single-artifact critique. For formal sign-off with tracked comments use `/ea-review`; for cross-artifact contradictions and ID checks use `/ea-consistency`; for engagement-level reviews use `/ea-engage-review` (structured) or `/ea-lens` (opinionated). See the "Which Review Command?" table in `/ea-help`.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

---

### Argument Parsing — Mode Selection

Check the arguments provided:

- If `all` appears as an argument (e.g. `/ea-grill all` or `/ea-grill all --skill artifact`), jump to **[All Mode](#all-mode)** below. Do not proceed to Step 1.
- If `security` appears as an argument (in any position, e.g. `/ea-grill security <artifact-id>` or `/ea-grill <artifact-id> security`), extract the artifact ID (the non-`security` argument) and jump to **[Security Mode](#security-mode)** below. Do not proceed to Step 1.
- Otherwise, continue to Step 1 (standard grill workflow).

---

### Step 1 — Identify the artifact

If an artifact name was provided as an argument, locate it in `EA-projects/{slug}/artifacts/`. If not specified, list all artifacts in the engagement and ask the user to select one.

---

### Step 2 — Select the grill-me skill

If `--skill` was provided, use that skill. Otherwise, recommend a skill based on artifact type using this table:

| Artifact | Recommended Skill | Reason |
|---|---|---|
| Architecture Vision | `grill-me-boardroom-strategy` | Needs strategic depth + board pressure + pre-mortem — the most comprehensive review. For direction-only quality review (categorization, phrasing, evidence, isolation), use `--skill direction` |
| Statement of Architecture Work | `grill-me-decision` | A formal commitment — review as a decision memo |
| Architecture Principles | `grill-me-stress-test` | Each principle needs to survive assumption testing |
| Business Architecture | `grill-me-design` | Reviews for user needs, incentives, edge cases, and unintended consequences |
| Operating Model | `grill-me-design` | Reviews execution design: org, decision rights, controls, process orchestration, sourcing, and performance management |
| Application Architecture | `grill-me-software-design` | Reviews architecture patterns, coupling, API contracts, testability, and scalability |
| Data Architecture | `grill-me-software-design` | Reviews data model ownership, shared-state risks, access patterns, and quality |
| Technology Architecture | `grill-me-infra-design` | Reviews topology, resilience, blast radius, cost, security boundaries, and observability |
| Architecture Roadmap | `grill-me-premortem` | Assumes delivery failure — surfaces sequencing risks and missed dependencies |
| Migration Plan | `grill-me-premortem` | Red-teams the migration — finds failure modes before they occur |
| Gap Analysis | `grill-me-stress-test` | Tests whether gaps are correctly identified and prioritised |
| Architecture Contract | `grill-me-decision` | Reviews the commitment and its governance implications |
| Compliance Assessment | `grill-me-boardroom-strategy` | Simulates a board / audit panel reviewing compliance posture |
| Stakeholder Map | `grill-me-design` | Tests whether stakeholder concerns, incentives, and engagement levels are realistic |
| Requirements Register | `grill-me-requirements` | NFR coverage, measurability, traceability, consistency, and feasibility review |
| Decision Register | `grill-me-decision` | Reviews whether decisions are defensible, owned, and governed |
| Business Model Canvas | `grill-me-boardroom-strategy` | Needs full strategic + commercial + execution review |
| Business Case | `finance` | The financial instrument — review cost coverage, TCO, payback/value, and funding against the Cost Model (`FIN-NNN`) |

**Cost review:** Any cost-bearing artifact (Business Case, Architecture Roadmap, Migration Plan, or a high-cost ADR) can be reviewed financially with `--skill finance`, which audits cost coverage, whole-life TCO, payback/value, and funding against the Cost Model Register (`FIN-NNN`) and the T4-TCO / T4-ECON rules.

**Advanced mode overrides:** If the engagement is at L3+ maturity, the user may request an advanced review. When `--skill practitioner`, `--skill maturity`, `--skill failure-mode`, `--skill requirements`, `--skill direction`, `--skill waf`, `--skill caf`, or `--skill gcaf` is specified, bypass the default recommendation and use the requested skill. (The cloud lenses — `waf`, `caf`, `gcaf` — are available at any maturity level when the engagement has cloud scope.)

Confirm the skill with the user before proceeding, and offer the full list as alternatives.
The `--skill` argument accepts these short names:

| Short name | Skill ID | What it does |
|---|---|---|
| `stress-test` | `ea-assistant:ea-grill-skills` | Tests assumptions, surfaces risks, forces execution realism |
| `premortem` | `ea-assistant:ea-grill-skills` | Generate new risks (pre-mortem) or review an existing risk register |
| `decision` | `ea-assistant:ea-grill-skills` | Decision memo extractor: options, criteria, tradeoffs, recommendation, next steps |
| `design` | `ea-assistant:ea-grill-skills` | Design critique: user needs, failure points, edge cases, incentives, scalability (service/UX/org) |
| `software-design` | `ea-assistant:ea-grill-skills` | Software architecture: patterns, coupling, APIs, data models, testability, operational readiness |
| `infra-design` | `ea-assistant:ea-grill-skills` | Infrastructure: topology, resilience, blast radius, cost, security boundaries, observability |
| `artifact` | `ea-assistant:ea-grill-skills` | Structured artifact review: section-by-section completeness, traceability chains, consistency |
| `diagram` | `ea-assistant:ea-grill-skills` | Visual design review: topology, missing components, anti-patterns, readability |
| `boardroom-strategy` | `ea-assistant:ea-grill-skills` | Hybrid: strategic depth + board pressure + pre-mortem (most thorough) |
| `finance` | `ea-assistant:ea-grill-skills` | Financial & cost critique: cost coverage vs `FIN-NNN`, whole-life TCO, payback/ROI, option economics, funding & cost risk — applies T4-TCO / T4-ECON |
| `practitioner` | `ea-assistant:ea-grill-skills` | Practitioner-level review: economic framing, decision quality, optionality, complexity reduction — load `skills/ea-engagement-lifecycle/references/practitioner-tips/part-i-original-50-high-impact-togaf-tips.md`, `practitioner-tips/part-ii-phase-by-phase-deep-tactics.md`, and `practitioner-tips/part-iii-cross-cutting-expert-moves.md` |
| `maturity` | `ea-assistant:ea-grill-skills` | Maturity assessment: evaluates artifact against L1–L5 model and suggests advancement steps — load from `skills/ea-engagement-lifecycle/references/adm-maturity-model.md` |
| `failure-mode` | `ea-assistant:ea-grill-skills` | Failure-mode pre-mortem: detects symptoms of the 6 failure modes and suggests fixes — load from `skills/ea-engagement-lifecycle/references/failure-modes.md` |
| `requirements` | `ea-assistant:ea-grill-skills` | Requirements quality: NFR coverage scorecard, measurability, traceability, consistency, feasibility — load from `skills/ea-engagement-lifecycle/references/grill-requirements-skill.md` |
| `direction` | `ea-assistant:ea-grill-skills` | Direction item quality: categorization correctness, phrasing quality, evidence rigour, isolation — load from `skills/ea-engagement-lifecycle/references/grill-direction-quality.md` |
| `waf` | `ea-assistant:ea-framework-lenses` | AWS Well-Architected lens: pillar-by-pillar review (Operational Excellence, Security, Reliability, Performance, Cost, Sustainability) against the artifact's phase — load from `skills/ea-framework-lenses/references/aws-well-architected.md` and follow its Review Checklist per the lens consumption rules in that skill |
| `caf` | `ea-assistant:ea-framework-lenses` | Azure Cloud Adoption Framework lens: adoption-lifecycle review (Strategy, Plan, Ready, Adopt, Govern, Manage) — strongest on Phase A/B/E/F artifacts (vision, portfolio dispositions, roadmap, migration plan) — load from `skills/ea-framework-lenses/references/azure-caf.md` |
| `gcaf` | `ea-assistant:ea-framework-lenses` | Google Cloud Architecture Framework lens: pillar review (System Design, Operational Excellence, Security, Reliability, Cost, Performance) against the artifact's phase — load from `skills/ea-framework-lenses/references/google-caf.md` |

For the 10 core skills (stress-test through finance): after loading `ea-assistant:ea-grill-skills`, locate and follow the `## Mode: {short-name}` section that matches the requested skill. Ignore all other mode sections.

For the 8 advanced skills (practitioner, maturity, failure-mode, requirements, direction, waf, caf, gcaf): after loading the skill named in the table, if a `## Mode: {short-name}` section exists for the requested skill, follow it. If not, load the referenced file from the path in the table and follow its instructions as the review protocol.

---

### Step 3 — Load the artifact

Read the artifact file. Extract:
- The artifact type and phase
- All populated sections (skip empty `{{placeholder}}` fields)
- Any A3 Decision Log entries
- The current status, version, and review status from frontmatter

Then load full artifact-scoped context using **Scope A** from `skills/ea-engagement-lifecycle/references/context-loading.md`. Announce the loaded context to the user before proceeding to Step 4.

**Detail file challenge points:** If any detail files were loaded (Scope A step 8), scan them for content in the Issues and Concerns sections. Include these as additional challenge material during Step 5 — treat open items from detail files as known weaknesses the grill should probe. Announce:
> "Detail files loaded: {N} — {N} open issues, {N} open concerns. These will be used as additional challenge points during the review."

**Step 3b — Extract Section Guidance**

After loading the artifact, scan the full file for all `<details><summary>📋 Guidance</summary>...</details>` blocks. For each block found, record the nearest preceding section heading (the last `## ` or `### ` line before the block) as the key.

Build an internal map: `{section heading} → {guidance text}` — stripping the `<details>`, `<summary>`, and `</details>` tags to retain only the plain text content.

If the artifact has no guidance blocks (e.g. auto-generated registers or older artifacts pre-dating this format), skip silently.

Announce:
> "Guidance blocks extracted: {N} section(s) with documented quality criteria. These will be used as scoring standards during the review."

If N = 0, do not announce — skip silently.

---

### Step 4 — Brief the reviewer

Before starting the grill, present a one-paragraph framing to the user:

```
## Artifact Grill — [Artifact Name] using [skill-name]

**Artifact:** [name] | **Phase:** [phase] | **Status:** [status] | **Version:** [version]
**Skill:** [skill description — one line]

I've loaded the artifact. I'll now act as [role from skill] and review it one question at a time.
After each of your answers I'll push back and identify weaknesses — I will NOT propose edits during the Q&A.
All proposed revisions are collected and presented at the end (Step 7), where you can accept, edit, or reject each one.

Ready? Here is my first question.
```

---

### Step 5 — Run the grill

Apply the selected grill-me skill, using the artifact content as the "proposal" being reviewed. You have full context of every section. Ask questions that specifically challenge the content of this artifact — do not ask generic questions that ignore what is written.

For example:
- If reviewing an Architecture Vision and §4 Business Drivers lists only internal drivers, challenge whether external forces have been overlooked.
- If reviewing an Architecture Vision and §11 Strategic Direction Summary has strategies that don't link to any goal, challenge the traceability.
- If reviewing a Migration Plan and Wave 1 has no rollback procedure, ask directly about that gap.
- If reviewing an Architecture Principles artifact and a principle lacks an Implications section, probe whether the team understands the practical consequences.

**Two Layers challenge (for Business Architecture, Architecture Vision, Requirements Register, and Stakeholder Map):**
When grilling an artifact that captures business-layer concepts, actively check for mixed-layer content:
- If a Business Architecture Use Case describes a "governance process," "review board," or "architecture standard," challenge: *"This subject is EA / TOGAF governance — it would disappear if the EA team were disbanded. Should this be an EA Capability Use Case in the Governance Framework instead?"*
- If an Architecture Vision Goal is about "establishing EA governance," "defining architecture standards," or "building EA capability," challenge: *"This is an EA Goal — it belongs in the Governance Framework or Architecture Principles, not the business strategy. Is this a business outcome or an EA enabler?"*
- If a Requirements Register requirement's subject is governance, standard, or EA process, challenge: *"Is this a Business Requirement (what the business needs) or an Architecture Requirement (how EA governs solutions)?"*
Reference `skills/ea-artifact-templates/references/two-layers-of-intent.md` for the naming conventions and quick test.

Follow the selected skill's interviewing protocol exactly: one question at a time, with the question framing, recommended answer, and what a board member / critic / red-teamer would worry about.

**During Q&A — do NOT propose specific text edits or artifact changes.** Your role here is to challenge, probe, and record findings. After each user answer: acknowledge it, push back on weaknesses, note the finding internally, then ask the next question. All proposed revisions are batched and presented in Step 7 with `y/n/edit` confirmation per revision.

When asking questions, actively use the loaded context — do not treat it as passive background:
- **Brainstorm notes:** If a session noted a concern that the artifact should address, challenge whether it has been resolved.
- **Interview notes:** If a prior interview captured an answer that diverges from the artifact's current content, surface the discrepancy directly.
- **Review / grill files:** If a prior grill identified revisions that were recommended but appear unapplied, flag them.
- **Research items:** If a research item contains findings that contradict or qualify an artifact claim, cite it: `[research: {title}]`
- **Related artifacts:** If a cross-referenced artifact labels the same ID differently or states a contradicting fact, challenge the inconsistency.
- **Missing links (web of links):** If the artifact describes a relationship that is not yet recorded as a link — an item that clearly traces to a goal, capability, requirement, or decision in another artifact but carries no `relatedArtifacts` / detail-file `relatedItems` entry — flag it and propose the missing link as a Step 7 revision. Treat an unrecorded but evident relationship as a gap, not just a stylistic omission.

### Decision-Specific Grilling Protocol

When the selected skill is `grill-me-decision` or when reviewing any artifact containing A3 Decision Log entries, ADR references, or technology/pattern choices, apply these additional challenge layers:

**Layer 1 — Decide vs Defer Matrix**
For each significant decision in the artifact, challenge using the five factors:
- **Evidence:** "What evidence exists for this decision? Is it sufficient to justify commitment, or is this still an assumption?" If evidence is weak, probe: "Should this be a PAD-NNN (Pending Architecture Decision) rather than a committed A3 entry?"
- **Reversibility:** "If this decision is wrong, how easily can it be reversed? What is the cost and timeline of reversal?" If hard to reverse and evidence is weak, flag as premature.
- **Impact:** "What is the blast radius if this decision is wrong? How many teams, systems, or capabilities are affected?" Cross-reference with the A3 Impact classification.
- **Urgency:** "Is there a real deadline forcing this decision now, or is the pressure artificial?" If artificial, challenge why it cannot be deferred.
- **Capability:** "Does the team have the skills, data, and tools to implement and operate this decision? If not, what is the plan to close that gap before commitment?"

**Layer 2 — Premature Decision Detection**
When reviewing architecture patterns, technology selections, or vendor choices in Phases A–D:
- If the artifact is Phase A and contains a technology/pattern decision (e.g., "microservices", "Kubernetes", "SAP S/4HANA"), challenge explicitly:
  > "You are proposing a specific technology/pattern in Phase A, before business capabilities, data domains, or application boundaries are defined. This creates risk of rework if the downstream architecture contradicts this choice. Should this be a PAD-NNN with constraint boundaries instead?"
- Reference the microservices example: "A microservices decision in Phase A without service boundary analysis is a classic premature decision — it forces decomposition before business domain analysis is complete."

**Layer 3 — Evidence Sufficiency Check**
For any decision with a stated rationale, challenge:
- "What evidence would change this decision? Do you have it now?"
- "What experiments, POCs, or spikes are planned to validate the assumptions behind this decision before it becomes binding?"
- "Are there MUST requirements that act as disqualifiers? If a candidate option violates a MUST, is it still being considered?"

**Layer 4 — Political Alignment Probe**
When the artifact states "strong pressure to adopt X" or "stakeholder insists on Y":
- "What is the defensible governance position if this decision is challenged? Can you articulate the evidence-based case for or against, independent of the political pressure?"
- "Has the Architecture Board or governance forum reviewed this with the evidence presented, or was this a fiat decision?"
- "What guardrails or constraint boundaries would make this politically driven decision architecturally safe?"

**Layer 5 — Phase-Appropriateness Check**
Map each decision to the phase-specific decision flow:
- **Preliminary:** Can decide directly (principles, governance model). Challenge if too specific.
- **Phase A:** Should be directional only. Challenge any specific technology or pattern choice.
- **Phase B–D:** Decide where feasible (baseline-to-target gaps, capability needs). Log uncertainties as PAD-NNN entries.
- **Phase E:** Convert gaps and PADs into work packages. Challenge any remaining unconverted PADs.
- **Phase F:** Prioritize work packages by evidence quality. Challenge low-evidence packages.
- **Phase G:** Enforce decided architecture. Challenge any unenforced deviations.
- **Phase H:** Adapt based on evidence. Challenge decisions that are not being revisited despite new evidence.

**Layer 6 — Concept Type Validation**
Check that every item is recorded under the correct concept type. Raise a finding for each mismatch:

- **Capability vs Implementation (CAP-NNN):** Does the capability describe a business or technology ability (what the organisation can do) — or does it describe an implementation mechanism (how something is built)? A capability must be vendor-neutral and technology-agnostic. Flag: specific products, platform names, or build techniques in the capability name or description. Also flag: capabilities phrased as system functions ("The system shall expose an API") rather than organisational abilities — challenge whether this is what the *organisation* must be able to do, or what a *system* must do.
- **Requirement vs Story (REQ-NNN / STY-NNN):** Is the item a verifiable, binding constraint ("must", "shall", "the system is required to") — or a delivery intent framed as user value ("as a X, I want Y so that Z")? Requirements belong in the Requirements Register (REQ-NNN); stories belong in the Stories subsection (STY-NNN). Flag: "as a" phrasing in a REQ row, or "must/shall" binding language in a STY row. Also flag: REQ-NNN rows with no Measurable Target — without one, the requirement cannot be verified ("What metric confirms this requirement is met?").
- **ABB vs SBB (ABB-NNN / SBB-NNN):** Is the component a logical, vendor-neutral definition — or a specific vendor/product choice? An ABB names the logical capability ("Immutable Log Store"); an SBB names the concrete implementation ("AWS CloudTrail + S3 Glacier"). Flag: vendor names, version numbers, or brand names in an ABB field; purely logical descriptions (no product) in an SBB field. Also flag: technical components in Gap Analysis that carry no ABB-NNN or SBB-NNN identifier — challenge whether each is a baseline ABB (what the current architecture provides), a target SBB (what will be built or procured), or an unclassified item that needs labelling.
- **Story vs Task (STY-NNN):** Is the item a user-value statement (story) or an atomic implementation action (task)? Stories carry a STY-NNN ID and appear in the Stories table. Tasks are unnumbered bullets under a story. Flag: task-level actions ("configure X", "write script Y", "run migration Z") given a STY-NNN ID; story-level items buried as bullet points with no ID.
- **Constraint vs Requirement (CST-NNN / REQ-NNN):** Check that binding obligation language (`must`, `shall`, `required to`, `cannot`, `prohibited`) is assigned to the correct concept type:
  - **Requirement (REQ-NNN):** The statement defines *what* the architecture must achieve or ensure — a verifiable outcome ("RTO < 4 hours", "All data encrypted at rest"). Must have a Measurable Target. Flag if missing.
  - **Constraint (CST-NNN):** The statement restricts *how* something may be implemented — a non-negotiable boundary on solution space ("Must use existing AWS account", "Budget capped at $2M", "No on-premise deployment"). Does NOT have a measurable target; has a Source (policy, regulation, contract) and Owner. Flag a finding when:
    1. A REQ-NNN row describes an implementation restriction → extract as CST-NNN, cross-reference
    2. A CST-NNN row describes an outcome with no restriction → extract as REQ-NNN
    3. A constraint has no Source or Owner field → flag as governance gap
    4. An SBB's "Constraints" field contains restriction text but no `Referenced Constraints: [CST-NNN]` link → flag traceability gap

---

### Note Capture Interrupt

At any point during the grill — during Q&A or the revision review loop in Step 7 — if the user's input starts with `n: ` (note prefix):

1. Strip the `n: ` prefix to extract the note text.
2. Determine the current phase folder from the active artifact's location (e.g. artifact at `artifacts/phase-a/...` → phase folder `phase-a`).
3. Determine N: glob `EA-projects/{slug}/artifacts/{phase-folder}/notes/adhoc/note-{YYYY-MM-DD}-*.md`, count existing files and add 1.
4. Write `EA-projects/{slug}/artifacts/{phase-folder}/notes/adhoc/note-{YYYY-MM-DD}-{N}.md` with:
   ```yaml
   ---
   type: adhoc
   engagement: {name}
   phase: {phase label}
   date: {YYYY-MM-DD}
   source: grill
   parentArtifact: {artifact-id being grilled}
   status: Open
   resolvedDate: null
   resolvedBy: []
   crossPhase: false
   ---
   ```
   Body: note text followed by `\n\n## Resolution\n\n*(not yet resolved)*`
5. Confirm inline without breaking the session flow:
   ```
   📌 Note saved. _(`/ea-note resolve {path}` to record resolution when addressed)_
   ```
6. Resume the session:
   - **During Q&A:** Re-present the current question — do not advance to the next one.
   - **During Step 7 revision loop:** Re-display the current revision and `Apply this revision? (y/n/edit)` prompt — do not advance to the next revision.

This interrupt is available throughout the grill session and does not affect grill findings or revision state.

---

### Step 6 — Produce the output

When the review is complete (or the user types `done` or `finish`), produce the skill's structured output as specified:

- **stress-test** → refined strategy summary, top 5 unresolved risks, hardest objection, next decision required
- **premortem** → top failure modes, early warning signs, safeguards, proceed/pause/redesign verdict
- **decision** → decision statement, options analysis, recommendation, risks, next steps
- **design** → strengths, design flaws, recommended revisions, unresolved design bets
- **software-design** → architecture pattern assessment, coupling/cohesion findings, API contract gaps, testability rating, operational readiness checklist, top 5 recommended changes
- **infra-design** → topology assessment, resilience gaps, blast radius analysis, cost observations, security boundary issues, observability gaps, top 5 recommended changes
- **artifact** → section-by-section completeness scorecard, traceability chain gaps, cross-artifact consistency issues, top recommended revisions
- **diagram** → topology assessment, missing components, anti-patterns identified, readability issues, recommended structural changes
- **boardroom-strategy** → executive summary, case for proceeding, case against, top unresolved risks, next decision required, 2-minute board-ready version
- **finance** → cost coverage scorecard (% of options/Wave-1 WPs with FIN-backed estimates + uncosted list), whole-life TCO gaps, value/payback verdict, top financial risks, recommended `FIN-NNN` entries, funding decision required
- **practitioner** → economic framing assessment, decision quality scorecard, optionality audit, complexity heatmap, top 5 practitioner recommendations
- **maturity** → current maturity level (L1–L5), gap analysis vs next level, specific advancement actions, blockers to progress
- **failure-mode** → failure mode symptom scan (6 modes), root cause analysis for any detected, prevention recommendations, proceed/pause/redesign verdict
- **requirements** → NFR coverage scorecard (9 categories × covered/no target/missing), traceability gap list, top 5 quality findings, proceed/pause/rework verdict
- **direction** → quality scan per direction item: categorization flags, missing evidence, isolation warnings, phrasing advisories, summary counts (warnings / advisories / clean)

Offer to save the output as a review note:
```
Save this grill output as a review file? (y/n)
File would be saved to: EA-projects/{slug}/artifacts/{phase-folder}/notes/reviews/grill-{artifact-id}-{skill}-{YYYY-MM-DD}.md
```

Resolve `{phase-folder}` from the artifact frontmatter `phase:` field using the Phase Folder Mapping table in `skills/ea-engagement-lifecycle/SKILL.md`.

If the user confirms, write the file with a frontmatter header:
```yaml
---
artifact: [artifact-name]
skill: [grill-me-skill-used]
date: [YYYY-MM-DDTHH:MM:SSZ]
reviewer: ea-grill
---
```

---

### Step 6b — Populate Appendix A4 from grill output

After saving (or declining to save) the review file, and **before** offering to apply findings, offer to populate the artifact's A4 appendix with the concerns and objections surfaced during the grill:

```
Populate Appendix A4 — Stakeholder Concerns & Objections?

The grill identified [N] objections, concerns, or tough questions. I can add these to
the artifact's A4 appendix now, tagged as raised by "[skill-name] session".

Options:
  (a) Add all — I'll add all identified concerns to A4
  (s) Select — I'll list them and you choose which to add
  (n) Skip — leave A4 unchanged
```

If the user selects `a` or `s`:

1. For each selected concern/objection from the grill output:
   - Assign the next available `CON-NNN` ID (read existing A4 rows first to determine last used number across all artifacts in the engagement)
   - Set `Raised By` to the skill name (e.g., `"grill-me-boardroom-strategy session"`)
   - Set `Category` based on the nature of the concern:
     - Challenge to scope or boundaries → `Scope`
     - Challenge to a goal, driver, or objective → `Goal`
     - Challenge to an architectural approach or decision → `Approach`
     - Feasibility doubt (cost, time, capability) → `Feasibility`
     - Risk or failure mode identified → `Risk`
     - Stakeholder alignment issue → `Stakeholder`
     - Decision made before sufficient evidence or correct phase → `Premature`
     - Insufficient evidence to justify commitment → `Evidence`
     - Decision driven by stakeholder pressure rather than rationale → `Political`
     - Should have been a PAD-NNN instead of committed decision → `Deferral`
     - Other → `Other`
   - Set `Status` based on whether the artifact has a documented response:
     - If the artifact section being challenged contains a clear answer → `Addressed`; record the section reference in `Response`
     - If the artifact section exists but is weak or incomplete → `Partially Addressed`; note what is missing
     - If no adequate response exists in the artifact → `Requires Attention`; leave `Response` blank
   - Set `Action / Owner` for `Requires Attention` items: propose the action (e.g., "Expand §3 Goals to address retail scope exclusion — Owner: Lead Architect")

2. Append all new A4 rows to the artifact's `## Appendix A4 — Stakeholder Concerns & Objections` table.
3. Update `lastModified` in the artifact frontmatter.
4. Confirm: "Added [N] concerns to Appendix A4. [M] require attention — run `/ea-concerns` to see the full register."

**Concerns that are `Category: Risk`:** After adding to A4, flag them:
> "⚠️ [N] concern(s) in category Risk. Run `/ea-risks` to register them in the Risk Register."

**Cross-reference CON-NNN to item detail files:** After all A4 rows are written, scan the concern text of each new CON-NNN for recognisable engagement ID patterns (e.g. `G-001`, `WP-003`, `CAP-007`). If any are found, offer:

```
Cross-reference {N} concern(s) in item detail files?

  CON-001 → G-001 (Goal — Reduce operational costs)
  CON-003 → WP-002 (Work Package — CRM Platform Replacement)

Options:
  (a) Add all — append each concern to its item's detail file Concerns section
  (s) Select — choose which to cross-reference
  (n) Skip
```

If `a` or `s` selected:
- For each chosen CON-NNN: check whether `artifacts/details/{ID}.md` exists.
  - If not: create a stub using `templates/cross-cutting/item-detail.md`.
  - Append to the **Concerns** section: `- CON-NNN: {concern text} — {grill skill}, {YYYY-MM-DD}`
  - Update `lastModified` in the detail file frontmatter.
- If the concern text does not clearly map to an ID, ask: "Which item ID does CON-NNN relate to? (enter ID or skip)"

---

### Step 7 — Apply findings to the artifact

After saving (or declining to save) the review, offer to apply the findings:

```
Apply findings to the artifact?

I identified [N] recommended revisions. I can apply them now, one at a time, with your confirmation on each.

Options:
  (a) Apply all — I'll walk through each revision and apply on your go-ahead
  (s) Select — I'll list the revisions and you pick which to apply
  (n) Skip — leave the artifact unchanged for now
```

If the user selects `a` or `s`:

1. List each recommended revision with:
   - **Section** — which artifact section it affects
   - **Issue** — what the grill identified as the problem
   - **Proposed change** — the specific text or structural fix

   Example:
   ```
   Revision 1 of 3
   ───────────────────────────────────
   Section: §3 Goals
   Issue: G-002 has no Business Driver (DRV) linked — traceability broken
   Proposed: Add "DRV-001" to the Linked Drivers field of G-002

   Apply this revision? (y/n/edit)
   ```

2. For each confirmed revision:
   - Write the change to the artifact
   - Confirm: `✅ Applied — §3 Goals / G-002 updated`

3. For `edit` responses — present the proposed text and let the user dictate the replacement before writing

4. After all revisions are processed:
   - Bump the artifact `version` by a patch increment (e.g. `0.1` → `0.2`)
   - Update `lastModified` to today's date
   - Set `reviewStatus` to `In Review` if it was `Not Reviewed` or `Needs Revision`, or keep existing if already `In Review` or `Approved`
   - Confirm: `Artifact updated — [N] revisions applied, version bumped to [new version]`

5. **Populate Artifact Working Notes — Critiques.** After confirming the version bump, scan the grill findings for any issues that were surfaced but NOT resolved inline (i.e., the user typed `n` or skipped them). For each unresolved finding:
   - Append a row to the artifact's `## Artifact Working Notes > Critiques` table:
     `| {auto-number} | {section name} | {finding summary — one sentence} | ea-grill / {skill-name} | {YYYY-MM-DD} | Open |`
   - This is additive — do not overwrite or delete existing rows.
   - If the `## Artifact Working Notes` section does not yet exist in the artifact (pre-dates this feature), append the full section block at the end of the artifact before writing the critique rows.
   - If all findings were resolved inline, skip this step silently.
   - Announce: `📋 {N} unresolved finding(s) added to Artifact Working Notes — Critiques.` (omit if N = 0)

**Constraints:**
- Never apply a revision to an `Approved` artifact without explicit user confirmation — warn first: `⚠️ This artifact is Approved. Applying revisions will reset reviewStatus to In Review. Continue? (y/n)`
- Never invent content — only apply revisions derived directly from the grill output
- If a revision touches a field that references other artifacts (e.g. adds a GAP-NNN or REQ-NNN ID), flag it: `⚠️ This adds a reference to [ID] — verify it exists in the source artifact before saving`

After all revisions are applied or the user skips Step 7:

### Executive Summary Refresh

If any revisions were applied and the artifact has a `## Executive Summary` section:
1. Read the updated artifact content.
2. Draft a 3–5 sentence executive summary reflecting the current state of the artifact. Avoid technical jargon.
3. Present to the user:
   > **Updated Executive Summary for {Artifact Name}:**
   > {drafted summary}
   > Accept? (y / edit / skip)
4. On `y`: write the summary to the `## Executive Summary` section.
   On `edit`: show the text for editing; apply the user's version.
   On `skip`: leave unchanged.

If the artifact has no `## Executive Summary` section, skip this step silently.

Then proceed to Step 8.

---

### Step 8 — Diagram Coverage

Check whether the expected diagrams for this artifact type exist and are referenced.

1. **Look up expected diagrams.** Read `skills/ea-artifact-templates/references/diagram-catalogue/{phase-or-artifact-file}` — find the section for this artifact type and note the expected diagram names and standard filenames.

2. **Check what is present.** For each expected diagram:
   - Check the artifact frontmatter `diagrams: []` for a matching path
   - Search the artifact body for an inline reference (`../diagrams/...`)
   - Check `EA-projects/{slug}/diagrams/` for a file matching the standard filename pattern (`{artifact-id}-*.mmd` or `{artifact-id}-*.png`)

3. **Report coverage:**
   ```
   ## Diagram Coverage — [Artifact Name]

   | Diagram | Expected File | Status |
   |---|---|---|
   | Motivation Map | architecture-vision-motivation-map.mmd | ✅ Present |
   | Stakeholder Grid | architecture-vision-stakeholder-grid.mmd | ❌ Missing |
   ```
   Status values: ✅ Present | ⚠️ Source only (not rendered) | ❌ Missing

4. **For each ❌ Missing diagram:** state in one sentence what it would show and offer to create it:
   > "The Stakeholder Power/Interest Grid would show stakeholder positioning by influence and interest. Create it now? (y/n)"
   - If yes: delegate to the `ea-diagram` agent with the standard filename, the relevant artifact section as context, and the Mermaid starter from the diagram catalogue.
   - If no: continue.

5. **For each ⚠️ Source only:** offer to render it:
   > "Found `architecture-vision-motivation-map.mmd` but no rendered image. Run `/ea-generate png` to produce a `.png` for export."

After Step 8 is complete, ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md (the --next flag section)` and output the recommendation.

---

## All Mode

**Triggered by:** `/ea-grill all` or `/ea-grill all --skill <name>`

Runs a non-interactive structural review on every artifact in the engagement, saves a review file per artifact, and outputs a consolidated summary table. No Q&A, no apply loop, no A4 population, no version bumps.

### AM-1 — Determine the skill

If `--skill <name>` was provided, use that skill for all artifacts. Otherwise default to `artifact`.

### AM-2 — Enumerate artifacts

Glob `EA-projects/{slug}/artifacts/**/*.md`, then exclude:
- Any path containing `/notes/`
- Any path containing `/details/`

Sort by phase folder order: `preliminary → requirements → phase-a → phase-b → phase-c-data → phase-c-app → phase-d → phase-e → phase-f → phase-g → phase-h → cross-cutting`.

Announce:
```
## Grill All — [Engagement Name]

Skill: [skill name]
Artifacts found: [N]

Reviewing each artifact non-interactively. Review files will be saved under each artifact's notes/reviews/ folder.
```

### AM-3 — Review each artifact

For each artifact in turn:

1. **Read** the artifact file in full.
2. **Load** the artifact's frontmatter: `title`, `phase`, `status`, `version`.
3. **Apply the `artifact` skill** (or the overriding `--skill`) directly to the artifact content — do not ask questions. Instead, produce the full structured output for that skill as if the review session were complete. For the `artifact` skill this means:
   - Section-by-section scorecard with **Completeness and Quality (0–100 + band) per section** (rubric: `skills/ea-engagement-lifecycle/references/grill-scoring-rubric.md`), plus the legacy state (Complete / Partial / Empty / Inconsistent); then the **overall Completeness and Quality** roll-up, and write/refresh the artifact's author-only `📊 Scorecard` block
   - Traceability gaps (dangling or missing ID references)
   - Governance anti-patterns found (each with specific text and recommended fix)
   - Three weakest sections and why
   - Three strongest sections and why
   - Recommended revisions (prioritised, top 5 maximum per artifact to keep output scannable)
   - Overall verdict: **Ready for review** / **Needs revision** / **Incomplete**
4. **Save** the output as a review file:
   `EA-projects/{slug}/artifacts/{phase-folder}/notes/reviews/grill-{artifact-id}-{skill}-{YYYY-MM-DD}.md`
   with frontmatter:
   ```yaml
   ---
   artifact: [artifact-id]
   skill: [skill-name]
   date: [YYYY-MM-DDTHH:MM:SSZ]
   reviewer: ea-grill-all
   ---
   ```
5. **Append a summary row** to the consolidated table (built in AM-4).

If a review file for this artifact + skill + date already exists, skip that artifact and note it as `(skipped — already reviewed today)` in the summary.

### AM-4 — Consolidated summary

After all artifacts are processed, output:

```
## Grill All — Summary

| Artifact | Phase | Status | Verdict | Findings | Review File |
|---|---|---|---|---|---|
| Architecture Vision | Phase A | Draft | Needs revision | 6 | notes/reviews/grill-architecture-vision-artifact-2026-05-14.md |
| ...                 | ...     | ...   | ...           | ... | ... |

**[N] artifacts reviewed. [N] Ready for review · [N] Needs revision · [N] Incomplete.**

Run `/ea-grill <artifact-name>` on any artifact to walk through findings interactively and apply revisions.
```

Resolve `{phase-folder}` from each artifact's frontmatter `phase:` field using the Phase Folder Mapping table in `skills/ea-engagement-lifecycle/SKILL.md`.

---

## Security Mode

**Triggered by:** `/ea-grill security <artifact-id>` or `/ea-grill <artifact-id> security`

**Difference from `/ea-security-review`:** This mode is interactive — findings are walked through one at a time with `y/n/edit` confirmation, and accepted fixes are applied to the artifact immediately. `/ea-security-review` produces a read-only report.

### SM-1 — Load the artifact

Locate the artifact file in `EA-projects/{slug}/artifacts/` using the provided artifact ID. Load full artifact-scoped context using **Scope A** from `skills/ea-engagement-lifecycle/references/context-loading.md`. Announce loaded context to the user.

### SM-2 — Dispatch `ea-security-auditor`

Invoke the `ea-security-auditor` agent with **Scope A** (single artifact). Pass the full artifact content. The auditor produces a structured list of security findings in the form:

```
Finding S-W1: <title>
Gap: <what is missing or wrong>
Suggested fix: <specific text or structural change to apply>
```

Present a summary to the user:
```
## Security Audit — [Artifact Name]

ea-security-auditor identified [N] finding(s). I'll walk through each one now.
Accept (y), skip (n), or provide your own text (edit) for each suggested fix.
```

### SM-3 — Interactive finding walkthrough

For each finding, present:

```
Finding S-W1: Authentication model undefined
Gap: No auth model specified in Application Architecture
Suggested fix: Add authentication model section specifying SSO via Azure AD (MFA required)
Apply this fix? (y/n/edit)
```

- **`y`** — apply the suggested fix text to the artifact, confirm applied, continue to next finding
- **`n`** — skip without change, continue to next finding
- **`edit`** — prompt the user: "Enter your replacement text:", apply that text instead, confirm applied, continue

### SM-4 — Version bump and close

After all findings are processed:

1. Bump the artifact `version` by a patch increment (e.g. `0.3` → `0.4`)
2. Update `lastModified` in frontmatter to today's date
3. Set `reviewStatus` to `In Review` if it was `Not Reviewed` or `Needs Revision`; warn before writing to an `Approved` artifact: `⚠️ This artifact is Approved. Applying fixes will reset reviewStatus to In Review. Continue? (y/n)`
4. Confirm: `Security grill complete — [N] fix(es) applied, version bumped to [new version]`

**Constraints (same as Step 7):**
- Never invent content — only apply fixes derived from auditor output or user-supplied text
- If a fix references an ID (GAP-NNN, REQ-NNN, etc.), flag it: `⚠️ This adds a reference to [ID] — verify it exists before saving`
