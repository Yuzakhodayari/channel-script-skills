# channel-storytelling

Stage 2/4 — cold opens, story engines, tension, callbacks, endings.

Pipeline order: **structure → storytelling → audience → language**.

## Layout

- `SKILL.md` — entry point (YAML frontmatter + rules)
- `references/` — patterns, drills, pipeline, strategy selector, detector gate
- `exams/` — optional classic harness scores (see `exams/README.md`)

## Install

**Claude Code**
```bash
# global
mkdir -p ~/.claude/skills && cp -R channel-storytelling ~/.claude/skills/channel-storytelling
# or project-local
mkdir -p .claude/skills && cp -R channel-storytelling .claude/skills/channel-storytelling
```

**Antigravity / Gemini**
```bash
mkdir -p ~/.gemini/config/skills && cp -R channel-storytelling ~/.gemini/config/skills/channel-storytelling
# or project-local
mkdir -p .agent/skills && cp -R channel-storytelling .agent/skills/channel-storytelling
```

From the repo root you can also run `./install.sh` (or `./install.ps1` on Windows) to install all four skills at once.

## Corpus

Trained on a weighted set of 117 third-party transcripts. Full transcripts are not shipped; see [`corpus/weights.csv`](../../corpus/weights.csv) for per-video weights and creator credits.
