---
name: channel-audience
description: Engineer a YouTube script for the AUDIENCE the way the user's channel blend does it (Adam 7x, Gen 4x, Oil 5x, Especially 3x, After 1x). Covers retention devices, re-hook intervals, curiosity gaps, open loops, pattern interrupts, direct "you" address, objection pre-emption, relatability, fear/outrage/hope calibration, us-vs-them, credibility signals, share/rewatch triggers, comment bait, subscribe/CTA psychology, parasocial cues, humor, density control, and stakes for "you". Use when the user asks to make a script more watchable or bingeable, fix drop-off, add hooks or re-hooks, make it hit harder emotionally, get more comments or shares, or asks why viewers leave at minute X. Pair with channel-structure (where beats go) and channel-language (word-level voice).
---

# Channel audience engineering

## Purpose
Keep a specific viewer watching, feeling, and coming back, using the devices these hosts actually use at the rates they use them. That means:
- a re-hook every ~17-33 s
- "you" in the open and close
- fear front-loaded and hope/agency back-loaded
- credibility from documents and dates, not adjectives
- one-line humor asides
- light parasocial presence ("I think", "if I had to guess")
- CTAs only at the end

The skill has 106 criteria (A001-A106) and 83 catalogued devices. All are measured on host-only text from 31 videos, weighted per video at Adam 7 / Gen 4 / Oil 5 / Especially 3 / After 1.

## When to use
- "Make this hook stronger", "viewers drop at 4:00", "add retention", "more re-hooks"
- "Make it hit emotionally", "it's too doom-y", "too dry", "make me care"
- "Get people to comment or share", "where do I ask to subscribe?"
- Any device-level pass on a structured draft, after channel-structure and before channel-language

