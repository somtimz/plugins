---
name: status
description: Display the current TOGAF ADM project status — project metadata, active phase, phases completed, artifacts generated, and open gaps. Provides a quick snapshot of engagement progress.
allowed-tools: Read
---

Display a full status dashboard for the current TOGAF ADM project.

## Steps

1. Read `.claude/togaf-adm.local.md` to load the project context.

2. If no project context exists, display:
   "No active TOGAF project found. Start one with `/togaf:phase preliminary` to set up your project."

3. Display the status dashboard with these sections:

### Project Overview
- Project name
- Organisation
- Lead architect
- Architecture scope
- Start date
- Current phase

### ADM Phase Progress
Show all phases with status:
- ✅ Complete
- 🔄 In Progress
- ⬜ Not Started

Phases: Preliminary | A | B | C | D | E | F | G | H | Requirements Management

### Artifacts Status
For each of the nine priority artifacts, show:
- ✅ Generated (and output format)
- 📝 In Progress (fields populated: X/Y)
- ⬜ Not Started

### Requirements Summary
- Total requirements captured: N
- By type: Business (N), Functional (N), Non-Functional (N), Constraint (N)
- Requirements without phase assignment: N

### Open Gaps
List any identified gaps that have not yet been addressed.

### Recommended Next Step
Based on current phase and artifact completion, suggest the most logical next action. Examples:
- "Recommended: Run `/togaf:phase b` to start Business Architecture"
- "Recommended: Run `/togaf:generate gap-analysis` to complete Phase B"
- "Recommended: Run `/togaf:export word` to produce the Architecture Vision document"
