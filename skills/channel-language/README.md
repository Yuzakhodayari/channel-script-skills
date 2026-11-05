# channel-language

Stage 4/4 — sentence voice; humanize AI-sounding narration; detector gate ≤2.

Pipeline order: **structure → storytelling → audience → language**.

## Layout

- `SKILL.md` — entry point (YAML frontmatter + rules)
- `references/` — patterns, drills, pipeline, strategy selector, detector gate
- `exams/` — optional classic harness scores (see `exams/README.md`)

## Install

**Claude Code**
```bash
# global
mkdir -p ~/.claude/skills && cp -R channel-language ~/.claude/skills/channel-language
# or project-local
mkdir -p .claude/skills && cp -R channel-language .claude/skills/channel-language
```

**Antigravity / Gemini**
```bash
mkdir -p ~/.gemini/antigravity/skills && cp -R channel-language ~/.gemini/antigravity/skills/channel-language
# or project-local
mkdir -p .agent/skills && cp -R channel-language .agent/skills/channel-language
```

From the repo root you can also run `./install.sh` (or `./install.ps1` on Windows) to install all four skills at once.

## Corpus

Built from **117** weighted transcripts under `../../corpus/` (see `corpus/weights.csv`). Non-host speech filtered where applicable.
