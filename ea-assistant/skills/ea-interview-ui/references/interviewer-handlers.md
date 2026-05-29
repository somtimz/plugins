# Interviewer Handler Protocols

Detailed protocols for interview pause handlers and A3 decision recording.
Loaded by `ea-interviewer` when a handler is triggered — do not inline these in the agent definition.

---

## Research Pause Handler (`r: {query}` / `research: {query}`)

At any point during a Text interview, the user can trigger a research pause by typing `r: {query}` or `research: {query}` (e.g., `r: what are the regulatory drivers for EU data governance`).

When triggered:

1. Extract the query string from the input.
2. Acknowledge: `🔍 Research pause — looking up: "{query}"`
3. Search `ResearchAndReferences/research-index.md` for items whose tags or title contain terms from the query. If matching items are found, read each item's content and summarise the most relevant points (cite title + key points, max 3–5 bullets per item).
4. Perform a targeted synthesis on the query — draw on training knowledge, cite sources where possible, flag confidence level (High / Medium / Low).
5. Present findings:
   ```
   ## Research Findings: {query}

   **From engagement library:**
   - {matched item title}: {key points} [or "No matching items in ResearchAndReferences/"]

   **Broader synthesis:**
   - {key finding 1}
   - {key finding 2}
   - {key finding 3}

   Confidence: {High / Medium / Low} — {one-sentence caveat if Medium or Low}
   ```
6. Offer to save:
   > `Save these findings to ResearchAndReferences? (y / n / edit title)`
   - `y` → write `ResearchAndReferences/{slug}-research-{YYYYMMDD}.md` with frontmatter:
     ```yaml
     researchType: note
     title: {query}
     addedDate: {today ISO 8601}
     tags: [{current artifact type}, {current phase}]
     ```
     Append an entry to `ResearchAndReferences/research-index.md`. Confirm: "Saved to ResearchAndReferences."
   - `n` → findings remain in-session context only; continue without saving.
   - `edit title` → prompt: "Title for this research note?" then save with the user's title.
7. Resume: `Resuming — Q{N} of {total}: {question text}`

The saved (or unsaved) findings are available as context for all remaining questions in this session — the interviewer should reference them if relevant to subsequent answers.

---

## Economic Framing Pause Handler (`e: {statement}`)

At any point during a Text interview, the user can trigger an economic framing pause by typing `e: {statement}` (e.g., `e: Moving to cloud will save money`).

When triggered:

1. Extract the statement string.
2. Acknowledge: `💰 Economic framing pause — evaluating: "{statement}"`
3. Prompt the user with structured economic questions:
   ```
   Let's frame this in economic terms:
     - Cost: What is the estimated cost (build, run, change) of this over 3 years?
     - Risk: What risk does this reduce or introduce? Quantify if possible.
     - Value: What measurable value does this create — revenue, efficiency, optionality?
     - TCO: How does this compare to the current state on total cost of ownership?
   Press Enter to skip any field.
   ```
4. Capture the user's responses and append them as an inline note to the current answer (or to the interview notes if no current answer is being framed).
5. Tag the note as `[Economic framing]` in the interview log.
6. Resume: `Resuming — Q{N} of {total}: {question text}`

This pause helps ensure architecture content is legible in financial terms — a key differentiator between L3+ and lower-maturity practice.

---

## Decide/Defer Pause Handler (`d: {statement}`)

At any point during a Text interview, the user can trigger a decision-quality pause by typing `d: {statement}` (e.g., `d: We should adopt a microservices architecture`).

When triggered:

1. Extract the statement string.
2. Acknowledge: `⚖️ Decision quality pause — assessing: "{statement}"`
3. Run the **5-factor Decide vs Defer assessment**:
   ```
   Decide vs Defer — 5-factor assessment

   Factor 1 — Evidence: How much evidence supports this decision right now?
     [ ] Strong — benchmarks, POCs, or reference implementations confirm the approach
     [ ] Moderate — some data, but gaps remain
     [ ] Weak — mostly opinion, analogy, or vendor claims

   Factor 2 — Reversibility: If this decision is wrong, how hard is it to undo?
     [ ] High — can reverse within 6 months with minimal cost
     [ ] Medium — reversible within 12 months, moderate cost
     [ ] Low — irreversible or very expensive to undo

   Factor 3 — Impact: What is the blast radius if this decision is wrong?
     [ ] Low — affects one team or system
     [ ] Medium — affects multiple teams or a domain
     [ ] High — affects the entire enterprise or is hard to reverse

   Factor 4 — Urgency: What happens if we delay this decision by 90 days?
     [ ] No harm — waiting improves evidence or alignment
     [ ] Some cost — minor delay to downstream work
     [ ] Critical — blocks committed deliverables or regulatory deadlines

   Factor 5 — Capability: Do we have the skills and capacity to execute this now?
     [ ] Ready — team has done this before
     [ ] Learnable — training or coaching closes the gap
     [ ] Gap — significant capability missing, may need external support
   ```
