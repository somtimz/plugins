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

### Step 3: Read and Extract Artifact Content

1. Read the artifact file from `EA-projects/{slug}/artifacts/{artifact-id}.md`.
2. Read the engagement metadata from `EA-projects/{slug}/engagement.json`.
3. Parse the artifact into a content JSON object with this structure:

```json
{
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

Rules for extraction:
- Map each `## Heading` → `level: 1`, `### Heading` → `level: 2`
- Skip `<details>` guidance blocks — they are template guidance, not content
- Skip YAML frontmatter
- For each markdown table, extract it as an entry in `"tables"` — include the section heading it belongs to
- Where a field is `{{placeholder}}` or empty, use `""` as the content value (the script will render it as "[To be completed]")
- Collapse the content to plain text — do not include raw markdown syntax in content strings

4. Write the extracted JSON to a temp file: `/tmp/ea-gen-{artifact-id}.json`

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

Locate the script, bootstrap the venv, then run:

```bash
# Locate the script in the plugin install
SCRIPT=$(find "$HOME/.claude" -name "generate-docx.py" -path "*/ea-assistant/scripts/*" 2>/dev/null | head -1)
if [ -z "$SCRIPT" ]; then
  echo "ERROR: generate-docx.py not found. Is the ea-assistant plugin installed?"
  exit 1
fi

# Bootstrap venv
VENV="$HOME/.ea-assistant-venv"
if [ ! -f "$VENV/bin/python" ]; then
  echo "Setting up EA Assistant Python environment..."
  python3 -m venv "$VENV"
fi
if ! "$VENV/bin/python" -c "import docx" 2>/dev/null; then
  echo "Installing python-docx and python-pptx..."
  "$VENV/bin/pip" install --quiet python-docx python-pptx
fi

"$VENV/bin/python" "$SCRIPT" \
  --type {script-type} \
  --engagement-dir EA-projects/{slug} \
  --content @/tmp/ea-gen-{artifact-id}.json \
  --output EA-projects/{slug}/artifacts/{artifact-id}.docx
```

**For pptx:**

Run the same bootstrap block, then:

```bash
SCRIPT=$(find "$HOME/.claude" -name "generate-pptx.py" -path "*/ea-assistant/scripts/*" 2>/dev/null | head -1)
if [ -z "$SCRIPT" ]; then
  echo "ERROR: generate-pptx.py not found. Is the ea-assistant plugin installed?"
  exit 1
fi

"$VENV/bin/python" "$SCRIPT" \
  --type {script-type} \
  --engagement-dir EA-projects/{slug} \
  --content @/tmp/ea-gen-{artifact-id}.json \
  --output EA-projects/{slug}/artifacts/{artifact-id}.pptx
```

If the script exits with a non-zero status, display the error output and stop. Do not update the engagement.

> **Windows (PowerShell / WSL):** The bootstrap uses `$HOME` and `bin/python`. On native Windows PowerShell replace `$HOME` with `$env:USERPROFILE`, `bin/python` with `Scripts\python.exe`, and `bin/pip` with `Scripts\pip.exe`. On WSL2, the Unix paths work as-is.

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

`{script-type}` is the value passed to `--type` in the script. It must match the keys the script recognises.

| Artifact Name            | `{script-type}` | Primary Format | Mermaid Available |
|--------------------------|-----------------|----------------|-------------------|
| Architecture Vision      | `vision`        | docx           | No                |
| Stakeholder Map          | `stakeholder-map` | mermaid       | Yes               |
| Business Architecture    | `business`      | docx           | No                |
| Gap Analysis             | `gap-analysis`  | docx           | No                |
| Architecture Roadmap     | `roadmap`       | mermaid        | Yes               |
| Requirements Register    | `requirements-register` | docx   | No                |
| Capability Map           | `capability-map` | mermaid       | Yes               |
| Application Portfolio    | `app-portfolio` | docx           | No                |
| Data Architecture        | `data`          | docx           | No                |
| Migration Plan           | `roadmap`       | pptx           | No                |
| Risk Register            | `risk-register` | docx           | No                |
| Implementation Roadmap   | `roadmap`       | pptx           | No                |
