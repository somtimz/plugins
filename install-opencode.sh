#!/usr/bin/env bash
# Install skills from somtimz/plugins into OpenCode
# OpenCode discovers skills from ~/.config/opencode/skills/
# Usage: bash install-opencode.sh [--uninstall]

set -euo pipefail

SKILL_TARGET="${OPENCODE_SKILLS_DIR:-$HOME/.config/opencode/skills}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

SKILLS=(
  ea-assistant/skills/archimate-notation
  ea-assistant/skills/ea-artifact-templates
  ea-assistant/skills/ea-document-ingestion
  ea-assistant/skills/ea-engagement-lifecycle
  ea-assistant/skills/ea-generation
  ea-assistant/skills/ea-requirements-management
  ea-assistant/skills/ea-interview-ui
  ea-assistant/skills/zachman-framework
  RAG-assistant/skills/doc-ingestion-pipeline
  RAG-assistant/skills/rag-chat
  ITIL-assistant/skills/itil-change-request
  ITIL-assistant/skills/cab-review
)

if [[ "${1:-}" == "--uninstall" ]]; then
  echo "Uninstalling skills from $SKILL_TARGET ..."
  for skill_path in "${SKILLS[@]}"; do
    skill_name=$(basename "$skill_path")
    target="$SKILL_TARGET/$skill_name"
    if [ -L "$target" ]; then
      rm "$target"
      echo "  removed: $skill_name"
    fi
  done
  echo "Done."
  exit 0
fi

mkdir -p "$SKILL_TARGET"
echo "Installing skills into $SKILL_TARGET ..."
for skill_path in "${SKILLS[@]}"; do
  skill_name=$(basename "$skill_path")
  src="$SCRIPT_DIR/$skill_path"
  target="$SKILL_TARGET/$skill_name"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    echo "  skipped (exists, not a symlink): $skill_name"
    continue
  fi
  ln -sfn "$src" "$target"
  echo "  linked: $skill_name → $src"
done
echo "Done. Restart OpenCode to pick up new skills."
