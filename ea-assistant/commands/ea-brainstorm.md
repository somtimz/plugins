---
name: ea-brainstorm
description: Capture freeform thoughts, concerns, and context about the current EA engagement — or a specific phase — for use during interviews
argument-hint: "[phase: Prelim|A|B|C|D|E|F|G|H] (optional)"
allowed-tools: [Read, Write, Glob]
---

Capture freeform brainstorm notes for the active EA engagement.

## Instructions

1. **Require an active engagement.** Check for `engagement.json` in context. If no engagement is active, prompt: "No engagement is currently active. Run `/ea-open` to open one first."

1b. **Extract slug.** Read `engagement.json` and extract the `slug` field. Use it in all file paths throughout this command (e.g. `EA-projects/{slug}/brainstorm/brainstorm-notes.md`).

2. **Resolve phase scope.** If a phase argument was provided (e.g. `/ea-brainstorm phase B`), map it to a full phase name:
   - `Prelim` → Preliminary
   - `Req` or `Requirements` → Architecture Requirements Management
   - `A` → Architecture Vision
   - `B` → Business Architecture
   - `C` → Information Systems Architecture
   - `D` → Technology Architecture
   - `E` → Opportunities & Solutions
   - `F` → Migration Planning
   - `G` → Implementation Governance
   - `H` → Architecture Change Management

   Note the phase scope for use in the session header and opening prompt.

3. **Check for existing notes.** Look for `EA-projects/{slug}/brainstorm/brainstorm-notes.md`.
   - If found, read the frontmatter to get `sessions` and `lastUpdated`.
   - Show: "You have {N} brainstorm session(s) — last updated {date}."
   - Offer: "Would you like to view existing notes first, or go straight to adding new thoughts?"
   - If the user wants to view, display the full file content, then ask if they want to add more.
   - If not found, continue silently to the capture session.

4. **Launch the brainstorm pad.** Load the `ea-interview-ui` skill and present the **Brainstorm Pad** artifact.
   - If phase-scoped, announce before opening: "Opening a brainstorm pad scoped to {Phase Name}. Fill in thoughts freely across any category, then click 'Done' and paste the results back."
   - If not phase-scoped: "Opening the brainstorm pad. Fill in any thoughts across the categories, then click 'Done' and paste the results back."
   - The app handles all input — do not run a parallel chat Q&A.

5. **Wait for the user to paste their notes.** The app's result screen has a "Copy to clipboard" button. When the user pastes the `BRAINSTORM NOTES` block back into the chat, proceed to step 6.

6. **Save the pasted notes.** Parse the `BRAINSTORM NOTES` block from the user's paste. The categories are already structured by the app (Concerns / Goals & Vision / Constraints / Opportunities / Assumptions / Other) — use them as-is; do not re-categorise.

   **Append** a new session block to `EA-projects/{slug}/brainstorm/brainstorm-notes.md`. Never overwrite prior sessions. If the file does not exist, create it.

   **File format:**
   ```markdown
   ---
   engagement: {name}
   lastUpdated: YYYY-MM-DD
   sessions: N
   ---

   ## Session N — YYYY-MM-DD [Phase B — Business Architecture] (only if phase-scoped)

   ### Concerns
   - {thought}

   ### Goals & Vision
   - {thought}

   ### Constraints
   - {thought}

   ### Opportunities
   - {thought}

   ### Assumptions
   - {thought}

   ### Other
   - {thought}
   ```

   When creating the file for the first time, set `sessions: 1` in the frontmatter.

   When updating an existing file:
   - Increment `sessions` by 1 in the frontmatter
   - Update `lastUpdated` to today's date
   - Append the new session block after all existing content

7. **Confirm.** After saving:
   > "Saved. These notes will be available when you run `/ea-interview` — the interviewer will reference relevant thoughts as it asks questions."

   If this was a phase-scoped session, also note:
   > "You can also open the phase directly with `/ea-phase {phase}` and select 'Brainstorm about this phase' from the next actions."
