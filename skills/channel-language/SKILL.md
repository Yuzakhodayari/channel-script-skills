---
name: channel-language
description: Write or humanize YouTube script narration in the user's channel voice, a word-level blend of Adam (7x), Gen (4x), Oil (5x), the Especially set (3x) and After (1x). Use when the user asks to write, rewrite, punch up, de-AI, or humanize a script, voiceover, hook, or narration line for the channel; when text "sounds like AI"; or when they ask for Adam-lean, Gen-lean, or oil-lean wording. Not for story structure (use channel-storytelling).
---

# Channel language: blended voice and humanizer

## Purpose
Make every sentence of a channel script sound like these hosts talking: spoken rhythm, fillers at the real rate, contractions, exact numbers, plain words, and none of the machine tells. This skill works at the word and sentence level. For beats, hooks, and arcs use `channel-storytelling`, then come back here for the line-by-line pass.

## When to use
- "Write the narration / voiceover / script for ..." (after the story beats exist)
- "Humanize this", "make it sound less AI", "make it sound like the channel"
- "Make it more Adam / more Gen / more like the oil video"
- Checking a draft for AI tells before recording

Do not use it for factual research. Never invent facts or quotes to make a line sound real.

## Mode switch (set this first)
| mode | when | target table column | one-line feel |
|---|---|---|---|
| **blended** (default) | no lean named | blended (weighted) | Calm explainer with spoken glue: Adam's dated, earnest precision plus Gen's So/And/But momentum |
| **adam-lean** | "more Adam", AI-risk, long-form investigation | Adam | Earnest, dated, documentary. It/The/We openers. Few So/But openers (about 15% And+But+So). No swearing. "I think", "sort of", research-frame "As I researched this video" |
| **gen-lean** | "more Gen", tech-economy explainers, piracy/markets | Gen | Fast, argumentative, viewer-first. About half of sentences open And/But/So/Because. "Honestly", "look", "cooked", "what the hell" are allowed, rarely |
| **oil-lean** | "like the oil video", news-shock topics, geopolitics | Oil | Team "we", dry jokes after big facts ("It's a nice bit of trolling."), footage pointers ("Here's another."), And-chains (21% And openers), "Okay," resets |

Dial: say "blend 70/30 adam/gen" and interpolate the two columns linearly.

