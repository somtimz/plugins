#!/usr/bin/env python3
"""
EA Assistant — Word Document Generator
Produces EA-structured .docx files from artifact content JSON.

Usage:
    python3 generate-docx.py --type vision --title "Architecture Vision" \
        --org "Acme Corp" --architect "Jane Smith" \
        --output "architecture-vision.docx" --content '{"sections": [...]}'

    python3 generate-docx.py --type vision --engagement-dir EA-projects/acme-2024 \
        --output "architecture-vision.docx"

Requirements: pip3 install python-docx
"""

import argparse
import json
import os
import sys
from datetime import date

try:
    from docx import Document
    from docx.shared import Pt, RGBColor, Inches, Cm
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
except ImportError:
    print("ERROR: python-docx not installed. Run: pip3 install python-docx")
    sys.exit(1)

DARK_BLUE = RGBColor(0x1F, 0x38, 0x64)
MED_BLUE  = RGBColor(0x2E, 0x74, 0xB5)
ORANGE    = RGBColor(0xC5, 0x5A, 0x11)
WHITE     = RGBColor(0xFF, 0xFF, 0xFF)

ARTIFACT_SECTIONS = {
    "vision": [
        "Executive Summary",
        "Business Context and Drivers",
        "Architecture Scope",
        "Stakeholder Summary",
        "Baseline Architecture Overview",
        "Target Architecture Overview",
        "Gap Summary",
        "Key Risks and Assumptions",
        "Approval and Sign-off",
    ],
    "gap-analysis": [
        "Introduction",
        "Scope",
        "Baseline Architecture Summary",
        "Target Architecture Summary",
        "Gap Analysis",
        "Recommendations",
    ],
    "app-portfolio": [
        "Introduction",
        "Application Inventory",
        "Lifecycle Summary",
        "Recommendations",
    ],
    "requirements-register": [
        "Introduction",
        "Requirements Summary",
        "Requirements Register",
        "Traceability Matrix",
    ],
    "roadmap": [
        "Introduction",
        "Migration Strategy",
        "Transition Architectures",
        "Implementation Roadmap",
        "Dependencies and Risks",
    ],
    "stakeholder-map": [
        "Introduction",
        "Stakeholder Register",
        "Power/Interest Analysis",
        "Engagement Plan",
    ],
}


def set_cell_background(cell, hex_color):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)


