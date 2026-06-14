---
name: ea-issues
description: Manage architecture issues — list, add, update, trace to goals and gaps, and generate an Issues Register
argument-hint: "[list|add|update|trace|generate] [ISS-NNN] [--domain Business|Technology|Data|Application|Engagement] [--type Organisational|Process|Technology|Regulatory|Capability] [--severity Critical|High|Medium|Low] [--status Open|Under Mitigation|Resolved|Accepted]"
allowed-tools: [Read, Write, Bash]
---

You are executing the `/ea-issues` command. All mode mechanics follow `skills/ea-engagement-lifecycle/references/register-protocol.md` — read it, then apply the Register Spec below. For the Issue concept and its distinctions from Problem/Risk/Driver/Gap, read `ea-concepts.md`; do not restate definitions here.

Issues are systemic concerns threatening goals — present and ongoing, broad, with multiple contributing causes. The **Issues Register** is the management interface; the Architecture Vision (§5) summarises and links to it rather than rendering a live table. The **Engagement** domain covers issues about the EA engagement itself (methodology, governance, team, tooling).

## Register Spec

| Element | Value |
|---|---|
| Prefix / concept | `ISS-NNN` — Issue |
| Storage | `engagement.json → direction.issues[]` |
| Register file | `artifacts/cross-cutting/issues-register.md` (artifactId `issues-register`; relatedArtifacts `["architecture-vision"]`) |
| Seed template | `templates/phase-a/issues-register.md` (scored artifact; `generate` fills its Summary + per-domain item blocks) |
| Groupings | `list` and `generate` group by Domain (Engagement first, then Business, Technology, Data, Application); summary counts by Severity, Status, plus "No evidence" and "No goals" |
| Orphan rule | No linked goals → `⚠️ Orphan` |

### Fields

| Field | Prompt | Valid values | Req |
|---|---|---|---|
| `statement` | Name the systemic concern — what pattern of dysfunction, capability gap, or sustained barrier? | any string | ✓ |
| `domain` | Which area is primarily affected? | Business / Technology / Data / Application / Engagement | ✓ |
| `type` | Category | Organisational / Process / Technology / Regulatory / Capability | ✓ |
| `severity` | Severity | Critical / High / Medium / Low | ✓ |
| `status` | Status | Open / Under Mitigation / Resolved / Accepted (default Open) | ✓ |
| `threatensGoals` | Which goals does this issue put at risk? (list available G-NNN) | comma-separated G-NNN | ✓ |
| `evidence` | Observable signal, data point, or event confirming this issue is real (e.g. "Incident log: 12 P1 outages in 90 days") | any string | ✓ (recommended) |
| `raisedBy` | Stakeholder or source that surfaced this issue | any string | opt |

### Link fields

| Field | Target | Orphan semantics |
|---|---|---|
| `threatensGoals` | `direction.goals[]` | No goals → "link to a G-NNN or consider whether this is in scope" |

### Trace chain

| Direction | Hop | Source |
|---|---|---|
| Upstream | Related Drivers (contextual) | drivers linked to the goals this issue threatens |
| Threatens | Goals (show Priority) | `direction.goals[]` matching `threatensGoals` |
| Related | Problems contributing to this issue | `direction.problems[]` blocking objectives under the threatened goals |
| Downstream | Architecture Gaps this issue may feed | GAP-NNN entries (artifacts + `direction.gaps[]`) referencing this issue or its threatened goals |

### Status transitions

| Transition | Extra prompt |
|---|---|
| `status: Resolved` | "Resolution notes (optional):" |
| `status: Accepted` | "Acceptance rationale (required):" — do not proceed without rationale |

## Register-Specific Checks

**Issue vs Problem disambiguation (pre-add):**

```
Is this concern systemic and broad (affecting a domain or goal generally, with multiple contributing causes)?
Or is it specific, observable, and directly fixable (blocking a particular objective)?

(i) Issue — systemic, broad, multiple causes, sustained response needed
(p) Problem — specific, observable, directly fixable, blocks an objective
```

If (p): "Routing to `/ea-problems add` — use Problems for specific, fixable symptoms that block objectives." Stop.

**Specificity check (post-prompt, add):** If the statement contains a number, file name, or individual system name, warn:

```
⚠️  Your statement looks specific and measurable.
Issues are systemic — they describe a broad pattern, not a single event.
Example of an Issue: "Integration architecture lacks resilience and monitoring"
Example of a Problem: "The payment API returns 500 errors 3× per week"
Proceed as an Issue? (y/n)
```

**Escalation flag (`list`):** "🔴 {N} critical/high issue(s) are Open or Under Mitigation — review for escalation."

## Messages

- **Empty state:** "No issues found. Capture issues during interviews or `/ea-brainstorm`, then add them with `/ea-issues add`."
- **Add success:** "ISS-NNN added to engagement.json. Run `/ea-issues generate` to refresh the Issues Register, then '/ea-issues trace ISS-NNN' to verify goal linkage and check for related gaps."
- **Orphan nudge:** "⚠️ No goals linked. Use `/ea-goals list` to review goals, then `/ea-issues update ISS-NNN threatensGoals G-NNN`."
- **No-evidence flag:** "⚠️ {N} issue(s) have no evidence — unverified issues are assumptions, not confirmed concerns."
