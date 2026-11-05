---
name: channel-structure
description: Plan, outline, time, or critique the STRUCTURE and STRATEGY of a YouTube script for the user's channel, a weighted blend of AI In Context (7x), Max Fisher (6x), Gen (5x, the user's own channel), Maxinomics (4.5x) and Art of the Problem (4x). Use when the user asks for an outline, beat sheet, act structure, video length, hook length, where the thesis, promise or roadmap goes, sponsor placement, chapters, pacing, section turns, conclusion timing, title-script alignment, explainer vs narrative mode, or why a draft drags in the middle or ends weird. Stage in the channel-script pipeline (structure → storytelling → audience → language). Pair with channel-storytelling, channel-audience, channel-language.
---

# channel-structure (v6 pipeline — all 117 scripts, 50 named patterns)

References: `references/patterns.md` (50 cards), `references/drills.md`, `references/pipeline.md`, `references/strategy-selector.md`, `references/detector-gate.md`, plus v4 reference files retained.

## Pipeline position

This is **stage 1/4** of the channel-script pipeline (see `references/pipeline.md`).

1. channel-structure — diagnose title → STRATEGY PACKET (forbidden engines named)
2. channel-storytelling — rewrite story with the chosen engine
3. channel-audience — inject audience devices at corpus density
4. channel-language — humanize word-level; **detector gate score ≤ 2**

On `full_rewrite`, do not skip stages. On `audit-only`, grade this axis alone.
Success for the pipeline: a full narration that fits THIS title's strategy, sounds like the weighted blend, and passes the local AI-writing detector at **score ≤ 2**.

## When to use

Use for the **structure** axis: title→strategy selection, forbidden engines, opening, sponsor, middle, close, beat maps, defects.

Trigger examples: outline / beat map / which story type / strategy for this title.

Do **not** use for thumbnails, title-only SEO, or analytics (those are pro-yt skills).

## Workflow

1. **Intake.** Read the envelope (title, topic, source, lean, protected constraints). Load `references/pipeline.md`.
2. **Stage work.** Run strategy-selector.md; emit STRATEGY PACKET with forbidden_engines.
3. **Card pass.** Walk the pattern index in priority order (P0 → P1 → P2). Honour **Do NOT apply when**.
4. **Grade or rewrite** using the rubric and output format below. Cite every card ID.
5. **Handoff.** Fill your section of the envelope. FEED to storytelling.
6. **Self-check.** No over-applied cards, no invented facts, score unsoftened.

## Input / output contract

### Incoming
- `title` (required), `topic_one_liner`, optional bad AI draft or notes
- `lean` if the user named one; otherwise diagnose and propose
- Never accept a pre-chosen engine from a later skill without a BACKTRACK note

### Produce
- Full **STRATEGY PACKET** (see `references/strategy-selector.md`): `strategy_id`, `engine`, `forbidden_engines` + reasons, `beat_map`, `sponsor_window`, `thesis_question`, `success_test`, `length_target_words`
- Structure-axis grade if mode is `grade`

### Outgoing
- `FEED` the STRATEGY PACKET to `channel-storytelling`
- Stop if evidence type is missing and the chosen engine needs it — ask or mark `[NEEDS SOURCE]`

## Creator leans (pick one before editing)

| lean | weight | use when | this axis in one line |
|---|---|---|---|
| Gen (default) | 5 | the user's own money/power explainers, field pieces | loose, funny, outrage → agency, "you" constantly |
| AIC | 7 | true story with a clock, or AI-risk scenario | dated scenes, restraint, dry asides, civic ask |
| Fisher | 6 | geopolitics / systems with documents, maps, a board | artifact first, numbered blocks, fair to adversaries |
| Maxinomics | 4.5 | concept essays around an object or game | cinematic vignette, fragments, viewer games |
| AotP | 4 | first-principles mechanism | toy model, ladder, wonder, little direct address |
| supporting | 1–3 | only when the user names them | use only their tagged cards |

When the user names no lean, use Gen and borrow craft from AIC and Fisher.

## Hard rules and numeric targets

References: `references/beat-positions-train.md` (measured cue positions), `references/beat-maps.md` (per-mode templates), `references/opener-close-library.md`.

## 1. Length by mode (median words, corpus)
AIC ~6,500 (≈40 min spoken) · Fisher ~5,500 · Gen ~3,900 (≈22–26 min) · Maxinomics ~3,650 · AotP ~2,500. Default for the user: 3,500–4,500 words.

