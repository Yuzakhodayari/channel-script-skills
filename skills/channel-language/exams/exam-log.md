# Exam log (lang)

## How these exams were run (read this)
The exams were run by a deterministic harness that implements this skill's rules as code: feature scorers for discrimination and placement, and a rule-based humanizer for rewrites. It does not use an independent model's free judgement. The harness started with one base rule per exam type. Every 10 exams, the miss types that a still-inactive rule would have fixed switched that rule on, and its lesson was written into SKILL.md and references/criteria.md. So the curve measures how much the folded rules help on new, unseen passages.

**Contamination notes:** (1) The AI versions come from my own transformer (pool.aiify), and the humanizer knows the general shape of those transforms. That makes type C easier than real-world AI text. (2) Opener statistics are rebuilt without the exam's own file, but the same creator's other files stay in. (3) The rules were designed by the same author who wrote the skill. (4) Training passages were excluded from the exam pool.

## Curve
| window | all | type A | type B | type C |
|---|---|---|---|---|

| 1-10 | 0.722 | 1.000 | 0.600 | 0.804 |
| 11-20 | 0.564 | 0.333 | 0.600 | 0.819 |
| 21-30 | 0.926 | 1.000 | 1.000 | 0.815 |
| 31-40 | 0.757 | 0.500 | 0.750 | 0.893 |
| 41-50 | 0.894 | 0.833 | 1.000 | 0.938 |
| 51-60 | 0.781 | 0.714 | 1.000 | 0.903 |
| 61-70 | 0.992 | 1.000 | 1.000 | 0.979 |
| 71-80 | 0.881 | 1.000 | 0.750 | 0.903 |
| 81-90 | 0.992 | 1.000 | 1.000 | 0.972 |
| 91-100 | 0.875 | 0.833 | nan | 0.937 |

**Early (1-20) avg 0.643 vs late (81-100) avg 0.933.** 1-30 0.737 vs 71-100 0.916. Overall 0.838. By type: A 0.825, B 0.800, C 0.894.

## Folds

