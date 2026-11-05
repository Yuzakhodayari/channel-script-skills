# Channel script skills

Four private agent skills that write YouTube scripts in one channel's blended voice. Pipeline order matters:

**structure → storytelling → audience → language**

Nothing publishes itself. These skills write. You ship.

| skill | what it does |
| --- | --- |
| [`channel-structure`](skills/channel-structure) | Outlines, beat timing, strategy selection, sponsor/CTA placement |
| [`channel-storytelling`](skills/channel-storytelling) | Cold opens, story engines, tension, callbacks, endings |
| [`channel-audience`](skills/channel-audience) | Retention devices, re-hooks, emotional calibration, CTAs |
| [`channel-language`](skills/channel-language) | Sentence voice; humanize AI-sounding narration; detector gate ≤ 2 |

Each skill is a folder with `SKILL.md` + `references/`. Optional classic exam scores live under `exams/`.

## Install

### One command (Claude Code + Antigravity + Codex)

```bash
git clone git@github.com:Yuzakhodayari/channel-script-skills.git
cd channel-script-skills
./install.sh            # global: ~/.claude/skills, ~/.gemini/config/skills, ~/.codex/skills
./install.sh --project  # into ./.claude/skills, ./.agent/skills, ./.agents/skills, ./.cursor/skills
```

```powershell
git clone git@github.com:Yuzakhodayari/channel-script-skills.git
cd channel-script-skills
.\install.ps1           # Windows
.\install.ps1 -Project
```

**Prefer `--project` / `-Project` for channel work.** Skills stay inside the YouTube workspace, travel with the folder, and beat global skills on name collisions.

### Claude Code (manual)

```bash
cp -R skills/channel-* ~/.claude/skills/
# or project-local
mkdir -p .claude/skills && cp -R skills/channel-* .claude/skills/
```

### Antigravity / Gemini

Antigravity discovers skills in `~/.gemini/config/skills/` (not `~/.gemini/antigravity/skills`). On Windows that is `C:\Users\<you>\.gemini\config\skills\<skill-name>\SKILL.md`.

```bash
# Global
mkdir -p ~/.gemini/config/skills
cp -R skills/channel-* ~/.gemini/config/skills/

# Project-local (recommended for a YouTube workspace)
mkdir -p .agent/skills
cp -R skills/channel-* .agent/skills/
```

```powershell
# Global
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills"
Copy-Item -Recurse -Force .\skills\channel-* "$HOME\.gemini\config\skills\"

# Project-local (recommended)
New-Item -ItemType Directory -Force -Path ".agent\skills"
Copy-Item -Recurse -Force .\skills\channel-* ".agent\skills\"
```

Each skill folder must keep its own `SKILL.md` with YAML `name` and `description` frontmatter (already present). Without that, Antigravity skips the folder.

Paste any single `SKILL.md` at the top of a chat if you are not using a skills folder. You lose automatic discovery; the rules still run as a mode.

## Corpus

**117** weighted transcripts under [`corpus/`](corpus/), one folder per creator, plus [`corpus/weights.csv`](corpus/weights.csv).

| creator | role in the blend |
| --- | --- |
| `ai-in-context` | highest weight (Adam-style deep dive) |
| `max-fisher` | high-weight narrative news deep dive |
| `gen` | the owner's channel |
| `maxinomics` | object-demo / mechanism stories |
| `art-of-the-problem` | explanatory story craft |
| `especially-misc` | SpaceX / AI / data-center essays |
| others (`coldfusion`, `johnny-harris`, `species`, …) | lower-weight contrast |

Exact per-video weights and inclusion notes are in `corpus/weights.csv`. Non-host speech is filtered where the source allows.

## Classic exam scores (honest)

Optional. Re-run of the **original** discrimination harnesses (deterministic solvers, held-out or fold-in). Weight-averaged 0–1.

| skill | classic after |
| --- | --- |
| channel-storytelling | **0.646** |
| channel-structure | **0.757** |
| channel-audience | **0.717** |
| channel-language | **0.838** |

Per-task tables: each skill's `exams/heldout-2026.md` and `exams/scores.csv`.

A later rewrite-script exam pack that scored near 1.0 was **rejected** — those grades were not real. Do not treat them as progress. The numbers above are the comparable classic harness.

These scores are a lexical proxy for how well a rule solver applies the skill, not a human judgement of agent output.

## Layout

```
skills/
  channel-structure/     SKILL.md  references/  exams/  README.md
  channel-storytelling/  …
  channel-audience/      …
  channel-language/      …
corpus/
  <creator>/*.txt
  weights.csv
install.sh
install.ps1
NOTICE.md
```

## Private

Personal use. Keep this repository private. See `NOTICE.md`.