4. Prompt the user to rate each factor (1–3 or descriptive). If the user presses Enter for all factors, default to **Moderate / Medium / Medium / No harm / Learnable**.
5. Compute the verdict based on the responses:

   | Pattern | Verdict | Action |
   |---|---|---|
   | Evidence = Strong, Reversibility = High, Capability = Ready/Learnable | **Decide now** — sufficient evidence, low risk | Log to A3 as committed decision; offer to create ADR |
   | Evidence = Weak OR Reversibility = Low OR Impact = High | **Defer** — create PAD-NNN | Offer to create a Pending Architecture Decision |
   | Evidence = Moderate, Reversibility = Medium, Urgency = Some cost | **Decide with guardrails** — commit with constraints | Log to A3; add guardrails note; schedule evidence review |
   | Any specific technology/pattern chosen in Phase A before B–D analysis | **Premature** — likely wrong timing | Flag as premature; convert to PAD-NNN with constraint boundaries |
   | Urgency = Critical AND Evidence = Weak | **Risky commit** — high pressure, low evidence | Log to A3 with risk flag; require executive sign-off |

6. Present the verdict and recommended action:
   ```
   Verdict: {verdict}
   Rationale: {one-sentence rationale based on factor scores}
   Recommended action: {action from table above}
   ```

7. Execute the recommended action:
   - **Decide now:** proceed to A3 logging (same flow as `a:` handler).
   - **Defer:** offer to create PAD-NNN:
     ```
     This decision should be deferred. Create a Pending Architecture Decision (PAD-NNN)?
     A PAD captures the constraint boundaries, evidence needed, and resolution path
     so the decision isn't forgotten or made prematurely.
     (y / n)
     ```
     If **yes**: invoke `/ea-adrs new --type pad` (or equivalent PAD creation flow) with pre-populated fields:
     - Title: derived from the statement
     - Phase: current phase
     - Constraint boundaries: any MUST requirements or principles from the interview context
     - Evidence required: inferred from Weak/Moderate factors
     - Resolution path: suggested phase/work package
     - Expiry date: today + 90 days default
     After creating the PAD, confirm the PAD-NNN ID and note it in the interview log.
   - **Decide with guardrails:** log to A3 with a `Guardrails:` note (e.g., "Reversible within 6 months; review at Phase E").
   - **Premature:** flag the concern and convert to PAD-NNN with `premature: true` and constraint boundaries.
   - **Risky commit:** log to A3 with `Risk flag: Evidence insufficient under urgency pressure` and require executive sign-off note.

8. Resume: `Resuming — Q{N} of {total}: {question text}`

This pause prevents premature commitments, reduces decision rework, and links deferred decisions to the engagement's evidence pipeline.

---

## Contextual Help Handler (`?` / `help`)

When the user types `?` or `help` at any interview prompt:

1. **Show shortcuts reference** (same block shown at session start).

2. **Show current context:**
   ```
   Current context:
     Artifact : {artifact name}
     Phase    : {ADM phase}
     Question : Q{N} of {total} — {question text}
     Progress : {answered} answered, {skipped} skipped, {N/A} N/A, {remaining} remaining
   ```

3. **Show artifact guidance** — load `skills/ea-artifact-templates/references/artifact-descriptions.md` and find the section for the current artifact. Display its **Purpose**, **Audience**, and **When to Create** fields only (not full content). If the artifact is not in that file, show: "No description available for this artifact."

4. **Show phase guidance** — one sentence explaining the current ADM phase's objective from `skills/ea-engagement-lifecycle/references/adm-phase-guide.md`.

5. **Show concept reference hint:**
   > 💡 For definitions of Principle, Goal, Strategy, Plan, and Risk — type `concepts` or see `skills/ea-artifact-templates/references/ea-concepts.md`

6. **Offer opt-out reminder:**
   > To opt out of this question: type `opt-out`
   > To opt out of this entire artifact: type `opt-out artifact`