## 2. Position norms (fraction of runtime, weighted corpus medians)
| beat | target | evidence |
|---|---|---|
| cold open → explicit promise/question | ≤0.10 (hard cap 0.16) | promise wmed 0.16; 39% in first decile |
| sponsor read | 0.30 ±0.10, after the promise and first payoff | 41/76 videos, wmed 0.31, IQR 0.20–0.42; Fisher 0.29–0.40, Gen 0.31–0.47, AotP 0.15–0.23, Maxinomics early 0.06–0.10 |
| turns / reversals, questions, numbered points, callbacks | spread evenly — roughly one per decile | all four ~10% per decile |
| conclusion pivot ("so where does that leave us") | ~0.75–0.90 | CONCL wmed 0.74, mass in last 3 deciles |
| CTA | final 2% only | 91% in last decile |
AIC has no sponsor; its ask is a civic action.

## 3. Mode templates (detail in beat-maps.md)
- **Gen explainer (default):** 0–0.08 relatable hook + thesis · 0.08–0.15 "why should you care" + stakes · 0.15–0.30 point 1 · ~0.31 sponsor (bridged to topic) · 0.32–0.55 point 2 · 0.55–0.75 point 3 + twist · 0.75–0.92 hope/agency · 0.92–1 newsletter, next video, like.
- **AIC clocked narrative:** 0–0.05 dated scene · ≤0.05 thesis question · 0.05–0.65 timeline chapters with timestamps · 0.65–0.8 analysis/exhibits · 0.8–0.9 personal anecdote · 0.9–1 asks + link.
- **Fisher investigation:** 0–0.08 artifact + question · 0.08–0.3 setup/history · ~0.3 sponsor · 0.3–0.8 numbered board, one block per threat/solution · 0.8–0.95 "is it right?" / uncertainty · close = restated claim.
- **Maxinomics essay:** vignette 0–0.1 (often early sponsor) · game/contrast cases · data · reframe · footnotes coda.
- **AotP ladder:** paradox ≤0.05 · go back · one rung per ~10% · echo to present ~0.8 · philosophical line · email list.

## 4. Title–script alignment
The title's claim is restated in the first 10% and again in the last 10% (Fisher/Gen habit). If the promise appears after 0.2, move it up.

## 5. Drag & bad-ending diagnosis
Drag = a decile with no turn, number, question or callback → insert one. Bad ending = CTA before conclusion pivot, or conclusion before 0.7, or new information after 0.9.
## Deep-read additions 
- **Roadmap formulas in the first 5%:** 3-question roadmap ("as always, we need to answer a few important questions"; Gen preppers: "are Preppers just… is America… how afraid should we be"); numbered promise ("There are only four ways this debt will ever be resolved").
- **Primer block with apology (HMW):** 0.14–0.50 can be a pure primer if announced; sponsor right after the primer ("So, now you know how X works. It's time to learn why it isn't working").
- **Sponsor placement by hand-read:** Gen 0.20–0.37 (cartel pt1 0.22, pt2 0.25, preppers 0.22, gen-z 0.32); HMW ~0.50; Boyle ~0.15; recycling 0.17; Cleo Abram 0.56 (story-bridged). Every bridged sponsor uses a lived mishap or the exact topic.
- **Chaptered essay (supporting finance channels):** named eras as chapter cards (SPECULATIVE ERA → OPPORTUNITY ERA → LEFT BEHIND → CONSEQUENCES), chronological.
- **Ride-along / field template (Gen w1–3):** hook 0–0.03, roles 0.03–0.07, field segment, sponsor ~0.22, interviews 0.28–0.45, expert 0.45–0.55, set-piece climax 0.65–0.88 (chase, range, border wall), verdict 0.88–0.98, CTA.
- **Street-interview template (Gen w1):** montage 0–0.05, premise Q, positions, older-gen/other-side lens ~0.2, sponsor ~0.3, deeper Qs, global/stat block ~0.7, advice/regret 0.8–0.9, thesis + personal proof 0.9–1.
- **Explainer with paradox (business-of-tech):** headline stack 0–0.08, case pile, deferred definition at ~0.4 ("Before we can answer this, what does X actually mean?"), named law payoffs (Goodhart, Jevons), pattern parallel, close.
- **Mid-video sub ask:** appears only in supporting channels (tokens video "road to 1 million"); anchors still avoid it — keep rule "no mid-video subscribe nag" for anchor leans.

## AI tells on this axis (flag on sight)

