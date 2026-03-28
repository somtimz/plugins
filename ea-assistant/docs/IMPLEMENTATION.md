# EA Assistant — Implementation Guide

**Complements:** `docs/PRD.md` (what and why) · `CLAUDE.md` (developer quick reference)

This document covers how the plugin is built, how to extend it, and the conventions that keep it coherent as it grows.

---

## 1. Plugin Architecture

EA Assistant is a Claude Code plugin. It has no runtime server — all behaviour is expressed through markdown instruction files that Claude interprets at invocation time.

```
ea-assistant/
├── .claude-plugin/plugin.json   # plugin identity and version
├── agents/                      # autonomous sub-agents (.md)
├── commands/                    # user-invokable slash commands (.md)
├── skills/                      # reusable instruction libraries (SKILL.md per skill)
│   ├── ea-artifact-templates/   # templates + reference files
│   ├── ea-engagement-lifecycle/ # ID scheme, facilitator styles, opt-out rules
│   ├── ea-document-ingestion/   # format-layer extraction (docx, pdf, xlsx, ...)
│   ├── ea-generation/           # export/generation logic
│   ├── ea-interview-ui/         # React interview form artifacts
│   ├── ea-requirements-management/
│   ├── archimate-notation/
│   └── zachman-framework/
├── templates/                   # TOGAF artifact .md templates (16)
├── scripts/                     # Python generators (generate-docx.py, generate-pptx.py)
├── hooks/hooks.json             # plugin lifecycle hooks
└── docs/                        # PRD.md, IMPLEMENTATION.md
```

### Component types and their roles

| Type | Format | Role | Invoked by |
|---|---|---|---|
| **Command** | `commands/*.md` | User-facing slash command; orchestrates agents and skills | User typing `/ea-*` |
| **Agent** | `agents/*.md` | Autonomous specialist; owns a bounded domain; invoked by commands or by asking Claude | Commands or natural language |
| **Skill** | `skills/*/SKILL.md` | Reusable instruction set referenced by agents and commands; not invoked directly | Agents and commands via `see SKILL.md` references |
| **Template** | `templates/*.md` | TOGAF artifact scaffold; filled by the interviewer and written to `artifacts/` | `/ea-artifact create` |
| **Script** | `scripts/*.py` | Python for binary output (Word, PPTX); invoked via Bash tool | `/ea-generate` |
| **Hook** | `hooks/hooks.json` | Lifecycle callbacks (pre/post command) | Plugin framework |

---

## 2. Data Flow

```
User intent
    │
    ▼
Command (.md)          ← reads: engagement.json, artifact files, skill references
    │
    ├──► Agent (.md)   ← reads: engagement.json, templates, reference files
    │        │
    │        └──► Skill (SKILL.md)   ← read-only reference; never writes directly
    │
    └──► Script (.py)  ← reads: engagement.json, artifact .md
             │
             └──► .docx / .pptx output
```

All persistent state lives in `EA-projects/{slug}/`. Commands and agents read and write there. Skills are read-only references — they never write files directly.

---

## 3. Reference File Hierarchy

When adding logic to an agent or command, check these files before writing anything inline:

| File | What it owns |
|---|---|
| `skills/ea-artifact-templates/references/ea-concepts.md` | All 13 EA concept definitions — **never redefine inline** |
| `skills/ea-artifact-templates/references/compliance-check.md` | All compliance rules (T1/T2/T3) — add new T3 rules here |
| `skills/ea-artifact-templates/references/phase-interview-questions.md` | All phase question banks and output routing tables |
| `skills/ea-artifact-templates/references/cross-topic-detection.md` | Signal map for routing answers to the right artifact |
| `skills/ea-artifact-templates/references/artifact-descriptions.md` | Purpose, audience, contents, phase for every artifact type |
| `skills/ea-artifact-templates/SKILL.md` | A3 governance states and transition rules |
| `skills/ea-engagement-lifecycle/SKILL.md` | ID scheme, facilitator style behaviour, opt-out rules |

**Rule:** If the same logic (e.g., a concept definition, a compliance rule, a signal detection heuristic) appears in more than one place, it belongs in a reference file — not inline.

---

## 4. Adding a New Command

1. Create `commands/ea-{name}.md` with required frontmatter:
   ```yaml
   ---
   name: ea-{name}
   description: One-line description
   argument-hint: "[optional] [args]"
   allowed-tools: [Read, Write, Bash]
   ---
   ```

2. Structure the command as numbered steps. Each step should:
   - Have a single clear responsibility
   - Reference skills and agents rather than duplicating their logic inline
   - Show example output blocks for any user-facing prompts

3. If the command writes to `engagement.json`, document the fields it touches in the step.

4. Validate frontmatter: `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`

