---
name: ea-help
description: Show how to get started with EA Assistant and list all available commands
allowed-tools: [Read, Bash]
---

Display a getting-started guide and command reference for EA Assistant.

## Instructions

1. **Check for existing engagements.** Run `ls EA-projects/*/engagement.json 2>/dev/null` to detect any existing projects.

2. **Display the guide.** Print the following, adapting the "Getting Started" section based on whether engagements exist:

---

**If no engagements exist:**

```
## EA Assistant — Getting Started

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

**If engagements exist, replace the Quick Start section with:**

```
### Resume Work

You have existing engagements. Common next steps:

  `/ea-status`                  → See all engagements and progress
  `/ea-open [name]`             → Open an engagement to continue work
  `/ea-phase [phase]`           → Start or resume an ADM phase
  `/ea-interview start phase A` → Run Phase A interview questions
```

---

3. **Always show the full command reference:**

```
### All Commands

| Command | Description |
|---|---|
| `/ea-new` | Create a new engagement |
| `/ea-open` | Open, edit, archive, or delete an engagement |
| `/ea-status` | Portfolio dashboard — progress, artifacts, phases |
| `/ea-phase [phase]` | Start, edit, or resume an ADM phase |
| `/ea-artifact [action]` | Create or list artifacts |
| `/ea-interview [mode]` | Stakeholder interviews (artifact or phase mode) |
| `/ea-generate [artifact] [format]` | Export artifact as Word, PPTX, or Mermaid |
| `/ea-review [artifact]` | Review and assess an artifact |
| `/ea-requirements [action]` | Manage architecture requirements |
| `/ea-publish` | Merge artifacts into a consolidated report |
| `/ea-help` | This guide |

### Tips

• Use `/ea-interview start phase [name]` for guided phase interviews
  with output routing to the right artifacts.
• Use `/ea-generate` to export individual artifacts; `/ea-publish` for
  a full consolidated document.
• Upload documents to `EA-projects/{name}/uploads/` and the
  requirements analyst agent will extract structured requirements.
• Ask "how does architecture governance work" for a full explanation of
  the governance structure, cascade, roles, and TOGAF tool mapping.
```

4. **If the user asks about architecture governance** (e.g. "how does governance work", "explain the ARB", "what is the governance cascade", "governance roles", "Phase G governance"), read `skills/ea-engagement-lifecycle/references/governance-framework.md` and present it in full. The file contains two images (`images/governance-structure.png` and `images/governance-cascade.png`) — display both inline at the points where they are referenced in the document. Do not summarise — present the full reference.

5. **Otherwise, do not add any content beyond what is specified above.** Keep the output clean and scannable.
