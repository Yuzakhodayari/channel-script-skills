---
name: channel-audience
description: Engineer a YouTube script for the AUDIENCE the way the user's channel blend does it — AI In Context (7x), Max Fisher (6x), Gen (5x, the user's own channel), Maxinomics (4.5x), Art of the Problem (4x). Covers retention devices, re-hooks, curiosity gaps, open loops, direct "you" address, objection pre-emption, relatability, outrage/hope calibration, credibility and honesty signals, scale comparisons, viewer games, share triggers, CTA psychology, humor and stakes for "you". Use when the user asks to make a script more watchable, fix drop-off, add hooks or re-hooks, make it hit harder, get more comments or shares. Stage in the channel-script pipeline (structure → storytelling → audience → language). Pair with channel-structure and channel-language.
---

# channel-audience (v6 pipeline — all 117 scripts, 45 named patterns)

References: `references/patterns.md` (45 cards), `references/drills.md`, `references/pipeline.md`, `references/strategy-selector.md`, `references/detector-gate.md`, plus v4 reference files retained.

## Pipeline position

This is **stage 3/4** of the channel-script pipeline (see `references/pipeline.md`).

1. channel-structure — diagnose title → STRATEGY PACKET (forbidden engines named)
2. channel-storytelling — rewrite story with the chosen engine
3. channel-audience — inject audience devices at corpus density
4. channel-language — humanize word-level; **detector gate score ≤ 2**

On `full_rewrite`, do not skip stages. On `audit-only`, grade this axis alone.
Success for the pipeline: a full narration that fits THIS title's strategy, sounds like the weighted blend, and passes the local AI-writing detector at **score ≤ 2**.

## When to use

Use for the **audience** axis: placing the viewer, trust, retention, community, humor, calibration, CTAs, density restraint.

Trigger examples: retention / you-address / CTA / comment prompt.

Do **not** use for thumbnails, title-only SEO, or analytics (those are pro-yt skills).

## Workflow

1. **Intake.** Read the envelope (title, topic, source, lean, protected constraints). Load `references/pipeline.md`.
2. **Stage work.** Inject devices; count density; match CTA to lean.
3. **Card pass.** Walk the pattern index in priority order (P0 → P1 → P2). Honour **Do NOT apply when**.
4. **Grade or rewrite** using the rubric and output format below. Cite every card ID.
5. **Handoff.** Fill your section of the envelope. FEED to language.
6. **Self-check.** No over-applied cards, no invented facts, score unsoftened.

## Input / output contract

### Incoming
- STORY DRAFT + STRATEGY PACKET
- Lean's density target (A42)

### Produce
- **AUDIENCE-ENGINEERED DRAFT**: same story with viewer address, trust, retention, comment prompt, CTA matched to lean
- Device-density count per 1k words

### Outgoing
- `FEED` to `channel-language`
- Do not invent personal stakes (A44)

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

References: `references/device-catalog.md` (Method 5: device → example → where), `references/device-rates-train.md` (measured rates per creator and decile).

## 1. Device budget for a ~4,000-word script (scaled from weighted corpus rates)
| device | per script | where (measured deciles) |
|---|---|---|
| question to the viewer | ~20 (5% of sentences) | everywhere |
| show-and-tell / "look at this" artifact | 3–6 | everywhere; open with one |
| viewer game / "imagine you" | 1–2 | spread (d2, d5, d8 peaks) |
| honesty hedge ("I don't know", "to be clear") | 1–2 | back half (d9–d10 = 43%) |
| objection pre-empt ("I know what you're thinking") | 1 (Gen lean: 2) | d4–d5 or d9 |
| reveal tease / open loop ("more on that later") | 1 | first decile (38%) |
| "what others get wrong" | 0–1 | first decile (43%) |
| stakes "if something isn't done" | 1 (Gen) | intro and final decile |
| scale comparison ("It would be like…") | 1–2 | where the big number lands; d9 peak |
| personal stake (where I live / I met him) | 1 | middle or d9 |
| agency / concrete ask | 1 | last 20% only (100%) |
| self-deprecating joke | 0–1 | early or at sign-off |

## 2. Calibrating emotion by lean
- Gen: outrage → hope. Name the system, give the viewer a lever ("you have options"). Stakes are cultural ("one of the last things Americans can agree on").
- AIC: worry with restraint. Dry humor deflates fear; honesty hedges keep trust; close = specific civic actions + "send them this video".
- Fisher: curiosity over outrage. "Okay, with me so far?" check-ins, sympathetic logic for adversaries, honest uncertainty.
- Maxinomics: playful; second-person games; low outrage.
- AotP: wonder; the viewer builds the model; minimal direct address.

