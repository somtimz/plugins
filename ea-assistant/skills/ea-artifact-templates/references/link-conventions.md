# Link Conventions — Internal Link Styles

Single source of truth for how internal links are written in engagement artifacts. Commands that write or parse links follow this reference; do not restate the rules inline.

## The `linkStyle` setting

| Aspect | Value |
|---|---|
| Location | engagement `.claude/rules/ea-local-config.md` → `linkStyle:` line |
| Values | `wikilink` \| `markdown` |
| Default (new engagements) | `wikilink` — seeded by `/ea-new` |
| Absent (legacy engagements) | `markdown` — existing engagements keep their current link behavior; add `linkStyle: wikilink` to the local config to switch |

## Link forms by target

All paths in the markdown column are relative to the artifact file at `artifacts/{phase}/`.

| Target | `wikilink` (Obsidian) | `markdown` |
|---|---|---|
| Detail file (ID cell) | `[[G-001]]` | `[G-001](../details/G-001.md)` |
| Detail file (Details column) | `[[G-001\|→]]` | `[→](../details/G-001.md)` |
| Same-phase artifact | `[[statement-of-architecture-work\|SAoW]]` | `[SAoW](./statement-of-architecture-work.md)` |
| Different-phase artifact | `[[business-architecture\|Business Architecture]]` | `[Business Architecture](../phase-b/business-architecture.md)` |
| Diagram (link) | `[[context-diagram.png\|Context Diagram]]` | `[Context Diagram](../../diagrams/context-diagram.png)` |
| Diagram (embed) | `![[context-diagram.png]]` | `![Context Diagram](../../diagrams/context-diagram.png)` |
| Upload | `[[strategy-2026.pdf\|Strategy Paper]]` | `[Strategy Paper](../../uploads/strategy-2026.pdf)` |
| Research document | `[[zero-trust-research\|Zero Trust Research]]` | `[Zero Trust Research](../../ResearchAndReferences/zero-trust-research.md)` |

## Wikilink rules

- **Bare file name, no path, no `.md` extension** (non-`.md` files keep their extension). Obsidian resolves wikilinks vault-wide by file name.
- **Alias with `|`** when the display text differs from the file name: `[[G-001|→]]`, `[[architecture-vision|Architecture Vision]]`.
- **Inside markdown tables, escape the alias pipe** — write `[[G-001\|→]]` so the link does not split the cell. This is Obsidian's own escaping convention for links in tables. Prose links use the plain `|`.
- **Collision caveat:** file names like `architecture-vision.md` or `G-001.md` repeat across engagements. In a vault holding multiple engagements, bare-name wikilinks may resolve to the wrong engagement — use one vault per engagement, or set `linkStyle: markdown`.
- **Frontmatter is always plain paths.** `relatedArtifacts`, `diagrams`, and `links[].path` keep relative path strings regardless of `linkStyle` — they are data fields, not rendered links.
- **ID-token scanning is unaffected.** Regexes like `G-\d{3}` match inside `[[G-001]]` the same as inside `[G-001](...)`.

## Parsing rule (all commands)

Commands that detect internal links must recognise **both** forms regardless of the engagement's `linkStyle`. Detail-file link patterns:

```
[→](../details/{ID}.md)    [{ID}](../details/{ID}.md)    [[{ID}]]    [[{ID}|→]]    [[{ID}\|→]]    [[{ID}|...]]
```

Alias separators appear as `|` (prose) or `\|` (inside tables) — treat them identically when parsing.

## Export rule (`/ea-generate`, `/ea-publish`)

Wikilinks do not survive into Word/PPTX or consolidated publish output. Before export, resolve them to text: `[[target|label]]` → `label`, `[[target]]` → `target`. Markdown links follow the existing link-rewriting rules.

## Templates

Templates ship with wikilink-form example rows (matching the default). When an engagement has `linkStyle: markdown`, write markdown links per the table above when authoring rows — including rows mirrored by Display View Sync.
