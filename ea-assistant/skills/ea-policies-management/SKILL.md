---
name: ea-policies-management
description: This skill should be used when the user asks to "manage architecture policies", "add a policy", "view policies", "trace a policy to constraints", "update the policies register", or "assess policy impact". Handles the full policy lifecycle from capture through traceability and linkage to constraints.
version: 0.9.88
---

# EA Policies Management

Architecture Policies Management captures, classifies, traces, and manages formal governance documents and mandates that authorise constraints. Policies are distinct from principles (internal decision filters), constraints (binding restrictions), and requirements (verifiable outcomes).

## Policies Storage

Local policies are stored in `EA-projects/{slug}/artifacts/cross-cutting/governance/policies-register.md`:

```
artifacts/cross-cutting/governance/
├── policies-register.md   # human-readable policies register (stable filename; superseded versions in snapshots/)
```

The `policies` array in `engagement.json` stores metadata and links for fast lookup.

## Policies Register Format

`policies-register.md` uses a structured template:

```markdown
# Architecture Policies Register

**Engagement:** {{engagement_name}}
**Last Synced:** {{last_sync_date}}
**Version:** {{version}}

---

## 🔒POL-001: {{policy_title}}   ← Enterprise example

| Field | Value |
|---|---|
| **ID** | POL-001 |
| **Title** | {{policy_title}} |
| **Type** | Security / Procurement / Data Governance / Technology / Compliance / HR / Operational |
| **Issuing Authority** | {{authority_name}} |
| **Effective Date** | {{YYYY-MM-DD}} |
| **Review Cycle / Expiry** | {{YYYY-MM-DD or "Annual" / "Biennial"}} |
| **Scope of Authority** | Enterprise 🔒 / Divisional / Geographic |
| **Statement** | {{summary_of_what_the_policy_mandates}} |
| **Document Reference / URL** | {{link_to_policy_document}} |
| **Linked Constraints** | {{CST-NNN IDs}} |
| **Linked Principles** | {{principle_names_or_ids}} |
| **Status** | Draft / Enacted / Under Review / Superseded (by POL-NNN) / Retired |

---

## POL-00N: {{policy_title}}   ← Divisional example

| Field | Value |
|---|---|
| **ID** | POL-00N |
| **Title** | {{policy_title}} |
| **Type** | Security / Procurement / Data Governance / Technology / Compliance / HR / Operational |
| **Issuing Authority** | {{authority_name}} |
| **Effective Date** | {{YYYY-MM-DD}} |
| **Review Cycle / Expiry** | {{YYYY-MM-DD or "Annual" / "Biennial"}} |
| **Scope of Authority** | Divisional / Geographic |
| **Statement** | {{summary_of_what_the_policy_mandates}} |
| **Document Reference / URL** | {{link_to_policy_document}} |
| **Linked Constraints** | {{CST-NNN IDs}} |
| **Linked Principles** | {{principle_names_or_ids}} |
| **Status** | Draft / Enacted / Under Review / Superseded (by POL-NNN) / Retired |
```

## Engagement.json Schema

Policies are tracked in `engagement.json` under the **top-level `policies[]` array** (a governance register, sibling to `metrics[]`/`finance[]` — not inside `direction`):

```json
{
  "policies": [
    {
      "id": "POL-001",
      "title": "",
      "type": "Security | Procurement | Data Governance | Technology | Compliance | HR | Operational",
      "issuingAuthority": "",
      "effectiveDate": "YYYY-MM-DD",
      "reviewCycle": "YYYY-MM-DD",
      "scope": "Enterprise | Divisional | Geographic",
      "status": "Draft | Enacted | Under Review | Superseded | Retired",
      "supersededBy": "",
      "linkedConstraints": [],
      "linkedPrinciples": [],
      "sourceFile": "policies-register.md"
    }
  ]
}
```

## Enterprise Edit Protection

For `Scope: Enterprise` policies:
- **Read-only fields:** `title`, `type`, `issuingAuthority`, `effectiveDate`, `statement`
- **Editable fields:** `status`, `linkedConstraints`, `linkedPrinciples`, `reviewCycle`, `documentReference`
- Enforce `supersededBy` field when `status` is `Superseded`

## Traceability

Policies trace to:
- **Constraints** they generate (via `linkedConstraints`)
- **Principles** derived from or aligned with them (via `linkedPrinciples`)
- **SBBs** indirectly — through linked CST-NNN constraints that bound SBB selection
- **Artifacts** that must respect the constraints derived from this policy

## Policy Lifecycle

```
Draft → Enacted → Under Review → Superseded (by POL-NNN) → Retired
```

- **Draft:** Policy captured but not yet enacted. May have linked constraints in draft status.
- **Enacted:** Policy is binding. All linked constraints should be Active.
- **Under Review:** Policy is being reassessed. Linked constraints remain Active but may need revalidation.
- **Superseded:** Policy replaced by a newer policy. Update `supersededBy` field. Linked constraints should be reviewed for migration to the new policy.
- **Retired:** Policy is no longer binding. All linked constraints should be reviewed for waiver or retirement.

## Stale Policy Check

A policy is **stale** when:
- `status` = Enacted AND `reviewCycle` date is in the past
- `status` = Under Review AND review has been open for > 90 days

Stale policies are flagged in `/ea-policies list` and may invalidate linked constraints.
