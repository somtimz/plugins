# engagement.json Write Protocol

Multiple agents and commands write to `engagement.json`. To prevent silent overwrites, each owns a specific section:

| Section | Owner |
|---|---|
| `name`, `slug`, `description`, `sponsor`, `organisation`, `scope`, `startDate`, `targetEndDate`, `status`, `engagementType`, `architectureDomains`, `requirementsRepoPath`, `lastModified` | `/ea-open` (metadata edits) and `/ea-new` (creation) |
| `currentPhase` | `ea-facilitator` (on phase advance) |
| `phases[*].status`, `phases[*].startedAt`, `phases[*].completedAt` | `ea-facilitator` (on phase transition) |
| `artifacts[*].status`, `artifacts[*].reviewStatus`, `artifacts[*].lastModified` | `ea-interviewer` and `/ea-open` artifact edit |
| `artifacts[]` (add new entry) | The command or agent that creates the artifact (e.g. `/ea-artifact`, `ea-roadmap`) |
| `direction` | `/ea-open` metadata edit; `ea-interviewer` (during interviews when explicitly prompted) |
| `metrics` | `/ea-open` metadata edit |
| `optOuts[]` | `ea-interviewer` only (append only — never remove); removal via `/ea-config optouts` only |
| `analysis_runs` | `ea-requirements-analyst` only |

## Rules

- Always read `engagement.json` fresh before writing — never write from a stale in-memory copy
- Write only the section you own; do not touch other sections
- Update `lastModified` (engagement-level) on every write
- Never delete existing entries from `optOuts[]`, `artifacts[]`, or `analysis_runs` — append only

---

## Post-Artifact-Save Sequence

Every agent or command that writes or updates an artifact `.md` file in `artifacts/**/*.md` must run this sequence immediately after the write succeeds. It does **not** apply to read-only operations, or to generated register files (risk-register, adr-register, change-register, zachman-diagram).

**Triggers:** `ea-interviewer` after recording answers · `/ea-artifact create` or update · `/ea-grill` after applying a finding revision · `/ea-review` after updating review status

### Step A — Compliance check (silent, automatic)

Apply Tier 1/2/3 rules from `skills/ea-artifact-templates/references/compliance-check.md`.

**If no failures** — show a clean confirmation and proceed to Step B:
```
✓ {artifact-name} saved.
```

**If failures found** — surface them before offering further options:
```
✓ {artifact-name} saved.

⚠️  Compliance issues found:
  [T1] Missing required frontmatter field: reviewStatus
  [T3] Appendix A3 — Decision Log section absent

  Fix compliance issues now? (y / n / view details)
```

- `y` — remediate inline using the "Achieve compliance" logic (add missing fields/sections; preserve all existing content); then proceed to Step B
- `n` — record `complianceNote: accepted-non-standard` in frontmatter; proceed to Step B
- `view details` — show the full compliance report; re-prompt `y / n`

### Step B — Consistency and review options

Always show after Step A (whether clean or after compliance is resolved/skipped):

```
  1. Check this artifact for consistency   →  /ea-consistency artifact {id}
  2. Run a full engagement review          →  /ea-engage-review
  3. Continue
```

- Option 1: invoke `/ea-consistency artifact {id}` inline; do not navigate away from the current workflow
- Option 2: hand off to `/ea-engage-review`
- Option 3 (or Enter): continue with the current workflow
