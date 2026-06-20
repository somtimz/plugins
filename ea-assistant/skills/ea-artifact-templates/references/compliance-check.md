# Artifact Compliance Check — Reference

This reference defines what makes an EA artifact compliant with the current template standard, how to detect non-compliance, and what remediation options to offer the user. All commands that load or display an artifact MUST run this check before presenting the artifact for editing, review, or interview.

---

## What Is a Compliant Artifact?

A compliant artifact satisfies all rules in its applicable tier. Rules are additive — Tier 1 applies to all artifacts, Tier 2 to artifacts with rich templates, and Tier 3 to specific artifact types.

---

### Tier 1 — Universal (all artifacts)

These checks apply to every `.md` file in `artifacts/`:

| # | Rule | Compliant example | Non-compliant |
|---|---|---|---|
| T1-1 | Frontmatter block present (YAML between `---` delimiters) | `--- artifact: ... ---` | No frontmatter |
| T1-2 | `artifact` field present and non-empty | `artifact: Architecture Vision` | Missing or blank |
| T1-3 | `engagement` field present and non-empty | `engagement: Acme Retail` | Missing or blank |
| T1-4 | `phase` field present | `phase: A` | Missing |
| T1-5 | `status` field present with valid value | `status: Draft` | Missing or invalid value |
| T1-6 | `reviewStatus` field present with valid value | `reviewStatus: Not Reviewed` | Missing |
| T1-7 | `version` field present | `version: 0.1` | Missing |
| T1-8 | `lastModified` field present | `lastModified: 2026-03-26` | Missing |
| T1-9 | Document has at least one top-level heading | `# Architecture Vision` | No headings |
| T1-10 | `taxonomy` block present with `domain`, `category`, `audience`, `layer`, `sensitivity` | `taxonomy: domain: Cross-cutting ...` | Missing taxonomy block or missing sub-fields |
| T1-11 | `templateVersion` field present | `templateVersion: 0.9.5` | Missing — run `/ea-migrate` to add |

**Valid `status` values:** `Draft` | `In Review` | `Approved` | `Needs Revision`
**Valid `reviewStatus` values:** `Not Reviewed` | `In Review` | `Approved` | `Needs Revision`
**Valid `taxonomy.domain` values:** `Business` | `Data` | `Application` | `Technology` | `Cross-cutting`
**Valid `taxonomy.category` values:** `Strategy` | `Analysis` | `Design` | `Planning` | `Governance` | `Register`
**Valid `taxonomy.audience` values:** `Executive` | `Business` | `Architecture` | `Delivery` | `Governance` | `All`
**Valid `taxonomy.layer` values:** `Motivation` | `Baseline` | `Target` | `Transition` | `Governance` | `Reference`
**Valid `taxonomy.sensitivity` values:** `Internal` | `Confidential` | `Restricted`

See `references/taxonomy.md` for the canonical taxonomy definition and the full mapping table.

---

### Tier 2 — Standard template structure

Applies to artifacts created from plugin templates (detected by the presence of a `# {Artifact Name}` heading):

| # | Rule | Notes |
|---|---|---|
| T2-1 | Engagement header block present: `**Engagement:**`, `**Organisation:**`, `**Date:**` | Often at lines 1–6 after the heading |
| T2-2 | At least one content section (`## {N}. {Section Name}`) | Blank artifact skeletons are non-compliant |
| T2-3 | No raw `{{placeholder}}` tokens in frontmatter fields | Unreplaced template tokens in frontmatter |

---

### Tier 3 — Artifact-specific requirements

Applies only to named artifact types:

| Artifact | Requirement | Rule ID |
|---|---|---|
| Architecture Vision, Business Architecture, Data Architecture, Application Architecture, Technology Architecture, Gap Analysis, Consolidated Gap Analysis, Architecture Roadmap, Statement of Architecture Work, Migration Plan, Business Case, Engagement Charter, Governance Framework, Implementation Governance Plan, Communications Plan, Architecture Definition Document, Transition Architectures | `## Appendix A3 — Decision Log` section present | T3-A3 |
| Architecture Vision, Business Architecture, Data Architecture, Application Architecture, Technology Architecture, Gap Analysis, Consolidated Gap Analysis, Architecture Roadmap, Statement of Architecture Work, Migration Plan, Business Case, Communications Plan, Architecture Definition Document, Transition Architectures | `## Appendix A4 — Stakeholder Concerns & Objections` section present | T3-A4 |
| Architecture Roadmap | `## Strategic Alignment` section present with at least one populated row (non-placeholder) | T3-ROAD-SA |
| Architecture Roadmap | At least one WP-NNN entry has a non-empty `Advances Goals / Objectives` or `Executes Strategies` field | T3-ROAD-WP |
| Requirements Register | Scope column present (Corporate / Project distinction) | T3-REQ |
| Traceability Matrix | Two-section structure (Corporate / Project) present | T3-TRACE |
| Data Architecture | Data Flows table includes a `State` column (Current / Planned / Deprecated); every DF-NNN row has a non-blank State value | T3-DF-STATE |
| Architecture Vision, Business/Data/App/Tech Architecture, Gap Analysis, Consolidated Gap Analysis, Architecture Roadmap, Statement of Architecture Work, Migration Plan, Business Case, Compliance Assessment, Requirements Register, Engagement Charter, Governance Framework, Implementation Governance Plan, Communications Plan, Architecture Definition Document, Transition Architectures | `## Appendix A5 — Related Architecture Decisions` section present | T3-ADR |
| Same artifact list as T3-A3 | Any A3 row with `Authority = Strategic` has no corresponding `#### A3.N — {Item}` block and no sentinel `*(rationale not captured)*` below the A3 table. Surfaces in: `/ea-artifact view`, `/ea-engage-review`, `/ea-grill` — not checked during `/ea-interview` (rationale is captured live). | T3-RATIONALE |
| Constraints Register | Type column present (Technology / Regulatory / Budget / Timeline / Organisational / Interoperability) | T3-CON |
| Constraints Register | Every Active constraint has a non-empty Owner field | T3-CON-OWNER |
| Technology Architecture, Application Architecture | Every SBB with a non-empty "Constraints / Lock-in Risk" field has a `Referenced Constraints: [CST-NNN]` link or a documented justification for why no CST-NNN exists | T3-CON-SBB |

---

### Tier 4 — Practitioner Compliance (advanced)

Tier 4 rules apply to mature engagements (L3+) and focus on economic reasoning, decision quality, and adaptive governance. These are **aspirational** at L3 and **expected** at L5.