5. Add the command to:
   - `README.md` commands table
   - `commands/ea-help.md` all-commands table
   - `docs/PRD.md` §7 commands table

---

## 5. Adding a New Agent

1. Create `agents/ea-{name}.md` with required frontmatter:
   ```yaml
   ---
   name: ea-{name}
   description: >
     Use this agent when [trigger condition]. Examples:
     <example>...</example>
   model: inherit
   color: {colour}
   tools: ["Read", "Write", "Glob", "Grep"]
   ---
   ```

2. Define the agent's **boundary** clearly at the top: what it owns, what it explicitly does NOT do.

3. If the agent references concepts from `ea-concepts.md`, cite them by name — do not redefine them.

4. Add the agent to `docs/PRD.md` §8 agents table.

5. Validate frontmatter.

**Colours in use:** yellow (ea-facilitator), cyan (ea-roadmap), magenta (ea-document-analyst). Pick an unused colour to distinguish the new agent visually.

---

## 6. Adding a New Skill

1. Create `skills/ea-{name}/SKILL.md` with required frontmatter:
   ```yaml
   ---
   name: EA {Name}
   description: One-line description — what triggers this skill
   version: 0.1.0
   ---
   ```

2. Skills are reference material, not executable commands. Write them as clear prose or structured tables that agents and commands can cite. Avoid imperative step lists — those belong in commands.

3. Bump version when the skill content changes materially.

4. Validate frontmatter.

---

## 7. Adding a New Artifact Template

1. Create `templates/{artifact-name}.md` using the standard template structure:
   ```markdown
   ---
   artifact: {Artifact Name}
   engagement: {{engagement_name}}
   phase: {phase}
   status: Draft
   reviewStatus: Not Reviewed
   version: 0.1
   lastModified: {{YYYY-MM-DD}}
   ---

   <details>
   <summary>📋 Guidance</summary>
   ...guidance block (hidden in rendered view)...
   </details>

   # {Artifact Name}

   **Engagement:** {{engagement_name}}
   **Organisation:** {{organisation}}
   **Date:** {{YYYY-MM-DD}}

   ---
   ## 1. {Section}
   ...
   ## Appendix A3 — Decision Log     ← include for key Phase A/B/D/E/G artifacts
   ```

2. Add an entry to `skills/ea-artifact-templates/references/artifact-descriptions.md`.

3. Add the artifact to the artifact table in `docs/PRD.md` §5.4.

4. Add a T3 compliance rule in `skills/ea-artifact-templates/references/compliance-check.md` if the artifact has mandatory sections.

5. Add the artifact to the `ARTIFACT_SECTIONS` dictionary in `scripts/generate-docx.py` and the `DEFAULT_DECKS` dictionary in `scripts/generate-pptx.py` if Word/PPTX export is needed.

6. Add a row to the Artifact Type Mapping table in `commands/ea-generate.md`.

---

## 8. Extending the Python Scripts

`scripts/generate-docx.py` and `scripts/generate-pptx.py` accept content via `--content @{json-file}`.

**Content JSON format for docx:**
```json
{
  "sections": [
    { "heading": "Section Title", "content": "Body text", "level": 1 },
    { "heading": "Subsection", "content": "Body text", "level": 2 }
  ],
  "tables": [
    {
      "heading": "Table Title",
      "headers": ["Col A", "Col B", "Col C"],
      "rows": [["val", "val", "val"]]
    }
  ]
}
```

**Content JSON format for pptx:**
```json
{
  "slides": [
    { "layout": "title", "title": "{title}", "subtitle": "{org} | {date}" },
    { "layout": "content", "title": "Slide Title", "bullets": ["Point 1", "Point 2"] },
    { "layout": "table", "title": "Table Slide", "headers": ["A", "B"], "rows": [["v", "v"]] }
  ]
}
```

**Script invocation pattern:**
```bash
SCRIPT=$(find "$HOME/.claude" -name "generate-docx.py" -path "*/ea-assistant/scripts/*" | head -1)
VENV="$HOME/.ea-assistant-venv"
[ ! -f "$VENV/bin/python" ] && python3 -m venv "$VENV"
"$VENV/bin/pip" install --quiet python-docx python-pptx 2>/dev/null
"$VENV/bin/python" "$SCRIPT" \
  --type {script-type} \
  --engagement-dir EA-projects/{slug} \
  --content @/tmp/ea-gen-{id}.json \
  --output EA-projects/{slug}/artifacts/{id}.docx
```

`--type` values must match keys in `ARTIFACT_SECTIONS` (docx) or `DEFAULT_DECKS` (pptx): `vision`, `gap-analysis`, `app-portfolio`, `requirements-register`, `roadmap`, `stakeholder-map`.

---

## 9. Compliance Rule Authoring

New Tier 3 rules go in `skills/ea-artifact-templates/references/compliance-check.md` under the Tier 3 table.

