# Reference Architecture Schema

## RA-NNN Entry Frontmatter

| Field | Type | Values | Notes |
|---|---|---|---|
| `id` | string | `RA-NNN` (3-digit zero-padded) | Allocated from `repo.json → referenceArchitecture.nextId` (repo-level) or `engagement.json → localRA.nextId` (local) |
| `name` | string | any | Short descriptive name of the pattern |
| `domain` | enum | `Business \| Data \| Application \| Technology \| Cross-cutting` | Primary architecture domain |
| `status` | enum | `Draft \| Approved \| Deprecated` | Lifecycle state |
| `version` | string | semver `MAJOR.MINOR.PATCH` | Start at `1.0.0` |
| `source` | enum | `internal \| industry` | `industry` = derived from a named standard or body (e.g. BIAN, AWS WAF, Azure CAF) |
| `industryBody` | string | any | If `source: industry`, name the issuing body (e.g. "BIAN", "AWS") |
| `linkedSTDs` | array | `STD-NNN` strings | Standards this RA is derived from or aligns to |
| `linkedADRs` | array | `ADR-NNN` strings | ADRs ratified against this RA (populated during engagement adoption) |
| `createdDate` | ISO date | `YYYY-MM-DD` | |
| `lastModified` | ISO date | `YYYY-MM-DD` | Updated on every edit |

## Markdown Sections

| Section | Required | Content |
|---|---|---|
| `## Overview` | yes | 1–3 paragraphs: what the pattern is and when to use it |
| `## Architecture Layers` | yes | Table: Layer \| ABB-NNN \| ABB Name \| Role in Pattern |
| `## Key Decisions` | yes | Table: Decision \| Rationale Summary \| Candidate ADR Title |
| `## Constraints` | yes | Table: Description \| Candidate CST Title \| Flexibility (Mandatory \| Recommended) |
| `## Implied Principles` | yes | Bullet list of BP/DP/AP/TP IDs (if linked to a repo) or free-text principle statements |
| `## Adoption Notes` | yes | What is mandatory vs. flexible; known adaptations for common contexts |
| `## Grill Checklist` | yes | Numbered list of testable statements used by `/ea-grill` when this RA is adopted |

### Grill Checklist format

Each item is a single testable statement in present tense, e.g.:

```
1. All inter-service communication uses the event bus — no direct synchronous DB calls across service boundaries.
2. Each service owns exactly one bounded context — no shared schema between services.
3. Events are named in past tense (OrderPlaced, PaymentReceived) — no imperative commands (ProcessOrder).
```

The grill check passes if the engagement's artifacts are consistent with the statement; it fails (and is reported as a finding) if they contradict it or cannot be verified.

## Scope Labels

`(local)` — displayed in list output when the RA lives in `artifacts/cross-cutting/reference-architectures/` rather than the Architecture Repository. Local RAs are scoped to one engagement and are not shared. If a local and repo RA share the same ID, `/ea-refarch show` resolves the repo entry first; use `/ea-refarch show RA-NNN --local` to force local resolution.

## Storage Paths

| Scope | Path |
|---|---|
| Repo-level | `Architecture-Repository/reference-library/entries/RA-NNN.md` |
| Per-engagement | `artifacts/cross-cutting/reference-architectures/RA-NNN.md` |
| Repo index | `Architecture-Repository/reference-library/reference-architecture-index.md` |
| Engagement index | `artifacts/cross-cutting/reference-architectures/reference-architecture-index.md` |
