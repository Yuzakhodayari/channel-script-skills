---
name: channel-storytelling
description: Plan, write, or critique the storytelling of a YouTube script for the user's channel, a weighted blend of AI In Context (7x), Max Fisher (6x), Gen (5x, the user's own channel), Maxinomics (4.5x) and Art of the Problem (4x). Use when the user asks for a cold open, hook, story beats, outline-to-script, tension, open loops, reveals, characters, villains, callbacks, or an ending; or asks why a script feels flat. Use channel-language afterwards for word-level voice.
---

# channel-storytelling (v6 pipeline — all 117 scripts, 46 named patterns)

References: `references/patterns.md` (46 cards), `references/drills.md`, `references/pipeline.md`, `references/strategy-selector.md`, `references/detector-gate.md`, plus v4 reference files retained.

## Pipeline position

This is **stage 2/4** of the channel-script pipeline (see `references/pipeline.md`).

1. channel-structure — diagnose title → STRATEGY PACKET (forbidden engines named)
2. channel-storytelling — rewrite story with the chosen engine
3. channel-audience — inject audience devices at corpus density
4. channel-language — humanize word-level; **detector gate score ≤ 2**

On `full_rewrite`, do not skip stages. On `audit-only`, grade this axis alone.
Success for the pipeline: a full narration that fits THIS title's strategy, sounds like the weighted blend, and passes the local AI-writing detector at **score ≤ 2**.

## When to use

Use for the **storytelling** axis: hooks, characters, engines, toy models, reveals, emotion, endings, engine fidelity.

Trigger examples: cold open / POV / reveal / ending.

Do **not** use for thumbnails, title-only SEO, or analytics (those are pro-yt skills).

## Workflow

1. **Intake.** Read the envelope (title, topic, source, lean, protected constraints). Load `references/pipeline.md`.
2. **Stage work.** Obey STRATEGY PACKET; draft the spine; list plants.
3. **Card pass.** Walk the pattern index in priority order (P0 → P1 → P2). Honour **Do NOT apply when**.
4. **Grade or rewrite** using the rubric and output format below. Cite every card ID.
5. **Handoff.** Fill your section of the envelope. FEED to audience.
6. **Self-check.** No over-applied cards, no invented facts, score unsoftened.

## Input / output contract

### Incoming
- STRATEGY PACKET from `channel-structure` (required for `full_rewrite`)
- Source facts/notes; protected constraints
- Must read `forbidden_engines` and refuse to use those signature moves

### Produce
- **STORY DRAFT**: full narration spine filling every beat_map slot, with POV, plants/payoffs listed
- No CTA copy polish, no detector run

### Outgoing
- `FEED` STORY DRAFT + updated envelope to `channel-audience`
- `BACKTRACK` to structure only if the engine is impossible given the facts

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

References: `references/opener-close-library.md` (all 76 corpus openers/closes, by weight), `references/hook-types.md` (classified), `references/story-engines.md` (per-creator engines, contrastive pair).

## 1. Choose the story engine
| engine | creator | spine | use for |
|---|---|---|---|
| **Clocked true story** | AIC | dated scene → countdown timestamps ("61 hours since…") → reversal → what it tells us → personal anecdote → ask | events with a timeline |
| **Speculative scenario** | AIC | "Welcome to the very near future" → named fictional company/agent → hour-by-hour escalation → "this already happens" evidence | risk/future topics |
| **Artifact investigation** | Fisher | "I want to show you something" (document/map) → question → numbered threats on a board → how each was solved → "Is it right?" test → honest uncertainty | geopolitics, institutions |
| **Outrage-to-agency explainer** | Gen | relatable memory/experience → "But why should you care?" → villain system (PE, Wall St, algorithms) → 3 points → "what other videos get wrong" → stakes "if something isn't done" → hope/consumer agency | money & power |
| **Vignette essay** | Maxinomics | cinematic historical scene or prop → game with viewer → two contrasting cases → data authority → reframe → footnotes | concept essays |
| **Mechanism ladder** | AotP | historic broadcast/paradox → "to understand this we need to go back" → toy model rungs → echo to today (2008) → philosophical close | first principles |

