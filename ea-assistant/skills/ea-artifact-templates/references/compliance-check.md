# Artifact Compliance Check — Reference

This reference defines what makes an EA artifact compliant with the current template standard, how to detect non-compliance, and what remediation options to offer the user. All commands that load or display an artifact MUST run this check before presenting the artifact for editing, review, or interview.

---

## What Is a Compliant Artifact?

A compliant artifact satisfies all rules in its applicable tier. Rules are additive — Tier 1 applies to all artifacts, Tier 2 to artifacts with rich templates, and Tier 3 to specific artifact types.

---

### Tier 1 — Universal (all artifacts)

These checks apply to every `.md` file in `artifacts/`:

| # | Rule | Compliant example | Non-compliant |
|---|---|---|---|
| T1-1 | Frontmatter block present (YAML between `---` delimiters) | `--- artifact: ... ---` | No frontmatter |
| T1-2 | `artifact` field present and non-empty | `artifact: Architecture Vision` | Missing or blank |
| T1-3 | `engagement` field present and non-empty | `engagement: Acme Retail` | Missing or blank |
| T1-4 | `phase` field present | `phase: A` | Missing |
| T1-5 | `status` field present with valid value | `status: Draft` | Missing or invalid value |
| T1-6 | `reviewStatus` field present with valid value | `reviewStatus: Not Reviewed` | Missing |
| T1-7 | `version` field present | `version: 0.1` | Missing |
| T1-8 | `lastModified` field present | `lastModified: 2026-03-26` | Missing |
| T1-9 | Document has at least one top-level heading | `# Architecture Vision` | No headings |
| T1-10 | `taxonomy` block present with `domain`, `category`, `audience`, `layer`, `sensitivity` | `taxonomy: domain: Cross-cutting ...` | Missing taxonomy block or missing sub-fields |
| T1-11 | `templateVersion` field present | `templateVersion: 0.9.5` | Missing — run `/ea-migrate` to add |

**Valid `status` values:** `Draft` | `In Review` | `Approved` | `Needs Revision`
**Valid `reviewStatus` values:** `Not Reviewed` | `In Review` | `Approved` | `Needs Revision`
**Valid `taxonomy.domain` values:** `Business` | `Data` | `Application` | `Technology` | `Cross-cutting`
**Valid `taxonomy.category` values:** `Strategy` | `Analysis` | `Design` | `Planning` | `Governance` | `Register`
**Valid `taxonomy.audience` values:** `Executive` | `Business` | `Architecture` | `Delivery` | `Governance` | `All`
**Valid `taxonomy.layer` values:** `Motivation` | `Baseline` | `Target` | `Transition` | `Governance` | `Reference`
**Valid `taxonomy.sensitivity` values:** `Internal` | `Confidential` | `Restricted`

See `references/taxonomy.md` for the canonical taxonomy definition and the full mapping table.

---

### Tier 2 — Standard template structure

Applies to artifacts created from plugin templates (detected by the presence of a `# {Artifact Name}` heading):

| # | Rule | Notes |
|---|---|---|
| T2-1 | Engagement header block present: `**Engagement:**`, `**Organisation:**`, `**Date:**` | Often at lines 1–6 after the heading |
| T2-2 | At least one content section (`## {N}. {Section Name}`) | Blank artifact skeletons are non-compliant |
| T2-3 | No raw `{{placeholder}}` tokens in frontmatter fields | Unreplaced template tokens in frontmatter |

---

### Tier 3 — Artifact-specific requirements

Applies only to named artifact types:

| Artifact | Requirement | Rule ID |
|---|---|---|
| Architecture Vision, Business Architecture, Data Architecture, Application Architecture, Technology Architecture | `## Appendix A3 — Decision Log` section present | T3-A3 |
| Architecture Vision, Business Architecture, Data Architecture, Application Architecture, Technology Architecture, Gap Analysis, Architecture Roadmap, Statement of Architecture Work, Migration Plan | `## Appendix A4 — Stakeholder Concerns & Objections` section present | T3-A4 |
| Architecture Roadmap | `## Strategic Alignment` section present with at least one populated row (non-placeholder) | T3-ROAD-SA |
| Architecture Roadmap | At least one WP-NNN entry has a non-empty `Advances Goals / Objectives` or `Executes Strategies` field | T3-ROAD-WP |
| Requirements Register | Scope column present (Corporate / Project distinction) | T3-REQ |
| Traceability Matrix | Two-section structure (Corporate / Project) present | T3-TRACE |
| Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Architecture Roadmap, Statement of Architecture Work, Migration Plan, Compliance Assessment, Requirements Register, Engagement Charter, Governance Framework, Implementation Governance Plan | `## Related Architecture Decisions` section present | T3-ADR |

---

## Compliance Check Procedure

Run this check whenever an artifact is loaded for any of the following operations:
- Interview (ea-interviewer, step 1)
- Review (ea-review, Load Artifact step)
- View (ea-artifact, view mode)

**Steps:**

1. Read the artifact file.
2. Check Tier 1 rules — collect all failures.
3. Check Tier 2 rules — collect all failures.
4. Check Tier 3 rules relevant to this artifact type — collect all failures.
5. If zero failures → artifact is compliant. Continue silently.
6. If one or more failures → classify and present the compliance prompt (see below).

**Failure classification:**

| Classification | Condition | Urgency |
|---|---|---|
| **Structural** | Any T1 failure | High — affects data integrity and interview/review reliability |
| **Template drift** | Any T2 or T3 failure, no T1 failure | Medium — artifact usable but missing expected sections |