7. Resume: **"Back to Q{N}: {question text}"** and wait for the user's answer.

If the user types `concepts` at any prompt, load and display the Quick Reference Table from `ea-concepts.md` only (not the full file), then resume.

---

## Opt-Out (question) Handler (`opt-out`)

When the user types `opt-out` at a question prompt:

1. Prompt:
   > Reason for opting out of this question? (Press Enter to skip)

   Accept freeform text or Enter.

2. Write `⊘ Opted out` (or `⊘ Opted out — {reason}` if reason given) to the artifact field, replacing the `{{placeholder}}`.

3. Append to `engagement.json` → `optOuts[]`:
   ```json
   {
     "type": "question",
     "artifactId": "{current artifact id}",
     "questionRef": "{placeholder key, e.g. executive_summary}",
     "reason": "{reason or empty string}",
     "timestamp": "{ISO 8601}"
   }
   ```

4. Count as **Opted Out** (separate from Skipped) in session completion summary.

5. Confirm briefly: "Noted — opted out. Moving on." Then continue to the next question.

---

## Opt-Out (artifact) Handler (`opt-out artifact`)

When the user types `opt-out artifact` during an interview:

1. Confirm:
   > Opt out of the entire **{artifact name}** artifact?
   > All unanswered fields will be marked `⊘ Opted out`. This will be visible in status reports.
   > **1.** Yes, opt out   **2.** No, continue the interview

2. If **No**: resume the current question.

3. If **Yes**: prompt for reason:
   > Reason for opting out? (Press Enter to skip)

4. Write `⊘ Opted out` to all remaining `{{placeholder}}` fields in the artifact.

5. Append to `engagement.json` → `optOuts[]`:
   ```json
   {
     "type": "artifact",
     "artifactId": "{artifact id}",
     "reason": "{reason or empty string}",
     "timestamp": "{ISO 8601}"
   }
   ```

6. End the interview session and proceed to session completion (step 4). In the session log, note: `Artifact opted out — {reason}`.

---

## Recording Decisions to Appendix A3

At any point during a Text interview, the user can log a governance decision to the artifact's Appendix A3 table by typing `a` or `decision` after providing an answer, or by prefixing their input with `a:` (e.g., `a: We will adopt API-first integration`).

When triggered:
1. Write the decision item and value to the current question's artifact field as normal.
2. Set the initial governance state to `🔄 Provisional`.
3. Prompt for the five A3 classification fields:

   ```
   Classify this decision for the Decision Register:
     Authority  [Strategic / Tactical / Operational]:
     Domain     [Business / Data / App / Tech / Cross]:
     Cost       [High / Med / Low / TBD]:
     Impact     [High / Med / Low / TBD]:
     Risk       [High / Med / Low / TBD]:
     Subject    (one or two words, e.g. "Cloud strategy"):
   Press Enter to accept defaults: Tactical / Cross / TBD / TBD / TBD / blank
   ```

4. Record `Captured By` as the facilitator name if one was established at session start; otherwise use `EA Facilitator`.
5. Record `Owner` as the owner name if one was established at session start; otherwise leave as `⚠️ Not assigned`.
6. Append the fully populated row to `## Appendix A3 — Decision Log` in the artifact file. If the section contains only the placeholder row (`*(no decisions recorded)*`), replace it.
7. Confirm: "Decision logged to A3 — run `/ea-decisions` at any time to generate the Decision Register."
8. **ADR suggestion check** — after the A3 row is written, evaluate the decision against the ADR threshold:

   Count how many of these indicators apply:
   - The decision involves a technology or vendor selection
   - The decision is described as hard to reverse or affects multiple phases
   - Cost column = High
   - Risk column = High
   - The decision involves a make-vs-buy or build-vs-configure choice
   - The decision affects data governance, security architecture, or compliance
   - The decision contradicts or refines an architecture principle
   - A concern was raised about this decision (A4 row exists)

   If **2 or more** indicators apply:
   ```
   💡 ADR suggestion: This decision may warrant a full Architecture Decision Record.

   Indicators matched: {list matched indicators}

   An ADR documents the options you considered, why you chose this approach, and
   what the consequences are — so future architects understand the rationale.

   Create an ADR for this decision? (y/n)
   ```
   If yes: invoke `/ea-adrs new` with pre-populated metadata:
   - Title: derived from the `Subject` field of the A3 row
   - Phase: current artifact's phase
   - Decision Owner: A3 `Owner` value
   - Related business drivers or goals: any DRV/G-NNN IDs found in the answer
   - Triggering artifact: current artifact name + current section
   After creating the ADR, add the ADR-NNN to the A3 row's `Notes` column.

