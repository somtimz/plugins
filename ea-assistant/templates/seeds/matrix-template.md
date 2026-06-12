# Matrix Template Seed

Used by `/ea-matrix new` and the `/ea-interview` matrix offer. Substitute all `{{placeholders}}` before writing.

---

```markdown
---
id: {{key}}-matrix
name: {{name}}
matrixKey: {{key}}
phase: {{phase}}
status: Draft
version: 0.1.0
relatedArtifacts: []
diagrams: []
links: []
lastModified: {{YYYY-MM-DD}}
---

# {{name}}

## Overview

{{overview}}

## Matrix

| {{rowEntityLabel}} \ {{columnEntityLabel}} | {{column1}} | {{column2}} |
|---|---|---|
| {{row1}} |  |  |
| {{row2}} |  |  |

## Legend

{{legend}}

## Observations

*(none yet)*

## Open Questions

*(none yet)*
```

**Substitution notes:**
- `{{key}}`, `{{name}}`, `{{phase}}` — from the catalogue entry (`skills/ea-artifact-templates/references/matrix-catalogue.md`)
- `{{overview}}` — one or two sentences: the catalogue's "Why" line adapted to this engagement
- `{{rowEntityLabel}}` / `{{columnEntityLabel}}` — the axis names from the catalogue (e.g. "Data Entity \ Application")
- Row/column placeholders — replace with the confirmed seeded axes; add as many rows/columns as confirmed
- `{{legend}}` — copy the catalogue entry's **Markers** line verbatim as a bulleted list
