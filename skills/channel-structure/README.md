# channel-structure

Stage 1/4 — outlines, beat timing, strategy selection, sponsor/CTA placement.

Pipeline order: **structure → storytelling → audience → language**.

## Layout

- `SKILL.md` — entry point (YAML frontmatter + rules)
- `references/` — patterns, drills, pipeline, strategy selector, detector gate
- `exams/` — optional classic harness scores (see `exams/README.md`)

## Install

**Claude Code**
```bash
# global
mkdir -p ~/.claude/skills && cp -R channel-structure ~/.claude/skills/channel-structure
# or project-local
mkdir -p .claude/skills && cp -R channel-structure .claude/skills/channel-structure
```

**Antigravity / Gemini**
```bash
# global — Antigravity loads ~/.gemini/config/skills (not ~/.gemini/antigravity/skills)
mkdir -p ~/.gemini/config/skills && cp -R channel-structure ~/.gemini/config/skills/channel-structure
# or project-local
mkdir -p .agents/skills && cp -R channel-structure .agents/skills/channel-structure
```

From the repo root:

```bash
./install.sh            # or ./install.ps1 on Windows
npx skills add Yuzakhodayari/channel-script-skills -a antigravity -g -y
```

## Corpus

Built from **117** weighted transcripts under [`../../corpus/`](../../corpus/) (see [`weights.csv`](../../corpus/weights.csv)). Non-host speech filtered where applicable.

## License

MIT for the skills. See [`LICENSE`](../../LICENSE) and [`NOTICE.md`](../../NOTICE.md). Transcripts in `corpus/` remain with their creators.