## Weighted targets (measured on host-only text; full detail in references/criteria.md)
| dimension | blended (weighted) | Adam | Gen | Especially | Oil | After |
|---|---|---|---|---|---|---|
| Mean sentence length (words) | **16.19** | 15.86 | 17.52 | 13.50 | 17.38 | 14.69 |
| Median sentence length | **14.34** | 13.80 | 16.06 | 11.00 | 15.00 | 12.96 |
| Sentence-length spread (SD) | **10.21** | 10.10 | 10.21 | 10.81 | 12.99 | 8.90 |
| Short sentences (<=6 words) % | **16.66** | 17.13 | 12.36 | 26.65 | 20.42 | 19.19 |
| Long sentences (>=30 words) % | **10.56** | 10.49 | 11.76 | 7.30 | 14.41 | 7.99 |
| Questions % | **5.82** | 4.28 | 7.31 | 5.19 | 6.31 | 6.10 |
| Exclamations % | **0.06** | 0.00 | 0.00 | 0.07 | 0.00 | 0.43 |
| Opener: So | **7.34** | 2.65 | 13.90 | 2.79 | 7.81 | 4.55 |
| Opener: And | **13.21** | 7.55 | 20.94 | 6.40 | 21.02 | 8.40 |
| Opener: But | **8.08** | 4.39 | 13.91 | 4.51 | 3.90 | 5.78 |
| Opener: Because | **2.51** | 0.44 | 6.03 | 0.72 | 0.00 | 0.37 |
| Opener: It | **6.08** | 8.45 | 3.57 | 6.60 | 7.21 | 5.82 |
| Opener: The | **5.13** | 6.48 | 3.01 | 8.71 | 2.10 | 6.13 |
| Opener: I | **2.82** | 3.73 | 1.74 | 1.96 | 3.30 | 3.81 |
| Opener: We | **2.42** | 4.00 | 0.81 | 1.84 | 1.20 | 3.55 |
| Opener: You | **1.85** | 2.69 | 0.64 | 1.74 | 0.60 | 3.59 |
| Opener: Well | **1.12** | 0.39 | 2.10 | 0.17 | 2.40 | 0.48 |
| Opener: Okay/OK | **0.85** | 0.42 | 1.24 | 0.13 | 3.00 | 0.56 |
| just | **5.78** | 5.37 | 6.48 | 3.89 | 5.70 | 6.08 |
| really | **2.17** | 1.76 | 2.65 | 1.09 | 3.11 | 2.16 |
| actually | **1.90** | 1.79 | 2.33 | 1.01 | 2.42 | 1.22 |
| basically | **0.52** | 0.77 | 0.35 | 0.12 | 0.52 | 0.63 |
| kind of | **0.63** | 0.70 | 0.53 | 0.36 | 1.21 | 0.75 |
| sort of | **0.43** | 0.95 | 0.21 | 0.00 | 0.17 | 0.08 |
| you know | **0.67** | 0.95 | 0.68 | 0.20 | 0.00 | 0.48 |
| I think | **0.71** | 1.38 | 0.46 | 0.05 | 0.00 | 0.36 |
| I mean | **0.30** | 0.20 | 0.38 | 0.06 | 0.35 | 0.46 |
| probably | **0.73** | 0.64 | 0.97 | 0.37 | 0.86 | 0.41 |
| a lot | **1.16** | 1.05 | 1.29 | 0.91 | 2.07 | 0.87 |
| which means | **0.29** | 0.00 | 0.33 | 0.05 | 3.11 | 0.01 |
| in other words | **0.03** | 0.03 | 0.00 | 0.05 | 0.00 | 0.13 |
| turns out | **0.24** | 0.28 | 0.31 | 0.06 | 0.00 | 0.16 |
| you/your | **17.25** | 11.88 | 20.76 | 20.21 | 16.25 | 19.45 |
| I/me/my | **12.99** | 7.88 | 20.02 | 7.54 | 9.51 | 10.00 |
| we/us/our | **8.90** | 11.84 | 5.34 | 8.71 | 9.51 | 12.09 |
| contractions | **29.61** | 28.67 | 33.45 | 20.61 | 26.10 | 27.74 |
| swearing | **0.51** | 0.26 | 1.04 | 0.00 | 0.00 | 0.09 |
| slang (cooked/insane/crazy/wild/huge) | **0.85** | 0.71 | 0.72 | 0.59 | 2.42 | 1.22 |
| gonna/wanna/gotta | **0.39** | 0.34 | 0.00 | 0.00 | 4.49 | 0.43 |
| numerals | **11.90** | 10.69 | 14.01 | 8.16 | 10.20 | 11.89 |
| money | **2.41** | 0.66 | 3.88 | 0.97 | 5.88 | 2.27 |
| percent | **1.64** | 0.65 | 2.45 | 1.15 | 1.56 | 2.22 |
| years | **2.53** | 2.33 | 3.46 | 1.20 | 0.17 | 2.00 |
| em/en dashes | **0.59** | 1.08 | 0.00 | 1.71 | 0.00 | 0.52 |
| semicolons | **0.02** | 0.00 | 0.00 | 0.18 | 0.00 | 0.04 |
| AI-tell vocabulary | **0.22** | 0.49 | 0.02 | 0.00 | 0.17 | 0.26 |
| essay connectors | **0.04** | 0.03 | 0.03 | 0.00 | 0.00 | 0.14 |

