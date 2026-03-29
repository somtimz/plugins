---
name: ea-adrs
description: Create, manage, and track Architecture Decision Records (ADRs) — generate the ADR Register, create new ADRs, update ADR status, and surface ADR summaries across artifacts
argument-hint: "[generate | status | new | update ADR-NNN <field> <value>] [--status <status>] [--domain <domain>] [--phase <phase>] [--owner <owner>]"
allowed-tools: [Read, Write, Glob, Bash]
---

You are executing the `/ea-adrs` command. Load the `ea-engagement-lifecycle` skill and the `ea-artifact-templates` skill for context.

## Overview

`/ea-adrs` manages Architecture Decision Records for the active engagement. ADRs document significant architecture decisions — technology or vendor selection, architecture pattern choices, make-vs-buy decisions, data governance approaches, security architecture choices, and any decision that is hard to reverse or whose rationale may be questioned later.

**Modes:**
- `generate` (default) — scan all ADR files and write a consolidated `adr-register-{YYYY-MM-DD}.md`
- `status` — show an inline ADR summary without writing a file
- `new` — create a new ADR document from the template
- `update ADR-NNN <field> <value>` — update a single field on a specific ADR

**Filters (apply to `generate` and `status`):**
- `--status <status>` — filter by lifecycle status (Candidate / In Progress / Completed / Superseded / Deprecated)
- `--domain <domain>` — filter by architecture domain (Business / Data / Application / Technology / Cross-cutting)
- `--phase <phase>` — filter by ADM phase (Preliminary / A / B / C / D / E / F / G / H)
- `--owner <name>` — filter by decision owner

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, artifacts.

---

## Mode: `generate` (default)

### Step 2 — Scan for ADR Files

Scan `EA-projects/{slug}/artifacts/` for files matching `adr-*.md`. For each file found:

1. Read the frontmatter: `adrid`, `title`, `status`, `decisionDate`, `decisionOwner`, `phase`, `supersededBy`, `taxonomy.domain`
2. Read `## 5. Decision` section — extract the chosen option name and A3 governance reference
3. Read `## 9. Affected Artifacts` section — extract artifact names and impact descriptions
4. Apply any active filters (`--status`, `--domain`, `--phase`, `--owner`)

Build an in-memory ADR index with all extracted data.

### Step 3 — Compile ADR Register

Using the ADR register template (`templates/adr-register.md`):

1. Populate the Summary table with counts by status
2. Populate the phase tables — place each ADR in the correct phase section
3. Populate the Open ADRs table (Candidate + In Progress only)
4. Populate the Completed ADRs table
5. Populate the Superseded ADRs table
6. Populate the Artifact Impact Map from §9 data
7. Build the Supersession Tree for any chains where `supersededBy` is set

### Step 4 — Write the Register File

Write the completed register to: `EA-projects/{slug}/artifacts/adr-register-{YYYY-MM-DD}.md`

Register all register artifacts in `engagement.json → artifacts[]` if not already present.

Confirm: `"ADR Register written: {N} ADRs ({N} Candidate, {N} In Progress, {N} Completed, {N} Superseded)"`

---

## Mode: `status`

Display an inline summary without writing a file:

```
ADR Status — {engagement name}
Generated: {YYYY-MM-DD}

Open ADRs
  Candidate   : {N}
    ADR-001   {short title}   Owner: {owner}   Phase: {phase}
  In Progress : {N}
    ADR-002   {short title}   Owner: {owner}   Phase: {phase}

Completed     : {N}
Superseded    : {N}
Deprecated    : {N}
Total         : {N}

{if N > 0 open}: Use '/ea-adrs generate' to write the full register.
```

---

## Mode: `new`

Create a new ADR document.

### Step 2 — Determine Next ADR Number

Scan `EA-projects/{slug}/artifacts/` for files matching `adr-*.md`. Find the highest existing ADR-NNN number. Assign the next number: `ADR-{NNN+1}` (zero-padded to 3 digits).

### Step 3 — Collect ADR Metadata

Ask the user:

```
Creating new ADR — {next ADR ID}

1. Title (short, noun-phrase — e.g. "Cloud Platform Selection"):
2. Phase (Preliminary / A / B / C / D / E / F / G / H / Cross-phase):
3. Decision Owner (name or role):
4. Reviewed By (names/roles, or press Enter to leave blank):
5. Related business drivers or goals (e.g. "DRV-001, G-002", or press Enter to skip):
6. Triggering artifact and section (e.g. "Architecture Vision §7 STR-002", or press Enter to skip):
```

Wait for responses before proceeding.

### Step 4 — Create ADR File

1. Read the ADR template from `templates/architecture-decision-record.md`
2. Replace all `{{placeholder}}` tokens with the collected metadata:
   - `ADR-{{NNN}}` → assigned ADR ID
   - `{{decision_title}}` → title entered by user
   - `{{engagement_name}}` → from `engagement.json`
   - `{{phase}}` → phase entered by user
   - `{{owner}}` → decision owner
   - `{{reviewed_by}}` → reviewed by
   - `{{YYYY-MM-DD}}` → today's date
   - Leave body `{{placeholder}}` tokens intact (for interview population)
