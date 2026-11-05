# Channel script pipeline — handoff contract

Four skills form one pipeline. A bad AI draft (or a title + notes) goes in; a full narration that scores ≤ 2 on the local AI-writing detector comes out. Skills do not re-decide work owned upstream.

## Order (fixed)

```
title + topic + (optional bad draft)
        │
        ▼
[1] channel-structure   → STRATEGY PACKET
        │
        ▼
[2] channel-storytelling → STORY DRAFT
        │
        ▼
[3] channel-audience     → AUDIENCE-ENGINEERED DRAFT
        │
        ▼
[4] channel-language     → FINAL SCRIPT + DETECTOR GATE (score ≤ 2)
```

Run them in this order on a full rewrite. For a grade-only request, each skill may run alone in `audit-only` mode.

## Handoff envelope (YAML, carry forward)

```yaml
pipeline: channel-script-v6
intent: full_rewrite | grade | plan | drill
title: "..."
topic_one_liner: "..."
source_kind: bad_ai_draft | outline | notes | blank
source_ref: optional path
lean: Gen | AIC | Fisher | Maxinomics | AotP | supporting:<name>
length_target_words: 3500-4500   # default Gen
protected_constraints: [facts, numbers, urls, quotes, names, dates]
pass: { index: 0, max: 3 }       # detector-loop budget lives in language
structure:
  status: pending | done
  strategy_id: null              # e.g. STR-GEN-EXPLAINER
  engine: null                   # clocked | speculative | artifact | explainer | essay | ladder | field | street
  beat_map: []                   # [{frac, beat, card}]
  forbidden_engines: []          # engines ruled out for THIS title
  sponsor_window: null
story:
  status: pending | done
  pov: null
  open_loops: []
  plants: []
audience:
  status: pending | done
  device_density_per_1k: null
  cta: null
language:
  status: pending | done
  detector: { executed: false, score: null, label: null, loops: 0 }
  gate: pending | PASS | FAIL
```

## Ownership (do not cross)

| skill | owns | must not |
|---|---|---|
| structure | strategy_id, engine, forbidden_engines, beat_map, sponsor_window, act breaks | rewrite prose, add jokes, pick CTA copy |
| storytelling | POV, scenes, reveals, plants/payoffs, ending image | change the beat_map windows, add subscribe asks |
| audience | viewer address, trust, retention devices, comment prompt, CTA | change engine, rewrite every sentence for voice |
| language | word-level voice, bans, detector gate | invent facts, change structure or engine |

When two skills flag the same span, keep the higher-priority card and drop the other. Any P0 on any axis means the draft is not ready.

## Typed edges

- `ROUTE` — user request picks the pipeline (or a single skill in audit-only).
- `FEED` — upstream packet is evidence for the next skill, not a command to ignore its own cards.
- `VERIFY` — language runs the detector gate; on FAIL within budget, `REPAIR` stays inside language.
- `BACKTRACK` — only if language or audience finds the *engine* itself is wrong for the title (rare). Return to structure with a one-line objection; do not silently swap engines mid-prose.

## Success criteria (pipeline)

1. Strategy fits THIS title (structure lists forbidden engines and why).
2. Story uses the chosen engine end to end.
3. Audience devices land at corpus density for the lean.
4. Final narration reads like the weighted blend (Gen default; AIC/Fisher craft bar).
5. Local detector `score ≤ 2` with `execution_evidence.detector: executed` (or honest `model_only` if Node is down).
