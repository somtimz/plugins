---
name: load
description: Load an existing document, requirements file, or architecture input into the current TOGAF project context. Parses the content, extracts architecture-relevant information, and maps it to ADM phases and artifact fields. Accepts a file path argument.
argument-hint: "[file-path]"
allowed-tools: Read, Write, Bash
---

Ingest an existing document as input to the current TOGAF ADM engagement.

## Steps

1. Read `.claude/togaf-adm.local.md` to load the project context.

2. Determine the file to load:
   - If an argument was provided, use that file path.
   - Otherwise, ask: "Please provide the path to the file you want to load."

3. Validate the file:
   - Check the file exists and is readable
   - Confirm the file type: `.txt`, `.md`, or `.docx`
   - For `.docx` files, extract text using: `python3 -c "from docx import Document; doc = Document('[file]'); print('\n'.join([p.text for p in doc.paragraphs]))"`
   - For `.txt` and `.md` files, read directly with the Read tool

4. Analyse the document content:
   - Identify the document type (strategy doc, requirements spec, business case, existing architecture, etc.)
   - Extract key entities: goals, drivers, constraints, assumptions, stakeholder names, systems, processes, technologies

5. Map extracted information to TOGAF artifact fields:
   - Goals/drivers → Architecture Vision, Architecture Principles
   - Requirements → Requirements Register
   - Constraints → Requirements Register (type: Constraint)
   - Stakeholders mentioned → Stakeholder Map
   - Systems/applications → Application Portfolio Catalog
   - Technologies → Technology Portfolio Catalog
   - Processes → Process Flow Diagram inputs

6. Present a structured extraction summary:
   - Document type identified
   - Number of requirements/items extracted
   - Which artifacts will be populated
   - List of extracted items with their target artifact

7. Ask: "Would you like me to add all of these to the project context, or review them one by one?"
   - If all: append to the relevant sections in `.claude/togaf-adm.local.md`
   - If review: show each item and await confirmation before adding

8. Identify gaps — requirements or information the document does not address — and offer to add them to a gaps list for follow-up interviews.
