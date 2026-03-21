# ITIL Change Request — Word Document Template

## Document Structure

Produce the document in this order:

1. **Cover block** (header table with RFC number, status, dates)
2. **Section 1** — Change Overview
3. **Section 2** — Implementation Steps
4. **Section 3** — Change Window & Schedule
5. **Section 4** — Risk & Impact Assessment
6. **Section 5** — Rollback Plan
7. **Section 6** — Testing & Validation
8. **Section 7** — Approvals
9. **Preparer's Notes** (always last)

---

## Styling

- Page size: US Letter (12240 x 15840 DXA), 1-inch margins
- Font: Arial throughout
- Body text: 11pt
- Heading 1: 16pt bold, dark blue (#1F3864)
- Heading 2: 13pt bold, medium blue (#2E75B6)
- Cover block background: light blue (#D5E8F0) via ShadingType.CLEAR
- Table borders: SINGLE, size 1, color #CCCCCC
- Always use WidthType.DXA (never PERCENTAGE)

---

## Cover Block (top of document)

Two-column table, full width (9360 DXA), columns: 4680 / 4680.

| Left | Right |
|---|---|
| **Change Request** (16pt bold) | RFC Number (right-aligned) |
| Change Title | Status: PENDING CAB APPROVAL |
| | Date Submitted |
| | Priority |

---

## Section Layouts

### Section 1 — Change Overview

Two-column info table (label / value):

| Field | Value |
|---|---|
| Change Title | |
| Change Type | |
| Priority | |
| Requested By | |
| Change Owner | |
| Affected Systems | |
| Business Justification | (full paragraph, may span full width) |

### Section 2 — Implementation Steps

Numbered list using `LevelFormat.DECIMAL`. Each step on its own line. If sub-steps exist, use a second level with indent.

### Section 3 — Change Window & Schedule

Two-column table:

| Field | Value |
|---|---|
| Proposed Start | |
| Estimated Duration | |
| Maintenance Window | |

### Section 4 — Risk & Impact Assessment

Two-column table:

| Field | Value |
|---|---|
| Risk Level | [color-coded: Low=green, Medium=amber, High=red text] |
| Impact if Change Fails | |
| Affected Users/Services | |
| Dependencies | |

For risk level color coding, use TextRun color:
- Low: `00B050` (green)
- Medium: `FF9900` (amber)  
- High: `FF0000` (red)

### Section 5 — Rollback Plan

Numbered list, same style as Implementation Steps. If only one step exists, still use numbered list for consistency.

### Section 6 — Testing & Validation

Bullet list using `LevelFormat.BULLET`. Each validation criterion on its own line.

### Section 7 — Approvals

Table with 4 columns: Name | Role | Decision | Date/Signature

Column widths: 2500 / 2000 / 2360 / 2500 (sum = 9360 DXA)

Leave Decision and Date/Signature cells blank for CAB to fill in.
Add one row per approver named by the user, plus a "CAB Chair" row at the bottom.

---

## Footer

Left: "CONFIDENTIAL — For CAB Use Only"  
Right: Page number

Use tab stops on a footer paragraph (not a table).

---

## Complete Node.js Script Pattern

```javascript
const {
  Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell,
  Header, Footer, AlignmentType, HeadingLevel, BorderStyle, WidthType,
  ShadingType, VerticalAlign, PageNumber, LevelFormat, TabStopType, TabStopPosition
} = require('docx');
const fs = require('fs');

// Build all content arrays first, then pass to Document constructor
const doc = new Document({
  numbering: {
    config: [
      {
        reference: "impl-steps",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }]
      },
      {
        reference: "rollback-steps",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }]
      },
      {
        reference: "validation-bullets",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }]
      }
    ]
  },
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, color: "1F3864", font: "Arial" },
        paragraph: { spacing: { before: 240, after: 120 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, color: "2E75B6", font: "Arial" },
        paragraph: { spacing: { before: 180, after: 60 }, outlineLevel: 1 } }
    ]
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 }
      }
    },
    headers: { default: new Header({ children: [] }) },
    footers: {
      default: new Footer({
        children: [
          new Paragraph({
            tabStops: [
              { type: TabStopType.RIGHT, position: 9360 }
            ],
            children: [
              new TextRun({ text: "CONFIDENTIAL — For CAB Use Only", size: 18, color: "666666" }),
              new TextRun({ text: "\t", size: 18 }),
              new TextRun({ text: "Page ", size: 18, color: "666666" }),
              new PageNumber()
            ]
          })
        ]
      })
    },
    children: [
      // ... all document content
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync('/mnt/user-data/outputs/change-request.docx', buffer);
  console.log('Done');
});
```
