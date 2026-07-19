# Phase E — Opportunities & Solutions


### Gap Heat Map
**Artifact:** Gap Analysis  
**Viewpoint:** Custom — Capability/priority analysis  
**Purpose:** Visual prioritisation of gaps by strategic impact and closure effort.

**Filename:** `gap-analysis-heat-map.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
quadrantChart
  title Gap Priority Matrix
  x-axis Low Effort --> High Effort
  y-axis Low Impact --> High Impact
  quadrant-1 Quick Wins
  quadrant-2 Major Projects
  quadrant-3 Fill-ins
  quadrant-4 Thankless Tasks
  GAP-001: [0.2, 0.8]
  GAP-002: [0.7, 0.9]
  GAP-003: [0.3, 0.3]
```

---

### Architecture Roadmap (Gantt)
**Artifact:** Architecture Roadmap  
**Viewpoint:** Custom — Timeline / delivery  
**Purpose:** Delivery timeline showing work packages sequenced into waves.

**Filename:** `architecture-roadmap-gantt.mmd`

```mermaid
%% 🤖 AI Draft — Review Required
gantt
  title Architecture Roadmap
  dateFormat  YYYY-MM-DD
  section Wave 1 — Foundation
    WP-001 Capability A   :wp1, 2025-01-01, 90d
    WP-002 Capability B   :wp2, after wp1, 60d
  section Wave 2 — Core Build
    WP-003 Capability C   :wp3, after wp1, 120d
    WP-004 Capability D   :wp4, after wp3, 90d
  section Wave 3 — Optimise
    WP-005 Capability E   :wp5, after wp4, 60d
```

---
