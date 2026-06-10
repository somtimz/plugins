# EA-Assistant Improvement Advisory — 2026-06-10

Analysis of ea-assistant v0.9.55 (53 commands, 12 agents, 17 skills, 46 templates, ~12,500 lines of command markdown) against its source and the live Veloria AI Program engagement (`/mnt/d/EA-workspace`, 252 artifact files, 8 weeks of activity). Assessed dimensions: TOGAF/ADM alignment, multi-framework support, ease of use, design simplicity, deliverable consumability, and methodology gaps.

**Overall verdict:** TOGAF, Zachman, and security-framework alignment is strong and mature. The dominant problems are (a) surface-area complexity — too many near-duplicate commands, (b) ceremony that outpaces content — 157 empty detail stubs, 47 of 49 artifacts stuck in Draft, and (c) weak stakeholder-facing output — an 11,000-line consolidated report that embeds full artifacts instead of summarizing, with no "start here" entry point.

---

## Findings

### 1. TOGAF / ADM alignment — strong, with specific gaps

**Strong:** Full Preliminary→H cycle with phase folders, templates, interview banks (1,325-line question bank), compliance tiers T3/T4, PAD-NNN premature-decision detection, motivation traceability (DRV→G→OBJ→STR→REQ→WP), Business Scenarios fully operationalized, phase re-entry supported.

**Gaps:**
- **Phase G thin** — no dedicated interview bank; Compliance Assessment is template-only.
- **Phase H minimal** — Change Request template only; no change-management tactics, escalation rules, or ACR triage guidance.
- **Requirements Management modeled as a sequential phase**, not the continuous center-of-cycle discipline TOGAF defines. No automatic bridge from Requirements into Phase A; requirements are not systematically re-surfaced when entering each phase.
- **No ADM tailoring/partitioning** — all 11 phases seeded for every engagement regardless of architectureLevel (Strategic/Segment/Capability/Solution). No way to skip/merge phases or run scoped iterations; `optOuts[]` exists but doesn't prune.
- **Iteration support is shallow** — phases can be reopened but there's no audit trail or reconciliation of what changed on re-entry.
- **Missing TOGAF techniques:** Business Transformation Readiness Assessment, formal Capability-Based Planning method, Interoperability Requirements analysis, TOGAF risk appetite/tolerance method, Enterprise Continuum.

### 2. Framework support

| Framework | Status |
|---|---|
| Zachman 6×6 | Mature — generate/interview/gap/classify modes, integrated into lifecycle. Keep as-is. |
| SABSA | Mature — all 6 layers + 10 BSAs mapped to ADM phases |
| ISO 27001:2022 | Mature — 4 domains, 93 controls referenced, SoA→Phase G mapping |
| NIST CSF 2.0 | Mature — 6 functions, 22 categories, maturity tiers |
| AWS Well-Architected | **Absent** — zero support; cloud appears only as example text |
| Azure CAF / GCP AF | Absent |
| ArchiMate 3.x | Mature notation guide; no metamodel validation (acceptable) |

**Security integration gap:** security frameworks are available only as a *post-hoc audit* (`/ea-security-review`). Security questions are not injected into phase interviews, so gaps surface late.

**Recommendation — generic "framework lens" mechanism** rather than bespoke per-framework commands: a `skills/ea-framework-lenses/` skill with one reference file per framework (pillars/layers → ADM phase mapping → review checklist → interview question injection). Ship AWS Well-Architected first (6 pillars mapped to Phases C/D/E review and a `/ea-grill` mode); Azure CAF/GCP become drop-in reference files later. Reuse the existing ea-security pattern (`sabsa-adm-mapping.md` is the proven shape).

### 3. Ease of use — the core problem is 53 commands

- **9 register commands are near-clones** (`/ea-goals`, `/ea-drivers`, `/ea-issues`, `/ea-problems`, `/ea-risks`, `/ea-constraints`, `/ea-policies`, `/ea-standards`, `/ea-decisions`) — same list/add/update/trace/generate structure, ~30–40% duplicated logic (~2,000–2,500 lines).
- **5 overlapping review commands** (`/ea-grill`, `/ea-review`, `/ea-consistency`, `/ea-lens`, `/ea-engage-review`) with an implicit decision tree — users can't tell which to run when.
- **Ceremony outpaces content** (Veloria evidence): 157 detail files bulk-created as empty stubs and never filled; 7 TBDs and a TODO leaked into the "complete" Business Architecture; 4 dated risk-register snapshots cluttering cross-cutting/.
- **Lifecycle stalls:** 47 of 49 artifacts permanently in Draft — there's no lightweight finalize/publish gate that motivates closure.

### 4. Design / implementation simplicity

