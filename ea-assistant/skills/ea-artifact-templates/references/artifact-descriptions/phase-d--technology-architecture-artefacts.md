# Phase D — Technology Architecture Artefacts


### Technology Standards Catalogue

**Purpose:** Documents the approved technology standards, products, and versions that all architecture and implementation work must conform to.

**Audience:** Solution architects, developers, infrastructure engineers, procurement.

**Contents:**
- **Technology Direction** — drawn from `engagement.json direction.Technology`; presented in three sections:
  - *Goals* — desired technology state (e.g., "cloud-native platform", "zero-trust security posture")
  - *Objectives* — measurable technology targets (e.g., "achieve 99.9% availability for Tier-1 systems by Q3 2026")
  - *Strategies* — chosen technology approaches (e.g., cloud-first, containerisation, open-source preferred)
- Technology domain (e.g., Database, Middleware, Identity, Compute)
- Standard name and product/technology
- Approved versions
- Rationale for selection (including which Technology direction items the standard supports)
- **Technology Metrics** — drawn from `engagement.json metrics.Technology`; table of Technology metrics grouped by type with measure, baseline → target, deadline, frequency, source, and current status
- Exceptions process
- Review/expiry date

**When to Create:** Phase D (may originate in Preliminary if standards pre-exist).

**Who Reviews:** CTO, architecture review board, security team.

**Phase:** D (Preliminary for pre-existing standards).

---

### Environments and Locations Diagram

**Purpose:** Shows the physical and logical deployment topology of the architecture: data centres, cloud regions, network zones, and how they interconnect.

**Audience:** Infrastructure architects, security architects, operations teams.

**Contents:**
- Data centres / cloud regions / edge locations
- Network zones and security tiers (DMZ, internal, management)
- High-level server / cluster placement
- Communication paths and protocols between locations
- External network connections (internet, partner links, regulatory networks)

**When to Create:** Phase D.

**Who Reviews:** Infrastructure architect, network architect, security architect.

**Phase:** D.

---
