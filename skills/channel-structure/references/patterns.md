# channel-structure — Structure patterns

Named-pattern catalogue for **title→strategy selection, forbidden engines, opening, sponsor, middle, close, beat maps, defects**, distilled from a full reading of all 117 transcripts.

**How to use a card.** Each card has an ID, creators (with weight), and priority (P0 blocks publish, P1 is off-voice, P2 is polish).
- **Apply** — rule and rate/position.
- **Edit** — generic draft → corpus way.
- **Keep** — when to leave the draft alone.
- **Do NOT apply when** — hard skip conditions (wrong lean, missing evidence, over-rate).
- **Flag a gap** — when to report missing.
- **Corpus quote** — verbatim, checked by `render.py` across all 117 transcripts.

Cite card IDs in every grade and change log. Do not invent IDs. Do not apply a card more often than Apply allows. Do not apply a card when **Do NOT apply when** matches.



## A. Opening architecture (0-0.12)

### `R01` — Hook inside 15 seconds
**Creators:** all; AIC 7, Fisher 6, Gen 5  ·  **Priority:** P0

**What it is:** The first 40 words carry a stake, a contradiction, or a scene. No channel intro before it.

- **Apply:** Count words to the first stake. Over 60 = fail.
- **Edit:** “Hi everyone, welcome back to the channel. Today we're going to be talking about oil.” → “Do you remember that oil shock we warned you about a few months ago? Well, it is here.”
- **Keep:** ColdFusion's fixed 'Hi. Welcome to another episode' is a brand tag, followed at once by a number.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Do you remember that oil shock we warned you about a few months ago? Well, it is here.”

### `R02` — Thesis question stated by 0.08
**Creators:** Fisher 6, Gen 5, AIC 7  ·  **Priority:** P0

**What it is:** One explicit question the video answers, said aloud.

- **Apply:** Locate it; if absent by 10%, flag.
- **Edit:** “There are many interesting aspects of North Korea's history.” → “And the question I want to ask is, if North Korea was doomed, why did it survive?”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “And the question I want to ask is, if North Korea was doomed, why did it survive?”

### `R03` — Why-should-you-care beat
**Creators:** Gen 5/3  ·  **Priority:** P0

**What it is:** Right after the hook, a spoken 'But why should you care?' that links to the viewer.

- **Apply:** Gen lean: required within 0.1.
- **Edit:** “This issue has broad implications.” → “And oh yeah, all that happened in just one year. But why should you give a damn?”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Okay, but why should you care?”

### `R04` — Agenda roadmap
**Creators:** Boyle 2, Fisher 6, Econ Explained 1  ·  **Priority:** P1

**What it is:** 'So, today we're going to look at how... how... and how...'

- **Apply:** One sentence, 2-3 items, by 0.12.
- **Edit:** “In this video, I will discuss several topics related to this issue.” → “today we are going to talk about how they did it.”
- **Keep:** Mystery-led stories (AIC) can skip the roadmap.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Well, to find out, as always, we need to answer a few important questions.”

### `R05` — Why-I-made-this beat
**Creators:** AIC 7, Gen 5, Johnny Harris 2  ·  **Priority:** P1

**What it is:** Narrator names the trigger for the video (a TikTok, a book, a conversation).

- **Apply:** Within 0.15.
- **Edit:** “This topic has been widely discussed.” → “The reason I'm actually making this video is because I saw a viral Tik Tok”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Before we go any further, I just want to tell you why I wanted to make this video.”

### `R06` — Credibility tag for scenarios
**Creators:** Species 2, AIC 7  ·  **Priority:** P1

**What it is:** Say what research the scenario is based on.

- **Apply:** Within 0.05 in any speculative script.
- **Edit:** “This is a possible future.” → “This scenario is based on highly cited research by top”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “This scenario is based on highly cited research by top”

### `R07` — Steelman 'other videos get it wrong' position
**Creators:** Gen 5, Econ Explained 1  ·  **Priority:** P1

**What it is:** Name the common take, say what it misses.

