---
name: ea-workshop
description: Facilitate a multi-stakeholder architecture workshop — structured agenda, group capture, and outcome tracking
argument-hint: "[start [artifact <name>|phase <phase>|topic <text>] | resume <WS-NNN> | export <WS-NNN> | list]"
allowed-tools: [Read, Write, Glob, Bash]
---

Facilitate a multi-stakeholder architecture workshop with structured agenda, outcome capture, and integration with the EA decision and concerns registers.

## Engagement Resolution

Check conversation context for the active engagement slug. If none found, scan `EA-projects/*/engagement.json` and display a numbered list; ask the user to select one. Load `engagement.json`.

## Dispatcher

1. Read the argument (if any).
2. Dispatch:
   - `start [artifact <name> | phase <phase> | topic <text>]` → Mode: Start
   - `resume <WS-NNN>` → Mode: Resume
   - `export <WS-NNN>` → Mode: Export
   - `list` → Mode: List
   - No argument → display menu:
     ```
     EA Workshop

       1. Start new workshop
       2. Resume workshop (WS-NNN)
       3. Export workshop (WS-NNN)
       4. List workshops

     Select (1–4) or Enter to exit:
     ```

---

## Mode: Start

Create and run a new workshop session.

### Step 1 — Determine Next WS Number

Scan `EA-projects/{slug}/artifacts/**/workshops/workshop-minutes-*.md`. Parse the WS-NNN from each filename. Assign the next number as `WS-{NNN}` (zero-padded to 3 digits). If no workshops exist, start at `WS-001`.

### Step 2 — Collect Workshop Header

Collect:
- **Title** (required) — short workshop title (e.g. "Phase A Visioning Workshop")
- **Date** (default: today's date)
- **Facilitator** (required) — name of the facilitator
- **Location / Platform** (default: "Video call")
- **Scope** — what this workshop covers:
  - `artifact <name>` (if provided as argument) — pre-fill scope from artifact name
  - `phase <phase>` (if provided) — pre-fill scope from phase name
  - `topic <text>` (if provided) — pre-fill scope from topic text
  - Otherwise ask: "What will this workshop cover? (artifact name, phase, or topic)"

### Step 3 — Collect Attendees

Ask for attendees one at a time:
```
Attendee 1 — Name and role (or press Enter when done):
```
Repeat until user presses Enter. Require at least 2 attendees.

Ask: "Minimum number of voting members required for quorum? (press Enter to skip)"

### Step 4 — Build Agenda

Ask for agenda items one at a time:
```
Agenda item 1 — Description (or press Enter when done):
  Time-box in minutes (optional):
```

If the scope is an artifact or phase, offer a default agenda based on it. For example, if scope is `artifact architecture-vision`:
- Current state review
- Target state discussion
- Decision capture
- Open items and parking lot
- Next steps and actions

The user can accept the default or replace it.

### Step 5 — Determine Storage Path

- If scope is a phase (`phase <phase>`): resolve the phase folder (e.g. `A` → `phase-a`). Use `artifacts/{phase-folder}/workshops/`.
- If scope is an artifact: use the artifact's phase folder + `/workshops/`.
- If scope is a topic or no scope: use `artifacts/cross-cutting/workshops/`.

Create the folder if it does not exist.

### Step 6 — Create Workshop Minutes File

1. Read `templates/workshop-minutes.md` as the template.
2. Replace all `{{placeholder}}` tokens with collected values.
3. Write to: `EA-projects/{slug}/{storage-path}/workshop-minutes-{NNN}-{YYYY-MM-DD}.md`
4. Register in `engagement.json → artifacts[]`:
   ```json
   {
     "id": "workshop-{NNN}",
     "name": "{title}",
     "workshopId": "WS-{NNN}",
     "phase": "{phase or cross-cutting}",
     "file": "{storage-path}/workshop-minutes-{NNN}-{YYYY-MM-DD}.md",
     "status": "In Progress",
     "type": "workshop-minutes",
     "createdAt": "{ISO 8601}",
     "lastModified": "{ISO 8601}"
   }
   ```
5. Update `engagement.json → lastModified`.

### Step 7 — Run Facilitated Session

Hand off to the `ea-facilitator` agent in Workshop Facilitation Mode, providing:
- Workshop file path
- Attendee list
- Agenda items with time-boxes
- Engagement direction context (from `engagement.json`)
- Scope artifact/phase/topic

The facilitator runs each agenda item, capturing outcomes in the workshop file.

---

## Mode: Resume

Resume an in-progress workshop.

1. If no WS-NNN provided, scan workshops and show list; ask which to resume.
2. Find the file: `EA-projects/{slug}/artifacts/**/workshops/workshop-minutes-{NNN}-*.md`.
3. Read the file. Display what is complete (agenda items with status "Covered") and what remains.
4. Hand off to `ea-facilitator` in Workshop Facilitation Mode to continue from the next incomplete agenda item.

---

## Mode: Export

Export workshop minutes to Word format.

1. Find the workshop file by WS-NNN.
2. Invoke `/ea-generate` with the workshop minutes file and `docx` format.

---

## Mode: List

Display all workshops for the active engagement.

Scan `EA-projects/{slug}/artifacts/**/workshops/workshop-minutes-*.md`. For each file, read frontmatter (`workshopId`, `title`, `date`, `status`, `facilitator`).

Display:
```
Workshops — {engagement name}

  WS-001  2026-05-01  Architecture Vision Visioning          Facilitator: Jane  Status: Complete    Attendees: 5
  WS-002  2026-05-10  Phase B Business Architecture Review   Facilitator: Jane  Status: In Progress Attendees: 4

{N} workshops total.
```

If no workshops exist: `No workshops recorded for this engagement. Run '/ea-workshop start' to create one.`
