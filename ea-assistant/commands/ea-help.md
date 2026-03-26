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
| `/ea-generate [artifact] [format]` | Export artifact as Word, PPTX, or Mermaid |
| `/ea-review [artifact]` | Review and assess an artifact |
| `/ea-requirements [action]` | Manage architecture requirements |
| `/ea-decisions [options]` | Generate Decision Register from all A3 decision logs |
| `/ea-publish` | Merge artifacts into a consolidated report |
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
| `?` / `help` | Show this guide + current artifact context and purpose |
| `concepts` | Show the EA concepts quick reference (Principle/Goal/Strategy/Plan/Risk) |

**Opt-out vs. Skip:**
- **Skip** (`s`) means "I'll come back to this" — temporary, does not appear in reports as a concern
- **Opt-out** (`opt-out`) means "I am deliberately not doing this" — permanent, tracked in `engagement.json`, flagged in `/ea-status` and consolidated reports

### Tips

• Run `/ea-brainstorm` before or during interviews — the interviewer
  will reference your notes as it asks questions. You can also brainstorm
  inline by typing "brainstorm" at any interview prompt.
• Use `/ea-interview start phase [name]` for guided phase interviews
  with output routing to the right artifacts.
• Use `/ea-generate` to export individual artifacts; `/ea-publish` for
  a full consolidated document.
• Upload documents to `EA-projects/{name}/uploads/` and the
  requirements analyst agent will extract structured requirements.
• Type `?` at any interview prompt for contextual help including
  the artifact's purpose, value, and guidance on the current question.
• Ask "how does architecture governance work" for a full explanation of
  the governance structure, cascade, roles, and TOGAF tool mapping.
```

5. **If the user asks about architecture governance** (e.g. "how does governance work", "explain the ARB", "what is the governance cascade", "governance roles", "Phase G governance"), read `skills/ea-engagement-lifecycle/references/governance-framework.md` and present it in full. The file contains two images (`images/governance-structure.png` and `images/governance-cascade.png`) — display both inline at the points where they are referenced in the document. Do not summarise — present the full reference.

6. **Otherwise, do not add any content beyond what is specified above.** Keep the output clean and scannable.
