# Language exams (classic fold-in harness)

Source: `/workspace/channel-build/exams.py` via `gen.run_exams(kind='lang')`, seed 11.
Types A (real-vs-AI), B (opener cloze), C (humanize). Fold-in every 10 exams.
Training passages excluded from exam pool (same as historical).

| window | score |
|---|---|
| early 1-20 | 0.643 |
| late 81-100 | 0.933 |
| overall | 0.838 |
| type A | 0.825 |
| type B | 0.800 |
| type C | 0.894 |