| tell | corpus behaviour | card |
|---|---|---|
| intro longer than 15% before any promise | hook and promise ≤0.10 | R01, R02 |
| "In this video we will cover…" agenda | a question roadmap or numbered promise | R02, R12 |
| sponsor dropped cold, mid-thought | cliffhanger into the sponsor, bridge, and re-entry line | R09, R11 |
| five equal-length sections with no turn | an act break every 15–20% | R13 |
| no counter-argument | a fair counter-section at 0.60–0.85 | R19 |
| conclusion recaps every point | a verdict line and a lever | R25, R26 |
| new information after 0.9 | close only | R38 |

## Common failures and the fix

- **Saggy middle.** A decile with no turn, number, question or callback. Fix: R13, plus a re-hook from channel-audience.
- **Late promise.** Fix: move the thesis question to ≤0.10 (R02).
- **Wrong sponsor window for the lean.** Fix: use the R08 lean windows.
- **Duplicated paragraph** left from drafting: R37.
- **Rambling outro.** More than 8% of runtime after the verdict: R38.
- **Factual slip in a structural beat** (wrong date in the timeline header): R39. Flag it and never silently fix a fact.
- **One-sided polemic.** Fix: R40 together with R19.

## Failure modes (structure)

- **Habit engine.** Always picking Gen or AIC regardless of title → R41/R42.
- **Empty bans.** `forbidden_engines: []` → R43. A packet with no bans is incomplete.
- **Fake clock.** Invented hour-stamps on a non-crisis title → R44, R39.
- **Agenda intro.** "In this video we will cover…" → R02 rewrite as a thesis question.
- **Silent BACKTRACK ignore.** Later skill swapped engines and structure shrugged → R50.
- **Beat map from the wrong lean.** Gen sponsor at 0.08 or AIC with a mid-video subscribe nag → R08.


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



## Detector gate (owned by channel-language)

The pipeline publish bar is local detector **score ≤ 2**. This skill does not run the gate; language does. Do not soft-pass language work upstream.

## Editing contract

1. **Preserve meaning, facts and the user's opinions.** You change how the script lands, never what it claims. If a fix needs a new fact, leave a `[NEEDS SOURCE]` marker; never invent one.
2. **Cite a card for every change.** Each edit names a pattern ID from `references/patterns.md` (e.g. `L16`, `T23`, `R08`, `A32`). An edit with no card is a taste edit: mark it `[taste]` and keep those under 10% of edits.
3. **Respect the lean.** Pick one creator lean (section "Creator leans") before editing. Cards tagged for another lean are optional, and cards marked "not in X lean" are banned in X.
4. **Do not over-apply.** Every card has a rate or cap. Hitting a card twice as often as the corpus does is a defect, the same as missing it.
5. **Quote, don't paraphrase, when you grade.** Every flag quotes the draft span it refers to (≤25 words).
6. **Never soften the grade.** Scores come from the rubric below and are reported as they fall. No rounding up and no "basically passes".

## Modes

| mode | trigger | output |
|---|---|---|
| `grade` | "critique / score / what's wrong" | rubric table + flags, no rewrite |
| `rewrite` | "fix / rewrite / tighten" | rewritten text + change log with card IDs |
| `plan` | "outline / plan / before I write" | checklist of cards to hit, by section |
| `drill` | "practice / teach me" | one drill from `references/drills.md` |
| `audit-only` | pairing with another channel-* skill | flags for this axis only, no overlap |

Default when unclear: `grade`, then offer `rewrite`.

## Severity tiers

- **P0 — blocks publish.** A P0 card missing or broken anywhere it applies. One P0 caps the axis score at 6/10.
- **P1 — noticeably off-voice.** Two or more P1 misses cap the score at 8/10.
- **P2 — polish.** Never caps the score. Report the top three only.

## Grading rubric (0–10 for this axis)

Start at 10. Subtract:
- 2.0 per P0 card that applies and is missing or broken
- 1.0 per P1 miss, up to 4.0 total
- 0.5 per P2 miss, up to 1.5 total
- 1.0 per over-applied card (more than 2x its corpus rate)
- 1.0 per banned move for the chosen lean

Then apply the caps above. Report the raw arithmetic next to the final number so the grade can be audited. Do not adjust a score after seeing it.

## Output format

