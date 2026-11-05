# Exam log — channel-structure

## Honest note on who took these
The exams were taken by a **codified solver** (`build/exam_structure.py`, class `Solver`) that executes this skill's checklist rules as written at v1, not by a free-form model reading. After every 10 exams its misses were folded back: cue lists, position priors, mode templates, feature weights. The same lessons were written into `SKILL.md` ("Lessons from the exams") and `training/lessons-learned.md`. Gold answers come from the real transcripts and detector beat maps, so the remaining error is partly the solver's and partly detector noise.

## Curve

Block averages (10 exams each): [0.7, 0.81, 0.82, 0.64, 0.63, 0.54, 0.59, 0.78, 0.68, 0.72]

- Early (exams 1-50): **0.722**
- Late (exams 51-100): **0.663**
- First 20: 0.754 · Last 20: 0.7
- Overall: 0.693

## By type

| type | n | mean | first half | second half |
|---|---|---|---|---|
| T1 | 17 | 0.76 | 0.62 | 0.89 |
| T2 | 17 | 0.59 | 0.5 | 0.67 |
| T3 | 17 | 0.53 | 0.75 | 0.33 |
| T4 | 17 | 0.84 | 0.84 | 0.83 |
| T5 | 16 | 0.81 | 0.88 | 0.75 |
| T6 | 16 | 0.63 | 0.67 | 0.58 |

## Fold-backs (every 10 exams)

### After exam 10 — block average 0.7
- Exam 1: section turns also open with "We" — added opener cue.
- Exam 2: promise lines often are "to understand…", "what no one is talking about", "the full story" — added.
- Exam 2: position miss (45% vs gold 7.3%) — shifted the PROMISE / ROADMAP prior toward gold.
- Exam 4: outline for Gen off (score 0.75); template moved toward gold → {'hook': 6.1, 'spon': 40.8, 'conc': 81.8, 'turns': 6}.
- Exam 10: outline for Gen off (score 0.75); template moved toward gold → {'hook': 10.3, 'spon': 41.0, 'conc': 81.8, 'turns': 6}.

### After exam 20 — block average 0.81
- Exam 14: CTA lines include "thanks/see you/comment" sign-offs, not just "subscribe".
- Exam 14: position miss (45% vs gold 99.6%) — shifted the CTA prior toward gold.
- Exam 16: outline for Adam off (score 0.75); template moved toward gold → {'hook': 3.1, 'spon': None, 'conc': 83.5, 'turns': 7}.

### After exam 30 — block average 0.82
- Exam 21: picked a mid-video line as the opener; reweighted opener features (now {"num": 0.5, "date": 1.0, "you": 0.5, "short": 1.0, "anaphora": -1.0, "so_open": -0.5, "question": 0.3, "name": 0.5, "meta": -1.0}).
- Exam 22: outline for Mechanism off (score 0.75); template moved toward gold → {'hook': 6.0, 'spon': 18.0, 'conc': 90, 'turns': 7}.

### After exam 40 — block average 0.64
- Exam 31: section turns also open with "Because" — added opener cue.
- Exam 35: profile was Mechanism, answered Adam; moved Mechanism centroid → {'dur': 31.4, 'wpm': 185.2, 'hook': 95.0, 'you': 16.6}.
- Exam 38: conclusions open with "But here's the thing" / "I think…" / "So where does this leave" — added.
- Exam 38: position miss (45% vs gold 88.7%) — shifted the CONCLUSION prior toward gold.
- Exam 40: outline for Adam off (score 0.75); template moved toward gold → {'hook': 4.4, 'spon': None, 'conc': 83.5, 'turns': 7}.

### After exam 50 — block average 0.63
- Exam 43: section turns also open with "So" — added opener cue.
- Exam 44: promise lines often are "to understand…", "what no one is talking about", "the full story" — added.
- Exam 44: position miss (45% vs gold 6.1%) — shifted the PROMISE / ROADMAP prior toward gold.
- Exam 45: picked a mid-video line as the opener; reweighted opener features (now {"num": 0.0, "date": 1.0, "you": 0.5, "short": 1.0, "anaphora": -0.5, "so_open": -0.5, "question": 0.3, "name": 0.0, "meta": -1.0}).