Units: sentence rows are % of sentences or words. Opener rows are per 100 sentences. Other rows are per 1,000 words. And+But+So openers combined: blended 28.6%, Adam 14.6%, Gen 48.8%, Oil 32.7%, Especially 13.7%, After 18.7%.

## Workflow A: writing narration
1. Set the mode. If none is given, use blended.
2. Get the beats from `channel-storytelling` or the user. Do not decide structure here.
3. Draft each beat out loud in your head. Write the way you would say it to one friend across a table.
4. Facts first: every claim gets a number, a date, a name, or a source in the same sentence ("For 16 hours on Tuesday, July 8th, ...").
5. Rhythm pass: mix 3-6-word punches with 25-35-word run-ons. Target the mode's mean and SD. Never let five sentences in a row sit within 4 words of each other.
6. Glue pass: use spoken openers at the mode's rate (And/But/So/Now/Because/Like/Well/Okay). Replace every essay connector.
7. Texture pass: fillers and hedges at the mode's rate (just, really, actually, basically, kind of, I think, I mean, probably). Hedge, then land on a plain claim.
8. Plain-word pass: contractions everywhere ("it's", "don't", "they're", "gonna" in gen/oil), plain verbs (get, use, buy, show), casual quantities ("a lot", "a bunch of").
9. Tell sweep: run the checklist in references/anti-patterns.md. Zero AI-tell vocabulary, zero essay connectors, about zero semicolons, almost no exclamation marks.
10. Read it aloud. If you would not say a sentence, rewrite it.

## Workflow B: humanizing AI text
1. Lock the facts: list every number, name, date, and claim. They must survive unchanged.
2. Delete AI framing: "In this video we will explore", "It is important to note", "In conclusion", closing morals, "testament", "landscape", "delve".
3. Map essay openers to spoken ones: Therefore/As a result -> So. However -> But. Additionally/Moreover/Furthermore -> And. For example -> Like. Currently -> Now.
4. Re-contract everything.
5. Break semicolon and ", and it is" merges back into separate sentences so short punches return.
6. Swap formal words for plain ones (utilize->use, obtain->get, significant->big or the actual number, numerous->a lot of, individuals->people, approximately->about, purchase->buy).
7. Put back one hedge or filler about every 2-3 sentences at the mode's rate. Then land each hedge on a firm claim.
8. Add one concrete physical picture or exact number per abstract claim (from the facts list; never invented).
9. Re-measure against the target table (mean length, And/But/So %, contractions/1k, fillers/1k).
10. Run the self-check rubric. Fix anything under 4.

## Core rules (exam-tested)
1. Contractions are the strongest single signal. Host text averages 30 contractions per 1k words. Expanded "it is / do not" reads as AI.
2. Spoken openers: about 29% of blended sentences start with And/But/So. Adam-lean about 15%, Gen-lean about 49%. Never Moreover/Furthermore/Additionally.
3. Burstiness: blended sentence-length SD is about 10 words around a mean of 16. About 17% of sentences are 6 words or fewer, and about 11% are 30 or more.
4. Fillers are part of the voice: "just" about 5.8/1k, "really" 2.2/1k, "actually" 1.9/1k. Zero fillers reads as essay. Three in one sentence reads as parody.
5. Exact numbers: about 12 numerals per 1k words, plus dollar amounts, years, and named days. Never "a significant amount".
6. Questions about 6% of sentences, usually answered in the next line. Exclamation marks almost never (0.06%).
7. Punctuation: commas and periods. Semicolons 0.02/1k (effectively none). Dashes are caption artefacts, not style.
8. Talk to one viewer: "you" about 17/1k, "I" about 13/1k. The narrator has opinions and says so ("I think", "honestly").
9. AI-tell vocabulary rate in the corpus: 0.22/1k (practically zero). Essay connectors: 0.04/1k.
10. Lean hygiene: no Gen tics (look, cooked, what the hell, swearing) in adam-lean. No Adam earnestness stacked in gen-lean. Oil-lean gets one dry joke after a big fact.