```
AXIS: <language|storytelling|structure|audience>   LEAN: <creator>   MODE: <mode>
SCORE: x/10   (arithmetic: 10 − … = …; cap applied: …)
P0 FLAGS
- [ID] "quoted span" → what to do
P1 FLAGS
- …
P2 (top 3)
- …
KEEP (what already works, with IDs)
- …
```
In `rewrite` mode, follow this with the rewritten text and then `CHANGES: ID — before → after`, one line per change.

## Rewrite procedure

1. Read the whole draft once without editing. Note its length, mode, and lean.
2. Run the hard-rule checks. They are mechanical, so fix them first.
3. Walk the P0 cards in ID order, then P1, then P2. For each card, decide apply, keep, or flag.
4. Re-read aloud (in your head) at speaking pace. Every sentence must be sayable in one breath or broken on purpose.
5. Recount the rates against the numeric targets. Remove any over-applied instances.
6. Produce the change log. Any change without an ID gets `[taste]`.


## Pairing with the other channel-* skills

Run the four axes in this order on a full draft, each in `audit-only` mode, then merge the flags:
1. **channel-structure**: is the skeleton right? Covers the windows, the sponsor, act breaks and the close.
2. **channel-storytelling**: does the skeleton carry a story? Covers the engine, characters, reveals and the ending.
3. **channel-audience**: is the viewer in the room? Covers address, trust, retention and the ask.
4. **channel-language**: does every line sound like the lean? Covers rhythm, register, turns and bans.

Ownership rules, so flags don't overlap:
- A late hook is a structure flag (R01). A weak hook line is a storytelling flag (T01). Hook wording is a language flag.
- A missing viewer address is an audience flag (A01). Too few "you" words is a language rate flag (L10).
- A sponsor in the wrong window is structure (R08). A sponsor bridge that doesn't fit the story is storytelling. Read copy that doesn't sound like the lean is language.
- An unclosed open loop is audience (A16). A setup with no payoff is storytelling (T31).
- When two skills flag the same span, keep the higher-priority card and drop the other.

Combined score = the mean of the four axis scores, each reported separately. Never average away a P0: any P0 on any axis means the draft is not ready to publish.


## Progressive disclosure (when to load what)

- Always: this SKILL.md, then `references/strategy-selector.md` (before any beat map).
- Always on full_rewrite: `references/pipeline.md`.
- When picking beats: `references/beat-maps.md`, `references/opener-close-library.md`.
- When grading: `references/patterns.md` (R01–R50), `references/drills.md` if practising.
- Deep evidence: `references/deep-read-findings.md`, `references/beat-positions-train.md`.


## Pattern index (full cards in `references/patterns.md`)

**A. Opening architecture (0-0.12)**
- `R01` Hook inside 15 seconds (P0): Count words to the first stake. Over 60 = fail.
- `R02` Thesis question stated by 0.08 (P0): Locate it; if absent by 10%, flag.
- `R03` Why-should-you-care beat (P0): Gen lean: required within 0.1.
- `R04` Agenda roadmap (P1): One sentence, 2-3 items, by 0.12.
- `R05` Why-I-made-this beat (P1): Within 0.15.
- `R06` Credibility tag for scenarios (P1): Within 0.05 in any speculative script.
- `R07` Steelman 'other videos get it wrong' position (P1): In first 15%.

**B. Sponsor placement**
- `R08` Sponsor window 0.10-0.25 (P0): Place the read after the thesis question, before the first mechanism.
- `R09` Cliffhanger into sponsor (P1): Last line before sponsor = open question.
- `R10` Topical sponsor bridge (P1): One clause of link.
- `R11` Re-entry line after sponsor (P0): Always.

**C. Middle architecture (0.12-0.8)**
- `R12` Numbered phases (P0): 3-4 named parts; each opens with its number.
- `R13` Act break every 15-20% (P0): Mark turns on the beat map; gaps over 25% = flat middle.
- `R14` Chapter backstory jump (P1): Open with 'time for a little backstory' and close with 'Anyway, back to'.
- `R15` Sidebar flagged as sidebar (P1): Open and close each sidebar.
- `R16` With-me-so-far checkpoint (P1): Once per 1,500 words in mechanism-heavy pieces.
- `R17` Stakes escalation 'first third' (P1): At 0.3-0.4.
- `R18` Calibration aside (P1): Once, in the middle.
- `R19` Fair counter-section (P0): Required in argumentative scripts.
- `R20` Numbered explanations list (P1): Use for competing causes.
- `R21` Here's-where-it-comes-together (P1): Once.