| # | Rule | Applies to | Compliant example | Non-compliant |
|---|---|---|---|---|
| T4-ECON | Economic traceability: Major strategic decisions (Authority = Strategic in A3) include cost, risk, or value framing in the rationale block | All artifacts with A3 | `#### A3.2 — Cloud Strategy … Rationale: Reduces TCO by 30% over 3 years; eliminates €2.1M legacy maintenance` | Rationale describes only technical benefits with no economic quantification |
| T4-LATENCY | Decision latency documented: A3 or ADR captures how long the decision took from first identification to resolution, and identifies the bottleneck | All artifacts with A3 / ADR-NNN references | `Decision latency: 14 days (blocked by vendor legal review)` | No mention of decision duration or blocker |
| T4-OPTION | Optionality preservation: Target-state choices that are hard to reverse (vendor lock-in, data model changes) include an `Optionality` note describing how the decision preserves future flexibility or why the risk is accepted | Architecture Vision, Roadmap, Data/App/Tech Architecture, Migration Plan | `Optionality: API-first design allows swapping vendor without consumer changes` | No discussion of reversibility or future flexibility |
| T4-FITNESS | Fitness function coverage: For technology or application standards introduced in the architecture, at least one automated validation mechanism is specified or referenced (CI check, policy-as-code, conformance test) | Technology Architecture, Application Architecture, Governance Framework, Implementation Governance Plan | `Fitness function: API schema compliance validated via spectral in CI pipeline` | Standard is documented but no automated enforcement is described |
| T4-PREMAT | Premature decision detection: Technology, vendor, or pattern decisions documented in Phase A artifacts (before business capability and application boundary analysis) are flagged as premature | Architecture Vision, Statement of Architecture Work | Phase A contains only directional choices; any specific tech choice is in a PAD-NNN with constraint boundaries | Architecture Vision §11 contains "We will adopt microservices" without service boundary analysis |
| T4-EVID | Evidence quality: ADRs and Strategic A3 entries include an Evidence Assessment table with at least one row, and overall sufficiency is rated | All ADRs, all A3 rows with Authority = Strategic | ADR §3b has Evidence Assessment table with 3 rows, overall = Sufficient | ADR has no Evidence Assessment section, or A3 rationale block describes only technical benefits with no evidence sources |
| T4-POLIT | Political alignment documented: High-impact or high-cost decisions include a Political Alignment note recording whether the decision faced stakeholder pressure and what the defensible evidence-based position is | ADRs, A3 rows with Cost = High or Impact = High | ADR §5c records "Strong pressure to adopt vendor X; defensible position = API-first design allows vendor swap" | No mention of stakeholder pressure or governance forum review |
| T4-PAD | Pending decision hygiene: Open PAD-NNN entries have an expiry date within 90 days of creation and a defined resolution path | All PAD-NNN artifacts | PAD-001 has expiryDate: 2026-06-15 and resolutionPhase: Phase E | PAD-001 has no expiry date or resolution path |
| T4-WPEVID | Work package evidence gating: Work packages with Evidence Status = Insufficient are not scheduled in Wave 1 | Architecture Roadmap | WP-002 has Evidence Status = Partial and is scheduled in Wave 2 with guardrails; WP-003 has Evidence Status = Insufficient and is flagged as deferred | WP-003 with no evidence is scheduled in Wave 1 without risk flag |
| T4-TCO | Quantified economics: strategic options and Wave-1 work packages carry a numeric cost estimate (Capex/Opex or 3-Year TCO) with a stated confidence rating, not just qualitative framing. Costed via Cost Entries (FIN-NNN) in the Cost Model Register | Business Case, Architecture Roadmap, Migration Plan, ADRs with Cost = High | Business Case Options table shows each option's 3-Year TCO and payback at Medium confidence sourced from FIN-002/FIN-003; Roadmap Wave-1 WPs each have a Capex/Opex figure | Business Case recommends an option with no TCO; Wave-1 WP has empty cost fields and no linked FIN entry |
| T4-CON-TRACE | Constraint traceability: Every High-priority Active constraint has at least one linked artifact or SBB reference | Constraints Register | CST-001 (High) has `Linked Artifacts: [technology-architecture-001]` and `SBB References: [SBB-003]` | CST-001 (High) has no linked artifacts and no SBB references |
| T4-CON-IMPACT | Constraint impact assessment: Every Enterprise-scoped constraint has a non-empty Impact Assessment describing which capabilities, ABBs, or work packages are bounded | Constraints Register | CST-002 (Enterprise) has Impact Assessment: "Bounds CAP-007 (Claims Processing) and WP-003 (Core Platform Migration)" | CST-002 (Enterprise) has blank Impact Assessment |

**Note on compliance philosophy:** Compliance is a means, not an end. See `failure-modes.md` → Failure Mode 1 (The Documentation Trap). If your compliance process produces checklists without improving decision quality, it has become part of the problem.

---

## Maturity-Based Compliance Expectations

Not every engagement needs to satisfy Tier 4 from day one. Use the maturity model (`adm-maturity-model.md`) to set realistic compliance targets:

