# Standards Information Base — STD Schema

Entries stored at: `Architecture-Repository/sib/standards/STD-NNN.md`

## YAML Frontmatter

```yaml
id: STD-NNN
name: "<Standard name>"
version: "<Version / year>"
issuingBody: "<ISO | IEEE | NIST | TOGAF | BIAN | eTOM | Regulatory | Other>"
adoptionStatus: "<Mandatory | Recommended | Informational | Deprecated>"
applicableDomains: [] # subset of: Business, Data, Application, Technology
linkedCSTs: []        # CST-NNN constraints that enforce this standard
linkedPOLs: []        # POL-NNN policies that reference this standard
applicablePhases: []  # ADM phases where most relevant (e.g. Preliminary, D, G)
lastReviewed: "YYYY-MM-DD"
nextReviewDate: "YYYY-MM-DD"
```

## Markdown Body Sections

- **Summary** — what the standard covers, its purpose, and why it matters to the organisation
- **Key Requirements** — principal obligations this standard imposes on the architecture
- **Compliance Evidence** — how to demonstrate compliance in EA artifacts (which sections, what artefacts)
- **Engagement Impact** — which artifact sections and ADM phases reference this standard

## Field Reference

| Field | Type | Values | Notes |
|---|---|---|---|
| `id` | string | `STD-NNN` (e.g. STD-001) | Allocated from `repo.json → sib.nextId` |
| `name` | string | any | Full standard name |
| `version` | string | any | Version or year (e.g. "2022", "v3.1") |
| `issuingBody` | enum | ISO, IEEE, NIST, TOGAF, BIAN, eTOM, Regulatory, Other | Standards body |
| `adoptionStatus` | enum | Mandatory, Recommended, Informational, Deprecated | Mandatory = must comply; Recommended = best practice; Informational = awareness only; Deprecated = no longer applicable |
| `applicableDomains` | array | Business, Data, Application, Technology | Architecture domains where standard applies |
| `linkedCSTs` | array | CST-NNN | Per-engagement constraints enforcing this standard |
| `linkedPOLs` | array | POL-NNN | Per-engagement policies referencing this standard |
| `applicablePhases` | array | Prelim, A, B, C-Data, C-App, D, E, F, G, H | ADM phases most relevant |
| `lastReviewed` | ISO date | YYYY-MM-DD | Last assessment date |
| `nextReviewDate` | ISO date | YYYY-MM-DD | Next scheduled review |

## Surface During Phase Interviews

When `/ea-standards surface --phase <phase>` is called (or Phase D interview runs with repoPath set):
- Show all STD entries where `applicablePhases` includes the current phase
- Highlight Mandatory entries first
- For Technology domain phases (C-App, D): surface STD entries where `applicableDomains` includes Technology

## Index File

`Architecture-Repository/sib/sib-index.md` — maintained by `/ea-standards`:

```markdown
# Standards Information Base Index

| ID | Standard | Version | Body | Adoption Status | Domains | Linked Constraints |
|---|---|---|---|---|---|---|
| STD-001 | ... | ... | ... | Mandatory | Technology | CST-001 |
```
