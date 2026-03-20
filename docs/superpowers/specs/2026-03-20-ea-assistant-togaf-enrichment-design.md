# EA-Assistant TOGAF Enrichment — Design Specification

**Date:** 2026-03-20
**Status:** Draft
**Scope:** Add generation capabilities, interview question bank, requirements analyst agent, and ADM reference material to the ea-assistant plugin, drawing from the togaf-adm plugin.

---

## 1. Motivation

The `togaf-adm` plugin contains capabilities that complement `ea-assistant` but are not currently available within it:

- **Artifact generation** (Word/PPTX/Mermaid) via Python scripts and a dedicated skill
- **Phase-by-phase interview question sets** with output routing to artifacts
- **Requirements analyst agent** that extracts structured requirements from uploaded documents
- **ADM reference material** (phase inputs/outputs, tailoring guidance)

ea-assistant has a richer engagement lifecycle model (engagement.json, project folders, artifact tracking, review workflow) but lacks these depth features. This design enriches ea-assistant by porting and adapting the best of togaf-adm into ea-assistant's existing architecture.

## 2. Design Approach

**Approach 2 — Enrich Existing + Add Missing:** Update existing components to absorb togaf-adm's depth. Add only genuinely new components. No wholesale duplication.

## 3. New Files

### 3.1 Skill: ea-generation

**File:** `skills/ea-generation/SKILL.md`

**Purpose:** Governs how to produce formatted output files from individual EA artifacts. Three formats: Mermaid diagrams (inline), Word (.docx), PowerPoint (.pptx).

**Content structure:**
- Format selection guide (table mapping each artifact type to recommended formats)
- Mermaid diagram patterns per artifact type:
  - Capability Map → `graph TD` with L1/L2/L3 hierarchy
  - Process Flow → `flowchart LR` with `subgraph` swim lanes
  - Stakeholder Map → `quadrantChart` (power vs interest)
  - Technology Landscape → `C4Context` / `C4Container`
  - Architecture Roadmap → `gantt` with transition sections
  - Data Flow → `flowchart TD` with labeled edges
- Word document standard structure (cover page, ToC, executive summary, content sections, appendices)
- PowerPoint deck standard structure (title slide, exec summary, overview, detail slides, roadmap, next steps)
- Script invocation instructions (adapted for engagement context)
- Styling conventions (fonts, colours, heading hierarchy)

**Key adaptation from togaf-adm:** Scripts read engagement metadata (org, sponsor, dates) from `engagement.json` instead of requiring CLI arguments. Output files go to `EA-projects/{slug}/artifacts/`.

**Frontmatter:**
```yaml
name: ea-generation
description: This skill should be used when the user asks to "generate a Word document", "export an artifact as PowerPoint", "create a .docx", "produce slides", "make a Mermaid diagram", "export artifact", or any request to produce a formatted file from an EA artifact.
version: 0.1.0
```

### 3.2 Scripts: generate-docx.py, generate-pptx.py

**Files:** `scripts/generate-docx.py`, `scripts/generate-pptx.py`

**Purpose:** Python scripts that produce formatted Word and PowerPoint files from artifact content JSON.

**Adapted from:** `togaf-adm/scripts/generate-docx.py` and `togaf-adm/scripts/generate-pptx.py`

