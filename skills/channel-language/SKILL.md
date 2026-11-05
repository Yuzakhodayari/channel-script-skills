---
name: channel-language
description: Write or humanize YouTube script narration in the user's channel voice, a word-level weighted blend of AI In Context (Aric Floyd, 7x), Max Fisher (6x), Gen (5x, the user's own channel), Maxinomics (4.5x) and Art of the Problem (4x), with supporting creators at 1-3x. Use when the user asks to write, rewrite, punch up, de-AI, or humanize a script, voiceover, hook, or narration line; when text "sounds like AI"; or when they ask for an AIC-, Fisher-, Gen-, Maxinomics- or AotP-lean. Not for story or act structure (use channel-storytelling / channel-structure).
---

# channel-language (v6 pipeline — all 117 scripts, 52 named patterns)

References: `references/patterns.md` (52 cards), `references/drills.md`, `references/pipeline.md`, `references/strategy-selector.md`, `references/detector-gate.md`, plus v4 reference files retained.

## Pipeline position

This is **stage 4/4** of the channel-script pipeline (see `references/pipeline.md`).

1. channel-structure — diagnose title → STRATEGY PACKET (forbidden engines named)
2. channel-storytelling — rewrite story with the chosen engine
3. channel-audience — inject audience devices at corpus density
4. channel-language — humanize word-level; **detector gate score ≤ 2**

On `full_rewrite`, do not skip stages. On `audit-only`, grade this axis alone.
Success for the pipeline: a full narration that fits THIS title's strategy, sounds like the weighted blend, and passes the local AI-writing detector at **score ≤ 2**.

## When to use

Use for the **language** axis: word-level voice: rhythm, register, turns, humor, concrete language, hedging, sign-offs, detector gate.

Trigger examples: humanize / de-AI / punch up / detector gate / sounds like Gen or AIC.

Do **not** use for thumbnails, title-only SEO, or analytics (those are pro-yt skills).

## Workflow

1. **Intake.** Read the envelope (title, topic, source, lean, protected constraints). Load `references/pipeline.md`.
2. **Stage work.** Voice pass → ban-list → burstiness → detect.js loop until score ≤ 2 or FAIL.
3. **Card pass.** Walk the pattern index in priority order (P0 → P1 → P2). Honour **Do NOT apply when**.
4. **Grade or rewrite** using the rubric and output format below. Cite every card ID.
5. **Handoff.** Fill your section of the envelope. Return FINAL SCRIPT + GATE.
6. **Self-check.** No over-applied cards, no invented facts, score unsoftened.

## Input / output contract

### Incoming
- AUDIENCE-ENGINEERED DRAFT + full envelope
- Must load `references/detector-gate.md` and the local avoid-ai-writing / humanizer / anti-ai-slop skills

### Produce
- **FINAL SCRIPT** (narration only)
- `GATE: PASS|FAIL` with integer detector `score` (bar: ≤ 2), `label`, `loops`
- Change log citing L* / avoid-ai tiers

### Outgoing
- On PASS: return script + score to the user / parent
- On FAIL after 3 loops: return best draft + unresolved issues; never soft-pass
- Never claim `executed` unless `detect.js` actually ran

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

Read `references/weighted-metrics-train.md` for the numbers, `references/contrastive-pairs.md` and `references/drills.md` for worked examples. Everything here was measured or read on the 76 corpus videos only.

