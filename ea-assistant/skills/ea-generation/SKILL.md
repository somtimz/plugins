---
name: ea-generation
description: This skill should be used when the user asks to "generate a Word document", "export an artifact as PowerPoint", "create a .docx", "produce slides", "make a Mermaid diagram", "export artifact", "create a presentation", or any request to produce a formatted file output from an EA artifact.
version: 0.2.0
---

# EA Artifact Generation — Word, PowerPoint, and Mermaid

This skill governs how to produce formatted output files from individual EA artifacts within an engagement. Three formats are supported: Mermaid diagrams (embedded in Markdown or rendered as images), Word documents (.docx), and PowerPoint presentations (.pptx). For consolidated reports merging all artifacts across an engagement, use `/ea-publish` instead.

## Format Selection Guide

| Artifact | Mermaid | Word (.docx) | PowerPoint (.pptx) |
|---|---|---|---|
| Architecture Vision | — | ✓ primary | ✓ exec version |
| Statement of Architecture Work | — | ✓ primary | — |
| Architecture Principles | — | ✓ primary | ✓ summary slide |
| Stakeholder Map | ✓ quadrantChart | ✓ matrix table | ✓ slide |
| Business Architecture | — | ✓ primary | ✓ summary |
| Data Architecture | — | ✓ primary | ✓ summary |
| Application Architecture | — | ✓ primary | ✓ summary |
| Technology Architecture | — | ✓ primary | ✓ summary |
| Gap Analysis | — | ✓ table | ✓ table slide |
| Architecture Roadmap | ✓ gantt | ✓ embedded | ✓ roadmap slide |
| Migration Plan | ✓ gantt | ✓ primary | ✓ summary |
| Architecture Contract | — | ✓ primary | — |
| Compliance Assessment | — | ✓ primary | — |
| Change Request | — | ✓ primary | — |
| Requirements Register | — | ✓ table | — |
| Traceability Matrix | — | ✓ table | — |

## Mermaid Diagram Patterns

### 1. Capability Map

```mermaid
graph TD
    L1_Customer["Customer Management"]
    L1_Ops["Operations"]
    L1_Finance["Finance"]

    L1_Customer --> L2_CRM["CRM"]
    L1_Customer --> L2_Support["Customer Support"]
    L2_CRM --> L3_Lead["Lead Management"]
    L2_CRM --> L3_Account["Account Management"]

    L1_Ops --> L2_Supply["Supply Chain"]
    L1_Ops --> L2_Fulfil["Order Fulfilment"]
    L2_Supply --> L3_Proc["Procurement"]
    L2_Supply --> L3_Inv["Inventory"]

    L1_Finance --> L2_AR["Accounts Receivable"]
    L1_Finance --> L2_AP["Accounts Payable"]
    L2_AR --> L3_Invoice["Invoicing"]
    L2_AP --> L3_Payment["Payment Processing"]
```

### 2. Process Flow

```mermaid
flowchart LR
    subgraph Customer
        C1([Submit Order]) --> C2([Receive Confirmation])
        C2 --> C3([Track Shipment])
    end
    subgraph Operations
        O1([Validate Order]) --> O2([Pick & Pack])
        O2 --> O3([Dispatch])
    end
    subgraph Finance
        F1([Raise Invoice]) --> F2([Collect Payment])
        F2 --> F3([Reconcile])
    end

    C1 --> O1
    O3 --> C3
    O1 --> F1
    F2 --> C2
```

### 3. Stakeholder Map

```mermaid
quadrantChart
    title Stakeholder Power / Interest
    x-axis Low Interest --> High Interest
    y-axis Low Power --> High Power
    quadrant-1 Manage Closely
    quadrant-2 Keep Satisfied
    quadrant-3 Monitor
    quadrant-4 Keep Informed
    CIO: [0.85, 0.90]
    CFO: [0.60, 0.80]
    Business Sponsor: [0.90, 0.75]
    IT Ops Team: [0.70, 0.40]
    End Users: [0.80, 0.20]
    Regulator: [0.30, 0.85]
    Vendor: [0.50, 0.35]
```

### 4. Technology Landscape