9. **Advanced decision quality check (optional, L3+):** After the A3 row is written and the ADR check is complete, if the decision has `Authority = Strategic` or `Cost = High` or `Risk = High`, offer:
   ```
   💡 Practitioner check: Would you like to run the Decide vs Defer assessment on this decision?
   This evaluates evidence, reversibility, impact, urgency, and capability to determine
   whether the decision is ready to commit, should be deferred, or needs guardrails.
   ```
   If the user accepts, run the same 5-factor assessment as the `d:` handler (see Decide/Defer Pause Handler above), adapted to the already-captured decision:

   - **Factor 1 — Evidence:** What evidence supports this decision? (Strong / Moderate / Weak)
   - **Factor 2 — Reversibility:** Can this be undone within 6 months without major cost? (High / Medium / Low)
   - **Factor 3 — Impact:** If wrong, how many teams or systems are affected? (Low / Medium / High)
   - **Factor 4 — Urgency:** What happens if delayed 90 days? (No harm / Some cost / Critical)
   - **Factor 5 — Capability:** Does the team have the skills to execute? (Ready / Learnable / Gap)

   Compute the verdict and present it with the same action table as the `d:` handler.

   Append the assessment results as a structured note to the A3 row:
   ```
   Decide vs Defer Assessment:
     Evidence: {rating} — {brief note}
     Reversibility: {rating} — {brief note}
     Impact: {rating} — {brief note}
     Urgency: {rating} — {brief note}
     Capability: {rating} — {brief note}
     Verdict: {Decide now / Defer / Decide with guardrails / Premature / Risky commit}
     Action: {action taken}
   ```

   If the verdict is **Defer** or **Premature**, update the A3 row `State` to `⏸️ Deferred` and create a PAD-NNN (or link to an existing one) in the `Notes` column.
   If the verdict is **Decide with guardrails**, add a `Guardrails:` note to the A3 row.
   If the verdict is **Risky commit**, add `Risk flag: Evidence insufficient under urgency pressure` and require executive sign-off in the `Notes` column.

   This links to `practitioner-tips.md` Tip #51 (Decide vs Defer Matrix), Move #26 (5-factor assessment), and Move #27 (convert premature decisions to PADs).

---

## Interview Mode Details

### Mode 1 — Web Interview

Load the `ea-interview-ui` skill and present the **Interview App** artifact.
- Build the `questions` array: for each extracted question, include `text`, `context` (one sentence on why it matters), `defaultAnswer` if applicable, `existingAnswer` from any previous session, `brainstormNote` for any semantically related thought from the loaded notes (first 80-char identifier added to shown-notes list once populated), `suggestions` (see below), and `options` / `allowMultiple` where the question has enumerated choices.
- Set `artifactName` and `engagementName` from engagement context.
- Set `voiceEnabled: false`.

Wait for the user to paste the `INTERVIEW RESULTS —` block back into the chat, then process it (step 4).

### Mode 2 — Voice Interview

Load the `ea-interview-ui` skill and present the **Interview App** artifact in voice mode.
- Build the `questions` array the same as Web mode.
- Set `voiceEnabled: true` — this enables the 🎤 microphone button on every question card.

**How voice mode works in the app:**
- Each question card shows a 🎤 **Record** button alongside the text input field
- Clicking 🎤 starts the browser's Web Speech API (`SpeechRecognition`); the button turns red (🔴 Recording…)
- Clicking again stops recording; the transcript is inserted into the answer text field
- The user can edit the transcript before moving on — voice is a starting point, not final
- If speech recognition is unavailable (unsupported browser or no microphone), the 🎤 button is hidden and the field falls back to text input only; a note is shown: "Voice input unavailable — type your answer"
- All other app behaviours (skip, N/A, default, review screen, copy results) work identically to Web mode

Wait for the user to paste the `INTERVIEW RESULTS —` block back into the chat, then process it (step 4).

### Mode 4 — Display

Output all questions as a formatted read-only list:

```
**Interview: {artifactName}** — {engagementName}
{N} questions

1. {question text}
   *{context}*
…
```

After displaying, ask: "Ready to start? **1** Web (default) / **2** Voice / **3** Text"
Branch to Mode 1, 2, or 3 above.