## 1. Pick the lean first
| lean | when | signature moves |
|---|---|---|
| **Gen (default for the user's own scripts)** | money/power explainers, outrage-with-a-fix | `So,` / `And` / `But` starters, `Look,`, `here's the thing`, `I know what you're thinking`, light swearing, self-aware jokes, "you" every other sentence |
| **AIC** | a true story with a clock (firing, incident, scenario) | dated present-tense scene narration, dry one-line asides, short declaratives, first-person "I think" verdict at the end |
| **Fisher** | geopolitics / systems with documents and maps | "I want to show you…", physical artifact, numbered threats, `Okay, with me so far?`, `which means`, scale analogies |
| **Maxinomics** | concept essays, object as metaphor | cinematic scene open, sentence fragments and list fragments, games with the viewer, footnotes, "See you." |
| **AotP** | first-principles mechanism | toy model with small numbers (rice, gold coins), "Imagine…", ladder of definitions, paradox framing |

## 2. Hard numeric targets (weighted corpus blend, per 1k words unless marked)
Mean sentence 15–18 words (AIC 15, Maxinomics 13, Gen-new runs longer). Short sentences (≤6 words) ~20% of sentences; long (≥30) ≤11%.
Questions ~5% of sentences. Starters: `And` ~12%, `So` ~6%, `But` ~6% (Gen: 24 / 12.5 / 12). 
`just` ~4.4, `really` ~2, `actually` ~1.7, `I think` ~0.7, `you know` ~0.6, contractions ~27, "you/your" ~13, "I/me/my" ~12, numerals ~11.
**Near zero:** semicolons (0.02), em-dashes outside AIC (0), "delve/tapestry/testament/landscape/crucial/pivotal/realm/moreover/furthermore/additionally/in conclusion/navigate" (0.09 total).

## 3. Twelve core rules
1. Talk, don't write: contractions everywhere; start sentences with And/So/But; let a thought run on with "and" rather than a semicolon.
2. Concrete over abstract: a dollar figure, date, named company, or physical object every 2–3 sentences. Numbers are spoken ("$1,300 per year", "100 million users in 2 months").
3. Short punch after a long setup: "It is not a routine call." / "Didn't work." / "Fine." / "This was supposed to be impossible."
4. Dry aside inside narration (AIC): "Super not ominous name." "to use the technical term, pissed." "Quora, you know, the website with the questions, you know the one."
5. Say the turn out loud: "But here's the problem." "Here's the thing." "Or are they?" "Not exactly." "Which actually is a good question."
6. Pre-empt the viewer (Gen): "And look, I know what you're thinking… But just please stick with me here."
7. Analogy that rescales the number (Fisher): "$10 billion… It would be like if the US booked a trade deal that brought in 11 trillion dollars."
8. Hedge like a person, not a lawyer: "I don't know which is true." "This is pure speculation, but…" "You should check my work. You should assume I'm biased." Never "It is important to note".
9. Humor is self-aware and specific: "Well, except my videos, of course." "Streamies, that I've definitely never used." "This, to be clear, is not career advice."
10. Mild swearing only in Gen lean (≈1/1k): "pissed", "the hell", "f*cked" in titles. None in AIC/Fisher/AotP leans.
11. Fragments and lists (Maxinomics): "Menus, clicking buttons, steering. Tapping. Messaging. Sorting. Waiting on hold."
12. Ban list: no semicolons, no em-dash chains, no tricolon-of-abstractions ("innovation, resilience and growth"), no "In today's world", no "Let's dive in", no ending on a moral platitude without a concrete image.

## 4. Workflow A — write fresh
1) choose lean; 2) draft as you'd say it to a friend; 3) pass 2: add one concrete number/name every ~40 words; 4) pass 3: insert one short punch sentence after each long build; 5) pass 4: scan the ban list; 6) read aloud test — anything you wouldn't say on camera, cut.

## 5. Workflow B — humanize an AI draft
Run the contrastive-pairs checklist (references/contrastive-pairs.md): replace abstractions with objects, split balanced sentences, add an And/So/But starter, add the turn phrase, add one aside, remove ban-list words, end paragraphs on a fact or a short line, not a summary.