```mermaid
C4Context
    title Technology Landscape — Current State
    Person(user, "Business User", "Internal staff accessing applications")
    System(crm, "CRM Platform", "Salesforce — customer relationship management")
    System(erp, "ERP System", "SAP S/4HANA — finance and operations")
    System_Ext(ext_pay, "Payment Gateway", "External payment processing service")
    System_Ext(ext_id, "Identity Provider", "Azure AD B2C — SSO")

    Rel(user, crm, "Uses")
    Rel(user, erp, "Uses")
    Rel(crm, ext_pay, "Processes payments via")
    Rel(crm, ext_id, "Authenticates via")
    Rel(erp, ext_id, "Authenticates via")
```

### 5. Architecture Roadmap

```mermaid
gantt
    title Architecture Roadmap
    dateFormat  YYYY-MM
    axisFormat  %b %Y

    section Current State
    Legacy CRM Decommission Plan  :done,    cs1, 2025-01, 2025-03
    Network Audit                 :done,    cs2, 2025-02, 2025-04

    section Transition
    CRM Migration                 :active,  t1, 2025-04, 2025-09
    Data Lake Setup               :         t2, 2025-06, 2025-11
    IAM Consolidation             :         t3, 2025-07, 2025-10

    section Target State
    Cloud-Native Operations       :         ts1, 2025-10, 2026-03
    AI-Enabled Analytics          :         ts2, 2025-12, 2026-06
```

### 6. Data Flow

```mermaid
flowchart TD
    SRC1[(CRM Database)] -->|Extract| STAGE[Staging Area]
    SRC2[(ERP Database)] -->|Extract| STAGE
    SRC3[Flat File Exports] -->|Extract| STAGE

    STAGE -->|Transform| DQ[Data Quality Layer]
    DQ -->|Cleanse & Enrich| DWH[(Data Warehouse)]

    DWH -->|Load| MART1[(Sales Data Mart)]
    DWH -->|Load| MART2[(Finance Data Mart)]
    DWH -->|Stream| RT[Real-Time Dashboard]

    MART1 -->|Serve| BI[BI Reporting Tool]
    MART2 -->|Serve| BI
```

## Word Document Generation (.docx)

### Prerequisites

**No manual setup required.** When `/ea-generate` runs for the first time it:

1. Creates `~/.ea-assistant-venv` if it does not exist
2. Installs `python-docx` and `python-pptx` into that venv
3. Uses the venv Python for all subsequent runs

This avoids WSL2 / externally-managed-environment errors without touching system Python.

### Standard Document Structure

Generated Word documents follow this standard structure:

1. Cover Page — engagement name, artifact title, version, date, classification
2. Table of Contents — auto-generated from heading styles
3. Executive Summary — 1–2 page overview of key findings and recommendations
4. Content Sections — artifact-specific structured content
5. Appendices — supporting data, glossary, reference architecture diagrams

### Running the Script

With engagement directory (recommended):

```bash
SCRIPT=$(find "$HOME/.claude" -name "generate-docx.py" -path "*/ea-assistant/scripts/*" | head -1)
VENV="$HOME/.ea-assistant-venv"
[ ! -f "$VENV/bin/python" ] && python3 -m venv "$VENV" && "$VENV/bin/pip" install --quiet python-docx python-pptx
"$VENV/bin/python" "$SCRIPT" \
  --engagement-dir ./EA-projects/my-engagement \
  --type vision \
  --content @/tmp/ea-gen-{artifact-id}.json \
  --output ./output/architecture-vision.docx
```

Standalone (content JSON supplied directly):

```bash
SCRIPT=$(find "$HOME/.claude" -name "generate-docx.py" -path "*/ea-assistant/scripts/*" | head -1)
"$HOME/.ea-assistant-venv/bin/python" "$SCRIPT" \
  --type gap-analysis \
  --content @/tmp/ea-gen-gap.json \
  --output ./output/gap-analysis.docx
```

**Artifact type values:** `vision`, `gap-analysis`, `app-portfolio`, `requirements-register`, `roadmap`, `stakeholder-map`

### Content JSON Format

