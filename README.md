# Channel script skills

Four agent skills that write YouTube scripts in one channel's blended voice. Pipeline order matters:

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

### One line from GitHub (Gemini / Antigravity)

Paste this into Antigravity or run it in a terminal:

```bash
npx skills add Yuzakhodayari/channel-script-skills -a antigravity -g -y
```

That installs all four `channel-*` skills. Then copy them into the folder Antigravity actually loads (the `npx skills` tool sometimes leaves them in `~/.agents/skills`):

```bash
mkdir -p ~/.gemini/config/skills
cp -R ~/.agents/skills/channel-* ~/.gemini/config/skills/
```

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills"
Copy-Item -Recurse -Force "$HOME\.agents\skills\channel-*" "$HOME\.gemini\config\skills\"
```

Restart Antigravity. Skills show up as `/channel-language`, `/channel-storytelling`, `/channel-structure`, `/channel-audience`.

The repo is public, so no token is needed. If a clone ever fails, log into GitHub first (`gh auth login`).

### Project-local (recommended for a YouTube workspace)

From your channel folder:

```bash
npx skills add Yuzakhodayari/channel-script-skills -a antigravity -y
# lands in ./.agents/skills/ — Antigravity discovers that automatically
```

Or clone once and copy:

```powershell
git clone https://github.com/Yuzakhodayari/channel-script-skills.git
Copy-Item -Recurse -Force .\channel-script-skills\skills\channel-* ".agents\skills\"
```

### Claude Code / Codex (same repo)

```bash
npx skills add Yuzakhodayari/channel-script-skills -a claude-code -g -y
# or
./install.sh            # global: ~/.claude/skills, ~/.gemini/config/skills, ~/.codex/skills
./install.sh --project  # ./.claude/skills, ./.agent/skills, ./.agents/skills, ./.cursor/skills
```

```powershell
.\install.ps1
.\install.ps1 -Project
```

Each skill folder already has `SKILL.md` with YAML `name` + `description`. Antigravity skips folders that lack that frontmatter.

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
LICENSE
NOTICE.md
```

## License

MIT for the skills and install scripts. See [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md). Third-party transcripts in `corpus/` stay with their creators.
