---
name: ea-arb
description: Create, manage, and view Architecture Review Board meeting minutes — link decisions to the ADR register and concerns register
argument-hint: "[new | council [ARB-NNN] | list | view <ARB-NNN> | close <ARB-NNN>]"
allowed-tools: [Read, Write, Glob, Grep, Bash]
---

Manage Architecture Review Board (ARB) meeting minutes for the active engagement.

> The **ARB** is the engagement's strategic architecture governance body — the forum that ratifies hard-to-reverse decisions, governs principles/dispensations, and gates phase conformance. For its role and function within the governance model, see `skills/ea-engagement-lifecycle/references/governance-framework.md` → **The Architecture Review Board (ARB)**; for its duties, membership, and RACI, see `references/role-catalogue.md`. This command manages the **minutes** (`ARB-NNN`) — the record of what the board decided.

## Engagement Resolution

Check conversation context for the active engagement slug. If none found, scan `EA-projects/*/engagement.json` and display a numbered list; ask the user to select one. Load `engagement.json`.

## Dispatcher

1. Read the argument (if any).
2. Dispatch:
   - `new` → Mode: New
   - `council [ARB-NNN]` → Mode: Council
   - `list` → Mode: List
   - `view <ARB-NNN>` → Mode: View
   - `close <ARB-NNN>` → Mode: Close
   - No argument → display menu:
     ```
     ARB Meeting Minutes — {engagement name}

       1. New ARB minutes
       2. Convene the ARB council (panel review + vote)
       3. List ARB meetings
       4. View ARB-NNN
       5. Close ARB-NNN (approve minutes)

     Select (1–5) or Enter to exit:
     ```

---

## Mode: New

Create a new ARB minutes document.

### Step 1 — Determine Next ARB Number

Scan `EA-projects/{slug}/artifacts/cross-cutting/arb-minutes-*.md`. Parse ARB-NNN from each filename. Assign the next number as `ARB-{NNN}` (zero-padded to 3 digits). If none exist, start at `ARB-001`.

### Step 2 — Collect Meeting Details

