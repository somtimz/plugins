---
name: ea-generate
description: Generate a formatted file (Word, PowerPoint, Mermaid diagram, or rendered image) from an EA artifact or .mmd file
argument-hint: "[artifact-name] [docx|pptx|mermaid|png|svg] [--theme <theme>] [--bg <color>]"
allowed-tools: [Read, Write, Bash]
---

Export a single EA artifact as a formatted file. See `skills/ea-generation/references/artifact-type-mapping.md` for format recommendations and `--type` values per artifact.

If no engagement is active, display "No engagement is currently open. Run /ea-open first." and stop.

### Step 1: Select Artifact

If no artifact name was given, read `EA-projects/{slug}/engagement.json → artifacts[]` and display a numbered list of existing artifacts with their status and recommended format. Prompt for selection.

**Rendering an existing `.mmd` file directly:** If the user provides a `.mmd` file path or specifies `png`/`svg` with no artifact name, skip to the **Render to Image** section of Step 4.

### Step 2: Select Format

Recommend the primary format for the artifact type (see `skills/ea-generation/references/artifact-type-mapping.md`). Offer: `docx`, `pptx`, `mermaid` (if available), `png`, `svg`. Omit mermaid/png/svg for non-Mermaid artifact types.

### Step 3: Read and Extract Artifact Content

1. Read the artifact file from `engagement.json → artifacts[].file`
2. **Resolve relative image links** — for each `![alt](relative-path)` in the body, resolve to an absolute path before extraction
3. **Rewrite cross-artifact and relative text links** — apply the following rules to every `[display](target)` link in the body before extraction:

   | Link type | Example | Action |
   |---|---|---|
   | External URL | `[TOGAF](https://...)` | Keep as-is — pandoc and python-docx preserve clickable hyperlinks |
   | Same-document section anchor | `[Goals](#3-goals)` | Keep as-is — pandoc resolves internal anchors in docx/pdf |
   | Relative artifact link | `[Arch Vision](../phase-a/architecture-vision.md)` | Strip link, keep display text only: `Architecture Vision` |
   | Relative artifact + section | `[Goals](../phase-a/architecture-vision.md#3-goals)` | Strip link, keep display text only: `Goals` |
   | Relative path, no display text | `[../phase-a/architecture-vision.md](../phase-a/architecture-vision.md)` | Replace with the prettified artifact name: `Architecture Vision` |

   **Rule:** any link whose target starts with `./`, `../`, or a relative filename (no `http`) and is not an image is a relative file link — strip the link target and keep only the display text.

4. Parse into a content JSON object per the schema in `skills/ea-generation/references/content-extraction-schema.md`
5. Write extracted JSON to `/tmp/ea-gen-{artifact-id}.json`

### Step 4: Generate Output

**For Mermaid (inline):**
- Select diagram type from artifact type: Stakeholder Map → `graph TD/LR`, Roadmap → `gantt`, Capability Map → `graph TD`, other → `graph TD`
- Build and render diagram; save source to `EA-projects/{slug}/diagrams/{artifact-id}.mmd`
- Render as fenced mermaid code block inline
- After display, offer: Render to PNG, Render to SVG, No thanks

**For png / svg (Render to Image):**

Input (in order of preference): user-provided `.mmd` path → current session `.mmd` → scan `EA-projects/{slug}/diagrams/` and ask.

Options: `--theme` (`default` | `dark` | `forest` | `neutral` | `base`), `--bg` (`white` | `transparent` | `#rrggbb`). Use defaults silently if not specified.

Check for `mmdc`:
```bash
if command -v mmdc &>/dev/null; then
    MMDC_CMD="mmdc"
elif command -v npx &>/dev/null; then
    MMDC_CMD="npx -y @mermaid-js/mermaid-cli"
else
    echo "ERROR: mermaid-cli not found. Install: npm install -g @mermaid-js/mermaid-cli"
    exit 1
fi
```

Render:
```bash
$MMDC_CMD -i "{input.mmd}" -o "EA-projects/{slug}/diagrams/{stem}.{format}" -t {theme} -b {bg} -w 1920 -s 2
# For SVG omit -w and -s
```

If render fails: display stderr; suggest `npx puppeteer browsers install chrome` for Chromium errors, check `.mmd` syntax for syntax errors, and on WSL2: `export PUPPETEER_EXECUTABLE_PATH=/usr/bin/google-chrome-stable`.

**Render all (`--all`):**
```bash
SCRIPT=$(find "$HOME/.claude" -name "render-mermaid.py" -path "*/ea-assistant/scripts/*" 2>/dev/null | head -1)
python3 "$SCRIPT" "EA-projects/{slug}/diagrams/" --format {format} --theme {theme} --bg {bg}
```

**Diagram discovery (docx/pptx):**

Collect diagrams from two sources, merge and deduplicate (Source A first):
- **Source A** — `meta.diagrams` from artifact frontmatter (paths relative to engagement root → resolve to absolute)
- **Source B** — scan `diagrams/` for `{artifact-id}-*.png`; also render any `{artifact-id}-*.mmd` with no matching `.png`

Write diagram list to `/tmp/ea-diagrams-{artifact-id}.json`:
```json
[{"title": "Capability Map", "path": "EA-projects/{slug}/diagrams/{artifact-id}-capability-map.png"}]
```
Derive `title` from filename stem (strip `{artifact-id}-` prefix, spaces, title-case). If no diagrams found, proceed without `--diagrams`.

**For docx:**
```bash
SCRIPT=$(find "$HOME/.claude" -name "generate-docx.py" -path "*/ea-assistant/scripts/*" 2>/dev/null | head -1)
VENV="$HOME/.ea-assistant-venv"
[ ! -f "$VENV/bin/python" ] && python3 -m venv "$VENV"
"$VENV/bin/python" -c "import docx" 2>/dev/null || "$VENV/bin/pip" install --quiet python-docx python-pptx
DIAGRAMS_ARG=""
[ -f "/tmp/ea-diagrams-{artifact-id}.json" ] && DIAGRAMS_ARG="--diagrams @/tmp/ea-diagrams-{artifact-id}.json"
"$VENV/bin/python" "$SCRIPT" \
  --type {script-type} --engagement-dir EA-projects/{slug} \
  --content @/tmp/ea-gen-{artifact-id}.json $DIAGRAMS_ARG \
  --output EA-projects/{slug}/artifacts/{phase-folder}/{artifact-id}.docx
```

**For pptx:** Same bootstrap; replace `generate-docx.py` with `generate-pptx.py` and `.docx` with `.pptx`.

> **WSL2:** Unix paths work as-is. Native Windows PowerShell: replace `$HOME` with `$env:USERPROFILE`, `bin/python` with `Scripts\python.exe`.

If the script exits non-zero, display the error and stop. Do not update the engagement.

### Step 5: Update Engagement

After successful docx/pptx generation, update `artifacts[].lastModified` in `engagement.json` to now.

### Step 6: Confirm

Report file path, size, and diagram count. Offer: generate another format, generate diagrams (`/ea-diagram`), return to engagement.