- **Register-command boilerplate** — biggest consolidation win (see above).
- **Monolithic references:** `ea-concepts.md` (1,436 lines), `phase-interview-questions.md` (1,325 lines) — every change has wide blast radius; split by domain/phase.
- **engagement.json** grows large in practice (Veloria: 2,403 lines / 88 KB), has no `schemaVersion` field, and has a dual source-of-truth problem: registers live in JSON *and* in generated dated markdown registers.
- **Agent wiring:** `ea-advisor`, `ea-document-converter`, `ea-requirements-analyst` are not invoked by any command — they are referenced agent-to-agent (ea-facilitator → ea-advisor; ea-document-analyst → converter/requirements-analyst). Not dead, but the command→agent→skill routing has no master index; document or simplify.
- **No transaction safety** on engagement.json writes (acceptable risk for now; noted only).

### 5. Deliverable organization & consumability (Veloria evidence)

- **Consolidated report ≈ 11,000 lines / 10 MB PDF** — embeds full artifact text (370 headers) rather than layering summary→detail. It's an archive, not a briefing.
- **No stakeholder entry point** — no index/reading-guide; engagement CLAUDE.md is machine-orientation; Executive Summary exists but is Draft/Not Reviewed.
- **Reading one artifact requires navigating 8–12 files** (artifact + review + interviews + grills + linked registers + detail stubs + diagrams).
- **Scaffolding leaks into output** — guidance comments, TBD placeholders, and empty appendices appear in publishable artifacts.

### 6. Definition / methodology gaps (ea-concepts.md)

Missing or underspecified concepts: **Service** (Business/App/Tech), **Interface/API contract**, **Application Component / Technology Component**, **Capability Increment**, **Plateau**, **Deliverable** (vs Work Package vs artifact), **Architecture Partitioning**, **Enterprise Continuum**, formalized **Stakeholder Management technique**, formalized **Maturity Assessment** method.

---

## Recommended Improvements (prioritized)

### P1 — Quick wins: ceremony reduction + consumable output

1. **Stop bulk detail-stub creation** — `/ea-detail` and register commands create detail files *on demand only* (when content is supplied).
2. **Layered publish pipeline** — rework `/ea-publish` to produce: (a) 3–5 page executive brief, (b) per-domain 1–2 page summaries, (c) full artifacts as appendix links — replacing full-text embedding; auto-generate a stakeholder `index.md` reading guide; strip guidance comments and block on unresolved TBD/placeholder text with a warning list.
3. **Review decision tree** — add a "which review command when" table to `/ea-help` and to each review command's preamble.
4. **Snapshot hygiene** — dated register generations go to a `snapshots/` subfolder; the current register is the only file at the top level.

### P2 — Surface-area consolidation

5. **Shared register framework** — extract the common list/add/update/trace/generate logic into one reference; each of the 9 register commands shrinks to a thin parameterization (ID prefix, fields, trace chain). Keep existing command names as aliases. ~2,000+ line reduction.
6. **Unify review commands** — keep `/ea-grill` (distinct skill-driven persona) but fold `/ea-consistency` into `/ea-engage-review --consistency`; clarify `/ea-review` (formal sign-off + comments) vs `/ea-lens` (opinionated practitioner pass). Net: 5 commands → 3 with explicit lanes.
7. **Requirements as continuous discipline** — on every `/ea-phase <X>` entry, auto-surface open/affected REQ-NNN items for that phase; document the Requirements→Phase A bridge.

### P3 — Framework & methodology depth

8. **Framework-lens mechanism + AWS Well-Architected lens** — new `skills/ea-framework-lenses/` with `references/aws-well-architected.md` (6 pillars → ADM phase mapping → checklist → interview questions); wire into `/ea-grill` and Phase C/D/E interviews. Extensible to Azure CAF/GCP.
9. **Security interview injection** — inject phase-relevant SABSA/ISO/NIST questions into `/ea-interview` phase mode (question sets already exist in `skills/ea-security/references/`); keep `/ea-security-review` as the audit backstop.
10. **ADM tailoring** — at `/ea-new`, derive the phase set from architectureLevel; record tailoring in engagement.json; allow explicit phase opt-out that actually prunes seeded folders.
11. **Phase G/H deepening** — Phase G interview bank + Compliance Assessment scaffolding; Phase H change-management guidance (ACR triage, escalation rules, re-entry mapping to ADM phases).

### P4 — Definitions & schema hardening

12. **Concept additions to ea-concepts.md** — Service, Interface, Application/Technology Component, Capability Increment, Plateau, Deliverable, Architecture Partitioning, Enterprise Continuum; new ID prefixes only where register-worthy (e.g. SVC-NNN, IFC-NNN).
13. **TOGAF technique stubs** — Business Transformation Readiness Assessment (Phase A/E artifact + template), Capability-Based Planning reference, Interoperability Requirements checklist, risk appetite/tolerance fields on the Risk Register.
14. **Schema versioning** — add `schemaVersion` to the engagement.json seed; `/ea-migrate` reads/writes it and logs a migration audit entry. Declare engagement.json the single source of truth for registers; generated markdown registers are explicitly labeled as rendered snapshots.

---

## Status

P1 implemented in `feat/advisory-p1-consumability` (this advisory's first PR). P2–P4 to follow as separate PRs, one priority band each.
