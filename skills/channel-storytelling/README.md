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
# global — Antigravity loads ~/.gemini/config/skills (not ~/.gemini/antigravity/skills)
mkdir -p ~/.gemini/config/skills && cp -R channel-storytelling ~/.gemini/config/skills/channel-storytelling
# or project-local
mkdir -p .agents/skills && cp -R channel-storytelling .agents/skills/channel-storytelling
```

From the repo root you can also run `./install.sh` (or `./install.ps1` on Windows) to install all four skills at once, or:

```bash
npx skills add Yuzakhodayari/channel-script-skills -a antigravity -g -y
```

## Corpus

Built from **117** weighted transcripts under [`../../corpus/`](../../corpus/) (see [`weights.csv`](../../corpus/weights.csv)). Non-host speech filtered where applicable.

## License

MIT for the skills. See [`LICENSE`](../../LICENSE) and [`NOTICE.md`](../../NOTICE.md). Transcripts in `corpus/` stay with their creators.