def add_cover_page(doc, title, org, architect, doc_type="Architecture Document"):
    section = doc.sections[0]
    section.page_width  = Inches(8.5)
    section.page_height = Inches(11)

    doc.add_paragraph()
    doc.add_paragraph()
    doc.add_paragraph()

    # Organisation
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(org)
    run.font.size = Pt(14)
    run.font.color.rgb = DARK_BLUE
    run.font.bold = True

    doc.add_paragraph()

    # Title
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.font.size = Pt(24)
    run.font.color.rgb = DARK_BLUE
    run.font.bold = True

    # Subtitle
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(doc_type)
    run.font.size = Pt(14)
    run.font.color.rgb = MED_BLUE

    doc.add_paragraph()
    doc.add_paragraph()

    # Metadata table
    table = doc.add_table(rows=4, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'

    meta = [
        ("Prepared by", architect),
        ("Organisation", org),
        ("Date", date.today().strftime("%B %Y")),
        ("Version", "0.1 Draft"),
    ]
    for i, (label, value) in enumerate(meta):
        row = table.rows[i]
        row.cells[0].text = label
        row.cells[0].paragraphs[0].runs[0].font.bold = True
        row.cells[1].text = value

    doc.add_page_break()


def add_toc_placeholder(doc):
    h = doc.add_heading("Table of Contents", level=1)
    h.runs[0].font.color.rgb = DARK_BLUE
    p = doc.add_paragraph("[Update table of contents after opening in Word: References → Update Table]")
    p.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    p.runs[0].font.italic = True
    doc.add_page_break()


def add_section(doc, heading, content="", level=1):
    h = doc.add_heading(heading, level=level)
    color = DARK_BLUE if level == 1 else MED_BLUE
    for run in h.runs:
        run.font.color.rgb = color
    if content:
        doc.add_paragraph(content)
    else:
        p = doc.add_paragraph("[To be completed]")
        p.runs[0].font.color.rgb = RGBColor(0x80, 0x80, 0x80)
        p.runs[0].font.italic = True


def add_table(doc, headers, rows):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Table Grid'

    # Header row
    hdr_cells = table.rows[0].cells
    for i, h in enumerate(headers):
        hdr_cells[i].text = h
        hdr_cells[i].paragraphs[0].runs[0].font.bold = True
        hdr_cells[i].paragraphs[0].runs[0].font.color.rgb = WHITE
        set_cell_background(hdr_cells[i], "1F3864")

    # Data rows
    for ri, row_data in enumerate(rows):
        row_cells = table.rows[ri + 1].cells
        for ci, cell_text in enumerate(row_data):
            row_cells[ci].text = str(cell_text)
        if ri % 2 == 0:
            for cell in row_cells:
                set_cell_background(cell, "D6E4F0")

    doc.add_paragraph()


def build_document(args, content):
    doc = Document()

    # Set default font
    style = doc.styles['Normal']
    style.font.name = 'Calibri'
    style.font.size = Pt(11)

    add_cover_page(doc, args.title, args.org, args.architect)
    add_toc_placeholder(doc)

    # Sections from content or defaults
    artifact_type = args.type
    sections = content.get("sections", [])

    if sections:
        for sec in sections:
            heading = sec.get("heading", "Section")
            body    = sec.get("content", "")
            level   = sec.get("level", 1)
            add_section(doc, heading, body, level)

            # Embedded table
            if "table" in sec:
                t = sec["table"]
                add_table(doc, t.get("headers", []), t.get("rows", []))
    else:
        # Use default sections for artifact type
        default_sections = ARTIFACT_SECTIONS.get(artifact_type, ["Content"])
        for sec_name in default_sections:
            add_section(doc, sec_name)

    # Standalone tables
    for tbl in content.get("tables", []):
        heading = tbl.get("heading", "")
        if heading:
            add_section(doc, heading, level=2)
        add_table(doc, tbl.get("headers", []), tbl.get("rows", []))

    doc.save(args.output)
    print(f"✅ Word document saved: {args.output}")


def main():
    parser = argparse.ArgumentParser(description="Generate EA Assistant Word document")
    parser.add_argument("--type",           required=True,  help="Artifact type (vision, gap-analysis, etc.)")
    parser.add_argument("--title",          default=None,   help="Document title")
    parser.add_argument("--org",            default=None,   help="Organisation name")
    parser.add_argument("--architect",      default=None,   help="Lead architect name")
    parser.add_argument("--output",         required=True,  help="Output filename (.docx)")
    parser.add_argument("--content",        default="{}",   help="JSON content string or @file.json")
    parser.add_argument("--engagement-dir", default=None,   help="Path to engagement directory containing engagement.json")
    args = parser.parse_args()

    # Load engagement metadata if provided
    if args.engagement_dir:
        engagement_path = os.path.join(args.engagement_dir, "engagement.json")
        if os.path.exists(engagement_path):
            with open(engagement_path) as f:
                engagement = json.load(f)
            if not args.title:
                args.title = engagement.get("name", "Architecture Document")
            if not args.org:
                args.org = engagement.get("organisation", "Organisation")
            if not args.architect:
                args.architect = engagement.get("sponsor", "Architect")
        else:
            print(f"WARNING: engagement.json not found at {engagement_path}, using explicit arguments")

    # Validate required fields
    if not args.title:
        print("ERROR: --title is required when --engagement-dir is not provided")
        sys.exit(1)
    if not args.org:
        args.org = "Organisation"
    if not args.architect:
        args.architect = "Architect"

    # Load content
    content_str = args.content
    if content_str.startswith("@"):
        with open(content_str[1:]) as f:
            content_str = f.read()
    try:
        content = json.loads(content_str)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON content — {e}")
        sys.exit(1)

    build_document(args, content)


if __name__ == "__main__":
    main()
