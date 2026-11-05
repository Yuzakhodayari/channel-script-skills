# channel-structure

Structure and strategy: outlines, beat timing, hook length, sponsor and CTA placement, section turns.

This is an agent skill (a `SKILL.md` folder) built from transcripts of the creators in the channel blend: **Adam 7x, Gen 4x, Oil 5x, Especially (AI/SpaceX/data-centers) 3x, After 1x**. Only host speech is used.

> **Personal use.** This skill was built for one creator's channel. It has no license and is not for redistribution. The reference files quote short excerpts of third-party videos for analysis; keep the repo private.

## What's inside
| path | contents |
|---|---|
| `SKILL.md` | The skill: rules, workflow and v2 checklists (frontmatter `name: channel-structure`) |
| `references/` | Criteria, examples, anti-patterns, and the v2 `position-signatures.md` (reverse-outline tables) |
| `training/` | `training/` L1-L5 plus v2 method files: `method1-contrastive-pairs.md`, `method3-shuffle-reorder.md`, `worked-examples.md`, `rule-log.md` |
| `exams/` | v1 exams and logs, plus `heldout-2026.md` (the v2 held-out exam) |
| `sample.md` | A sample output |
| `build/` (if present) | v1 build and exam scripts |

## Install
Copy the whole folder (not just `SKILL.md`):
- **Claude Code**, all projects: `~/.claude/skills/channel-structure/`. One project only: `<project>/.claude/skills/channel-structure/`.
- **Antigravity / Gemini**: `~/.gemini/antigravity/skills/channel-structure/` (or `<workspace>/.agent/skills/channel-structure/`).
- **Cursor**: `<project>/.cursor/skills/channel-structure/`, or paste `SKILL.md` into a Project Rule (`.cursor/rules/channel-structure.mdc`) and keep `references/` alongside.
- **Codex CLI**: `~/.codex/skills/channel-structure/`, or reference `SKILL.md` from `AGENTS.md`.
- Or run `install.sh` / `install.ps1` from the repo root.

Trigger it by asking for what the description lists, for example "outline this video with sponsor placement".

## How to train (re-run the methods)
You need the transcripts, which are not shipped. Put them in a corpus folder (`adam-transcripts/*.txt`, `transcripts/<n>.txt`, `other-transcripts/especially/*.txt`, `other-transcripts/after/*.txt`) and set `CHANNEL_CORPUS_DIR` to that folder. Then, from `tools/heldout-v2/` in the repo:
```bash
python3 story_learn.py; python3 structure_learn.py; python3 audience_learn.py   # TRAIN induces, VAL accepts or rejects
python3 round2_cv.py                                                          # optional round 2
python3 build_docs.py && python3 write_skillmd.py                             # regenerate training/ and the checklists
```
The split is in `split.py` and is by whole video, so no video appears in two splits.

## How to run the exams
```bash
cd tools/heldout-v2 && python3 exam_runner.py        # round 1, writes final_scores.json
python3 exam_runner.py r2                            # round 2
```
v1 exams: `python3 build/run_exams.py` (structure and audience), or `tools/v1-build/exams.py` (story and language).

## Latest scores
| task | before (v1) | after round 1 | after round 2 |
|---|---|---|---|
| T1 | 0.494 | 0.753 | 0.753 |
| T2 | 0.427 | 0.787 | 0.787 |
| T3 | 0.343 | 0.457 | 0.229 |
| T4 | 0.87 | 0.87 | 0.87 |
| T5 | 0.928 | 0.928 | 0.928 |
| T6 | 0.617 | 0.726 | 0.726 |
| overall | 0.61 | 0.757 | 0.722 |

The exam has 100 items drawn only from held-out TEST videos, with seed 2026, weight-averaged. Round 1 rules were selected on VAL. Round 2 used leave-one-video-out CV on TRAIN+VAL. Both rounds are shown because each one wins on different tasks, and picking per task from test results would be tuning on the test set.