**Rule format:**

| Artifact | Requirement | Rule ID |
|---|---|---|
| {Artifact Name} | {What must be present/true} | T3-{SHORT-CODE} |

**Severity guidance (for compliance prompt output):**

| Level | Condition | Effect |
|---|---|---|
| **Critical** | Any T1 failure (missing frontmatter field) | Block artifact open; must remediate |
| **High** | Missing mandatory section (T3 rule) | Warn; offer remediate or accept-as-is |
| **Medium** | Template drift (T2 — missing standard section) | Warn; offer remediate or accept-as-is |
| **Low** | Style or content quality (e.g. placeholder not filled) | Inform only; no block |

---

## 10. Consistency Checking

The `ea-consistency-checker` agent performs cross-artifact analysis. When reporting issues it uses this severity scale:

| Severity | Example |
|---|---|
| **Critical** | A Goal in Architecture Vision has no corresponding entry in Business Architecture (traceability broken) |
| **High** | A Strategy references a Goal ID that doesn't exist in the vision |
| **Medium** | Phase E work packages reference gaps not found in any Gap Analysis artifact |
| **Low** | Stakeholder listed in Vision not present in Stakeholder Map |

Findings are reported as a structured table: `Severity | Artifact A | Artifact B | Issue | Recommended action`.

---

## 11. Interview Question Bank Authoring

New questions for an ADM phase go in `skills/ea-artifact-templates/references/phase-interview-questions.md` under the relevant `## Phase {X} Interview` section.

**Each question block must include:**
- A `**Goal:**` line stating the interview objective
- Numbered questions
- An **Output Routing** table (`Response Topic | Target Artifact | Target Field`)
- **Facilitation Notes** (when to probe, when to accept, what the question is really testing)

**Output routing convention:** `Target Field` values use `{{snake_case_placeholder}}` matching the corresponding template token.

---

## 12. Hooks

`hooks/hooks.json` declares lifecycle callbacks. The current schema requires the `hooks` key:

```json
{
  "hooks": {}
}
```

To add a hook:
```json
{
  "hooks": {
    "pre-command": "echo 'before any command'",
    "post-command": "echo 'after any command'"
  }
}
```

An empty `{}` at the top level (without the `hooks` key) causes plugin load failure.

---

## 13. Feature Specification Workflow

When adding a significant new feature, follow this sequence before writing any code:

### Step 1 — Clarify
Identify ambiguities before planning. For each uncertain area, write down:
- What is underspecified?
- What are the 2–3 plausible interpretations?
- Which interpretation aligns best with the PRD principles?

Resolve ambiguities in the PRD (`docs/PRD.md`) before proceeding.

### Step 2 — Specify
Define the feature in the PRD:
- Which section does it belong to? (§5.x Feature, §7 Commands, §8 Agents)
- What are the user-facing behaviours?
- What files does it touch?
- What quality gates apply?

Use this checklist to validate the spec:
- [ ] User-facing behaviour described from the user's perspective (not implementation detail)
- [ ] All affected files listed
- [ ] Output format or example shown
- [ ] Edge cases and error states covered
- [ ] Consistent with existing ID scheme, naming conventions, and agent boundaries

### Step 3 — Plan
Before writing files, list:
- New files to create (agent, command, skill, template)
- Existing files to modify (reference files, compliance rules, help, README, PRD)
- Dependencies between changes (e.g., new T3 rule requires template change first)
- Validation step (frontmatter check, manual test scenario)

### Step 4 — Implement
Work through the plan file by file. After each file:
- Run frontmatter validation if the file has frontmatter
- Check that cross-references (e.g., skill citations, ID references) resolve

### Step 5 — Document
After implementation, update in this order:
1. `docs/PRD.md` — add/update the relevant feature section
2. `README.md` — add feature to the Features list
3. `commands/ea-help.md` — update command table and tips if needed
4. `CLAUDE.md` (plugin-level) — update if agent boundaries, ID scheme, or key files changed

---

## 14. Versioning

| File | When to bump |
|---|---|
| `.claude-plugin/plugin.json` `version` | Any user-facing change (new command, agent, skill, template) |
| Skill `SKILL.md` `version` | Any change to skill content |
| `docs/PRD.md` `Version` | Any feature addition or significant change |

Version format: `MAJOR.MINOR.PATCH`
- **PATCH** — bug fix, doc update, wording correction
- **MINOR** — new feature, new agent/command/skill/template
- **MAJOR** — breaking change to engagement.json schema, artifact template structure, or ID scheme

---

## 15. Engagement.json Schema Extension

When adding new fields to `engagement.json`:
- Add the field to the schema in `docs/PRD.md` §6
- Add the field to the `engagement.json Template` block in `commands/ea-new.md`
- Update the CLAUDE.md refresh step in `commands/ea-open.md` if the field should appear in the per-engagement CLAUDE.md
- Ensure backward compatibility — new fields must be optional or have safe defaults; do not require migration of existing engagement files

