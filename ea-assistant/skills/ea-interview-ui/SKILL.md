---
name: ea-interview-ui
description: >
  Render interactive React artifacts for EA interview sessions and brainstorming.
  Use the interview app when conducting structured Q&A for an artifact or phase.
  Use the brainstorm pad when capturing freeform engagement thoughts.
version: 0.3.0
---

# EA Interview UI Skill

Provides two interactive UI apps for EA interview sessions and brainstorming.

**This skill is only invoked when the user selects Web mode.** The default interview mode is Text (chat Q&A). Only load this skill when `mode = "web"` has been explicitly chosen.

**Runtime detection — choose the delivery mode before proceeding:**

| Runtime | Delivery mode |
|---|---|
| Claude Code or Claude Cowork | **React artifact** — present JSX inline |
| Any harness + `preview_artifact` MCP tool available | **MCP preview** — call `preview_artifact(html, title)` |
| OpenCode or any non-artifact environment | **HTML file** — write to disk, open in browser |

Check for MCP mode before falling back to HTML file: if the `preview_artifact` tool is listed in the available tools, use it — pass the completed HTML string and the artifact/session title. The server handles opening the browser.

Both apps are stateless — all state lives in React `useState`. A page refresh resets the form, so complete the session in one sitting before copying the output.

---

## App 1 — Interview App

**When to use:** When the user selects **Web mode** for an interview session. Not used for Text or Display modes.

### Mode A: React artifact (Claude Code / Cowork)

1. Read `references/interview-app-template.jsx`.
2. Replace the `INTERVIEW_DATA` constant (lines beginning `const INTERVIEW_DATA = {`) with the actual session data:

```js
const INTERVIEW_DATA = {
  artifactName: "<artifact or phase name>",
  engagementName: "<engagement name from engagement.json>",
  mode: "artifact",   // or "phase"
  questions: [
    {
      id: "q1",
      text: "<question text extracted from {{placeholder}} or phase question bank>",
      context: "<one-sentence explanation of why this matters>",
      defaultAnswer: "<single best-practice default, or null>",
      existingAnswer: "<value from previous session, or null>",
      brainstormNote: "<relevant thought from brainstorm-notes.md, or null>",
      suggestions: [
        { label: "<short chip label>", value: "<full answer text the user can edit>" },
        // 2–4 entries covering common good-practice answers for this question in context
        // null if no common answers are relevant
      ],
      options: ["<option 1>", "<option 2>"],  // or null — for checklist questions
      allowMultiple: true,  // false for single-select (radio); omit if options is null
    },
    // ... one entry per question
  ],
};
```

Set `options` when the question bank has enumerated choices (e.g. constraint types, data migration approaches, cut-over approaches). Set `allowMultiple: false` for single-select questions (radio buttons).

Set `suggestions` when common good-practice answers exist for the question given the engagement context. Suggestions are rendered as clickable chips labelled with `label`; clicking one loads the full `value` text into the textarea so the user can edit it before submitting. Use 2–4 suggestions per question. Suppress suggestions when `existingAnswer` is set (the user already has a prior answer to work from). Do not set both `suggestions` and `options` on the same question — use `options` for constrained enumerated choices and `suggestions` for open-ended questions with common starting points.

Set `voiceEnabled: true` when the user selects Voice mode. This adds a 🎤 microphone button to every question card:
- Clicking 🎤 starts `window.SpeechRecognition` (or `window.webkitSpeechRecognition`); button shows 🔴 Recording…
- Clicking again stops recording; the transcript is inserted into the answer text field (editable)
- If speech recognition is unavailable, the button is hidden and a note shown: "Voice input unavailable — type your answer"
- All other app behaviours (skip, N/A, default, review, copy results) are identical to Web mode

3. Present the modified JSX as a **React artifact**.

### Mode B: HTML file (OpenCode / no artifact renderer)