| Maturity Level | Tier 1 | Tier 2 | Tier 3 | Tier 4 | Enforcement |
|---|---|---|---|---|---|
| **L1** — Compliance-oriented | Required | Required | Required (basic) | Not expected | Manual review |
| **L2** — Tailored | Required | Required | Required | Not expected | Manual review |
| **L3** — Integrated | Required | Required | Required | Aspirational — T4-ECON, T4-EVID, T4-PREMAT, T4-TCO encouraged | Manual + some automated |
| **L4** — Value-driven | Required | Required | Required | Required — T4-ECON, T4-EVID, T4-PREMAT, T4-POLIT, T4-TCO expected; T4-PAD, T4-WPEVID encouraged | Automated + selective manual |
| **L5** — Adaptive | Required | Required | Required | Required — all T4 rules enforced including T4-PAD and T4-WPEVID | Fully automated with exception handling |

**How to apply:** When an engagement is at L1–L2, run Tier 1–3 checks and report T4 as "advanced — optional." At L3+, surface T4 as recommendations. At L4+, treat T4 failures as warnings that block approval. At L5, T4 failures are blocking.

---

## Compliance Check Procedure

Run this check whenever an artifact is loaded for any of the following operations:
- Interview (ea-interviewer, step 1)
- Review (ea-review, Load Artifact step)
- View (ea-artifact, view mode)

**Steps:**

1. Read the artifact file.
2. Check Tier 1 rules — collect all failures.
3. Check Tier 2 rules — collect all failures.
4. Check Tier 3 rules relevant to this artifact type — collect all failures.
5. If zero failures → artifact is compliant. Continue silently.
6. If one or more failures → classify and present the compliance prompt (see below).

**Failure classification:**

| Classification | Condition | Urgency |
|---|---|---|
| **Structural** | Any T1 failure | High — affects data integrity and interview/review reliability |
| **Template drift** | Any T2 or T3 failure, no T1 failure | Medium — artifact usable but missing expected sections |

---

## Compliance Prompt

When failures are found, pause the current operation and present:

```
⚠️ Compliance check — {artifact name}

This artifact does not fully conform to the current template standard.

Issues found:
  {bullet list of each failure with rule ID and short description}

Options:
  1. Achieve compliance  — add missing fields/sections (your content is preserved)
  2. Accept as-is        — use with defaults for missing fields (no structure changes)
  3. View details        — show full compliance report before deciding
```

Wait for the user's response before proceeding with the original operation.

---

## Option 1 — Achieve Compliance

Apply all required changes to bring the artifact up to the current standard. **Preserve all existing content without modification.**

**Remediation actions by rule:**

| Rule | Remediation |
|---|---|
| T1-1 (no frontmatter) | Add frontmatter block at the top with all required fields populated from context or defaults |
| T1-2 (no `artifact`) | Add `artifact: {inferred from heading or filename}` |
| T1-3 (no `engagement`) | Add `engagement: {from active engagement.json}` |
| T1-4 (no `phase`) | Add `phase: {infer from artifact type or ask}` |
| T1-5 (no/invalid `status`) | Add `status: Draft` |
| T1-6 (no `reviewStatus`) | Add `reviewStatus: Not Reviewed` |
| T1-7 (no `version`) | Add `version: 0.1` |
| T1-8 (no `lastModified`) | Add `lastModified: {current ISO 8601 timestamp — YYYY-MM-DDTHH:MM:SSZ}` |
| T1-9 (no heading) | Add `# {artifact name}` as first line after frontmatter |
| T2-1 (no engagement header) | Add `**Engagement:** {name}` etc. block below the heading |
| T2-2 (no content sections) | Add placeholder: `## 1. Content\n\n⚠️ Not answered` |
| T2-3 (unreplaced frontmatter tokens) | Replace `{{engagement_name}}` etc. from `engagement.json`; leave body tokens intact |
| T3-A3 (missing Appendix A3) | Append the standard A3 section at the end of the artifact, before the footer line |
| T3-A4 (missing Appendix A4) | Append the standard A4 section after A3 (or before the footer line if A3 is absent) |
| T3-REQ (missing scope column) | Note: offer to run `/ea-requirements migrate` to add Enterprise/Program scope |
| T3-TRACE (missing sections) | Note: offer to regenerate via `/ea-requirements trace` |
| T3-DF-STATE (missing State column or blank State values) | Add `State` column to the Data Flows table header; for each DF-NNN row prompt the user: "Is this flow Current, Planned (Target), or Deprecated?" — do not guess |
| T3-RATIONALE (Strategic A3 entries without rationale) | Run `/ea-decisions rationale --artifact {artifact-name} --authority strategic` to capture missing rationale interactively; or add `#### A3.N — {Item}` blocks manually below the A3 table |

