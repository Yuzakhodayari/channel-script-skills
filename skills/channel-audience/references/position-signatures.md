# Method 2: Audience-device position signatures

| feature | 0-10% (open) | 10-80% (body) | 80-100% (close) | signature |
|---|---|---|---|---|
| you | 20.2% | 15.9% | 25.2% | CLOSE |
| question | 7.0% | 5.2% | 3.8% | flat |
| stakes | 11.9% | 6.8% | 7.8% | OPEN |
| hope | 4.1% | 5.5% | 7.9% | flat |
| future | 7.1% | 6.0% | 8.9% | flat |
| reflective | 1.3% | 1.5% | 4.8% | CLOSE |
| signoff | 0.7% | 1.1% | 4.3% | CLOSE |
| callback | 2.7% | 4.6% | 5.3% | flat |
| past | 39.8% | 41.4% | 34.1% | flat |
| number | 16.0% | 13.0% | 9.6% | flat |
| in_medias_res | 9.6% | 10.4% | 15.5% | flat |
| contrast | 14.0% | 15.9% | 16.7% | flat |
| starts_anaphor | 15.3% | 14.8% | 12.0% | flat |
| profanity | 2.5% | 1.7% | 0.6% | flat |
| we | 10.8% | 10.2% | 20.8% | CLOSE |

_Weighted share of host sentences where the cue fires (TRAIN+VAL videos only; weights Adam 7, Gen 4, Oil 5, Especially-AI/SpaceX 3, After 1)._

## Accepted rules
- **Close vs mid (A4):** HOPE and agency words point to the close. Past-tense narration, many named entities and anaphor starts ("It/This/They …") point to the middle. Val 0.88.
- **Hook vs mid (A2):** the learned open-vocabulary score plus dated and demonstrative starts. Val only reaches 0.58. One opening line taken alone is often indistinguishable from body text.
- **Mode (A3):** first-person rate, number density, in-scene narration, callbacks and "you" rate. Val 0.83.
