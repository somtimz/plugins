---
name: ea-generate
description: Generate a formatted file (Word, PowerPoint, or Mermaid) from an EA artifact
argument-hint: "[artifact-name] [docx|pptx|mermaid]"
allowed-tools: [Read, Write, Bash]
---

Export a single EA artifact as a formatted file.

## Instructions

If no engagement is active in context, display:

```
No engagement is currently open.

Run /ea-open to open an existing engagement first.
```

Then stop.

### Step 1: Select Artifact

If no artifact name was provided as an argument, list all artifacts in the active engagement with format recommendations. Read `EA-projects/{slug}/engagement.json` to get the artifacts array. Display:

```
Select artifact to generate:
1. Architecture Vision           [docx recommended, pptx available]
2. Stakeholder Map               [mermaid recommended, docx/pptx available]
3. Business Architecture         [docx recommended, pptx available]
4. Gap Analysis                  [docx recommended, pptx available]
5. Architecture Roadmap          [mermaid recommended, docx/pptx available]
6. Requirements Register         [docx recommended]
```

Show only artifacts that exist in the engagement (have a corresponding `.md` file in `EA-projects/{slug}/artifacts/`). Include the artifact status in brackets beside the name, e.g. `[Draft]` or `[Approved]`.

Prompt the user to select an artifact by number or name.

### Step 2: Select Format

If no format was provided as an argument, recommend the primary format for the selected artifact type (see Artifact Type Mapping below) and ask the user to confirm or choose another.

Example prompt:

```
Recommended format for Architecture Vision: docx (Word)

Generate as:
1. docx  — Word document (recommended)
2. pptx  — PowerPoint presentation
3. mermaid — inline diagram (not available for this artifact type)

Select format [1]:
```

For artifact types where mermaid is not applicable, omit that option.

### Step 3: Read Artifact Content

1. Read the artifact file from `EA-projects/{slug}/artifacts/{artifact-id}.md`.
2. Read the engagement metadata from `EA-projects/{slug}/engagement.json`.
3. Parse the artifact content into structured sections (headings, tables, lists, body text).

### Step 4: Generate Output

**For Mermaid:**

- Determine the correct Mermaid diagram type from the artifact content and type:
  - Stakeholder Map → `graph TD` or `graph LR`
  - Architecture Roadmap → `gantt`
  - Capability Map → `graph TD`
  - Other → `graph TD` as fallback
- Build the diagram from the artifact content.
- Render it as a fenced mermaid code block inline in the conversation. No file is created.

Example output:

````
```mermaid
graph TD
    ...
```
````

**For docx:**

- Build a content JSON object from the artifact content and engagement metadata.
- Determine the output path: `EA-projects/{slug}/artifacts/{artifact-id}.docx`
- Run the generation script:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docx.py \
  --type {artifact-type} \
  --input EA-projects/{slug}/artifacts/{artifact-id}.md \
  --output EA-projects/{slug}/artifacts/{artifact-id}.docx \
  --engagement EA-projects/{slug}/engagement.json
```

**For pptx:**

- Build a content JSON object from the artifact content and engagement metadata.
- Determine the output path: `EA-projects/{slug}/artifacts/{artifact-id}.pptx`
- Run the generation script:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-pptx.py \
  --type {artifact-type} \
  --input EA-projects/{slug}/artifacts/{artifact-id}.md \
  --output EA-projects/{slug}/artifacts/{artifact-id}.pptx \
  --engagement EA-projects/{slug}/engagement.json
```

If the script exits with a non-zero status, display the error output and stop. Do not update the engagement.

### Step 5: Update Engagement

After successful generation (docx or pptx only), update the artifact entry in `EA-projects/{slug}/engagement.json`:

- Set `lastModified` on the artifact entry to the current ISO 8601 timestamp.
- Write the updated `engagement.json` back to disk.

### Step 6: Confirm

For docx or pptx, report:

```
Generated: EA-projects/{slug}/artifacts/{artifact-id}.{ext}
Size: {file-size}

Options:
1. Generate in another format
2. Return to engagement (/ea-status)
```

For mermaid, the diagram is already shown inline. Offer:

```
Options:
1. Generate as docx instead
2. Generate as pptx instead
3. Return to engagement (/ea-status)
```

---

### Artifact Type Mapping

| Artifact Name            | `--type` value (docx/pptx) | Primary Format | Mermaid Available |
|--------------------------|----------------------------|----------------|-------------------|
| Architecture Vision      | `architecture-vision`      | docx           | No                |
| Stakeholder Map          | `stakeholder-map`          | mermaid        | Yes               |
| Business Architecture    | `business-architecture`    | docx           | No                |
| Gap Analysis             | `gap-analysis`             | docx           | No                |
| Architecture Roadmap     | `architecture-roadmap`     | mermaid        | Yes               |
| Requirements Register    | `requirements-register`    | docx           | No                |
| Capability Map           | `capability-map`           | mermaid        | Yes               |
| Application Portfolio    | `application-portfolio`    | docx           | No                |
| Data Architecture        | `data-architecture`        | docx           | No                |
| Migration Plan           | `migration-plan`           | pptx           | No                |
| Risk Register            | `risk-register`            | docx           | No                |
| Implementation Roadmap   | `implementation-roadmap`   | pptx           | No                |
