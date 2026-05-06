---
name: ea-help
description: Show how to get started with EA Assistant and list all available commands
allowed-tools: [Read, Bash]
---

Display a getting-started guide and command reference for EA Assistant.

## Instructions

1. **Read the plugin version.** Read `.claude-plugin/plugin.json` from the ea-assistant plugin directory and extract the `version` field.

2. **Check for existing engagements.** Run `ls EA-projects/*/engagement.json 2>/dev/null` to detect any existing projects.

3. **Display the guide.** Print the following, adapting the "Getting Started" section based on whether engagements exist:

---

**If no engagements exist:**

```
## EA Assistant v{version} — Getting Started

EA Assistant manages Enterprise Architecture engagements using TOGAF 10,
Zachman Framework, and ArchiMate 3.x.

### Quick Start

1. `/ea-new`           → Create your first engagement
2. `/ea-phase prelim`  → Start the Preliminary phase
3. `/ea-interview`     → Run a stakeholder interview
4. `/ea-artifact`      → Generate an architecture artifact
5. `/ea-review`        → Review and assess an artifact
6. `/ea-publish`         → Produce a consolidated report

### Typical Workflow

  Create engagement → Preliminary phase → Phase A (Vision) → Phase B–D
  (domain architectures) → Phase E/F (roadmap) → Phase G/H (governance)

  At each phase you can:
  • `/ea-interview start phase [phase-name]` — run the phase question bank
  • `/ea-artifact [artifact-type]` — generate artifacts from templates
  • `/ea-generate [artifact] [docx|pptx|mermaid]` — export to Word/PPTX/diagram
  • `/ea-requirements` — manage architecture requirements
  • `/ea-review` — review artifacts for completeness and quality
```

**If engagements exist:**

```
## EA Assistant v{version} — Getting Started

### Resume Work

You have existing engagements. Common next steps:

  `/ea-status`                  → See all engagements and progress
  `/ea-open [name]`             → Open an engagement to continue work
  `/ea-phase [phase]`           → Start or resume an ADM phase
  `/ea-interview start phase A` → Run Phase A interview questions
```

---

4. **Always show the full command reference:**

