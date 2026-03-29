---
name: ea-zachman
description: Create, populate, and review the Zachman Diagram for an EA engagement — generate from existing artifacts, interview to fill gaps, produce coverage analysis, and classify any artifact against the 6×6 grid
argument-hint: "[generate | review | gap | interview | classify <artifact-name>]"
allowed-tools: [Read, Write, Glob, Bash]
---

You are executing the `/ea-zachman` command. Load the `zachman-framework` skill and the `ea-artifact-templates` skill for context.

## Overview

`/ea-zachman` manages the Zachman Diagram artifact for the active engagement. The Zachman Framework classifies architecture content by **audience row** (Contextual through Functioning) and **interrogative column** (What / How / Where / Who / When / Why). This command provides a structured workflow to populate, review, and gap-analyse the 6×6 diagram.

**Modes:**
- `generate` (default) — auto-populate cells from existing engagement artifacts; write `zachman-diagram-{YYYY-MM-DD}.md`
- `review` — produce an inline coverage matrix (✅/⚠️/❌) without writing a file
- `gap` — identify empty or partial cells and recommend remediation actions
- `interview` — guided Q&A to fill empty cells row-by-row
- `classify <artifact-name>` — classify a specific artifact or concept against the Zachman grid

---

## Step 1 — Resolve Active Engagement

1. Check the conversation context for an active engagement slug.
2. If none found, scan `EA-projects/*/engagement.json` and ask the user to select one.
3. Load `engagement.json` — extract: name, slug, currentPhase, artifacts, architectureDomains.

---

## Mode: `generate` (default)

Scans all artifacts in the engagement, extracts content relevant to each Zachman cell, and writes a populated Zachman Diagram artifact.

### Step 2 — Build the Cell Extraction Map

For each cell, define the source artifacts and sections to scan:

| Cell | Source Artifacts | Sections / Fields |
|---|---|---|
| R1,C1 | Architecture Vision, Engagement Charter | §1 Organisation Background, §3 Scope — in-scope subject areas |
| R1,C2 | Architecture Vision, Engagement Charter | §3 Scope in-scope processes, §2 Business Drivers process scope |
| R1,C3 | Architecture Vision, Engagement Charter | §3 Scope locations, §1 Organisation Background geography |
| R1,C4 | Stakeholder Map, Engagement Charter | All stakeholder rows; §5 Organisations Affected |
| R1,C5 | Engagement Charter, Architecture Vision | §7 Programme Structure phase table; scope constraints on timing |
| R1,C6 | Architecture Vision, Engagement Charter | §2 DRV-NNN, §3 G-NNN, §4 OBJ-NNN, §7 STR-NNN; §6 Motivation Framework |
| R2,C1 | Data Architecture, Business Architecture | §2 Conceptual Data Model, §4 Data Entity Catalogue |
| R2,C2 | Business Architecture, Business Model Canvas | §3 Capability Model, §4 Business Process Catalogue, Value Propositions, Key Activities |
| R2,C3 | Business Architecture | §5 Business Logistics / Location model |
| R2,C4 | Business Architecture, Stakeholder Map | §6 Organisation Model, Role Catalogue |
| R2,C5 | Business Architecture, Architecture Roadmap | §4 Business Event Cycles, milestone sequence |
| R2,C6 | Architecture Vision, Requirements Register | §5 ISS-NNN, §6 PRB-NNN, §7 STR-NNN; Motivation column |
| R3,C1 | Data Architecture | §3 Logical Data Model, §4 Data Entity Catalogue |
| R3,C2 | Application Architecture | §3 Application Portfolio, §4 Application Function Catalogue |
| R3,C3 | Application Architecture | §6 Application Communication Diagram, §5 Integration Architecture |
| R3,C4 | Application Architecture, Business Architecture | §7 Role–Application Matrix, §8 Access Control Model |
| R3,C5 | Application Architecture | §8 Processing Architecture, any state machine or event-driven diagrams |
| R3,C6 | Requirements Register, Data Architecture | Constraint-type REQ-NNN entries; §5 Data Governance rules |
| R4,C1 | Data Architecture | §6 Physical Data Model, Data Dictionary |
| R4,C2 | Application Architecture, Technology Architecture | §9 Component Design, §4 Platform Design |
| R4,C3 | Technology Architecture | §3 Infrastructure Model, §4 Network Topology, §5 Platform Catalogue |
| R4,C4 | Application Architecture, Technology Architecture | §10 UI Architecture, §6 Security Architecture |
| R4,C5 | Technology Architecture, Migration Plan | §7 Integration Architecture, §3 Wave Plan |
| R4,C6 | Application Architecture, Technology Architecture | Rule engine design, policy enforcement |
| R5,Cx | All | Reference delivery repository / CMDB — do not extract content; record reference only |