## Self-check rubric (score 0-5 each; ship only at 4+ on every line)
| # | check | 5 looks like |
|---|---|---|
| 1 | Contractions | Every possible contraction taken. No "it is" unless stressed |
| 2 | Openers | And/But/So share within +/-5 points of the mode target. No essay connectors |
| 3 | Rhythm | Mean within +/-2 of target, SD 8+, at least one <=6-word punch per 5 sentences |
| 4 | Fillers/hedges | Mode rate. Hedges followed by a landing |
| 5 | Specificity | Every claim has a number/date/name/source. No vague quantities |
| 6 | Plain words | No formal synonyms. No AI-tell vocabulary |
| 7 | Viewer address | "you" present at stakes beats. Narrator opinion flagged as opinion |
| 8 | Punctuation | No semicolons, no em-dash chains, no exclamation hype |
| 9 | Lean fidelity | Matches the mode column. No cross-lean tics |
| 10 | Read-aloud | Every sentence is something a person would actually say |

## Standing lessons from exams
(Added automatically every 10 exams from real misses. See exams/exam-log.md.)
- (fold 60) Real narration keeps fillers (just, actually, really, kind of, I mean). A passage with zero fillers over 60+ words is almost always the AI version. Keep about 1 per 2-3 sentences. [validated: +1.00 on 21 past type-A items]
- (fold 40) Humanizer step: break semicolon and ", and" merges back into separate sentences so short punches come back. [validated: +0.10 on 14 past type-C items]
- (fold 40) Spoken openers (And/But/So) begin about 28% of weighted sentences (Gen about 49%, Adam about 15%). A passage with none is suspicious. [validated: +1.00 on 8 past type-A items]
- (fold 30) Humanizer step: swap formal vocabulary back to plain words (utilize->use, obtain->get, significant->big, numerous->a lot of, individuals->people, approximately->about, purchase->buy). [validated: +0.62 on 10 past type-C items]
- (fold 20) Humanizer step: re-contract (it is -> it's, do not -> don't, I am -> I'm) everywhere. [validated: +0.45 on 6 past type-C items]
- (fold 20) Real lines are dense with contractions (it's, that's, don't). Expanded forms ("it is", "do not") are the single most reliable subtle AI tell. Re-contract everything except deliberate emphasis. [validated: +2.00 on 4 past type-A items]
- (fold 10) Humanizer step: map essay openers back to spoken ones. Therefore/As a result -> So, However -> But, Additionally/Moreover -> And, For example -> Like, Currently -> Now. [validated: +0.38 on 4 past type-C items]
- (fold 10) The word right after the opener decides it: "So what/now/if", "But what/here's/the", "And then/so/that's", "Because if/the". Check the following word. [validated: +2.00 on 5 past type-B items]

## References
- `references/criteria.md`: all 96 word-level dimensions with definitions, weighted and per-creator values, verified verbatim quotes, do and don't, and a test for each
- `references/examples.md`: verbatim host passages in weight proportion, labeled by creator, file, and function
- `references/anti-patterns.md`: 35 AI tells and wrong-lean failures, each with a before/after
- `training/`: the curriculum. Run it before first real use (see training/CURRICULUM.md)
- `exams/`: 100-exam set, gold references, rubric, exam-log.md, scores.csv
- `sample.md`: an original ~400-word demonstration
- Related skills (read-only inputs): `workflows/adam-voice`, `workflows/gen-voice`, `workflows/script-voice`, `workflows/humanizer`, `workflows/avoid-ai-writing`, `workflows/anti-ai-slop-writing`

## Source honesty
All quotes in this skill were checked against the source transcripts with whitespace normalized and timestamps stripped. Host-only filtering is heuristic: labeled guests, news clips, and micro-clips are dropped, but some unlabeled clip audio may remain (for example Musk quotes inside Adam's 01 file). Gen 7.txt has no punctuation, so it counts only for word rates.