```
### All Commands

| Command | Description |
|---|---|
| `/ea-new` | Create a new engagement |
| `/ea-open` | Open, edit, archive, or delete an engagement |
| `/ea-status` | Portfolio dashboard — progress, artifacts, phases, opt-outs |
| `/ea-phase [phase]` | Start, edit, or resume an ADM phase |
| `/ea-artifact [action]` | Create or list artifacts |
| `/ea-interview [mode]` | Stakeholder interviews (artifact or phase mode) |
| `/ea-brainstorm [phase]` | Capture freeform thoughts and context for use during interviews |
| `/ea-generate [artifact] [format]` | Export artifact as Word, PPTX, Mermaid, PNG, or SVG; embeds diagrams in docx/pptx by default |
| `/ea-review [artifact]` | Review and assess an artifact |
| `/ea-grill [artifact] [--skill]` | Deep-review an artifact using a grill-me skill; then optionally apply findings back to the artifact one revision at a time |
| `/ea-requirements [action]` | Manage architecture requirements |
| `/ea-decisions [options]` | Generate Decision Register from all A3 decision logs |
| `/ea-adrs [mode]` | Manage Architecture Decision Records (generate, new, update) |
| `/ea-risks [mode]` | Generate and maintain a cross-cutting Risk Register |
| `/ea-changes [mode]` | Generate Change Register for Phase H ACR artifacts |
| `/ea-concerns` | Manage CON-NNN stakeholder concerns (Appendix A4) |
| `/ea-roles [ROLE-ID\|--domain\|--generate\|--update]` | Role Catalogue — list, filter, and generate role assignments with RACI, triggers, and calendar |
| `/ea-direction [goals\|objectives\|strategies] [--domain X]` | View Direction Register — Goals, Objectives, Strategies from motivation artifacts |
| `/ea-zachman [mode]` | Manage the Zachman 6×6 classification diagram (generate, review, gap, interview, classify) |
| `/ea-research [mode]` | Research library — add, note, link, list, view, apply findings to artifacts |
| `/ea-next` | Suggest the single most valuable next action for the active engagement |
| `/ea-notes [mode]` | List, view, edit, or delete interview notes, brainstorm notes, and review files |
| `/ea-consistency [options]` | Focused consistency check — cross-artifact contradictions, within-artifact section inconsistencies, or ID reference scan only (`--ids`) |
| `/ea-engage-review` | Full engagement health check — coverage, traceability, governance, ADR status, Zachman |
| `/ea-security-review` | Security audit — SABSA, ISO 27001, and NIST CSF 2.0 coverage across the engagement or a single artifact |
| `/ea-reorganize [--report]` | Move flat-path artifacts into correct phase subfolders; update engagement.json paths |
| `/ea-migrate [--report]` | Align legacy engagement to current plugin version conventions |
| `/ea-publish` | Merge artifacts into a consolidated report |
| `/ea-summary [refresh\|status]` | Refresh or review per-artifact executive summaries |
| `/ea-brief [--focus decisions\|risks\|gaps\|strategy] [--save]` | Synthesized one-page engagement brief — ranked decisions, gaps, risks, open concerns |
| `/ea-workshop [start\|resume\|export\|list]` | Facilitated multi-stakeholder workshops — WS-NNN minutes, agenda, decisions, actions |
| `/ea-arb [new\|list\|view\|close]` | ARB meeting minutes — ARB-NNN, quorum, decisions, propagate to ADR register |
| `/ea-config [section]` | Configure plugin settings, engagement rules, opt-outs, and refresh CLAUDE.md |
| `/ea-help` | This guide |

### Interview Shortcuts

Type these at any interview prompt:

| Shortcut | What it does |
|---|---|
| `d` / `default` | Accept the suggested default answer |
| `s` / `skip` | Skip for now — field marked ⚠️ Not answered (can revisit) |
| `n/a` | Mark not applicable — field marked ➖ |
| `opt-out` | Opt out of this question — field marked ⊘, reason tracked |
| `opt-out artifact` | Opt out of the entire artifact — all fields marked ⊘ |
| `y` | Keep the existing/previous answer |
| `a: {text}` | Log as a governance decision (writes to Appendix A3) |
| `govern` / `g` | Update governance state of an A3 decision row |
| `b:` / `brainstorm` | Start a freeform brainstorm pause |
| `resume` / `done` | End brainstorm and return to the interview |
| `r: {query}` / `research: {query}` | Research a topic mid-interview; findings surfaced inline with option to save to ResearchAndReferences |
| `e: {statement}` | Economic framing pause — add cost/risk/value analysis to any answer |
| `d: {statement}` | Decide/Defer pause — 5-factor assessment (evidence, reversibility, impact, urgency, capability); recommends: Decide now / Defer / Guardrails / Premature / Risky commit; offers to create PAD-NNN |
| `?` / `help` | Show this guide + current artifact context and purpose |
| `concepts` | Show the EA concepts quick reference (Vision/Mission/Principle/Goal/Objective/Strategy/Plan/Risk/Issue/Problem/Capability Model/Operating Model/Metrics) |

**Opt-out vs. Skip:**
- **Skip** (`s`) means "I'll come back to this" — temporary, does not appear in reports as a concern
- **Opt-out** (`opt-out`) means "I am deliberately not doing this" — permanent, tracked in `engagement.json`, flagged in `/ea-status` and consolidated reports

### Tips

• Run `/ea-brainstorm` before or during interviews — the interviewer
  will reference your notes as it asks questions. You can also brainstorm
  inline by typing "brainstorm" at any interview prompt.
• Use `/ea-interview start phase [name]` for guided phase interviews
  with output routing to the right artifacts.
• Use `/ea-generate [artifact] [docx|pptx|mermaid|png|svg]` to export
  individual artifacts — diagrams are embedded automatically in docx/pptx.
  Use `/ea-publish` for a full consolidated document.
• Upload documents to `EA-projects/{name}/uploads/` and the
  ea-document-analyst agent will extract architecture-relevant content
  and map it to the appropriate artifact sections.
• Type `?` at any interview prompt for contextual help including
  the artifact's purpose, value, and guidance on the current question.
• Ask "let's build the roadmap" to start the ea-roadmap agent —
  it reads your Vision goals and strategies to seed work packages
  automatically (or works from scratch if no artifacts exist yet).
• After `/ea-grill`, choose "apply findings" to revise the artifact
  one recommendation at a time, with confirm/skip/edit per change.
• Use `/ea-research` to add whitepapers, notes, or URL references to
  the engagement library. Run `/ea-research apply` to synthesise
  research against any artifact and apply findings with y/n/edit.
• Type `r: {query}` at any interview or brainstorm prompt to trigger
  an inline research pause — the interviewer searches your engagement
  library and synthesises findings, then offers to save them to
  ResearchAndReferences before resuming.
• Use `/ea-adrs` to manage Architecture Decision Records. The interviewer
  suggests an ADR automatically when a significant decision is detected.
• Use `/ea-zachman` to classify and review engagement content across the
  Zachman 6×6 grid — generate, review, gap, interview, or classify modes.
• Use `/ea-risks` to generate a cross-cutting Risk Register from all
  artifact risk sections; `/ea-changes` for Phase H change management.
• Use `/ea-consistency --ids` for a fast ID reference scan before publishing —
  finds broken references and orphaned IDs without the full consistency sweep.
  Use `/ea-consistency artifact [name]` to check a single artifact for
  within-section label contradictions and broken ID refs.
• Use `/ea-engage-review` for a full engagement health check — coverage,
  traceability, governance, ADR status, and Zachman completeness.
• Use `/ea-grill --skill practitioner` for an economic framing and decision
  quality review; `--skill maturity` to assess against the L1–L5 maturity model;
  `--skill failure-mode` to run a pre-mortem against the 6 failure modes.
• During `/ea-brainstorm`, type `p:`, `f:`, `o:`, `m:`, or `e:` to trigger
  advanced practitioner pauses (pattern discovery, failure-mode scan, optionality
  exploration, maturity assessment, economic framing).
• During `/ea-interview`, type `e: {statement}` to trigger an economic framing
  pause — add cost/risk/value analysis to any answer.
• Use `/ea-config rules` to teach the engagement project-specific rules (e.g. naming
  conventions, methodology constraints, compliance requirements). Rules are written to
  `.claude/rules/ea-engagement.md` and loaded automatically by Claude Code each session.
• Ask "how does architecture governance work" for a full explanation of
  the governance structure, cascade, roles, and TOGAF tool mapping.
• Each engagement folder contains `.claude/rules/ea-engagement.md` —
  persistent session rules automatically loaded by Claude Code. They
  enforce /ea-open at session start, protect Approved artifacts, and
  point to the single-source-of-truth reference files for concepts and
  phase guidance. Run `/ea-migrate` if the file is missing.

### Research in an engagement — two agents

**`ea-research` agent** — EA-aware research intelligence. Use it for:
- "Quick research: what are the key risks of cloud-first for financial services?" (1-2 search fast lookup with confidence scores)
- "Deep research: investigate zero-trust architecture options for Phase D" (structured 4-phase investigation — planning, searches, analysis, synthesis report)
- "What should I research before Phase D?" (phase research planning — recommends a backlog, no searches)
- "Synthesise the vendor reports into a comparison matrix" (consolidates existing library items — no searches)
- "Are there gaps or outdated sources in our research library?" (quality audit)
- "Which research items influenced the Phase D technology choices?" (impact tracing)

Unlike `@research-agent`, the `ea-research` agent is EA-context-aware: it reads the active engagement, current phase, and open decisions before responding.

**`@research-agent`** — General deep research. Use it when you need
evidence, citations, or deeper investigation before populating an artifact.

| When | Example |
|---|---|
| Identifying business drivers | `@research-agent research current regulatory drivers for financial services data governance in the EU` |
| Validating a technology choice | `@research-agent investigate event-driven architecture adoption patterns in retail banking` |
| Grounding a risk or assumption | `@research-agent find evidence on failure rates for large-scale ERP consolidations` |
| Populating a Business Model Canvas | `@research-agent research competitor business models in the B2B SaaS payroll space` |

The agent maps the topic, gathers primary evidence with citations, flags contradictions, and
returns an executive-ready synthesis with confidence scores. Paste findings directly into
brainstorm notes or artifact fields.
```

5. **If the user asks about architecture governance** (e.g. "how does governance work", "explain the ARB", "what is the governance cascade", "governance roles", "Phase G governance"), read `skills/ea-engagement-lifecycle/references/governance-framework.md` and present it in full. The file contains two images (`images/governance-structure.png` and `images/governance-cascade.png`) — display both inline at the points where they are referenced in the document. Do not summarise — present the full reference.

6. **Otherwise, do not add any content beyond what is specified above.** Keep the output clean and scannable.
