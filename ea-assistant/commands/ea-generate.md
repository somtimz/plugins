---
name: ea-generate
description: Generate a formatted file (Word, PowerPoint, Mermaid diagram, or rendered image) from an EA artifact or .mmd file
argument-hint: "[artifact-name] [docx|pptx|mermaid|png|svg] [--theme <theme>] [--bg <color>]"
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
1. docx    — Word document (recommended)
2. pptx    — PowerPoint presentation
3. mermaid — inline diagram (not available for this artifact type)
4. png     — rendered image via mermaid-cli (Mermaid artifacts only)
5. svg     — scalable vector image via mermaid-cli (Mermaid artifacts only)

Select format [1]:
```

For artifact types where mermaid is not applicable, omit options 3, 4, and 5.

**Rendering existing `.mmd` files directly:**
If the user runs `/ea-generate` with a `.mmd` file path or with `png`/`svg` as the format and no artifact name, skip Steps 1–3 and go directly to the **Render to Image** section of Step 4.

### Step 3: Read and Extract Artifact Content

1. Read the artifact file from `EA-projects/{slug}/artifacts/{artifact-id}.md`.
2. Read the engagement metadata from `EA-projects/{slug}/engagement.json`.
3. Parse the artifact into a content JSON object with this structure:

```json
{
  "meta": {
    "artifact":      "Architecture Vision",
    "artifactId":    "architecture-vision",
    "phase":         "A",
    "status":        "Draft",
    "reviewStatus":  "Pending",
    "version":       "0.2",
    "lastModified":  "2026-03-28T10:00:00"
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

Rules for extraction:
- **Extract YAML frontmatter** into the `meta` block. Map these fields:
  - `artifact` → `meta.artifact` (e.g. `"Architecture Vision"`)
  - `artifactId` → `meta.artifactId` (e.g. `"architecture-vision"`)
  - `phase` → `meta.phase` (ADM phase letter, e.g. `"A"`)
  - `status` → `meta.status` (e.g. `"Draft"`, `"Approved"`)
  - `reviewStatus` → `meta.reviewStatus` (e.g. `"Pending"`, `"Revised"`)
  - `version` → `meta.version` (string, e.g. `"0.2"`)
  - `lastModified` → `meta.lastModified` (ISO 8601 string)
  - `taxonomy` → `meta.taxonomy` (object — copy the full nested taxonomy block as-is: `{domain, category, audience, layer, sensitivity, tags}`)
  - Omit any field that is absent from the frontmatter.
- Map each `## Heading` → `level: 1`, `### Heading` → `level: 2`
- Skip `<details>` guidance blocks — they are template guidance, not content
- For each markdown table, extract it as an entry in `"tables"` — include the section heading it belongs to
- Where a field is `{{placeholder}}` or empty, use `""` as the content value (the script will render it as "[To be completed]")
- Collapse the content to plain text — do not include raw markdown syntax in content strings

4. Write the extracted JSON to a temp file: `/tmp/ea-gen-{artifact-id}.json`

### Step 4: Generate Output

**For Mermaid (inline source):**

- Determine the correct Mermaid diagram type from the artifact content and type:
  - Stakeholder Map → `graph TD` or `graph LR`
  - Architecture Roadmap → `gantt`
  - Capability Map → `graph TD`
  - Other → `graph TD` as fallback
- Build the diagram from the artifact content.
- Save the source to `EA-projects/{slug}/diagrams/{artifact-id}.mmd`
- Render it as a fenced mermaid code block inline in the conversation.

Example output:

````
```mermaid
graph TD
    ...
```
````

After showing the inline diagram, offer:
```
Render to image file?
  1. PNG  — high-resolution raster image (recommended for Word/PowerPoint)
  2. SVG  — scalable vector image (recommended for web/HTML export)
  3. No thanks
```
If the user selects 1 or 2, proceed to **Render to Image** below.

**For png / svg (Render to Image):**

Renders a `.mmd` file to a raster or vector image using mermaid-cli (`mmdc`).

**Input resolution — in order of preference:**
1. A `.mmd` file path provided directly by the user
2. A `.mmd` file generated in the current session (from the Mermaid step above)
3. Scan `EA-projects/{slug}/diagrams/` for `.mmd` files and ask the user to select one

**Theme and background options** (from command arguments or prompt):
- `--theme`: `default` (default) | `dark` | `forest` | `neutral` | `base`
- `--bg`: `white` (default) | `transparent` | `#rrggbb`

If no options were provided and the user didn't specify, use defaults silently.

**Check for mmdc:**

```bash
# Check if mmdc is available
if command -v mmdc &>/dev/null; then
    MMDC_CMD="mmdc"
elif command -v npx &>/dev/null; then
    MMDC_CMD="npx -y @mermaid-js/mermaid-cli"
    echo "ℹ️  mmdc not found globally — using npx (will download on first run)"
else
    echo "ERROR: mermaid-cli not found."
    echo "Install it with:  npm install -g @mermaid-js/mermaid-cli"
    exit 1
fi
```

If neither `mmdc` nor `npx` is available, display:
```
⚠️  mermaid-cli (mmdc) is not installed.

To install:
  npm install -g @mermaid-js/mermaid-cli

Or, if you have Node.js with npx:
  npx -y @mermaid-js/mermaid-cli (used automatically on next run)

After installing, run /ea-generate again to render the image.
```
Then stop.

**Render the file:**

```bash
OUTPUT_FILE="EA-projects/{slug}/diagrams/{stem}.{format}"

$MMDC_CMD \
  -i "{input.mmd}" \
  -o "$OUTPUT_FILE" \
  -t {theme} \
  -b {bg} \
  -w 1920 \
  -s 2
```

For SVG, omit `-w` and `-s` (they apply to raster output only):
```bash
$MMDC_CMD \
  -i "{input.mmd}" \
  -o "$OUTPUT_FILE" \
  -t {theme} \
  -b {bg}
```

If the command fails (non-zero exit):
- Display the stderr output
- Suggest common fixes:
  - "If you see a Puppeteer/Chromium error, run: `npx puppeteer browsers install chrome`"
  - "If you see a syntax error, open the .mmd file and check the diagram syntax"
  - "On WSL2, try setting: `export PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable`"

**Render all `.mmd` files in the diagrams directory:**

If the user runs `/ea-generate png --all` or `/ea-generate svg --all`:

```bash
SCRIPT=$(find "$HOME/.claude" -name "render-mermaid.py" -path "*/ea-assistant/scripts/*" 2>/dev/null | head -1)
if [ -z "$SCRIPT" ]; then
  echo "ERROR: render-mermaid.py not found. Is the ea-assistant plugin installed?"
  exit 1
fi

python3 "$SCRIPT" \
  "EA-projects/{slug}/diagrams/" \
  --format {format} \
  --theme {theme} \
  --bg {bg}
```

This renders every `.mmd` file in the engagement's diagrams directory to images in the same directory.

**Diagram discovery (docx and pptx only):**

Before invoking the generation script, collect associated diagrams for inclusion:

1. Scan `EA-projects/{slug}/diagrams/` for files matching `{artifact-id}-*.png` — these are pre-rendered diagrams linked to this artifact.
2. Also scan for `{artifact-id}-*.mmd` files that have no corresponding `.png`. For each:
   - Render it to PNG automatically using the same mmdc detection logic from the **Render to Image** section above.
   - If rendering fails, skip that diagram and show a warning; continue with the rest.
3. Build a diagrams list in this format and write it to `/tmp/ea-diagrams-{artifact-id}.json`:

```json
[
  {"title": "Capability Map", "path": "EA-projects/{slug}/diagrams/{artifact-id}-capability-map.png"},
  {"title": "Stakeholder Power/Interest", "path": "EA-projects/{slug}/diagrams/{artifact-id}-stakeholder-power-interest.png"}
]
```

Derive `title` from the filename stem: strip `{artifact-id}-` prefix, replace `-` with spaces, capitalise each word.

If no diagrams are found, proceed without `--diagrams` (no appendix will be added). Do not prompt the user — include diagrams by default.

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

# Include diagrams if the list file was written above
DIAGRAMS_ARG=""
[ -f "/tmp/ea-diagrams-{artifact-id}.json" ] && DIAGRAMS_ARG="--diagrams @/tmp/ea-diagrams-{artifact-id}.json"

"$VENV/bin/python" "$SCRIPT" \
  --type {script-type} \
  --engagement-dir EA-projects/{slug} \
  --content @/tmp/ea-gen-{artifact-id}.json \
  $DIAGRAMS_ARG \
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

DIAGRAMS_ARG=""
[ -f "/tmp/ea-diagrams-{artifact-id}.json" ] && DIAGRAMS_ARG="--diagrams @/tmp/ea-diagrams-{artifact-id}.json"

"$VENV/bin/python" "$SCRIPT" \
  --type {script-type} \
  --engagement-dir EA-projects/{slug} \
  --content @/tmp/ea-gen-{artifact-id}.json \
  $DIAGRAMS_ARG \
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
Diagrams included: {N} (or "none")

Options:
1. Generate in another format
2. Generate diagrams for this artifact  (/ea-diagram)
3. Return to engagement (/ea-status)
```

For mermaid (inline), the diagram is already shown. Offer:

```
Options:
1. Render as PNG image  (mermaid-cli)
2. Render as SVG image  (mermaid-cli)
3. Generate as docx instead
4. Generate as pptx instead
5. Return to engagement (/ea-status)
```

For png/svg, after successful render report:

```
Generated: EA-projects/{slug}/diagrams/{filename}.{ext}
Size: {file-size}

Options:
1. Render another diagram
2. Render all diagrams in this engagement  (/ea-generate {format} --all)
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