3. Write the file to: `EA-projects/{slug}/artifacts/adr-{NNN}-{kebab-slug-of-title}.md`
4. Register in `engagement.json → artifacts[]` with:
   ```json
   {
     "id": "adr-{NNN}",
     "file": "adr-{NNN}-{title-slug}.md",
     "artifact": "Architecture Decision Record",
     "adrid": "ADR-{NNN}",
     "title": "{title}",
     "phase": "{phase}",
     "status": "Candidate",
     "lastModified": "{today}"
   }
   ```

Confirm: `"ADR-{NNN} created: 'EA-projects/{slug}/artifacts/adr-{NNN}-{title-slug}.md'"`

Then offer:

```
ADR-{NNN} is ready. What would you like to do next?

  1. Interview — populate the ADR using guided Q&A (/ea-interview adr-{NNN})
  2. View template — open the new ADR file
  3. Done

```

---

## Mode: `update ADR-NNN <field> <value>`

Update a single field on the specified ADR.

### Step 2 — Find the ADR File

Scan `EA-projects/{slug}/artifacts/` for a file with `adrid: ADR-NNN` in its frontmatter.

If not found: `"ADR-NNN not found in EA-projects/{slug}/artifacts/. Use '/ea-adrs status' to see all ADRs."`

### Step 3 — Apply the Update

**Valid fields and values:**

| Field | Valid values |
|---|---|
| `status` | `Candidate` / `In Progress` / `Completed` / `Superseded` / `Deprecated` |
| `decisionOwner` | any string |
| `reviewedBy` | any string |
| `decisionDate` | `YYYY-MM-DD` format |
| `supersededBy` | `ADR-NNN` (required when setting status to Superseded) |

**Validation rules:**
- Setting `status: Superseded` requires `supersededBy` to be provided and to reference an existing ADR
- Setting `status: Completed` without a `decisionDate` → set `decisionDate` to today
- Setting `status: Deprecated` → prompt for a deprecation reason if not provided

**Update procedure:**
1. Show the proposed change: `"ADR-NNN: {field} — '{old_value}' → '{new_value}'"`
2. Ask: `"Apply this change? (y/n)"`
3. On confirm: update the frontmatter field in the ADR file AND update `engagement.json → artifacts[]` for the matching entry
4. If `status` changed to `Superseded`: also update the `supersededBy` ADR's `## 8. Related Architecture Decisions` table to add a row: `ADR-NNN | {this title} | Superseded by | {new status}`
5. Update `lastModified` in both the ADR frontmatter and `engagement.json`

Confirm: `"Updated ADR-NNN: {field} set to '{new_value}'"`

---

## ADR Lifecycle State Machine

```
Candidate → In Progress → Completed
                                └──→ Superseded (by ADR-NNN)
          └──→ Deprecated (any time, with reason)
```

Status transition rules:
- `Candidate → In Progress`: options analysis has started
- `In Progress → Completed`: decision has been made; `decisionDate` is set
- `Completed → Superseded`: a new ADR replaces this one; `supersededBy` is required
- Any → `Deprecated`: ADR is no longer relevant; deprecation reason must be recorded

---

## ADR-NNN in Artifact Context

When `/ea-adrs` is invoked from within an artifact interview (`ea-interviewer`) or after a significant decision is recorded in an A3 Decision Log:

1. Check the A3 row for the decision: if the A3 row has no `ADR-NNN` reference and the decision score (cost + risk + reversibility — see below) exceeds the threshold, prompt:

   ```
   💡 ADR suggestion: This decision may warrant a full Architecture Decision Record.

   Indicators:
   {list matched indicators}

   Create an ADR for this decision? (y/n)
   If yes: I'll run '/ea-adrs new' and pre-populate it from this context.
   ```

2. If the user confirms, invoke Mode: `new` with pre-populated metadata from the A3 row.

**ADR threshold indicators** (2 or more = suggest ADR):
- Decision involves a technology or vendor selection
- Decision is described as hard to reverse or affects multiple phases
- Decision has High cost impact (A3 Cost column = High)
- Decision has High risk impact (A3 Risk column = High)
- Decision involves a make-vs-buy or build-vs-configure choice
- Decision affects data governance, security architecture, or compliance approach
- Decision contradicts or refines an existing architecture principle
- Decision was contested by a stakeholder (concern recorded in A4)

---

## ADR Summary Block (for use in other artifacts)

When the `ea-interviewer` or any artifact-creation command needs to include ADR context in a `## Related Architecture Decisions` section, use this format:

```markdown
| ADR ID | Title | Status | Summary |
|---|---|---|---|
| ADR-NNN | {title} | {status} | {one-sentence decision statement from ADR §5} |
```

Pull the decision statement from the ADR's `## 5. Decision` section — first sentence of the `**Decision:**` field.

---

## Filter Behaviour

When filters are applied:

- `--status Candidate` — show only Candidate ADRs in the register/status
- `--status "In Progress"` — use quotes for multi-word values
- `--domain Technology` — show only ADRs where `taxonomy.domain = Technology`
- `--phase B` — show only ADRs where `phase = B`
- `--owner "Jane Smith"` — show only ADRs where `decisionOwner` contains the given name

Multiple filters are ANDed: `--status Candidate --phase A` shows only Candidate ADRs in Phase A.
