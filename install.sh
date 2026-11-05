#!/usr/bin/env bash
# Installs the four channel skills for Claude Code, Antigravity/Gemini and Codex.
# Usage: ./install.sh            (global)
#        ./install.sh --project  (into ./.claude/skills, ./.agent/skills and ./.cursor/skills)
set -euo pipefail
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"
if [[ "${1:-}" == "--project" ]]; then
  # Project-local: preferred for channel work (portable, higher precedence)
  TARGETS=("$PWD/.claude/skills" "$PWD/.agent/skills" "$PWD/.agents/skills" "$PWD/.cursor/skills")
else
  # Global discovery paths
  # Antigravity/Gemini: ~/.gemini/config/skills/  (NOT ~/.gemini/antigravity/skills)
  TARGETS=("$HOME/.claude/skills" "$HOME/.gemini/config/skills" "$HOME/.codex/skills")
fi
for t in "${TARGETS[@]}"; do
  mkdir -p "$t"
  for s in "$SRC"/*/; do
    n="$(basename "$s")"; rm -rf "$t/$n"; cp -R "$s" "$t/$n"; echo "installed $n -> $t/$n"
  done
done
