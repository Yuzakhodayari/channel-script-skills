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
# global — Antigravity loads ~/.gemini/config/skills (not ~/.gemini/antigravity/skills)
mkdir -p ~/.gemini/config/skills && cp -R channel-audience ~/.gemini/config/skills/channel-audience
# or project-local
mkdir -p .agents/skills && cp -R channel-audience .agents/skills/channel-audience
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
