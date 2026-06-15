---
name: ea-engagement-lifecycle
description: This skill should be used when the user asks to "start an EA engagement", "manage an EA project", "set up a new architecture engagement", "what phase are we in", "advance the ADM", "continue the engagement", "resume an EA project", or when working within any TOGAF ADM phase. Provides end-to-end lifecycle guidance for Enterprise Architecture engagements using TOGAF 10 as the backbone.
version: 0.9.81
---

# EA Engagement Lifecycle

This skill guides the management of Enterprise Architecture engagements from initiation through closeout using TOGAF 10 as the process backbone, with Zachman as the classification lens and ArchiMate as the notation language.

## Engagement Structure

Every EA engagement is stored as a folder under `EA-projects/`:

```
EA-projects/
├── {engagement-slug}/
│   ├── engagement.json
│   ├── CLAUDE.md                    # auto-generated pointer doc (refreshed on /ea-open)
│   ├── .claude/rules/ea-engagement.md  # persistent session guardrails
│   ├── artifacts/                   # phase-organized artifact files
│   │   ├── preliminary/             # Prelim: Architecture Principles, Engagement Charter
│   │   ├── requirements/            # Requirements: Register, Traceability Matrix
│   │   ├── phase-a/                 # Phase A: Architecture Vision, SAoW, Stakeholder Map
│   │   ├── phase-b/                 # Phase B: Business Architecture, Business Model Canvas, Gap Analysis
│   │   ├── phase-c-data/            # Phase C: Data Architecture, Gap Analysis (Data)
│   │   ├── phase-c-app/             # Phase C: Application Architecture, Gap Analysis (Application)
│   │   ├── phase-d/                 # Phase D: Technology Architecture, Gap Analysis (Technology)
│   │   ├── phase-e/                 # Phase E: Consolidated Gap Analysis, Architecture Roadmap, Transition Architectures
│   │   ├── phase-f/                 # Phase F: Migration Plan
│   │   ├── phase-g/                 # Phase G: Architecture Contract, Compliance Assessment
│   │   ├── phase-h/                 # Phase H: Change Request
│   │   └── cross-cutting/           # Cross-cutting: registers and context artifacts
│   │       ├── governance/          # ADR Register, Decision Register, Constraints, Policies, Principles
│   │       ├── operations/          # Risk Register, Change Register, Stakeholder Concerns, Cost Model Register
│   │       ├── context/             # Zachman Diagram, Role Catalogue
│   │       ├── notes/               # unscoped notes (no active phase)
│   │       └── cross-cutting-index.md  # navigation hub — links to all cross-cutting artifacts
│   ├── diagrams/
│   ├── uploads/
│   └── ResearchAndReferences/
└── .archive/
```

Each phase folder and `cross-cutting/` may contain a `workshops/` subfolder created on demand, containing `workshop-minutes-{WS-NNN}-{YYYY-MM-DD}.md` files (managed by `/ea-workshop`).

Each phase folder contains a `notes/` subfolder created on demand with three subdirectories:
- `notes/interviews/` — dated interview note files (`interview-{artifact-id}-{YYYY-MM-DD}-v{N}.md`)
- `notes/brainstorm/` — `brainstorm-notes.md` (one file per phase, seeded on first use)
- `notes/reviews/` — grill/review output files (`grill-{artifact-id}-{skill}-{YYYY-MM-DD}.md`)

Use `/ea-notes` to list, view, edit, or delete notes across all phases.

### Phase Folder Mapping

| Frontmatter `phase:` | Folder | Primary artifacts |
|---|---|---|
| `Prelim` | `artifacts/preliminary/` | Architecture Principles, Engagement Charter, Governance Framework |
| `Requirements` | `artifacts/requirements/` | Requirements Register, Traceability Matrix |
| `A` | `artifacts/phase-a/` | Architecture Vision, Statement of Architecture Work, Stakeholder Map |
| `B` | `artifacts/phase-b/` | Business Architecture, Business Model Canvas, Gap Analysis |
| `C-Data` | `artifacts/phase-c-data/` | Data Architecture, Gap Analysis (Data) |
| `C-App` | `artifacts/phase-c-app/` | Application Architecture, Gap Analysis (Application) |
| `D` | `artifacts/phase-d/` | Technology Architecture, Gap Analysis (Technology) |
| `E` or `E/F` | `artifacts/phase-e/` | Consolidated Gap Analysis, Architecture Roadmap, Transition Architectures |
| `F` | `artifacts/phase-f/` | Migration Plan |
| `G` | `artifacts/phase-g/` | Architecture Contract, Compliance Assessment, Implementation Governance Plan |
| `H` | `artifacts/phase-h/` | Change Request |
| `All` or `cross-cutting` — governance | `artifacts/cross-cutting/governance/` | ADR Register, Decision Register, Architecture Principles (cross-cutting), Constraints Register, Policies Register |
| `All` or `cross-cutting` — operations | `artifacts/cross-cutting/operations/` | Risk Register, Change Register, Stakeholder Concerns, Cost Model Register |
| `All` or `cross-cutting` — context | `artifacts/cross-cutting/context/` | Zachman Diagram, Role Catalogue |
| `{{phase}}` | resolve from `engagement.json → currentPhase` at creation time | Gap Analysis, ADRs |

