# Exam rubric

Each exam is scored 0-1:

| type | scoring |
|---|---|
| MCQ types (T1, T3, T5, A1-A5) | 1 = exact gold, 0 = otherwise |
| T2 position | 1 = within ±10 points, 0.5 = within ±20, else 0 |
| T4 outline | 4 sub-points (hook ±3%, sponsor ±10% or both none, conclusion ±8%, turns ±2), each 0.25 |
| T6 ordering | pairwise order accuracy |

**Gold sources.** Real host-only transcript text, the detector beat maps (`references/beat-maps.md`), and real % positions.

**Sampling.** Each exam's video is drawn with probability ∝ its weight (Adam 7, Gen 4, Oil 5, Esp 3, After 1). Types rotate. The seed is fixed, so runs reproduce.

**Fold rule.** After each block of 10, every miss becomes a lesson (a rule, cue, prior, or template update). It is applied to the solver and recorded in `exam-log.md` and SKILL.md.
