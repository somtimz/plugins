---
name: togaf-generation
description: This skill should be used when the user asks to "generate a Word document", "export to PowerPoint", "create a .docx", "produce slides", "make a presentation", "generate a Mermaid diagram", "export artifact as Word", "create TOGAF slides", "generate a PPTX", or any request to produce a formatted file output from TOGAF artifact content.
version: 0.1.0
---

# TOGAF Artifact Generation — Word, PowerPoint, and Mermaid

This skill governs how to produce formatted output files from TOGAF artifact content. Three formats are supported: Mermaid diagrams (inline text), Word documents (.docx), and PowerPoint slides (.pptx).

## Format Selection Guide

| Artifact | Mermaid | Word (.docx) | PowerPoint (.pptx) |
|----------|---------|-------------|-------------------|
| Architecture Vision | ✗ | ✓ primary | ✓ exec version |
| Stakeholder Map | ✓ quadrant | ✓ matrix table | ✓ slide |
| Business Capability Map | ✓ graph TD | ✓ table | ✓ slide |
| Process Flow | ✓ flowchart | ✓ embedded | ✓ slide |
| Application Portfolio | ✗ | ✓ table | ✓ table slide |
| Technology Landscape | ✓ C4 | ✓ embedded | ✓ slide |
| Gap Analysis | ✗ | ✓ table | ✓ table slide |
| Architecture Roadmap | ✓ gantt | ✓ embedded | ✓ roadmap slide |
| Requirements Register | ✗ | ✓ table | ✗ |

## Mermaid Diagram Generation

Render Mermaid diagrams inline as fenced code blocks. Always include a diagram title using `---` frontmatter or a `title` directive where supported.

**Standard diagram types used in TOGAF:**
- `graph TD` — hierarchical structures (capability maps, org charts)
- `flowchart LR` — process flows with swim lanes (use subgraph for lanes)
- `gantt` — roadmaps and timelines
- `C4Context` / `C4Container` — technology landscapes
- `quadrantChart` — stakeholder power/interest maps

To render, wrap in a fenced block:
````
```mermaid
graph TD
    ...
```
````

## Word Document Generation (.docx)

Use `scripts/generate-docx.py` to produce structured Word documents.

**Prerequisites**: `pip install python-docx` (or `pip3 install python-docx`)

### Standard TOGAF Document Structure

All Word documents follow this layout:
1. **Cover Page** — Title, Organisation, Date, Architect Name, Version
2. **Table of Contents** — Auto-generated
3. **Executive Summary** — 1–2 paragraphs
4. **[Content Sections]** — Phase/artifact specific
5. **Appendices** — Supporting detail, references

### Running the Script

```bash
python3 /path/to/togaf-adm/scripts/generate-docx.py \
  --type [artifact-type] \
  --title "[Document Title]" \
  --org "[Organisation Name]" \
  --architect "[Architect Name]" \
  --output "[output-filename.docx]" \
  --content "[JSON content string or @file.json]"
```

**Artifact type values**: `vision`, `gap-analysis`, `app-portfolio`, `requirements-register`, `roadmap`, `stakeholder-map`

### Content JSON Format

Pass content as a JSON object matching the artifact schema. See `references/docx-content-schemas.md` for the schema of each artifact type.

## PowerPoint Generation (.pptx)

Use `scripts/generate-pptx.py` to produce structured slide decks.

**Prerequisites**: `pip install python-pptx` (or `pip3 install python-pptx`)

### Standard TOGAF Deck Structure

| Slide | Title | Content |
|-------|-------|---------|
| 1 | Title Slide | Document title, org, date, architect |
| 2 | Executive Summary | 3–5 bullet points |
| 3 | Architecture Overview | High-level diagram or capability map |
| 4–N | Phase / Topic Detail | One topic per slide |
| N+1 | Gap Analysis | Table of key gaps |
| N+2 | Architecture Roadmap | Gantt-style timeline visual |
| Last | Appendix / Next Steps | Supporting detail |

### Running the Script

```bash
python3 /path/to/togaf-adm/scripts/generate-pptx.py \
  --type [deck-type] \
  --title "[Deck Title]" \
  --org "[Organisation Name]" \
  --architect "[Architect Name]" \
  --output "[output-filename.pptx]" \
  --content "[JSON content string or @file.json]"
```

**Deck type values**: `vision`, `phase-summary`, `gap-analysis`, `roadmap`, `stakeholder`

### Content JSON Format

See `references/pptx-content-schemas.md` for slide content schemas.

## Export Workflow

1. Generate or confirm artifact content in the current session
2. Run `/togaf:export [format]` — the `artifact-generator` agent will:
   a. Confirm which artifact to export
   b. Collect any missing fields
   c. Prepare the content JSON
   d. Run the appropriate generation script
   e. Confirm the output file path
3. Open the output file to review

## Styling Conventions

### Word Documents
- Heading 1: Section titles (14pt, bold, dark blue `#1F3864`)
- Heading 2: Subsections (12pt, bold, medium blue `#2E74B5`)
- Body: Calibri 11pt
- Tables: Header row dark blue background, white text; alternating row shading
- Cover page: Organisation name, document title, version, date, architect name

### PowerPoint Slides
- Title slide: Dark blue background (`#1F3864`), white text
- Content slides: White background, dark blue headings
- Accent colour: Orange `#C55A11` for highlights and callouts
- Font: Calibri throughout
- Bullet style: Simple dash, max 2 levels, max 6 bullets per slide

## Troubleshooting

**`python-docx` not found**: Run `pip3 install python-docx` or `python -m pip install python-docx`
**`python-pptx` not found**: Run `pip3 install python-pptx` or `python -m pip install python-pptx`
**Script not found**: Verify plugin root path; scripts are at `scripts/generate-docx.py` and `scripts/generate-pptx.py`

