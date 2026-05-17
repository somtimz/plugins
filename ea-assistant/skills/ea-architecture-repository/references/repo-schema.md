# Architecture Repository Schema

## workspace.json fields

| Field | Type | Description |
|---|---|---|
| `name` | string | Workspace display name |
| `organisation` | string | Owning organisation |
| `version` | string | Schema version (start: "1.0.0") |
| `createdDate` | ISO date | When workspace was initialised |
| `lastModified` | ISO datetime | Last update timestamp |
| `repoPath` | string | Relative path to Architecture-Repository/ (always "Architecture-Repository") |
| `projectsPath` | string | Relative path to EA-Projects/ (always "EA-Projects") |
| `projects` | array | List of EA engagements in this workspace |

`projects` array entry:
```json
{ "slug": "", "name": "", "path": "EA-Projects/<slug>", "status": "Active", "linkedDate": "YYYY-MM-DD" }
```

## repo.json fields

| Field | Type | Description |
|---|---|---|
| `name` | string | Repository display name |
| `organisation` | string | Owning organisation |
| `description` | string | Purpose and scope |
| `version` | string | Schema version (start: "1.0.0") |
| `createdDate` | ISO date | When repo was initialised |
| `lastModified` | ISO datetime | Last update timestamp |
| `owner` | object | `{ name, email, role }` — Architecture Repository Owner (ROLE-003) |
| `linkedEngagements` | array | `[{ slug, name, path, linkedDate }]` — EA project slugs using this repo |
| `linkedProjects` | array | `[{ id, name, path, type }]` — IT project references |
| `governance` | object | `{ enterprisePrinciplesFile, enterprisePoliciesFile, enterpriseConstraintsFile }` |
| `sib` | object | `{ enabled: bool, indexFile: "sib/sib-index.md", nextId: 1 }` |
| `vendorLandscape` | object | `{ enabled: bool, indexFile: "vendor-landscape/vendor-index.md", nextId: 1 }` |
| `technologyHorizon` | object | `{ enabled: bool, indexFile: "technology-horizon/horizon-index.md", nextId: 1 }` |

## Directory Structure (produced by /ea-repo init)

```
EA-Workspace/
├── workspace.json                    # workspace root — created by /ea-repo init
├── Architecture-Repository/
│   ├── repo.json
│   ├── governance/
│   │   ├── enterprise-principles.md
│   │   ├── enterprise-policies.md
│   │   └── enterprise-constraints.md
│   ├── sib/
│   │   ├── sib-index.md
│   │   └── standards/
│   ├── vendor-landscape/
│   │   ├── vendor-index.md
│   │   └── entries/
│   ├── technology-horizon/
│   │   ├── horizon-index.md
│   │   └── entries/
│   └── reference-library/
│       └── abb-catalogue.md
└── EA-Projects/                      # engagement projects go here
```

`repoPath` in `engagement.json` is always relative: `../../Architecture-Repository` (from `EA-Projects/<slug>/`).
