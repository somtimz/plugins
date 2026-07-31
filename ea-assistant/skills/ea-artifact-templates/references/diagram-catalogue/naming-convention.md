# Naming Convention


`{artifact-id}-{diagram-type}.{ext}`

| Ext | Format | When to Use |
|---|---|---|
| `.mmd` | Mermaid source | Primary authoring format; commit to `diagrams/` |
| `.png` / `.svg` | Rendered output | Embedded in exports via `/ea-generate`; regenerated from `.mmd` |
| `.drawio` | Draw.io XML | Complex free-form diagrams or when stakeholders edit in Draw.io |

---
