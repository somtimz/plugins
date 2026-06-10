---
name: ea-principles-management
description: Principles lifecycle management — ID assignment, traceability to policies and constraints, violation detection
version: 0.9.60
allowed-tools: [Read, Grep, Glob]
---

## Purpose

This skill provides the reference logic for managing Architecture Principles (BP/DP/AP/TP-NNN) across the engagement. It is loaded by `/ea-principles` and by `/ea-grill` when reviewing the Architecture Principles artifact or the Architecture Vision.

---

## 1. ID Assignment Rules

Principles use four domain-scoped prefixes (TOGAF standard):

| Type | Prefix | Example | Scope |
|---|---|---|---|
| Business Principle | BP | BP-001 | Governs business strategy, operating model, and value-stream decisions |
| Data Principle | DP | DP-001 | Governs data management, quality, sovereignty, and classification decisions |
| Application Principle | AP | AP-001 | Governs application design, integration patterns, and coupling decisions |
| Technology Principle | TP | TP-001 | Governs infrastructure, platform, and vendor selection decisions |

**Assignment rule:** scan existing entries for the highest N in that prefix group; assign N+1 zero-padded to 3 digits (e.g. existing: BP-001, BP-002 → next: BP-003).

IDs are assigned once and never reused. If a principle is deprecated, its ID remains in the file with `Status: Deprecated`.

---

## 2. Principle Structure (Required Fields)

Every principle entry must have all four TOGAF-required fields. A principle missing any of these is **structurally incomplete** and must be flagged in reviews.

| Field | Purpose | Quality test |
|---|---|---|
| **Name** | Short label (2–5 words) | Can a reader guess the rule from the name alone? |
| **Statement** | The normative rule — one sentence, starting with a modal verb (must/shall/will/should) | Is it normative? Testable? Unambiguous? Free of implementation detail? |
| **Rationale** | Why this rule exists (1–3 sentences) | Does it explain the business driver, risk, or policy mandate? |
| **Implications** | What following this rule requires or prohibits in practice | Are at least some implications specific enough to detect a violation? |

**Optional fields:**
- **Source Policy** — POL-NNN: the governance document that mandates this principle
- **Status** — Active / Draft / Deprecated (default: Active)

---

## 3. Traceability Hierarchy

Architecture Principles sit at the second level of the governance cascade:

```
Policy (POL-NNN)
    └── Principle (BP/DP/AP/TP-NNN)      ← "Source Policy" field in principle
            └── Constraint (CST-NNN)      ← "Source" field in constraint
                    └── Solution (ABB-NNN / SBB-NNN)
                            └── User Story (STY-NNN)
```

- A principle **without** a source policy is self-grounded (valid, but note in reviews).
- A constraint **without** a source principle may be under-justified — flag in consistency checks.
- An ADR that selects a solution must not contradict the principle governing its domain.

**Tracing rules:**
- Principles → Constraints: match `Source` field in `constraints-register.md` to principle ID or name
- Principles → ADRs: grep ADR files for the principle ID (e.g. `BP-001`) in body or `## Related Principles` section
- Principles → Artifacts: grep all phase artifacts for the principle ID

---

## 4. Violation Detection Heuristics

When scanning for principle violations in completed ADRs and A3 decision rows, look for these patterns:

| Principle domain | Violation signal | Example |
|---|---|---|
| Technology Independence (TP) | ADR selects a proprietary API or single-vendor lock-in with no abstraction layer or exit strategy noted | "Decided to use vendor-specific messaging queue with no abstraction" |
| Data Sovereignty (DP) | Data residency constraint waived or PII moved cross-border without a POL reference | "Exception: store EU customer data in US region" with no governance link |
| Loose Coupling (AP) | Decision mandates synchronous point-to-point integration between bounded services | "All order services must call the billing service directly" |
| Reuse Before Buy Before Build (AP/TP) | ADR selects net-new build when existing capability or COTS option was not evaluated | Rationale section shows no alternatives for reuse or procurement |
| Business principle | Decision bypasses a stated business rule | Principle: "Customer data is never monetised" but ADR approves a data-sharing agreement |

Report each candidate violation as:
> ⚠️ **{ID} may be violated by {ADR-NNN}:** {one-line reason} — review required.

These are candidates, not confirmed violations — a human must review each flag.

---

## 5. Compliance Checks (for `/ea-grill`)

When `/ea-grill` reviews an Architecture Principles artifact, apply these checks in order:

| # | Check | Criterion | Severity |
|---|---|---|---|
| C1 | All four fields present | Name + Statement + Rationale + Implications | Blocking |
| C2 | Statement is normative | Starts with "must", "shall", "will", or "should" | Warning |
| C3 | Statement is free of implementation detail | Does not name a specific product, vendor, or technology | Warning |
| C4 | Rationale references a driver or policy | Links to DRV-NNN or POL-NNN, or names a specific risk | Advisory |
| C5 | Implications are testable | At least one implication describes a detectable prohibited behaviour | Advisory |
| C6 | Domain coverage | At least one Active principle per engaged domain (B/D/A/T) | Warning |
| C7 | Principle count per domain | Typically 5–12 per domain; flag if > 15 in one domain | Advisory |
| C8 | Orphaned principles | Any principle with no linked constraint or ADR | Advisory |

---

## 6. Cross-Command Integration

When these commands execute, load this skill for the relevant logic:

| Triggering command | What to apply |
|---|---|
| `/ea-principles list` | Section 4 violation detection; Section 5 C8 (orphaned check) |
| `/ea-principles add` | Section 1 (ID assignment); Section 2 (field validation prompts) |
| `/ea-principles trace` | Section 3 (traceability rules); Section 4 (violation detection) |
| `/ea-grill` on architecture-principles artifact | All of Section 5 compliance checks |
| `/ea-constraints add` | Section 3 — when Source is prompted, offer to link to an existing principle |
| `/ea-policies trace` | Section 3 — when tracing a policy, show principles that cite it as Source Policy |
| `/ea-adrs new` | Section 3 — prompt "Which principles govern this decision?" and record in ADR |
| `/ea-engage-review` | Section 5 — include principle compliance in the health report |