Ask:
- **Date** (default: today's date)
- **Chair** (required) — name of the ARB chair
- **Secretary** (required) — name of the secretary (may be same as facilitator)
- **Quorum required** — minimum number of voting members for a valid meeting (press Enter to skip)
- **Location / Platform** (default: "Video call")

### Step 3 — Collect Attendees

Ask for attendees one at a time:
```
Attendee 1 — Name, role, voting member? (Y/N) (or press Enter when done):
```
Repeat until user presses Enter. Require at least 2 attendees.

Determine whether quorum is met based on the count of voting members present vs. quorum required. If quorum is not met: inform the user that decisions will be flagged `🔄 Provisional — pending quorum confirmation`.

### Step 4 — Build Agenda

Ask for agenda items one at a time:
```
Agenda item 1 — Description (or press Enter when done):
  Presenter:
  Time-box in minutes (optional):
```
Repeat until user presses Enter.

**Pre-populate with open ADRs:** After collecting agenda items, offer:
```
Pre-populate agenda with open ADRs? (y/n)
```
If yes, scan `EA-projects/{slug}/artifacts/adr-*.md` for ADRs with status `Candidate` or `In Progress`. List them and ask which to add as agenda items (multiple select allowed).

**Pre-populate deferred items from prior ARB:** If a prior ARB minutes file exists (highest ARB number), scan its `## Deferred Items` table for items without "Resolved" status. Offer to carry them forward as agenda items.

### Step 5 — Create ARB Minutes File

1. Read `templates/cross-cutting/arb-minutes.md` as the template.
2. Replace all `{{placeholder}}` tokens with collected values.
3. Write to: `EA-projects/{slug}/artifacts/cross-cutting/arb-minutes-{NNN}-{YYYY-MM-DD}.md`
4. Create `artifacts/cross-cutting/` folder if it does not exist.
5. Register in `engagement.json → artifacts[]`:
   ```json
   {
     "id": "arb-{NNN}",
     "name": "ARB Meeting {NNN} — {YYYY-MM-DD}",
     "arbId": "ARB-{NNN}",
     "phase": "cross-cutting",
     "file": "artifacts/cross-cutting/arb-minutes-{NNN}-{YYYY-MM-DD}.md",
     "status": "Draft",
     "type": "arb-minutes",
     "createdAt": "{ISO 8601}",
     "lastModified": "{ISO 8601}"
   }
   ```
6. Update `engagement.json → lastModified`.

Confirm: `"ARB-{NNN} created: artifacts/cross-cutting/arb-minutes-{NNN}-{YYYY-MM-DD}.md"`

Offer:
```
ARB-{NNN} is ready. What next?

  1. Populate decisions now (facilitated session)
  2. Convene the ARB council on an agenda item (panel review + vote)
  3. View the file
  4. Done
```

If option 1 selected, hand off to `ea-facilitator` in ARB facilitation mode (similar to Workshop Mode — run through agenda items, capture decisions in the Decisions table, record votes and governance references).

If option 2 selected, run **Mode: Council** targeting this `ARB-{NNN}`.

---

## Mode: Council

Convene the **ARB Council** — a multi-member review panel — on a subject, and record its votes and verdict into an ARB meeting. This is the `/ea-arb` alias for `/ea-council`; the panel logic lives in the `ea-arb-council` skill (membership in `skills/ea-engagement-lifecycle/references/arb-council-roster.md`). Do not restate the member logic here.

### Step 1 — Resolve the target meeting

- If a council subject is already in flight (called from Mode: New, or `council ARB-NNN` given), use that `ARB-{NNN}`.
- Otherwise scan `EA-projects/{slug}/artifacts/cross-cutting/arb-minutes-*.md`. If a Draft meeting exists, offer it; else offer to create one via Mode: New first (a council review should be recorded against a meeting).

### Step 2 — Resolve the subject

If a subject and its loaded context were passed in from a prior `/ea-council` run (Option 3), skip the prompt and context load — use what was passed.

Otherwise ask what the council should review:
```
What should the council review?
  1. An agenda item from this meeting
  2. A specific artifact            (e.g. architecture-vision)
  3. A phase                        (e.g. phase A)
  4. A specific ADR                 (e.g. ADR-003)
  5. The whole engagement
```
Resolve the subject and load its context using the same load + exclusions list as `/ea-council` Step 3 (exclude `*.review.md` and generated `*-register*.md`).

### Step 3 — Run the council

If a `## Council Verdict` was passed in from a prior `/ea-council` run (check conversation context for an already-produced verdict for this subject), use it directly — do not re-invoke the skill. Otherwise, load the `ea-arb-council` skill, pass the subject and context (and any `--member`/`--quick` flags), and present the produced verdict.

### Step 4 — Write back into the minutes

With confirmation, edit `arb-minutes-{NNN}-{YYYY-MM-DD}.md`:

1. **`## Council Review` section** — populate the panel table (Member · Vote · Top Concern · Conditions) and the Consensus / Points of Contention / Consolidated Recommendation fields from the verdict. If the subject is a phase or the whole engagement, add a sub-heading naming the subject; multiple council reviews in one meeting stack as sub-blocks.
2. **`## Decisions` row** — add a row for the subject: **Vote** = the council tally (`{Approve} For / {Reject} Against / {Abstain} Abstain`, with `Approve-with-conditions` counted as For and noted), **Decision** = the consolidated recommendation, **Outcome** = `Endorsed / Endorsed with conditions / Not endorsed / Deferred`, **ADR Reference** = the `ADR-NNN` if the subject was an ADR, **Governance Authority** per the subject, **Owner** as captured.
3. **`## Actions Register`** — append each verdict **condition** as an action (Owner = the member or assignee, Status `Open`).
4. **`## Appendix A4`** — add stakeholder-facing concerns as `CON-NNN` rows. Before adding, read existing A4 rows and skip any concern already present (matched by source `ea-council` or the same member name and finding text) to avoid duplicates if Option 2 was also selected.
5. Update `lastModified` (frontmatter and `engagement.json`).

Then offer the standard `/ea-council` Step 5 follow-ups (raise `RIS-NNN` for blocking Security/Budget findings; push Critiques to the reviewed artifact). A blocking Reject or a "Not endorsed" recommendation should **not** be auto-approved — leave the meeting `Draft` for the board, and surface it for `/ea-arb close`.

Confirm: `"Council review recorded in ARB-{NNN}: {recommendation}. {N} conditions added as actions."`

---

## Mode: List

Display all ARB minutes for the active engagement.

Scan `EA-projects/{slug}/artifacts/cross-cutting/arb-minutes-*.md`. For each file, read frontmatter (`arbId`, `title`, `date`, `status`, `chair`, `quorumMet`).

Count the decisions in each file's `## Decisions` table (rows that are not the empty-state row).

Display:
```
ARB Meetings — {engagement name}

  ARB-001  2026-01-15  Chair: Jane Smith   Quorum: Met    Status: Approved   Decisions: 3
  ARB-002  2026-02-20  Chair: Jane Smith   Quorum: Met    Status: Draft      Decisions: 2

{N} meetings total.
```

If no ARB meetings exist: `No ARB meetings recorded for this engagement. Run '/ea-arb new' to create one.`

---

## Mode: View ARB-NNN

Display a formatted inline summary (not the raw file).

1. Find the file: `EA-projects/{slug}/artifacts/cross-cutting/arb-minutes-{NNN}-*.md`
2. If not found: `"ARB-{NNN} not found. Use '/ea-arb list' to see all ARB meetings."`
3. Read all sections and display a formatted summary:

```
ARB-{NNN} — {title}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Date:      {date}
Chair:     {chair}
Secretary: {secretary}
Quorum:    {quorumRequired} required — {quorumMet: Met / Not Met}
Status:    {status}

Attendees ({N}):
  {name} ({role}) — {Voting / Observer}
  ...

Agenda ({N} items):
  1. {item}  [{status}]
  ...

Decisions ({N}):
  {#}  {item}  →  {decision}  [{vote: X/Y/Z}]  [{ADR ref or —}]
  ...

Actions ({N}):
  {#}  {action}  Owner: {owner}  Due: {due}  [{status}]
  ...

Deferred ({N}):
  {#}  {item}  Reason: {reason}  Owner: {owner}

Next meeting: {date or "Not scheduled"}
```

---

## Mode: Close ARB-NNN

Finalise an ARB minutes document and mark it Approved.

1. Find the file.
2. Display the draft content using Mode: View.
3. Confirm quorum:
   - If `quorumMet: false` or unknown: `"⚠️ Quorum was not met. Decisions in these minutes are provisional. Do you want to mark this meeting Void instead of Approved? (y to void / n to approve as provisional record)"`
   - If yes to void: set `status: Void`.
   - If quorum met or user proceeds: set `status: Approved`.
4. Update `lastModified`.
5. Write the file.

**Offer to propagate decisions to ADR register:**
```
Propagate decisions to ADR register? (y/n)
```
If yes: for each Decisions table row that has an ADR reference:
- Find the referenced ADR file.
- Ask: `"ADR-{NNN} '{title}' — vote was {X} For / {Y} Against. Set ADR status to: 1. Completed  2. Candidate (no change)  3. Deprecated"`
- Apply the chosen status update using the same procedure as `/ea-adrs update ADR-NNN status <value>`.
- Update the ADR's `Governance Reference` field (§5) to `ARB-{NNN}`.
- Note in the ADR's `## 8. Related Architecture Decisions` table: `ARB-{NNN} | {date} | Approved at ARB | {outcome}`.

**Offer to create risks from outstanding actions:**
```
Create Risk Register entries for outstanding actions? (y/n)
```
If yes: for each action with Status `Open` and a past due date, offer to create a RIS-NNN entry via `/ea-risks add` — prefilling: statement from the action, domain from the ARB agenda item, severity `Medium`, owner from the action.

Confirm: `"ARB-{NNN} closed. Status: {Approved/Void}. {N} ADRs updated."`
