# Content Extraction Schema

The JSON structure produced when extracting an artifact for docx/pptx generation. Written to `/tmp/ea-gen-{artifact-id}.json`.

## Schema

```json
{
  "meta": {
    "artifact":         "Architecture Vision",
    "artifactId":       "architecture-vision",
    "phase":            "A",
    "status":           "Draft",
    "reviewStatus":     "Pending",
    "version":          "0.2",
    "lastModified":     "2026-03-28T10:00:00",
    "relatedArtifacts": ["architecture-principles", "requirements-register"],
    "diagrams":         ["diagrams/context-diagram.png"],
    "links":            [{"label": "Architecture Principles", "path": "../preliminary/architecture-principles.md"}],
    "taxonomy": {
      "domain": "Cross-cutting",
      "category": "Strategy",
      "audience": "Executive",
      "layer": "Motivation",
      "sensitivity": "Internal",
      "tags": ["vision", "strategy"]
    }
  },
  "sections": [
    {"heading": "Section Heading", "content": "Body text here", "level": 1},
    {"heading": "Subsection", "content": "Body text", "level": 2}
  ],
  "tables": [
    {
      "heading": "Table Title",
      "headers": ["Col 1", "Col 2", "Col 3"],
      "rows": [["val", "val", "val"], ["val", "val", "val"]]
    }
  ]
}
```

## Extraction Rules

- **YAML frontmatter** → `meta` block. Map: `artifact`, `artifactId`, `phase`, `status`, `reviewStatus`, `version`, `lastModified`, `taxonomy` (copy nested block as-is), `relatedArtifacts`, `diagrams`, `links`. Use `[]` for absent arrays.
- **Headings:** `## Heading` → `level: 1`, `### Heading` → `level: 2`
- **Skip** `<details>` guidance blocks — template guidance, not content
- **Tables** — extract each as an entry in `"tables"`, including its section heading
- **Placeholders** — `{{placeholder}}` or empty → use `""` (script renders as "[To be completed]")
- **Content format** — plain text only; no raw markdown syntax in `content` strings
- **Exception** — inline image syntax `![alt](absolute-path)` (already resolved to absolute path) should be retained so the generation script can embed the image

## Relative Image Resolution

Before extraction, scan the artifact body for `![alt](relative-path)`. For each:
1. Resolve the relative path against the artifact file's location to an absolute path
2. Replace with the absolute path in the extraction output

Example: artifact at `artifacts/phase-a/architecture-vision.md` with `![Context](../../diagrams/context.png)` → resolves to `EA-projects/{slug}/diagrams/context.png`
