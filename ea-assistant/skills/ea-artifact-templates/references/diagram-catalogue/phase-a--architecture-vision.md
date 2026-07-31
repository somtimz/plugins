# Phase A — Architecture Vision


### Motivation Map
**Artifact:** Architecture Vision  
**Viewpoint:** ArchiMate — Motivation viewpoint  
**Purpose:** Shows the full DRV → Goal → Strategy chain. Communicates *why* the engagement exists and *how* the organisation intends to respond.

**Filename:** `architecture-vision-motivation-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
flowchart LR
  DRV1["📌 DRV-001\n{{driver_1}}"]
  DRV2["📌 DRV-002\n{{driver_2}}"]
  G1["🎯 G-001\n{{goal_1}}"]
  G2["🎯 G-002\n{{goal_2}}"]
  STR1["🗺️ STR-001\n{{strategy_1}}"]
  STR2["🗺️ STR-002\n{{strategy_2}}"]
  ISS1["⚠️ ISS-001\n{{issue_1}}"]

  DRV1 --> G1
  DRV2 --> G1
  DRV2 --> G2
  G1 --> STR1
  G2 --> STR2
  ISS1 -. "threatens" .-> G1
```

---

### Stakeholder Power/Interest Grid
**Artifact:** Architecture Vision / Stakeholder Map  
**Viewpoint:** Custom — Stakeholder analysis  
**Purpose:** Positions stakeholders by influence and interest to guide engagement strategy.

**Filename:** `architecture-vision-stakeholder-grid.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
quadrantChart
  title Stakeholder Power / Interest Grid
  x-axis Low Interest --> High Interest
  y-axis Low Power --> High Power
  quadrant-1 Manage Closely
  quadrant-2 Keep Satisfied
  quadrant-3 Monitor
  quadrant-4 Keep Informed
  Sponsor: [0.8, 0.9]
  Programme Director: [0.7, 0.75]
  Lead Architect: [0.6, 0.6]
  End Users: [0.5, 0.3]
```

---