- **Apply:** In first 15%.
- **Edit:** “There are various perspectives on this topic.” → “None of what these videos are saying is wrong, but they're missing one key element.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “both of those YouTube narratives got it wrong”


## B. Sponsor placement

### `R08` — Sponsor window 0.10-0.25
**Creators:** Gen 5, Boyle 2, Maxinomics 4.5, JH 2  ·  **Priority:** P0

**What it is:** Corpus sponsors sit at 0.1-0.25 (Boyle 0.12-0.2, JH 0.1-0.13, HMW 0.42-0.55 outlier).

- **Apply:** Place the read after the thesis question, before the first mechanism.
- **Edit:** “[sponsor at 0.02 before the hook]” → “So, just how crazy is $2 trillion in valuation? Well, before I get into that”
- **Keep:** Later sponsor (0.4-0.55) only if bridged (R10).
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “This video is brought to you by Commentaire Coffee. More on them later.”

### `R09` — Cliffhanger into sponsor
**Creators:** Boyle 2, Gen 5  ·  **Priority:** P1

**What it is:** Ask the next question, then cut to the sponsor.

- **Apply:** Last line before sponsor = open question.
- **Edit:** “Now a word from our sponsor.” → “But first, context on the trial.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “So, just how crazy is $2 trillion in valuation?”

### `R10` — Topical sponsor bridge
**Creators:** Boyle 2, Gen 5, JH 2  ·  **Priority:** P1

**What it is:** Link sponsor to the story's theme (news bias -> Ground News).

- **Apply:** One clause of link.
- **Edit:** “Speaking of which, NordVPN.” → “what's also dangerous is how today it feels like every news outlet has a side.”
- **Keep:** Self-aware clumsy bridge (Gooden) is acceptable as a joke once.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Weak bridge (car-prices) = flag.
- **Corpus quote (verified verbatim):** “what's also dangerous is how today it feels like every news outlet has a side.”

### `R11` — Re-entry line after sponsor
**Creators:** Maxinomics, Gen, Fisher, ColdFusion  ·  **Priority:** P0

**What it is:** Explicit return phrase.

- **Apply:** Always.
- **Edit:** “[story resumes without transition]” → “And now, back to the video.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “And now, back to the story.”


## C. Middle architecture (0.12-0.8)

### `R12` — Numbered phases
**Creators:** Gen 5, HMW 2, Fisher 6  ·  **Priority:** P0

**What it is:** Middle split into Phase one/two or First/Second/Third.

- **Apply:** 3-4 named parts; each opens with its number.
- **Edit:** “The industry developed over time.” → “start phase one with ads”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Which brings us to phase two”

### `R13` — Act break every 15-20%
**Creators:** AIC 7, Gen 5, Fisher 6  ·  **Priority:** P0

**What it is:** A turn (L16) at roughly 0.2, 0.4, 0.6, 0.8.

- **Apply:** Mark turns on the beat map; gaps over 25% = flat middle.
- **Edit:** “[2,000 words of steady explanation with no turn]” → “But then something changed.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “But unfortunately, the story doesn't end there.”

### `R14` — Chapter backstory jump
**Creators:** AIC 7, ColdFusion 1  ·  **Priority:** P1

**What it is:** Announce a flashback chapter, then return.

- **Apply:** Open with 'time for a little backstory' and close with 'Anyway, back to'.
- **Edit:** “Historically, the company was founded in 2015.” → “Alright, time for a little backstory.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Anyway, back to the scenario.”

### `R15` — Sidebar flagged as sidebar
**Creators:** AIC 7, JH 2, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** Mark a detour so the viewer knows it ends.

- **Apply:** Open and close each sidebar.
- **Edit:** “Feedback loops are an important concept in mathematics.” → “A quick sidebar to talk about feedback loops. Woo. Math.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “A quick sidebar to talk about feedback loops. Woo. Math.”

### `R16` — With-me-so-far checkpoint
**Creators:** Fisher 6  ·  **Priority:** P1

**What it is:** A mid-video recap question.

- **Apply:** Once per 1,500 words in mechanism-heavy pieces.
- **Edit:** “To summarize the previous section,” → “So, okay, you see why this is all much, much bigger than just a normal trade dispute. You got it?”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Pause here for a second. Do you see how this works?”