- after exam 10: The word right after the opener decides it: "So what/now/if", "But what/here's/the", "And then/so/that's", "Because if/the". Check the following word. [validated: +2.00 on 5 past type-B items]
- after exam 10: Humanizer step: map essay openers back to spoken ones. Therefore/As a result -> So, However -> But, Additionally/Moreover -> And, For example -> Like, Currently -> Now. [validated: +0.38 on 4 past type-C items]
- after exam 20: Real lines are dense with contractions (it's, that's, don't). Expanded forms ("it is", "do not") are the single most reliable subtle AI tell. Re-contract everything except deliberate emphasis. [validated: +2.00 on 4 past type-A items]
- after exam 20: Humanizer step: re-contract (it is -> it's, do not -> don't, I am -> I'm) everywhere. [validated: +0.45 on 6 past type-C items]
- after exam 30: Humanizer step: swap formal vocabulary back to plain words (utilize->use, obtain->get, significant->big, numerous->a lot of, individuals->people, approximately->about, purchase->buy). [validated: +0.62 on 10 past type-C items]
- after exam 40: Spoken openers (And/But/So) begin about 28% of weighted sentences (Gen about 49%, Adam about 15%). A passage with none is suspicious. [validated: +1.00 on 8 past type-A items]
- after exam 40: Humanizer step: break semicolon and ", and" merges back into separate sentences so short punches come back. [validated: +0.10 on 14 past type-C items]
- after exam 60: Real narration keeps fillers (just, actually, really, kind of, I mean). A passage with zero fillers over 60+ words is almost always the AI version. Keep about 1 per 2-3 sentences. [validated: +1.00 on 21 past type-A items]

## Per-exam record
| # | type | source | gold | answer | score | miss -> rule |
|---|---|---|---|---|---|---|
| 1 | C | gen `1.txt` | (gold passage in exa | (humanized) | 0.78 | openers |
| 2 | A | gen `4.txt` | B | B | 1.0 |  |
| 3 | B | after `02-greed.txt` | And | And | 1.0 |  |
| 4 | C | gen `2.txt` | (gold passage in exa | (humanized) | 0.936 |  |
| 5 | B | gen `3.txt` | So | But | 0.0 | bigram |
| 6 | B | gen `5.txt` | But | But | 1.0 |  |
| 7 | B | adam `02-bestselling-book.txt` | It | But | 0.0 | group |
| 8 | C | gen `3.txt` | (gold passage in exa | (humanized) | 0.831 | contract |
| 9 | C | gen `6.txt` | (gold passage in exa | (humanized) | 0.671 | contract |
| 10 | B | especially `02-ai-paradox.txt` | And | And | 1.0 |  | **FOLD:** bigram, openers, tried burst on type A: rejected (would lose 1.00 on 1 past items), tried hedge on type C: rejected (would lose 0.01 on 4 past items)
| 11 | B | adam `01-ai-disaster.txt` | And | And | 1.0 |  |
| 12 | A | adam `04-superintelligence.txt` | B | A | 0.0 | contr |
| 13 | B | adam `01-ai-disaster.txt` | I | Okay | 0.0 | no-rule-fixes |
| 14 | B | especially `06-data-centers.txt` | The | The | 1.0 |  |
| 15 | B | gen `9.txt` | So | And | 0.0 | no-rule-fixes |
| 16 | C | adam `01-ai-disaster.txt` | (gold passage in exa | (humanized) | 0.988 |  |
| 17 | C | after `10-water.txt` | (gold passage in exa | (humanized) | 0.65 | contract |
| 18 | A | after `07-trump-family.txt` | C | B | 0.0 | contr |
| 19 | A | gen `8.txt` | B | B | 1.0 |  |
| 20 | B | gen `6.txt` | So | So | 1.0 |  | **FOLD:** contr, contract, tried semi on type A: rejected (would lose 1.00 on 4 past items), tried hedge on type C: rejected (would lose 0.01 on 6 past items)
| 21 | B | adam `02-bestselling-book.txt` | The | The | 1.0 |  |
| 22 | C | adam `01-ai-disaster.txt` | (gold passage in exa | (humanized) | 0.747 | casual |
| 23 | B | gen `3.txt` | So | So | 1.0 |  |
| 24 | C | adam `01-ai-disaster.txt` | (gold passage in exa | (humanized) | 0.981 |  |
| 25 | B | adam `02-bestselling-book.txt` | I | I | 1.0 |  |
| 26 | B | adam `03-no-longer-in-control.txt` | And | And | 1.0 |  |
| 27 | C | adam `01-ai-disaster.txt` | (gold passage in exa | (humanized) | 0.756 | casual |
| 28 | C | gen `2.txt` | (gold passage in exa | (humanized) | 0.775 | casual |
| 29 | A | gen `1.txt` | B | B | 1.0 |  |
| 30 | A | especially `06-data-centers.txt` | B | B | 1.0 |  | **FOLD:** casual, tried hedge on type C: rejected (would lose 0.01 on 10 past items)
| 31 | A | gen `3.txt` | A | A | 1.0 |  |
| 32 | C | gen `8.txt` | (gold passage in exa | (humanized) | 0.802 | residual (lost fillers/wording cannot be recovered) |
| 33 | B | gen `3.txt` | But | But | 1.0 |  |
| 34 | C | gen `8.txt` | (gold passage in exa | (humanized) | 0.916 |  |
| 35 | B | gen `1.txt` | So | And | 0.0 | no-rule-fixes |
| 36 | C | adam `04-superintelligence.txt` | (gold passage in exa | (humanized) | 0.992 |  |
| 37 | B | after `12-data-centres-not-working.txt` | And | And | 1.0 |  |
| 38 | C | after `12-data-centres-not-working.txt` | (gold passage in exa | (humanized) | 0.86 |  |
| 39 | B | especially `06-data-centers.txt` | So | So | 1.0 |  |
| 40 | A | gen `9.txt` | C | B | 0.0 | opener | **FOLD:** opener, split, tried hedge on type C: rejected (would lose 0.01 on 14 past items)
| 41 | C | adam `04-superintelligence.txt` | (gold passage in exa | (humanized) | 0.938 |  |
| 42 | B | adam `03-no-longer-in-control.txt` | You | You | 1.0 |  |
| 43 | B | adam `04-superintelligence.txt` | So | So | 1.0 |  |
| 44 | A | adam `01-ai-disaster.txt` | A | A | 1.0 |  |
| 45 | B | especially `01-spacex.txt` | So | So | 1.0 |  |
| 46 | A | adam `05-sam-altman.txt` | C | C | 1.0 |  |
| 47 | A | oil `03-oil-apocalypse.txt` | C | C | 1.0 |  |
| 48 | A | adam `05-sam-altman.txt` | C | B | 0.0 | subtle-variant tie |
| 49 | A | after `06-diamonds.txt` | A | A | 1.0 |  |
| 50 | A | oil `03-oil-apocalypse.txt` | B | B | 1.0 |  | **FOLD:** no rule passed validation, tried burst on type A: rejected (would lose 1.00 on 14 past items), tried semi on type A: rejected (would lose 1.00 on 14 past items), tried group on type B: rejected (would lose 1.00 on 21 past items)
| 51 | A | adam `01-ai-disaster.txt` | C | A | 0.0 | fill |
| 52 | A | adam `03-no-longer-in-control.txt` | C | C | 1.0 |  |
| 53 | A | after `01-dark-side-data-centers.txt` | C | C | 1.0 |  |
| 54 | A | gen `2.txt` | C | C | 1.0 |  |
| 55 | A | after `09-microchip-war.txt` | C | C | 1.0 |  |
| 56 | A | adam `05-sam-altman.txt` | A | B | 0.0 | subtle-variant tie |
| 57 | C | adam `01-ai-disaster.txt` | (gold passage in exa | (humanized) | 0.809 | residual (lost fillers/wording cannot be recovered) |
| 58 | A | gen `6.txt` | A | A | 1.0 |  |
| 59 | B | especially `01-spacex.txt` | I | I | 1.0 |  |
| 60 | C | adam `04-superintelligence.txt` | (gold passage in exa | (humanized) | 0.997 |  | **FOLD:** fill, tried burst on type A: rejected (would lose 1.00 on 21 past items), tried semi on type A: rejected (would lose 2.00 on 21 past items), tried group on type B: rejected (would lose 1.00 on 22 past items)
| 61 | C | adam `01-ai-disaster.txt` | (gold passage in exa | (humanized) | 0.933 |  |
| 62 | B | adam `04-superintelligence.txt` | So | So | 1.0 |  |
| 63 | C | after `07-trump-family.txt` | (gold passage in exa | (humanized) | 0.989 |  |
| 64 | A | especially `01-spacex.txt` | A | A | 1.0 |  |
| 65 | A | adam `02-bestselling-book.txt` | B | B | 1.0 |  |
| 66 | C | adam `03-no-longer-in-control.txt` | (gold passage in exa | (humanized) | 1.0 |  |
| 67 | C | adam `01-ai-disaster.txt` | (gold passage in exa | (humanized) | 0.995 |  |
| 68 | A | especially `06-data-centers.txt` | C | C | 1.0 |  |
| 69 | A | adam `02-bestselling-book.txt` | C | C | 1.0 |  |
| 70 | A | gen `4.txt` | B | B | 1.0 |  | **FOLD:** no rule passed validation, tried semi on type A: rejected (would lose 3.00 on 26 past items), tried group on type B: rejected (would lose 2.00 on 23 past items), tried hedge on type C: rejected (would lose 0.01 on 21 past items)
| 71 | B | gen `1.txt` | Because | But | 0.0 | no-rule-fixes |
| 72 | A | gen `10.txt` | C | C | 1.0 |  |
| 73 | B | adam `02-bestselling-book.txt` | But | But | 1.0 |  |
| 74 | C | gen `8.txt` | (gold passage in exa | (humanized) | 1.0 |  |
| 75 | C | adam `02-bestselling-book.txt` | (gold passage in exa | (humanized) | 0.807 | residual (lost fillers/wording cannot be recovered) |
| 76 | B | adam `05-sam-altman.txt` | And | And | 1.0 |  |
| 77 | A | adam `03-no-longer-in-control.txt` | C | C | 1.0 |  |
| 78 | A | after `09-microchip-war.txt` | B | B | 1.0 |  |
| 79 | B | especially `06-data-centers.txt` | You | You | 1.0 |  |
| 80 | A | oil `03-oil-apocalypse.txt` | C | C | 1.0 |  | **FOLD:** no rule passed validation, tried semi on type A: rejected (would lose 3.00 on 30 past items), tried group on type B: rejected (would lose 2.00 on 27 past items), tried hedge on type C: rejected (would lose 0.02 on 23 past items)
| 81 | C | adam `03-no-longer-in-control.txt` | (gold passage in exa | (humanized) | 1.0 |  |
| 82 | A | adam `05-sam-altman.txt` | C | C | 1.0 |  |
| 83 | A | oil `03-oil-apocalypse.txt` | C | C | 1.0 |  |
| 84 | B | gen `8.txt` | So | So | 1.0 |  |
| 85 | A | after `12-data-centres-not-working.txt` | C | C | 1.0 |  |
| 86 | C | adam `03-no-longer-in-control.txt` | (gold passage in exa | (humanized) | 1.0 |  |
| 87 | B | adam `04-superintelligence.txt` | And | And | 1.0 |  |
| 88 | B | especially `01-spacex.txt` | But | But | 1.0 |  |
| 89 | C | adam `04-superintelligence.txt` | (gold passage in exa | (humanized) | 0.917 |  |
| 90 | A | adam `04-superintelligence.txt` | B | B | 1.0 |  | **FOLD:** no rule passed validation, tried semi on type A: rejected (would lose 3.00 on 34 past items), tried group on type B: rejected (would lose 2.00 on 30 past items), tried hedge on type C: rejected (would lose 0.03 on 26 past items)
| 91 | C | gen `5.txt` | (gold passage in exa | (humanized) | 0.76 | residual (lost fillers/wording cannot be recovered) |
| 92 | C | adam `03-no-longer-in-control.txt` | (gold passage in exa | (humanized) | 1.0 |  |
| 93 | A | gen `6.txt` | B | B | 1.0 |  |
| 94 | A | adam `05-sam-altman.txt` | C | B | 0.0 | subtle-variant tie |
| 95 | C | gen `1.txt` | (gold passage in exa | (humanized) | 1.0 |  |
| 96 | A | after `06-diamonds.txt` | C | C | 1.0 |  |
| 97 | C | gen `2.txt` | (gold passage in exa | (humanized) | 0.989 |  |
| 98 | A | gen `5.txt` | A | A | 1.0 |  |
| 99 | A | oil `03-oil-apocalypse.txt` | A | A | 1.0 |  |
| 100 | A | adam `02-bestselling-book.txt` | C | C | 1.0 |  | **FOLD:** no rule passed validation, tried semi on type A: rejected (would lose 3.00 on 40 past items), tried group on type B: rejected (would lose 2.00 on 30 past items), tried hedge on type C: rejected (would lose 0.03 on 30 past items)