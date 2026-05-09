---
name: ea-interview
description: Start, export, import, or resume a stakeholder interview about an EA artifact
argument-hint: "[start|export|import|resume] [artifact|phase] [name]"
allowed-tools: [Read, Write, Glob, Bash]
---

Conduct or manage a stakeholder interview for an EA artifact.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

Delegate to the `ea-interviewer` agent for the actual interview flow. This command handles setup, routing, and file management.

---

### Mode: `start [artifact-name]`

1. Identify the target artifact. If not specified, show a list of artifacts eligible for interview (those with `Draft` status or unanswered `{{placeholder}}` fields).

2. Load the artifact file and extract all `{{placeholder}}` fields as interview questions.

3. Resolve the phase folder for the artifact (read `phase:` from artifact frontmatter and map to the folder using the Phase Folder Mapping table in `skills/ea-engagement-lifecycle/SKILL.md`). Use this folder for all note paths in this mode.

   Load any existing dated interview notes from `artifacts/{phase-folder}/notes/interviews/` for this artifact. If notes exist, ask: "Previous interview notes found (v{N}, {date}). Resume from these, or start fresh?"

3b. **Check for brainstorm notes:** Look for `EA-projects/{slug}/artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md`. Note whether it exists.

3c. **Select interview mode** — the `ea-interviewer` agent will present the mode selection menu (Web default, with Text, Voice, and Display options). Pass the artifact name and pre-loaded context; the agent handles mode selection.

4. Load artifact-scoped context using **Scope A** from `skills/ea-engagement-lifecycle/references/context-loading.md`.

   Hand off to the `ea-interviewer` agent with:
   - The artifact name and file path
   - The extracted question list
   - Any pre-existing answers from previous notes or uploaded docs
   - The selected mode (text / web / display)
   - Brainstorm notes path (if available): `artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md`
   - Loaded research items relevant to this artifact type or phase
   - Summaries of other completed artifacts in the same phase (for cross-reference awareness)
   - Prior grill review files for this artifact (so the interviewer can note whether earlier critique findings were addressed)

   The `ea-interviewer` agent must reference this context during Q&A: if a loaded research item or prior note directly supports or contradicts a user answer, it should cite it — e.g. `"Research [title] suggests {finding} — does this align with what you've described?"`

