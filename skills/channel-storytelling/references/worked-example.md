# Worked pipeline example (demo seed)

**Title:** "Why Your City's Insurance Market Is Collapsing"

## Bad AI draft (input — deliberate slop)

In today's rapidly evolving landscape, it is crucial to delve into the multifaceted realm of homeowners insurance. Moreover, this pivotal issue serves as a testament to the challenges facing American communities across the nation. Furthermore, stakeholders must navigate these complexities in order to unlock resilient solutions that foster innovation, resilience, and growth.

In this video, we will cover three key aspects of the insurance crisis. First, we will explore the underlying factors. Second, we will examine the broader implications. Third, we will discuss potential pathways forward. It is important to note that this transformative moment requires careful consideration from all parties involved.

The insurance industry has found itself at a crossroads. Rising claims, regulatory pressures, and climate-related events have created a perfect storm. Companies are making difficult decisions about where they can continue to operate. Homeowners are left wondering what the future holds for their coverage and their financial security.

Additionally, experts suggest that a combination of policy reform, community engagement, and technological innovation could help address these challenges. By leveraging data-driven insights and fostering collaboration between the public and private sectors, we can begin to make meaningful progress.

At the end of the day, the path forward will require bold leadership and a willingness to embrace change. In conclusion, we must all come together to build a more resilient future for homeowners, insurers, and communities alike. Let me know your thoughts in the comments below, and don't forget to like and subscribe for more content.

## Stage 1 — structure (STRATEGY PACKET excerpt)

```yaml
strategy_id: STR-GEN-EXPLAINER
engine: explainer
lean: Gen
length_target_words: 4000
forbidden_engines: [clocked, street, ladder, speculative]
forbid_reasons:
  - "No dated single incident → clocked banned (R44)"
  - "No interview shoot → street banned (R46)"
  - "Stakes are wallet/cultural not first-principles → ladder banned (R45)"
  - "Settled/ongoing market, not near-future fiction → speculative banned (R48)"
thesis_question: "Why are insurers fleeing your zip code — and what can you actually do about it?"
success_test: "Viewer can name the mechanism (risk pooling break), one villain incentive, and one lever (shop, mitigate, vote)."
sponsor_window: [0.28, 0.34]
```

## Stage 2 — storytelling (spine)

Cold open: viewer gets a non-renewal letter → why care (zip-code map) → point 1 capital flight → point 2 climate + reinsurance → twist (it's also rate caps) → agency (mitigation, shopping, local ballot) → bookend the letter.

## Stage 3 — audience

A01 viewer-in-example on the letter; A03 name the assumption ("you thought it was just hurricanes"); A16 open loop on the third cause; A32 don't-panic calibration; A23 specific comment question; A37 ballot lever.

## Stage 4 — language + gate

Ban-list wipe (landscape/crucial/testament/furthermore/in conclusion). And/So/But starters. Short punches. Then:

```bash
node /home/box/agent-data/workflows/ai-writing-detector/scripts/detect.js --file final.md --context general
```

Target: `score ≤ 2`, `GATE: PASS`.