### `R17` — Stakes escalation 'first third'
**Creators:** Fisher 6  ·  **Priority:** P1

**What it is:** Reveal that everything so far was the small part.

- **Apply:** At 0.3-0.4.
- **Edit:** “There are further consequences.” → “Everything that we talked about up to this point is actually just the first third”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Everything that we talked about up to this point is actually just the first third”

### `R18` — Calibration aside
**Creators:** Species 2, AIC 7  ·  **Priority:** P1

**What it is:** Stop the story to say how much of this is justified.

- **Apply:** Once, in the middle.
- **Edit:** “The scenario continues.” → “Okay, Sable is starting to sound a little sci-fi here, so I want to talk about how much of this is justified.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Okay, Sable is starting to sound a little sci-fi here, so I want to talk about how much of this is justified.”

### `R19` — Fair counter-section
**Creators:** Gen 5, Boyle 2, ColdFusion 1  ·  **Priority:** P0

**What it is:** A section for the other side, at 0.6-0.85.

- **Apply:** Required in argumentative scripts.
- **Edit:** “[no counterargument]” → “this wouldn't be complete without the other side of the coin”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing = P0 (one-sided).
- **Corpus quote (verified verbatim):** “this wouldn't be complete without the other side of the coin”

### `R20` — Numbered explanations list
**Creators:** Boyle 2, AotP 4, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** 'There are four fairly sensible explanations. First...'

- **Apply:** Use for competing causes.
- **Edit:** “There are several reasons.” → “There are only four ways this debt will ever be resolved”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “four very specific examples”

### `R21` — Here's-where-it-comes-together
**Creators:** Maxinomics 4.5, Gen 5  ·  **Priority:** P1

**What it is:** A synthesis beat at 0.75-0.85 joining the threads.

- **Apply:** Once.
- **Edit:** “These factors combine.” → “here's where it all comes together”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “here's where it all comes together”


## D. Mid-roll and engagement placement

### `R22` — Mid-video subscribe ask
**Creators:** Maxinomics 4.5, Gen 5  ·  **Priority:** P2

**What it is:** Ask framed with a stat or joke, at 0.4-0.6.

- **Apply:** Max one.
- **Edit:** “Please like and subscribe.” → “four out of five people who watch these videos regularly are not actually subscribed”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “People keep telling me that I've got to ask people to like and subscribe.”

### `R23` — Late plug for still-watching viewers
**Creators:** JH 2, AIC 7  ·  **Priority:** P2

**What it is:** 'if you're still watching...' at 0.75-0.95.

- **Apply:** Reward loyal viewers with the plug.
- **Edit:** “Check out our book.” → “if you're still watching, you are probably somebody who wants to better understand the world”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “if you're the kind of person who made it all the way to the end of this video, we want to keep talking to you”

### `R24` — Footnotes segment
**Creators:** Maxinomics 4.5, especially-misc  ·  **Priority:** P2

**What it is:** Post-close segment for corrections and extra facts.

- **Apply:** After the main close.
- **Edit:** “Sources in description.” → “here are the footnotes. The part that everybody keeps asking for”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Time for everybody's favorite part. Footnote time.”


## E. Closing architecture (0.85-1.0)

### `R25` — Verdict line
**Creators:** AIC 7, Fisher 6, Gen 5  ·  **Priority:** P0

**What it is:** First-person answer to the thesis question.

- **Apply:** In final 10%.
- **Edit:** “There are many viewpoints.” → “North Korea really has won.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “North Korea really has won.”

### `R26` — Lever / what you can do
**Creators:** AIC 7, Gen 5, other 1  ·  **Priority:** P0

**What it is:** Concrete action for the viewer after the verdict.

- **Apply:** Required in advocacy pieces.
- **Edit:** “Stay informed.” → “You really do have more leverage”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “data centers are on the ballot in November”

### `R27` — Next-video CTA
**Creators:** Species, Gen, Boyle, other  ·  **Priority:** P1