### Step 3 — Scan Artifacts

For each artifact listed in `engagement.json → artifacts[]`:
1. Read the artifact file from `EA-projects/{slug}/artifacts/`
2. Identify which Zachman cells it contributes to (using the Cell Extraction Map above)
3. Extract the relevant content: copy key statements, IDs, and table rows — do not summarise vaguely
4. Record the source artifact name and section for traceability

For each cell, classify coverage:
- **✅ Populated** — at least one substantive content item extracted
- **⚠️ Partial** — content extracted but sparse (< 3 items, or all placeholder text)
- **❌ Empty** — no content found in any source artifact
- **🚫 Out of scope** — cell is deliberately excluded (Row 6, or scoped-out domain)

### Step 4 — Write the Zachman Diagram

1. Read the template from `templates/zachman-diagram.md`
2. Replace all `{{placeholder}}` frontmatter tokens from `engagement.json`
3. Populate the Coverage Summary table with ✅/⚠️/❌ per cell
4. For each cell section, replace `{{rNcN_content}}` with the extracted content items, formatted as a bullet list. Replace `{{rNcN_source}}` with the artifact name(s) and section(s).
5. For Row 5, populate the reference column with any delivery artifact references found
6. Populate the Gap Analysis table (see Mode: `gap` for gap classification rules)
7. Write to: `EA-projects/{slug}/artifacts/zachman-diagram-{YYYY-MM-DD}.md`
8. Register in `engagement.json → artifacts[]`:
   ```json
   {
     "id": "zachman-diagram",
     "file": "zachman-diagram-{YYYY-MM-DD}.md",
     "artifact": "Zachman Diagram",
     "phase": "All",
     "status": "Draft",
     "lastModified": "{today}"
   }
   ```

Confirm: `"Zachman Diagram written: {N} cells populated (✅ {N} / ⚠️ {N} / ❌ {N})"`

Then offer:
```
Zachman Diagram generated. What would you like to do next?

  1. Review coverage  — /ea-zachman review
  2. See gaps         — /ea-zachman gap
  3. Fill empty cells — /ea-zachman interview
  4. Done
```

---

## Mode: `review`

Produces an inline coverage matrix and cell summary without writing a file.

### Step 2 — Scan Existing Zachman Diagram

Look for `zachman-diagram-*.md` in `EA-projects/{slug}/artifacts/`. Use the most recent file.

If no file exists: scan all artifacts directly (same logic as `generate` Step 3) and compute coverage on-the-fly. Do not write a file.

### Step 3 — Output Coverage Report

```
════════════════════════════════════════════════════════════════
ZACHMAN COVERAGE — {engagement name}
Generated: {YYYY-MM-DD}  |  Phase: {currentPhase}
════════════════════════════════════════════════════════════════

         What      How      Where    Who      When     Why
R1  ✅ Scope    ✅ Scope  ✅ Scope  ✅ Scope ⚠️ Scope  ✅ Scope
R2  ✅ Concept ✅ Concept ❌       ✅ Org   ⚠️ Events ✅ Strategy
R3  ✅ Logical ⚠️ App    ⚠️ Dist   ❌       ❌        ⚠️ Rules
R4  ❌         ⚠️ Design ✅ Infra  ❌       ❌        ❌
R5  🚫         🚫        🚫        🚫       🚫        🚫

Legend: ✅ Populated  ⚠️ Partial  ❌ Empty  🚫 Out of scope

Populated : {N}   Partial : {N}   Empty : {N}
Coverage  : {N}% of in-scope cells ({N}/30 excluding Row 6)
════════════════════════════════════════════════════════════════
```

