---
name: ea-drivers
description: Manage business drivers — list, add, update, trace to goals and work packages, and generate a drivers register
argument-hint: "[list|add|update|trace|generate] [DRV-NNN] [--type External|Internal] [--priority High|Medium|Low]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-drivers` command. Load the `ea-drivers-management` skill for schema and traceability detail. All mode mechanics follow `skills/ea-engagement-lifecycle/references/register-protocol.md` — read it, then apply the Register Spec below. For the Business Driver concept and its distinctions, read `ea-concepts.md`; do not restate definitions here.

Drivers sit at the top of the motivation chain (DRV → G → OBJ → STR → WP). Every goal should trace to at least one driver; every driver should have at least one linked goal.

## Register Spec

| Element | Value |
|---|---|
| Prefix / concept | `DRV-NNN` — Business Driver |
| Storage | `engagement.json → direction.drivers[]` |
| Register file | `artifacts/cross-cutting/drivers-register.md` (artifactId `drivers-register`) |
| Display view | Architecture Vision `§2 Business Drivers` — columns `ID \| Driver \| Type \| Force \| Impact on Strategy \| Linked Goals \| Evidence / Source \| Details` ← `id, statement, type, —, —, linkedGoals, evidence` |
| Groupings | `list` and `generate` group by Type (External first); summary counts by Priority, plus "Orphans (no linked goal)" and "No evidence" |
| Orphan rule | No linked goals → `⚠️ Orphan` |

### Fields

| Field | Prompt | Valid values | Req |
|---|---|---|---|
| `statement` | The business pressure or imperative (e.g. "Regulatory mandates for data residency in the EU by 2027") | any string | ✓ |
| `type` | Type | External / Internal | ✓ |
| `priority` | Priority | High / Medium / Low | ✓ |
| `evidence` | Source document, metric, or external reference | any string or URL | opt (absence flagged `⚠️ No evidence cited`) |
| `linkedGoals` | Linked Goals (list available G-NNN) | comma-separated G-NNN | opt |

### Link fields

| Field | Target | Orphan semantics |
|---|---|---|
| `linkedGoals` | `direction.goals[]` | No goals → orphan flag: "run `/ea-drivers trace` to review" |

### Trace chain

| Direction | Hop | Source |
|---|---|---|
| Downstream | Goals | `direction.goals[]` where `drivers` contains this DRV-NNN |
| Downstream | Objectives | `direction.objectives[]` where `linkedGoal` is in the goal set |
| Downstream | Strategies | `direction.strategies[]` where `supports` intersects the goal/objective set |
| Downstream | Work Packages | Architecture Roadmap WP rows where `Advances Goals/Objectives` or `Executes Strategies` references any found ID |

Drivers have no status field — they are present (active) or removed. Before removing a driver, check for goals referencing it and offer to update those goals first (see `ea-drivers-management`).

## Messages

- **Empty state:** "No drivers found. Capture drivers during engagement-level interviews (`/ea-interview start engagement`) or `/ea-brainstorm`, then add them with `/ea-drivers add`."
- **Add success:** "DRV-NNN added. Use '/ea-drivers trace DRV-NNN' to verify goal linkage."
- **Orphan nudge:** "⚠️ No goals linked. Consider running `/ea-drivers update DRV-NNN linkedGoals G-NNN` after capturing goals."
