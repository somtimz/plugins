# engagement.json Schema Reference

This reference describes the `engagement.json` schema used by the EA Assistant. The canonical JSON schema lives in [`engagement-schema/engagement-schema.json`](engagement-schema/engagement-schema.json); this page provides commentary and usage rules. Per-version field history lives in [`engagement-schema/field-version-history.md`](engagement-schema/field-version-history.md) so routine callers don't pay for it.

---

## Quick Navigation

| Topic | Section |
|---|---|
| Full schema example | [`engagement-schema.json`](engagement-schema/engagement-schema.json) |
| Versioning rules | [Schema Versioning & Source of Truth](#schema-versioning--source-of-truth) |
| Field history by plugin version | [engagement-schema/field-version-history.md](engagement-schema/field-version-history.md) |
| `artifacts[]` entry shape | [Artifact Entry Schema](#artifact-entry-schema) |
| `optOuts[]` shape | [optOuts Entry Schema](#optouts-entry-schema) |
| Cross-cutting artifact paths | [Cross-cutting Artifact Paths](#cross-cutting-artifact-paths) |
| Decision register entry | [Decision Register Entry Schema](#decision-register-entry-schema) |

---

## Schema Versioning & Source of Truth

**`schemaVersion`** (integer, current: **1**) tracks the structure of `engagement.json` itself, independent of the plugin version (`pluginVersion` tracks which plugin release last touched the engagement; `lastMigratedVersion` tracks the last `/ea-migrate` alignment). Increment the schema version only when the JSON structure changes incompatibly (renamed/moved keys, changed types) — additive fields do not bump it. Engagements without the field are pre-versioning; `/ea-migrate` adds it.

**`migrations[]`** is the audit trail: `/ea-migrate` appends one entry per run — `{ date, fromPluginVersion, toPluginVersion, fromSchemaVersion, toSchemaVersion, gapsFound, gapsFixed, gapsSkipped }`. Never edit or prune entries manually.

**Source of truth:** `engagement.json` is the single source of truth for the strategic direction (`direction.{vision, mission, drivers, goals, objectives, strategies, issues, problems, opportunities, gaps}`), the top-level governance/measurement registers (`metrics[]`, `policies[]`, `finance[]` — siblings of `direction`, not nested in it), phase state, and the artifact registry. Generated register markdown files (`*-register.md`) are **rendered views** — regenerate them after any change; never edit them to change state (the exceptions are registers whose content lives only in markdown: Risk, Requirements, Constraints, Policies registers, which are file-mastered with `engagement.json` holding metadata). Snapshot files under `snapshots/` are point-in-time archives per the register snapshot convention.

**Operating Model artifact storage:** The Operating Model is an **authored Phase B artifact** (`artifacts/phase-b/operating-model.md`) tracked in `engagement.json → artifacts[]`. It has no dedicated top-level array: structured business processes live in `businessProcesses[]`, service delivery notes in `services[]`, and org design / decision rights / controls / sourcing / workforce content in the artifact body. This keeps the OM artifact free-form while reusing the existing registers for mastered items.

For per-version field shapes, valid enum values, defaults, and migration notes, see [`engagement-schema/field-version-history.md`](engagement-schema/field-version-history.md).

---

## Artifact Entry Schema

```json
{
  "id": "architecture-vision",
  "name": "Architecture Vision",
  "phase": "A",
  "file": "artifacts/phase-a/architecture-vision.md",
  "reviewFile": "artifacts/phase-a/architecture-vision.review.md",
  "status": "Draft",
  "createdAt": "YYYY-MM-DDTHH:MM:SSZ",
  "lastModified": "YYYY-MM-DDTHH:MM:SSZ",
  "reviewStatus": "Not Reviewed",
  "scores": { "completeness": 78, "quality": 66, "scoredAt": "YYYY-MM-DD" }
}
```

Artifact status: `Draft` | `In Review` | `Approved` | `Needs Revision`

**`scores`** (v0.9.72; optional, absent until first scored): the latest overall artifact scores from `/ea-score` or `/ea-grill` — `completeness` and `quality` are `0–100` integers, `scoredAt` is the date last scored. The per-section breakdown lives in the artifact's `📊 Scorecard` block (the source of truth); this is the roll-up cache for `/ea-score --status` and `/ea-status`. Command-generated artifacts (registers/matrices/derived) are not scored and have no `scores` field.
Review status: `Not Reviewed` | `In Review` | `Approved` | `Needs Revision`

## optOuts[] Entry Schema

```json
{
  "type": "question | artifact",
  "artifactId": "architecture-vision",
  "questionRef": "executive_summary",
  "reason": "Not yet available — revisit in Phase A review",
  "timestamp": "ISO 8601"
}
```

- `questionRef` — placeholder key (question opt-outs only)
- Opt-outs accumulate across sessions; never auto-removed
- Removal permitted only via `/ea-config optouts`

## Cross-cutting Artifact Paths

Cross-cutting artifacts are organized into three sub-folders under `artifacts/cross-cutting/`:

| Sub-folder | Artifacts stored |
|---|---|
| `artifacts/cross-cutting/governance/` | ADR Register, Decision Register, Architecture Principles (cross-cutting), Constraints Register, Policies Register |
| `artifacts/cross-cutting/operations/` | Risk Register, Change Register, Stakeholder Concerns, Cost Model Register |
| `artifacts/cross-cutting/context/` | Zachman Diagram, Role Catalogue |

The `cross-cutting-index.md` file at `artifacts/cross-cutting/cross-cutting-index.md` is a navigation hub linking to all cross-cutting artifacts. It is created on first use and updated whenever a new cross-cutting artifact is registered.

## Decision Register Entry Schema

A single decision register entry exists at the stable path (superseded versions are archived to `snapshots/` per the register snapshot convention):

```json
{
  "id": "decision-register",
  "name": "Decision Register",
  "phase": "All",
  "file": "artifacts/cross-cutting/governance/decision-register.md",
  "reviewFile": "artifacts/cross-cutting/governance/decision-register.review.md",
  "status": "Draft",
  "createdAt": "{ISO 8601}",
  "lastModified": "{ISO 8601}",
  "reviewStatus": "Not Reviewed"
}
```

`/ea-decisions status` uses the current `decision-register.md` for its summary.