**What it is:** Point to one specific next video.

- **Apply:** Last 20 seconds.
- **Edit:** “Check out my other videos.” → “Click here to learn the rest of the story.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Click here to learn the rest of the story.”

### `R28` — Sign-off last
**Creators:** all  ·  **Priority:** P1

**What it is:** Fixed sign-off is the final line (L40).

- **Apply:** Nothing after except footnotes.
- **Edit:** “Bye guys, peace, see ya.” → “See you in the next video, bye.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “See you in the next video, bye.”


## F. Beat maps by format (positions are fractions of runtime)

### `R29` — Mystery-story beat map (AIC)
**Creators:** AIC 7  ·  **Priority:** P0

**What it is:** Cold open scene 0-0.05; why-I-made-this 0.05; backstory 0.1-0.3; incident clock 0.3-0.7; aftermath 0.7-0.85; verdict + lever 0.85-1.

- **Apply:** Check each beat position ±0.07.
- **Edit:** “[backstory first, incident at 0.8]” → “I want to tell you the full story.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “I wanna tell you the extraordinary story of the past few months.”

### `R30` — Map explainer beat map (Fisher)
**Creators:** Fisher 6  ·  **Priority:** P0

**What it is:** Hook claim 0-0.04; map/board 0.04-0.1; thesis q 0.08; 3-4 threads 0.1-0.75; stakes escalation 0.35; consequence 0.75-0.9; open question/verdict.

- **Apply:** As R29.
- **Edit:** “[no map until 0.5]” → “This all makes more sense if we look at it on a map.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “This all makes more sense if we look at it on a map.”

### `R31` — Money-power exposé beat map (Gen)
**Creators:** Gen 5  ·  **Priority:** P0

**What it is:** Contradiction hook 0-0.03; why care 0.05; promise 0.07; sponsor 0.12-0.2; phases 0.2-0.75; personal angle 0.5; counter 0.75; fix + sign-off.

- **Apply:** As R29.
- **Edit:** “[fix never given]” → “By the end, you'll see why waiting for prices to drop won't save you, but I will show you what actually will.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “by the end, you'll see the choice”

### `R32` — Concept essay beat map (Maxinomics)
**Creators:** Maxinomics 4.5  ·  **Priority:** P0

**What it is:** Dated scene 0-0.06; name the force 0.08; history 0.1-0.4; present 0.4-0.7; synthesis 0.75; choice close; footnotes.

- **Apply:** As R29.
- **Edit:** “[force never named]” → “This is our force at work. Reflexivity.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “But fear not, there is a choice to be made and it is your choice.”

### `R33` — First-principles beat map (AotP)
**Creators:** AotP 4  ·  **Priority:** P0

**What it is:** Origin story 0-0.1; puzzle 0.1; toy model 0.15-0.5; breakthrough 0.5-0.7; generalize 0.7-0.9; open question.

- **Apply:** As R29.
- **Edit:** “[jargon before toy model]” → “This story starts over 2600 years ago with two magic rocks.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “This is the breakthrough.”

### `R34` — Scenario beat map (Species)
**Creators:** Species 2  ·  **Priority:** P1

**What it is:** Future hook 0-0.02; origin 0.02-0.08; POV character 0.1-0.3; escalation rungs to 0.85; calibration ~0.55; collapse; truth disclaimer + CTA.

- **Apply:** As R29.
- **Edit:** “[no calibration beat]” → “It all started six months ago, with a tweet.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “This was a story, but every experiment I mentioned in this video is real.”

### `R35` — Finance-satire beat map (Boyle/HMW)
**Creators:** Boyle 2, HMW 2  ·  **Priority:** P1

**What it is:** Irony hook; disclaimer of stance 0.08; method 0.1-0.2; sponsor 0.2; numbered dissection; fair bull case 0.88; callback close.

- **Apply:** As R29.
- **Edit:** “[no bull case]” → “To be fair to Anthropic, they published that themselves”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “keep on learning how money works.”

### `R36` — Street-interview beat map (old Gen)
**Creators:** Gen 1  ·  **Priority:** P2

