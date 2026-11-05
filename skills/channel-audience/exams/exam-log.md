# Exam log — channel-audience

## Honest note on who took these
The exams were taken by a **codified solver** (`build/exam_audience.py`, class `Solver`) that executes this skill's checklist rules as written at v1, not by a free-form model reading. After every 10 exams its misses were folded back: cue lists, position priors, mode templates, feature weights. The same lessons were written into `SKILL.md` ("Lessons from the exams") and `training/lessons-learned.md`. Gold answers come from the real transcripts and detector beat maps, so the remaining error is partly the solver's and partly detector noise.

## Curve

Block averages (10 exams each): [0.6, 0.8, 0.6, 0.7, 0.6, 0.5, 0.8, 0.7, 0.6, 0.8]

- Early (exams 1-50): **0.66**
- Late (exams 51-100): **0.68**
- First 20: 0.7 · Last 20: 0.7
- Overall: 0.67

## By type

| type | n | mean | first half | second half |
|---|---|---|---|---|
| A1 | 20 | 1.0 | 1.0 | 1.0 |
| A2 | 20 | 0.35 | 0.3 | 0.4 |
| A3 | 20 | 0.55 | 0.5 | 0.6 |
| A4 | 20 | 0.55 | 0.5 | 0.6 |
| A5 | 20 | 0.9 | 1.0 | 0.8 |

## Fold-backs (every 10 exams)

### After exam 10 — block average 0.6
- Exam 2 (A2): wrong pick; reweighted features → {"you": 0.3, "q": 0.3, "num": -0.3, "fear": 0.3, "hope": 0.0, "i": 0.0, "so": -0.8, "sl": -0.09, "prof": 0.0}.
- Exam 3: passage was Gen, answered Adam; moved Gen centroid → {'you': 2.55, 'i': 1.6, 'sl': 38.6, 'q': 0.64, 'prof': 0.16}.
- Exam 7 (A2): wrong pick; reweighted features → {"you": 0.3, "q": 0.3, "num": -0.73, "fear": 0.3, "hope": 0.0, "i": 0.6, "so": -0.83, "sl": -0.06, "prof": 0.0}.
- Exam 9 (A4): wrong pick; reweighted features → {"you": -0.34, "q": 0.0, "num": 0.0, "fear": -0.3, "hope": -0.3, "i": 0.2, "so": -0.34, "sl": 0.17, "prof": 0.0}.

### After exam 20 — block average 0.8
- Exam 17 (A2): wrong pick; reweighted features → {"you": 0.3, "q": 0.3, "num": -0.73, "fear": 0.3, "hope": 0.0, "i": 0.6, "so": -0.83, "sl": -0.06, "prof": 0.0}.
- Exam 19 (A4): wrong pick; reweighted features → {"you": -0.31, "q": 0.0, "num": 0.0, "fear": 0.3, "hope": -0.9, "i": 0.8, "so": 0.26, "sl": 0.14, "prof": 0.0}.

### After exam 30 — block average 0.6
- Exam 22 (A2): wrong pick; reweighted features → {"you": 0.3, "q": 0.3, "num": -0.13, "fear": 0.3, "hope": 0.0, "i": 0.6, "so": -0.83, "sl": 0.03, "prof": 0.0}.
- Exam 23: passage was Gen, answered Mechanism; moved Gen centroid → {'you': 3.41, 'i': 1.43, 'sl': 35.25, 'q': 0.51, 'prof': 0.13}.
- Exam 24 (A4): wrong pick; reweighted features → {"you": -0.31, "q": -0.6, "num": 0.6, "fear": 0.3, "hope": -0.9, "i": 0.8, "so": -0.03, "sl": 0.25, "prof": 0.0}.
- Exam 28: passage was Adam, answered Others; moved Adam centroid → {'you': 0.81, 'i': 1.47, 'sl': 14.25, 'q': 0.4, 'prof': 0.12}.

### After exam 40 — block average 0.7
- Exam 32 (A2): wrong pick; reweighted features → {"you": -0.3, "q": 0.3, "num": 0.47, "fear": 0.3, "hope": 0.0, "i": 0.0, "so": -0.83, "sl": 0.12, "prof": 0.0}.
- Exam 37 (A2): wrong pick; reweighted features → {"you": -0.3, "q": 0.3, "num": 0.47, "fear": 0.3, "hope": 0.6, "i": -0.6, "so": -0.83, "sl": 0.04, "prof": 0.0}.
- Exam 38: passage was Gen, answered Adam; moved Gen centroid → {'you': 2.73, 'i': 1.14, 'sl': 32.53, 'q': 0.41, 'prof': 0.1}.

