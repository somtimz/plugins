---
name: ea-security
description: Security architecture knowledge store for ea-assistant — SABSA layer mapping, ISO 27001:2022 controls, NIST CSF 2.0 functions, artifact security checklists, and phase-specific interview questions
version: 0.9.59
---

# EA Security Skill

This skill provides the security architecture reference layer for ea-assistant engagements. It maps SABSA layers to TOGAF ADM phases, surfaces ISO 27001:2022 control obligations and NIST CSF 2.0 functions against TOGAF artifacts, and supplies structured interview questions and per-artifact checklists for security-scoped work. Load this skill when an engagement has security drivers (DRV-NNN type:security) or when running /ea-security-review or /ea-grill with a security focus.

## Reference Files

| Reference file | Read by | Purpose |
|---|---|---|
| sabsa-adm-mapping.md | ea-security-advisor, ea-security-auditor | SABSA layer → TOGAF ADM phase mapping |
| iso27001-controls.md | ea-security-advisor, ea-security-auditor | ISO 27001:2022 control domains and artifact mapping |
| nist-csf-functions.md | ea-security-advisor, ea-security-auditor | NIST CSF 2.0 functions and artifact coverage |
| artifact-security-checklist.md | ea-security-auditor, /ea-security-review, /ea-grill security | Per-artifact security control checklist |
| security-interview-questions.md | ea-interviewer | Phase-by-phase optional security questions |