```json
{
  "title": "Architecture Vision",
  "version": "1.0",
  "engagement": "Digital Transformation Programme",
  "classification": "CONFIDENTIAL",
  "executive_summary": "Single paragraph summarising the vision.",
  "sections": [
    {
      "heading": "Strategic Context",
      "level": 1,
      "body": "Paragraph text describing strategic context."
    },
    {
      "heading": "Architecture Drivers",
      "level": 2,
      "body": "Paragraph text describing key drivers."
    }
  ],
  "tables": [
    {
      "title": "Key Stakeholders",
      "headers": ["Stakeholder", "Role", "Interest"],
      "rows": [
        ["CIO", "Executive Sponsor", "Strategic alignment"],
        ["IT Architect", "Solution Owner", "Technical delivery"]
      ]
    }
  ]
}
```

## PowerPoint Generation (.pptx)

### Prerequisites

```bash
pip install python-pptx
```

### Standard Deck Structure

| Slide | Content |
|---|---|
| 1 | Title slide — engagement name, presentation title, date |
| 2 | Agenda — list of sections covered in the deck |
| 3–N | Content slides — one topic per slide, max 7 bullets |
| N+1 | Summary / Key Recommendations |
| N+2 | Next Steps and Owner table |
| Last | Appendix divider + supporting detail slides |

### Running the Script

With engagement directory:

```bash
SCRIPT=$(find "$HOME/.claude" -name "generate-pptx.py" -path "*/ea-assistant/scripts/*" | head -1)
"$HOME/.ea-assistant-venv/bin/python" "$SCRIPT" \
  --engagement-dir ./EA-projects/my-engagement \
  --type vision \
  --content @/tmp/ea-gen-{artifact-id}.json \
  --output ./output/architecture-vision.pptx
```

**Deck type values:** `vision`, `phase-summary`, `gap-analysis`, `roadmap`, `stakeholder`

### Content JSON Format

```json
{
  "title": "Architecture Vision",
  "subtitle": "Digital Transformation Programme",
  "date": "2026-03-20",
  "slides": [
    {
      "layout": "title",
      "title": "Architecture Vision",
      "subtitle": "Digital Transformation Programme — March 2026"
    },
    {
      "layout": "content",
      "title": "Strategic Objectives",
      "bullets": [
        "Modernise core banking platform by Q4 2026",
        "Consolidate data estates onto unified cloud data platform",
        "Reduce time-to-market for new products by 40%"
      ]
    },
    {
      "layout": "table",
      "title": "Capability Gap Summary",
      "headers": ["Capability", "Current", "Target", "Gap"],
      "rows": [
        ["Data Analytics", "Level 2", "Level 4", "High"],
        ["Cloud Adoption", "Level 1", "Level 3", "High"],
        ["API Management", "Level 3", "Level 4", "Medium"]
      ]
    }
  ]
}
```

## Styling Conventions

### Word Documents

- **Heading 1:** 14pt bold, dark blue `#1F3864`
- **Heading 2:** 12pt bold, medium blue `#2E74B5`
- **Body text:** Calibri 11pt, black `#000000`
- **Tables:** Header row dark blue background `#1F3864` with white text; alternating row shading `#D6E4F0`

### PowerPoint Slides

- **Title slide:** Dark blue background `#1F3864`, white text
- **Content slides:** White background `#FFFFFF`, dark blue headings `#1F3864`
- **Accent colour:** Orange `#C55A11` for highlights, callouts, and icons
- **Font:** Calibri throughout
- **Max 7 bullets per slide** — split into multiple slides if content exceeds this limit

## Troubleshooting

- **WSL2 / externally-managed-environment error:** Use a venv — `python3 -m venv ~/.ea-assistant-venv && ~/.ea-assistant-venv/bin/pip install python-docx python-pptx`. The generation commands detect and use it automatically.
- **python-docx not found:** Run `~/.ea-assistant-venv/bin/pip install python-docx` (venv) or `pip3 install python-docx` (system).
- **python-pptx not found:** Run `~/.ea-assistant-venv/bin/pip install python-pptx` (venv) or `pip3 install python-pptx` (system).
- **Script not found:** Verify the plugin root path is set correctly. Check that `${CLAUDE_PLUGIN_ROOT}` resolves to the plugin installation directory and that the `scripts/` subdirectory exists.
