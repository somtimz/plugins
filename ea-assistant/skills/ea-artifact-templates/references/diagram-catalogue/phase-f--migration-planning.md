# Phase F — Migration Planning


### Migration Wave Diagram
**Artifact:** Migration Plan  
**Viewpoint:** Custom — Transition sequence  
**Purpose:** Shows what moves in each wave and the transition state at each checkpoint.

**Filename:** `migration-plan-waves.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
gantt
  title Migration Waves
  dateFormat  YYYY-MM-DD
  section Wave 1
    Decommission System A   :done, w1a, 2025-01-01, 60d
    Deploy Replacement B    :w1b, 2025-01-01, 90d
  section Wave 2
    Migrate Data Domain X   :w2a, after w1b, 60d
    Cutover Users           :w2b, after w2a, 30d
  section Wave 3
    Decommission Legacy     :w3, after w2b, 45d
```

---