## 6. Lean quick-switch
- AIC: "Friday, November 17th, 2023. Sam Altman is in a hotel room in Las Vegas." present tense, timestamps as headers.
- Fisher: "Okay, so we are going to use this board here to map out…", "Remember, …", "And you know what? They succeeded."
- Gen: "But why should you care? Well, fast forward to today…", "So, point is,…", close "…learn how money and power works."
- AotP: "Imagine a world with no money: just people, land and time."
## 7. Deep-read additions 
New word-level moves found by full reading that the stats pass missed:
- **Deadpan understatement + named source (Boyle/AIC):** "a company whose main product is, broadly speaking, air." "Super not ominous name." Rule: state the absurd fact flatly, no exclamation.
- **Running refrain (Gen, Boyle, comedic explainers):** pick one 2–6 word tag and reuse it 3x (open, middle, close): "It's always technically or money." / "France is not Greece." / "I guess we gonna see." / "it's just a theory".
- **Planted callback phrase:** "Keep that in mind for later." / "We'll come back to that." / "This will matter later." Must be paid off with "Remember…".
- **Apologetic meta-prep before jargon (HMW):** "I'm sorry, but you're going to need to understand how X is supposed to work so you can understand how it could stop working."
- **Plain-English translation tag:** "In plain English, …", "In other words, …", "Or if you think the way these agents do, I'm stuck."
- **Self-correcting count (AIC/Fisher):** "one hack. I mean, two hacks." / "three oil shocks… actually kind of four".
- **Gen self-positioning lines:** "as a son of legal immigrants…", "someone on the cusp of gen Z and Millennial", "I dead ass still live out a suitcase"; voice tags "but in all seriousness", "I'm kidding, bad joke", "your boy can shoot".
- **Fake-redemption reversal joke:** build a sincere-sounding paragraph, then "I'm kidding. It's time to plot."
- **Anaphora indictment for the thesis paragraph (max once):** "Corporations are the ones that…" x5.
- **Aphorism close-line:** "People will put up with Scandinavian tax rates if they get Scandinavian schools." "reputation can take years to build but then seconds to ruin." One per script, final 10%.
- **Sign-off formulas by lean:** Gen "that's what I call exploring the unfamiliar"; HMW "keep on learning how money works"; Boyle "See you in the next video, bye."; Econ Explained "Thanks for watching, mate."; Species "I'm Drew… thank you so much for watching."
- Gen street-interview era (weight 1): host pushback lines in interviews ("wouldn't you say that's like most middle schoolers though", "you're not helping your case") — use only for interview formats.

## AI tells on this axis (flag on sight)

| tell | corpus rate | card |
|---|---|---|
| "delve / tapestry / testament / landscape / crucial / pivotal / realm" | ~0/1k | L32 |
| "Moreover / Furthermore / Additionally / In conclusion" as connectors | ~0/1k | L32, L02 |
| semicolons | 0.02/1k | L33 |
| abstract tricolon ("innovation, resilience and growth") | ~0 | L31 |
| "It is important to note that" / "It's worth noting" | ~0 | L36 |
| balanced "not X, but Y" every paragraph | rare, ≤1 per script | L01 |
| every paragraph ends on a summary sentence | anchors end on a fact or a punch | L01, L29 |
| no contractions in a paragraph | ~27 contractions/1k | L09 |
| zero "you" in 200 words | ~13/1k (Gen ~21) | L10 |
| "Let's dive in" / "In today's world" / "Buckle up" | 0 | L32 |

## Common failures and the fix

- **Writing, not talking.** Long nominal phrases. Fix: verb-first clauses, And/So/But starters (L02), contractions (L09).
- **Flat rhythm.** Every sentence is 15–20 words. Fix: long build, then a ≤6-word punch (L01), about one in five sentences.
- **Silent turns.** The argument pivots without telling the viewer. Fix: say the turn out loud (L16).
- **Number with no scale.** Fix: rescale it to the viewer's world (L29).
- **Lawyer hedging.** Fix: a human hedge, at most twice (L36).
- **Wrong lean's humor.** Profanity in an AIC or Fisher lean is a banned move (L13).
- **Generic sign-off.** Fix: the lean's own sign-off tag (L40–L45).

