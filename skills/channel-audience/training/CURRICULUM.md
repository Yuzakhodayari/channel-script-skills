# Curriculum: learn it, don't just read it

This curriculum trains device spotting, hook/close placement, real-vs-flattened, creator attribution, punch-up rewrites against **real transcript gold**. Reading the skill is step 0. You learn by answering before you look.

## How to run a session (30-60 min)
1. Pick the lowest level you have not yet passed twice in a row.
2. Open the drill file and answer **every** item in a scratch file without opening answer-keys.md. Write your reasoning in one line per item.
3. Open `answer-keys.md` and score with `rubric.md`.
4. For every miss, write a row in `lessons-learned.md`: item id, what you answered, the gold answer, *which rule or criterion would have caught it*, and the fix to your mental rule.
5. If one rule keeps causing misses, re-read that criterion in `references/criteria.md` and its rows in `references/device-catalog.md`.
6. Pass mark: ≥80% on L1-L3, ≥3/4 average on L4, ≥16/20 (structure) or ≥18/22 (audience) on L5. Pass twice before moving up.
7. After every 10 scored items, re-read your last 10 lessons and keep only the ones that generalise. Promote recurring ones into SKILL.md "Lessons from the exams" (append; never delete the measured norms).

## Levels
| level | file | skill trained | gold source |
|---|---|---|---|
| L1 | `L1-recognition.md` | recognise the unit (beat label / device) | detector labels on real host lines |
| L2 | `L2-placement.md` | place it in time | real % positions |
| L3 | `L3-discrimination.md` | discriminate real from wrong (openers, mode, flattened lines, creator) | real transcripts |
| L4 | `L4-rewrite.md` | reconstruct / restore | gold beat maps / original lines |
| L5 | `L5-production.md` | produce original work | rubric + criteria tests |

## Regenerating fresh drills
`cd build && python3 build_train.py` regenerates L1-L4 with new seeds. Change the seed numbers in the `mk(...)` plan. Items are sampled by corpus weight, so you'll see Adam and Gen most.

## Running the full exam
`cd build && python3 build_exams.py` re-runs all 100 exams with the codified solver and rewrites `exams/`. To grade **yourself**, read `exams/exams.md` with the Gold and Taken-answer lines covered, answer, then score with `exams/rubric.md`.
