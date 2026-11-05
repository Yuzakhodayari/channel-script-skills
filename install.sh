#!/usr/bin/env bash
# Installs the four channel skills for Claude Code, Antigravity/Gemini and Codex.
# Usage: ./install.sh            (global)
#        ./install.sh --project  (into ./.claude/skills, ./.agent/skills and ./.cursor/skills of the current dir)
set -euo pipefail
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"
if [[ "${1:-}" == "--project" ]]; then
  TARGETS=("$PWD/.claude/skills" "$PWD/.agent/skills" "$PWD/.cursor/skills")
else
  TARGETS=("$HOME/.claude/skills" "$HOME/.gemini/antigravity/skills" "$HOME/.codex/skills")
fi
for t in "${TARGETS[@]}"; do
  mkdir -p "$t"
  for s in "$SRC"/*/; do
    n="$(basename "$s")"; rm -rf "$t/$n"; cp -R "$s" "$t/$n"; echo "installed $n -> $t/$n"
  done
done
