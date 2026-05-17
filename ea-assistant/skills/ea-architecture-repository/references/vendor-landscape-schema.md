# Vendor Landscape Register — VDR Schema

Entries stored at: `Architecture-Repository/vendor-landscape/entries/VDR-NNN.md`

## YAML Frontmatter

```yaml
id: VDR-NNN
vendor: "<Vendor name>"
product: "<Product / service name>"
category: "<IaaS | PaaS | SaaS | On-prem | Open-source | Consulting>"
version: "<Current assessed version>"
roadmapStatus: "<Active | Sunset | EoL | Unknown>"
contractStatus: "<Contracted | Evaluating | No contract | Expired>"
lockInRisk: "<Low | Medium | High>"
linkedABBs: []        # ABB-NNN list — ABBs this product implements
linkedSBBs: []        # SBB-NNN list — per-engagement SBBs that reference this vendor
linkedADRs: []        # ADR-NNN list — decisions that reference this vendor
linkedSTDs: []        # STD-NNN list — standards this vendor claims compliance with
lastReviewed: "YYYY-MM-DD"
reviewedBy: ""
notes: ""
```

## Markdown Body Sections

- **Product Summary** — what the product does, target use case, current version
- **Roadmap** — known upcoming releases, EOL dates, migration paths, vendor support commitments
- **Risk Assessment** — lock-in risk rationale, financial stability, support quality, competitive alternatives
- **Architecture Fit** — which ABBs/SBBs this product implements; gaps vs. ABB requirements
- **Compliance** — standards and certifications claimed (cross-reference STD-NNN)

## Field Reference

| Field | Type | Values | Notes |
|---|---|---|---|
| `id` | string | `VDR-NNN` (e.g. VDR-001) | Allocated from `repo.json → vendorLandscape.nextId` |
| `vendor` | string | any | Vendor company name |
| `product` | string | any | Specific product/service name |
| `category` | enum | IaaS, PaaS, SaaS, On-prem, Open-source, Consulting | Product deployment model |
| `version` | string | any | Version assessed at lastReviewed date |
| `roadmapStatus` | enum | Active, Sunset, EoL, Unknown | Active = vendor actively develops; Sunset = limited new investment; EoL = end of life |
| `contractStatus` | enum | Contracted, Evaluating, No contract, Expired | Organisation's procurement relationship |
| `lockInRisk` | enum | Low, Medium, High | Low = open standards/easy migration; High = proprietary, costly exit |
| `linkedABBs` | array | ABB-NNN | ABBs this vendor product can implement |
| `linkedSBBs` | array | SBB-NNN | Per-engagement SBBs selecting this vendor (cross-ref only — SBB is authoritative) |
| `linkedADRs` | array | ADR-NNN | Architecture decisions that reference this vendor |
| `linkedSTDs` | array | STD-NNN | Standards this vendor claims to comply with |
| `lastReviewed` | ISO date | YYYY-MM-DD | Date of last assessment update |

## VDR vs SBB Distinction

- **VDR** is organisation-wide and lives in `Architecture-Repository/`. It captures whether the organisation should trust/use this vendor at all.
- **SBB** is per-engagement and lives in `EA-Projects/<slug>/`. It captures the specific deployment decision for one project.
- A SBB links to a VDR via `linkedVDR: VDR-NNN` (added in Task 9). The VDR records which SBBs reference it in `linkedSBBs[]`.

## Index File

`Architecture-Repository/vendor-landscape/vendor-index.md` — maintained by `/ea-vendors`:

```markdown
# Vendor Landscape Register Index

| ID | Vendor | Product | Category | Roadmap Status | Lock-in Risk | Last Reviewed |
|---|---|---|---|---|---|---|
| VDR-001 | ... | ... | ... | ... | ... | ... |
```
