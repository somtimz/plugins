# Cross-Cutting Artifacts


### Risk Heat Map
**Artifact:** Risk Register  
**Viewpoint:** Custom — Risk analysis  
**Purpose:** Positions risks by likelihood and impact.

**Filename:** `risk-register-heat-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
quadrantChart
  title Risk Heat Map
  x-axis Low Likelihood --> High Likelihood
  y-axis Low Impact --> High Impact
  quadrant-1 Critical — Act Now
  quadrant-2 High — Mitigate
  quadrant-3 Low — Monitor
  quadrant-4 Medium — Watch
  RIS-001: [0.7, 0.8]
  RIS-002: [0.3, 0.9]
  RIS-003: [0.5, 0.4]
```

---

### Requirements Traceability Chain
**Artifact:** Requirements Register  
**Viewpoint:** Custom — Motivation traceability  
**Purpose:** Shows how requirements trace from drivers through goals, objectives, and strategies.

**Filename:** `requirements-register-traceability.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
flowchart LR
  DRV["📌 DRV-001\n{{driver}}"]
  G["🎯 G-001\n{{goal}}"]
  OBJ["🔢 OBJ-001\n{{objective}}"]
  REQ1["📋 REQ-001\n{{requirement}}"]
  REQ2["📋 REQ-002\n{{requirement}}"]
  DRV --> G --> OBJ --> REQ1
  OBJ --> REQ2
```

---
