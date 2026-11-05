# Channel script skills

[![GitHub stars](https://img.shields.io/github/stars/Yuzakhodayari/channel-script-skills?style=flat)](https://github.com/Yuzakhodayari/channel-script-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Four agent skills for writing YouTube video scripts in a blended explainer voice. Run them in order:

**structure → storytelling → audience → language**

| skill | what it does |
| --- | --- |
| [`channel-structure`](skills/channel-structure) | Outlines, beat timing, strategy selection, sponsor and CTA placement |
| [`channel-storytelling`](skills/channel-storytelling) | Cold opens, story engines, tension, callbacks, endings |
| [`channel-audience`](skills/channel-audience) | Retention devices, re-hooks, emotional calibration, CTAs |
| [`channel-language`](skills/channel-language) | Sentence voice; humanizes AI-sounding narration; detector gate ≤ 2 |

Each skill is a folder with a `SKILL.md` (YAML `name` + `description`) and a `references/` directory.

## Install

### Antigravity / Gemini (one line)

```bash
npx skills add Yuzakhodayari/channel-script-skills -a antigravity -g -y
```

`npx skills` sometimes leaves the skills in `~/.agents/skills`. Copy them into the folder Antigravity loads:

```bash
mkdir -p ~/.gemini/config/skills
cp -R ~/.agents/skills/channel-* ~/.gemini/config/skills/
```

```powershell
New-Item -ItemType Directory -Force -Path "$HOME\.gemini\config\skills"
Copy-Item -Recurse -Force "$HOME\.agents\skills\channel-*" "$HOME\.gemini\config\skills\"
```

Restart Antigravity. The skills appear as `/channel-structure`, `/channel-storytelling`, `/channel-audience`, and `/channel-language`.

### Project-local

From your channel workspace (for example `your-channel-project/`):

```bash
npx skills add Yuzakhodayari/channel-script-skills -a antigravity -y
```

This installs into `./.agents/skills/`, which Antigravity discovers automatically.

### Claude Code / Codex

```bash
npx skills add Yuzakhodayari/channel-script-skills -a claude-code -g -y
```

Or clone the repo and use the install scripts:

```bash
./install.sh            # global: ~/.claude/skills, ~/.gemini/config/skills, ~/.codex/skills
./install.sh --project  # ./.claude/skills, ./.agent/skills, ./.agents/skills, ./.cursor/skills
```

```powershell
.\install.ps1
.\install.ps1 -Project
```

No skills folder? Paste a single `SKILL.md` at the top of a chat. You lose automatic discovery, but the rules still apply.

## Usage

1. `/channel-structure`: turn a topic and research notes into a timed outline.
2. `/channel-storytelling`: build the cold open, story engine, and ending.
3. `/channel-audience`: add re-hooks and retention devices, and place CTAs.
4. `/channel-language`: rewrite the narration into the channel voice and run the detector gate.

The skills write drafts. Review and publishing are up to you.

## Voice blend

The voice is a weighted blend of explainer channels. Art of the Problem, AI In Context, Max Fisher, Gen, and Maxinomics carry the most weight. ColdFusion, Johnny Harris, Species, and others are weighted lower as contrast.

Per-video weights and creator credits are in [`corpus/weights.csv`](corpus/weights.csv). Full transcripts are not included in this repo; see [`corpus/README.md`](corpus/README.md).

## Exam scores

Classic discrimination harness (deterministic rule solvers), weight-averaged 0–1:

| skill | score |
| --- | --- |
| channel-structure | 0.757 |
| channel-storytelling | 0.646 |
| channel-audience | 0.717 |
| channel-language | 0.838 |

These scores are a lexical proxy for how well the rules are applied. They are not a human judgement of script quality. Details are in each skill's `exams/`.

## Layout

```
skills/
  channel-structure/     SKILL.md  references/  exams/  README.md
  channel-storytelling/
  channel-audience/
  channel-language/
corpus/
  weights.csv  README.md
install.sh
install.ps1
LICENSE
NOTICE.md
```

## License

[MIT](LICENSE) © 2026 Youza Khodayari. See [NOTICE.md](NOTICE.md) for source attribution.
