# Template Authoring Guide

This guide explains how to write, extend, and maintain the document templates used by the EA Assistant to generate architecture artefacts. It covers placeholder token conventions, guidance text markup, answer state markers, template file structure, and best practices for template quality.

---

## Template File Structure

Each artefact template is a Markdown file (`.md`) stored in the `templates/` directory of the EA Assistant plugin. The file structure is:

```
templates/
  <artefact-slug>.md        ← The template file
  <artefact-slug>.meta.yaml ← Optional metadata sidecar (see below)
```

Template file names use kebab-case and match the artefact identifier used in the plugin's artefact registry. For example:

- `architecture-vision.md`
- `business-capability-map.md`
- `architecture-requirements-specification.md`
- `application-portfolio-catalogue.md`

---

## Template File Anatomy

A template file has three sections, in order:

### 1. Front Matter (YAML)

A YAML front matter block enclosed in `---` delimiters. This is required in every template.

```yaml
---
artefact_id: architecture-vision
artefact_name: Architecture Vision
adm_phase: A
version: "1.0"
owner: EA Assistant Plugin
description: >
  High-level description of the target architecture delivered at the end of Phase A
  to secure stakeholder approval to proceed.
required_inputs:
  - engagement_name
  - sponsor_name
  - architecture_scope
  - business_drivers
tags:
  - phase-a
  - vision
  - stakeholder
---
```

**Front matter fields:**

| Field | Type | Required | Description |
|---|---|---|---|
| `artefact_id` | String | Yes | Matches the filename stem; used as the template's unique key |
| `artefact_name` | String | Yes | Human-readable artefact name |
| `adm_phase` | String | Yes | Primary ADM phase (Prelim, A, B, C, D, E, F, G, H) |
| `version` | String | Yes | Template version in semver format |
| `owner` | String | Yes | Who maintains this template |
| `description` | String | Yes | One-paragraph description of the artefact's purpose |
| `required_inputs` | List | No | Token names that must be resolved before the template can be rendered |
| `tags` | List | No | Arbitrary tags for filtering and discovery |

### 2. Guidance Header (Optional)

A comment block immediately after the front matter that is visible only to template authors, not rendered in the output document.

```markdown
<!-- TEMPLATE GUIDANCE
This template is used by the generate-artifact command for Phase A Architecture Vision.
Key instruction points are marked with [GUIDANCE] blocks.
Placeholder tokens are marked with {{double_braces}}.
Answer state markers are used in section fields that may be populated from interview data.
-->
```

### 3. Document Body

The main template content. This is the actual artefact structure. It uses standard Markdown with the additions described in this guide.

---

## Placeholder Token Conventions

Placeholder tokens represent dynamic values that are substituted when the template is rendered. They use double-brace syntax: `{{token_name}}`.

### Syntax Rules

- Token names use `snake_case`.
- Tokens are case-sensitive: `{{Engagement_Name}}` and `{{engagement_name}}` are different tokens.
- Tokens may appear anywhere in the document body: headings, paragraphs, table cells, code blocks.
- A token may appear multiple times in the same template; all occurrences are substituted with the same value.

### Token Categories

#### Engagement Tokens
Available in all templates. Populated from the active engagement record.

| Token | Description | Example Value |
|---|---|---|
| `{{engagement_name}}` | Name of the EA engagement | "ANZ Bank — Digital Core Modernisation" |
| `{{engagement_id}}` | Unique engagement ID | "ENG-2025-042" |
| `{{client_name}}` | Client organisation name | "ANZ Bank" |
| `{{sponsor_name}}` | Engagement sponsor name | "Jane Smith" |
| `{{lead_architect}}` | Lead architect name | "Alex Johnson" |
| `{{date_created}}` | ISO date the document was generated | "2025-09-15" |
| `{{adm_phase}}` | Current ADM phase | "Phase A" |

#### Architecture Scope Tokens
Populated from the scope definition in the engagement record.

| Token | Description |
|---|---|
| `{{architecture_scope}}` | Narrative scope statement |
| `{{in_scope_domains}}` | Comma-separated list of domains in scope |
| `{{out_of_scope_items}}` | Comma-separated list of explicit exclusions |
| `{{target_date}}` | Target completion date for the architecture work |

#### Section-specific Tokens
Populated from the relevant interview data or architecture decisions. These are defined per template in the front matter `required_inputs` list.

Convention: section-specific tokens use a prefix matching the template area. For example, in the Architecture Vision template:
- `{{vision_summary}}` — the aspirational one-paragraph vision statement
- `{{business_drivers_list}}` — a formatted list of business drivers
- `{{key_stakeholders_table}}` — a rendered Markdown table of stakeholders

### Unresolved Tokens

If a token has no value at render time:
- If the token is in `required_inputs`, the render fails with an error listing unresolved tokens.
- If the token is not in `required_inputs`, it is rendered as `[UNRESOLVED: token_name]` in the output document — a visible marker that the author must complete.

---

## Guidance Text Markup

Guidance text is instructional content within the template body that helps the author understand what to write in a section. Guidance text is rendered differently from document content: it appears in the output document as a clearly marked callout, but it is not considered part of the formal artefact content.

### Guidance Block Syntax