---

## Compliance Prompt

When failures are found, pause the current operation and present:

```
⚠️ Compliance check — {artifact name}

This artifact does not fully conform to the current template standard.

Issues found:
  {bullet list of each failure with rule ID and short description}

Options:
  1. Achieve compliance  — add missing fields/sections (your content is preserved)
  2. Accept as-is        — use with defaults for missing fields (no structure changes)
  3. View details        — show full compliance report before deciding
```

Wait for the user's response before proceeding with the original operation.

---

## Option 1 — Achieve Compliance

Apply all required changes to bring the artifact up to the current standard. **Preserve all existing content without modification.**

**Remediation actions by rule:**

| Rule | Remediation |
|---|---|
| T1-1 (no frontmatter) | Add frontmatter block at the top with all required fields populated from context or defaults |
| T1-2 (no `artifact`) | Add `artifact: {inferred from heading or filename}` |
| T1-3 (no `engagement`) | Add `engagement: {from active engagement.json}` |
| T1-4 (no `phase`) | Add `phase: {infer from artifact type or ask}` |
| T1-5 (no/invalid `status`) | Add `status: Draft` |
| T1-6 (no `reviewStatus`) | Add `reviewStatus: Not Reviewed` |
| T1-7 (no `version`) | Add `version: 0.1` |
| T1-8 (no `lastModified`) | Add `lastModified: {today's date}` |
| T1-9 (no heading) | Add `# {artifact name}` as first line after frontmatter |
| T2-1 (no engagement header) | Add `**Engagement:** {name}` etc. block below the heading |
| T2-2 (no content sections) | Add placeholder: `## 1. Content\n\n⚠️ Not answered` |
| T2-3 (unreplaced frontmatter tokens) | Replace `{{engagement_name}}` etc. from `engagement.json`; leave body tokens intact |
| T3-A3 (missing Appendix A3) | Append the standard A3 section at the end of the artifact, before the footer line |
| T3-A4 (missing Appendix A4) | Append the standard A4 section after A3 (or before the footer line if A3 is absent) |
| T3-REQ (missing scope column) | Note: offer to run `/ea-requirements migrate` to add Corporate/Project scope |
| T3-TRACE (missing sections) | Note: offer to regenerate via `/ea-requirements trace` |

After applying all remediations:
- Update `lastModified` in both the artifact frontmatter and `engagement.json`
- Confirm: "Compliance achieved — {N} issues resolved. {list of changes made}"
- Continue with the original operation (interview / review / view)

---

## Option 2 — Accept As-Is (with sensible defaults)

Apply **only** the minimum changes needed to make the artifact loadable and functional. Do **not** change the document structure.

**Minimum changes:**

1. If T1 frontmatter failures exist: add a minimal frontmatter block with defaults — do not modify the document body.
2. Set `complianceNote: accepted-non-standard` in the frontmatter.
3. Update `lastModified` to today.
4. Write these minimal changes to the artifact file.
5. Continue with the original operation immediately.

**Defaults for all fields:**

| Field | Default |
|---|---|
| `artifact` | Inferred from filename (e.g., `architecture-vision.md` → `Architecture Vision`) or "Unknown Artifact" |
| `engagement` | From active `engagement.json` → `name` |
| `phase` | Inferred from artifact type; "Unknown" if cannot determine |
| `status` | `Draft` |
| `reviewStatus` | `Not Reviewed` |
| `version` | `0.1` |
| `lastModified` | Today's date (YYYY-MM-DD) |

**Behaviour for missing sections:**
- Do NOT add missing sections.
- For interview: extract questions from whatever `{{placeholder}}` tokens exist; treat sections not in the current template as freeform content.
- For review: present the document as-is; note in the review summary that the artifact is non-standard.
- Note in the session log: "Artifact accepted non-standard — {N} compliance issues noted."

---

## Option 3 — View Details

Display the full compliance report before the user decides:

```
Compliance Report — {artifact name}
Generated: {date}

Tier 1 — Universal checks
  ✅ T1-1  Frontmatter present
  ❌ T1-6  reviewStatus field missing
  ✅ T1-7  version field present
  ...

Tier 2 — Template structure
  ❌ T2-1  Engagement header block missing
  ✅ T2-2  Content sections present
  ...

Tier 3 — Artifact-specific
  ❌ T3-A3  Appendix A3 — Decision Log section missing

Summary: 3 issues (1 structural, 2 template drift)
```

After displaying, re-present the three-option prompt (Option 1 / Option 2 / Option 3 removed, back to 1 and 2).

---

## Compliance State in Frontmatter

After any compliance operation, the artifact frontmatter may contain:

| Field | Value | Meaning |
|---|---|---|
| `complianceNote` | *(absent)* | Artifact is fully compliant |
| `complianceNote` | `accepted-non-standard` | User accepted the artifact as-is; structural issues remain |
| `complianceNote` | `remediated-{YYYY-MM-DD}` | Compliance was achieved on this date |

The `complianceNote` field is informational only — it does not affect artifact status or review workflows.

---

## Reporting Compliance in `/ea-status`

`/ea-status` reads each artifact in `engagement.json → artifacts[]` and checks for `complianceNote: accepted-non-standard`. If any exist, add to the engagement summary:

```
⚠️ Non-standard artifacts: {N} accepted as-is — run /ea-review to remediate
```