## Failure modes (language)

- **Skipped detector.** No GATE line → L46 (P0).
- **Full regen on fail.** Drops facts → L47, L49.
- **Fake typos to beat the gate.** → L48.
- **Ban-list leftovers.** crucial/landscape/moreover → L50, L32.
- **Flat burstiness.** All sentences ~13 words → L51, L01.
- **Wrong-lean swearing.** → L13.
- **Soft-passed score.** Reporting PASS at score 8 → never; bar is ≤ 2.


## Strategy selection (owned by channel-structure)

Not every story engine fits every title. Structure emits `forbidden_engines`. This skill must obey them (see T43 / packet).


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

- Always: this SKILL.md.
- Always on full_rewrite: `references/pipeline.md` + `references/detector-gate.md`.
- Before the gate: `/home/box/agent-data/workflows/avoid-ai-writing/references/patterns.md`, humanizer A–F, anti-ai-slop self-check.
- When grading/rewriting: `references/patterns.md` (L01–L52), `references/contrastive-pairs.md`.
- Metrics: `references/weighted-metrics-train.md`.
- Drills: `references/drills.md`.
- Run: `node /home/box/agent-data/workflows/ai-writing-detector/scripts/detect.js`.


## Pattern index (full cards in `references/patterns.md`)

**A. Sentence rhythm and starters**
- `L01` Long build, short punch (P0): After any sentence over 25 words that carries a surprise, a reversal, or a stake, check whether the next sente
- `L02` And/So/But sentence starters (P0): Replace Moreover/Furthermore/Additionally with And; Therefore/Thus with So; However with But. Do not push star
- `L03` Fragment lists (P1): Use when listing concrete actions or objects (not abstractions). 4-8 items, each 1-3 words, at least one surpr
- `L04` Ellipsis hesitation for unease (P2): Max 3 per scenario script, at moments where confidence cracks.
- `L05` Question then answer in one breath (P0): Convert 'It is worth considering why X' into 'Why X? Because...' Keep the question under 12 words.
- `L06` Self-correcting count (P2): Use once per script when the revision is real (an extra item exists).
- `L07` Repetition for rhythm (triple word) (P2): Once per script, on the single most important adjective or verdict.
- `L08` Mantra refrain line (P1): Introduce early, repeat 2-3 times, twist the last use.

