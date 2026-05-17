---
seed: architecture-repo-json
description: Seed template for Architecture-Repository/repo.json — written by /ea-repo init
---

```json
{
  "name": "{{organisation}} Architecture Repository",
  "organisation": "{{organisation}}",
  "description": "Shared TOGAF Architecture Repository — Standards Information Base, Vendor Landscape, Technology Horizon, and enterprise governance.",
  "version": "1.0.0",
  "createdDate": "{{YYYY-MM-DD}}",
  "lastModified": "{{YYYY-MM-DDTHH:MM:SSZ}}",
  "owner": { "name": "", "email": "", "role": "Architecture Repository Owner" },
  "linkedEngagements": [],
  "linkedProjects": [],
  "governance": {
    "enterprisePrinciplesFile": "governance/enterprise-principles.md",
    "enterprisePoliciesFile": "governance/enterprise-policies.md",
    "enterpriseConstraintsFile": "governance/enterprise-constraints.md"
  },
  "sib": { "enabled": true, "indexFile": "sib/sib-index.md", "nextId": 1 },
  "vendorLandscape": { "enabled": true, "indexFile": "vendor-landscape/vendor-index.md", "nextId": 1 },
  "technologyHorizon": { "enabled": true, "indexFile": "technology-horizon/horizon-index.md", "nextId": 1 }
}
```
