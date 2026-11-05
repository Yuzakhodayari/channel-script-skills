# channel-audience

Stage 3/4 — retention devices, re-hooks, emotional calibration, CTAs.

Pipeline order: **structure → storytelling → audience → language**.

## Layout

- `SKILL.md` — entry point (YAML frontmatter + rules)
- `references/` — patterns, drills, pipeline, strategy selector, detector gate
- `exams/` — optional classic harness scores (see `exams/README.md`)

## Install

**Claude Code**
```bash
# global
mkdir -p ~/.claude/skills && cp -R channel-audience ~/.claude/skills/channel-audience
# or project-local
mkdir -p .claude/skills && cp -R channel-audience .claude/skills/channel-audience
```

**Antigravity / Gemini**
```bash
mkdir -p ~/.gemini/antigravity/skills && cp -R channel-audience ~/.gemini/antigravity/skills/channel-audience
# or project-local
mkdir -p .agent/skills && cp -R channel-audience .agent/skills/channel-audience
```

From the repo root you can also run `./install.sh` (or `./install.ps1` on Windows) to install all four skills at once.

## Corpus

Built from **117** weighted transcripts under `../../corpus/` (see `corpus/weights.csv`). Non-host speech filtered where applicable.
