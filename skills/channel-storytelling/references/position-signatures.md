# Method 2: Reverse outline and position-signature table

Every TRAIN and VAL video was reverse-outlined sentence by sentence and bucketed by runtime position. Use this table to place a passage. If OPEN cues fire, it belongs in the first 10%. If CLOSE cues fire, it belongs in the last 20%. Otherwise it is body.

| feature | 0-10% (open) | 10-80% (body) | 80-100% (close) | signature |
|---|---|---|---|---|
| in_medias_res | 9.6% | 10.4% | 15.5% | flat |
| year_date | 4.8% | 5.0% | 2.6% | flat |
| number | 16.0% | 13.0% | 9.6% | flat |
| dated_start | 1.6% | 0.8% | 0.3% | OPEN |
| viewer_frame | 0.5% | 0.1% | 0.4% | OPEN |
| greeting | 1.3% | 0.2% | 0.2% | OPEN |
| hedge_project | 7.9% | 6.8% | 11.4% | CLOSE |
| mechanism | 9.6% | 10.7% | 12.5% | flat |
| callback | 2.7% | 4.6% | 5.3% | flat |
| reflective | 1.3% | 1.5% | 4.8% | CLOSE |
| conclusion | 0.0% | 0.4% | 0.7% | CLOSE |
| hope | 4.1% | 5.5% | 7.9% | flat |
| signoff | 0.7% | 1.1% | 4.3% | CLOSE |
| future | 7.1% | 6.0% | 8.9% | flat |
| past | 39.8% | 41.4% | 34.1% | flat |
| question | 7.0% | 5.2% | 3.8% | flat |
| you | 20.2% | 15.9% | 25.2% | CLOSE |
| we | 10.8% | 10.2% | 20.8% | CLOSE |
| stakes | 11.9% | 6.8% | 7.8% | OPEN |
| promise | 3.3% | 1.2% | 0.4% | OPEN |

_Weighted share of host sentences where the cue fires (TRAIN+VAL videos only; weights Adam 7, Gen 4, Oil 5, Especially-AI/SpaceX 3, After 1)._

## Placement rule (accepted on validation)
The validation-selected features were `lex_close` (a learned close-vocabulary score), `in_medias_res`, `past` and `year_date`. In plain words:
1. Past-tense, dated, in-scene narration means **open** or **middle**, not close.
2. Reflective, future, hope and callback wording means **close**.
3. When nothing fires, answer **middle**. It is the base rate.
