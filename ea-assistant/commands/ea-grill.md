---
name: ea-grill
description: Deep-review an EA artifact using a grill-me skill — stress-test, boardroom simulation, pre-mortem, decision critique, or design critique
argument-hint: "[artifact-name] [--skill stress-test|premortem|decision|design|software-design|infra-design|artifact|diagram|boardroom-strategy] | security <artifact-id>"
allowed-tools: [Read, Glob, Bash]
---

Deeply review an EA artifact using a grill-me skill.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

---

### Argument Parsing — Mode Selection

Check the arguments provided:

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
| Architecture Vision | `grill-me-boardroom-strategy` | Needs strategic depth + board pressure + pre-mortem — the most comprehensive review |
| Statement of Architecture Work | `grill-me-decision` | A formal commitment — review as a decision memo |
| Architecture Principles | `grill-me-stress-test` | Each principle needs to survive assumption testing |
| Business Architecture | `grill-me-design` | Reviews for user needs, incentives, edge cases, and unintended consequences |
| Application Architecture | `grill-me-software-design` | Reviews architecture patterns, coupling, API contracts, testability, and scalability |
| Data Architecture | `grill-me-software-design` | Reviews data model ownership, shared-state risks, access patterns, and quality |
| Technology Architecture | `grill-me-infra-design` | Reviews topology, resilience, blast radius, cost, security boundaries, and observability |
| Architecture Roadmap | `grill-me-premortem` | Assumes delivery failure — surfaces sequencing risks and missed dependencies |
| Migration Plan | `grill-me-premortem` | Red-teams the migration — finds failure modes before they occur |
| Gap Analysis | `grill-me-stress-test` | Tests whether gaps are correctly identified and prioritised |
| Architecture Contract | `grill-me-decision` | Reviews the commitment and its governance implications |
| Compliance Assessment | `grill-me-boardroom-strategy` | Simulates a board / audit panel reviewing compliance posture |
| Stakeholder Map | `grill-me-design` | Tests whether stakeholder concerns, incentives, and engagement levels are realistic |
| Requirements Register | `grill-me-stress-test` | Tests whether requirements are complete, traceable, and achievable |
| Decision Register | `grill-me-decision` | Reviews whether decisions are defensible, owned, and governed |
| Business Model Canvas | `grill-me-boardroom-strategy` | Needs full strategic + commercial + execution review |

**Advanced mode overrides:** If the engagement is at L3+ maturity, the user may request an advanced review. When `--skill practitioner`, `--skill maturity`, or `--skill failure-mode` is specified, bypass the default recommendation and use the requested skill.

Confirm the skill with the user before proceeding, and offer the full list as alternatives.
The `--skill` argument accepts these short names (mapped to the full `grill-me-*` skill IDs):

| Short name | Skill ID | What it does |
|---|---|---|
| `stress-test` | `grill-me-stress-test` | Tests assumptions, surfaces risks, forces execution realism |
| `premortem` | `grill-me-premortem` | Generate new risks (pre-mortem) or review an existing risk register |
| `decision` | `grill-me-decision` | Decision memo extractor: options, criteria, tradeoffs, recommendation, next steps |
| `design` | `grill-me-design` | Design critique: user needs, failure points, edge cases, incentives, scalability (service/UX/org) |
| `software-design` | `grill-me-software-design` | Software architecture: patterns, coupling, APIs, data models, testability, operational readiness |
| `infra-design` | `grill-me-infra-design` | Infrastructure: topology, resilience, blast radius, cost, security boundaries, observability |
| `artifact` | `grill-me-artifact` | Structured artifact review: section-by-section completeness, traceability chains, consistency |
| `diagram` | `grill-me-diagram` | Visual design review: topology, missing components, anti-patterns, readability |
| `boardroom-strategy` | `grill-me-boardroom-strategy` | Hybrid: strategic depth + board pressure + pre-mortem (most thorough) |
| `practitioner` | `grill-me-practitioner` | Practitioner-level review: economic framing, decision quality, optionality, complexity reduction |
| `maturity` | `grill-me-maturity` | Maturity assessment: evaluates artifact against L1–L5 model and suggests advancement steps |
| `failure-mode` | `grill-me-failure-mode` | Failure-mode pre-mortem: detects symptoms of the 6 failure modes and suggests fixes |

---

### Step 3 — Load the artifact

Read the artifact file. Extract:
- The artifact type and phase
- All populated sections (skip empty `{{placeholder}}` fields)
- Any A3 Decision Log entries
- The current status, version, and review status from frontmatter

Then load full artifact-scoped context using **Scope A** from `skills/ea-engagement-lifecycle/references/context-loading.md`. Announce the loaded context to the user before proceeding to Step 4.

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
- If reviewing an Architecture Vision and §2 Business Drivers lists only internal drivers, challenge whether external forces have been overlooked.
- If reviewing an Architecture Vision and §7 Strategic Direction Summary has strategies that don't link to any goal, challenge the traceability.
- If reviewing a Migration Plan and Wave 1 has no rollback procedure, ask directly about that gap.
- If reviewing an Architecture Principles artifact and a principle lacks an Implications section, probe whether the team understands the practical consequences.

Follow the selected skill's interviewing protocol exactly: one question at a time, with the question framing, recommended answer, and what a board member / critic / red-teamer would worry about.

**During Q&A — do NOT propose specific text edits or artifact changes.** Your role here is to challenge, probe, and record findings. After each user answer: acknowledge it, push back on weaknesses, note the finding internally, then ask the next question. All proposed revisions are batched and presented in Step 7 with `y/n/edit` confirmation per revision.

When asking questions, actively use the loaded context — do not treat it as passive background:
- **Brainstorm notes:** If a session noted a concern that the artifact should address, challenge whether it has been resolved.
- **Interview notes:** If a prior interview captured an answer that diverges from the artifact's current content, surface the discrepancy directly.
- **Review / grill files:** If a prior grill identified revisions that were recommended but appear unapplied, flag them.
- **Research items:** If a research item contains findings that contradict or qualify an artifact claim, cite it: `[research: {title}]`
- **Related artifacts:** If a cross-referenced artifact labels the same ID differently or states a contradicting fact, challenge the inconsistency.

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
- **practitioner** → economic framing assessment, decision quality scorecard, optionality audit, complexity heatmap, top 5 practitioner recommendations
- **maturity** → current maturity level (L1–L5), gap analysis vs next level, specific advancement actions, blockers to progress
- **failure-mode** → failure mode symptom scan (6 modes), root cause analysis for any detected, prevention recommendations, proceed/pause/redesign verdict

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

1. **Look up expected diagrams.** Read `skills/ea-artifact-templates/references/diagram-catalogue.md` — find the section for this artifact type and note the expected diagram names and standard filenames.

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
   - If yes: invoke `/ea-diagram` with the standard filename, the relevant artifact section as context, and the Mermaid starter from the diagram catalogue.
   - If no: continue.

5. **For each ⚠️ Source only:** offer to render it:
   > "Found `architecture-vision-motivation-map.mmd` but no rendered image. Run `/ea-generate png` to produce a `.png` for export."

After Step 8 is complete, ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-next.md` and output the recommendation.

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