### After exam 50 — block average 0.6
- Exam 42 (A2): wrong pick; reweighted features → {"you": -0.3, "q": 0.3, "num": 0.47, "fear": 0.3, "hope": 0.6, "i": -0.6, "so": -0.23, "sl": -0.12, "prof": 0.0}.
- Exam 44 (A4): wrong pick; reweighted features → {"you": -0.31, "q": -0.6, "num": 0.0, "fear": 0.9, "hope": -0.3, "i": 0.8, "so": -0.03, "sl": 0.46, "prof": 0.0}.
- Exam 48: passage was Mechanism, answered Adam; moved Mechanism centroid → {'you': 1.62, 'i': 1.3, 'sl': 16.76, 'q': 0.38, 'prof': 0.06}.
- Exam 49 (A4): wrong pick; reweighted features → {"you": 0.07, "q": -0.6, "num": -0.6, "fear": 0.9, "hope": 0.3, "i": 0.2, "so": -0.06, "sl": 0.61, "prof": 0.0}.

### After exam 60 — block average 0.5
- Exam 52 (A2): wrong pick; reweighted features → {"you": 0.3, "q": 0.3, "num": -0.13, "fear": 0.3, "hope": 0.6, "i": -0.6, "so": -0.83, "sl": -0.18, "prof": 0.0}.
- Exam 55 (A5): wrong pick; reweighted features → {"you": 0.5, "q": 0.5, "so": 0.3, "num": 0.2, "fear": 0.1, "hope": 0.1, "i": 0.1, "sl": 0.0, "prof": 0.1}.
- Exam 57 (A2): wrong pick; reweighted features → {"you": 0.9, "q": 0.3, "num": -0.73, "fear": 0.3, "hope": 0.6, "i": -0.6, "so": -0.83, "sl": -0.01, "prof": 0.0}.
- Exam 59 (A4): wrong pick; reweighted features → {"you": -0.53, "q": -0.6, "num": -0.6, "fear": 0.9, "hope": -0.3, "i": 0.2, "so": 0.15, "sl": 0.4, "prof": 0.0}.
- Exam 60 (A5): wrong pick; reweighted features → {"you": 0.49, "q": 0.5, "so": 0.3, "num": 0.2, "fear": 0.1, "hope": 0.09, "i": 0.1, "sl": 0.01, "prof": 0.1}.

### After exam 70 — block average 0.8
- Exam 64 (A4): wrong pick; reweighted features → {"you": -0.05, "q": -0.6, "num": -0.6, "fear": 0.3, "hope": 0.15, "i": 0.04, "so": 0.75, "sl": 0.17, "prof": 0.0}.
- Exam 69 (A4): wrong pick; reweighted features → {"you": -0.05, "q": -0.6, "num": -0.08, "fear": 0.3, "hope": 0.15, "i": 0.04, "so": 0.75, "sl": 0.07, "prof": 0.0}.

### After exam 80 — block average 0.7
- Exam 72 (A2): wrong pick; reweighted features → {"you": 0.3, "q": 0.3, "num": -0.73, "fear": 0.3, "hope": 0.6, "i": -0.6, "so": -0.83, "sl": -0.03, "prof": 0.0}.
- Exam 73: passage was Adam, answered Others; moved Adam centroid → {'you': 0.67, 'i': 0.93, 'sl': 14.84, 'q': 0.11, 'prof': 0.03}.
- Exam 77 (A2): wrong pick; reweighted features → {"you": -0.3, "q": 0.3, "num": -0.13, "fear": 0.3, "hope": 0.0, "i": -0.6, "so": -0.83, "sl": -0.06, "prof": 0.0}.

### After exam 90 — block average 0.6
- Exam 82 (A2): wrong pick; reweighted features → {"you": -0.3, "q": -0.3, "num": -0.13, "fear": 0.3, "hope": 0.0, "i": -0.6, "so": -0.83, "sl": 0.1, "prof": 0.0}.
- Exam 83: passage was Mechanism, answered Adam; moved Mechanism centroid → {'you': 2.5, 'i': 0.95, 'sl': 14.75, 'q': 0.51, 'prof': 0.04}.
- Exam 84 (A4): wrong pick; reweighted features → {"you": -0.65, "q": -0.6, "num": -0.08, "fear": 0.3, "hope": -0.45, "i": -0.56, "so": 0.75, "sl": 0.1, "prof": 0.0}.
- Exam 88: passage was Gen, answered Adam; moved Gen centroid → {'you': 2.33, 'i': 0.91, 'sl': 28.98, 'q': 0.63, 'prof': 0.08}.

### After exam 100 — block average 0.8
- Exam 97 (A2): wrong pick; reweighted features → {"you": 0.3, "q": 0.3, "num": -0.13, "fear": 0.3, "hope": 0.0, "i": -0.6, "so": -0.83, "sl": 0.26, "prof": 0.0}.
- Exam 98: passage was Gen, answered Adam; moved Gen centroid → {'you': 1.9, 'i': 0.99, 'sl': 25.45, 'q': 0.55, 'prof': 0.15}.