1. Read `references/interview-app-shell.html`.
2. Replace `%%ARTIFACT_NAME%%` with the artifact or phase name.
3. Replace `%%INTERVIEW_DATA_JSON%%` with the JSON-serialised `INTERVIEW_DATA` object (same shape as above).
4. Replace `%%COMPONENT_BODY%%` with the full body of `references/interview-app-template.jsx` — everything **after** the `import` line and `INTERVIEW_DATA` constant (i.e. from `const ANSWER_STATE` to the end of the file), excluding the final `export default` keyword (change `export default function InterviewApp` → `function InterviewApp`).
5. Write the completed HTML to `EA-projects/{slug}/ui/interview-{YYYY-MM-DD}.html`.
6. Open it in the user's browser:
   - WSL2: `cmd.exe /c start "" "$(wslpath -w EA-projects/{slug}/ui/interview-{YYYY-MM-DD}.html)"`
   - Linux/Mac: `xdg-open` / `open`
7. Tell the user: "Interview opened in your browser. Fill in your answers, then click 'Copy results' and paste back here."

**App behaviour (for reference — do not re-implement in instructions):**
- Shows one question card at a time with a progress bar
- User can: type a free-text answer (Ctrl+Enter to submit), accept the default, keep the previous answer, skip, or mark N/A
- Back navigation and "Review answers" jump are available at all times
- Review screen shows all answers with badges; each can be edited
- "Copy results to clipboard" produces a structured text block the user pastes back into the chat

**Processing the paste-back:**

When the user pastes the results block, parse each line:
- `Q{N} [Answered]: ...` + `Answer: ...` → write the answer to the artifact field
- `Q{N} [Default accepted]: ...` + `Answer: ...` → write the answer, append `✓ Default accepted`
- `Q{N} [Skipped]: ...` → write `⚠️ Not answered`
- `Q{N} [N/A]: ...` → write `➖ Not applicable`

Then save interview notes and update `engagement.json` as per the normal interview completion flow.

---

## App 2 — Brainstorm Pad

**When to use:** At the start of every `ea-brainstorm` command session, in place of the iterative chat loop.

The brainstorm pad is parameterised via a `BRAINSTORM_DATA` constant injected at render time (same pattern as `INTERVIEW_DATA` in App 1). When no phase is provided, all fields are `null` and the app shows generic hints.

### BRAINSTORM_DATA shape

```js
const BRAINSTORM_DATA = {
  phase: "<phase label, e.g. 'Phase D — Technology Architecture'>",  // null = no badge
  subtitle: "<one-sentence focus prompt>",                            // null = generic subtitle
  categories: [   // null = use all generic defaults
    { id: "concerns",      hint: "<phase-specific hint text>",
      suggestions: ["<common concern for this phase>", "<another common concern>"] },  // or omit/null
    { id: "goals",         hint: "<phase-specific hint text>",
      suggestions: ["<common goal>", "<another common goal>"] },
    { id: "constraints",   hint: "<phase-specific hint text>",
      suggestions: null },
    { id: "opportunities", hint: "<phase-specific hint text>",
      suggestions: null },
    { id: "assumptions",   hint: "<phase-specific hint text>",
      suggestions: null },
    { id: "other",         hint: "<phase-specific hint text>",
      suggestions: null },
  ],
  questions: [   // null if no artifact/phase context — upcoming interview questions shown as prompts
    {
      id: "q1",
      text: "<question that will be asked in the upcoming interview>",
      category: "concerns | goals | constraints | opportunities | assumptions | other",
    },
    // ... up to 8 questions
  ],
  prefilled: [   // null if no pre-existing answers — document/artifact answers pre-populated in pad
    {
      questionRef: "<placeholder key or question id>",
      questionText: "<full question text>",
      answer: "<pre-existing answer from document or artifact>",
      source: "<'artifact' or upload filename>",
      category: "concerns | goals | constraints | opportunities | assumptions | other",
    },
    // ...
  ],
};
```