---

## 16. Development Checklist

Before committing any change:

- [ ] Frontmatter validated: `~/.bun/bin/bun .github/scripts/validate-frontmatter.ts ea-assistant/`
- [ ] No concept definitions duplicated inline (reference `ea-concepts.md`)
- [ ] No style rules duplicated inline (reference `ea-engagement-lifecycle/SKILL.md`)
- [ ] No cross-topic detection logic duplicated inline (reference `cross-topic-detection.md`)
- [ ] All new agents have a boundary statement
- [ ] All new T3 compliance rules added to `compliance-check.md`
- [ ] All new artifact types added to `artifact-descriptions.md`
- [ ] `docs/PRD.md`, `README.md`, `commands/ea-help.md` updated if user-facing
- [ ] `CLAUDE.md` (plugin-level) updated if architecture changed
- [ ] Conventional commit message used: `feat|fix|docs|chore(ea-assistant): ...`
- [ ] Feature branch + PR for multi-file changes; direct commit for single-file fixes

---

## 17. Open Design Questions

These are known architectural trade-offs that have been consciously deferred. Each is marked with a suggested trigger for revisiting.

### OD-001 — `ea-interviewer` monolith vs. split agents

**Status:** Deferred — potential future enhancement

**The bet:** `ea-interviewer` is a 550+ line agent covering artifact interview, phase interview, 4 UI modes, cross-topic detection, concept-checking, A3 decision logging, governance transitions, inline brainstorm, opt-out handling, contextual help, and session logging. The bet is that Claude can reliably execute the full file without missing branches.

**Risk:** As the file grows, reliability degrades. Specific failure modes to watch for:
- Cross-topic detection not firing during Text interviews
- Session log not being written after opt-out sessions
- Governance state transitions (`govern` command) being missed

**Trigger to revisit:** If any of the above failure modes are observed in practice, split the A3/governance logic and opt-out/help handlers into a reference file the interviewer loads (`references/interview-handlers.md`), and separate the Phase Interview flow into a dedicated `ea-phase-interviewer` agent.

---

### OD-002 — `ea-document-analyst` vs. `ea-requirements-analyst` as separate agents

**Status:** Deferred — potential future enhancement

**The bet:** Two agents process uploaded documents. `ea-document-analyst` does broad EA mapping (strategy → Vision, processes → Business Architecture). `ea-requirements-analyst` does structured requirements extraction with ADM phase coverage and Zachman classification. They are different enough in output format to justify separate agents.

**Risk:** Users may not know which to invoke. The natural entry point ("I have a document") could reach either agent depending on how it's phrased. The engagement may end up with duplicate or inconsistent extractions from the same source file.

**Trigger to revisit:** If user confusion is observed (wrong agent invoked, same document processed twice), consider merging into one `ea-document-analyst` agent with two modes: `general` (current document analyst) and `requirements` (current requirements analyst). The `ea-requirements-analyst` would become a mode, not a separate agent.

---

### OD-003 — No `engagement.json` write conflict resolution

**Status:** Deferred — potential future enhancement

**The bet:** In any given session, only one agent is active at a time. The write protocol (§ engagement.json Write Protocol in `ea-engagement-lifecycle/SKILL.md`) is followed by each agent, so section-level isolation prevents conflicts.

**Risk:** If a user switches between agents mid-session without completing the first agent's write (e.g. abandons an interview mid-way, then runs `/ea-open`), the last write wins and the intermediate state is silently discarded.

**Trigger to revisit:** If data loss from mid-session switches is reported, implement a write-verify step: before writing `engagement.json`, read it fresh and check whether the key fields you're about to overwrite have changed since you last read them. If they have, alert the user before proceeding.

---

### OD-004 — `ea-engagement-lifecycle` SKILL.md as reference vs. executable specification

**Status:** Deferred — potential future enhancement

**The bet:** Skills are read-only reference material; agents and commands cite them. `ea-engagement-lifecycle/SKILL.md` currently contains prescriptive workflow steps (Starting a New Engagement, Editing Workflows, Archive/Restore/Delete) that go beyond classification or reference — they read like a command definition.

**Risk:** If the skill continues to grow with workflow logic, it will become a shadow command that agents partially execute, partially ignore, creating unpredictable behaviour. Commands (`/ea-new`, `/ea-open`) are the authoritative source for workflow steps; the skill should be the authoritative source for schema definitions and status values only.

**Trigger to revisit:** If the skill exceeds 600 lines, extract the workflow steps into a `references/engagement-workflows.md` reference document, and reduce the skill to: schema definitions, status enumerations, state transition rules, write protocol, and content policy.
