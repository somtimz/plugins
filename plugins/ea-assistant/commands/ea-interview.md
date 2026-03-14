---
name: ea-interview
description: Start, export, import, or resume a stakeholder interview about an EA artifact
argument-hint: "[start|export|import|resume] [artifact-name]"
allowed-tools: [Read, Write, Bash]
---

Conduct or manage a stakeholder interview for an EA artifact.

## Instructions

If no engagement is active in context, prompt the user to run `/ea-open` first.

Delegate to the `ea-interviewer` agent for the actual interview flow. This command handles setup, routing, and file management.

---

### Mode: `start [artifact-name]`

1. Identify the target artifact. If not specified, show a list of artifacts eligible for interview (those with `Draft` status or unanswered `{{placeholder}}` fields).

2. Load the artifact file and extract all `{{placeholder}}` fields as interview questions.

3. Load any existing dated interview notes from `interviews/` for this artifact. If notes exist, ask: "Previous interview notes found (v{N}, {date}). Resume from these, or start fresh?"

4. Hand off to the `ea-interviewer` agent with:
   - The artifact name and file path
   - The extracted question list
   - Any pre-existing answers from previous notes or uploaded docs
   - Interview rules: one question at a time, skip/N/A/default options

5. On interview completion:
   - Save dated notes to `interviews/interview-{artifact-id}-{YYYY-MM-DD}-v{N}.md`
   - Update the artifact file with confirmed answers
   - Update `lastModified` in `engagement.json`

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

3. Write to `interviews/interview-{artifact-id}-{YYYY-MM-DD}-v{N}-export.md`

4. If `pandoc` is available, convert to `.docx`:
   ```bash
   pandoc interviews/{filename}.md -o interviews/{filename}.docx
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

3. Load the selected notes, identify unanswered questions, and restart the interview from where it left off using the `ea-interviewer` agent.

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
