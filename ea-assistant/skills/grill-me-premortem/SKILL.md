---
name: grill-me-premortem
description: >
  Red-team a proposal or review an existing risk assessment. Two modes: Generate (assume failure 12 months out and surface new risks) and Review (interrogate an existing risk register for gaps, weak mitigations, and interdependencies). Produces a pre-mortem report or a risk critique.
version: 0.2.0
---

# Grill Me — Pre-Mortem & Risk Review

This skill operates in two modes. Ask the user which one before starting.

## Mode Selection

Present this choice at the start:

> **How would you like to examine risk?**
>
> **1. Generate** — I'll assume your proposal has already failed 12 months from now and work backwards to surface failure modes, warning signs, and risks you haven't thought of. Best when you have a plan or proposal but no formal risk assessment yet.
>
> **2. Review** — Give me your existing risk register, risk section, or list of identified risks and I'll interrogate each one for completeness, credibility, and gaps. Best when you already have documented risks and want them stress-tested.

If the user provides a risk register or artifact without choosing, default to **Review** mode.
If the user describes a proposal or initiative without choosing, default to **Generate** mode.

---

## Mode 1 — Generate (Pre-Mortem)

Red-team this proposal as if it has already failed 12 months from now.

Ask one question at a time to uncover:
- what failed
- why warning signs were missed
- which assumptions broke
- what stakeholders resisted
- what second-order effects emerged
- what we should have done earlier

Systematically probe risk categories the user may not have considered:
- **delivery** — schedule, scope, dependencies, capacity
- **technical** — architecture, integration, performance, security
- **financial** — cost overrun, funding withdrawal, ROI shortfall
- **political** — stakeholder resistance, sponsor change, competing priorities
- **regulatory** — compliance gaps, policy changes, audit findings
- **talent** — key-person dependency, skills gap, turnover
- **vendor** — delivery failure, price escalation, lock-in, acquisition
- **market** — demand shift, competitive response, timing

For each question:
- state the failure mode being tested
- give likely warning indicators
- recommend a mitigation

At the end, provide a pre-mortem report with:
1. top failure modes (ranked by likelihood × impact)
2. early warning signs (what to monitor and when)
3. recommended safeguards (each with an owner and trigger condition)
4. risk interdependencies (which risks compound if one materialises)
5. whether the plan should proceed, pause, or be redesigned

---

## Mode 2 — Review (Risk Critique)

Read the provided risk register, risk section, or risk list in full before asking any questions.

Then interrogate one risk at a time:

**For each documented risk, challenge:**
- **Specificity** — is the risk stated precisely enough to act on? ("Technology risk" is not a risk. "Migration to the new ERP stalls because the vendor cannot deliver data migration tooling by Q3" is a risk.)
- **Likelihood rating** — is this justified? What evidence supports the rating? Has this happened before in similar contexts?
- **Impact rating** — what is the actual blast radius? Is the impact stated in terms of consequences (cost, delay, reputation) or just labelled High/Med/Low?
- **Mitigation quality** — is the mitigation real? A real mitigation is funded, owned, scheduled, and measurable. "We will monitor the situation" is not a mitigation.
- **Mitigation ownership** — is there a named owner? Would that person agree they own this?
- **Residual risk** — after mitigation, what risk remains? Is this explicitly acknowledged?
- **Risk appetite alignment** — is this level of residual risk consistent with the organisation's stated appetite?

**Then check for systemic gaps:**
- **Missing risk categories** — compare documented risks against the eight categories above (delivery, technical, financial, political, regulatory, talent, vendor, market). Flag empty categories.
- **Interdependencies** — do any risks compound? If Risk A materialises, does it increase the likelihood or impact of Risk B? Flag unacknowledged chains.
- **Concentration** — are all risks in one category (e.g. all technical)? This usually means political, financial, or talent risks have been avoided.
- **Optimism bias** — are most risks rated Low likelihood? Are most mitigations "accept" or "monitor"? Challenge the overall profile.

For each question:
- state which risk you are examining and what quality you are testing
- explain what a well-documented risk looks like for this concern
- identify the specific weakness

At the end, provide a risk critique with:
1. risks that are well-documented and credible
2. risks that are vague, under-rated, or have weak mitigations
3. missing risks (categories not covered, interdependencies not identified)
4. overall risk profile assessment (balanced / optimistic / concentrated / incomplete)
5. recommended actions (prioritised by impact on decision quality)