5. On interview completion:
   - Save dated notes to `artifacts/{phase-folder}/notes/interviews/interview-{artifact-id}-{YYYY-MM-DD}-v{N}.md`
   - Update the artifact file with confirmed answers
   - Update `lastModified` in `engagement.json`
   - **Refresh Executive Summary:** Read the updated artifact. Draft a 3–5 sentence executive summary covering what was decided or described, and what is still open. Present:
     > **Updated Executive Summary for {Artifact Name}:**
     > {drafted summary}
     > Accept? (y / edit / skip)
     Apply or skip per user response. Only offer if the artifact has a `## Executive Summary` section.
   - Ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md (the --next flag section)` and output the recommendation.

---

### Mode: `start phase [phase-name]`

1. Identify the target phase. If not specified, use the `currentPhase` from `engagement.json`. If no current phase, show a list:
   ```
   Select phase for interview:
   1. Preliminary
   2. Phase A — Architecture Vision
   3. Phase B — Business Architecture
   4. Phase C — Information Systems
   5. Phase D — Technology Architecture
   6. Phase E — Opportunities and Solutions
   7. Phase F — Migration Planning
   8. Phase G — Implementation Governance
   9. Phase H — Architecture Change Management
   10. Requirements Management
   ```

2. Load the question bank from `skills/ea-artifact-templates/references/phase-interview-questions.md` for the selected phase.

3. Resolve the phase folder from the selected phase using the Phase Folder Mapping table in `skills/ea-engagement-lifecycle/SKILL.md`.

   Load any existing interview notes for this phase from `artifacts/{phase-folder}/notes/interviews/interview-phase-{phase}-*`. If notes exist, ask: "Previous phase interview notes found (v{N}, {date}). Resume from these, or start fresh?"

3b. **Check for brainstorm notes:** Look for `EA-projects/{slug}/artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md`. Note whether it exists.

3c. **Select interview mode** — the `ea-interviewer` agent will present the mode selection menu. Pass the phase name and context; the agent handles mode selection.

4. Load phase-scoped context using **Scope B** from `skills/ea-engagement-lifecycle/references/context-loading.md`.

   Hand off to the `ea-interviewer` agent in **phase mode** with:
   - The phase name
   - The question list from the question bank
   - The output routing table for this phase
   - Any pre-existing answers from previous sessions
   - All artifacts that this phase's routing table targets
   - The selected mode (text / web / display)
   - Brainstorm notes path (if available): `artifacts/{phase-folder}/notes/brainstorm/brainstorm-notes.md`
   - Loaded research items relevant to this phase
   - Prior grill review files for any artifact in this phase

   The `ea-interviewer` agent must reference this context during Q&A: cite research or prior notes when they support or contradict a user's answer.

5. On interview completion:
   - Save dated notes to `artifacts/{phase-folder}/notes/interviews/interview-phase-{phase}-{YYYY-MM-DD}-v{N}.md`
   - Update target artifacts with confirmed answers (per output routing)
   - Update `lastModified` in `engagement.json`
   - **Refresh Executive Summaries:** For each updated artifact that has a `## Executive Summary` section, draft a fresh 3–5 sentence executive summary and present: `Accept? (y / edit / skip)`. Apply per user response.
   - Ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-status.md (the --next flag section)` and output the recommendation.

---

### Mode: `start engagement`

Capture the full engagement direction in one cross-phase session before any TOGAF phase work begins. Equivalent to Preliminary + Phase A combined, routing all outputs to `engagement.json → direction` only — no phase-specific artifacts are created.

1. **Load question bank.** Read `skills/ea-artifact-templates/references/phase-interview-questions.md`. Merge questions from Preliminary and Phase A into this sequence:

   - **Part 1 — Organisation & Mandate** (Prelim Q1–7): organisation context, engagement type, scope, constraints, assumptions
   - **Part 2 — Stakeholders** (Prelim Q8–11): related programmes, affected internal/external orgs, regulatory bodies
   - **Part 3 — Motivation** (Prelim Q12–17 + Phase A §2–§6): drivers (with evidence), vision, mission, goals (with rationale), objectives, strategies, issues (with evidence and raised-by), problems (with evidence and raised-by)
   - **Part 4 — Opportunities & Metrics** (Phase A §7): opportunities, success measures, baseline sources
   - **Part 5 — Programme & Risks** (Prelim Q18–20 + Phase A §10–§16): programme structure, timeline, constraints, assumptions, key risks

2. **Check for cross-cutting brainstorm notes.** Look for `EA-projects/{slug}/artifacts/cross-cutting/notes/brainstorm/brainstorm-notes.md`. If found, pass to `ea-interviewer` as pre-context — items tagged `[ISS?]`/`[PRB?]` should be promoted to formal ISS-NNN/PRB-NNN entries during this session.

3. **Check for prior engagement interview notes.** Look for any `artifacts/cross-cutting/notes/interviews/interview-engagement-*` files. If found, ask: "Prior engagement interview notes found (v{N}, {date}). Resume from these, or start fresh?"

4. **Select interview mode** — same as other modes (Text / Web / Display).

5. **Hand off to `ea-interviewer`** in engagement mode with:
   - The merged question list (sequenced as above)
   - Cross-cutting brainstorm notes (if available)
   - Any pre-existing answers from prior engagement interview notes
   - The selected mode
   - The direction quality rules from `skills/ea-engagement-lifecycle/references/grill-direction-quality.md` — loaded for inline challenge during Part 3

   **Direction Quality Challenge — Part 3 only:** After the user provides each direction item during Part 3 (Motivation), before writing it to `engagement.json`, apply the direction quality rules:
   - **Miscategorization detected:** Challenge directly — "This reads more like a {correct type} than a {entered type}. A {entered type} should {defining characteristic}. Would you like to reclassify it, or keep it as entered?"
   - **Missing evidence (Driver, Issue, Problem):** Prompt — "This item needs supporting evidence. Can you cite a source, metric, or document?" If the user skips, note the item with `⚠️ Evidence pending` in the interview notes.
   - **Ambiguous phrasing (Advisory):** Prompt — "This statement could mean different things. Could you be more specific about '{vague element}'?" If the user declines, note `ℹ️ Phrasing advisory` in the interview notes.
   - **Isolated item:** Inform — "This item has no linked {goals/drivers/objectives} yet. You can add links now or address this in `/ea-status --direction --quality` after the session."
   - Do **not** block progress — if the user declines to revise any item, accept it and continue. Flag it for the Direction Quality Summary below.

   **Direction Quality Summary — end of Part 3:** After all Part 3 items are captured, before moving to Part 4, present:
   ```
   Direction Quality Summary
   ─────────────────────────────────────────────
   Items captured: {N}   Flagged for attention: {N}

   ⚠️ Warnings (address before Phase A):
     DRV-001: Evidence pending — add source before Architecture Vision
     G-002: Reads as Objective (contains deadline) — consider reclassifying
     OBJ-001: Missing measure and deadline — cannot be validated as-is

   ℹ️ Advisory (can proceed, worth revisiting):
     STR-001: Phrasing reads as outcome — consider "Adopt X" framing

   ✅ {N} items are well-formed.

   These will appear in /ea-status --direction --quality. Continue to Part 4? (y / revisit flagged items)
   ```
   If "revisit flagged items" is chosen: step through each flagged item one at a time and allow the user to revise or accept it as-is.

6. **On completion:**
   - Save notes to `artifacts/cross-cutting/notes/interviews/interview-engagement-{YYYY-MM-DD}-v{N}.md`
   - Route confirmed answers to `engagement.json → direction`: `vision`, `mission`, `drivers[]`, `goals[]`, `objectives[]`, `strategies[]`, `issues[]`, `problems[]`, `opportunities[]`
   - Do **not** create or update any phase-specific artifact files — this session populates the direction layer only
   - Update `lastModified` in `engagement.json`
   - Confirm: "Engagement interview complete — direction captured in `engagement.json`. When you start Preliminary phase work, run `/ea-interview start phase Prelim`; when you start Phase A, run `/ea-interview start phase A`. Your answers will be available as pre-loaded context in both sessions."

---

### Mode: `export [artifact-name]`

1. Load the artifact and extract all questions (placeholder fields + guidance-derived questions).

2. Build a Word-compatible interview document using this structure:
   ```markdown
   # Interview: {Artifact Name}
   # Engagement: {Engagement Name}
   # Date: {YYYY-MM-DD}
   # Version: {N}

   ---

   ## Question 1: {Question text}
   <!-- GUIDANCE: {explanation of what this field means} -->
   **Answer:** [Write your answer here — or type SKIP or N/A]

   ## Question 2: {Question text}
   **Answer:** [Write your answer here — or type SKIP or N/A]
   ```

3. Resolve the artifact's phase folder. Write to `artifacts/{phase-folder}/notes/interviews/interview-{artifact-id}-{YYYY-MM-DD}-v{N}-export.md`

4. Convert to `.docx` — bootstrap pandoc if not already installed, then run:
   ```bash
   if ! command -v pandoc &>/dev/null; then
     echo "Installing pandoc..."
     if command -v brew &>/dev/null; then
       brew install pandoc
     elif command -v apt-get &>/dev/null; then
       sudo apt-get install -y pandoc
     else
       echo "Cannot auto-install pandoc. Skipping .docx export — interview saved as .md only."
       exit 0
     fi
   fi
   pandoc "artifacts/{phase-folder}/notes/interviews/{filename}.md" -o "artifacts/{phase-folder}/notes/interviews/{filename}.docx"
   ```

5. Confirm export location and instruct the user to fill in answers and import with `/ea-interview import`.

---

### Mode: `import [file-path]`

1. Accept a file path to a completed interview document (`.md` or `.docx`).

2. Delegate to the `ea-document-analyst` agent to parse Q&A pairs from the document.

3. Present a summary of extracted answers:
   ```
   Extracted 12 answers from interview-architecture-vision-2026-03-10-v1.docx:
   ✅ 8 answered
   ⚠️  2 skipped
   ➖ 1 N/A
   ❓ 1 unrecognised (could not map to artifact field)
   ```

4. Ask the user to confirm before applying answers to the artifact.

5. Apply confirmed answers and save dated interview notes.

6. **Refresh Executive Summary:** Read the updated artifact. Draft a 3–5 sentence executive summary and present: `Accept? (y / edit / skip)`. Apply per user response. Only offer if the artifact has a `## Executive Summary` section.

