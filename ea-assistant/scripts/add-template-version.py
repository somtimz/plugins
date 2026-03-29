#!/usr/bin/env python3
"""
One-time script: inject templateVersion field into all EA artifact template frontmatters.
Run from the repo root:
  python3 ea-assistant/scripts/add-template-version.py
"""
import os, re, sys

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")
TEMPLATE_VERSION = "0.9.5"

FRONTMATTER_RE = re.compile(r"^(---\s*\n)([\s\S]*?)(---\s*\n)", re.MULTILINE)

updated = []
skipped = []
errors = []

for filename in sorted(os.listdir(TEMPLATES_DIR)):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(TEMPLATES_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m = FRONTMATTER_RE.match(content)
    if not m:
        errors.append(f"NO FRONTMATTER: {filename}")
        continue

    fm_body = m.group(2)
    if "templateVersion:" in fm_body:
        skipped.append(filename)
        continue

    # Insert templateVersion after the version field, or before taxonomy if no version field
    if "version:" in fm_body:
        new_fm = re.sub(
            r"(version:\s*[^\n]+\n)",
            r"\1templateVersion: " + TEMPLATE_VERSION + "\n",
            fm_body,
            count=1,
        )
    else:
        new_fm = fm_body + f"templateVersion: {TEMPLATE_VERSION}\n"

    new_content = m.group(1) + new_fm + m.group(3) + content[m.end():]
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated.append(filename)

print(f"Updated : {len(updated)}")
for f in updated:
    print(f"  + {f}")
print(f"Skipped : {len(skipped)} (already have templateVersion)")
if errors:
    print(f"Errors  : {len(errors)}")
    for e in errors:
        print(f"  ! {e}")
    sys.exit(1)
