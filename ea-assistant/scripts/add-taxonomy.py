#!/usr/bin/env python3
"""
One-time script: inject taxonomy: block into all EA artifact template frontmatters.
Run from the repo root:
  python3 ea-assistant/scripts/add-taxonomy.py
"""
import os, re, sys

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")

# Per-template taxonomy values
TAXONOMY = {
    "architecture-vision.md": dict(
        domain="Cross-cutting", category="Strategy", audience="Executive",
        layer="Motivation", sensitivity="Internal",
        tags=["vision", "drivers", "goals", "strategy", "phase-a"],
    ),
    "architecture-principles.md": dict(
        domain="Cross-cutting", category="Strategy", audience="Architecture",
        layer="Reference", sensitivity="Internal",
        tags=["principles", "standards", "governance", "preliminary"],
    ),
    "governance-framework.md": dict(
        domain="Cross-cutting", category="Strategy", audience="Governance",
        layer="Governance", sensitivity="Internal",
        tags=["governance", "arb", "decision-rights", "preliminary"],
    ),
    "business-model-canvas.md": dict(
        domain="Business", category="Strategy", audience="Executive",
        layer="Motivation", sensitivity="Confidential",
        tags=["business-model", "value-proposition", "phase-b"],
    ),
    "statement-of-architecture-work.md": dict(
        domain="Cross-cutting", category="Planning", audience="Governance",
        layer="Governance", sensitivity="Confidential",
        tags=["scope", "commitment", "deliverables", "phase-a"],
    ),
    "stakeholder-map.md": dict(
        domain="Cross-cutting", category="Analysis", audience="Architecture",
        layer="Reference", sensitivity="Confidential",
        tags=["stakeholders", "concerns", "influence", "phase-a"],
    ),
    "requirements-register.md": dict(
        domain="Cross-cutting", category="Analysis", audience="All",
        layer="Reference", sensitivity="Internal",
        tags=["requirements", "nfr", "constraints", "traceability"],
    ),
    "gap-analysis.md": dict(
        domain="Cross-cutting", category="Analysis", audience="Architecture",
        layer="Transition", sensitivity="Internal",
        tags=["gaps", "baseline", "target", "phase-e"],
    ),
    "traceability-matrix.md": dict(
        domain="Cross-cutting", category="Analysis", audience="Architecture",
        layer="Reference", sensitivity="Internal",
        tags=["traceability", "requirements", "goals", "cross-cutting"],
    ),
    "business-architecture.md": dict(
        domain="Business", category="Design", audience="Business",
        layer="Target", sensitivity="Internal",
        tags=["capabilities", "processes", "organisation", "phase-b"],
    ),
    "data-architecture.md": dict(
        domain="Data", category="Design", audience="Architecture",
        layer="Target", sensitivity="Internal",
        tags=["data-model", "information", "data-flow", "phase-c"],
    ),
    "application-architecture.md": dict(
        domain="Application", category="Design", audience="Architecture",
        layer="Target", sensitivity="Internal",
        tags=["applications", "integration", "portfolio", "phase-c"],
    ),
    "technology-architecture.md": dict(
        domain="Technology", category="Design", audience="Architecture",
        layer="Target", sensitivity="Internal",
        tags=["infrastructure", "platforms", "technology", "phase-d"],
    ),
    "architecture-roadmap.md": dict(
        domain="Cross-cutting", category="Planning", audience="All",
        layer="Transition", sensitivity="Internal",
        tags=["roadmap", "work-packages", "sequencing", "phase-e"],
    ),
    "migration-plan.md": dict(
        domain="Cross-cutting", category="Planning", audience="Delivery",
        layer="Transition", sensitivity="Internal",
        tags=["migration", "waves", "cutover", "phase-f"],
    ),
    "consolidated-report.md": dict(
        domain="Cross-cutting", category="Planning", audience="Executive",
        layer="Reference", sensitivity="Internal",
        tags=["summary", "executive", "portfolio", "cross-cutting"],
    ),
    "architecture-contract.md": dict(
        domain="Cross-cutting", category="Governance", audience="Governance",
        layer="Governance", sensitivity="Confidential",
        tags=["contract", "conformance", "commitment", "phase-g"],
    ),
    "compliance-assessment.md": dict(
        domain="Cross-cutting", category="Governance", audience="Governance",
        layer="Governance", sensitivity="Internal",
        tags=["compliance", "conformance", "assessment", "phase-g"],
    ),
    "implementation-governance-plan.md": dict(
        domain="Cross-cutting", category="Governance", audience="Governance",
        layer="Governance", sensitivity="Internal",
        tags=["governance", "review-schedule", "checkpoints", "phase-g"],
    ),
    "change-request.md": dict(
        domain="Cross-cutting", category="Governance", audience="Governance",
        layer="Governance", sensitivity="Confidential",
        tags=["change", "impact", "disposition", "phase-h"],
    ),
    "decision-register.md": dict(
        domain="Cross-cutting", category="Register", audience="Governance",
        layer="Governance", sensitivity="Internal",
        tags=["decisions", "register", "a3", "cross-cutting"],
    ),
    "risk-register.md": dict(
        domain="Cross-cutting", category="Register", audience="Governance",
        layer="Governance", sensitivity="Confidential",
        tags=["risks", "register", "mitigation", "cross-cutting"],
    ),
    "change-register.md": dict(
        domain="Cross-cutting", category="Register", audience="Governance",
        layer="Governance", sensitivity="Internal",
        tags=["changes", "register", "acr", "phase-h"],
    ),
}

FRONTMATTER_RE = re.compile(r"^(---\s*\n)([\s\S]*?)(---\s*\n)", re.MULTILINE)

def build_taxonomy_block(t: dict) -> str:
    tags = "[" + ", ".join(t["tags"]) + "]"
    return (
        f"taxonomy:\n"
        f"  domain: {t['domain']}\n"
        f"  category: {t['category']}\n"
        f"  audience: {t['audience']}\n"
        f"  layer: {t['layer']}\n"
        f"  sensitivity: {t['sensitivity']}\n"
        f"  tags: {tags}\n"
    )

updated = []
skipped = []
errors = []

for filename, tax in TAXONOMY.items():
    filepath = os.path.join(TEMPLATES_DIR, filename)
    if not os.path.exists(filepath):
        errors.append(f"NOT FOUND: {filename}")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m = FRONTMATTER_RE.match(content)
    if not m:
        errors.append(f"NO FRONTMATTER: {filename}")
        continue

    fm_body = m.group(2)
    if "taxonomy:" in fm_body:
        skipped.append(filename)
        continue

    new_content = m.group(1) + fm_body + build_taxonomy_block(tax) + m.group(3) + content[m.end():]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated.append(filename)

print(f"Updated : {len(updated)}")
for f in updated:
    print(f"  + {f}")
print(f"Skipped : {len(skipped)} (already have taxonomy)")
if errors:
    print(f"Errors  : {len(errors)}")
    for e in errors:
        print(f"  ! {e}")
    sys.exit(1)
