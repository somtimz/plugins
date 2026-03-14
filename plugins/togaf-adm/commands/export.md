---
name: export
description: Export a TOGAF artifact as a Word document (.docx) or PowerPoint presentation (.pptx). Prompts the user to select which artifact to export and the desired output format, then runs the appropriate generation script.
argument-hint: "[word|powerpoint|mermaid]"
allowed-tools: Read, Write, Bash
---

Export a TOGAF artifact to a formatted output file.

## Steps

1. Read `.claude/togaf-adm.local.md` to load the project context and available artifacts.

2. Determine the output format:
   - If argument is `word` or `docx`, export as Word document
   - If argument is `powerpoint` or `pptx`, export as PowerPoint
   - If argument is `mermaid`, display the Mermaid source in a code block
   - If no argument, ask: "Which format would you like to export? (word / powerpoint / mermaid)"

3. Ask which artifact to export (if context has multiple generated artifacts):
   "Which artifact would you like to export?"
   List only artifacts that have been generated.

4. Confirm the output file name:
   Default: `[organisation]-[artifact-type]-[date].[ext]`
   Example: `acme-architecture-vision-2025-03.docx`
   Ask: "Save as [filename]? (Press Enter to confirm or type a new name)"

5. For Word export:
   - Prepare the content JSON from the project context
   - Run: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docx.py --type [type] --title "[title]" --org "[org]" --architect "[architect]" --output "[filename]" --content '[json]'`
   - Confirm: "✅ Word document saved to [filename]"

6. For PowerPoint export:
   - Prepare the content JSON from the project context
   - Run: `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-pptx.py --type [type] --title "[title]" --org "[org]" --architect "[architect]" --output "[filename]" --content '[json]'`
   - Confirm: "✅ PowerPoint saved to [filename]"

7. For Mermaid export:
   - Display the diagram source in a fenced mermaid block
   - Suggest: "Copy the above and paste it into any Mermaid renderer (VS Code, Mermaid Live, Notion, etc.)"

8. If the generation script fails:
   - Show the error message
   - Check if `python-docx` / `python-pptx` is installed
   - Suggest: "Run `pip3 install python-docx python-pptx` to install dependencies, then retry."
