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
   - Ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-next.md` and output the recommendation.

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
   - Ask: "Want a next step suggestion? (y/n)" — if yes, apply the Next Step Algorithm from `commands/ea-next.md` and output the recommendation.

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

---

### Interview Notes Format

All interview sessions produce dated, versioned notes:

```markdown
---
artifact: Architecture Vision
engagement: Acme Retail Transformation
interviewer: EA Facilitator
date: 2026-03-10
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