**What it is:** Question 0; rounds escalate ('final round, take it up a notch'); host takeaway; sign-off.

- **Apply:** Only for interview formats.
- **Edit:** “[random question order]” → “for the final round let's take it up a notch”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “for the final round let's take it up a notch”


## G. Structural defects to flag

### `R37` — Duplicated paragraph
**Creators:** contrast: Gen lose-their-cars  ·  **Priority:** P0

**What it is:** A block repeated verbatim in the script.

- **Apply:** Search for repeated 15+ word spans.
- **Edit:** “[same paragraph twice]” → “[keep the first, cut the second]”
- **Keep:** Intentional refrains under 8 words.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Report the duplication.
- **Corpus quote (verified verbatim):** “So, with that, am I saying that car debt is going to cause a 2008 level recession? No.”

### `R38` — Rambling outro
**Creators:** contrast: microchip-war, ColdFusion blooper  ·  **Priority:** P1

**What it is:** Close loses its line in loose talk.

- **Apply:** Last 150 words must contain verdict, lever or callback.
- **Edit:** “So yeah, anyway, there's a lot more, maybe I'll do another one, who knows.” → “Now that Albanians are saying enough, will Americans do the same?”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Report.
- **Corpus quote (verified verbatim):** “Now that Albanians are saying enough, will Americans do the same?”

### `R39` — Factual-slip flag
**Creators:** contrast: Iran '15 years'  ·  **Priority:** P0

**What it is:** A number or date that contradicts the source.

- **Apply:** Check every number against the brief.
- **Edit:** “[wrong year]” → “[corrected year from source]”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Flag; never correct from memory.
- **Corpus quote (verified verbatim):** “This is literally what happened in COVID”

### `R40` — One-sided polemic
**Creators:** contrast: Gooden greed, Palantir  ·  **Priority:** P1

**What it is:** No concession or counter.

- **Apply:** Grade with R19.
- **Edit:** “[no counter]” → “There's always two sides to every story and this is just my side.”
- **Keep:** Satire channels state they are one-sided.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Report.
- **Corpus quote (verified verbatim):** “There's always two sides to every story and this is just my side.”


## H. Strategy selection (title → engine)

### `R41` — Diagnose title before engine
**Creators:** all  ·  **Priority:** P0

**What it is:** Write claim / evidence type / stakes / clock before picking a strategy_id.

- **Apply:** Mandatory first move of every structure run. Emit all four lines.
- **Edit:** “This video is about AI.” → “Claim: how a $2T valuation can unwind. Evidence: filings + history. Stakes: wallet. Clock: no.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** You already know the engine from a habit (always Gen, always AIC).
- **Flag a gap:** Starting a beat map with no diagnosis.
- **Corpus quote (verified verbatim):** “So, just how crazy is $2 trillion in valuation?”

### `R42` — One strategy_id only
**Creators:** all  ·  **Priority:** P0

**What it is:** Pick exactly one STR-* id from strategy-selector.md.

- **Apply:** Packet must contain one strategy_id and its engine.
- **Edit:** “We'll mix a timeline with street interviews and a toy model.” → “strategy_id: STR-GEN-EXPLAINER; engine: explainer”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Title is ambiguous and you refuse to choose.
- **Flag a gap:** Two engines in one packet.
- **Corpus quote (verified verbatim):** “There are only four ways this debt will ever be resolved”

### `R43` — Forbidden engines list
**Creators:** all  ·  **Priority:** P0

**What it is:** Name ≥1 engine this title must NOT use, with a one-line why.

- **Apply:** forbidden_engines length ≥ 1.
- **Edit:** “Any structure is fine.” → “forbidden: clocked (no dated incident); street (no interview plan)”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** You list bans with no reasons.
- **Flag a gap:** Empty forbidden_engines.
- **Corpus quote (verified verbatim):** “Before we can answer this, what does "token" actually mean?”

### `R44` — Ban clocked without a clock
**Creators:** AIC 7, all  ·  **Priority:** P0

**What it is:** No real hour/day facts → never STR-AIC-CLOCKED.