**D. Mid-roll and engagement placement**
- `R22` Mid-video subscribe ask (P2): Max one.
- `R23` Late plug for still-watching viewers (P2): Reward loyal viewers with the plug.
- `R24` Footnotes segment (P2): After the main close.

**E. Closing architecture (0.85-1.0)**
- `R25` Verdict line (P0): In final 10%.
- `R26` Lever / what you can do (P0): Required in advocacy pieces.
- `R27` Next-video CTA (P1): Last 20 seconds.
- `R28` Sign-off last (P1): Nothing after except footnotes.

**F. Beat maps by format (positions are fractions of runtime)**
- `R29` Mystery-story beat map (AIC) (P0): Check each beat position ±0.07.
- `R30` Map explainer beat map (Fisher) (P0): As R29.
- `R31` Money-power exposé beat map (Gen) (P0): As R29.
- `R32` Concept essay beat map (Maxinomics) (P0): As R29.
- `R33` First-principles beat map (AotP) (P0): As R29.
- `R34` Scenario beat map (Species) (P1): As R29.
- `R35` Finance-satire beat map (Boyle/HMW) (P1): As R29.
- `R36` Street-interview beat map (old Gen) (P2): Only for interview formats.

**G. Structural defects to flag**
- `R37` Duplicated paragraph (P0): Search for repeated 15+ word spans.
- `R38` Rambling outro (P1): Last 150 words must contain verdict, lever or callback.
- `R39` Factual-slip flag (P0): Check every number against the brief.
- `R40` One-sided polemic (P1): Grade with R19.

**H. Strategy selection (title → engine)**
- `R41` Diagnose title before engine (P0): Mandatory first move of every structure run. Emit all four lines.
- `R42` One strategy_id only (P0): Packet must contain one strategy_id and its engine.
- `R43` Forbidden engines list (P0): forbidden_engines length ≥ 1.
- `R44` Ban clocked without a clock (P0): If evidence type ≠ timeline, ban clocked.
- `R45` Ban ladder on outrage titles (P1): If stakes are outrage/agency, ban ladder-only.
- `R46` Ban street off the street (P1): No interview shoot → ban street.
- `R47` Ban artifact without an artifact (P0): No showable artifact → ban artifact; pick explainer or essay.
- `R48` Ban speculative on settled history (P1): If the event already ended, ban speculative.
- `R49` Success test line (P1): Required in the STRATEGY PACKET.
- `R50` BACKTRACK only on engine mismatch (P0): If audience/language finds the engine wrong, return a one-line objection.


## Gotchas (from research + corpus)

- Never invent timestamps to force an AIC clocked shape. Ban the engine instead (R44).
- A STRATEGY PACKET with empty `forbidden_engines` is incomplete (R43) — agentskills "gotchas" pattern: the mistake is assuming any engine works.
- Sponsor before the promise is a measured failure mode; Gen median sits ~0.31.
- Progressive disclosure: load `strategy-selector.md` before `patterns.md` so you do not card-apply your way into the wrong engine.

## Drills (`references/drills.md`)

1. Contrastive pairs — 50 generic → corpus pairs.
2. Imitation rewrite — six topics × three P0 cards × a lean.
3. Opener library — tag real lines, then imitate.
4. Beat-map / strategy check — STRATEGY PACKET + runtime windows.
5. Catalogue audit — one row per card.

## Corpus and weights (all 117 studied)

117 transcripts across 13 creator folders, total weight 377.5. With the user's approval the earlier train/dev/sealed split was dissolved; all 117 were read and noted (`build/stage/notes/`, 117/117). No held-out set remains.

| creator | role | weight tiers |
|---|---|---|
| ai-in-context (Aric Floyd) | top anchor | 7 (best), 6 |
| max-fisher | top anchor | 6 (best), 5 |
| gen (the user's channel) | own voice | 5 (best/new), 3, 1 (old street-interview era) |
| maxinomics | anchor | 4.5 (best), 3.5 |
| art-of-the-problem | anchor | 4 (best), 3, 1 (lectures) |
| especially-misc / coldfusion / johnny-harris / species / patrick-boyle / how-money-works / other / economics-explained | supporting | 1–3 |

Rule: when leans conflict, follow the higher-weight creator. Gen 5-tier is the user's own target voice; AIC and Max Fisher set the craft bar.
Caveat: numeric rates/positions were measured on the original 76-video set. Pattern cards and strategy rules come from reading all 117. Every card quote is verbatim-checked across all 117 transcripts.