---

### Mode: `resume [artifact-name]`

1. List all interview notes for the artifact from `interviews/`, sorted by date descending.

2. Let the user select which version to resume from.

3. Load the selected notes, identify unanswered questions.

3b. **Check for brainstorm notes:** Look for `EA-projects/{slug}/brainstorm/brainstorm-notes.md`. Note whether it exists.

3c. **Select interview mode** — the `ea-interviewer` agent will present the mode selection menu. Pass context; the agent handles mode selection.

4. Hand off to the `ea-interviewer` agent to restart the interview from where it left off, passing:
   - The artifact name and file path
   - Unanswered questions from the selected notes
   - The selected mode (text / web / display)
   - Brainstorm notes path (if available): `brainstorm/brainstorm-notes.md`

5. On interview completion:
   - Save updated notes to `artifacts/{phase-folder}/notes/interviews/interview-{artifact-id}-{YYYY-MM-DD}-v{N}.md`
   - Update the artifact file with newly confirmed answers
   - Update `lastModified` in `engagement.json`
   - **Refresh Executive Summary:** Read the updated artifact. Draft a 3–5 sentence executive summary and present: `Accept? (y / edit / skip)`. Apply per user response. Only offer if the artifact has a `## Executive Summary` section.

---

### A3 Decision Rationale Capture