**Modifications:**
- Accept `--engagement-dir` argument to read metadata from `engagement.json`
- Fall back to explicit `--org`, `--architect`, `--title` arguments if no engagement dir provided
- Output to `{engagement-dir}/artifacts/` by default
- Same artifact type values as togaf-adm: `vision`, `gap-analysis`, `app-portfolio`, `requirements-register`, `roadmap`, `stakeholder-map`
- Same styling conventions (Calibri, dark blue #1F3864 headings, alternating row shading for tables)

**Dependencies:** `python-docx`, `python-pptx` (pip installable)

### 3.3 Command: ea-generate

**File:** `commands/ea-generate.md`

**Purpose:** Export a single EA artifact as a formatted file.

**Usage:** `/ea-generate [artifact-name] [docx|pptx|mermaid]`

**Workflow:**
1. If no engagement active, prompt for `/ea-open`
2. If no artifact name, list artifacts with format recommendations
3. If no format, recommend based on artifact type (from format selection guide)
4. Read artifact content from `EA-projects/{slug}/artifacts/{artifact-id}.md`
5. Read engagement metadata from `engagement.json`
6. For Mermaid: render inline fenced code block
7. For docx/pptx: build content JSON, invoke script, confirm output path
8. Update `engagement.json` artifact entry with export timestamp

**Frontmatter:**
```yaml
name: ea-generate
description: Generate a formatted file (Word, PowerPoint, or Mermaid) from an EA artifact
argument-hint: "[artifact-name] [docx|pptx|mermaid]"
allowed-tools: [Read, Write, Bash]
```

### 3.4 Reference: Phase Interview Questions

**File:** `skills/ea-artifact-templates/references/phase-interview-questions.md`

**Purpose:** Curated question bank for each ADM phase, with output routing tables mapping each response to the artifact field it populates.

**Content structure (per phase):**
```
### Phase X — [Name] Interview
**Goal:** [one-line goal]

Key questions:
1. [question]
2. [question]
...

**Output Routing:**
| Response Topic | Target Artifact | Target Field |
|---------------|-----------------|-------------|
| Business goals | Architecture Vision | Strategic Goals |
| Stakeholder names | Stakeholder Map | Name, Role, Concerns |
...

**Facilitation Notes:** [tips for this phase]
```

**Phases covered:** Preliminary, A (Vision), B (Business), C (Information Systems), D (Technology), E/F (Opportunities & Roadmap), G (Governance), H (Change Management)

**Adapted from:** togaf-adm `togaf-interview-techniques` skill. Enhanced with output routing tables that reference ea-assistant artifact template field names.

### 3.5 Agent: ea-requirements-analyst

**File:** `agents/ea-requirements-analyst.md`

**Purpose:** Reads uploaded documents and extracts structured requirements mapped to ADM phases and Zachman cells. Populates the engagement's requirements register.

**Frontmatter:**
```yaml
name: ea-requirements-analyst
description: >
  Use this agent when the user loads a document for analysis, wants to extract
  architecture requirements from an existing file, needs requirements mapped to
  TOGAF ADM phases, or wants a requirements register built from a document.
model: inherit
color: cyan
tools: ["Read", "Write", "Bash", "Glob"]
```

**Capabilities:**
1. Parse documents from `EA-projects/{slug}/uploads/` (.md, .txt, .docx)
2. Classify document type (Strategy, Business Case, Requirements Spec, Existing Architecture, Policy)
3. Extract items and classify: Business Requirement, Functional, Non-Functional, Constraint, Assumption, Driver
4. Assign IDs (REQ-001, CON-001, ASM-001), priority, ADM phase mapping
5. Produce ADM Phase Coverage Map (which phases have inputs)
6. Produce Zachman Coverage Matrix (which cells are addressed) — unique to ea-assistant
7. Identify gaps and suggest follow-up interview questions
8. Populate requirements register in `EA-projects/{slug}/requirements/` with user confirmation
9. Update `engagement.json` artifacts array

**Content policy compliance:** All AI-extracted content marked with `> AI Draft — Review Required`. User confirms before writing to artifacts.

**Integration points:**
- `ea-document-ingestion` skill: file format handling reference
- `ea-requirements-management` skill: requirements register schema and sync formats
- `ea-interview` command: gap-derived questions feed back as follow-up interviews
- `zachman-framework` skill: Zachman cell classification for coverage analysis

### 3.6 Reference: Phase Inputs and Outputs

**File:** `skills/ea-engagement-lifecycle/references/phase-inputs-outputs.md`

**Purpose:** Detailed input/output tables for every ADM phase. More granular than the existing `adm-phase-guide.md`.

**Content structure (per phase):**
```
### Phase X — [Name]

**Required Inputs:**
| Input | Source | Description |
|-------|--------|-------------|
| Architecture Principles | Preliminary | Approved principles catalog |
...

**Key Activities:**
1. [activity]
...

**Required Outputs:**
| Output | Consumer | Description |
|--------|----------|-------------|
| Architecture Vision | Phase B, C, D | High-level target state |
...

**Quality Gates:**
- [ ] All required inputs available
- [ ] Stakeholder sign-off obtained
- [ ] Artifacts reviewed and approved
```

### 3.7 Reference: ADM Tailoring

**File:** `skills/ea-engagement-lifecycle/references/adm-tailoring.md`

**Purpose:** Guidance on adapting the ADM for different delivery contexts.

**Sections:**
- Agile delivery (sprint-based ADM, lightweight artifacts, iterative phases)
- Programme-level architecture (multiple projects, federated governance)
- Capability-based planning (capability increments vs phase-sequential)
- Security architecture overlay (SABSA integration points)
- Decision trees for when to skip or combine phases

## 4. Updated Files

### 4.1 agents/ea-interviewer.md

**Changes:**
- Add a second interview mode description in the agent prompt:
  - **Artifact mode** (existing): extracts `{{placeholder}}` questions from artifact templates
  - **Phase mode** (new): loads questions from `skills/ea-artifact-templates/references/phase-interview-questions.md` for the specified ADM phase
- Add output routing logic: after each answer in phase mode, identify which artifact(s) the response feeds and propose writing to each with user confirmation
- Add reference to the question bank file path in the agent instructions

### 4.2 commands/ea-interview.md

**Changes:**
- Add new mode: `start phase [phase-name]`
  - Loads questions from the phase interview question bank
  - Hands off to `ea-interviewer` agent in phase mode
  - Routes answers to multiple artifacts across the phase
  - Saves interview notes to `interviews/interview-phase-{phase}-{date}-v{N}.md`
- Update the mode documentation header to list: `start [artifact|phase] [name]`, `export`, `import`, `resume`

### 4.3 commands/ea-merge.md

**Changes:**
- Add a note after Step 1 (Select Artifacts):
  ```
  > To export a single artifact as Word, PowerPoint, or Mermaid, use `/ea-generate` instead.
  ```
- No other changes. ea-merge remains the consolidated report tool.

### 4.4 skills/ea-engagement-lifecycle/SKILL.md

**Changes:**
- Add two lines to the "Additional Resources" section:
  ```
  - **`references/phase-inputs-outputs.md`** — Detailed input/output tables per ADM phase with quality gates
  - **`references/adm-tailoring.md`** — Tailoring the ADM for agile, programme, capability-based, and security contexts
  ```

## 5. What Is NOT Changing

- `plugin.json` version — bumped at release time, not in this design
- `.claude-plugin/marketplace.json` — updated at release time
- Existing agent behaviour for `ea-advisor`, `ea-consistency-checker`, `ea-diagram`, `ea-document-analyst`, `ea-facilitator` — unchanged
- Existing skill content for `archimate-notation`, `ea-artifact-templates`, `ea-document-ingestion`, `ea-requirements-management`, `zachman-framework` — unchanged (only new references added alongside)
- Engagement folder structure — unchanged
- `engagement.json` schema — unchanged

## 6. Implementation Order

1. **Reference files first** (phase-inputs-outputs, adm-tailoring, phase-interview-questions) — no dependencies, pure content
2. **ea-requirements-analyst agent** — depends on reference files existing
3. **Generation scripts** (generate-docx.py, generate-pptx.py) — independent, can be tested standalone
4. **ea-generation skill** — depends on scripts existing
5. **ea-generate command** — depends on skill and scripts
6. **Update ea-interviewer agent + ea-interview command** — depends on question bank reference
7. **Update ea-merge command + ea-engagement-lifecycle SKILL.md** — minor, last

## 7. Testing Strategy

Each component can be validated by:
- **Reference files:** Frontmatter validation (CI workflow), content review
- **Agent:** Load in Claude Code, run against a test engagement with sample uploads
- **Scripts:** Run with sample JSON input, verify output files open correctly
- **Skill:** Frontmatter validation, verify format selection guide is accurate
- **Commands:** Run each mode against a test engagement, verify file outputs
- **Updated files:** Verify existing modes still work, verify new modes function
