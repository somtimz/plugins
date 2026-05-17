# Technology Horizon Register — THR Schema

Entries stored at: `Architecture-Repository/technology-horizon/entries/THR-NNN.md`

## Ring Model

| Ring | Meaning | Action |
|---|---|---|
| **Adopt** | Production-ready; organisation endorses for new projects | Use in new projects without special approval |
| **Trial** | Shows promise; PoC encouraged | Run targeted proof-of-concept; report findings |
| **Assess** | Worth watching; too early for broad use | Monitor actively; revisit at next review cycle |
| **Hold** | Do not start new work with this technology | Plan migration away from existing usage |

Ring changes are tracked in `ringHistory[]` for audit purposes.

## YAML Frontmatter

```yaml
id: THR-NNN
name: "<Technology name>"
category: "<Platform | Language | Framework | Pattern | Practice | Tool | Standard>"
ring: "<Adopt | Trial | Assess | Hold>"
rationale: "<One-line reason for current ring placement>"
pocEvidence: ""       # path to ResearchAndReferences/ item or uploads/ if PoC was run
linkedADRs: []        # ADR-NNN — decisions that referenced this THR entry
linkedVDRs: []        # VDR-NNN — vendors implementing this technology
linkedABBs: []        # ABB-NNN — ABBs this technology could implement
ringHistory:
  - date: "YYYY-MM-DD"
    from: ""
    to: ""
    reason: ""
reviewDate: "YYYY-MM-DD"
addedDate: "YYYY-MM-DD"
addedBy: ""
```

## Markdown Body Sections

- **Overview** — what it is, maturity level, ecosystem size, major adopters
- **Organisational Fit** — why this ring was assigned; specific risks or benefits for the organisation
- **PoC Results** — if a trial was run: scope, findings, recommendation (link to pocEvidence)
- **Alternatives** — other technologies in the same ABB space at similar ring positions
- **Migration Path** — for Hold entries: what to migrate to and recommended timeline

## Field Reference

| Field | Type | Values | Notes |
|---|---|---|---|
| `id` | string | `THR-NNN` (e.g. THR-001) | Allocated from `repo.json → technologyHorizon.nextId` |
| `name` | string | any | Technology, framework, pattern, or practice name |
| `category` | enum | Platform, Language, Framework, Pattern, Practice, Tool, Standard | Classification |
| `ring` | enum | Adopt, Trial, Assess, Hold | Current organisation position |
| `rationale` | string | any | One-line reason for ring placement |
| `pocEvidence` | string or null | path | Link to PoC research document |
| `linkedADRs` | array | ADR-NNN | Decisions referencing this technology |
| `linkedVDRs` | array | VDR-NNN | Vendors implementing this technology |
| `linkedABBs` | array | ABB-NNN | ABBs this technology can implement |
| `ringHistory` | array | objects | Ordered list of ring changes with date, from, to, reason |
| `reviewDate` | ISO date | YYYY-MM-DD | Next scheduled ring review |
| `addedDate` | ISO date | YYYY-MM-DD | When first added to radar |

## Index File

`Architecture-Repository/technology-horizon/horizon-index.md` — maintained by `/ea-horizon`:

```markdown
# Technology Horizon Register Index

| ID | Name | Category | Ring | Rationale | Review Date |
|---|---|---|---|---|---|
| THR-001 | ... | ... | Adopt | ... | ... |
```