After applying all remediations:
- Update `lastModified` in both the artifact frontmatter and `engagement.json`
- Confirm: "Compliance achieved — {N} issues resolved. {list of changes made}"
- Continue with the original operation (interview / review / view)

---

## Option 2 — Accept As-Is (with sensible defaults)

Apply **only** the minimum changes needed to make the artifact loadable and functional. Do **not** change the document structure.

**Minimum changes:**

1. If T1 frontmatter failures exist: add a minimal frontmatter block with defaults — do not modify the document body.
2. Set `complianceNote: accepted-non-standard` in the frontmatter.
3. Update `lastModified` to today.
4. Write these minimal changes to the artifact file.
5. Continue with the original operation immediately.

**Defaults for all fields:**

| Field | Default |
|---|---|
| `artifact` | Inferred from filename (e.g., `architecture-vision.md` → `Architecture Vision`) or "Unknown Artifact" |
| `engagement` | From active `engagement.json` → `name` |
| `phase` | Inferred from artifact type; "Unknown" if cannot determine |
| `status` | `Draft` |
| `reviewStatus` | `Not Reviewed` |
| `version` | `0.1` |
| `lastModified` | Current ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SSZ) |

**Behaviour for missing sections:**
- Do NOT add missing sections.
- For interview: extract questions from whatever `{{placeholder}}` tokens exist; treat sections not in the current template as freeform content.
- For review: present the document as-is; note in the review summary that the artifact is non-standard.
- Note in the session log: "Artifact accepted non-standard — {N} compliance issues noted."

---

## Option 3 — View Details

Display the full compliance report before the user decides:

```
Compliance Report — {artifact name}
Generated: {date}

Tier 1 — Universal checks
  ✅ T1-1  Frontmatter present
  ❌ T1-6  reviewStatus field missing
  ✅ T1-7  version field present
  ...

Tier 2 — Template structure
  ❌ T2-1  Engagement header block missing
  ✅ T2-2  Content sections present
  ...

Tier 3 — Artifact-specific
  ❌ T3-A3  Appendix A3 — Decision Log section missing

Summary: 3 issues (1 structural, 2 template drift)
```

After displaying, re-present the three-option prompt (Option 1 / Option 2 / Option 3 removed, back to 1 and 2).

---

## Compliance State in Frontmatter

After any compliance operation, the artifact frontmatter may contain:

| Field | Value | Meaning |
|---|---|---|
| `complianceNote` | *(absent)* | Artifact is fully compliant |
| `complianceNote` | `accepted-non-standard` | User accepted the artifact as-is; structural issues remain |
| `complianceNote` | `remediated-{YYYY-MM-DD}` | Compliance was achieved on this date |

The `complianceNote` field is informational only — it does not affect artifact status or review workflows.

---

## Reporting Compliance in `/ea-status`

`/ea-status` reads each artifact in `engagement.json → artifacts[]` and checks for `complianceNote: accepted-non-standard`. If any exist, add to the engagement summary:

```
⚠️ Non-standard artifacts: {N} accepted as-is — run /ea-review to remediate
```
