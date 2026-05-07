# Appendix Templates

Standard markdown blocks for appendices A3, A4, and A5. Used by `/ea-migrate` when injecting missing appendices into existing artifacts.

**Ordering:** When multiple appendices are missing, inject in this order: A3 → A4 → A5. Each is appended after the previous, or before the closing footer if none exist.

---

## Appendix A3 — Decision Log

Inject before Appendix A4 (or before footer if A4 absent):

```markdown
## Appendix A3 — Decision Log

<details>
<summary>📋 Guidance</summary>
Record governance decisions made during the development of this artifact. Use `/ea-decisions` to generate a cross-artifact Decision Register.
</details>

| ID | Decision | State | Authority | Domain | Cost | Impact | Risk | Subject | Captured By | Owner | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|
| *(no decisions recorded)* | — | — | — | — | — | — | — | — | — | — | — |
```

---

## Appendix A4 — Stakeholder Concerns & Objections

Inject after Appendix A3 (or before footer if A3 absent):

```markdown
## Appendix A4 — Stakeholder Concerns & Objections

<details>
<summary>📋 Guidance</summary>
Record all stakeholder concerns, objections, and tough questions raised about this artifact. Use `/ea-concerns` to generate a cross-artifact Concerns Register.
</details>

| ID | Concern | Raised By | Category | Status | Response | Action / Owner |
|---|---|---|---|---|---|---|
| *(no concerns recorded)* | — | — | — | — | — | — |
```

---

## Appendix A5 — Related Architecture Decisions

Inject after Appendix A4 (or after A3 if A4 is absent; or at end of document if neither present):

```markdown
## Appendix A5 — Related Architecture Decisions

| ADR ID | Title | Status | Summary |
|---|---|---|---|
| *(no related ADRs recorded)* | — | — | — |
```
