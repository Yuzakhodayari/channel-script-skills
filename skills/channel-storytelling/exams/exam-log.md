# Exam log (story)

## How these exams were run (read this)
The exams were run by a deterministic harness that implements this skill's rules as code: feature scorers for discrimination and placement, and a rule-based humanizer for rewrites. It does not use an independent model's free judgement. The harness started with one base rule per exam type. Every 10 exams, the miss types that a still-inactive rule would have fixed switched that rule on, and its lesson was written into SKILL.md and references/criteria.md. So the curve measures how much the folded rules help on new, unseen passages.

**Contamination notes:** (1) The AI versions come from my own transformer (pool.aiify), and the humanizer knows the general shape of those transforms. That makes type C easier than real-world AI text. (2) Opener statistics are rebuilt without the exam's own file, but the same creator's other files stay in. (3) The rules were designed by the same author who wrote the skill. (4) Training passages were excluded from the exam pool.

## Curve
| window | all | type A | type B | type C |
|---|---|---|---|---|

| 1-10 | 0.500 | 0.333 | 1.000 | 0.500 |
| 11-20 | 0.600 | 0.333 | 0.333 | 1.000 |
| 21-30 | 0.600 | 0.800 | 0.000 | 0.667 |
| 31-40 | 0.700 | 0.750 | 0.750 | 0.500 |
| 41-50 | 0.600 | 1.000 | 0.200 | 1.000 |
| 51-60 | 0.600 | 0.500 | 0.500 | 0.750 |
| 61-70 | 0.600 | 0.600 | 0.500 | 0.667 |
| 71-80 | 0.700 | 0.667 | 0.750 | 0.667 |
| 81-90 | 0.200 | 0.333 | 0.200 | 0.000 |
| 91-100 | 0.500 | 0.333 | 0.600 | 0.500 |

**Early (1-20) avg 0.550 vs late (81-100) avg 0.350.** 1-30 0.567 vs 71-100 0.467. Overall 0.560. By type: A 0.600, B 0.457, C 0.633.

## Folds

- after exam 10: Use the placement table in criteria.md: each criterion has a first-10% and last-10% share. Sum them over a passage (a naive-Bayes vote) to judge whether it reads as an open, a middle, or a close. Hook and stakes moves pull toward the open. Callbacks, projections, and sign-offs pull toward the close. [validated: +2.00 on 3 past type-A items]
- after exam 10: The true next beat keeps the same named entities (capitalized names, products, places) as the passage. Weight entity overlap over plain word overlap. [validated: +1.00 on 6 past type-C items]
- after exam 40: Use the placement table in criteria.md: each criterion has a first-10% and last-10% share. Sum them over a passage (a naive-Bayes vote) to judge whether it reads as an open, a middle, or a close. Hook and stakes moves pull toward the open. Callbacks, projections, and sign-offs pull toward the close. [validated: +1.00 on 10 past type-B items]
- after exam 50: Callbacks ("remember", "like I said", "back to", "that's why") belong to the middle and late sections, never the open. [validated: +3.00 on 15 past type-B items]