- **Apply:** If evidence type ≠ timeline, ban clocked.
- **Edit:** “Day 1: the model wakes. Day 2: it emails the board. (invented)” → “Welcome to the very near future… (speculative, labelled as such)”
- **Keep:** When the video is about a real dated crisis with public timestamps.
- **Do NOT apply when:** Title is 'what is quantitative easing'.
- **Flag a gap:** Fake timestamps in a non-crisis explainer.
- **Corpus quote (verified verbatim):** “Sam Altman is in a hotel room in Las Vegas.”

### `R45` — Ban ladder on outrage titles
**Creators:** AotP 4, Gen 5  ·  **Priority:** P1

**What it is:** Cultural/wallet outrage titles need explainer or essay, not pure toy-model ladder.

- **Apply:** If stakes are outrage/agency, ban ladder-only.
- **Edit:** “Imagine three villages trading rice… (on a cartel title)” → “So, let's buy a house together. Scratch that…”
- **Keep:** When the title is literally a paradox of first principles.
- **Do NOT apply when:** Title: 'Private equity is eating your city'.
- **Flag a gap:** Ladder used as the whole spine of a PE-villain video.
- **Corpus quote (verified verbatim):** “Imagine a world with no money: just people, land and time.”

### `R46` — Ban street off the street
**Creators:** Gen 1  ·  **Priority:** P1

**What it is:** Street-interview engine only when the plan is to ask strangers one question.

- **Apply:** No interview shoot → ban street.
- **Edit:** “Montage of stock nods as if interviewed.” → “strategy_id: STR-GEN-EXPLAINER”
- **Keep:** When there is a real street shoot.
- **Do NOT apply when:** Desk explainer pretending to be street.
- **Flag a gap:** Fake interview framing.
- **Corpus quote (verified verbatim):** “for my viewers like explain to me”

### `R47` — Ban artifact without an artifact
**Creators:** Fisher 6  ·  **Priority:** P0

**What it is:** Fisher artifact engine needs a document, map, board, or object to show.

- **Apply:** No showable artifact → ban artifact; pick explainer or essay.
- **Edit:** “I want to show you something. (nothing on screen)” → “Okay, so we are going to use this board here to map out…”
- **Keep:** When a real document/map is in hand.
- **Do NOT apply when:** Title has no document angle.
- **Flag a gap:** Verbal-only 'investigation' with no exhibit.
- **Corpus quote (verified verbatim):** “I want to show you something”

### `R48` — Ban speculative on settled history
**Creators:** AIC 7  ·  **Priority:** P1

**What it is:** Settled past events use clocked or chaptered, not speculative scenario.

- **Apply:** If the event already ended, ban speculative.
- **Edit:** “Welcome to the very near future: it is 2008…” → “Friday, September 12th, 2008. Lehman…”
- **Keep:** Near-future risk titles.
- **Do NOT apply when:** Title: 'What actually happened when SVB failed'.
- **Flag a gap:** Speculative framing of finished news.
- **Corpus quote (verified verbatim):** “Welcome to the very near future”

### `R49` — Success test line
**Creators:** all  ·  **Priority:** P1

**What it is:** One sentence: what the viewer can say after watching.

- **Apply:** Required in the STRATEGY PACKET.
- **Edit:** “Viewer will understand the topic.” → “Viewer can name the villain, the mechanism, and one lever they have.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Vague 'learn a lot' success test.
- **Flag a gap:** Missing success_test.
- **Corpus quote (verified verbatim):** “They want you to think it's inevitable. It's not.”

### `R50` — BACKTRACK only on engine mismatch
**Creators:** all  ·  **Priority:** P0

**What it is:** Later skills may not silently swap engines; they BACKTRACK to structure.

- **Apply:** If audience/language finds the engine wrong, return a one-line objection.
- **Edit:** “Rewrote the clocked piece as a street interview mid-pass.” → “BACKTRACK: no timestamps exist; request STR-GEN-EXPLAINER”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Engine swapped to chase a joke.
- **Flag a gap:** Silent engine swap.
- **Corpus quote (verified verbatim):** “So back to it,”
