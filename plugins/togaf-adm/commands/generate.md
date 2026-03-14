---
name: generate
description: Generate a specific TOGAF artifact from the current project context. Asks for any missing inputs, then produces a structured Mermaid diagram, formatted table, or document outline ready for export. Accepts an optional artifact name argument.
argument-hint: "[vision|stakeholder-map|capability-map|process-flow|app-portfolio|tech-landscape|gap-analysis|roadmap|requirements-register]"
allowed-tools: Read, Write, Bash
---

Generate a named TOGAF artifact from the current project context.

## Steps

1. Read `.claude/togaf-adm.local.md` to load the project context.

2. Determine the artifact to generate:
   - If an argument was provided, use it.
   - Otherwise, ask: "Which artifact would you like to generate?" and list the nine options with their phase.

3. Check what inputs are already available in the project context for this artifact.

4. For any missing required inputs, ask the user — ONE question at a time.

5. Generate the artifact in its native format:
   - **Diagrams** (capability-map, process-flow, tech-landscape, roadmap, stakeholder-map): Produce a Mermaid code block with a clear title
   - **Tables/Catalogs** (app-portfolio, gap-analysis, requirements-register): Produce a formatted Markdown table
   - **Documents** (vision): Produce a structured outline with section content

6. Display the generated artifact and ask: "Does this look correct, or would you like to adjust anything?"

7. After confirmation, ask: "Would you like to export this as a Word document, PowerPoint slides, or keep it as Mermaid/Markdown? (word / powerpoint / keep)"
   - If `word` or `powerpoint`, invoke `/togaf:export [format]` automatically

8. Save the confirmed artifact content to the project context file for future reference.

## Artifact Quick Reference

| Argument | Artifact | Phase | Primary Format |
|----------|----------|-------|----------------|
| `vision` | Architecture Vision Document | A | Word |
| `stakeholder-map` | Stakeholder Map | A | Mermaid + Table |
| `capability-map` | Business Capability Map | B | Mermaid |
| `process-flow` | Process Flow Diagram | B | Mermaid |
| `app-portfolio` | Application Portfolio Catalog | C | Table |
| `tech-landscape` | Technology Landscape | D | Mermaid (C4) |
| `gap-analysis` | Gap Analysis | B/C/D | Table |
| `roadmap` | Architecture Roadmap | F | Mermaid (Gantt) |
| `requirements-register` | Requirements Register | All | Table |
