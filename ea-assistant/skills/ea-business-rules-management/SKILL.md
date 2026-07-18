---
name: ea-business-rules-management
description: This skill should be used when the user asks to "manage business rules", "add a business rule", "view business rules", "trace a rule to services or motivation", "update the business rules register", or "assess rule impact". Handles the full business-rule lifecycle from capture through traceability and linkage to services, policies, constraints, and motivation elements.
version: 0.9.87
---

# EA Business Rules Management

This skill manages `BR-NNN` entries. Load `skills/ea-artifact-templates/references/ea-concepts.md` for the canonical **Business Rule** and **Service** definitions before prompting for or validating any rule.

## Business Rules Storage

Local business rules are stored in `EA-projects/{slug}/artifacts/cross-cutting/operations/business-rules-register.md`:

```
artifacts/cross-cutting/operations/
├── business-rules-register.md   # human-readable business rules register (stable filename; superseded versions in snapshots/)
```

The `rules` array in `engagement.json` stores metadata and links for fast lookup.

## Business Rules Register Format

`business-rules-register.md` uses a structured template:

```markdown
# Business Rules Register

**Engagement:** {{engagement_name}}
**Last Synced:** {{last_sync_date}}
**Version:** {{version}}

---

## 🔒BR-001: {{rule_subject}}   ← Enterprise example

| Field | Value |
|---|---|
| **ID** | BR-001 |
| **Subject** | {{subject}} |
| **Condition** | {{condition}} |
| **Directive** | Must / Must Not / Should / Should Not |
| **Outcome** | {{outcome}} |
| **Authority** | {{authority}} |
| **Source** | Regulatory / Internal / Contractual / Market Practice / Policy-derived |
| **Enforcement** | Manual review / Automated check / Workflow approval / Audit sample / System validation |
| **Scope** | Enterprise 🔒 / Program |
| **Status** | Active / Draft / Under Review / Superseded (by BR-NNN) / Retired |
| **ADM Phase** | {{phase}} |
| **Zachman Cell** | {{zachman_cell}} |
| **Linked Business Services** | {{SVC-NNN IDs}} |
| **Linked Business Processes** | {{PROC-NNN IDs}} |
| **Linked Use Cases** | {{UC-NNN IDs}} |
| **Linked Policies** | {{POL-NNN IDs}} |
| **Linked Constraints** | {{CST-NNN IDs}} |
| **Trace to Motivation** | {{DRV/G/OBJ/STR IDs}} |

---

## BR-00N: {{rule_subject}}   ← Program example

| Field | Value |
|---|---|
| ... | ... |
```

## Engagement.json Schema

Business Rules are tracked in `engagement.json` under the **top-level `rules[]` array** (a governance register, sibling to `metrics[]`, `policies[]`, `finance[]`, `services[]` — not inside `direction`):

```json
{
  "rules": [
    {
      "id": "BR-001",
      "subject": "",
      "condition": "",
      "directive": "Must | Must Not | Should | Should Not",
      "outcome": "",
      "authority": "",
      "source": "Regulatory | Internal | Contractual | Market Practice | Policy-derived",
      "enforcement": "Manual review | Automated check | Workflow approval | Audit sample | System validation",
      "scope": "Enterprise | Program",
      "status": "Active | Draft | Under Review | Superseded | Retired",
      "supersededBy": "",
      "admPhase": "Prelim | A | B | C-Data | C-App | D | E | F | G | H | Requirements",
      "zachmanCell": "",
      "linkedServices": [],
      "linkedProcesses": [],
      "linkedUseCases": [],
      "linkedPolicies": [],
      "linkedConstraints": [],
      "linkedMotivation": [],
      "sourceFile": "business-rules-register.md"
    }
  ]
}
```

## Enterprise Edit Protection

For `Scope: Enterprise` rules:
- **Read-only fields:** `subject`, `condition`, `directive`, `outcome`, `authority`, `source`
- **Editable fields:** `status`, `supersededBy`, `linkedServices`, `linkedPolicies`, `linkedConstraints`, `linkedMotivation`, `enforcement`, `zachmanCell`, `admPhase`
- Enforce `supersededBy` field when `status` is `Superseded`

## Traceability

Business Rules trace to:
- **Business Services** that operationalise the rule (`linkedServices`)
- **Policies** that authorise the rule (`linkedPolicies`)
- **Constraints** derived from or enforcing the rule (`linkedConstraints`)
- **Motivation elements** — drivers, goals, objectives, strategies (`linkedMotivation`)
- **Capabilities / ABB / SBB** indirectly — through linked services

## Business Rule Lifecycle

```
Draft → Active → Under Review → Superseded (by BR-NNN) → Retired
```

- **Draft:** Rule captured but not yet active. Links may be incomplete.
- **Active:** Rule is operational and must be enforced by linked services or processes.
- **Under Review:** Rule is being reassessed. Linked services remain active but may need revalidation.
- **Superseded:** Rule replaced by a newer rule. Update `supersededBy`. Linked services/constraints should be reviewed for migration.
- **Retired:** Rule is no longer operational. Linked services/constraints should be reviewed for removal or waiver.

## Capture Guidance

When prompting for a new rule:
1. **Subject first** — the business entity or process governed.
2. **Condition** — when the rule applies. Be specific enough to test.
3. **Directive** — Must / Must Not / Should / Should Not.
4. **Outcome** — the business result or action.
5. **Authority** — who owns the rule (prefer a POL-NNN or named governance role).
6. **Source** — Regulatory / Internal / Contractual / Market Practice / Policy-derived.
7. **Enforcement** — how compliance is verified.
8. **Scope** — Enterprise (read-only core) / Program (engagement-specific interpretation).
9. **Trace links** — offer existing SVC-NNN, POL-NNN, CST-NNN, DRV/G/OBJ/STR IDs from `engagement.json`.

## Validation Checks

- `directive` must be one of: `Must`, `Must Not`, `Should`, `Should Not`.
- `source` must be one of the allowed enum values.
- `enforcement` must be one of the allowed enum values.
- A rule with `status: Active` requires non-empty `authority` and `enforcement`.
- Linked IDs must exist in the engagement; flag broken references in `trace` and `list`.
- A rule with no linked service, process, use case, policy, constraint, or motivation element is an **orphan** — flag in `list` and suggest `/ea-rules update BR-NNN linkedServices`, `linkedProcesses`, `linkedUseCases`, or `linkedMotivation`.

## Maturity Marker

- **L1:** Rules scattered as free-text in process documents.
- **L3:** Rules catalogued with condition/directive/outcome and linked to services.
- **L5:** Rules versioned, traced to automated decision services, and validated by conformance tests.