### After exam 60 — block average 0.54
- Exam 51: picked a mid-video line as the opener; reweighted opener features (now {"num": 0.5, "date": 1.5, "you": 0.5, "short": 0.5, "anaphora": -0.5, "so_open": -0.5, "question": -0.2, "name": 0.5, "meta": -1.0}).
- Exam 56: promise lines often are "to understand…", "what no one is talking about", "the full story" — added.
- Exam 56: position miss (45% vs gold 6.1%) — shifted the PROMISE / ROADMAP prior toward gold.
- Exam 58: outline for Gen off (score 0.75); template moved toward gold → {'hook': 9.7, 'spon': 38.8, 'conc': 88.2, 'turns': 6}.
- Exam 59: profile was Mechanism, answered Others; moved Mechanism centroid → {'dur': 26.4, 'wpm': 180.4, 'hook': 85.8, 'you': 19.7}.

### After exam 70 — block average 0.59
- Exam 61: section turns also open with "But" — added opener cue.
- Exam 63: picked a mid-video line as the opener; reweighted opener features (now {"num": 0.5, "date": 1.5, "you": 0.5, "short": 0.0, "anaphora": -0.5, "so_open": -0.5, "question": 0.3, "name": 0.0, "meta": -1.0}).
- Exam 64: outline for Gen off (score 0.5); template moved toward gold → {'hook': 8.3, 'spon': 40.7, 'conc': 83.7, 'turns': 6}.
- Exam 68: promise lines often are "to understand…", "what no one is talking about", "the full story" — added.
- Exam 68: position miss (45% vs gold 6.1%) — shifted the PROMISE / ROADMAP prior toward gold.
- Exam 70: outline for Gen off (score 0.75); template moved toward gold → {'hook': 8.9, 'spon': 40.0, 'conc': 78.4, 'turns': 6}.

### After exam 80 — block average 0.78
- Exam 75: picked a mid-video line as the opener; reweighted opener features (now {"num": 0.0, "date": 1.0, "you": 0.5, "short": 0.0, "anaphora": 0.0, "so_open": -0.5, "question": 0.3, "name": 0.0, "meta": -1.0}).
- Exam 80: conclusions open with "But here's the thing" / "I think…" / "So where does this leave" — added.
- Exam 80: position miss (86.1% vs gold 70.5%) — shifted the CONCLUSION prior toward gold.

### After exam 90 — block average 0.68
- Exam 81: picked a mid-video line as the opener; reweighted opener features (now {"num": -0.5, "date": 0.5, "you": 0.5, "short": 0.0, "anaphora": -0.5, "so_open": -0.5, "question": 0.3, "name": -0.5, "meta": -1.0}).
- Exam 83: profile was Mechanism, answered Gen; moved Mechanism centroid → {'dur': 28.4, 'wpm': 187.3, 'hook': 95.8, 'you': 18.3}.
- Exam 87: picked a mid-video line as the opener; reweighted opener features (now {"num": -1.0, "date": 0.0, "you": 0.5, "short": 0.0, "anaphora": 0.0, "so_open": -0.5, "question": 0.3, "name": -0.5, "meta": -1.0}).

### After exam 100 — block average 0.72
- Exam 92: sponsor blocks start on the bridge ("that's where … comes in") — added bridge cues.
- Exam 92: position miss (34.5% vs gold 20.3%) — shifted the SPONSOR READ prior toward gold.
- Exam 93: picked a mid-video line as the opener; reweighted opener features (now {"num": -1.0, "date": 0.0, "you": 0.5, "short": 0.5, "anaphora": 0.0, "so_open": -0.5, "question": 0.3, "name": -0.5, "meta": -1.0}).
- Exam 94: outline for Gen off (score 0.5); template moved toward gold → {'hook': 6.5, 'spon': 37.8, 'conc': 78.4, 'turns': 7}.