**B. Register and person**
- `L09` Contractions everywhere (P0): Contract every auxiliary except where stress needs the full form ('It is not a routine call' keeps 'is not' fo
- `L10` Second person on every other line (P0): Turn 'consumers' and 'people' into 'you' where the claim applies to the viewer. Keep third person for named ac
- `L11` Narrator first person and stance (P0): Add one first-person stance sentence per section where the script draws a conclusion.
- `L12` Self-positioning credential line (P1): Once in the first 15% of the script, tied to the topic.
- `L13` Mild profanity in Gen lean only (P1): Use on a verdict or a self-own, never on a person or group.
- `L14` Slang and youth register (Gen) (P2): Max 2 per script, in asides, not in the factual claim.
- `L15` Address the chat / viewer by name (P2): 1-3 per script, at asides.

**C. Turns and signposts**
- `L16` Say the turn out loud (P0): Use one per act break (3-5 per script). Vary the wording; never repeat the same turn phrase twice in a row.
- `L17` Pre-empt the viewer's objection (P0): Once or twice per script at the claim most likely to provoke pushback.
- `L18` Plain-English translation tag (P1): Use right after any term the viewer might not know. The translation must be shorter than the jargon line.
- `L19` Apologetic jargon prep (P2): Before one mechanism section per script.
- `L20` Planted callback phrase (P1): Every plant must pay off. Count plants and payoffs in the audit.
- `L21` Get-back-to-it re-entry (P1): Always after a sponsor read.
- `L22` Spoiler / ending give-away (P2): Once, in the first 10%.

**D. Humor and asides**
- `L23` Dry deadpan aside (P0): 1 per 400-600 words in AIC lean. Place right after the fact it mocks.
- `L24` Self-deprecating aside (P1): Once or twice per script.
- `L25` Fake-sincere reversal joke (P2): Max once.
- `L26` Ironic understatement on a named source (P1): Once per script, on a conflict of interest the source documents.
- `L27` Pop-culture handle (P2): Once per section at most, and explained in the same sentence.
- `L28` Running gag tag (P2): Introduce in first third, re-use in middle and close.

**E. Concrete language**
- `L29` Rescale the number (P0): Any number over 1,000 or any percent that matters gets one comparison within two sentences.
- `L30` Physical object or document (P1): One per section where a claim rests on a document.
- `L31` Ban the abstract tricolon (P0): Search for 'X, Y, and Z' where all three are abstract nouns. Keep only real lists.
- `L32` Ban list: AI vocabulary (P0): Search and replace every one. Target zero.
- `L33` No semicolons, no em-dash chains (P0): Split at every semicolon. Allow at most one em-dash per 1k words, AIC lean only.
- `L34` Analogy simile with 'like' (P1): One per mechanism section. The analogy must be shorter than the thing it explains.
- `L35` Aphorism close line (P1): Exactly one per script.

**F. Hedging and honesty**
- `L36` Human hedge, not legal hedge (P0): Every uncertain claim gets one plain hedge in the narrator's voice.
- `L37` Admit bias openly (P1): Once, near the claim most affected by the bias.
- `L38` Fairness concession (P1): At least once per argumentative script.
- `L39` Allegedly / legal safe tag (P2): Only where the claim is opinion about a named party.

**G. Sign-offs and verbal tags by lean**
- `L40` Lean sign-off formulas (P1): Use only the user's own sign-off for Gen-lean scripts.
- `L41` Gen voice tags (P1): 2-4 per Gen script. Not more than one per paragraph.
- `L42` Fisher voice tags (P1): In Fisher lean, open each section with a show-you line.
- `L43` AIC voice tags (P1): In AIC lean, open with a story promise and use a time stamp at each scene.
- `L44` AotP voice tags (P1): In AotP lean, every mechanism starts with Imagine plus named characters (Alice, Bob, Eve).
- `L45` Maxinomics voice tags (P1): In Maxinomics lean, name the force in one word ('Reflexivity.') and reuse it.

**G. Detector gate and anti-AI tells (pipeline)**
- `L46` Run local detector before handoff (P0): Every full_rewrite ends with GATE PASS/FAIL and the integer score.
- `L47` Iterate on issue spans only (P0): Max 3 detector loops; cite L* / avoid-ai tiers per change.
- `L48` No fake typos to beat the detector (P0): Gen lean: ≤1 natural slip per 500 words; other leans: zero intentional slips.
- `L49` Preserve protected spans while de-AI-ing (P0): Diff every change; numbers and proper nouns must match the source packet.
- `L50` Ban list pass is mandatory (P0): Zero hits in the final narration (outside quotes).
- `L51` Burstiness check (P1): After rewrite, count; merge or split to hit the band.
- `L52` Load avoid-ai-writing patterns before gate (P0): Required once per full_rewrite session.


## Gotchas (from research + corpus)

- The publish bar is detector **score ≤ 2**, not "sounds fine to me" (L46). diagnosing-bugs lesson: build the feedback loop first.
- Do not regenerate the whole script when the gate fails — edit issue spans (L47). preservation contract.
- Do not plant typos to beat the detector (L48).
- Load avoid-ai-writing patterns + humanizer A–F before the first detect.js call (L52). agentskills validation loop: work → validate → repair → repeat (max 3).
- Soft-passing a score of 5–10 as "close enough" is cheating. Report the true score.

## Drills (`references/drills.md`)

1. Contrastive pairs — 52 generic → corpus pairs.
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
