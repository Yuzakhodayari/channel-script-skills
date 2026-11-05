# Strategy selector — pick the engine for THIS title

Load this file at the start of every `channel-structure` run. The job is to choose one strategy and explicitly ban the others for this title. A beautiful AIC clocked timeline on a "what is a bond" title is a failure. A Gen outrage essay on a dated 72-hour crisis is a failure.

## Step 0 — Read the title cold

Write one line each:
- **Claim the title makes** (what the clicker thinks they will get)
- **Evidence type available** (timeline, document, mechanism, field access, interviews, concept only)
- **Stakes** (civic, wallet, wonder, fear, cultural)
- **Clock?** (is there a real dated event with hours/days?)

If evidence type is missing, stop and ask, or mark `[NEEDS SOURCE]` — do not invent a timeline or a document.

## Step 1 — Match title signals → strategy

| If the title/topic looks like… | strategy_id | engine | default lean | length |
|---|---|---|---|---|
| Dated true event, firing, incident, "what happened inside X" | `STR-AIC-CLOCKED` | clocked true story | AIC | 5.5–7k |
| "What if", near-future, AI takeover, agent gone wrong | `STR-AIC-SPECULATIVE` | speculative scenario | AIC | 5–6.5k |
| "I found this document/map", sanctions, how does X state do Y | `STR-FISHER-ARTIFACT` | artifact investigation | Fisher | 5–6k |
| "Why X is happening to you", money/power, cartel, scam, PE | `STR-GEN-EXPLAINER` | explainer w/ villain+agency | Gen | 3.5–4.5k |
| Ride-along, border, range, "I spent a day with" | `STR-GEN-FIELD` | field / ride-along | Gen | 3.5–5k |
| Street answers to one question ("what is the American dream") | `STR-GEN-STREET` | street interview | Gen | 2.5–4k |
| Object-as-metaphor, "the elevator operator problem", games | `STR-MAX-ESSAY` | concept essay | Maxinomics | 3–4k |
| Paradox, "how does money even work", first principles | `STR-AOTP-LADDER` | toy-model ladder | AotP | 2–3.5k |
| Bubble/valuation explainer with history chapters | `STR-BOYLE-CHAPTERED` | chaptered essay | Boyle/HMW | 4–6k |
| Primer then failure ("how X is supposed to work… and why it isn't") | `STR-HMW-PRIMER` | primer + break | HMW | 4–5k |

Default when unclear and the channel is the user's: `STR-GEN-EXPLAINER`.

## Step 2 — Hard bans (when NOT to use)

Apply every row that matches. Put the banned engines in `forbidden_engines`.

| Signal | NEVER use | why |
|---|---|---|
| No real dated event, no hour-level facts | `clocked` | Fake timestamps are a trust kill (R39) and an AI tell |
| Title is a mechanism ("how does X work") with no villain | `explainer` outrage arc | Outrage without a target feels fake; use `ladder` or `essay` |
| Title promises a document / leak / map | anything except `artifact` (or clocked if the doc is inside a crisis) | Fisher viewers came for the artifact |
| Title is a personal field claim ("I went to…") | `ladder`, `essay`, pure `clocked` | You need scenes and people (field) |
| Title is a single survey question to strangers | anything except `street` | Interviews are the engine |
| Title is a paradox or "why does this even exist" | `street`, `field` | Need toy model + rungs |
| Title is near-future / speculative risk | `street`, pure `explainer` without scenario | AIC speculative exists for this |
| Title is cultural-food / "Americans and X" | `ladder`, `clocked` | Gen explainer or essay |
| Lean is AIC and topic is soft lifestyle | Gen slang engine | Wrong register (L13 bans) |
| Lean is Fisher and topic has no adversary logic | Gen bootlicker-preempt style | Fisher is fair-to-adversary |
| Only concept-level sources (no numbers, no names) | `clocked`, `artifact` | You will fabricate; pick `ladder`/`essay` and mark gaps |

## Step 3 — Emit the STRATEGY PACKET

```yaml
strategy_id: STR-GEN-EXPLAINER
engine: explainer
lean: Gen
length_target_words: 4000
forbidden_engines: [clocked, street, ladder]
forbid_reasons:
  - "No dated incident → clocked banned"
  - "No interview plan → street banned"
  - "Stakes are wallet/cultural not first-principles → ladder banned"
beat_map:   # from references/beat-maps.md for this strategy
  - {frac: 0.00, beat: "relatable cold open", card: "R01/T01"}
  - {frac: 0.08, beat: "why should you care + thesis", card: "R02/A03"}
  - {frac: 0.15, beat: "point 1", card: "R12"}
  - {frac: 0.30, beat: "bridged sponsor", card: "R08/R09/R11"}
  - {frac: 0.40, beat: "point 2", card: "R12"}
  - {frac: 0.60, beat: "point 3 + twist", card: "R13/T31"}
  - {frac: 0.80, beat: "agency / lever", card: "R26/A37"}
  - {frac: 0.95, beat: "CTA", card: "A38"}
sponsor_window: [0.25, 0.35]
thesis_question: "..."
success_test: "Viewer can say the villain, the mechanism, and one thing they can do."
```

Hand this packet to `channel-storytelling` unchanged. Storytelling may add POV and plants; it may not change `strategy_id` or `forbidden_engines` without a BACKTRACK.

## Step 4 — Sanity checks before leaving structure

- [ ] Exactly one `strategy_id`
- [ ] `forbidden_engines` has ≥ 1 entry (if it is empty you have not thought)
- [ ] Beat map windows match the lean's measured positions (R08, R01)
- [ ] Title claim is restated in the first 10% and last 10% plan
- [ ] No beat requires evidence you do not have
