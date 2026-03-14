---
name: phase
description: Enter or advance an ADM phase interactively. Loads the phase context, asks the user for required inputs one at a time, tracks completion, and populates artifact fields. Accepts an optional phase name argument.
argument-hint: "[preliminary|a|b|c|d|e|f|g|h|requirements]"
allowed-tools: Read, Write, Bash
---

Guide the user through a specific TOGAF 10 ADM phase interactively.

## Steps

1. Read the project settings file at `.claude/togaf-adm.local.md` to load the current project context (project name, organisation, current phase, completed phases).

2. Determine the target phase:
   - If an argument was provided (e.g., `phase a` or `phase preliminary`), use that phase.
   - If no argument, ask: "Which ADM phase would you like to work on? (Preliminary / A / B / C / D / E / F / G / H / Requirements Management)"

3. Display a phase summary:
   - Phase name and purpose
   - Key artifacts to produce in this phase
   - Required inputs (what we need to collect)
   - List any inputs already captured in the project context

4. Collect inputs interactively — ask ONE question at a time. Wait for the user's answer before asking the next. Use the phase-specific question set from the `togaf-interview-techniques` skill.

5. After each answer:
   - Acknowledge the response
   - Map it to the relevant artifact field
   - Confirm: "I've recorded that as [field] in the [artifact]. Is that correct?"

6. When sufficient inputs are collected for the phase's key artifacts, offer:
   - "You have enough to generate the following artifacts: [list]. Would you like to generate them now?"
   - If yes, invoke `/togaf:generate` for each artifact

7. Update the project settings file to record:
   - `current_phase` updated to this phase
   - Mark this phase as started in `completed_phases`

8. Close by summarising what was captured and what the natural next step is (e.g., "Phase A complete — recommend starting Phase B to define Business Architecture").
