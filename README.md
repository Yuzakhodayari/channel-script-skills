# Channel skills

Four agent skills (`SKILL.md` folders) that teach an AI agent to write YouTube scripts in one channel's blended style:

| skill | use it for |
|---|---|
| [`channel-storytelling`](skills/channel-storytelling) | cold opens, beats, tension, callbacks, endings |
| [`channel-structure`](skills/channel-structure) | outlines, beat timing, hook length, sponsor/CTA placement |
| [`channel-audience`](skills/channel-audience) | retention devices, re-hooks, emotional calibration, CTAs |
| [`channel-language`](skills/channel-language) | sentence voice; humanizing AI-sounding narration |

Use them in this order: structure, then storytelling, then audience, then language.

## Corpus weighting
Adam **7x** · Oil (Especially 03) **5x** · Gen **4x** · Especially AI/SpaceX/data-centers **3x** · After **1x**. Especially 04/05/07 count as Adam. Only host speech is used; guests and clips are filtered out.

## Install (one command)
```bash
git clone <this-repo> channel-skills && cd channel-skills && ./install.sh          # macOS/Linux, global
./install.sh --project                                                             # into the current project
```
```powershell
git clone <this-repo> channel-skills; cd channel-skills; .\install.ps1            # Windows
```
It copies `skills/*` into `~/.claude/skills` (Claude Code), `~/.gemini/antigravity/skills` (Antigravity) and `~/.codex/skills` (Codex). For Cursor, use `--project`, which also writes `.cursor/skills`. Each skill's README has manual steps.

## Scores
The 100-item held-out exams use whole TEST videos that were never used to write or select rules. Scores are weight-averaged.

| skill | v1 reported (online exam) | v1 rules on new held-out test | v2 round 1 | v2 round 2 |
|---|---|---|---|---|
| channel-storytelling | 0.56 | 0.549 | 0.533 | 0.646 |
| channel-structure | 0.69 | 0.61 | 0.757 | 0.722 |
| channel-audience | 0.68 | 0.636 | 0.717 | 0.69 |
| channel-language | 0.838 (0.933 late) | n/a | not changed | not changed |

Per-task tables are in each skill's README and `exams/heldout-2026.md`. **None of the three retrained skills reached 0.80 on the held-out test.** The causes are in "Honest caveats" below.

## How the skills were improved (v2)
There were five training methods on top of the old exam loop. All were induced on TRAIN videos and accepted or rejected on VAL videos:
1. **Contrastive pairs**: real line vs its most confusable distractor (`training/method1-contrastive-pairs.md`).
2. **Reverse outlines and position-signature tables** for the 0-10%, 10-80% and 80-100% buckets (`references/position-signatures.md`).
3. **Shuffle-reorder and rewrite-diff** (`training/method3-shuffle-reorder.md`).
4. **Worked examples**: 35-36 per skill, with misses kept (`training/worked-examples.md`).
5. **Rule induction with a held-out accept/reject log** (`training/rule-log.md`).

The tooling is in `tools/heldout-v2/` (v2) and `tools/v1-build/` (v1 story and language harness). Transcripts are **not** included; set `CHANNEL_CORPUS_DIR` to rebuild.

## Honest caveats
- The exams are scored by deterministic regex and logistic-regression harnesses: a lexical proxy for how well an agent applies the skill, not a human judgement.
- Opener tasks (story A, structure T3, audience A2) have only 14 training openers. The rules overfit validation (story A val 0.86, test 0.18 in round 1).
- Structure T1/T2 gold labels come from the same beat regexes the skill teaches, so those scores are optimistic.
- During the work the builder saw the first sentences of the test videos once, while listing all openers. Opener phrase lists were then restricted to TRAIN-only patterns, and no blind model-reader exam was run because it would be contaminated.
- Personal use, no license. The references quote short excerpts of third-party creators; keep the repo private.