```markdown
> [GUIDANCE] Describe the organisation's strategic context in 2–4 paragraphs.
> Cover: the industry context, key market pressures, and the strategic response the
> organisation is pursuing. This section is read by executive stakeholders; avoid
> technical jargon. Reference the engagement's primary business drivers.
```

All lines of a guidance block begin with `> [GUIDANCE]`. This distinguishes them from regular Markdown blockquotes.

### Inline Guidance

For brief, single-line hints within a table cell or paragraph:

```
| Stakeholder | Role | Primary Concern |
|---|---|---|
| {{sponsor_name}} | Programme Sponsor | <!-- [GUIDANCE] What is the sponsor's primary business concern? --> |
```

Inline guidance uses the `<!-- [GUIDANCE] ... -->` HTML comment syntax. It is rendered as a visible placeholder prompt in editable output but stripped when the document is exported for final distribution.

### Guidance Removal

When a template is rendered for final distribution (using the `finalize` option in the generate command), all guidance text is removed from the output. Authors should ensure they have replaced all guidance blocks with actual content before finalising.

---

## Answer State Markers

Answer state markers indicate the population status of a section or field in the rendered document. They are used when a template section may be populated from interview data or from direct input, and their status needs to be tracked.

### Marker Syntax

Markers are placed as the sole content of a section's response paragraph, or in a table cell:

| Marker | Meaning |
|---|---|
| `[DRAFT]` | Content has been populated but has not been reviewed |
| `[PENDING]` | Section is deliberately left for later population |
| `[SKIP]` | Section has been intentionally skipped for this engagement |
| `[N/A]` | Section is not applicable to this engagement |
| `[REVIEW]` | Content requires stakeholder review before it is accepted |

### Marker Placement Rules

- A marker must be the **only** content in its paragraph or cell to be recognised as a state marker.
- `[DRAFT]` is the default state for any section that has been auto-populated from interview data.
- `[PENDING]` is used by the template author to mark sections that will be completed in a future iteration.
- `[N/A]` suppresses the guidance block for that section in subsequent renders.

### Marker in Table Cells

```markdown
| Constraint ID | Statement | Source |
|---|---|---|
| CON-001 | Must deploy within existing Azure tenancy | Architecture Review Board |
| CON-002 | [PENDING] | [PENDING] |
```

A `[PENDING]` or `[N/A]` marker in any cell of a row marks that entire row as pending/not applicable.

---

## Extending an Existing Template

### Adding a New Section

1. Open the template file.
2. Add a new Markdown heading at the appropriate level.
3. Add guidance text under the heading using the `> [GUIDANCE]` syntax.
4. Add any required placeholder tokens.
5. If the section requires a specific input that must be available at render time, add the token name to the `required_inputs` list in the front matter.
6. Update the template `version` in the front matter (increment the patch version for minor additions; increment the minor version for structural changes).

### Adding a New Column to a Table

When extending a table in an existing template:
- Add the column to both the header row and the separator row (`|---|`).
- Add the appropriate token or `[PENDING]` marker as the default cell value in the body rows.
- Document the new column's expected content in a guidance block below the table.

### Modifying Guidance Text

Guidance text can be updated freely without version impact as long as the document structure (headings, tables, tokens) is unchanged. A guidance-only change increments only the patch version.

---

## Template Quality Guidelines

### Clarity of Guidance
Every section that is not self-explanatory must have a guidance block. Guidance blocks should answer:
- What information goes in this section?
- How long/detailed should it be?
- Who provides this information?
- What is an example of good content?

### Token Completeness
All values that vary per engagement must be tokens. Never hard-code client names, dates, project names, or specific technology names in a template. If you find yourself writing "Acme Corp" or "Azure" in the template body, it should be a token.

### Table Design
Tables in templates should have no more than 6 columns for readability in Word-exported documents. If more columns are needed, split into two related tables or use a heading/paragraph structure instead.

### Section Ordering
Follow the standard TOGAF artefact structure for the artefact type. Refer to the Artifact Descriptions reference for the expected contents and ordering. Architects who review the output will expect sections in a predictable order.

### Placeholder Tokens for Optional Sections
If a template section is optional (may not apply to all engagements), wrap it in an `[OPTIONAL]` block:

```markdown
<!-- [OPTIONAL: include only if the engagement has identified architecture patterns] -->
## Architecture Patterns

> [GUIDANCE] Identify any standard architecture patterns that will be applied in this engagement.

{{architecture_patterns_list}}
<!-- [/OPTIONAL] -->
```

The render engine omits optional blocks when the associated tokens are not present in the engagement record, unless the `include_optional` flag is set.

---

## Template Versioning and Deprecation

- Templates use semantic versioning: `MAJOR.MINOR.PATCH`.
- **MAJOR:** Structural changes that make the template incompatible with documents generated from the previous version (e.g., changing a required token name, removing a section).
- **MINOR:** Additive changes (new sections, new optional tokens).
- **PATCH:** Non-structural changes (guidance text updates, formatting fixes).

When a template is deprecated (superseded by a newer template design):
1. Add `deprecated: true` and `superseded_by: <new-template-id>` to the front matter.
2. The generate command will warn the user that a newer template is available.
3. Deprecated templates are retained for at least two major plugin versions to allow documents in progress to be completed.
