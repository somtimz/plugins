# Migration Gap Catalogue

Reference for `/ea-migrate`. Defines all gap checks, severity levels, and remediation actions.

## 3a — engagement.json Schema Gaps

| Check | Gap if… | Severity |
|---|---|---|
| `pluginVersion` field present | Field absent | Low |
| `lastMigratedVersion` field present | Field absent | Low |
| `direction` field present | Absent (pre-0.4.0) | Medium |
| `metrics` field present | Absent (pre-0.5.0) | Low |
| `engagementType` field present | Absent (pre-0.2.0) | Low |
| `architectureDomains` field present | Absent (pre-0.2.0) | Low |
| `optOuts` field present | Absent (pre-0.8.0) | Low |
| `architectureLevel` field present | Absent (pre-0.9.28) | Low |
| `requirements-index.json` scope values use Enterprise/Program | `scope: "Corporate"` or `"Project"` found (pre-0.9.35) | Low |

**Remediations:**
- `pluginVersion` absent → add `"pluginVersion": "{current_version}"`
- `lastMigratedVersion` absent → add `"lastMigratedVersion": "0.0.0"`
- `direction` absent → add empty `direction` object with keys matching `architectureDomains`
- `metrics` absent → add empty `metrics` object with keys matching `architectureDomains`
- `engagementType` absent → add `"engagementType": null`
- `architectureDomains` absent → add `"architectureDomains": ["Business","Data","Application","Technology"]`
- `optOuts` absent → add `"optOuts": []`
- `architectureLevel` absent → add `"architectureLevel": null`; inform: "Set this via `/ea-config metadata` — allowed values: Strategic, Segment, Capability, Solution. Defaults to Segment until set."
- Legacy scope values (`Corporate`/`Project`) → rename all `"Corporate"` → `"Enterprise"` and `"Project"` → `"Program"` in `requirements-index.json`. Non-destructive; no content change.

## 3b — Expected Artifacts Missing

| Artifact | Introduced in | Severity if absent |
|---|---|---|
| Engagement Charter (`engagement-charter`) | 0.9.5 | Medium |
| Governance Framework (`governance-framework`) | 0.9.4 | Low |

**Remediation:** Do NOT auto-create artifacts — they require interview input. Offer: "Would you like to create this artifact now? (`/ea-artifact create {artifact-id}`)"

## 3c — Artifact Frontmatter Gaps

For each artifact `.md` in `EA-projects/{slug}/artifacts/` and phase subdirectories (excluding `*.review.md`, registers, session logs):

| Check | Gap if… | Introduced in | Severity |
|---|---|---|---|
| `taxonomy:` block present with all 5 sub-fields | Block absent or incomplete | 0.9.4 | Medium |
| `templateVersion:` field present | Field absent | 0.9.5 | Low |
| `complianceNote` not set to `accepted-non-standard` | Flag for review only | — | Info |

**Taxonomy remediation:**
1. Look up artifact type from `artifact:` frontmatter field
2. Find canonical taxonomy from `skills/ea-artifact-templates/references/taxonomy.md`
3. If found: present canonical values for confirmation; inject `taxonomy:` block after `templateVersion:` (or after `version:` if `templateVersion` also absent)
4. If not found: present blank taxonomy block; ask user to fill in values

**templateVersion remediation:** Inject `templateVersion: 0.0.0` to signal pre-versioning origin.

## 3d — Phase-Organized Artifact Structure

| Check | Gap if… | Introduced in | Severity | Remediated by |
|---|---|---|---|---|
| Artifact files in `artifacts/{phase-folder}/` | Any `artifacts[]` entry has file path directly in `artifacts/` (flat) | 1.0.0 | Medium | `/ea-reorganize` |
| `relatedArtifacts:` field present | Field absent | 1.0.0 | Low | `/ea-migrate` |
| `diagrams:` field present | Field absent | 1.0.0 | Low | `/ea-migrate` |
| `links:` field present | Field absent | 1.0.0 | Low | `/ea-migrate` |

**Flat-path detection (GAP-M-015):** Count artifacts with flat paths and report the total. Do **not** offer to move them here — direct the user to `/ea-reorganize` for all file moves.

**Missing fields remediation (GAP-M-016):** Inject `relatedArtifacts: []`, `diagrams: []`, `links: []` after the `tags:` line in the taxonomy block. Non-destructive — safe to auto-apply.

## 3e — Rules File Gap

| Check | Gap if… | Introduced in | Severity |
|---|---|---|---|
| `.claude/rules/ea-engagement.md` exists | File absent | 0.9.12 | Low |
| `CLAUDE.md` contains `## Where to Find Content` | Section absent (old-format fat CLAUDE.md) | 0.9.12 | Medium |

**Rules file remediation:** Create `.claude/rules/ea-engagement.md` from `templates/seeds/engagement-rules.md` with current engagement name and slug.

**CLAUDE.md remediation:** Regenerate `CLAUDE.md` from `templates/seeds/engagement-claude-md.md` using current `engagement.json` state. Full strategic data is not lost — it remains in `engagement.json → direction` and artifact files.

## 3f — Artifact Content Gaps

| Check | Artifact Types | Gap if… | Introduced in | Severity |
|---|---|---|---|---|
| `## Appendix A3 — Decision Log` present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Roadmap, SAoW, Migration Plan | Section absent | 0.7.0 | Medium |
| `## Appendix A4 — Stakeholder Concerns & Objections` present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Roadmap, SAoW, Migration Plan, Engagement Charter, Governance Framework, Implementation Governance Plan | Section absent | 0.9.3 | Medium |
| `## Appendix A5 — Related Architecture Decisions` present | Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Architecture Roadmap, SAoW, Migration Plan, Compliance Assessment, Requirements Register, Engagement Charter, Governance Framework, Implementation Governance Plan | Section absent | 0.9.7 | Low |

**Appendix remediation:** See `skills/ea-artifact-templates/references/appendix-templates.md` for the markdown blocks to inject. Ordering: A3 → A4 → A5. Place each missing appendix after any existing lower-numbered appendix, or before any existing higher-numbered one. If none exist, append at the document end.

## Handling Special Cases

**Non-standard artifacts:** If `artifact:` field does not match a known template type, flag `[Info]` — not a migration error. Do not attempt canonical taxonomy. Suggest manual review or `/ea-grill artifact`.

**Approved artifacts:** Warn before writing:
```
⚠️ {artifact name} is Approved. This remediation only adds metadata (taxonomy/templateVersion) or appends
empty appendix tables — content sections are not changed. The reviewStatus will remain Approved. Proceed? (y/n)
```
Only structural metadata additions are permitted on Approved artifacts.