When the user types `a: {text}` during any interview, the `ea-interviewer` agent must follow this protocol **immediately after logging the A3 row**, before asking for governance classification (Authority/Domain/Cost/Impact/Risk):

1. Confirm the capture:
   ```
   Logged: **{Item} → {Value}** (🔄 Provisional)

   Capture the reasoning? Fill in any or all — type `skip` to skip all:

   - **Alternatives considered:** 
   - **Rationale:** 
   - **Tradeoffs accepted:** 
   - **Implications:** 
   ```

2. Parse the user's response:
   - Extract whichever of the four fields the user provided (partial responses are valid)
   - `skip` (or pressing Enter with no input) → write sentinel only

3. Write the A3.N block to the artifact file, below the A3 table and before the next `##`-level heading:
   - If the user provided any fields: write a `#### A3.N — {Item}` block with only the populated bullet lines
   - If `skip`: write `#### A3.N — {Item}\n*(rationale not captured)*`

4. Continue with governance classification (Authority/Domain/Cost/Impact/Risk) as usual.

5. **Offer detail file recording** (for ID-bearing items):
   After A3 governance classification is complete, if the item text, captured value, or assigned ISS-NNN / PRB-NNN contains a recognised ID pattern (e.g. `G-001`, `CAP-003`, `WP-007`), offer:
   > "Record this in the detail file for {ID}? Creates one if needed. (y/n)"
   - If accepted: check whether `artifacts/details/{ID}.md` exists.
     - If not: silently create it using `templates/item-detail.md` (substitute frontmatter placeholders from engagement context and parent artifact).
     - Append an entry to the **Issues** section (for ISS-NNN / PRB-NNN) or **Concerns** section (for A3 decisions or CON-NNN) in the format:
       `- [interview: {YYYY-MM-DD}] {captured text} — {ISS-NNN / PRB-NNN / A3 reference}`
     - Update `lastModified` in the detail file frontmatter to today's date.
   - If no ID is present in the item, skip this step silently.

The A3.N block format is defined in `skills/ea-artifact-templates/SKILL.md` under "A3.N Decision Rationale Blocks".

---

### Note Capture Interrupt

When the user's response starts with `n: ` (note prefix) at any point during the interview:

1. Strip the `n: ` prefix to extract the note text.
2. Determine the current phase folder from interview context (same phase mapping used elsewhere in this command).
3. Determine N: glob `EA-projects/{slug}/artifacts/{phase-folder}/notes/adhoc/note-{YYYY-MM-DD}-*.md`, count existing files and add 1.
4. Write `EA-projects/{slug}/artifacts/{phase-folder}/notes/adhoc/note-{YYYY-MM-DD}-{N}.md` with:
   ```yaml
   ---
   type: adhoc
   engagement: {name}
   phase: {phase label}
   date: {YYYY-MM-DD}
   source: interview
   parentArtifact: null
   status: Open
   resolvedDate: null
   resolvedBy: []
   crossPhase: false
   ---
   ```
   Body: note text followed by `\n\n## Resolution\n\n*(not yet resolved)*`
5. Confirm inline (do not break Q&A flow):
   ```
   📌 Note saved. _(`/ea-note resolve {path}` to record resolution when addressed)_
   Resuming interview...
   ```
6. Re-present the current question exactly as it was shown before — do not advance to the next question.

This interrupt is available in all interview modes (artifact, phase, engagement). It does not interact with A3 capture — `a:` and `n:` are independent prefixes.

---

### Interview Notes Format

All interview sessions produce dated, versioned notes:

```markdown
---
artifact: Architecture Vision
engagement: Acme Retail Transformation
interviewer: EA Facilitator
date: 2026-03-10T14:22:00Z
version: 1
status: Complete / In Progress
---

## Q: What is the strategic intent of this engagement?
**Answer:** To modernise the retail platform to support omnichannel operations.
**State:** Answered

## Q: Who are the key stakeholders?
**Answer:** ⚠️ Not answered
**State:** Skipped

## Q: What is the target architecture timeframe?
**Answer:** ➖ Not applicable
**State:** N/A
```
