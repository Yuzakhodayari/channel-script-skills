## Detector gate (hard publish bar)

The final script from `channel-language` must score **≤ 2** on the local Avoid-AI / AI-writing detector before it is handed back. Score is 0–100 from `detect.js`. Labels: 0 = Clean, 1–15 = Mild, 16–35 = Some AI patterns, 36–80 = Strong, 81+ = Heavy. The bar for this channel pipeline is **score ≤ 2** (effectively Clean / near-Clean). Class probabilities are not the bar; the integer `score` is.

### How to run (preferred path)

```bash
# From any cwd; paste the full narration (no stage directions, no YAML):
printf '%s' "$SCRIPT" | node /home/box/agent-data/workflows/ai-writing-detector/scripts/detect.js --context general

# Or a file:
node /home/box/agent-data/workflows/ai-writing-detector/scripts/detect.js --file /path/to/script.md --context general
```

Also load and apply (in order, do not skip):
1. `avoid-ai-writing` skill (canonical rulebook + `references/patterns.md`)
2. `anti-ai-slop-writing` self-check
3. `humanizer` patterns A–F when a tell survives the detector
4. `voice-preserving-rewriter` connection contract: preserve facts, numbers, URLs, quotes; never invent

If Node is unavailable, say so, run a model-only audit against avoid-ai-writing + anti-ai-slop, and mark `execution_evidence.detector: model_only`. Do not claim a numeric score you did not compute.

### Iterate-to-convergence

1. Run detector → record `score`, `label`, top issues.
2. If `score > 2`, rewrite only the spans the issues point at, citing language cards (L*) and avoid-ai tiers.
3. Re-run detector. Cap at **3** detector loops (initial + 2 repairs).
4. If still `score > 2` after 3 loops, return the best draft with `GATE: FAIL`, the last score, and the unresolved issues. Never soft-pass.
5. On `score ≤ 2`, return `GATE: PASS` with the score next to the script.

### What the gate is not

- Not a claim that a human wrote the script.
- Not permission to invent facts to "sound more human".
- Not a reason to add grammar errors on purpose (Gen lean allows ~1 slip per 500 words; other leans do not).