## Measured norms (weighted median, IQR)
| device family | norm | Adam | Gen |
|---|---|---|---|
| Re-hook gap (question / But / here's / turns out) | 26 s (17-33) | 33 s | 16.5 s |
| Question gap | 51 s (33-86) | 86 s | 44 s |
| Questions per minute | 0.42-0.84 | low | high |
| "You" per 1k words | 12.4-21.5 | lower | ~2× Adam |
| "You" in the open (first 8%) per 1k | 20.6 (10-28) | 12.8 | 27.6 |
| "You" in the close per 1k | 15.4-34.9 | | |
| Host "I" per 1k | 7.5-14.5 | | |
| Hedges per 1k | 3.0-5.8 | | |
| Exact numbers per minute | 1.5 (1.3-2.4) | 1.3 | 2.0 |
| Fear words per 1k (whole) | 1.5-3.3 | | |
| Hope words in close per 1k | 2.4 (1.0-5.2) | 5.9 | 2.7 |
| Outrage words per 1k | 0.3-1.0 | | |
| Short punch sentences (share) | 9.4-15.8% | | |
| Humor/aside lexicon per 1k | 0.4-1.1 | | |
| Sources per 1k | 1.0-3.8 | | |

Gen runs about twice as dense as Adam on address and re-hooks. Adam earns retention with narrative and documents. Pick the target column by the mode chosen in channel-structure.

## Workflow
1. **Map the viewer.** Who they are and what they have at stake (wallet, job, safety, identity). Write a single-sentence "stakes for you" line. Every act must touch it at least once.
2. **Hook pass (0-8%).**
   - "You" density at Gen/Oil level (≈28/1k) for explainers, or ≈13/1k for Adam narrative.
   - One curiosity gap naming a specific unknown ("details I haven't seen reported anywhere else").
   - Scope the claim, and put fear in the open if the topic carries danger.
3. **Re-hook pass.** Walk the draft in 30-second windows. Any window without a question, "But…", "here's the thing/why", "turns out", or "it gets worse" gets one. Stay below ~1 every 10 s so it doesn't become noise.
4. **Pattern interrupts.** Every 2-3 minutes:
   - "Okay, so, [date]…", a "Wait…", a clip or quote, or a tone drop to casual
   - each one carries the next fact
5. **Objection pre-emption.** At each claim a smart viewer would push on, voice the doubt ("Now you're probably thinking…", "surely…", "To be fair…") and answer it with evidence.
6. **Credibility stack.**
   - Every big claim gets a named source, document, date, or exact number.
   - Every big number gets an everyday or physical anchor.
   - Hedge where the evidence is thin.
7. **Emotion calibration.**
   - Fear: open and middle.
   - Outrage: aimed at a named actor with a motive.
   - Hope/agency: rises in the last 10-15%.
   - Never snap from horror to "thanks for watching".
8. **Us vs them.** Name "them" (an institution or person) and "us" (you as investor, citizen, or consumer) in the same breath.
9. **Relatability and humor.**
   - One concrete shared experience per act.
   - A one-line deadpan aside after heavy facts ("I swear to God", "by the way").
   - No bit runs longer than the fact it follows.
10. **Parasocial cues.** Use a flagged opinion ("I think", "if I had to guess") and a light admission. Keep one persona the whole way through. Gen plays along ("I'm going to stop playing CEO now…"). Adam stays a measured narrator.
11. **Share, rewatch, and comment.**
    - One quotable verdict line per act ("Every single metric says that the economy is cooked.").
    - One exclusive detail.
    - At most one opinion-question comment prompt tied to the thesis.
12. **Sponsor psychology.**
    - In: personal use plus a problem bridge ("that's why I use today's sponsor").
    - Out: the stakes restated as a question.
13. **Close.**
    - "You" density rises, plus an agency line and a verdict.
    - Subscribe/CTA only at 90-100%, in 1-3 lines.
14. **Score** with the rubric. Run `training/` drills if any family scores 0.

## Core rules
1. Re-hook at least every 30 s (Gen ~15 s, Adam ~30 s).
2. Put "you" in the first 30 s and the last 60 s.
3. Curiosity gaps name a specific unknown and are paid.
4. Credibility is a document, date, name, or number, never "experts say".
5. Fear early, agency late. Outrage needs a target.
6. Humor is a one-line aside.
7. Asks (subscribe, comment) come after value, at the end, once.
8. Short punch lines take ~10-16% of sentences.
9. Voice the objection before the comments do.
10. One persona per video.

## Lessons from the exams (see `exams/exam-log.md`)
- **Hook lines are hard to tell from mid-video lines by surface features alone** (A2 was the weakest type, 0.35). Weights for "you", questions, and fear kept flipping. The reliable cue is *self-containment*: a hook line introduces, and it doesn't refer back ("Remember…", "at this point", "again"). When writing, make the hook sentences stand alone.
- **Close vs middle (A4, 0.55):** hope words alone don't mark a close. The marks are "you" plus a future or agency frame ("what this all means for you", "your choice", "the window… is narrowing").
- **Creator attribution (A3, 0.55):** Gen = high "you", more questions, more profanity, "So/And/But" openers. Adam = long sentences, low "you", dates and documents. Mechanism and Others overlap with Gen. Don't over-rely on one feature.
- **Flattening kills lines (A5, 0.90):** swapping "you" for "people", dropping the question mark, and cutting "So/But" openers is the most reliable way to make corpus lines sound dead. Do the reverse when punching up a draft.
- **Surface forms matter (A1, 1.00):** each device has a headline form (see `device-catalog.md`). Learn that first, then the variants.

## Self-check rubric (0-2 each; ship at ≥ 18/22)
1. Re-hook gap within the mode band, and no 60 s window is flat.
2. "You" in the open and close at mode density.
3. ≥1 specific curiosity gap in the hook, paid later.
4. A pattern interrupt every 2-3 min, each carrying content.
5. Top 3 objections voiced and answered.
6. Every big claim sourced, and big numbers anchored.
7. Emotion curve: fear early, outrage targeted, agency late.
8. Us-vs-them names both sides.
9. Humor and relatability: one line per act, no long bits.
10. Parasocial: flagged opinions, one consistent persona, hedges where thin.
11. Asks only at the end. Sponsor bridged in and re-hooked out.

## References
- `references/criteria.md`: 106 criteria in categories A-U, each with a definition, detector, per-group stats, weighted IQR, verbatim verified quotes, do/don't, and a checklist test.
- `references/device-catalog.md`: 83 devices with headline form, full detector, decile heat strip, heaviest user, verbatim lines, plus re-hook timelines for all 31 videos.
- `references/examples.md`: 77 verbatim labeled device lines, weight-proportional.
- `references/anti-patterns.md`: 25 failures with before/after and a corpus model line.
- `training/CURRICULUM.md`, `exams/`, `sample.md`, and `build/` (all measurement scripts).

## Hard limits
Never invent quotes, sources, or numbers; use `[NEED SOURCE]`. Calibrate fear and outrage to the evidence and don't manufacture panic. This skill does not change the adam-voice, gen-voice, or script-voice skills.

## v2 checklists

**Close vs mid (A4).** The close is where agency lives.
- [ ] The close uses hope, agency and choice words ("can", "could", "still", "together", "matter", "future").
- [ ] Mid-video text is past narration, dense with named entities, and opens on anaphors ("It", "This", "They").
- [ ] Do not end on fear. End on what the viewer can do or watch for.

**Hook vs mid (A2).**
- [ ] A hook line is self-contained: a dated start, a demonstrative ("This is a diamond…"), or the channel's open vocabulary.
- [ ] A hook line does not use "but", "however" or "instead". Contrast words are a body signature.
- [ ] Note: one line taken alone is often ambiguous. Judge hooks in a 2-3 line window.

**Mode (A3).** Adam: low "I", few numbers, in-scene narration. Gen: high "you" and "I", profanity, callbacks. Mechanism (Oil, Especially): number-dense, definite explanatory. Others: first-person essay.

**Realness (A5).** The real line keeps "you", spoken connectors (So, And, But), questions and intensifiers. A flattened line removes them.

Training material: `references/position-signatures.md`, `training/method1-contrastive-pairs.md`, `training/method3-shuffle-reorder.md`, `training/worked-examples.md` (35), `training/rule-log.md`.