Only `hint` and `suggestions` are overridden in `categories` — `label` and `emoji` are always taken from defaults. `suggestions` is optional: omit or set to `null` for categories where no common starters apply. When `suggestions` is set, the app renders a "💡 Thought starters" toggle inside the category card — clicking a starter adds it as a pre-filled thought entry the user can edit.

**App behaviour for `questions`:** Within each category card, show a collapsible "📋 Upcoming questions" section (collapsed by default). List each question whose `category` matches the card. This gives the user context for what topics to brainstorm before the interview.

**App behaviour for `prefilled`:** Within each category card, pre-populate a thought entry for each `prefilled` item whose `category` matches. Tag each pre-filled entry with a `📄 From: {source}` badge. The user can:
- Keep the entry as-is (it will be included in the copied results with its `📄` tag)
- Edit the text (the `📄` tag is retained so Claude can detect modifications at paste-back)
- Delete the entry (removes it entirely from the results)

### Mode A: React artifact (Claude Code / Cowork)

1. Read `references/brainstorm-app.jsx`.
2. Replace the `BRAINSTORM_DATA` constant (lines beginning `const BRAINSTORM_DATA = {`) with the actual data provided by `ea-brainstorm.md`. When no phase is active, set all fields to `null`.
3. Present the modified JSX as a **React artifact**.

### Mode B: HTML file (OpenCode / no artifact renderer)

1. Read `references/brainstorm-app-shell.html`.
2. Replace `%%BRAINSTORM_DATA_JSON%%` with the JSON-serialised `BRAINSTORM_DATA` object (same shape as above).
3. Replace `%%COMPONENT_BODY%%` with the full body of `references/brainstorm-app.jsx` — everything **after** the `import` line and `BRAINSTORM_DATA` constant (i.e. from `const DEFAULT_CATEGORIES` to end of file), changing `export default function BrainstormPad` → `function BrainstormPad`.
4. Write to `EA-projects/{slug}/ui/brainstorm-{YYYY-MM-DD}.html`.
5. Open in browser using the same platform command as the interview app.
6. Tell the user: "Brainstorm pad opened in your browser. Fill in your thoughts, click 'Done', then copy the notes and paste back here."

**App behaviour (for reference):**
- Six collapsible category cards: Concerns, Goals & Vision, Constraints, Opportunities, Assumptions, Other
- Each card shows a phase-specific hint under its label when `BRAINSTORM_DATA.categories` is set
- Phase badge shown in the header label when `BRAINSTORM_DATA.phase` is set
- Each card has one or more text inputs; Enter adds a new thought; × removes one
- "Done — show notes →" produces a formatted text block (includes `Phase:` line when scoped); user copies and pastes it into chat
- "Clear all" resets the pad

**Processing the paste-back:**

When the user pastes the `BRAINSTORM NOTES` block, parse the categories and thoughts, then:
- Identify pre-filled entries by the `[📄 From: {source}]` tag in the thought text
- Pass the full structured results (with tags intact) back to `ea-brainstorm.md` step 5b for conflict detection before saving
- After conflict resolution, append the resolved session block to `EA-projects/{slug}/brainstorm/brainstorm-notes.md`
- Follow the append and frontmatter-update rules from `ea-brainstorm.md`
- Confirm: "Saved. These notes will be available when you run `/ea-interview`."

---

## Compatibility notes

Both apps:
- Use only React hooks (`useState`, `useEffect`, `useRef`) — no external CSS or icon libraries
- Are stateless — all state lives in React `useState`; a page refresh resets the form
- **React artifact mode**: no CDN or build step required — Claude Code and Cowork bundle React
- **HTML file mode**: requires an internet connection for CDN scripts (React 18 + Babel Standalone from unpkg); total ~1 MB
- The HTML shell files use `<script type="text/babel">` so the JSX is transformed at runtime — no pre-compilation needed