## 3. Re-hook rule
Every decile needs at least one of: question, turn, number, callback, artifact (structure stats show each spread ~10%/decile). If a 2-minute stretch has none, add the cheapest: a direct question or a "But here's the problem."

## 4. Trust signals
Cite a named source or document; hedge once where evidence is thin; admit bias ("assume I'm biased") at most once; never fake certainty. Trust > hype for every anchor.

## 5. CTA psychology
One ask, last 2%. Gen: newsletter → watch next video → like. AIC: action + link + share. Maxinomics: "I'll see you in the next video." No mid-video subscribe nags (absent in all anchors).
## 6. Deep-read additions 
- **Viewer-bias callout:** "let's be real you thought of a certain profile when you clicked on this video" (Gen preppers) — 0–1 per script, mid.
- **Voiced viewer objection with name:** "you might be thinking, okay, come on Max…"; "Okay, but I saw a TikTok of…" (recycling). Counts as objection pre-empt.
- **Proxy-for-viewer questions on location:** "for my viewers like explain to me…"; "I don't know if you guys as a viewer can feel it but we're going fast".
- **Invite correction:** "If someone can prove me wrong… comment section"; "I'm also always willing to change my mind" — pairs with an honesty hedge in the last 20%.
- **Disclaimer of expertise:** "I'm not an AI expert, not even close. But what I am extremely interested in is…"; "I'm by no means an expert".
- **Inclusivity / sub-audience address:** "so nobody feels left out. Good? Good."; "Fellas…"; Species message aimed at people working in AI.
- **Identity CTA:** "If you believe in optimistic science and tech stories, subscribe." Gen variants: newsletter ("one big story… without the bias"), mission link ("leading the future of Journalism together"), Discord ("debate… from both sides").
- **Stake to the viewer's wallet:** "No one wants to throttle a company whose value is tied to their 401k."; "it eats through my wallet".
- **Humor calibration:** self-roast (lab coat too small; "your boy can shoot"); "bad joke" retraction keeps edgy jokes safe; deadpan Irish/Australian identity jokes for Boyle/Econ Explained leans only.
- **Cross-creator credit** builds trust: "Patrick Boyle did an entire video on… I will leave a link".

## AI tells on this axis (flag on sight)

| tell | corpus behaviour | card |
|---|---|---|
| "Let me know your thoughts in the comments below!" | a specific question the viewer can answer | A23 |
| "Smash that like button" mid-video | asks only in the final 10% | A26, A27, A37 |
| the viewer is never in the example | the viewer is cast as the actor | A01 |
| relentless alarm with no calibration | a don't-panic calibration line | A32 |
| claims with no source or stake | source transparency and disclosed stake | A08, A11 |
| "We must all come together" close | one concrete action or a choice | A37, A40 |
| open loops never closed | every loop closed | A16 |

## Common failures and the fix

- **No viewer in the room.** Fewer than 3 devices per 1k words. Fix: A01, A03, A04 (A42 density).
- **Device spam.** More than 8 per 1k. Cut to the strongest, keeping P0 cards first.
- **Insulting the viewer.** Teasing (A05, A31) more than once, or in a non-Gen lean. Cut it.
- **Trust gap.** A critical claim with no disclosure or source. Fix: A08, A10, A11.
- **Dead CTA.** Generic subscribe. Fix: identity or community stat (A26, A39), or a real action (A37).

## Failure modes (audience)

- **No viewer in the room.** <3 devices/1k → A01, A42.
- **Device spam.** >8/1k → A43.
- **Fake personal stake.** → A44.
- **Wrong-lean CTA.** AIC ending on "smash like" → A45.
- **Unclosed open loops.** → A16.
- **Generic comment ask.** "Let me know your thoughts" → A23.


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

- Always: this SKILL.md + STORY DRAFT.
- Always on full_rewrite: `references/pipeline.md`.
- Rates: `references/device-rates-train.md`, catalogue: `references/device-catalog.md`.
- When grading: `references/patterns.md` (A01–A45).
- Drills: `references/drills.md`.


## Pattern index (full cards in `references/patterns.md`)