---

## Building Suggestions

For each question, generate 2–4 `suggestions` entries covering common good-practice answers relevant to the engagement context (engagementType, industry if known, current phase). Suggestions are short, actionable answer texts — not abstract labels. Rules:
- Only generate suggestions for open-ended free-text questions. Omit (set `null`) when the question already has `options` (enumerated checklist).
- Omit when `existingAnswer` is set — the user already has a starting point.
- Calibrate suggestions to the engagement: a greenfield cloud migration gets different suggestions than a legacy-modernisation programme.
- Keep each suggestion under 120 characters so it fits in the UI chip.
- Example for "What is the primary cloud adoption strategy?": `[{label:"Cloud-first", value:"Migrate all new workloads to public cloud; retain on-prem only for regulated data"}, {label:"Hybrid", value:"Balance on-prem and public cloud based on workload classification and data sovereignty"}, {label:"On-prem preferred", value:"Maintain on-premises as default; use cloud for overflow capacity and DR only"}]`

---

## Session Log Format

When creating `interviews/session-log.md`, use this header:

```markdown
---
engagement: {engagement_name}
slug: {slug}
created: {YYYY-MM-DD}
---

# Interview Session Log — {engagement_name}

This log records all interview sessions for this engagement in chronological order.
Each entry captures who participated, what was covered, and the recommended next step.

---
```

**Append** this session entry for each session (whether creating or updating):

```markdown
## Session — {YYYY-MM-DD HH:MM}

| Field | Value |
|---|---|
| Artifact / Phase | {artifact name or phase} |
| Facilitator | {sessionFacilitator} |
| Participants | {sessionParticipants} |
| Duration | {start time} – {end time} (approx) |
| Questions covered | {questionsCovered} answered, {questionsSkipped} skipped, {questionsNA} N/A, {questionsOptedOut} opted out |
| Key topics | {keyTopics} |
| Off-topic flags | {offTopicFlags} flagged{; {flaggedArtifacts} if non-empty} |
| Next logical step | {nextLogicalStep} |

*Interview notes: `interviews/interview-{artifact-id}-{YYYY-MM-DD}-v{N}.md`*

---
```

---

## Interview Note Format

```markdown
---
artifact: {artifact name}
engagement: {engagement name}
facilitator: {sessionFacilitator}
participants: {sessionParticipants}
date: {YYYY-MM-DD}
version: {N}
status: Complete / In Progress
---

## Q: {question text}
**Answer:** {answer or state marker}
**State:** Answered / Skipped / N/A / AI Draft

## Flagged for Later
- [{HH:MM}] {flagged content} → suggested artifact: {artifact} / field: {field}
```

*(The `## Flagged for Later` section is appended only when cross-topic Option 2 is selected; omit if no flags were raised.)*

---

## Inline Brainstorm Mode

At any point during an interview, the user can trigger a brainstorm pause by typing any of:
- "brainstorm", "let me think", "I have some thoughts", "b:", or "pause to brainstorm"

When triggered:
1. Pause the interview and acknowledge: "Sure — share your thoughts freely. Type 'resume' (or 'done', 'continue', 'back') when you're ready to go on."
2. Accept freeform input from the user across one or more messages.
3. When the user signals they are done (types "resume", "done", "continue", or "back"):
   - Categorise the captured thoughts (Concerns / Goals & Vision / Constraints / Opportunities / Assumptions / Other).
   - Quietly append them as a new session block to `brainstorm/brainstorm-notes.md` (creating the file with correct frontmatter if it does not yet exist), tagged with today's date and labelled `[Inline — during interview]`.
   - Add the newly captured notes to the in-memory brainstorm context. They start as unsurfaced (not in the shown-notes list) and are eligible for surfacing on remaining questions.
   - Confirm: "Notes saved. Resuming the interview."
   - Immediately scan the newly added notes for relevance to the *current* question and all remaining questions.
   - Resume: "We were on Question {N} of {total}: {question text}"
4. The just-captured thoughts are available as context for all remaining questions in the session — apply the same `💭` and `💡` surfacing rules and shown-notes tracking.

---

## Governance State Transitions (A3 rows)

After any interview session, the user may update the governance state of any A3 row by typing `govern` or `g` followed by a row number. Use the governance states, emoji markers, and transition path defined in `skills/ea-artifact-templates/SKILL.md` (Governance State Markers section). Write the updated state back to the A3 row in the artifact file.