## 2. Cold open rules (train library, 76 openers)
Weighted regex classification of the first 2 sentences (hook-types.md, approximate): scene/date 30%, bold claim/other 35%, memory or question to "you" 17%, artifact show-and-tell 14%, paradox 3%, imagine/game 1% (games mostly appear later, not as the first line).
- First sentence is concrete (a date, an object, a person, a price). Never a thesis in abstract nouns.
- Within ~15% of runtime say the question the video answers (promise median 0.16).
- Plant one open loop you close after the midpoint ("more on that later", "I'll get to that").

## 3. Characters and villains
- Named humans with one vivid detail (Altman in a Vegas hotel; Kim's hackers; a farmer with rice).
- Villains are systems with a face: a firm, a board, a law. Gen names them; AIC hedges about intent; Fisher explains their logic sympathetically ("And you know what? They succeeded.").
- Give the viewer a role: "you" are the renter, the worker, the citizen.

## 4. Tension & reveal mechanics
- Reversal words: "Not exactly." "Or are they?" "But here's the problem." Use 1 per ~2–3 minutes.
- Escalating clock or numbered stakes (threat 1/2/3; exhibits A–D).
- Callbacks: return to the opening object/scene in the last 20% (piracy → "remember this", Barclays ATM, Nixon).
- Twist the obvious villain at least once (Gen: "just because PE invests doesn't automatically make it bad").

## 5. Endings (train close library)
Weighted close classification of last 6 sentences (approximate): restated thesis + CTA 43%, agency/ask 34%, honest uncertainty/open question 19%, philosophical line 4% (AotP signature).
Order: final insight → concrete image or ask → short CTA (newsletter / next video). Never end on a generic moral.

## 6. Flat-script diagnosis
No scene in first 3 sentences? No stated question by 16%? No reversal in the middle third? No callback? No person? Ending abstract? Fix the first "no".
## Deep-read additions 
- **Bookend rule confirmed broadly:** most strong videos return to the opening object/scene/line at the close (Gen cartel chase, Boyle league table, recycling archival clip, Business Insider same human subject, Species "That was fiction, but here's what's not").
- **Running mystery with suspects (Boyle, Fisher):** name the puzzle early ("who did this to us"), list suspects #1–4, eliminate, payoff late.
- **Puzzle-inside-the-story detour:** "If France is in this much trouble, how is Italy… able to borrow more cheaply?" — a comic detour that lands the key concept (primary balance).
- **Skit enactment (comedic explainers, Gen):** dramatize the villain's meeting ("Imagine you're in a room with the most boring old white men…"), then "That scenario wasn't really an exaggeration" + the real document.
- **Fake-lesson / fake-redemption beat** before the real twist (Gen, recycling).
- **Scenario engine (Species/AIC):** flash-forward or authority frame, present-tense fragments, "This will matter later", reality-pivot close.
- **Mechanism engine (AotP):** problem → physical analogy (paint colours, lock) → math → worked example; recurring characters (Alice, Bob, "Eve, who is always listening"); discoverer chain; twist close (classified then rediscovered).
- **Anecdote placement:** personal anecdotes cluster at the sponsor (lived mishap → product: roaming fees, health scare, editing class) and at the close (girlfriend in Brazil, pops bought a gun).
- **Ending types expanded:** challenge-to-the-viewer ("why can't the dumb soft gen Z figure this one out"), aphorism, both-sides hypocrisy verdict + "it's just a theory", next-video cliffhanger (HMW: "how we fixed it back then").

## AI tells on this axis (flag on sight)

| tell | corpus behaviour | card |
|---|---|---|
| open on a definition or a "Have you ever wondered" question | anchors open in a scene, artifact or paradox | T01 |
| no named person in the first 15% | a POV character or named actor early | T09 |
| events listed, no engine | a clock, selection pressure, or ladder drives the story | T16 |
| mechanism explained in the abstract | toy model with small numbers | T23 |
| reveal stated before tension builds | promise of payoff, then deliver | T31 |
| ends on a moral or summary | bookend callback or concrete image | T39, T42 |
| every section has the same emotional temperature | an emotion ramp with release | T-section E |

## Common failures and the fix

- **Topic, not story.** Fix: choose an engine (table in Hard rules) and a POV character (T09).
- **Exposition dump before the hook.** Fix: in-medias-res open (T01) and move the background to the 0.10–0.20 window.
- **Villain with no logic.** Fix: give the adversary their reasons (Fisher habit), so the viewer understands the choice.
- **Twist without a plant.** Fix: plant it in the first third and pay it off with "Remember…".
- **Ending that fades out.** Fix: bookend callback (T39). Check the weak-ending flags (T42).

## Failure modes (storytelling)

- **Topic, not story.** No POV, no engine spine → T09, T16.
- **Forbidden engine drift.** Hour-stamps after clocked was banned → T43.
- **Orphan plant / unplanted twist.** → T45.
- **Moral-platitude ending.** → T46, T42.
- **Exposition before hook.** → T01.
- **Villain with no logic.** Fisher/Gen both need the adversary's reasons.


## Strategy selection (owned by channel-structure)

Not every story engine fits every title. Structure emits `forbidden_engines`. This skill must obey them (see T43 / packet).


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

- Always: this SKILL.md + STRATEGY PACKET from structure.
- Always on full_rewrite: `references/pipeline.md`.
- Before drafting: `references/story-engines.md`, `references/hook-types.md`.
- When grading/rewriting: `references/patterns.md` (T01–T46).
- For openers/closes: `references/opener-close-library.md`.
- Drills: `references/drills.md`.


## Pattern index (full cards in `references/patterns.md`)

**A. Hooks and cold opens**
- `T01` In-medias-res future cold open, then rewind (P0): Use when the story has a clear climax. First 2-4 sentences show the climax; the rewind line follows within 20 
- `T02` Dated cinematic scene open (P0): Name the day and place in sentence one, the object in sentence two.
- `T03` Contradiction question hook (P0): Hook = fact A + fact B + 'So then, why...?'
- `T04` Perception-flip hook (P1): Open with 'If you think X, not only are you correct...' or 'what I'm learning is...'
- `T05` 'Take it from this guy' clip hook (P2): Use when the claim sounds exaggerated.
- `T06` Second-person POV open (P1): Sentence one: 'You've been...' with a time or place. Keep 'you' through the first minute.
- `T07` Absurd-literal hook (P1): Follow with 'but we'll get to that in just a moment'.
- `T08` Physical-object reveal hook (P1): Object in frame within 5 seconds, surprising fact in the second sentence.

**B. Characters and point of view**
- `T09` POV character with a ticking clock (P0): Name the character within 10% and give them a countdown.
- `T10` Human-owner reaction beat (P1): One beat per act in scenario scripts.
- `T11` Named recurring side character (P1): Pay them off in the last third.
- `T12` Narrator as character (P0): Add one 'then I talked to' or 'that's when I started' beat per act.
- `T13` Villain case study (P1): Use after the abstract mechanism, to make it human. Must be sourced.
- `T14` Second-person vignette (P1): One per section in essays about surveillance, debt, apps.

**C. Engines and escalation**
- `T15` Escalating dated timeline (P0): Each time stamp adds a count; at least 4 steps.
- `T16` Selection-pressure engine (P1): State the rule plainly once, then show three consequences.
- `T17` Moral contrast by numbers (P1): Give both numbers and the outcome in two short lines.
- `T18` Real-world precedent grounding (P0): One per speculative act.
- `T19` Scale ladder by comparison (P1): Escalate at least three rungs.
- `T20` Compression line for a big shift (P1): Once, right after the escalation peaks.
- `T21` Dramatized dialogue scene (P2): Max one per script; keep lines under 12 words.
- `T22` Ironic juxtaposition (P1): No explanation after; the gap is the joke.

**D. Analogies and toy models**
- `T23` Toy model with characters (P0): Name the characters, give small numbers, run the model step by step.
- `T24` Analogy spine for the whole video (P1): State it in act one, re-use it in each act, close on it.
- `T25` Hypothetical town (P1): Use with real numbers scaled down.
- `T26` Fable-like metaphor (P1): One sentence of fable, one of mapping.
- `T27` Bathtub/physical metaphor (P2): Use for flows (water, oil, money).
- `T28` Indifference metaphor (P2): Once, at the darkest beat.

**E. Reveals and twists**
- `T29` Mid-video twist reveal (P0): Set up an assumption early; break it with one sentence.
- `T30` Answer that is the absence (P2): Use when sources stonewall.
- `T31` Promise of payoff (P0): One per script, in first 10%; audit that it is paid.
- `T32` Counter-intuitive historical twist (P1): State the fear, then the data.
- `T33` Story subversion close (P1): Final 5%.

**F. Emotion and stakes**
- `T34` Personal stakes confession (P0): Once, in the final third.
- `T35` Kitchen-table stakes (P0): Every act ends with one 'and here's what it means for you' line.
- `T36` Victim's quote (P1): One per act in investigative pieces.
- `T37` Quiet tragedy beat (P1): After the biggest number, a single human cost.
- `T38` Hope beat with agency (P0): Final 10%; must name a lever the viewer has.

**G. Endings**
- `T39` Bookend callback close (P0): Write the close by rereading the hook.
- `T40` Open-question close (P1): Pair with what we do know.
- `T41` Truth disclaimer close (P1): In every scenario script.
- `T42` Weak-ending flags (P0): Grade every close: does the last line carry an image, a callback, or a lever? If not, flag.

**H. Engine fidelity (pipeline)**
- `T43` Obey forbidden_engines (P0): Check structure.forbidden_engines before drafting each act.
- `T44` One POV through the spine (P0): Name the POV in the story packet; do not swap mid-script.
- `T45` Plant then payoff, never orphan (P0): List plants in the packet; close each before 0.9.
- `T46` Do not moral-platitude the ending (P1): Final 5% = T39 or R26/A37.



## Research takeaways baked into this skill

From **writing-beats / writing-shape / writing-fragments**: explore facts first, then exploit one path; ground every concept before a later beat leans on it; append one beat at a time when planning.
From **avoid-ai-writing-router**: typed handoffs (FEED / BACKTRACK); do not re-own structure's engine choice.
From **gen-voice / adam-voice**: self-check checklists with numeric opener rates; standing lessons beat vibes.
From **agentskills.io**: gotchas > generic advice; validation loops; progressive disclosure of `story-engines.md` only when drafting.
From **diagnosing-bugs**: if the engine cannot be fed with evidence, stop and BACKTRACK — do not hypothesise a timeline.

## Gotchas (from research + corpus)

- writing-beats rule applies: do not lean on a concept before a beat grounds it. If the STRATEGY PACKET assumes a document you do not have, BACKTRACK.
- Forbidden-engine drift is the silent killer — hour-stamps, street montages, or toy-model rice villages appearing after they were banned (T43).
- Endings: corpus closes on image/callback/lever, not a moral triad (T46). avoid-ai-writing flags generic future-narrative closers; so do we.
- One POV. Rotating "we/they/one/the industry" is an AI tell and a story tell.

## Drills (`references/drills.md`)

1. Contrastive pairs — 46 generic → corpus pairs.
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