**A. Who is watching: placing the viewer**
- `A01` Viewer inside the example (P0): Every mechanism section has one 'you' example the median viewer recognises.
- `A02` Put-yourself-there prompt (P1): Before a decision point.
- `A03` Name the viewer's assumption (P0): In the first 10%, name the picture the viewer arrived with.
- `A04` Bet on the viewer's experience (P1): Once, about a widely shared experience.
- `A05` Implicate the viewer (gently) (P1): Max twice; follow with a self-own (L24).
- `A06` Name the viewer's feeling (P0): Once, at the human-cost beat.
- `A07` Ask the viewer to be honest with themselves (P2): Once.

**B. Trust devices**
- `A08` Disclose your own stake (P0): Before criticising the thing you're tied to.
- `A09` Check-my-work invitation (P1): Once, near a contested claim.
- `A10` 'I'm not one of those people' disclaimer (P1): Before the critical thesis.
- `A11` Source transparency (P1): At each major claim.
- `A12` Admit confusion (P2): Once; makes the viewer feel smart.
- `A13` Not-cherry-picking line (P1): After the most striking example.
- `A14` Fair-to-the-dude line (P2): When an individual appears on screen.
- `A15` Content warning with skip (P1): Required before graphic content.

**C. Retention devices**
- `A16` Open loop with delayed reveal (P0): Each loop closed within 40% of runtime.
- `A17` 'But hold on, there's more' stacker (P1): Max twice.
- `A18` Bear-with-me promise (P1): Before any dry mechanism.
- `A19` Reward the stayers (P1): In final 10%.
- `A20` Mini-game with viewer (P2): Once per script.
- `A21` Sit-down warning before a number (P2): Once, on the biggest number.
- `A22` Ruin-your-day add-on (P2): Once.

**D. Comment and community devices**
- `A23` Opinion question to comments (P1): One, in the last 10%; must be specific.
- `A24` Pre-empt the comment insult (P1): Once, at the most contrarian claim.
- `A25` Viewer names / shout-outs (P2): In Q&A formats.
- `A26` Community stat for the ask (P2): Once.
- `A27` Milestone ask (P2): Once.

**E. Humor for the audience**
- `A28` In-group joke for regulars (P2): Once; regulars feel seen, newcomers don't miss the point.
- `A29` Joke on the narrator's location/life (P2): Once.
- `A30` Prop joke (P2): Once.
- `A31` Punchline at the viewer's expense, softened (P2): Max once per script.

**F. Calibration for audience trust**
- `A32` Don't-panic calibration (P0): Once per alarming script.
- `A33` Most-are-fine percentages (P1): After the scariest example.
- `A34` Reality anchor after fiction (P0): Every time a real study appears inside a fictional frame.
- `A35` Not-advice disclaimer (P1): Finance/legal tips.
- `A36` Can't-predict humility (P1): Before a forecast.

**G. Audience-specific calls to action**
- `A37` Action you can take (P0): Final 10%.
- `A38` Free resource, not a course (P2): Once, after the payoff.
- `A39` Identity-based subscribe (P2): Once.
- `A40` Choice close (P1): Final 5%.
- `A41` Respect-the-viewer framing (P1): Once.
- `A42` Audience-device density check (P0): Count devices per 1k words; flag under 3 or over 8.

**H. Pipeline density and restraint**
- `A43` Do not device-spam (P0): Count per 1k; cut weakest P2 first if over 8/1k.
- `A44` Do not invent a personal stake (P0): If no stake, skip A08 rather than fabricate.
- `A45` CTA matches strategy (P1): Pick CTA from the strategy packet's lean.



## Research takeaways baked into this skill

From **avoid-ai-writing** (infomercial hooks, engagement bait): device spam is an AI tell; density has a ceiling (A43).
From **voice-preserving-rewriter**: never invent a personal stake to sound warmer (A44).
From **humanizer** (wrong reader): do not re-explain what the regular viewer already knows; reward stayers instead (A19).
From **anti-ai-slop-writing**: self-check before handoff — specific comment question, not "let me know your thoughts".
From **agentskills.io**: checklists and validation loops; count devices per 1k before FEED to language.

## Gotchas (from research + corpus)

- Density has a ceiling. Gen is high; Fisher/AIC/AotP are lower. Over-winking reads as AI engagement bait (A43, avoid-ai "infomercial engagement hooks").
- Never fabricate "I've been short this stock" (A44). voice-preserving-rewriter + avoid-ai editing contract: no invented experience.
- CTA must match lean. AIC wants a civic action; Gen wants newsletter/next; Maxinomics wants a soft "see you".
- "Let me know your thoughts below" is banned; ask a specific question (A23).

## Drills (`references/drills.md`)

1. Contrastive pairs — 45 generic → corpus pairs.
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