Then list the top 3 empty cells that are most impactful to address, with a one-line reason each.

---

## Mode: `gap`

Identifies empty and partial cells, classifies each gap, and recommends concrete remediation actions.

### Step 2 — Determine Coverage

Same scan logic as `review`. Build a list of all ❌ and ⚠️ cells.

### Step 3 — Classify and Prioritise Gaps

For each gap, determine:

**Severity:**
- **High** — cell is in a domain that is in scope AND artifacts for that domain exist (content should have been extracted but wasn't) OR the cell is on the critical path for the current phase
- **Medium** — cell is in a domain that is in scope but the relevant artifact hasn't been created yet
- **Low** — cell is in Row 4 or Row 5 (physical/detailed) and the phase hasn't reached those rows yet; or cell is in a domain that is explicitly out of scope

**Recommended action for each gap:**

| Cell Pattern | Recommended Action |
|---|---|
| R1,Cx — Contextual empty | Check Engagement Charter and Architecture Vision; re-run `/ea-zachman generate` after updating those artifacts |
| R2,Cx — Conceptual empty | Run `/ea-interview` for Business Architecture (Phase B) to populate the missing conceptual content |
| R3,C1 empty | Data Architecture §3 Logical Data Model is not populated — run Phase C interview |
| R3,C2 empty | Application Architecture §3/§4 not populated — run Phase C interview |
| R3,C3 empty | Application Communication Diagram missing — add to Application Architecture |
| R3,C4 empty | Role–Application Matrix missing — add to Application Architecture §7 |
| R3,C5 empty | Processing/event model missing — add to Application Architecture §8 or diagram directory |
| R3,C6 empty | Business rules not captured — run `/ea-requirements` to extract constraint-type requirements |
| R4,Cx empty | Technology Architecture not yet populated — run Phase D interview |
| Any ⚠️ Partial | Run `/ea-zachman interview` and jump to that specific cell to add content |

### Step 4 — Output Gap Report

```
════════════════════════════════════════════════════════════════
ZACHMAN GAP ANALYSIS — {engagement name}
════════════════════════════════════════════════════════════════

HIGH PRIORITY GAPS
  R3,C4  Human Interface Model (Who — Logical)
         No role-to-application matrix or access control model found.
         Action: Add §7 Role–Application Matrix to Application Architecture.

  R3,C5  Processing Cycle / State Model (When — Logical)
         No event model or state machine diagram found.
         Action: Run /ea-zachman interview and answer the R3,C5 questions.

MEDIUM PRIORITY GAPS
  R4,C1  Physical Data Model (What — Physical)
         Technology Architecture exists but physical data model section is empty.
         Action: Populate Data Architecture §6 Physical Data Model.

  ...

LOW PRIORITY GAPS
  R5,Cx  (5 cells) — Detailed implementation artefacts out of EA scope.
         Action: Reference delivery repository when available.

════════════════════════════════════════════════════════════════
Total gaps: {N} High, {N} Medium, {N} Low
════════════════════════════════════════════════════════════════
```

Offer: `"Run '/ea-zachman interview' to fill the high-priority gaps now? (y/n)"`

---

## Mode: `interview`

Guides the user through filling empty cells via structured Q&A, row by row. Skips populated cells.

### Step 2 — Determine Which Cells to Interview

Scan for the Zachman Diagram file. If not found, run generate first (silently, without writing a file) to determine current coverage.

Build an ordered list of empty/partial cells, sorted by row (R1 → R2 → R3 → R4) then column.

Skip:
- Cells classified as 🚫 (Row 6, or out-of-scope domains)
- Cells already marked ✅ (unless user requests a full re-interview)

### Step 3 — Present Interview Plan

```
Zachman Interview — {engagement name}

{N} cells to fill ({N} empty, {N} partial)

Row 1 (Contextual — Executive): {N} cells
Row 2 (Conceptual — Business Owner): {N} cells
Row 3 (Logical — Architect): {N} cells
Row 4 (Physical — Builder): {N} cells

Options:
  1. Interview all empty cells (row by row)
  2. Interview one row only — select: R1 / R2 / R3 / R4
  3. Jump to a specific cell (e.g. R3,C4)
  4. Cancel

```

### Step 4 — Conduct the Interview

For each cell in scope:

1. **Announce the cell:**
   ```
   ── Cell R{N},C{N} — {Row Name} / {Column Name} ({Perspective}) ──
   {one-sentence purpose from zachman-cell-descriptions.md}
   ```

2. **Show existing content** (if partial):
   ```
   📎 Existing content:
   {current cell content}
   Add to this or replace it?  (a)dd / (r)eplace / (s)kip
   ```

3. **Ask the cell question** — use the question bank below.

4. **Accept input** — support multi-line input; user types `done` or presses Enter twice to finish.

5. **Offer traceability** — after each answer:
   ```
   Source artifact? (e.g. "Architecture Vision §3", or press Enter to leave blank)
   ```

6. **Write to the Zachman Diagram file** — update the cell section and coverage status in the file.

7. Move to the next cell.

### Cell Question Bank

**Row 1 — Contextual**

| Cell | Interview Question |
|---|---|
| R1,C1 | What are the major categories of things (entities, objects, subject areas) that are important to this business? List the key nouns of the domain — not a data model, just the vocabulary. |
| R1,C2 | What high-level business processes or functions are in scope for this engagement? List the main activities the organisation performs that this architecture must support. |
| R1,C3 | What are the relevant business locations — geographic sites, operational centres, or logical locations (e.g. web presence, shared services hub)? |
| R1,C4 | Who are the key players? List the business units, external organisations, regulators, and stakeholder groups that are in scope or materially affected. |
| R1,C5 | What are the significant business events, timeframes, and cycles that constrain or drive this engagement? (e.g. financial year end, regulatory reporting cycle, go-live target) |
| R1,C6 | What are the strategic goals and drivers behind this engagement? Why is this architecture being done? (Reference DRV-NNN and G-NNN IDs if already established.) |

**Row 2 — Conceptual**

| Cell | Interview Question |
|---|---|
| R2,C1 | Describe the key business entities and their relationships in business language — independent of any system. (e.g. "A Customer places many Orders; an Order contains Order Lines") |
| R2,C2 | What are the core business processes or value streams the organisation runs? Describe them in business terms — not system functions, but what the business does. |
| R2,C3 | How does the business connect its locations — what are the distribution, communication, and logistics networks that link them? |
| R2,C4 | Describe the organisational structure — business units, their relationships, and the key roles that operate the business processes. |
| R2,C5 | What are the key business lifecycle states or event sequences? (e.g. customer lifecycle, order fulfilment sequence, contract renewal cycle) |
| R2,C6 | What goals, strategies, issues, and problems has the organisation identified? How do they relate to each other? (Reference the motivation framework IDs already captured.) |

**Row 3 — Logical**

| Cell | Interview Question |
|---|---|
| R3,C1 | What are the data entities and their relationships required by the information systems — normalised and independent of any specific database? (Reference the logical data model if it exists.) |
| R3,C2 | What functions must the application systems perform to support the business processes? List the key application capabilities required. |
| R3,C3 | How are system functions logically distributed across nodes or zones — without specifying physical hardware? (e.g. "order processing at central node, customer portal at edge") |
| R3,C4 | Which roles interact with which systems, through which interfaces? Describe the human interface architecture and access control model. |
| R3,C5 | Describe the processing cycles, system state machines, and event-driven flows that govern system behaviour. |
| R3,C6 | What business rules govern system behaviour? List them in declarative, technology-independent form. (e.g. "A customer may not place an order if their account is suspended") |

**Row 4 — Physical**

| Cell | Interview Question |
|---|---|
| R4,C1 | How is the logical data model translated into a technology-specific design? (Table structures, indexing strategy, storage technology, database platform) |
| R4,C2 | How are the system functions designed in technology-specific terms? (Component architecture, API design, microservices decomposition, technology choices) |
| R4,C3 | What is the physical technology infrastructure? (Servers, cloud regions, network topology, deployment zones, platform choices) |
| R4,C4 | How do users interact with the system at a technology level? (UI frameworks, authentication mechanisms, channel architecture, device support) |
| R4,C5 | What are the technology-level timing controls? (Scheduling mechanism, message queue design, transaction management, retry policies) |
| R4,C6 | How are business rules implemented in the technology? (Rule engine platform, decision service design, parameterised validation, policy enforcement) |

### Step 5 — Session Completion

After all selected cells are answered:
```
Zachman interview complete.
  {N} cells populated
  {N} cells updated (partial → full)
  {N} cells skipped

Updated file: EA-projects/{slug}/artifacts/zachman-diagram-{YYYY-MM-DD}.md
New coverage: {N}% ({N}/30 in-scope cells)
```

Offer:
```
  1. View updated coverage  — /ea-zachman review
  2. See remaining gaps     — /ea-zachman gap
  3. Done
```

---

## Mode: `classify <artifact-name>`

Classifies a named artifact or concept against the Zachman grid.

### Step 2 — Identify the Artifact

Accept either:
- A known artifact name (e.g. "architecture-vision", "logical-data-model")
- A freeform description (e.g. "our BPMN process diagrams", "the API specification")

### Step 3 — Classify

Apply the Classification Workflow from `skills/zachman-framework/SKILL.md`:

1. Identify the **primary audience** → determines the row
2. Identify the **primary concern** → determines the column
3. Check `skills/zachman-framework/references/togaf-zachman-mapping.md` for known TOGAF artifacts
4. If the artifact is not in the mapping table, apply the classification rules directly

### Step 4 — Output

```
Classification: {artifact name}
──────────────────────────────────
Primary cell  : R{N},C{N} — {Row label} / {Column label}
Secondary cells: R{N},C{N}, R{N},C{N}
Audience      : {who should review/produce this}
Interrogative : {what question this artifact answers}

Rationale: {one paragraph explaining the classification}

Related cells: {cells that this artifact informs or is informed by}
TOGAF mapping: {TOGAF phase and artifact name, if applicable}
```

Offer: `"Update the Zachman Diagram to mark this cell as populated? (y/n)"`

---

## Zachman Diagram — Relationship to Other Artifacts

When producing or updating any EA artifact, note which Zachman cells it contributes to:

| If you are working on… | It primarily populates… |
|---|---|
| Architecture Vision (Phase A) | R1,C6 and R2,C6 — goals, drivers, strategies |
| Stakeholder Map (Phase A) | R1,C4 — contextual people |
| Business Architecture (Phase B) | R2,C2, R2,C4, R2,C6 — process, organisation, strategy |
| Data Architecture (Phase C) | R2,C1, R3,C1, R4,C1 — semantic, logical, physical data |
| Application Architecture (Phase C) | R3,C2, R3,C3, R3,C4 — functions, distribution, roles |
| Technology Architecture (Phase D) | R4,C3, R4,C2, R4,C4 — infrastructure, design, presentation |
| Requirements Register | R2,C6, R3,C6 — motivation and business rules |
| Architecture Roadmap (Phase E) | R2,C5 — business event cycle / timing |
| Migration Plan (Phase F) | R4,C5 — control structure / timing |
| Gap Analysis | All rows — identifies missing cells |