### Artifact Link Conventions

From `artifacts/{phase-folder}/{artifact-id}.md`:

| Target | Relative path |
|---|---|
| Diagram file | `../../diagrams/{name}.{ext}` |
| Same-phase artifact | `./{artifact-id}.md` |
| Different-phase artifact | `../{phase-folder}/{artifact-id}.md` |
| Upload document | `../../uploads/{filename}` |
| Research document | `../../ResearchAndReferences/{filename}.md` |

Artifact frontmatter cross-reference fields: `relatedArtifacts: []`, `diagrams: []`, `links: []` — populate these so `/ea-engage-review` can trace dependencies without parsing body content.

## Reference Files

All static data is in `references/`. Read these rather than relying on memory:

- **`references/engagement-schema.md`** — full `engagement.json` schema with field definitions and version history
- **`references/phase-transitions.md`** — engagement/phase status values and state transition table with timestamp rules
- **`references/engagement-types.md`** — engagement type definitions, domain table, and ADM phase map
- **`references/write-protocol.md`** — ownership rules for each section of `engagement.json`
- **`references/facilitator-config.md`** — settings file format, style behaviour, and audience level reference
- **`references/adm-phase-guide.md`** — detailed inputs, outputs, and steps per ADM phase
- **`references/engagement-patterns.md`** — common patterns and anti-patterns
- **`references/scaffolding-map.md`** — engagement type/domain → artifact scaffolding mapping
- **`references/phase-inputs-outputs.md`** — input/output tables per phase with quality gates
- **`references/phase-constraints.md`** — plugin-level per-phase constraints: required artifacts, ID rules, traceability rules, and blocking gates; read by `ea-facilitator` on phase entry, `ea-interviewer` at session start, and `ea-consistency-checker` during validation
- **`references/adm-tailoring.md`** — tailoring ADM for agile, programme, capability, and security contexts
- **`references/ai-security-guidance.md`** — AI/GenAI security guidance for TOGAF ADM: ISO/IEC 42001 (AIMS), NIST AI RMF, and OWASP Top 10 for LLMs mapped per phase; load when the engagement involves AI or agentic systems, or when the user asks about AI security architecture
- **`references/role-catalogue.md`** — canonical role catalogue (ROLE-001 to ROLE-015): definitions, responsibilities, RACI defaults, triggering events, cadence, and escalation paths; read when populating the Stakeholder Map, SAoW §5, or the Role Catalogue artifact
- **`references/persona-registry.md`** — stakeholder personas (EA, CIO, CISO, Chief Product/Privacy Officer, Business/Data Architect): interests, command subset, report bundle, audience tags, entry workflow; read by `/ea-help --persona` and `/ea-publish --persona`
- **`references/arb-council-roster.md`** — the ARB Council: evaluative *voting* review viewpoints (planner, security, budget, architect, innovator, conservative), each with a mandate, anchored reuse, evaluation questions, and vote criteria; read by the `ea-arb-council` skill (`/ea-council`, `/ea-arb council`). **Three independent registries:** *roles* (`role-catalogue.md`) are RACI engagement participants; *personas* (`persona-registry.md`) are reporting/menu lenses mapped to the `audience` taxonomy; *council members* (this file) are evaluative voting viewpoints — never merge them (adding a council member to the persona registry would corrupt `/ea-publish` audience filtering)

## Lifecycle Workflow

### Starting a New Engagement

1. Collect: Name, Description, Sponsor, Organisation, Scope, Engagement Type, Architecture Level, Architecture Domains, Start Date, Target End Date (optional), Status
2. Generate slug: lowercase, hyphens, no spaces, max 60 chars
3. **Capture direction per selected domain.** For each domain:
   - Goals (`G-NNN`) — where you want to be (qualitative)
   - Objectives (`OBJ-NNN`) — specific measurable targets with a deadline
   - Strategies (`STR-NNN`) — approaches; each links to goal/objective IDs via `supports`
   - IDs are sequential across all domains (do not restart per domain)
   - Classify each item before recording; if ambiguous, ask the user
   - Direction may be skipped — user can add later via Edit engagement metadata