## Per-exam record
| # | type | source | gold | answer | score | miss -> rule |
|---|---|---|---|---|---|---|
| 1 | C | gen `2.txt` | C | B | 0.0 | no-rule-fixes |
| 2 | A | gen `8.txt` | C | B | 0.0 | nb |
| 3 | C | gen `8.txt` | B | A | 0.0 | no-rule-fixes |
| 4 | C | adam `02-bestselling-book.txt` | A | A | 1.0 |  |
| 5 | A | adam `01-ai-disaster.txt` | C | A | 0.0 | event |
| 6 | A | adam `05-sam-altman.txt` | B | B | 1.0 |  |
| 7 | C | adam `04-superintelligence.txt` | C | C | 1.0 |  |
| 8 | C | especially `06-data-centers.txt` | A | C | 0.0 | entity |
| 9 | C | gen `9.txt` | B | B | 1.0 |  |
| 10 | B | gen `6.txt` | middle | middle | 1.0 |  | **FOLD:** nb, entity, tried open_promise on type B: rejected (would lose 1.00 on 1 past items)
| 11 | A | gen `4.txt` | A | B | 0.0 | no-rule-fixes |
| 12 | B | gen `8.txt` | open | middle | 0.0 | nb |
| 13 | B | adam `02-bestselling-book.txt` | middle | middle | 1.0 |  |
| 14 | B | gen `1.txt` | close | middle | 0.0 | no-rule-fixes |
| 15 | C | adam `02-bestselling-book.txt` | B | B | 1.0 |  |
| 16 | A | oil `03-oil-apocalypse.txt` | A | D | 0.0 | q |
| 17 | C | adam `01-ai-disaster.txt` | A | A | 1.0 |  |
| 18 | C | especially `06-data-centers.txt` | A | A | 1.0 |  |
| 19 | C | adam `01-ai-disaster.txt` | B | B | 1.0 |  |
| 20 | A | gen `9.txt` | A | A | 1.0 |  | **FOLD:** no rule passed validation, tried you on type A: rejected (would lose 1.00 on 6 past items), tried open_promise on type B: rejected (would lose 1.00 on 4 past items), tried pronoun on type C: rejected (would lose 1.00 on 10 past items)
| 21 | C | adam `04-superintelligence.txt` | A | A | 1.0 |  |
| 22 | C | adam `05-sam-altman.txt` | C | A | 0.0 | no-rule-fixes |
| 23 | A | especially `06-data-centers.txt` | A | A | 1.0 |  |
| 24 | A | adam `01-ai-disaster.txt` | D | D | 1.0 |  |
| 25 | A | adam `01-ai-disaster.txt` | C | C | 1.0 |  |
| 26 | C | after `01-dark-side-data-centers.txt` | C | C | 1.0 |  |
| 27 | A | gen `3.txt` | B | D | 0.0 | no-rule-fixes |
| 28 | A | adam `01-ai-disaster.txt` | A | A | 1.0 |  |
| 29 | B | after `11-anthropic-ipo.txt` | close | middle | 0.0 | no-rule-fixes |
| 30 | B | after `04-pov-ai.txt` | open | middle | 0.0 | no-rule-fixes | **FOLD:** no rule passed validation, tried you on type A: rejected (would lose 1.00 on 11 past items), tried open_promise on type B: rejected (would lose 1.00 on 6 past items), tried pronoun on type C: rejected (would lose 1.00 on 13 past items)
| 31 | B | adam `02-bestselling-book.txt` | middle | middle | 1.0 |  |
| 32 | C | adam `05-sam-altman.txt` | B | B | 1.0 |  |
| 33 | B | adam `02-bestselling-book.txt` | open | middle | 0.0 | open_promise |
| 34 | B | adam `04-superintelligence.txt` | middle | middle | 1.0 |  |
| 35 | A | gen `6.txt` | D | D | 1.0 |  |
| 36 | C | adam `02-bestselling-book.txt` | A | C | 0.0 | pronoun |
| 37 | B | gen `9.txt` | middle | middle | 1.0 |  |
| 38 | A | adam `01-ai-disaster.txt` | D | D | 1.0 |  |
| 39 | A | adam `02-bestselling-book.txt` | D | D | 1.0 |  |
| 40 | A | especially `06-data-centers.txt` | B | C | 0.0 | no-rule-fixes | **FOLD:** nb, tried you on type A: rejected (would lose 1.00 on 15 past items), tried event on type A: rejected (would lose 1.00 on 15 past items), tried open_promise on type B: rejected (would lose 1.00 on 10 past items)
| 41 | B | adam `05-sam-altman.txt` | close | close | 1.0 |  |
| 42 | A | adam `05-sam-altman.txt` | B | B | 1.0 |  |
| 43 | B | gen `5.txt` | middle | close | 0.0 | no-rule-fixes |
| 44 | A | gen `2.txt` | B | B | 1.0 |  |
| 45 | A | adam `05-sam-altman.txt` | D | D | 1.0 |  |
| 46 | B | adam `01-ai-disaster.txt` | middle | close | 0.0 | callback |
| 47 | B | gen `10.txt` | close | open | 0.0 | no-rule-fixes |
| 48 | A | after `08-tokens.txt` | A | A | 1.0 |  |
| 49 | B | after `09-microchip-war.txt` | middle | open | 0.0 | callback |
| 50 | C | gen `8.txt` | A | A | 1.0 |  | **FOLD:** callback, tried you on type A: rejected (would lose 1.00 on 19 past items), tried event on type A: rejected (would lose 2.00 on 19 past items), tried open_promise on type B: rejected (would lose 3.00 on 15 past items)
| 51 | C | adam `05-sam-altman.txt` | A | A | 1.0 |  |
| 52 | C | adam `05-sam-altman.txt` | B | B | 1.0 |  |
| 53 | A | gen `9.txt` | B | C | 0.0 | no-rule-fixes |
| 54 | A | gen `8.txt` | B | B | 1.0 |  |
| 55 | B | adam `02-bestselling-book.txt` | middle | close | 0.0 | no-rule-fixes |
| 56 | B | adam `03-no-longer-in-control.txt` | close | close | 1.0 |  |
| 57 | B | gen `3.txt` | open | close | 0.0 | no-rule-fixes |
| 58 | B | especially `06-data-centers.txt` | middle | middle | 1.0 |  |
| 59 | C | gen `3.txt` | A | B | 0.0 | no-rule-fixes |
| 60 | C | adam `01-ai-disaster.txt` | A | A | 1.0 |  | **FOLD:** no rule passed validation, tried you on type A: rejected (would lose 1.00 on 21 past items), tried event on type A: rejected (would lose 2.00 on 21 past items), tried close_cta on type B: rejected (would lose 1.00 on 19 past items)
| 61 | B | especially `06-data-centers.txt` | middle | middle | 1.0 |  |
| 62 | C | gen `1.txt` | B | B | 1.0 |  |
| 63 | C | gen `3.txt` | A | C | 0.0 | no-rule-fixes |
| 64 | A | adam `03-no-longer-in-control.txt` | A | B | 0.0 | no-rule-fixes |
| 65 | A | adam `05-sam-altman.txt` | D | D | 1.0 |  |
| 66 | A | adam `05-sam-altman.txt` | B | B | 1.0 |  |
| 67 | B | especially `01-spacex.txt` | middle | close | 0.0 | no-rule-fixes |
| 68 | A | adam `02-bestselling-book.txt` | B | B | 1.0 |  |
| 69 | A | gen `4.txt` | B | D | 0.0 | no-rule-fixes |
| 70 | C | adam `02-bestselling-book.txt` | A | A | 1.0 |  | **FOLD:** no rule passed validation, tried you on type A: rejected (would lose 1.00 on 26 past items), tried event on type A: rejected (would lose 2.00 on 26 past items), tried close_cta on type B: rejected (would lose 1.00 on 21 past items)
| 71 | A | gen `9.txt` | C | B | 0.0 | no-rule-fixes |
| 72 | C | adam `01-ai-disaster.txt` | A | A | 1.0 |  |
| 73 | A | adam `04-superintelligence.txt` | D | D | 1.0 |  |
| 74 | B | adam `05-sam-altman.txt` | close | close | 1.0 |  |
| 75 | B | gen `6.txt` | open | open | 1.0 |  |
| 76 | A | adam `01-ai-disaster.txt` | C | C | 1.0 |  |
| 77 | C | gen `1.txt` | C | B | 0.0 | no-rule-fixes |
| 78 | B | adam `03-no-longer-in-control.txt` | open | middle | 0.0 | no-rule-fixes |
| 79 | B | adam `04-superintelligence.txt` | middle | middle | 1.0 |  |
| 80 | C | gen `2.txt` | B | B | 1.0 |  | **FOLD:** no rule passed validation, tried you on type A: rejected (would lose 1.00 on 29 past items), tried event on type A: rejected (would lose 2.00 on 29 past items), tried close_cta on type B: rejected (would lose 1.00 on 25 past items)
| 81 | A | after `06-diamonds.txt` | A | D | 0.0 | no-rule-fixes |
| 82 | C | gen `2.txt` | C | A | 0.0 | pronoun |
| 83 | B | after `05-middle-class.txt` | close | middle | 0.0 | no-rule-fixes |
| 84 | B | adam `02-bestselling-book.txt` | open | middle | 0.0 | open_promise |
| 85 | A | after `02-greed.txt` | C | B | 0.0 | no-rule-fixes |
| 86 | B | adam `05-sam-altman.txt` | close | close | 1.0 |  |
| 87 | A | adam `02-bestselling-book.txt` | D | D | 1.0 |  |
| 88 | B | especially `01-spacex.txt` | middle | close | 0.0 | no-rule-fixes |
| 89 | C | after `01-dark-side-data-centers.txt` | C | A | 0.0 | no-rule-fixes |
| 90 | B | adam `01-ai-disaster.txt` | open | middle | 0.0 | no-rule-fixes | **FOLD:** no rule passed validation, tried q on type A: rejected (would lose 1.00 on 32 past items), tried you on type A: rejected (would lose 1.00 on 32 past items), tried event on type A: rejected (would lose 2.00 on 32 past items)
| 91 | B | adam `04-superintelligence.txt` | middle | middle | 1.0 |  |
| 92 | B | especially `01-spacex.txt` | close | close | 1.0 |  |
| 93 | B | adam `05-sam-altman.txt` | open | open | 1.0 |  |
| 94 | A | adam `03-no-longer-in-control.txt` | D | A | 0.0 | q |
| 95 | A | adam `01-ai-disaster.txt` | B | B | 1.0 |  |
| 96 | C | adam `01-ai-disaster.txt` | C | B | 0.0 | no-rule-fixes |
| 97 | B | gen `6.txt` | middle | close | 0.0 | no-rule-fixes |
| 98 | C | after `10-water.txt` | A | A | 1.0 |  |
| 99 | B | after `12-data-centres-not-working.txt` | open | middle | 0.0 | no-rule-fixes |
| 100 | A | gen `3.txt` | A | C | 0.0 | no-rule-fixes | **FOLD:** no rule passed validation, tried you on type A: rejected (would lose 2.00 on 35 past items), tried event on type A: rejected (would lose 2.00 on 35 past items), tried close_cta on type B: rejected (would lose 1.00 on 35 past items)