4. Optionally capture metrics. See `references/engagement-schema.md` for metric schema.
5. Display confirmation summary; allow edit or cancel
6. Create folder structure under `EA-projects/{slug}/` and seed files from `templates/seeds/`
7. Write `engagement.json` with all fields. Set phase applicability per `references/engagement-types.md` and `references/scaffolding-map.md`
8. Scaffold Preliminary phase artifacts (see `references/scaffolding-map.md`)
9. Set `currentPhase` to `Prelim`; confirm and offer to begin Preliminary phase

### Opening an Existing Engagement

1. Scan `EA-projects/*/engagement.json` (excludes `.archive/` dotdir)
2. Display picklist: name, engagement type, domain count, currentPhase, status, lastModified
3. If argument provided, match against names or slugs directly
4. Load selected engagement context; display full summary; offer next actions menu
5. Store the active engagement slug in conversation context

### Editing Workflows

All editing is accessed through `/ea-open` next actions menu.

- **Edit metadata** — name (display only), description, sponsor, organisation, scope, status, start date, target end date, direction, metrics. Non-editable after creation: `engagementType`, `architectureDomains`.
- **Edit direction** — add/edit/remove goals, objectives, strategies. IDs never reused. After saving, offer to propagate updated direction to relevant domain artifacts.
- **Edit metrics** — add/edit/remove metrics. Always confirm `supports` link; a metric without a linked direction item is an orphan. See `references/engagement-schema.md`.
- **Edit phase status** — apply state transition rules from `references/phase-transitions.md`. Suggest advancing `currentPhase` when a phase is marked Complete.
- **Edit artifact status** — status (Draft/In Review/Approved/Needs Revision) and review status.

### Archive, Restore, and Delete

- **Archive** — move `EA-projects/{slug}/` → `EA-projects/.archive/{slug}/`. Invisible in `/ea-status` and `/ea-open`.
- **Restore** — move back from `.archive/`. Blocked if active engagement with same slug exists.
- **Delete** — permanently remove. Requires user to type the slug to confirm.

### Advancing or Resuming a Phase

1. Update `currentPhase` in `engagement.json`
2. Update phase `status` to `In Progress`; set `startedAt` if first entry (see `references/phase-transitions.md`)
3. Read `references/phase-constraints.md` for the entering phase; surface any Blocking gaps to the user before starting work
4. Use: `ea-facilitator` agent for facilitation; `ea-artifact-templates` skill for artifacts; `ea-interviewer` agent for interviews; `/ea-publish` for export

### Completing a Phase

1. Verify all required artifacts exist in `artifacts/`
2. Set phase `status` to `Complete` and `completedAt` timestamp
3. Update `lastModified` in `engagement.json`; offer to advance to the next recommended phase

## Content Policy

Artifacts are populated from three sources only:
1. User interview answers
2. Uploaded documents (processed by `ea-document-ingestion` skill)
3. Explicit user input

Any AI-generated or suggested content MUST be marked:
```
> 🤖 **AI Draft — Review Required**
> [suggested content here]
```

Unanswered fields: `⚠️ Not answered`
Not applicable fields: `➖ Not applicable`
Default answers accepted by user: value written + `✓ Default accepted`

## Architecture Landscape Level

The `architectureLevel` field in `engagement.json` classifies the engagement by its scope and planning horizon. The four levels — `Strategic`, `Segment`, `Capability`, `Solution` — determine artifact depth expectations, governance forum, and ADM tailoring.

Load `references/landscape-levels.md` when:
- The user asks about artifact depth, section completeness, or what detail is expected
- The user asks which governance forum applies (ARB, portfolio board, project board)
- The user asks about ADM tailoring for their engagement type
- An artifact is being created or populated — check the Depth Expectation Matrix before starting

**Fallback rule:** When `architectureLevel` is `null` or absent in an existing engagement, treat it as `Segment` for artifact depth purposes. This is non-blocking. At the next `/ea-config` interaction, prompt the user to set it via `Section 6 — Engagement Metadata`.

## Architecture Repository

Engagements can optionally link to a shared Architecture Repository at the workspace level. When linked, `engagement.json → repoPath` is set to `"../../Architecture-Repository"` (relative from `EA-Projects/<slug>/`).

The linked repository provides:
- Standards Information Base (STD-NNN) — mandatory/recommended standards surfaced during phase interviews
- Vendor Landscape Register (VDR-NNN) — vendor context surfaced in `/ea-sbbs` and `/ea-adrs`
- Technology Horizon Register (THR-NNN) — technology radar surfaced during Phase D

Use `/ea-repo link <slug>` to link an engagement, or `/ea-new` inside an EA-Workspace to auto-link.
See skill `ea-architecture-repository` for full details.

## Write Protocol

See `references/write-protocol.md` for the full ownership table. Key rules:
- Always read `engagement.json` fresh before writing
- Write only the section you own
- Update `lastModified` on every write
- Never delete from `optOuts[]`, `artifacts[]`, or `analysis_runs` — append only
- For parallel agent dispatch, see `## Parallel Safety` in `write-protocol.md`
