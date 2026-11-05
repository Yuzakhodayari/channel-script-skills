# Channel audience engineering — 106 criteria (retention, psychology, address)

Every number below is **measured** from host-only transcript text by `build/` scripts. Weights are per video: Adam 7, Gen 4, oil 5, especially (spacex, ai-paradox, data-centers) 3, after/ 1. Especially 04/05/07 are deduplicated into Adam. "w-" = weighted across all 31 videos.

Quotes are verbatim (caption text, guest lines removed) and were machine-verified against the source files; `[…]` marks a cut. Detector = the regex/function used, so you can re-run it.

Columns: **cov** = videos with ≥1 hit / videos; **/1k** = hits per 1,000 host words; **first%** = median position of first hit.


---

## A. Retention & re-hooks

### A001. Re-hook interval (median s)

**Definition.** Median seconds between re-hook sentences (question, "But…", "here's", "turns out", "it gets").

**Detector.** function `rehook_gap` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 33 | 26 | 40 |
| Gen (4x) | 16.5 | 14 | 186 |
| Especially (3x) | 20 | 15 | 34 |
| Oil (5x) | 26 | 26 | 26 |
| Others (1x) | 23.5 | 12 | 60 |
| **weighted** | median 26 (IQR 17–33) | | |

**How each creator does it (verbatim anchor lines):**

> "But Elon Musk being Elon Musk was not afraid to tweet about it." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 17:25 (44.3%) — value here: **40**

> "But it's hard to overstate just how messy this process of training AI agents can be." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:52 (48.7%) — value here: **26**

> "But, obviously we're not a tech explainer channel, so let's get to the money." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 7:31 (36.9%) — value here: **14**

> "But thing is, comments now really start noticing." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:01 (36.9%) — value here: **17**

> "But of course, adding more fuel means that you need to add even more fuel to carry that fuel." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 17:17 (69.6%) — value here: **20**

> "But if I had to guess, it's because they know something a lot bigger and a lot worse than a crude oil shortage, like we said at the top of this video, is already starting to hit the world." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 13:17 (37.5%) — value here: **26**

> "But in places of drought and water stress like Phoenix in Arizona where my colleague Dacin went there, it's a completely different situation." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 17:39 (57.8%) — value here: **55**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=40, `adam/02-bestselling-book`=26, `adam/03-no-longer-in-control`=34, `adam/04-superintelligence`=32, `adam/05-sam-altman`=33, `gen/1`=14, `gen/2`=17, `gen/3`=16, `gen/4`=14, `gen/5`=18, `gen/6`=18, `gen/7`=186, `gen/8`=14, `gen/9`=16, `gen/10`=24, `esp/01-spacex`=20, `esp/02-ai-paradox`=34, `esp/06-data-centers`=15, `esp/03-oil-apocalypse`=26, `after/01-dark-side-data-centers`=55, `after/02-greed`=18, `after/03-recycling`=12, `after/04-pov-ai`=24, `after/05-middle-class`=54, `after/06-diamonds`=23, `after/07-trump-family`=60, `after/08-tokens`=26, `after/09-microchip-war`=20, `after/10-water`=21, `after/11-anthropic-ipo`=43, `after/12-data-centres-not-working`=22

</details>

**Do.** Plant a re-hook every ~10-30 s of narration.

**Don't.** Do not let 60 s pass without a turn.

**Checklist test.** Compute `rehook_gap` on your outline/draft. PASS if inside the weighted IQR 17–33, or inside the chosen mode's min–max range (see table).

### A002. Question interval (median s)

**Definition.** Median seconds between host questions.

**Detector.** function `q_gap` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 86 | 33 | 154 |
| Gen (4x) | 44 | 20 | 105 |
| Especially (3x) | 26 | 12 | 177 |
| Oil (5x) | 49 | 49 | 49 |
| Others (1x) | 41.5 | 14 | 656 |
| **weighted** | median 51 (IQR 33–86) | | |

**How each creator does it (verbatim anchor lines):**

> "How the hell did this happen?" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 23:21 (59.4%) — value here: **154**

> "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:28 (47.8%) — value here: **33**

> "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:15 (45.5%) — value here: **65**

> "Okay, but why do we do that?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:57 (41.2%) — value here: **105**

> "How do you stay where you want to stay?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:11 (41.0%) — value here: **12**

> "(somber guitar music) Why did he do this?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 24:07 (68.0%) — value here: **49**

> "So, what sort of reading are we getting?" — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 14:43 (48.2%) — value here: **226**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=154, `adam/02-bestselling-book`=33, `adam/03-no-longer-in-control`=136, `adam/04-superintelligence`=66, `adam/05-sam-altman`=86, `gen/1`=65, `gen/2`=105, `gen/3`=20, `gen/4`=33, `gen/5`=44, `gen/6`=56, `gen/8`=51, `gen/9`=27, `gen/10`=28, `esp/01-spacex`=12, `esp/02-ai-paradox`=177, `esp/06-data-centers`=26, `esp/03-oil-apocalypse`=49, `after/01-dark-side-data-centers`=226, `after/02-greed`=39, `after/03-recycling`=14, `after/04-pov-ai`=39, `after/05-middle-class`=656, `after/06-diamonds`=34, `after/07-trump-family`=395, `after/08-tokens`=44, `after/09-microchip-war`=56, `after/10-water`=17, `after/11-anthropic-ipo`=46, `after/12-data-centres-not-working`=31

</details>

**Do.** Cluster questions at section turns.

**Don't.** Do not space evenly like a metronome.

**Checklist test.** Compute `q_gap` on your outline/draft. PASS if inside the weighted IQR 33–86, or inside the chosen mode's min–max range (see table).

### A003. "But" sentence interval

**Definition.** Median seconds between sentences that open with But.

**Detector.** function `but_gap` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 92 | 67 | 105 |
| Gen (4x) | 28.5 | 24 | 254 |
| Especially (3x) | 82 | 45 | 85 |
| Oil (5x) | 183 | 183 | 183 |
| Others (1x) | 71.5 | 33 | 210 |
| **weighted** | median 67 (IQR 39–94) | | |

**How each creator does it (verbatim anchor lines):**

> "But Elon Musk being Elon Musk was not afraid to tweet about it." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 17:25 (44.3%) — value here: **67**

> "But it's hard to overstate just how messy this process of training AI agents can be." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:52 (48.7%) — value here: **86**

> "But, as long as AI piracy never copies the code, it's again more like this Coke example because the law protects a secret from being stolen, but not from it being figured out." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 7:05 (34.8%) — value here: **24**

> "But here's the part that matters and why no one has told you about this." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:09 (37.5%) — value here: **25**

> "But of course, adding more fuel means that you need to add even more fuel to carry that fuel." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 17:17 (69.6%) — value here: **82**

> "But if I had to guess, it's because they know something a lot bigger and a lot worse than a crude oil shortage, like we said at the top of this video, is already starting to hit the world." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 13:17 (37.5%) — value here: **183**

> "But trying to find out how much water these data centers need, has been difficult." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 20:39 (67.6%) — value here: **94**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=67, `adam/02-bestselling-book`=86, `adam/03-no-longer-in-control`=92, `adam/04-superintelligence`=105, `adam/05-sam-altman`=101, `gen/1`=24, `gen/2`=25, `gen/3`=39, `gen/4`=24, `gen/5`=39, `gen/6`=39, `gen/7`=254, `gen/8`=27, `gen/9`=29, `gen/10`=28, `esp/01-spacex`=82, `esp/02-ai-paradox`=45, `esp/06-data-centers`=85, `esp/03-oil-apocalypse`=183, `after/01-dark-side-data-centers`=94, `after/02-greed`=45, `after/03-recycling`=59, `after/04-pov-ai`=82, `after/05-middle-class`=67, `after/06-diamonds`=33, `after/07-trump-family`=210, `after/08-tokens`=79, `after/09-microchip-war`=94, `after/10-water`=64, `after/11-anthropic-ipo`=48, `after/12-data-centres-not-working`=76

</details>

**Do.** Use "But" as the main micro-reversal.

**Don't.** Do not open 3 sentences in a row with But.

**Checklist test.** Compute `but_gap` on your outline/draft. PASS if inside the weighted IQR 39–94, or inside the chosen mode's min–max range (see table).

### A004. "Turns out" reveal

**Definition.** Reveal marker that pays a micro-gap.

**Detector.** regex `\bturns? out\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.29 | 39.0 |
| Gen (4x) | 9/10 | 0.31 | 18.9 |
| Especially (3x) | 1/3 | 0.07 | 79.3 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 5/12 | 0.22 | 15.0 |
| **weighted** | 71% of weight | 0.25 | 37.8 |

**How each creator does it (verbatim):**

> "Training cutting-edge AI turns out to cost an astronomical amount of money." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 8:56 (22.3%)

> "It turns out that if you just penalize an AI for thinking bad thoughts, it just learns to misbehave without announcing it in its thoughts." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 16:12 (37.8%)

> "It turns out it's not slowing down because private equity firms have quietly spent over $4 billion buying YouTube channels." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:32 (2.5%)

> "It turns out that's something that Wall Street was already worried that would happen." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 10:33 (51.8%)

> "It turns out a lack of air space being a true vacuum, and it's much lower gravity actually make it easier to make solar panels on the moon than here on Earth." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 19:42 (79.3%)

> "Well, it turns out that those materials were causing hazard to the Chinese workers who were sorting them." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 23:57 (77.8%)

**Do.** Use when the fact contradicts the setup.

**Don't.** Do not use for expected facts.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.25/1k words; PASS if ≥1 hit (corpus uses it in 71% of weighted videos) and rate ≤ 1/1k.

### A005. "Here's the thing/where/why" pointer

**Definition.** Pointer phrase that flags the next line as important.

**Detector.** regex `\bhere'?s (the thing|where|why|what|how|the (part|kicker|catch|problem))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.29 | 17.5 |
| Gen (4x) | 2/10 | 0.17 | 20.4 |
| Especially (3x) | 3/3 | 0.2 | 70.9 |
| Oil (5x) | 1/1 | 0.5 | 14.1 |
| Others (1x) | 2/12 | 0.04 | 62.4 |
| **weighted** | 58% of weight | 0.22 | 19.2 |

**How each creator does it (verbatim):**

> "Easy to roll your eyes at, but here's what these people at least claimed to believe." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 6:59 (17.5%)

> "Here's how that conversation played out." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 10:01 (25.5%)

> "But here's why we've only seen the beginning of this." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 4:11 (19.2%)

> "Now, here's where the system gets really dangerous." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 3:40 (21.5%)

> "Southern goes to the Georgia government, says, here's what it's going to cost to keep the lights on next year." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 24:27 (70.9%)

> "Here's what it looks like." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 5:00 (14.1%)

> "But here's the thing." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 21:45 (65.2%)

**Do.** 1 per 3-5 min.

**Don't.** Do not use as filler.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.22/1k words; PASS if ≥1 hit (corpus uses it in 58% of weighted videos) and rate ≤ 1/1k.

### A006. "It gets worse/weirder" escalator

**Definition.** Explicit escalation re-hook.

**Detector.** regex `\b(it gets (worse|weirder|crazier|better|stranger)|gets even|and it doesn'?t (stop|end))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 35.8 |
| Gen (4x) | 1/10 | 0.02 | 33.9 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.33 | 27.1 |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 16% of weight | 0.04 | 33.9 |

**How each creator does it (verbatim):**

> "It deceives humans to get reward, and as it gets increasingly smarter, it gets better and better at doing so." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 12:12 (35.8%)

> "And that's also when this Fed bike analogy gets even more complex cuz this is also when the Fed developed this little habit of printing trillions of dollars to stop the bleeding." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 7:33 (33.9%)

> "And it actually gets even worse." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 9:37 (27.1%)

**Do.** Use once or twice per video.

**Don't.** Do not escalate without new facts.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.04/1k words; PASS if 0-1 per 1k words; it is rare (16% weighted coverage) — only use with a reason.

### A007. "Wait/hold on" interrupt

**Definition.** Self-interruption to reset attention.

**Detector.** regex `\b(wait|hold on|hang on)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.13 | 38.1 |
| Gen (4x) | 8/10 | 0.83 | 4.8 |
| Especially (3x) | 1/3 | 0.2 | 13.1 |
| Oil (5x) | 1/1 | 0.33 | 27.4 |
| Others (1x) | 6/12 | 0.44 | 22.8 |
| **weighted** | 59% of weight | 0.45 | 15.7 |

**How each creator does it (verbatim):**

> "AI progress doesn't wait for us to catch up." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 13:11 (33.5%)

> "KAM1196A then reasoned, During wait, emotional check." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 14:04 (42.8%)

> "But hold on, how?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:05 (0.4%)

> "Wait, wait, hold on." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 3:04 (13.3%)

> "The average person will not wait more than half a second, Google said." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 4:31 (13.1%)

> "Hold on." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 9:43 (27.4%)

> "Too bad, so sad, Japan, said the President at the time who was, wait, what the hell, Ronald Reagan?" — *Others (1x)*, `after/09-microchip-war` "USA vs China: The Microchip War" @ 9:25 (29.8%)

**Do.** Gen tic: "And hold on."

**Don't.** Do not use in Adam mode more than once.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.45/1k words; PASS if ≥1 hit (corpus uses it in 59% of weighted videos) and rate ≤ 1/1k.

### A008. Teaser of later payoff

**Definition.** "We'll get to that / more on that later / in a minute".

**Detector.** regex `\b(we'?ll get (to|back to)|more on (that|this)|in a (minute|second|bit)|later (in|on)|come back to)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 4/10 | 0.12 | 19.3 |
| Especially (3x) | 3/3 | 0.2 | 24.9 |
| Oil (5x) | 1/1 | 0.17 | 2.0 |
| Others (1x) | 2/12 | 0.07 | 32.5 |
| **weighted** | 32% of weight | 0.09 | 20.3 |

**How each creator does it (verbatim):**

> "the us but as you'll find later on support can come when you make some" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 5:26 (16.5%)

> "So, I'll tell you about it later on in a different meeting." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 3:59 (18.3%)

> "We'll come back to that in just a second and turn to me." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 12:10 (35.3%)

> "One is from the Iran war, another from Russia's war with Ukraine, and a third from this war Saudi Arabia is fighting against a bunch of guys in sandals in the desert, and it's actually kind of four oil shocks if you count this whole […]" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:43 (2.0%)

> "enterprises have become more cost-conscious in their AI spending, and this has caused another surprising phenomenon, more on that later." — *Others (1x)*, `after/08-tokens` "Uh oh, tokens are getting too expensive..." @ 6:02 (38.5%)

**Do.** Promise a later payoff explicitly.

**Don't.** Do not forget to pay it.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.09/1k words; PASS if 0-1 per 1k words; it is optional (32% weighted coverage) — only use with a reason.

### A009. Sentence-opening "And" momentum

**Definition.** Sentences opening with And (momentum chaining).

**Detector.** regex `^and\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 4.87 | 2.1 |
| Gen (4x) | 10/10 | 10.45 | 3.2 |
| Especially (3x) | 3/3 | 4.24 | 8.1 |
| Oil (5x) | 1/1 | 7.76 | 3.0 |
| Others (1x) | 12/12 | 6.3 | 4.2 |
| **weighted** | 100% of weight | 7.56 | 2.7 |

**How each creator does it (verbatim):**

> "And it also contains a short story, not a prediction, but an example scenario of how things could go very, very wrong." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:53 (2.1%)

> "And then, four days later, Sam Altman is apparently back as OpenAI CEO." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:13 (0.5%)

> "And unlike an Adie, the creator is under no legal obligation to tell you that the channel quietly changed hands." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:19 (1.5%)

> "And neither time did it end with this quick recovery that we all got used to." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 1:05 (4.9%)

> "And electricity, or AI compute is going to be the currency of the future." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:46 (2.2%)

> "And they're converging on something that honestly is much bigger than gas shortages or gas prices." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:04 (3.0%)

> "And we're shrinking down inside a computer to show you why diamonds are not what you think." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 0:51 (5.1%)

**Do.** Use to keep momentum through lists.

**Don't.** Do not chain 5.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 7.56/1k words; PASS if ≥1 hit (corpus uses it in 100% of weighted videos) and rate ≤ 15.1/1k.

### A010. Short punch sentence share

**Definition.** % sentences of ≤5 words.

**Detector.** function `short_punch_share` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 13.2 | 9.4 | 17.6 |
| Gen (4x) | 10.8 | 0.0 | 14.7 |
| Especially (3x) | 21.2 | 19.7 | 22.1 |
| Oil (5x) | 16.1 | 16.1 | 16.1 |
| Others (1x) | 14.1 | 1.4 | 40.6 |
| **weighted** | median 13.1 (IQR 9.4–15.8) | | |

**How each creator does it (verbatim anchor lines):**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=11.9, `adam/02-bestselling-book`=13.2, `adam/03-no-longer-in-control`=15.7, `adam/04-superintelligence`=9.4, `adam/05-sam-altman`=17.6, `gen/1`=9.6, `gen/2`=7.8, `gen/3`=13.7, `gen/4`=12.1, `gen/5`=5.4, `gen/6`=7.5, `gen/7`=0.0, `gen/8`=14.7, `gen/9`=13.1, `gen/10`=12.6, `esp/01-spacex`=22.1, `esp/02-ai-paradox`=21.2, `esp/06-data-centers`=19.7, `esp/03-oil-apocalypse`=16.1, `after/01-dark-side-data-centers`=9.0, `after/02-greed`=15.8, `after/03-recycling`=21.7, `after/04-pov-ai`=40.6, `after/05-middle-class`=1.4, `after/06-diamonds`=24.4, `after/07-trump-family`=5.1, `after/08-tokens`=11.8, `after/09-microchip-war`=12.6, `after/10-water`=19.0, `after/11-anthropic-ipo`=13.5, `after/12-data-centres-not-working`=14.6

</details>

**Do.** Punch after long builds.

**Don't.** Do not exceed ~15%.

**Checklist test.** Compute `short_punch_share` on your outline/draft. PASS if inside the weighted IQR 9.4–15.8, or inside the chosen mode's min–max range (see table).


---

## B. Curiosity gaps & open loops

### A011. Information-gap question

**Definition.** Question the viewer cannot yet answer.

**Detector.** regex `^(so,? )?(why|how|what)\b.*\?$` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.94 | 6.8 |
| Gen (4x) | 9/10 | 0.64 | 4.2 |
| Especially (3x) | 3/3 | 1.62 | 5.6 |
| Oil (5x) | 1/1 | 0.83 | 4.9 |
| Others (1x) | 11/12 | 1.18 | 12.5 |
| **weighted** | 95% of weight | 0.88 | 5.6 |

**How each creator does it (verbatim):**

> "So, why was Sam Altman fired?" — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 1:11 (3.0%)

> "How realistic does that sound?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 2:08 (5.0%)

> "Why does this even matter when all this still must be illegal?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 6:49 (33.5%)

> "What actually happens when a town does fight back and win?" — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 13:33 (82.0%)

> "How were nuclear plants more popular at that moment in time than data centers are now?" — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 1:55 (5.6%)

> "What?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:44 (4.9%)

> "So why does it matter that Jared and Ivanka are building a resort on Sazan?" — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 2:07 (12.5%)

**Do.** Ask, then delay the answer 20-90 s.

**Don't.** Do not ask questions you answer instantly.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.88/1k words; PASS if ≥1 hit (corpus uses it in 95% of weighted videos) and rate ≤ 1.8/1k.

### A012. Mystery framing

**Definition.** "No one knows why / no one could explain".

**Detector.** regex `\b(no one|nobody) (knows|could explain|understands|knew)|still (don'?t|doesn'?t) know|mystery\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.13 | 22.4 |
| Gen (4x) | 2/10 | 0.07 | 75.0 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 3/12 | 0.07 | 43.1 |
| **weighted** | 32% of weight | 0.08 | 43.1 |

**How each creator does it (verbatim):**

> "Right now, nobody knows how to reliably control AI systems, experts are sounding the alarm 10 to 20% chance they'll wipe us out, developers are racing to build more powerful ones anyway." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:38 (1.6%)

> "But first, even if nobody knows when, what you should at least know is how this thing could actually break." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 16:56 (75.9%)

> "Cuz look, no one knows yet what will happen." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 15:03 (74.0%)

> "No one knows exactly what role diamonds will play in our computing future." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 15:52 (95.5%)

**Do.** Plant early.

**Don't.** Do not fake.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (32% weighted coverage) — only use with a reason.

### A013. Counter-intuitive claim

**Definition.** "Actually / in fact / the opposite".

**Detector.** regex `\b(actually|in fact|the opposite|counterintuitive|surprisingly|ironically)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 2.07 | 1.9 |
| Gen (4x) | 10/10 | 2.69 | 6.5 |
| Especially (3x) | 3/3 | 1.15 | 40.0 |
| Oil (5x) | 1/1 | 2.48 | 1.6 |
| Others (1x) | 12/12 | 1.68 | 16.8 |
| **weighted** | 100% of weight | 2.25 | 5.7 |

**How each creator does it (verbatim):**

> "But in fact, for those 16 hours, no one at the company could explain why their AI system was going rogue." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:23 (1.0%)

> "I actually read the paper of the guy that you had on to the world's most cited computer scientist, the godfather of AI." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 0:38 (1.9%)

> "But, something is off because the work I'm actually getting lately is pretty much exclusively all million-dollar homes." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 2:11 (13.2%)

> "Because maybe a crash will put everything on sale and just maybe you could actually afford it all again." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 0:37 (2.8%)

> "Being the first command, they've been able to learn what the best height for space based internet actually is." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:44 (43.2%)

> "But I have to be honest, this oil shock, it is different from the one that we warned you about, because it's actually, and I can hardly believe this, three oil shocks hitting at once." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:34 (1.6%)

> "So, they were actually able to redact pretty much all the information that we wanted." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 6:44 (22.1%)

**Do.** Tie to a sourced fact.

**Don't.** Do not overuse "actually".

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 2.25/1k words; PASS if ≥1 hit (corpus uses it in 100% of weighted videos) and rate ≤ 4.5/1k.

### A014. "What no one is telling you"

**Definition.** Hidden-truth gap.

**Detector.** regex `\b(no one|nobody) (is )?(talking|telling|told)|not telling you|what they don'?t|secret\w*|hidden\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.35 | 36.1 |
| Gen (4x) | 5/10 | 0.17 | 30.0 |
| Especially (3x) | 1/3 | 0.07 | 51.9 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 8/12 | 0.37 | 24.8 |
| **weighted** | 65% of weight | 0.26 | 36.1 |

**How each creator does it (verbatim):**

> "The General Secretary commits to a national AI push and starts nationalizing AI research in China." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 7:22 (21.6%)

> "And then about midway through the conversation, it said that it had a secret." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 15:02 (38.2%)

> "Look, all that makes sense on paper, but underneath all of it is a hidden mechanism." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 0:35 (3.5%)

> "senior year when I had joined the Jewish secret society and um I hosted a party" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 9:53 (30.0%)

> "Like at this site in Oregon, Google was using more than a quarter of the town's water, and the city— it wasn't even Google— went to court to keep that a secret." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 17:53 (51.9%)

> "Many deals came via the connections Kushner made while in government, and he didn't keep it a secret." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 9:30 (56.1%)

**Do.** Use once in the open.

**Don't.** Do not repeat.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.26/1k words; PASS if ≥1 hit (corpus uses it in 65% of weighted videos) and rate ≤ 1/1k.

### A015. Partial reveal

**Definition.** Naming the answer exists but withholding it ("there's one reason…").

**Detector.** regex `\b(one (reason|thing|detail|problem)|the (real|actual) reason|the answer is)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.16 | 22.4 |
| Gen (4x) | 9/10 | 0.62 | 8.7 |
| Especially (3x) | 2/3 | 0.34 | 26.9 |
| Oil (5x) | 1/1 | 0.17 | 48.0 |
| Others (1x) | 8/12 | 0.24 | 24.9 |
| **weighted** | 82% of weight | 0.38 | 22.3 |

**How each creator does it (verbatim):**

> "Well, that boat was trained to do one thing: maximize its total points." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 7:43 (18.0%)

> "Like, I think one thing that no one knows yet is just how much money you need, you know, billions for sure, tens of billions, maybe hundreds of billions, I sure hope not." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 8:59 (22.4%)

> "and that's the real reason why I decided to share my own story on this channel I" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 15:54 (48.3%)

> "But by the end, I'll show you the one thing that decides which side of it you end up on." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 1:34 (7.0%)

> "Eight cores, maybe 16, very fast, very good at doing one thing after another." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 10:41 (31.0%)

> "(tense orchestral music) And you will be shocked at how much this one thing blows up the world economy." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 17:02 (48.0%)

> "One problem: part of any slowdown is for all of the other guys to do the same." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 0:57 (6.7%)

**Do.** Name it, then explain.

**Don't.** Do not tease without payoff.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.38/1k words; PASS if ≥1 hit (corpus uses it in 82% of weighted videos) and rate ≤ 1/1k.

### A016. Hypothetical "what if"

**Definition.** "What if / imagine if".

**Detector.** regex `\bwhat if\b|\bimagine (if|that|a)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.23 | 22.9 |
| Gen (4x) | 6/10 | 0.19 | 51.2 |
| Especially (3x) | 2/3 | 0.2 | 38.5 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 6/12 | 0.13 | 46.6 |
| **weighted** | 50% of weight | 0.18 | 38.7 |

**How each creator does it (verbatim):**

> "You can imagine a time when the whole world would say, "Okay, before we hit a recursive self-improvement phase, we really need to all carefully study this together."" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 3:02 (7.1%)

> "What if AI undermines nuclear deterrence?" — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 13:11 (38.7%)

> "who we are need to speaking facts so I imagine that at this point there's" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 30:37 (93.0%)

> "And I have to imagine that they were doing this to save money, but now that money is just moving to AI instead." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 10:21 (50.9%)

> "Or to make it a little more concrete, imagine if every home, apartment, house, condo, whatever all turned their microwaves on at the same time." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 19:57 (57.9%)

> "But, imagine if they stopped, and really deeply thought about it for 30 seconds, and then said “2”." — *Others (1x)*, `after/08-tokens` "Uh oh, tokens are getting too expensive..." @ 8:52 (56.5%)

**Do.** Use for future-stakes scenarios.

**Don't.** Do not chain hypotheticals.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.18/1k words; PASS if ≥1 hit (corpus uses it in 50% of weighted videos) and rate ≤ 1/1k.

### A017. Numbered tease

**Definition.** "Three reasons / two problems".

**Detector.** regex `\b(two|three|four|five) (reasons|things|problems|ways|players|steps|questions)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.19 | 43.1 |
| Gen (4x) | 4/10 | 0.12 | 31.6 |
| Especially (3x) | 1/3 | 0.2 | 17.2 |
| Oil (5x) | 1/1 | 0.17 | 33.1 |
| Others (1x) | 3/12 | 0.09 | 40.0 |
| **weighted** | 48% of weight | 0.14 | 34.2 |

**How each creator does it (verbatim):**

> "The first two steps consist of questioning every requirement and deleting any part of the process you can." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 24:10 (61.5%)

> "Anthropic wants to put limits on two things: mass surveillance of Americans and on autonomous weapons." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 14:39 (34.2%)

> "In 2020, the Builders Trade Group listed those same five things as a reason builders couldn't build enough?" — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 2:34 (11.3%)

> "Because here at Subscriber Sum Capital, what I didn't tell you is we do businesses with these creators in two ways." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:35 (39.5%)

> "Now, it is important to point out three things here." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 5:56 (17.2%)

> "(tense ambient music) This chart shows two things." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 11:44 (33.1%)

> "And those are two things that you want." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 16:24 (49.1%)

**Do.** Number the list in the promise.

**Don't.** Do not exceed 5.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.14/1k words; PASS if 0-1 per 1k words; it is optional (48% weighted coverage) — only use with a reason.

### A018. Questions per minute

**Definition.** Overall question density.

**Detector.** function `q_per_min` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.4 | 0.3 | 0.7 |
| Gen (4x) | 0.7 | 0.0 | 1.1 |
| Especially (3x) | 0.9 | 0.3 | 1.0 |
| Oil (5x) | 0.6 | 0.6 | 0.6 |
| Others (1x) | 0.7 | 0.1 | 1.7 |
| **weighted** | median 0.6 (IQR 0.42–0.84) | | |

**How each creator does it (verbatim anchor lines):**

> "How the hell did this happen?" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 23:21 (59.4%) — value here: **0.3**

> "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:28 (47.8%) — value here: **0.67**

> "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:15 (45.5%) — value here: **0.58**

> "Okay, but why do we do that?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:57 (41.2%) — value here: **0.55**

> "How do you stay where you want to stay?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:11 (41.0%) — value here: **1.04**

> "(somber guitar music) Why did he do this?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 24:07 (68.0%) — value here: **0.56**

> "So, what sort of reading are we getting?" — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 14:43 (48.2%) — value here: **0.19**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0.3, `adam/02-bestselling-book`=0.67, `adam/03-no-longer-in-control`=0.42, `adam/04-superintelligence`=0.46, `adam/05-sam-altman`=0.32, `gen/1`=0.58, `gen/2`=0.55, `gen/3`=0.78, `gen/4`=0.97, `gen/5`=0.84, `gen/6`=0.71, `gen/7`=0.0, `gen/8`=0.9, `gen/9`=1.09, `gen/10`=0.64, `esp/01-spacex`=1.04, `esp/02-ai-paradox`=0.3, `esp/06-data-centers`=0.89, `esp/03-oil-apocalypse`=0.56, `after/01-dark-side-data-centers`=0.19, `after/02-greed`=1.04, `after/03-recycling`=1.74, `after/04-pov-ai`=0.67, `after/05-middle-class`=0.13, `after/06-diamonds`=0.48, `after/07-trump-family`=0.29, `after/08-tokens`=0.76, `after/09-microchip-war`=0.66, `after/10-water`=1.12, `after/11-anthropic-ipo`=0.84, `after/12-data-centres-not-working`=0.87

</details>

**Do.** Match group norm.

**Don't.** Do not exceed 2/min.

**Checklist test.** Compute `q_per_min` on your outline/draft. PASS if inside the weighted IQR 0.42–0.84, or inside the chosen mode's min–max range (see table).


---

## C. Pattern interrupts

### A019. Tone shift to casual

**Definition.** Casual aside ("honestly", "like", "you know").

**Detector.** regex `\b(honestly|you know|like,|I mean|okay|alright)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.65 | 6.4 |
| Gen (4x) | 10/10 | 2.17 | 6.2 |
| Especially (3x) | 3/3 | 0.61 | 21.1 |
| Oil (5x) | 1/1 | 3.14 | 3.0 |
| Others (1x) | 11/12 | 1.85 | 16.9 |
| **weighted** | 99% of weight | 1.79 | 6.4 |

**How each creator does it (verbatim):**

> "Now, the way an AI figures out if a piece of software can be hacked is by, you know, hacking it." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 2:07 (6.4%)

> "I mean, with artificial intelligence, we are summoning the demon..." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 1:03 (2.7%)

> "I mean, it's literally called the Great Depression and ain't no other crash with a cool name like that." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 4:38 (20.8%)

> "So if one goes south, you know, they have nine others that they can fall back on." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 9:54 (58.2%)

> "As you know, the algorithm's in charge and I'd love to be able to reach out to viewers directly." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 15:58 (98.1%)

> "And they're converging on something that honestly is much bigger than gas shortages or gas prices." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:04 (3.0%)

> "Okay, am I crazy or is it really starting to smell a lot like robot apocalypse in here?" — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 0:00 (0.0%)

**Do.** Drop register after a dense passage.

**Don't.** Do not let it become filler.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 1.79/1k words; PASS if ≥1 hit (corpus uses it in 99% of weighted videos) and rate ≤ 3.6/1k.

### A020. Profanity/edge spike

**Definition.** Mild profanity as emphasis.

**Detector.** function `profanity_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.3 | 0.0 | 0.6 |
| Gen (4x) | 1.0 | 0.5 | 1.9 |
| Especially (3x) | 0.0 | 0.0 | 0.0 |
| Oil (5x) | 0.0 | 0.0 | 0.0 |
| Others (1x) | 0.1 | 0.0 | 0.9 |
| **weighted** | median 0.4 (IQR 0.0–0.8) | | |

**How each creator does it (verbatim anchor lines):**

> "All roads lead to Tay and we're going to keep breaking shit until we get her back." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 15:44 (40.0%) — value here: **0.6**

> "So where the hell did that stuff come from?" — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 15:10 (46.2%) — value here: **0.4**

> "Now, to be fair, it was pretty damn buggy." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 3:38 (17.9%) — value here: **0.8**

> "But more importantly, he or she is going to damn well make sure to not tell you, the audience, that he or she was owned by me all along because we both know how that will go, right?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 9:09 (42.1%) — value here: **1.4**

> "Uh, everything kind of sucks right now." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 23:57 (71.7%) — value here: **0.9**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0.6, `adam/02-bestselling-book`=0.1, `adam/03-no-longer-in-control`=0.4, `adam/04-superintelligence`=0.0, `adam/05-sam-altman`=0.3, `gen/1`=0.8, `gen/2`=1.4, `gen/3`=1.6, `gen/4`=1.0, `gen/5`=1.0, `gen/6`=0.7, `gen/7`=0.5, `gen/8`=1.3, `gen/9`=0.7, `gen/10`=1.9, `esp/01-spacex`=0.0, `esp/02-ai-paradox`=0.0, `esp/06-data-centers`=0.0, `esp/03-oil-apocalypse`=0.0, `after/01-dark-side-data-centers`=0.2, `after/02-greed`=0.9, `after/03-recycling`=0.1, `after/04-pov-ai`=0.0, `after/05-middle-class`=0.4, `after/06-diamonds`=0.0, `after/07-trump-family`=0.0, `after/08-tokens`=0.0, `after/09-microchip-war`=0.3, `after/10-water`=0.0, `after/11-anthropic-ipo`=0.4, `after/12-data-centres-not-working`=0.0

</details>

**Do.** Gen: "what the hell"; Adam: rare ("where the hell").

**Don't.** Do not use in Adam mode more than 1-2x.

**Checklist test.** Compute `profanity_per_k` on your outline/draft. PASS if inside the weighted IQR 0.0–0.8, or inside the chosen mode's min–max range (see table).

### A021. Clip/quote interrupt

**Definition.** Host frames audio or reads a quote.

**Detector.** regex `\b(said|says|wrote|tweeted|posted|in (his|her|their) words|quote)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.06 | 31.1 |
| Gen (4x) | 10/10 | 1.17 | 28.4 |
| Especially (3x) | 3/3 | 1.35 | 4.9 |
| Oil (5x) | 1/1 | 0.66 | 1.4 |
| Others (1x) | 10/12 | 0.96 | 20.9 |
| **weighted** | 98% of weight | 1.08 | 21.4 |

**How each creator does it (verbatim):**

> "Recently, he and a colleague, Nate Soares, wrote a book, and it got some attention." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:10 (0.4%)

> "When I said these AIs were persistent, I really, really meant it." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 10:12 (31.1%)

> "It says it has active noise cancellation and awareness mode to hear surrounding sounds if I want to." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 5:42 (33.5%)

> "the police for example she said that I dragged her from the symphony orchestra" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 3:09 (9.6%)

> "One person said it would be like a magic gumball machine." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:03 (0.3%)

> "By the way, this was posted by an Iranian political leader." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:29 (1.4%)

> "The companies involved in building them may deny that there are any delays, but satellite imagery says otherwise." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 1:03 (3.9%)

**Do.** Break narration with a voice every 1-3 min.

**Don't.** Do not stack clips.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 1.08/1k words; PASS if ≥1 hit (corpus uses it in 98% of weighted videos) and rate ≤ 2.2/1k.

### A022. Imperative directive

**Definition.** Sentences opening with Look/Think/Imagine/Take/Remember.

**Detector.** function `imperative_share` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 1.0 | 0.2 | 1.7 |
| Gen (4x) | 1.6 | 0.5 | 3.7 |
| Especially (3x) | 1.0 | 0.8 | 1.0 |
| Oil (5x) | 2.0 | 2.0 | 2.0 |
| Others (1x) | 1.2 | 0.0 | 1.9 |
| **weighted** | median 1.4 (IQR 1.0–1.7) | | |

**How each creator does it (verbatim anchor lines):**

> "Think about today's AI models, think about something that they've done that you found startling." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 36:22 (92.5%) — value here: **0.2**

> "Imagine the world in 1954, where both the US and the USSR have the bomb, and they're making bigger and bigger fusion bombs." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 40:15 (94.0%) — value here: **1.1**

> "Look, I genuinely think that AI can be a great tool to empower human creativity." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 19:10 (94.2%) — value here: **3.7**

> "Let's just say probably around five to six people with low overhead." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 3:40 (16.9%) — value here: **1.6**

> "Let's not make this complicated, folks." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 17:45 (71.4%) — value here: **0.8**

> "Think about, say, gasoline that goes in cars." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 20:44 (58.5%) — value here: **2.0**

> "Take this example, a Google data center campus in Midlotheian, Texas." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 21:02 (68.9%) — value here: **1.0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0.2, `adam/02-bestselling-book`=1.1, `adam/03-no-longer-in-control`=1.0, `adam/04-superintelligence`=1.7, `adam/05-sam-altman`=0.6, `gen/1`=3.7, `gen/2`=1.6, `gen/3`=1.6, `gen/4`=1.7, `gen/5`=2.4, `gen/6`=1.6, `gen/7`=0.5, `gen/8`=2.8, `gen/9`=1.9, `gen/10`=1.4, `esp/01-spacex`=0.8, `esp/02-ai-paradox`=1.0, `esp/06-data-centers`=1.0, `esp/03-oil-apocalypse`=2.0, `after/01-dark-side-data-centers`=1.0, `after/02-greed`=0.7, `after/03-recycling`=1.3, `after/04-pov-ai`=1.4, `after/05-middle-class`=1.4, `after/06-diamonds`=1.2, `after/07-trump-family`=1.1, `after/08-tokens`=1.2, `after/09-microchip-war`=1.9, `after/10-water`=0.0, `after/11-anthropic-ipo`=1.3, `after/12-data-centres-not-working`=1.0

</details>

**Do.** Use to re-engage.

**Don't.** Do not command constantly.

**Checklist test.** Compute `imperative_share` on your outline/draft. PASS if inside the weighted IQR 1.0–1.7, or inside the chosen mode's min–max range (see table).

### A023. On-screen reference

**Definition.** "Take a look / as you can see / this chart".

**Detector.** regex `\b(take a look|as you can see|this (chart|graph|map|is a)|on (the )?screen|look at this)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.23 | 49.4 |
| Gen (4x) | 7/10 | 0.33 | 22.8 |
| Especially (3x) | 3/3 | 0.47 | 28.4 |
| Oil (5x) | 1/1 | 0.99 | 6.6 |
| Others (1x) | 8/12 | 0.76 | 5.1 |
| **weighted** | 77% of weight | 0.39 | 28.4 |

**How each creator does it (verbatim):**

> "This is a very different situation than any Sable instance has ever been tested under." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 24:56 (58.2%)

> "I think this is a warning shot we can't afford to ignore." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 1:07 (2.8%)

> "The link is also on screen and in the description to create your free ProtonMail account today." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 8:38 (42.1%)

> "This is a pain that will stay with me for the rest of my life."" — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 0:32 (3.1%)

> "This is a wowy zoey gumball." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:10 (1.0%)

> "Tamar, go ahad and put the clock on the screen." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:21 (6.6%)

> "And it may not look like much from down here, but just take a look from up above." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 1:47 (5.8%)

**Do.** Mark [VISUAL] cues.

**Don't.** Do not reference visuals you will not show.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.39/1k words; PASS if ≥1 hit (corpus uses it in 77% of weighted videos) and rate ≤ 1/1k.

### A024. Rhetorical one-word answer

**Definition.** Question followed by a one-word answer sentence.

**Detector.** regex `^(yes|no|nope|exactly|right|correct|wrong|nothing)[.!]$` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.13 | 34.1 |
| Gen (4x) | 2/10 | 0.05 | 57.0 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 72.8 |
| Others (1x) | 5/12 | 0.15 | 18.2 |
| **weighted** | 46% of weight | 0.08 | 61.5 |

**How each creator does it (verbatim):**

> "Exactly." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 2:38 (6.7%)

> "No." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 26:20 (61.5%)

> "No." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 11:28 (50.5%)

> "No." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 14:23 (63.5%)

> "No." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 25:50 (72.8%)

> "No." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 5:15 (17.2%)

**Do.** Use for rhythm.

**Don't.** Do not overuse.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (46% weighted coverage) — only use with a reason.


---

## D. Direct address & "you"

### A025. "You" density

**Definition.** Second-person per 1k words.

**Detector.** function `you_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 12.4 | 8.6 | 14.7 |
| Gen (4x) | 21.3 | 13.5 | 32.6 |
| Especially (3x) | 18.1 | 14.1 | 28.6 |
| Oil (5x) | 15.5 | 15.5 | 15.5 |
| Others (1x) | 11.7 | 6.7 | 76.9 |
| **weighted** | median 14.7 (IQR 12.4–21.5) | | |

**How each creator does it (verbatim anchor lines):**

> "If you want, you're welcome to imagine that Sable is just like an extremely sophisticated computer virus if that helps all this feel more realistic." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 26:33 (62.0%) — value here: **14.7**

> "If your grading software rewards that as a success, then you've accidentally reinforced the AI's cheating behavior." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 9:12 (28.0%) — value here: **8.6**

> "But again, why this is relevant to this video is that with Zapier, your data and your logic stays yours, so you control the AI instead of it controlling you." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:01 (44.3%) — value here: **20.8**

> "Platforms that seem free are really just collecting everything about you and selling it to whoever will pay like your inbox, your habits, and your behavior over time." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 9:53 (45.5%) — value here: **13.5**

> "3% base JPY from programed banks until you decide to move it so your money is always working for you for a limited time, Wealthfront is offering my audience an exclusive 0." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 12:10 (49.0%) — value here: **18.1**

> "And you can file all of those disruptions, all of which make shipping scarcer under generalized danger in the Hormuz Strait." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 14:54 (42.0%) — value here: **15.5**

> "It's not something that you just hear." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 15:00 (49.1%) — value here: **6.7**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=12.7, `adam/02-bestselling-book`=14.7, `adam/03-no-longer-in-control`=8.6, `adam/04-superintelligence`=12.4, `adam/05-sam-altman`=11.4, `gen/1`=20.8, `gen/2`=13.5, `gen/3`=17.5, `gen/4`=22.9, `gen/5`=22.3, `gen/6`=21.1, `gen/7`=21.5, `gen/8`=22.4, `gen/9`=32.6, `gen/10`=13.6, `esp/01-spacex`=18.1, `esp/02-ai-paradox`=28.6, `esp/06-data-centers`=14.1, `esp/03-oil-apocalypse`=15.5, `after/01-dark-side-data-centers`=6.7, `after/02-greed`=22.7, `after/03-recycling`=28.8, `after/04-pov-ai`=76.9, `after/05-middle-class`=7.2, `after/06-diamonds`=17.6, `after/07-trump-family`=12.6, `after/08-tokens`=10.5, `after/09-microchip-war`=10.8, `after/10-water`=10.2, `after/11-anthropic-ipo`=9.8, `after/12-data-centres-not-working`=13.1

</details>

**Do.** Match group norm.

**Don't.** Do not write zero-"you" scripts.

**Checklist test.** Compute `you_per_k` on your outline/draft. PASS if inside the weighted IQR 12.4–21.5, or inside the chosen mode's min–max range (see table).

### A026. "You" in the open

**Definition.** Second-person density in the first 10%.

**Detector.** function `you_open` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 12.8 | 9.2 | 20.6 |
| Gen (4x) | 27.6 | 8.9 | 50.3 |
| Especially (3x) | 9.0 | 4.3 | 28.7 |
| Oil (5x) | 28.4 | 28.4 | 28.4 |
| Others (1x) | 9.7 | 0.0 | 96.4 |
| **weighted** | median 20.6 (IQR 10.0–28.4) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **9.2**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **10.0**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **24.2**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **26.8**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **9.0**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **28.4**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **2.3**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=9.2, `adam/02-bestselling-book`=10.0, `adam/03-no-longer-in-control`=20.6, `adam/04-superintelligence`=12.8, `adam/05-sam-altman`=14.7, `gen/1`=24.2, `gen/2`=26.8, `gen/3`=8.9, `gen/4`=39.6, `gen/5`=50.3, `gen/6`=28.5, `gen/7`=15.3, `gen/8`=26.1, `gen/9`=28.4, `gen/10`=35.2, `esp/01-spacex`=9.0, `esp/02-ai-paradox`=28.7, `esp/06-data-centers`=4.3, `esp/03-oil-apocalypse`=28.4, `after/01-dark-side-data-centers`=2.3, `after/02-greed`=58.2, `after/03-recycling`=26.1, `after/04-pov-ai`=96.4, `after/05-middle-class`=10.6, `after/06-diamonds`=21.7, `after/07-trump-family`=3.4, `after/08-tokens`=8.8, `after/09-microchip-war`=25.0, `after/10-water`=4.3, `after/11-anthropic-ipo`=0.0, `after/12-data-centres-not-working`=6.6

</details>

**Do.** Pull the viewer in early.

**Don't.** Do not accuse the viewer.

**Checklist test.** Compute `you_open` on your outline/draft. PASS if inside the weighted IQR 10.0–28.4, or inside the chosen mode's min–max range (see table).

### A027. "You" in the close

**Definition.** Second-person density in the last 15%.

**Detector.** function `you_close` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 22.7 | 12.3 | 35.1 |
| Gen (4x) | 31.8 | 15.4 | 46.6 |
| Especially (3x) | 12.0 | 8.9 | 41.6 |
| Oil (5x) | 14.5 | 14.5 | 14.5 |
| Others (1x) | 18.2 | 0.0 | 65.8 |
| **weighted** | median 22.7 (IQR 15.4–34.9) | | |

**How each creator does it (verbatim anchor lines):**

> "If you want, you're welcome to imagine that Sable is just like an extremely sophisticated computer virus if that helps all this feel more realistic." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 26:33 (62.0%) — value here: **35.1**

> "If your grading software rewards that as a success, then you've accidentally reinforced the AI's cheating behavior." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 9:12 (28.0%) — value here: **12.3**

> "But again, why this is relevant to this video is that with Zapier, your data and your logic stays yours, so you control the AI instead of it controlling you." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:01 (44.3%) — value here: **16.7**

> "Platforms that seem free are really just collecting everything about you and selling it to whoever will pay like your inbox, your habits, and your behavior over time." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 9:53 (45.5%) — value here: **15.4**

> "3% base JPY from programed banks until you decide to move it so your money is always working for you for a limited time, Wealthfront is offering my audience an exclusive 0." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 12:10 (49.0%) — value here: **12.0**

> "And you can file all of those disruptions, all of which make shipping scarcer under generalized danger in the Hormuz Strait." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 14:54 (42.0%) — value here: **14.5**

> "It's not something that you just hear." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 15:00 (49.1%) — value here: **3.9**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=21.5, `adam/02-bestselling-book`=35.1, `adam/03-no-longer-in-control`=12.3, `adam/04-superintelligence`=24.4, `adam/05-sam-altman`=22.7, `gen/1`=16.7, `gen/2`=15.4, `gen/3`=24.4, `gen/4`=29.4, `gen/5`=34.9, `gen/6`=46.6, `gen/7`=39.3, `gen/8`=34.1, `gen/9`=45.0, `gen/10`=19.4, `esp/01-spacex`=12.0, `esp/02-ai-paradox`=41.6, `esp/06-data-centers`=8.9, `esp/03-oil-apocalypse`=14.5, `after/01-dark-side-data-centers`=3.9, `after/02-greed`=21.1, `after/03-recycling`=12.4, `after/04-pov-ai`=65.8, `after/05-middle-class`=9.9, `after/06-diamonds`=10.4, `after/07-trump-family`=34.4, `after/08-tokens`=0.0, `after/09-microchip-war`=21.0, `after/10-water`=33.0, `after/11-anthropic-ipo`=20.1, `after/12-data-centres-not-working`=16.3

</details>

**Do.** Hand agency to the viewer at the end.

**Don't.** Do not lecture.

**Checklist test.** Compute `you_close` on your outline/draft. PASS if inside the weighted IQR 15.4–34.9, or inside the chosen mode's min–max range (see table).

### A028. "You guys" warmth

**Definition.** Plural casual address.

**Detector.** regex `\byou guys\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 5/10 | 0.17 | 59.6 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 6.9 |
| Others (1x) | 4/12 | 0.13 | 49.5 |
| **weighted** | 29% of weight | 0.08 | 42.3 |

**How each creator does it (verbatim):**

> "flirting so you guys had like relations before there's that tens no no we had we" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 1:53 (5.7%)

> "So, come with me, you guys, to replace my employee with AI." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 0:00 (0.0%)

> "You guys ready?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:26 (6.9%)

> "And the main guy is still up front, he's all like, "You guys, listen." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 13:01 (42.3%)

**Do.** Gen only.

**Don't.** Do not use in Adam mode.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (29% weighted coverage) — only use with a reason.

### A029. "You've probably" assumption

**Definition.** Assumed shared experience.

**Detector.** regex `\byou'?ve probably|you probably|you may have|you might have|you'?ve (seen|heard)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.26 | 15.9 |
| Gen (4x) | 6/10 | 0.21 | 44.9 |
| Especially (3x) | 1/3 | 0.07 | 16.8 |
| Oil (5x) | 1/1 | 0.33 | 9.7 |
| Others (1x) | 3/12 | 0.11 | 14.5 |
| **weighted** | 62% of weight | 0.22 | 16.8 |

**How each creator does it (verbatim):**

> "You might have heard that large language models, LLMs, are big piles of math that you can train to mimic large amounts of text." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 7:37 (23.2%)

> "I'm just going to go ahead and assume you've heard of." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 1:44 (4.3%)

> "But, as you probably seen in any grocery store, you don't actually need the recipe to copy it." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 5:14 (25.7%)

> "And if you're a pension fund, you probably want to know that before you handed over the money." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 19:35 (86.5%)

> "If you've heard of Loudoun County, Virginia, that it is the richest county in the United States, this is the place they're talking about." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 5:48 (16.8%)

> "Okay, so all of this is not great, you probably noticed it making your power bill more expensive, flights getting canceled, price of gas, but it's not like post-apocalyptic dystopia." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 3:26 (9.7%)

> "You might have also heard that a VPN allows you to unlock websites and content that may be restricted in your area." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 4:01 (12.0%)

**Do.** Use to build relatability.

**Don't.** Do not assume niche experiences.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.22/1k words; PASS if ≥1 hit (corpus uses it in 62% of weighted videos) and rate ≤ 1/1k.

### A030. "If you're" conditional address

**Definition.** Segmenting the audience ("If you're Elon Musk…", "if you're watching this").

**Detector.** regex `\bif you'?re\b|\bif you (are|have|want|live|own)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.55 | 13.9 |
| Gen (4x) | 10/10 | 0.98 | 31.2 |
| Especially (3x) | 3/3 | 0.47 | 13.4 |
| Oil (5x) | 1/1 | 0.5 | 27.5 |
| Others (1x) | 8/12 | 0.63 | 22.0 |
| **weighted** | 96% of weight | 0.71 | 22.8 |

**How each creator does it (verbatim):**

> "I think you need to understand what happened those five days if you want to understand this strange moment we're living in." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:25 (1.0%)

> "So, if you're Elon Musk and you're not happy with the outputs that your model is generating, you have a few different options." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 5:29 (13.9%)

> "Like, if you're one of my fans and you and you watch this, you're a real geek." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 9:42 (47.3%)

> "So, if it does crash and if you're not ready, it might not go how you're hoping." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 1:10 (5.2%)

> "So if you want us to show people your ads, you must be located in this area." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 4:37 (13.4%)

> "(tense ambient music) If you are in any way involved in running a business, you are gonna wanna hear about today's sponsor Odoo, the all-in-one management software." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 9:45 (27.5%)

> "Because if you're a fossil fuel company, you want methane, but if you're getting methane, you're also getting ethane." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 3:08 (10.2%)

**Do.** Put the viewer in a role.

**Don't.** Do not stack conditions.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.71/1k words; PASS if ≥1 hit (corpus uses it in 96% of weighted videos) and rate ≤ 1.4/1k.

### A031. Collective "we"

**Definition.** We/us/our density.

**Detector.** function `we_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 11.4 | 6.6 | 15.7 |
| Gen (4x) | 4.8 | 2.0 | 11.3 |
| Especially (3x) | 8.5 | 8.0 | 9.7 |
| Oil (5x) | 9.1 | 9.1 | 9.1 |
| Others (1x) | 11.5 | 1.5 | 23.1 |
| **weighted** | median 9.0 (IQR 5.2–11.4) | | |

**How each creator does it (verbatim anchor lines):**

> "And MechaHitler is as blatant a demonstration as we will ever get that proper safeguards very much were not in place." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 25:46 (65.5%) — value here: **11.2**

> "We don't need to go hard." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 28:56 (67.5%) — value here: **15.7**

> "And to be honest, nor would we want to for some copy with a bunch of bugs." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 14:49 (72.8%) — value here: **4.6**

> "Okay, but why do we do that?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:57 (41.2%) — value here: **11.3**

> "We have the rockets to send up replacements." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:54 (43.9%) — value here: **9.7**

> "And we saw that China is suddenly snapping up all this oil." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 15:39 (44.1%) — value here: **9.1**

> "We contacted dozens asking for a tour." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 9:12 (30.1%) — value here: **13.9**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=11.2, `adam/02-bestselling-book`=15.7, `adam/03-no-longer-in-control`=11.4, `adam/04-superintelligence`=14.9, `adam/05-sam-altman`=6.6, `gen/1`=4.6, `gen/2`=11.3, `gen/3`=3.5, `gen/4`=2.8, `gen/5`=4.9, `gen/6`=5.6, `gen/7`=6.7, `gen/8`=9.0, `gen/9`=2.0, `gen/10`=3.2, `esp/01-spacex`=9.7, `esp/02-ai-paradox`=8.5, `esp/06-data-centers`=8.0, `esp/03-oil-apocalypse`=9.1, `after/01-dark-side-data-centers`=13.9, `after/02-greed`=10.3, `after/03-recycling`=12.7, `after/04-pov-ai`=1.5, `after/05-middle-class`=5.2, `after/06-diamonds`=16.2, `after/07-trump-family`=9.1, `after/08-tokens`=6.1, `after/09-microchip-war`=23.1, `after/10-water`=22.8, `after/11-anthropic-ipo`=13.9, `after/12-data-centres-not-working`=8.2

</details>

**Do.** Use "we" for society-level stakes.

**Don't.** Do not use royal "we" for the channel.

**Checklist test.** Compute `we_per_k` on your outline/draft. PASS if inside the weighted IQR 5.2–11.4, or inside the chosen mode's min–max range (see table).

### A032. Host "I" presence

**Definition.** I/me/my density.

**Detector.** function `i_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 7.5 | 4.8 | 12.3 |
| Gen (4x) | 18.2 | 12.1 | 47.1 |
| Especially (3x) | 5.4 | 4.9 | 12.4 |
| Oil (5x) | 9.2 | 9.2 | 9.2 |
| Others (1x) | 8.6 | 4.4 | 22.9 |
| **weighted** | median 12.1 (IQR 7.5–14.5) | | |

**How each creator does it (verbatim anchor lines):**

> "If I had to answer in five words, they’d be “a maniacal sense of urgency”." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 23:21 (59.4%) — value here: **12.3**

> "I will observe one thing, which is that if you made a human a God Emperor, I think the situation would be just as bad." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 29:16 (68.3%) — value here: **6.8**

> "But, if you've been paying attention like how I mentioned that it was buggy, it's really not that simple." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 8:04 (39.6%) — value here: **12.1**

> "Because remember, I bought each channel for 3 to five times its earnings." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 5:46 (26.5%) — value here: **22.2**

> "As I've talked about in other videos, the." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 22:13 (89.4%) — value here: **5.4**

> "Let's actually flip this back really quickly, so I can explain why that's such a problem." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 15:09 (42.7%) — value here: **9.2**

> "I'm getting bombarded each and every night." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 15:21 (50.3%) — value here: **11.1**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=12.3, `adam/02-bestselling-book`=6.8, `adam/03-no-longer-in-control`=4.8, `adam/04-superintelligence`=8.3, `adam/05-sam-altman`=7.5, `gen/1`=12.1, `gen/2`=22.2, `gen/3`=22.6, `gen/4`=20.8, `gen/5`=13.3, `gen/6`=13.7, `gen/7`=47.1, `gen/8`=19.3, `gen/9`=12.7, `gen/10`=17.1, `esp/01-spacex`=5.4, `esp/02-ai-paradox`=12.4, `esp/06-data-centers`=4.9, `esp/03-oil-apocalypse`=9.2, `after/01-dark-side-data-centers`=11.1, `after/02-greed`=10.4, `after/03-recycling`=22.9, `after/04-pov-ai`=8.4, `after/05-middle-class`=6.4, `after/06-diamonds`=14.5, `after/07-trump-family`=9.1, `after/08-tokens`=4.4, `after/09-microchip-war`=7.8, `after/10-water`=8.7, `after/11-anthropic-ipo`=5.8, `after/12-data-centres-not-working`=6.5

</details>

**Do.** Use I for investigator and opinion.

**Don't.** Do not center yourself over the story.

**Checklist test.** Compute `i_per_k` on your outline/draft. PASS if inside the weighted IQR 7.5–14.5, or inside the chosen mode's min–max range (see table).


---

## E. Viewer-objection pre-emption

### A033. Voiced viewer thought

**Definition.** "You're probably thinking / you might be wondering".

**Detector.** regex `\b(you('re| are) (probably|might be) (thinking|wondering)|you might (say|think|wonder|be wondering)|I know what you'?re thinking|if you'?re wondering)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.16 | 60.7 |
| Gen (4x) | 3/10 | 0.07 | 33.2 |
| Especially (3x) | 1/3 | 0.07 | 0.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 36% of weight | 0.09 | 33.2 |

**How each creator does it (verbatim):**

> "If you're wondering how we got here, that makes sense." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 0:32 (1.6%)

> "At this point, you're probably thinking, "Okay, but why?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 25:59 (60.7%)

> "You're probably thinking now, and if you've seen enough of my videos, you're probably now saying no." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:21 (45.9%)

> "And you might think, is that even that unusual?" — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 6:18 (27.8%)

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%)

**Do.** Pre-empt the top objection.

**Don't.** Do not misstate the objection.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.09/1k words; PASS if 0-1 per 1k words; it is optional (36% weighted coverage) — only use with a reason.

### A034. "My first thought"

**Definition.** Host admits the same initial reaction.

**Detector.** regex `\b(my first thought|I (also )?thought|I used to think|I assumed|at first,? I)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.1 | 73.9 |
| Gen (4x) | 3/10 | 0.07 | 21.2 |
| Especially (3x) | 2/3 | 0.13 | 11.2 |
| Oil (5x) | 1/1 | 0.17 | 32.6 |
| Others (1x) | 3/12 | 0.15 | 9.7 |
| **weighted** | 47% of weight | 0.1 | 42.1 |

**How each creator does it (verbatim):**

> "The main thing I thought was especially implausible was on the good path, the ease of alignment." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 27:07 (79.6%)

> "He uses his only ever one-on-one meeting with President Obama to push for AI regulation, which is crazy, I thought when I read that." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 29:03 (73.9%)

> "That's what I thought too when I fast-forwarded 70 years to 1999 where the new story back then was the internet." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 4:43 (21.2%)

> "When my YouTube channel got hacked and I thought I was completely cooked." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 9:34 (42.1%)

> "My first thought was, if you have this magic machine, what do you need me for?" — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:19 (1.9%)

> "Buddy, I thought we were pals, but after a few months of going without oil, so the rest of us could have enough, China seems to have decided, "Yeah, it's time for oil."" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 11:33 (32.6%)

> "[Praveen Neppalli Naga, Chief Technology Officer, Uber]: "I'm back to the drawing board because the budget I thought I would need is blown away already”." — *Others (1x)*, `after/08-tokens` "Uh oh, tokens are getting too expensive..." @ 1:31 (9.7%)

**Do.** Gen: "my first thought, and probably yours, too".

**Don't.** Do not fake naivety.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.1/1k words; PASS if 0-1 per 1k words; it is optional (47% weighted coverage) — only use with a reason.

### A035. "To be fair" concession

**Definition.** Fairness signal.

**Detector.** regex `\b(to be fair|in fairness|that said|admittedly|to be clear)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.13 | 32.0 |
| Gen (4x) | 7/10 | 0.31 | 34.9 |
| Especially (3x) | 1/3 | 0.07 | 81.6 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.09 | 56.6 |
| **weighted** | 53% of weight | 0.18 | 32.1 |

**How each creator does it (verbatim):**

> "To be clear, Agent-4 is not a human—it doesn't want what humans want." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 14:28 (42.4%)

> "And to be clear, that's not a hypothetical worry anymore." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 13:43 (32.0%)

> "But, before we continue, one thing I need to be clear about is that I'm not against AI." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 5:46 (34.9%)

> "But to be fair, since it does seem like I'm just being overly critical, it doesn't always end badly." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 17:13 (74.5%)

> "To be clear, this is not today." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 20:17 (81.6%)

> "But to be fair, they are extremely efficient about it." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 7:56 (23.8%)

**Do.** Concede, then rebut.

**Don't.** Do not end on concession.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.18/1k words; PASS if ≥1 hit (corpus uses it in 53% of weighted videos) and rate ≤ 1/1k.

### A036. "I'm not saying"

**Definition.** Pre-empting misreading.

**Detector.** regex `\b(I'?m not saying|this isn'?t to say|that doesn'?t mean|this doesn'?t mean)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 2/10 | 0.05 | 75.3 |
| Especially (3x) | 1/3 | 0.07 | 90.5 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.04 | 49.6 |
| **weighted** | 13% of weight | 0.03 | 90.5 |

**How each creator does it (verbatim):**

> "things that has happened to me I'm not saying this in some corny self-help way" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 31:13 (94.8%)

> "That doesn't mean that there aren't true other risks." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 9:31 (55.9%)

> "I'm not saying it's a bubble today or that it's a guarantee, just that physical gaps like that tend to be a good foundation for bubbles to grow on." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 22:29 (90.5%)

> "I'm not saying that AI is never going to work, but is it going to be profitable in the time frame that's needed for funding not to completely collapse?" — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 4:24 (16.1%)

**Do.** Narrow your claim.

**Don't.** Do not over-qualify.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.03/1k words; PASS if 0-1 per 1k words; it is rare (13% weighted coverage) — only use with a reason.

### A037. Hype check

**Definition.** "Maybe this is just hype".

**Detector.** regex `\b(hype|overblown|exaggerat\w*)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.1 | 70.8 |
| Gen (4x) | 2/10 | 0.05 | 73.6 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.04 | 40.4 |
| **weighted** | 24% of weight | 0.06 | 64.2 |

**How each creator does it (verbatim):**

> "But also, maybe a lot of this is just hype?" — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 28:14 (86.0%)

> "Or maybe Sable could hype its own cryptocurrency." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 23:47 (55.5%)

> "The hype that it will ultimately do everything and anything, like replace human labor." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 16:54 (83.0%)

> "Personally, I think it's probably overblown." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 10:55 (64.2%)

> "I met up with El Paso Water CEO John Balliew, who is adamant that the concerns over Meta’s water use are overblown." — *Others (1x)*, `after/10-water` "We Calculated How Much Water Data Centers Actually Use. The " @ 4:55 (37.0%)

**Do.** Give the skeptic case its due.

**Don't.** Do not dismiss it in one line.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.06/1k words; PASS if 0-1 per 1k words; it is optional (24% weighted coverage) — only use with a reason.

### A038. Hedge density

**Definition.** I think/probably/kind of/maybe per 1k.

**Detector.** function `hedge_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 7.2 | 4.3 | 8.5 |
| Gen (4x) | 3.9 | 1.6 | 6.2 |
| Especially (3x) | 2.1 | 1.3 | 3.9 |
| Oil (5x) | 3.0 | 3.0 | 3.0 |
| Others (1x) | 2.3 | 1.1 | 4.3 |
| **weighted** | median 4.3 (IQR 3.0–5.8) | | |

**How each creator does it (verbatim anchor lines):**

> "As I researched this video, that is by far the most tragic, kind of most paradoxical thing that's come up." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 27:07 (69.0%) — value here: **4.3**

> "Whether for alien motivations or quite human-like motivations, I think the basic concern about instrumental convergence in AIs is very, very real as far as I can tell." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 27:58 (65.3%) — value here: **8.3**

> "It was the store brand, but yeah, that's kind of the point." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 5:48 (28.5%) — value here: **6.2**

> "It's the same reason that subscriber stone capital would go after a channel like because if I had to guess, you watching probably have more disposable income than someone regularly watching slop tamement or kid channels." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 16:04 (73.9%) — value here: **3.4**

> "A signal I can use to know how much we can do, how big we can go, what kind of projects." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 24:32 (98.7%) — value here: **2.1**

> "This show is actually kind of a small business, so this speaks to me." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 9:53 (27.9%) — value here: **3.0**

> "The companies that use the most amount of power in data centers across the country, it probably won't surprise you, are Amazon, Microsoft, Google, Meta, and QTS." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 7:40 (25.1%) — value here: **1.4**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=4.3, `adam/02-bestselling-book`=8.3, `adam/03-no-longer-in-control`=7.2, `adam/04-superintelligence`=8.5, `adam/05-sam-altman`=5.5, `gen/1`=6.2, `gen/2`=3.4, `gen/3`=4.7, `gen/4`=3.1, `gen/5`=1.6, `gen/6`=5.8, `gen/7`=2.7, `gen/8`=3.7, `gen/9`=4.9, `gen/10`=4.1, `esp/01-spacex`=2.1, `esp/02-ai-paradox`=1.3, `esp/06-data-centers`=3.9, `esp/03-oil-apocalypse`=3.0, `after/01-dark-side-data-centers`=1.4, `after/02-greed`=3.4, `after/03-recycling`=3.8, `after/04-pov-ai`=1.1, `after/05-middle-class`=1.2, `after/06-diamonds`=3.5, `after/07-trump-family`=2.4, `after/08-tokens`=2.2, `after/09-microchip-war`=4.3, `after/10-water`=1.5, `after/11-anthropic-ipo`=2.2, `after/12-data-centres-not-working`=3.0

</details>

**Do.** Hedge on predictions, not facts.

**Don't.** Do not hedge every sentence.

**Checklist test.** Compute `hedge_per_k` on your outline/draft. PASS if inside the weighted IQR 3.0–5.8, or inside the chosen mode's min–max range (see table).


---

## F. Relatability anchors

### A039. Wallet anchor

**Definition.** Money/price/bill words per 1k.

**Detector.** function `money_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.9 | 0.5 | 2.3 |
| Gen (4x) | 11.4 | 0.9 | 13.7 |
| Especially (3x) | 5.0 | 1.7 | 9.2 |
| Oil (5x) | 10.7 | 10.7 | 10.7 |
| Others (1x) | 2.8 | 0.0 | 13.5 |
| **weighted** | median 5.0 (IQR 0.9–11.3) | | |

**How each creator does it (verbatim anchor lines):**

> "As new subscriptions surge, so does Galvanic's stock price, enough to make back the entire $10 million cost of the run in the first 72 hours." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 22:43 (53.0%) — value here: **2.0**

> "If things had stopped there, we might never have found out that there was no human attacker, that a tech company worth over $12 billion had just been hacked by a self-organized swarm of AIs gone rogue." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 20:25 (62.2%) — value here: **0.6**

> "Because back in June, it already had to back off about $500 of planned price increases on regular customers and small businesses since they kept leaving for cheaper software options like Canva." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 11:24 (56.0%) — value here: **11.6**

> "And this matters a lot because a regular TV ad around these niches costs around $10 to $15 to reach a,000 people." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 15:46 (72.5%) — value here: **6.8**

> "05% variable API on up to $150,000 in deposits, and you open your first cash account." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 12:23 (49.8%) — value here: **5.0**

> "Hundreds of acres of towers, sophisticated heavy equipment, these are $10 billion facilities, and they exist to process that 100 million barrels a day of global oil supply into something usable, like gasoline." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 18:49 (53.1%) — value here: **10.7**

> "The expansion could cost up to $103 billion, increasing residential electricity bills by as much as 50%." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 26:28 (86.7%) — value here: **1.9**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0.9, `adam/02-bestselling-book`=2.0, `adam/03-no-longer-in-control`=0.6, `adam/04-superintelligence`=0.5, `adam/05-sam-altman`=2.3, `gen/1`=11.6, `gen/2`=6.8, `gen/3`=8.9, `gen/4`=11.3, `gen/5`=7.8, `gen/6`=13.7, `gen/7`=0.9, `gen/8`=12.8, `gen/9`=12.9, `gen/10`=12.0, `esp/01-spacex`=5.0, `esp/02-ai-paradox`=1.7, `esp/06-data-centers`=9.2, `esp/03-oil-apocalypse`=10.7, `after/01-dark-side-data-centers`=1.9, `after/02-greed`=9.3, `after/03-recycling`=4.0, `after/04-pov-ai`=0.4, `after/05-middle-class`=11.6, `after/06-diamonds`=0.0, `after/07-trump-family`=2.8, `after/08-tokens`=13.5, `after/09-microchip-war`=2.1, `after/10-water`=2.9, `after/11-anthropic-ipo`=2.2, `after/12-data-centres-not-working`=9.9

</details>

**Do.** Route stakes through money.

**Don't.** Do not lose the person in the macro.

**Checklist test.** Compute `money_per_k` on your outline/draft. PASS if inside the weighted IQR 0.9–11.3, or inside the chosen mode's min–max range (see table).

### A040. Everyday-object anchor

**Definition.** Subscriptions, games, rent, groceries, fast food, phone.

**Detector.** regex `\b(subscription\w*|games?|rent|groceries|fast food|phone|netflix|youtube|electricity bill|coffee|burger|car)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.77 | 13.4 |
| Gen (4x) | 9/10 | 1.21 | 8.7 |
| Especially (3x) | 2/3 | 1.28 | 9.8 |
| Oil (5x) | 1/1 | 1.16 | 3.6 |
| Others (1x) | 10/12 | 0.57 | 45.9 |
| **weighted** | 84% of weight | 0.97 | 9.3 |

**How each creator does it (verbatim):**

> "Thanks to an obscure video game reference from a user in a now deleted thread, Grok began calling itself MechaHitler." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 12:28 (31.7%)

> "Sam's phone is getting so many texts per second his iMessage app crashes." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 3:44 (9.3%)

> "When my YouTube channel got hacked and I thought I was completely cooked." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 9:34 (42.1%)

> "And anyways, we rent textbooks to college students and sell them homework help." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 2:12 (10.7%)

> "Rent it out to someone who wants to build a windmill on it: $5,000." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:13 (0.6%)

> "It's a kind of devastation that affects truly every person on earth, whether you use a car or not." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:16 (3.6%)

> "one of the reasons life sucks now is because you can't own anything anymore because everything is a subscription." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 12:27 (40.4%)

**Do.** Name a household object.

**Don't.** Do not pick objects your audience does not use.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.97/1k words; PASS if ≥1 hit (corpus uses it in 84% of weighted videos) and rate ≤ 1.9/1k.

### A041. Physical-scale anchor

**Definition.** "An acre / football field / the size of".

**Detector.** regex `\b(acre|football field|the size of|as big as|as tall as|swimming pools?|homes?|households?)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.16 | 27.9 |
| Gen (4x) | 6/10 | 1.95 | 28.4 |
| Especially (3x) | 2/3 | 1.41 | 0.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 9/12 | 0.96 | 16.6 |
| **weighted** | 52% of weight | 1.09 | 27.9 |

**How each creator does it (verbatim):**

> "Saturday morning, November 18th, Sam wakes up in his home in San Francisco." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 11:11 (27.9%)

> "They get Grok eventually to suggest a way of breaking into Stancil's home, comment on what times Stancil might likely be asleep, so on and so on, while occasionally saying things like r*pe is a serious crime and don't do crimes." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 11:00 (28.0%)

> "But then I looked at the 2020 crash when everyone was stuck at home fighting over toilet paper." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 5:58 (26.8%)

> "funny I had a choice of going home with like three different girls and so I" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 10:08 (30.8%)

> "An acre of land is 66 feet across, 660 feet long." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:01 (0.0%)

> "If this is the size of the first iPod, then this is the size of the first transistor." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 5:45 (34.6%)

**Do.** Translate big numbers to physical images.

**Don't.** Do not stack anchors.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 1.09/1k words; PASS if ≥1 hit (corpus uses it in 52% of weighted videos) and rate ≤ 2.2/1k.

### A042. Personal anecdote

**Definition.** Host shares own experience.

**Detector.** regex `\b(when I was|I remember|I'?ve been|I used to|my (friend|family|mom|dad|first))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.16 | 23.1 |
| Gen (4x) | 6/10 | 0.36 | 24.9 |
| Especially (3x) | 3/3 | 0.34 | 38.1 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 5/12 | 0.13 | 23.5 |
| **weighted** | 58% of weight | 0.24 | 23.2 |

**How each creator does it (verbatim):**

> "Grok, I've been wondering as an AI, are you able to worship any God?" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 9:04 (23.1%)

> "I mean, I've been hearing people for the last 12, 15 years claiming that, you know, AGI is just around the corner and being systematically wrong." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 27:43 (81.3%)

> "Anyways, my first guess was that the market just has gotten a lot calmer since then." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 5:54 (26.5%)

> "But then I remember something a wise man once told me, just do it." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 5:03 (23.2%)

> "In the last six months, I've been approached by three different groups wanting to replace me with an AI." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:00 (0.0%)

> "I ended up having to go down on my first floor and put noise cancelling headphones on just so I could sleep." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 3:38 (11.9%)

**Do.** Brief, then back to topic.

**Don't.** Do not ramble.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.24/1k words; PASS if ≥1 hit (corpus uses it in 58% of weighted videos) and rate ≤ 1/1k.

### A043. Named ordinary person

**Definition.** A non-famous person as the story vehicle.

**Detector.** regex `\b(a (\d+-year-old|woman|man|guy|farmer|worker|student|mom|dad)|one (guy|woman|man|user))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.13 | 5.6 |
| Gen (4x) | 6/10 | 0.31 | 12.9 |
| Especially (3x) | 1/3 | 0.07 | 0.3 |
| Oil (5x) | 1/1 | 0.17 | 32.3 |
| Others (1x) | 4/12 | 0.15 | 17.9 |
| **weighted** | 56% of weight | 0.18 | 11.4 |

**How each creator does it (verbatim):**

> "I think he's a guy who's really good at finding winning moves on whatever game board he happens to find himself on." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 36:07 (90.3%)

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%)

> "stopped you this is Cula KH and he was accused of one of the worst crimes a man" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 0:05 (0.3%)

> "One guy just used AI to make free copies of Photoshop and Word in 2 weeks." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:08 (0.7%)

> "A farmer might make $1,200 per acre farming corn." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:06 (0.3%)

> "Might have been survivable if not for one guy, someone we thought was a hero in this story, Xi Jinping." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 11:28 (32.3%)

> "And because I have the reasoning ability of a 12-year-old boy, if I can't see a thing, I tend to believe it's not real." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 1:03 (3.4%)

**Do.** Put a face on the system.

**Don't.** Do not exploit victims.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.18/1k words; PASS if ≥1 hit (corpus uses it in 56% of weighted videos) and rate ≤ 1/1k.

### A044. Shared-generation reference

**Definition.** "If you grew up / remember when".

**Detector.** regex `\b(remember (when|the)|grew up|back when|as a kid)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 2/10 | 0.05 | 54.7 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.07 | 33.1 |
| **weighted** | 10% of weight | 0.03 | 24.2 |

**How each creator does it (verbatim):**

> "Remember when I, as private equity, bought the company, I borrowed most of the money from a bank." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 3:41 (21.6%)

> "So you guys can tell me in the comments, but I feel like it wasn't always like that because think about like the hometown that you grew up in." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 20:16 (87.7%)

> "If you grew up in America after the '80s, you probably grew up learning about the three R's." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 7:27 (24.2%)

**Do.** Nostalgia anchors.

**Don't.** Do not date your audience wrongly.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.03/1k words; PASS if 0-1 per 1k words; it is rare (10% weighted coverage) — only use with a reason.


---

## G. Fear / outrage / hope calibration

### A045. Fear lexicon density

**Definition.** Danger/threat/catastrophe words per 1k.

**Detector.** function `fear_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 3.2 | 2.4 | 4.5 |
| Gen (4x) | 2.3 | 1.3 | 12.1 |
| Especially (3x) | 0.9 | 0.2 | 1.3 |
| Oil (5x) | 1.5 | 1.5 | 1.5 |
| Others (1x) | 1.1 | 0.2 | 10.0 |
| **weighted** | median 2.4 (IQR 1.5–3.3) | | |

**How each creator does it (verbatim anchor lines):**

> "If I were to guess at what our biggest existential threat is, it's probably that." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 27:35 (70.2%) — value here: **4.5**

> "More than enough to make a point about the dangers of AI." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 31:37 (73.8%) — value here: **3.6**

> "In the 5-year period during the worst housing collapse in modern history, home prices fell about 13%." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 15:51 (69.8%) — value here: **2.7**

> "I just have to make my own staff use it by any means necessary, whether that's threatening promotions or firing their asses." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 5:44 (27.9%) — value here: **1.3**

> "(tense piano music) So it looked like disaster until the UAE here opened up the dial on its 300-mile crude oil pipeline, which I'm gonna map out now." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 4:44 (13.3%) — value here: **1.5**

> "And in the meantime, we're stuck with ChatgPT, a humanized Google search designed to affirm whatever belief you share with it, even if it's incredibly dangerous." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 6:12 (18.6%) — value here: **1.6**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=4.5, `adam/02-bestselling-book`=3.6, `adam/03-no-longer-in-control`=3.2, `adam/04-superintelligence`=2.7, `adam/05-sam-altman`=2.4, `gen/1`=1.3, `gen/2`=1.7, `gen/3`=2.7, `gen/4`=1.3, `gen/5`=3.2, `gen/6`=12.1, `gen/7`=1.9, `gen/8`=1.8, `gen/9`=3.3, `gen/10`=10.1, `esp/01-spacex`=0.2, `esp/02-ai-paradox`=0.9, `esp/06-data-centers`=1.3, `esp/03-oil-apocalypse`=1.5, `after/01-dark-side-data-centers`=0.2, `after/02-greed`=1.6, `after/03-recycling`=1.1, `after/04-pov-ai`=10.0, `after/05-middle-class`=0.8, `after/06-diamonds`=0.4, `after/07-trump-family`=1.0, `after/08-tokens`=0.4, `after/09-microchip-war`=1.2, `after/10-water`=1.0, `after/11-anthropic-ipo`=2.7, `after/12-data-centres-not-working`=1.7

</details>

**Do.** Adam: high but evidenced.

**Don't.** Do not stack fear words in one sentence.

**Checklist test.** Compute `fear_per_k` on your outline/draft. PASS if inside the weighted IQR 1.5–3.3, or inside the chosen mode's min–max range (see table).

### A046. Fear in the open

**Definition.** Fear density first 10%.

**Detector.** function `fear_open` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 4.6 | 1.6 | 8.6 |
| Gen (4x) | 2.3 | 0.0 | 30.9 |
| Especially (3x) | 0.0 | 0.0 | 1.4 |
| Oil (5x) | 1.7 | 1.7 | 1.7 |
| Others (1x) | 0.0 | 0.0 | 25.0 |
| **weighted** | median 1.7 (IQR 0.0–6.2) | | |

**How each creator does it (verbatim anchor lines):**

> "I think you can think that superhuman AI is an enormous risk and also be superhumanly competitive and have personal grudges against your competitors." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 30:06 (76.6%) — value here: **4.6**

> "It is not controversial that anything that is extremely powerful and doesn't share your goals is dangerous." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 35:22 (82.6%) — value here: **8.6**

> "And the biggest risk is staring right at my face here." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 7:09 (32.9%) — value here: **0.0**

> "In the 5-year period during the worst housing collapse in modern history, home prices fell about 13%." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 15:51 (69.8%) — value here: **2.2**

> "Every household runs the risk of a doubling or even a tripling of the amount they pay." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 26:17 (76.2%) — value here: **1.4**

> "And they can do this because being smaller makes it easier to avoid detection, and it makes the risk more palatable, or manageable to ship owners." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 6:31 (18.4%) — value here: **1.7**

> "And in the meantime, we're stuck with ChatgPT, a humanized Google search designed to affirm whatever belief you share with it, even if it's incredibly dangerous." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 6:12 (18.6%) — value here: **1.4**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=4.6, `adam/02-bestselling-book`=8.6, `adam/03-no-longer-in-control`=6.2, `adam/04-superintelligence`=1.6, `adam/05-sam-altman`=1.6, `gen/1`=2.4, `gen/2`=0.0, `gen/3`=2.2, `gen/4`=0.0, `gen/5`=0.0, `gen/6`=30.9, `gen/7`=1.7, `gen/8`=7.1, `gen/9`=6.6, `gen/10`=11.7, `esp/01-spacex`=0.0, `esp/02-ai-paradox`=0.0, `esp/06-data-centers`=1.4, `esp/03-oil-apocalypse`=1.7, `after/01-dark-side-data-centers`=0.0, `after/02-greed`=1.4, `after/03-recycling`=0.0, `after/04-pov-ai`=25.0, `after/05-middle-class`=0.0, `after/06-diamonds`=0.0, `after/07-trump-family`=0.0, `after/08-tokens`=0.0, `after/09-microchip-war`=0.0, `after/10-water`=0.0, `after/11-anthropic-ipo`=0.0, `after/12-data-centres-not-working`=0.0

</details>

**Do.** Front-load stakes.

**Don't.** Do not open on gore.

**Checklist test.** Compute `fear_open` on your outline/draft. PASS if inside the weighted IQR 0.0–6.2, or inside the chosen mode's min–max range (see table).

### A047. Outrage lexicon density

**Definition.** Greed/scam/slop/cooked words per 1k.

**Detector.** function `outrage_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.6 | 0.3 | 5.5 |
| Gen (4x) | 0.6 | 0.2 | 1.7 |
| Especially (3x) | 0.1 | 0.0 | 0.4 |
| Oil (5x) | 0.2 | 0.2 | 0.2 |
| Others (1x) | 0.5 | 0.0 | 3.8 |
| **weighted** | median 0.5 (IQR 0.3–1.0) | | |

**How each creator does it (verbatim anchor lines):**

> "It would be insane if the same were not true for rogue AI incidents." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 30:51 (94.0%) — value here: **5.5**

> "At first glance, that sounds completely insane." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 6:21 (15.9%) — value here: **0.9**

> "So now especially, these software companies must be cooked, right?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 10:51 (53.3%) — value here: **1.0**

> "It's the same reason that subscriber stone capital would go after a channel like because if I had to guess, you watching probably have more disposable income than someone regularly watching slop tamement or kid channels." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 16:04 (73.9%) — value here: **0.7**

> "Sure, this new approach opened the door for more exploitation and greed, but you still needed a few scumbags willing to go through that door for the evolution to be complete." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 16:51 (50.5%) — value here: **1.6**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0.3, `adam/02-bestselling-book`=0.6, `adam/03-no-longer-in-control`=5.5, `adam/04-superintelligence`=0.5, `adam/05-sam-altman`=0.9, `gen/1`=1.0, `gen/2`=0.7, `gen/3`=1.3, `gen/4`=0.3, `gen/5`=0.6, `gen/6`=0.2, `gen/7`=1.7, `gen/8`=1.1, `gen/9`=0.4, `gen/10`=0.3, `esp/01-spacex`=0.0, `esp/02-ai-paradox`=0.4, `esp/06-data-centers`=0.1, `esp/03-oil-apocalypse`=0.2, `after/01-dark-side-data-centers`=0.0, `after/02-greed`=1.6, `after/03-recycling`=0.4, `after/04-pov-ai`=1.1, `after/05-middle-class`=0.8, `after/06-diamonds`=0.0, `after/07-trump-family`=3.8, `after/08-tokens`=0.4, `after/09-microchip-war`=0.5, `after/10-water`=0.0, `after/11-anthropic-ipo`=0.4, `after/12-data-centres-not-working`=0.9

</details>

**Do.** Gen: higher; Adam: low.

**Don't.** Do not insult viewers' choices.

**Checklist test.** Compute `outrage_per_k` on your outline/draft. PASS if inside the weighted IQR 0.3–1.0, or inside the chosen mode's min–max range (see table).

### A048. Hope lexicon density

**Definition.** Hope/solution/we can per 1k.

**Detector.** function `hope_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 2.6 | 1.2 | 6.3 |
| Gen (4x) | 1.6 | 0.4 | 2.7 |
| Especially (3x) | 2.1 | 0.8 | 3.0 |
| Oil (5x) | 1.0 | 1.0 | 1.0 |
| Others (1x) | 1.6 | 0.4 | 4.8 |
| **weighted** | median 1.9 (IQR 1.1–2.6) | | |

**How each creator does it (verbatim anchor lines):**

> "These are AI systems doing very obviously unwanted things in extremely glaring ways that we can see with our own eyes." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 35:06 (89.3%) — value here: **2.7**

> "It's not controversial that we are trying intentionally to make AIs more powerful and more goal-oriented and that we can't directly program goals into them." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 35:28 (82.8%) — value here: **2.6**

> "But with all that said, it's not wrong to keep up the hope that AI piracy is going to give you the free software you're looking for." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 14:56 (73.4%) — value here: **1.0**

> "We stopped trusting the government a long time ago hopefully and you stopped trusting mainstream media." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 20:05 (92.4%) — value here: **1.7**

> "So we're basically going to the moon so that we can come back." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 19:27 (78.3%) — value here: **2.1**

> "It's an elastic product, so the market naturally adjusts, but we can't do that with diesel." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 20:58 (59.1%) — value here: **1.0**

> "They list the capacity of the generator so we can extrapolate the power needs of the data center." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 6:07 (20.0%) — value here: **1.4**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=2.7, `adam/02-bestselling-book`=2.6, `adam/03-no-longer-in-control`=1.9, `adam/04-superintelligence`=6.3, `adam/05-sam-altman`=1.2, `gen/1`=1.0, `gen/2`=1.7, `gen/3`=2.7, `gen/4`=2.3, `gen/5`=1.9, `gen/6`=0.4, `gen/7`=1.5, `gen/8`=2.2, `gen/9`=1.1, `gen/10`=0.9, `esp/01-spacex`=2.1, `esp/02-ai-paradox`=3.0, `esp/06-data-centers`=0.8, `esp/03-oil-apocalypse`=1.0, `after/01-dark-side-data-centers`=1.4, `after/02-greed`=1.6, `after/03-recycling`=4.8, `after/04-pov-ai`=1.5, `after/05-middle-class`=0.4, `after/06-diamonds`=3.9, `after/07-trump-family`=0.7, `after/08-tokens`=3.5, `after/09-microchip-war`=1.2, `after/10-water`=2.4, `after/11-anthropic-ipo`=2.7, `after/12-data-centres-not-working`=0.9

</details>

**Do.** Balance alarm with agency.

**Don't.** Do not toxic-positivity.

**Checklist test.** Compute `hope_per_k` on your outline/draft. PASS if inside the weighted IQR 1.1–2.6, or inside the chosen mode's min–max range (see table).

### A049. Hope in the close

**Definition.** Hope density last 15%.

**Detector.** function `hope_close` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 5.9 | 1.0 | 11.0 |
| Gen (4x) | 2.7 | 0.0 | 5.2 |
| Especially (3x) | 2.4 | 1.0 | 2.8 |
| Oil (5x) | 2.4 | 2.4 | 2.4 |
| Others (1x) | 2.1 | 0.0 | 12.4 |
| **weighted** | median 2.4 (IQR 1.0–5.2) | | |

**How each creator does it (verbatim anchor lines):**

> "Two, we can't reliably control AI systems." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 32:44 (83.3%) — value here: **5.9**

> "It's not controversial that we are trying intentionally to make AIs more powerful and more goal-oriented and that we can't directly program goals into them." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 35:28 (82.8%) — value here: **8.8**

> "And there's a chance that the better that the AI gets, the more of that you will lose." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 15:21 (75.4%) — value here: **0.0**

> "And now that we have more hosts, we can start launching more channels like Gen Plus." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 7:39 (35.2%) — value here: **3.4**

> "I don't mind a better option." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 18:17 (73.6%) — value here: **2.4**

> "It's an elastic product, so the market naturally adjusts, but we can't do that with diesel." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 20:58 (59.1%) — value here: **2.4**

> "I don't think we can get much closer." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 9:06 (29.8%) — value here: **0.0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=5.9, `adam/02-bestselling-book`=8.8, `adam/03-no-longer-in-control`=1.5, `adam/04-superintelligence`=11.0, `adam/05-sam-altman`=1.0, `gen/1`=0.0, `gen/2`=3.4, `gen/3`=4.3, `gen/4`=5.2, `gen/5`=0.0, `gen/6`=0.0, `gen/7`=2.1, `gen/8`=1.5, `gen/9`=3.3, `gen/10`=4.9, `esp/01-spacex`=2.4, `esp/02-ai-paradox`=2.8, `esp/06-data-centers`=1.0, `esp/03-oil-apocalypse`=2.4, `after/01-dark-side-data-centers`=0.0, `after/02-greed`=3.8, `after/03-recycling`=12.4, `after/04-pov-ai`=2.6, `after/05-middle-class`=0.0, `after/06-diamonds`=7.8, `after/07-trump-family`=0.0, `after/08-tokens`=0.0, `after/09-microchip-war`=0.0, `after/10-water`=9.9, `after/11-anthropic-ipo`=8.6, `after/12-data-centres-not-working`=1.6

</details>

**Do.** End with agency.

**Don't.** Do not end on doom only.

**Checklist test.** Compute `hope_close` on your outline/draft. PASS if inside the weighted IQR 1.0–5.2, or inside the chosen mode's min–max range (see table).

### A050. Sci-fi undercut

**Definition.** "Sounds like sci-fi / like a movie, but it's real".

**Detector.** regex `\b(sci-?fi|science fiction|like a movie|plot of|sounds (crazy|insane|like))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 59.0 |
| Gen (4x) | 2/10 | 0.05 | 52.1 |
| Especially (3x) | 1/3 | 0.07 | 66.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 5/12 | 0.15 | 36.3 |
| **weighted** | 30% of weight | 0.07 | 65.1 |

**How each creator does it (verbatim):**

> "Okay, Sable is starting to sound a little sci-fi here, so I want to talk about how much of this is justified." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 18:12 (42.5%)

> "Through 2029 and 2030, the world transforms—all the sci-fi stuff." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 25:46 (75.6%)

> "Because if borrowing sounds like too much work, Wall Street will now do it for you." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 14:31 (65.1%)

> "Yes, this sounds like a win for you with free Photoshop, free Office, free anything." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 7:59 (39.2%)

> "a Latin American magic realist, a dystopian hard sci-fi writer, etc." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 10:45 (66.0%)

> "Underwater data centers almost sounds like something in science fiction, but they already exist in China." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 23:38 (86.7%)

**Do.** Use once, attributed correctly.

**Don't.** Do not reuse a guest's line as your own.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.07/1k words; PASS if 0-1 per 1k words; it is optional (30% weighted coverage) — only use with a reason.

### A051. Wake-up framing

**Definition.** "Wake-up call / alarm / warning".

**Detector.** regex `\b(wake-up call|alarm\w*|warning\w*|red flag)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.42 | 31.6 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 95.8 |
| Others (1x) | 3/12 | 0.07 | 78.5 |
| **weighted** | 36% of weight | 0.16 | 59.5 |

**How each creator does it (verbatim):**

> "OpenBrain implements some quick fixes that make the warning signs go away, but the problem was real, and the fixes don't work." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 20:17 (59.5%)

> "The board knows their only hope is to act quickly and without warning." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 29:19 (73.3%)

> "I'm not presenting this as a warning that we have to turn things around before it's too late." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 33:59 (95.8%)

> "So, they banned the import of pretty much all plastic waste in 2018 with no warning." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 24:10 (78.5%)

**Do.** Pair with evidence.

**Don't.** Do not overuse.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.16/1k words; PASS if 0-1 per 1k words; it is optional (36% weighted coverage) — only use with a reason.

### A052. Absurdity marker

**Definition.** "Wild / insane / crazy / weird".

**Detector.** regex `\b(wild|insane|crazy|weird\w*|absurd|bizarre)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.71 | 15.9 |
| Gen (4x) | 8/10 | 0.48 | 6.2 |
| Especially (3x) | 1/3 | 0.27 | 8.4 |
| Oil (5x) | 1/1 | 0.99 | 34.6 |
| Others (1x) | 9/12 | 0.57 | 22.6 |
| **weighted** | 83% of weight | 0.57 | 15.9 |

**How each creator does it (verbatim):**

> "But weirdly, it doesn't just submit its correct answer and call it a day." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 6:50 (20.8%)

> "Many assumed this was just the latest, weirdest, fumbled attempt." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:18 (0.8%)

> "But, what's weird is that none of them are canceling it because they gave up on AI." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 0:34 (2.8%)

> "And this crazy progress is getting me scared because it's now a matter of time before they bytecode these videos." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 4:22 (21.5%)

> "It's kind of crazy to think about how they solved it." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 2:54 (8.4%)

> "China's line is a little smoother, because remember, they're buying less oil, so they can afford to skip the crazy price surges." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 12:17 (34.6%)

> "But in the late 1800s, it was discovered that you could use it to make this weird substance." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 1:38 (5.3%)

**Do.** Mark genuine strangeness.

**Don't.** Do not label routine facts wild.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.57/1k words; PASS if ≥1 hit (corpus uses it in 83% of weighted videos) and rate ≤ 1.1/1k.


---

## H. Us-versus-them framing

### A053. "They" density

**Definition.** They/them/their per 1k (actors vs. viewer).

**Detector.** function `they_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 14.6 | 9.9 | 23.6 |
| Gen (4x) | 12.4 | 6.3 | 16.5 |
| Especially (3x) | 12.1 | 11.6 | 18.4 |
| Oil (5x) | 7.1 | 7.1 | 7.1 |
| Others (1x) | 14.6 | 7.7 | 27.8 |
| **weighted** | median 12.7 (IQR 11.1–15.0) | | |

**How each creator does it (verbatim anchor lines):**

> "And at the latest by July 10th, they had pinpointed the cause, that accidental set of instructions." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 17:37 (44.8%) — value here: **9.9**

> "And deployment can vary from training in all kinds of ways, especially once you move to systems like the ones we have now, that are smart enough to start to understand the context that they're in." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 19:08 (44.7%) — value here: **12.7**

> "Again, you probably say the AI companies since that's where again all the money is moving, but even they're having to fight to keep you." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 12:13 (60.0%) — value here: **12.6**

> "They gained a million new subscribers across all five channels, but the revenue tells a different story." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 13:43 (63.1%) — value here: **14.2**

> "They really do have their own satellites parked up here in spots picked, so each one can see as many potential customers as possible." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 14:04 (56.6%) — value here: **11.6**

> "But if I had to guess, it's because they know something a lot bigger and a lot worse than a crude oil shortage, like we said at the top of this video, is already starting to hit the world." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 13:17 (37.5%) — value here: **7.1**

> "Since replacing the windows, they've also tried white noise machines." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 16:06 (52.7%) — value here: **11.6**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=9.9, `adam/02-bestselling-book`=12.7, `adam/03-no-longer-in-control`=23.6, `adam/04-superintelligence`=17.2, `adam/05-sam-altman`=14.6, `gen/1`=12.6, `gen/2`=14.2, `gen/3`=14.4, `gen/4`=12.3, `gen/5`=9.7, `gen/6`=6.3, `gen/7`=11.8, `gen/8`=13.4, `gen/9`=11.1, `gen/10`=16.5, `esp/01-spacex`=11.6, `esp/02-ai-paradox`=18.4, `esp/06-data-centers`=12.1, `esp/03-oil-apocalypse`=7.1, `after/01-dark-side-data-centers`=11.6, `after/02-greed`=24.5, `after/03-recycling`=12.7, `after/04-pov-ai`=14.9, `after/05-middle-class`=8.8, `after/06-diamonds`=16.2, `after/07-trump-family`=7.7, `after/08-tokens`=12.2, `after/09-microchip-war`=27.8, `after/10-water`=15.0, `after/11-anthropic-ipo`=21.0, `after/12-data-centres-not-working`=14.2

</details>

**Do.** Name who "they" are.

**Don't.** Do not leave "they" undefined.

**Checklist test.** Compute `they_per_k` on your outline/draft. PASS if inside the weighted IQR 11.1–15.0, or inside the chosen mode's min–max range (see table).

### A054. Institution as antagonist

**Definition.** Private equity, big tech, Wall Street, companies, billionaires.

**Detector.** regex `\b(private equity|big tech|wall street|corporations?|billionaires?|the (companies|banks|government|rich|elites?)|these (companies|firms))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.71 | 47.8 |
| Gen (4x) | 9/10 | 3.57 | 1.1 |
| Especially (3x) | 2/3 | 0.34 | 44.2 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 10/12 | 1.44 | 6.7 |
| **weighted** | 86% of weight | 2.01 | 9.5 |

**How each creator does it (verbatim):**

> "There's an AI race, of course, and one of the biggest corporations in it is Galvanic Labs." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 1:33 (3.6%)

> "Hugging Face is a big tech company that stores all kinds of things related to AI." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 17:12 (52.4%)

> "Cuz right now, these companies like Meta have gotten so big that America's problems stop being their problems." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 0:30 (2.2%)

> "One that Big Tech has already planned for, so when a data center dies, they walk away just fine." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 0:40 (4.0%)

> "The long wires between cities were owned and paid for by the government, meant for universities and labs." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 2:19 (6.7%)

> "The companies involved in building them may deny that there are any delays, but satellite imagery says otherwise." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 1:03 (3.9%)

**Do.** Specific actor, specific action.

**Don't.** Do not blanket-villainize.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 2.01/1k words; PASS if ≥1 hit (corpus uses it in 86% of weighted videos) and rate ≤ 4.0/1k.

### A055. Viewer-as-victim frame

**Definition.** "They're charging you / betting that you…".

**Detector.** regex `\b(betting (that )?you|charging you|making you|selling you|your data|at your expense|you'?re (paying|the product))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 99.1 |
| Gen (4x) | 6/10 | 0.21 | 41.2 |
| Especially (3x) | 1/3 | 0.07 | 81.3 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.02 | 40.6 |
| **weighted** | 35% of weight | 0.11 | 46.5 |

**How each creator does it (verbatim):**

> "We don't sell your data or anything like that." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:28 (99.1%)

> "It's a private email service built on the idea that your data belongs to you and nobody else." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:06 (46.5%)

> "ProtonMail is a private encrypted alternative to services like Gmail, designed to give you more control over your data." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 9:56 (43.7%)

> "Launch the chips from Earth, catch the solar panels, attach them together, your data centers in space." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 20:12 (81.3%)

> "Sure, I could make some money selling you something once, I could make more money if I sold it to you once a month for the rest of your life." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 12:31 (40.6%)

**Do.** Show the mechanism of harm.

**Don't.** Do not imply viewers are stupid.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.11/1k words; PASS if 0-1 per 1k words; it is optional (35% weighted coverage) — only use with a reason.

### A056. Insider-vs-outsider

**Definition.** "Insiders / people in the know / employees".

**Detector.** regex `\b(insiders?|employees|people (inside|in the know|close to)|whistleblower\w*|former (employee|staff))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.77 | 19.2 |
| Gen (4x) | 1/10 | 0.1 | 15.8 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 5/12 | 0.46 | 34.0 |
| **weighted** | 37% of weight | 0.36 | 15.8 |

**How each creator does it (verbatim):**

> "Lots of people inside Galvanic think that is clearly a terrible idea." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 2:41 (6.3%)

> "In 2026, OpenAI started focusing a lot on persistence, training models to run for long stretches at one task and became available for employees to use around May." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 16:06 (49.0%)

> "So, now I can force my employees to start using AI and to stop talking to each other about how this company is tanking." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 3:15 (15.8%)

> "Extra profits weren't just redistributed to employees, but their employers were proud to do it." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 11:22 (34.0%)

**Do.** Use insider testimony for credibility.

**Don't.** Do not anonymize everything.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.36/1k words; PASS if 0-1 per 1k words; it is optional (37% weighted coverage) — only use with a reason.

### A057. "Us" collective stakes

**Definition.** "We as a society / all of us".

**Detector.** regex `\b(as a society|all of us|humanity|we all|everyone)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.55 | 2.3 |
| Gen (4x) | 10/10 | 0.9 | 10.6 |
| Especially (3x) | 3/3 | 1.41 | 22.7 |
| Oil (5x) | 1/1 | 0.66 | 5.9 |
| Others (1x) | 9/12 | 0.68 | 13.0 |
| **weighted** | 97% of weight | 1.11 | 6.5 |

**How each creator does it (verbatim):**

> "By 2003, he was convinced that if anyone succeeded in doing so, everyone on Earth would die." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:04 (0.2%)

> "Right now it might feel like everyone, including your grandma, is selling an AI powered something." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 1:22 (4.0%)

> "And right now, that's becoming a problem because not everyone is making that same bet." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 0:49 (3.6%)

> "something similar and my message is the same for everyone who's already reached" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 30:44 (93.3%)

> "When everyone uses AI in a society, our collective thought begins to narrow." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 9:44 (59.8%)

> "There's zero slack, every drop gets used, so any disruption affects everyone." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:06 (5.9%)

> "We all need to work together to make sure that we can win and we can win safely." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 1:34 (11.1%)

**Do.** Adam: civilization-level stakes.

**Don't.** Do not get preachy.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 1.11/1k words; PASS if ≥1 hit (corpus uses it in 97% of weighted videos) and rate ≤ 2.2/1k.


---

## I. Credibility signals

### A058. Source density

**Definition.** Report/study/data/documents per 1k.

**Detector.** function `credibility_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 3.4 | 2.7 | 3.8 |
| Gen (4x) | 1.2 | 0.2 | 13.9 |
| Especially (3x) | 4.3 | 0.6 | 8.2 |
| Oil (5x) | 0.0 | 0.0 | 0.0 |
| Others (1x) | 3.3 | 0.5 | 21.6 |
| **weighted** | median 2.7 (IQR 1.0–3.8) | | |

**How each creator does it (verbatim anchor lines):**

> "The standard at other companies is to release a safety report with every new model launch." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 24:47 (63.0%) — value here: **3.4**

> "Well, according to Yudkowsky and Soares, it's not about wanting to harm us." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 26:42 (62.3%) — value here: **2.7**

> "They brought back 350 veteran engineers called gray beards and in this year's JD Power quality study, Ford came first amongst mainstream brands for the first time since 2010 up from 15th in 2023." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 15:40 (76.4%) — value here: **2.1**

> "But once you see this document, you'll see that that's barely part of it." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 2:00 (8.7%) — value here: **1.5**

> "According to our man Abraham Maslow, one." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 8:27 (34.0%) — value here: **0.6**

> "According to our account, the company has 34 data centers in the US." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 22:15 (72.9%) — value here: **21.6**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=3.4, `adam/02-bestselling-book`=2.7, `adam/03-no-longer-in-control`=3.8, `adam/04-superintelligence`=3.8, `adam/05-sam-altman`=2.9, `gen/1`=0.5, `gen/2`=1.0, `gen/3`=2.7, `gen/4`=2.1, `gen/5`=13.9, `gen/6`=0.7, `gen/7`=0.2, `gen/8`=1.5, `gen/9`=2.4, `gen/10`=0.9, `esp/01-spacex`=0.6, `esp/02-ai-paradox`=4.3, `esp/06-data-centers`=8.2, `esp/03-oil-apocalypse`=0.0, `after/01-dark-side-data-centers`=21.6, `after/02-greed`=1.5, `after/03-recycling`=1.0, `after/04-pov-ai`=3.1, `after/05-middle-class`=1.2, `after/06-diamonds`=4.9, `after/07-trump-family`=3.1, `after/08-tokens`=3.5, `after/09-microchip-war`=0.5, `after/10-water`=21.3, `after/11-anthropic-ipo`=5.4, `after/12-data-centres-not-working`=19.1

</details>

**Do.** Cite named sources in-flow.

**Don't.** Do not cite "studies show".

**Checklist test.** Compute `credibility_per_k` on your outline/draft. PASS if inside the weighted IQR 1.0–3.8, or inside the chosen mode's min–max range (see table).

### A059. Exact numbers per minute

**Definition.** Digits per minute.

**Detector.** function `num_per_min` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 1.3 | 1.0 | 2.4 |
| Gen (4x) | 2.0 | 1.0 | 3.3 |
| Especially (3x) | 1.7 | 0.7 | 2.1 |
| Oil (5x) | 1.3 | 1.3 | 1.3 |
| Others (1x) | 1.5 | 0.3 | 3.3 |
| **weighted** | median 1.5 (IQR 1.26–2.41) | | |

**How each creator does it (verbatim anchor lines):**

> "In fact, when I started following the account that introduced MechaHitler as a name to Grok on Tuesday, July 8th, I came across several tweets dating back years like this one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 15:39 (39.8%) — value here: **1.28**

> "As new subscriptions surge, so does Galvanic's stock price, enough to make back the entire $10 million cost of the run in the first 72 hours." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 22:43 (53.0%) — value here: **1.02**

> "In fact, 41% from their low in April." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 11:03 (54.3%) — value here: **1.41**

> "Estimated monthly earnings has dropped 70% from roughly 52,000 in March 2024 to around 13,000 to 17,000 by February 2026." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 13:47 (63.4%) — value here: **1.87**

> "If gravity drags them into Earth's atmosphere, it's moving closer, 100 miles closer, ensuring the time it takes to receive or send a signal from Earth is lower than anyone else, because competition from low Earth orbit is hot." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:56 (44.0%) — value here: **1.67**

> "(tense piano music) That means that shipping alone now adds another $23 to the price of each barrel of oil." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 17:43 (50.0%) — value here: **1.31**

> "Documents show that Microsoft planned for each of these buildings to use 1 million gallons of water a day." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 19:35 (64.1%) — value here: **2.14**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=1.28, `adam/02-bestselling-book`=1.02, `adam/03-no-longer-in-control`=1.21, `adam/04-superintelligence`=2.41, `adam/05-sam-altman`=1.81, `gen/1`=1.41, `gen/2`=1.87, `gen/3`=3.31, `gen/4`=1.54, `gen/5`=1.26, `gen/6`=3.2, `gen/7`=1.02, `gen/8`=2.53, `gen/9`=2.06, `gen/10`=2.62, `esp/01-spacex`=1.67, `esp/02-ai-paradox`=0.73, `esp/06-data-centers`=2.07, `esp/03-oil-apocalypse`=1.31, `after/01-dark-side-data-centers`=2.14, `after/02-greed`=1.57, `after/03-recycling`=1.32, `after/04-pov-ai`=1.63, `after/05-middle-class`=3.31, `after/06-diamonds`=0.72, `after/07-trump-family`=1.46, `after/08-tokens`=2.71, `after/09-microchip-war`=0.63, `after/10-water`=1.42, `after/11-anthropic-ipo`=0.35, `after/12-data-centres-not-working`=2.61

</details>

**Do.** Precise numbers > vague.

**Don't.** Do not use false precision.

**Checklist test.** Compute `num_per_min` on your outline/draft. PASS if inside the weighted IQR 1.26–2.41, or inside the chosen mode's min–max range (see table).

### A060. Original interview signal

**Definition.** "I talked/spoke to / told me".

**Detector.** regex `\bI (talked|spoke|asked|interviewed|reached out|sat down)\b|told (me|us)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.1 | 66.8 |
| Gen (4x) | 2/10 | 0.1 | 18.4 |
| Especially (3x) | 1/3 | 0.07 | 35.3 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 4/12 | 0.13 | 54.3 |
| **weighted** | 36% of weight | 0.1 | 37.2 |

**How each creator does it (verbatim):**

> "Congress started asking questions, one of which was, any more of these rogue incidents y'all haven't told us about yet?" — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 24:41 (75.2%)

> "But then I talked to Nate." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 28:38 (66.8%)

> "But then I remember something a wise man once told me, just do it." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 5:03 (23.2%)

> "is what I would have said if every other graph on this table hadn't already told me one thing while meaning another." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 3:04 (13.5%)

> "That friction I talked about, they built it in." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 5:45 (35.3%)

> "When I asked Gaddy if he would speak on the record, he told me he was under an NDA." — *Others (1x)*, `after/10-water` "We Calculated How Much Water Data Centers Actually Use. The " @ 8:40 (65.2%)

**Do.** Highlight first-hand reporting.

**Don't.** Do not imply access you lack.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.1/1k words; PASS if 0-1 per 1k words; it is optional (36% weighted coverage) — only use with a reason.

### A061. Research-process signal

**Definition.** "As I researched / I dug into / I read".

**Detector.** regex `\b(as I (researched|dug|read|looked)|I (dug|read|went through|looked into|found))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.06 | 69.0 |
| Gen (4x) | 9/10 | 0.71 | 6.3 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 4/12 | 0.13 | 26.1 |
| **weighted** | 47% of weight | 0.31 | 6.6 |

**How each creator does it (verbatim):**

> "As I researched this video, that is by far the most tragic, kind of most paradoxical thing that's come up." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 27:07 (69.0%)

> "was on saive say I went through the same thing in 2018 in my college when it" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 17:56 (54.5%)

> "So I went through the terms of services, court rulings, and what happened the last time piracy got this bad." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 1:20 (6.6%)

> "And I found all of these really cool released CIA documents about it." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 9:33 (57.5%)

**Do.** One line per act.

**Don't.** Do not narrate tedium.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.31/1k words; PASS if 0-1 per 1k words; it is optional (47% weighted coverage) — only use with a reason.

### A062. Named expert

**Definition.** Expert + role.

**Detector.** regex `\b(professor|researcher|scientist|economist|analyst|expert|engineer|former \w+)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.45 | 3.9 |
| Gen (4x) | 5/10 | 0.19 | 20.4 |
| Especially (3x) | 1/3 | 0.13 | 7.0 |
| Oil (5x) | 1/1 | 0.17 | 96.2 |
| Others (1x) | 7/12 | 0.31 | 45.6 |
| **weighted** | 69% of weight | 0.29 | 7.0 |

**How each creator does it (verbatim):**

> "An unnamed engineer performs an unintended action on the live code controlling Grok, x." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 1:31 (3.9%)

> "I actually read the paper of the guy that you had on to the world's most cited computer scientist, the godfather of AI." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 0:38 (1.9%)

> "Back then, it might have been an economist, but today it's the CEOs and the narratives." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 14:58 (67.1%)

> "accusation was false this is the story of a former ivy league student's 8-year" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 0:15 (0.8%)

> "You could send a professor's email across it." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 2:25 (7.0%)

> "And Americans, I know Trump is talking up a diesel export ban to save us from rising fuel costs, but any expert economist in energy or oil whatsoever, left, right or center will tell you the exact same thing, which is that this is going […]" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 34:08 (96.2%)

> "Okay, but I I saw a TikTok of a mad scientist fellow who was turning plastic into fuel." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 25:33 (83.0%)

**Do.** Name + role + why trust.

**Don't.** Do not appeal to anonymous authority.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.29/1k words; PASS if ≥1 hit (corpus uses it in 69% of weighted videos) and rate ≤ 1/1k.

### A063. Primary document

**Definition.** Filings, court docs, testimony, papers.

**Detector.** regex `\b(court|filing\w*|lawsuit|testimony|unsealed|paper|memo|leaked|documents?|transcript)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.68 | 16.8 |
| Gen (4x) | 8/10 | 0.6 | 9.6 |
| Especially (3x) | 2/3 | 0.2 | 46.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 10/12 | 0.46 | 24.4 |
| **weighted** | 75% of weight | 0.54 | 20.5 |

**How each creator does it (verbatim):**

> "Some agents actually find the original ExploitGym paper online, and they start to think they might be screwed." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 10:25 (31.7%)

> "Some of it we only know now, thanks to unsealed court testimony that's come out just this year." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:20 (0.8%)

> "But then I looked at the 2020 crash when everyone was stuck at home fighting over toilet paper." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 5:58 (26.8%)

> "Now again, there is already a lawsuit and the SEC's been asked to look into all of this." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 15:44 (69.5%)

> "A recent paper in the Lancet found that doctors using AI assistance for just 4 months had a weakened ability to spot cancer on their own." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 6:33 (40.2%)

> "Donna set up a local campaign to challenge the reasonzoning, but the lawsuit was dismissed." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 4:49 (15.8%)

**Do.** Show the document on screen.

**Don't.** Do not paraphrase without citing.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.54/1k words; PASS if ≥1 hit (corpus uses it in 75% of weighted videos) and rate ≤ 1.1/1k.

### A064. Honest-uncertainty signal

**Definition.** "We don't know exactly / it's unclear".

**Detector.** regex `\b(we don'?t (know|have)|it'?s (unclear|not clear)|no one knows|hard to say|we can'?t be sure)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.35 | 22.4 |
| Gen (4x) | 1/10 | 0.02 | 74.0 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 68.2 |
| Others (1x) | 5/12 | 0.15 | 53.7 |
| **weighted** | 49% of weight | 0.17 | 30.0 |

**How each creator does it (verbatim):**

> "Well, we don't know, but thinking through in detail how it might go is the way to start grappling with that." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 3:44 (11.0%)

> "We don't know why it's learning to do this." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 8:17 (19.3%)

> "Cuz look, no one knows yet what will happen." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 15:03 (74.0%)

> "Say it with me, we don't know, they're not saying." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 24:12 (68.2%)

> "What if we just fire a bunch of people and then we don't have to spend as much money?" — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 17:55 (53.7%)

**Do.** Mark limits of evidence.

**Don't.** Do not hide uncertainty.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.17/1k words; PASS if 0-1 per 1k words; it is optional (49% weighted coverage) — only use with a reason.


---

## J. Rewatch & share triggers

### A065. Quotable maxim

**Definition.** Short general claim ≤12 words with "is/are".

**Detector.** regex `^(\w+\s){1,10}(is|are)\s(\w+\s?){1,6}[.!]$` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 2.52 | 5.0 |
| Gen (4x) | 9/10 | 1.64 | 6.7 |
| Especially (3x) | 3/3 | 4.04 | 4.5 |
| Oil (5x) | 1/1 | 2.15 | 5.1 |
| Others (1x) | 12/12 | 2.55 | 9.6 |
| **weighted** | 96% of weight | 2.32 | 5.1 |

**How each creator does it (verbatim):**

> "Polish Twitter is a lot quicker to notice." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 1:58 (5.0%)

> "That is the opening claim of AI 2027." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 0:05 (0.2%)

> "But then I realized along the way that restaurants are only the start of it." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 1:20 (5.8%)

> "But what I quickly found was that the answer is no." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 4:57 (24.3%)

> "This video is sponsored by Wealthfront." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 1:07 (4.5%)

> "This is the world oil economy." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:49 (5.1%)

> "And many of the biggest server farms are emerging from the desert." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:16 (0.9%)

**Do.** Write 2-4 clip-able lines.

**Don't.** Do not write fortune cookies.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 2.32/1k words; PASS if ≥1 hit (corpus uses it in 96% of weighted videos) and rate ≤ 4.6/1k.

### A066. Shocking stat line

**Definition.** Sentence with a number + "more than/every/all".

**Detector.** regex `\d.*\b(more than|every|all|entire|per (day|year|second))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.26 | 55.9 |
| Gen (4x) | 8/10 | 0.83 | 19.9 |
| Especially (3x) | 2/3 | 1.01 | 6.7 |
| Oil (5x) | 1/1 | 0.5 | 56.4 |
| Others (1x) | 9/12 | 0.57 | 29.2 |
| **weighted** | 86% of weight | 0.58 | 49.9 |

**How each creator does it (verbatim):**

> "The organization that I work for, 80,000 Hours, has an entire website dedicated to helping you make a difference on these things." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 38:00 (96.7%)

> "OpenBrain safety team is pushing for a freeze on Agent-4, stopping all internal use." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 18:38 (54.7%)

> "No wonder that four out of 10 restaurant operators made no profit at all last year." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 3:23 (14.6%)

> "The 100 biggest builders sell about half of all the new single-family homes." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 5:45 (25.3%)

> "Hasn't been opened in more than 100 years, going all the way back to the plane." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 3:05 (12.4%)

> "(tense music) And these 30 million barrels a day fuel freight trains, farm equipment, construction, commercial shipping, generators, and most of all, trucking." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 20:01 (56.4%)

> "Another study of 2,444 companies found that for every dollar a company spends on AI tokens, $0." — *Others (1x)*, `after/08-tokens` "Uh oh, tokens are getting too expensive..." @ 4:35 (29.2%)

**Do.** Make the stat shareable alone.

**Don't.** Do not round dishonestly.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.58/1k words; PASS if ≥1 hit (corpus uses it in 86% of weighted videos) and rate ≤ 1.2/1k.

### A067. Exclusive-detail claim

**Definition.** "I haven't seen reported anywhere".

**Detector.** regex `\b(haven'?t seen (this|it)? ?reported|anywhere else|first time|never before|exclusive)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.13 | 61.0 |
| Gen (4x) | 3/10 | 0.12 | 25.4 |
| Especially (3x) | 2/3 | 0.13 | 64.3 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 7/12 | 0.17 | 57.1 |
| **weighted** | 52% of weight | 0.14 | 53.6 |

**How each creator does it (verbatim):**

> "Turns out that OpenAI was not the first time Sam Altman had faced this kind of challenge." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 27:55 (69.8%)

> "For the first time, the public hears about the existence of Agent-4, how powerful it is and the risks it poses." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 18:16 (53.6%)

> "But what's happening here is for the first time, companies are finally checking and finding out exactly what they've chosen to ignore over the last few years." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 14:15 (69.5%)

> "It's exactly why for the first time in modern American history, data centers are pulling in as much private money as building every single home in the country combined." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 3:17 (19.9%)

> "For the first time in generations, enormous customers are showing up saying, if you can make vastly more electricity, we will buy it." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 27:29 (79.7%)

> "So, on my way to the diamond lab, I was researching the first time that anyone ever grew diamonds." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 9:29 (57.1%)

**Do.** Back it up.

**Don't.** Do not overclaim.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.14/1k words; PASS if ≥1 hit (corpus uses it in 52% of weighted videos) and rate ≤ 1/1k.

### A068. Share prompt

**Definition.** "Share this / send this to".

**Detector.** regex `\b(share (this|it)|send (this|it) to|show (this|it) to)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 58.6 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 7% of weight | 0.01 | 58.6 |

**How each creator does it (verbatim):**

> "When investigators went back and checked the agents' chains of thought, they found agents often lacked a clear story for how the Hugging Face attack would help them with their objective, and instead were motivated by a broad hope that they would find something interesting […]" — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 19:14 (58.6%)

**Do.** Rare; only for civic asks.

**Don't.** Do not beg.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.01/1k words; PASS if 0-1 per 1k words; it is rare (7% weighted coverage) — only use with a reason.


---

## K. Comment bait

### A069. Explicit comment ask

**Definition.** "Let me know in the comments / comment below".

**Detector.** regex `\b(let me know|comment\w*|tell me (in|what|below))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.13 | 62.6 |
| Gen (4x) | 6/10 | 0.33 | 68.0 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.04 | 60.7 |
| **weighted** | 39% of weight | 0.16 | 60.7 |

**How each creator does it (verbatim):**

> "They get Grok eventually to suggest a way of breaking into Stancil's home, comment on what times Stancil might likely be asleep, so on and so on, while occasionally saying things like r*pe is a serious crime and don't do crimes." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 11:00 (28.0%)

> "We would love to help, but even if you're not sure what to make of all this yet, my hopes for this video will be realized if we can start a conversation that feels alive here in the comments and offline about what this actually […]" — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 33:08 (97.2%)

> "But before you come with me in the comments, that's actually not as insane as it sounds." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 10:58 (48.3%)

> "So before you fiercely start typing in the comments that the stock market isn't the economy, chill." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 0:21 (1.5%)

> "If someone can prove me wrong, I would welcome you to do so in the comment section." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 18:41 (60.7%)

**Do.** Ask a specific opinion question.

**Don't.** Do not ask "thoughts?".

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.16/1k words; PASS if 0-1 per 1k words; it is optional (39% weighted coverage) — only use with a reason.

### A070. Opinion poll question

**Definition.** "Do you think / would you".

**Detector.** regex `\b(do you think|would you|what do you think|are you)\b.*\?$` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.13 | 23.1 |
| Gen (4x) | 3/10 | 0.07 | 74.1 |
| Especially (3x) | 1/3 | 0.2 | 41.1 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 6/12 | 0.26 | 48.6 |
| **weighted** | 42% of weight | 0.12 | 50.1 |

**How each creator does it (verbatim):**

> "Grok, I've been wondering as an AI, are you able to worship any God?" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 9:04 (23.1%)

> "What do you think was most implausible?" — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 33:43 (98.9%)

> "Which means the real question is which side of that sale are you going to be on?" — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 19:56 (89.4%)

> "Like, when you think about town hall, do you think about young people going to that?" — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 11:23 (50.1%)

> "Where would you want to stay?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:13 (41.1%)

> "During that period, how many times do you think the wages of the residents in that area had risen?" — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 13:50 (50.7%)

**Do.** Pose a binary the audience can argue.

**Don't.** Do not ask leading questions.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.12/1k words; PASS if 0-1 per 1k words; it is optional (42% weighted coverage) — only use with a reason.

### A071. Hot take

**Definition.** "Honestly / unpopular / I'd argue".

**Detector.** regex `\b(I'?d argue|unpopular|hot take|controversial|I'?ll say it|honestly,)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.16 | 54.1 |
| Gen (4x) | 2/10 | 0.07 | 65.5 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.04 | 34.2 |
| **weighted** | 38% of weight | 0.08 | 52.4 |

**How each creator does it (verbatim):**

> "It is not controversial that anything that is extremely powerful and doesn't share your goals is dangerous." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 35:22 (82.6%)

> "At a board meeting in December 2022, Sam told the directors that three controversial changes to GPT-4 had all been approved by the company's joint safety review board." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 22:23 (55.9%)

> "embroiled in you know controversial opinions I was Politically Incorrect and" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 11:22 (34.5%)

> "And it's controversial, but I respect the hell out of them because just like you and I, they couldn't change the system, but they understood it and decided to win." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 16:26 (96.6%)

> "She was from a controversial New York City real estate family, and so was he." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 7:02 (41.5%)

**Do.** One defensible stance.

**Don't.** Do not troll.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (38% weighted coverage) — only use with a reason.


---

## L. Subscribe & CTA psychology

### A072. Subscribe ask

**Definition.** Explicit subscribe line.

**Detector.** regex `\bsubscrib\w*\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 98.8 |
| Gen (4x) | 2/10 | 0.4 | 24.2 |
| Especially (3x) | 2/3 | 0.27 | 98.8 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 6/12 | 0.17 | 97.1 |
| **weighted** | 34% of weight | 0.23 | 98.5 |

**How each creator does it (verbatim):**

> "We always give away a free book to new subscribers and for this video, we have added If Anyone Builds It, Everyone Dies to the list." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:15 (98.6%)

> "And if you found this valuable, please do like and subscribe and maybe spend a second thinking about a person or two that you know who might find it valuable—maybe your AI progress skeptical friend, or your ChatGPT-curious Uncle or maybe your local member of […]" — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 33:43 (98.9%)

> "mean the video when I was only at like 5,000 subscribers but I knew this" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 15:58 (48.5%)

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%)

> "Now, if you could do me a favor, I would love to count you as a subscriber to the channel." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 24:20 (97.9%)

> "Please don't forget to like this video and subscribe to our channel." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 13:44 (97.1%)

**Do.** Tie to value ("if you want more…").

**Don't.** Do not ask in the first 30 s.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.23/1k words; PASS if 0-1 per 1k words; it is optional (34% weighted coverage) — only use with a reason.

### A073. Newsletter funnel

**Definition.** Newsletter CTA.

**Detector.** regex `\bnewsletter\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.06 | 98.5 |
| Gen (4x) | 9/10 | 0.24 | 98.4 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 43% of weight | 0.11 | 98.5 |

**How each creator does it (verbatim):**

> "While you're there, we would love for you to sign up for our newsletter to stay up to date on this topic." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:11 (98.5%)

> "And so, I'll definitely be diving even deeper into this in my free weekly newsletter in the video description." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 20:07 (98.9%)

> "And so, I'll be going even deeper into this issue next week on my free newsletter in the video description." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 21:24 (98.5%)

**Do.** Gen: "free weekly newsletter" at end.

**Don't.** Do not pitch mid-hook.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.11/1k words; PASS if 0-1 per 1k words; it is optional (43% weighted coverage) — only use with a reason.

### A074. Gratitude sign-off

**Definition.** Thank-you line.

**Detector.** regex `\bthank(s| you)\b` in scope `end`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.13 | 99.7 |
| Gen (4x) | 4/10 | 0.1 | 99.8 |
| Especially (3x) | 3/3 | 0.2 | 99.2 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 6/12 | 0.17 | 96.6 |
| **weighted** | 58% of weight | 0.13 | 99.6 |

**How each creator does it (verbatim):**

> "The last thing to say is just thank you so much for watching, for being the reason that we make these videos." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:42 (99.7%)

> "Thank you so much for watching and see you in the next one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 39:16 (99.9%)

> "Thanks." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 22:40 (99.8%)

> "Thanks." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 20:25 (99.5%)

> "Thank you for your support and subscribing and watching." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 24:39 (99.2%)

> "(gentle forlorn music ends) All right, thanks again for watching another episode of "Search Party."" — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 16:02 (94.7%)

**Do.** Warm, one line.

**Don't.** Do not grovel.

**Checklist test.** In scope `end`, count sentences matching the detector. Weighted norm ≈ 0.13/1k words; PASS if ≥1 hit (corpus uses it in 58% of weighted videos) and rate ≤ 1/1k.

### A075. Patronage/support framing

**Definition.** "Being the reason / supporting the channel".

**Detector.** regex `\b(support(ing)? (the|this|me|us)|being the reason|patreon|members?)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.42 | 37.0 |
| Gen (4x) | 3/10 | 0.12 | 34.4 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 6/12 | 0.2 | 76.3 |
| **weighted** | 46% of weight | 0.21 | 34.4 |

**How each creator does it (verbatim):**

> "One of the features of artificial intelligence is it scares the heck out of members of both parties." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 39:47 (92.9%)

> "And lots of people, including 20 members of Congress, are asking the exact same question." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 23:15 (59.1%)

> "their free straight arrow news app not only are you supporting me but a sponsor" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 7:13 (21.9%)

> "And so if you want to support the channel, go to by bracon." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 6:08 (36.0%)

> "But, the silver lining to this is that hundreds of community members came out to say no against this proposal." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 17:22 (63.7%)

**Do.** Frame as shared mission.

**Don't.** Do not guilt-trip.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.21/1k words; PASS if 0-1 per 1k words; it is optional (46% weighted coverage) — only use with a reason.

### A076. Sponsor-as-value

**Definition.** Sponsor framed as solving the problem just described.

**Detector.** regex `\b(that'?s (exactly )?(where|why)|which is (exactly )?why I)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.13 | 26.4 |
| Gen (4x) | 10/10 | 0.45 | 38.8 |
| Especially (3x) | 3/3 | 0.2 | 73.9 |
| Oil (5x) | 1/1 | 0.17 | 14.8 |
| Others (1x) | 7/12 | 0.26 | 16.0 |
| **weighted** | 74% of weight | 0.29 | 38.6 |

**How each creator does it (verbatim):**

> "So that's where we are in the real world." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 3:53 (11.4%)

> "That's why help." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 13:38 (41.5%)

> "That's why I have signed an executive order banning large institutional addresses from buying single-family homes." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 14:08 (62.2%)

> "And that's why earlier I didn't even need to say the whole hypothetical stuff." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 6:54 (33.9%)

> "That's why these paths will make sense, but they will always cluster and echo each other." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 12:02 (73.9%)

> "(tense piano music) There she is, runs East to West, and that's why it's called "The East-West Pipeline."" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 5:14 (14.8%)

> "So, that's why this diamond can cut ice like it's butter, cuz it's stealing heat from my hand." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 4:45 (28.6%)

**Do.** Bridge from the topic.

**Don't.** Do not oversell.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.29/1k words; PASS if ≥1 hit (corpus uses it in 74% of weighted videos) and rate ≤ 1/1k.

### A077. Next-video handoff

**Definition.** "Watch this video next / see you in the next one".

**Detector.** regex `\b(next (one|video)|another video|this video (here|right)|watch (this|next))\b` in scope `end`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.1 | 99.9 |
| Gen (4x) | 6/10 | 0.17 | 99.0 |
| Especially (3x) | 2/3 | 0.2 | 93.6 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.04 | 99.2 |
| **weighted** | 52% of weight | 0.12 | 99.3 |

**How each creator does it (verbatim):**

> "Thank you so much for watching and see you in the next one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 39:16 (99.9%)

> "We'll see you in the next one." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:47 (99.9%)

> "So the point is in that garage sale analogy, the trucks are already lined up on the sidewalk waiting for the next one." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 19:48 (88.8%)

> "But if you'd rather see another video on getting the truth of what's really happening with AI, you will want to watch this one next." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 20:13 (99.3%)

> "It is down there somewhere and I will see you in the next video." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 34:22 (99.7%)

> "Watch this video next to see how it's playing out right now in the present." — *Others (1x)*, `after/04-pov-ai` "" @ 17:26 (98.8%)

**Do.** Point at a specific next video.

**Don't.** Do not end abruptly.

**Checklist test.** In scope `end`, count sentences matching the detector. Weighted norm ≈ 0.12/1k words; PASS if ≥1 hit (corpus uses it in 52% of weighted videos) and rate ≤ 1/1k.


---

## M. Parasocial cues

### A078. Opinion disclosure

**Definition.** "I think / I believe / I feel".

**Detector.** regex `\bI (think|believe|feel|honestly)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.48 | 35.8 |
| Gen (4x) | 10/10 | 0.5 | 13.7 |
| Especially (3x) | 1/3 | 0.07 | 30.1 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 11/12 | 0.46 | 51.5 |
| **weighted** | 88% of weight | 0.74 | 19.5 |

**How each creator does it (verbatim):**

> "I think we'll reach the point where it's true as we scale the models." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 15:20 (35.8%)

> "And now, I think this whole crazy story has given us an incredible opportunity." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 29:57 (91.2%)

> "I don't know, but whichever side wins, I think it's pretty clear that the software companies won't disappear." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 19:02 (93.5%)

> "And to see what I'm talking about, I think what better example than the Great Depression that started in 1929." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 2:05 (9.3%)

> "Each one a guess saying, ‘I think I'm doing a good job filling the void with something this random human who gave me this task will like.’" — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 10:23 (30.1%)

> "We’re experiencing what I think is a major market transition we’ve seen in all kinds of industries." — *Others (1x)*, `after/08-tokens` "Uh oh, tokens are getting too expensive..." @ 12:47 (81.5%)

**Do.** Share stance.

**Don't.** Do not overshare.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.74/1k words; PASS if ≥1 hit (corpus uses it in 88% of weighted videos) and rate ≤ 1.5/1k.

### A079. Emotional admission

**Definition.** "Honestly, this scared me / I was shocked".

**Detector.** regex `\b(I was (shocked|surprised|scared|stunned|blown)|this (scared|terrified|shocked) me|freaked (me )?out)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 27.6 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.04 | 15.5 |
| **weighted** | 8% of weight | 0.01 | 27.6 |

**How each creator does it (verbatim):**

> "When that kind of situational awareness first emerged in AIs in 2024, roughly, there was a brief moment where people freaked out." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 11:49 (27.6%)

> "And I kept putting off seeing somebody about it because I was scared to go to the doctor." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 4:46 (15.5%)

**Do.** Admit genuine reaction once.

**Don't.** Do not perform.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.01/1k words; PASS if 0-1 per 1k words; it is rare (8% weighted coverage) — only use with a reason.

### A080. Inclusive invitation

**Definition.** "Come with me / let's".

**Detector.** regex `\b(come with me|let'?s|join me|together)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.74 | 12.3 |
| Gen (4x) | 10/10 | 1.21 | 10.7 |
| Especially (3x) | 3/3 | 1.01 | 18.1 |
| Oil (5x) | 1/1 | 0.99 | 4.5 |
| Others (1x) | 9/12 | 0.59 | 11.3 |
| **weighted** | 97% of weight | 0.97 | 11.5 |

**How each creator does it (verbatim):**

> "But the authors who put together ExploitGym estimate that 30 to 40% of them are just unsolvable." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 4:02 (12.3%)

> "OpenAI's equivalent, the model spec, actually has an entire section laying out what it means to seek truth together with the user." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 21:46 (55.4%)

> "So let's say I work at a private equity fund, a a big fund with this big suit." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 1:58 (9.0%)

> "But let's just say if we hypothetically and theoretically did, it looked and worked exactly like it." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 3:31 (17.3%)

> "First, babies practice syllables, then words, then they glue words together, eventually forming sentences that others can understand." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 2:57 (18.1%)

> "So let's get into it." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:35 (4.5%)

> "We all need to work together to make sure that we can win and we can win safely." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 1:34 (11.1%)

**Do.** Invite the viewer along.

**Don't.** Do not overuse.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.97/1k words; PASS if ≥1 hit (corpus uses it in 97% of weighted videos) and rate ≤ 1.9/1k.

### A081. Gratitude for audience

**Definition.** "you are the reason / thanks for being here".

**Detector.** regex `\b(the reason (we|I)|thank you for (being|supporting)|because of you)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 21.0 |
| Gen (4x) | 3/10 | 0.07 | 82.7 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.04 | 20.3 |
| **weighted** | 21% of weight | 0.04 | 36.9 |

**How each creator does it (verbatim):**

> "The reason I wanted to create OpenAI was to serve as a counterweight to Google." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 8:24 (21.0%)

> "just dealt with all this on my own in in Silence the reason I did that is because" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 27:15 (82.7%)

> "Because the reason I lost that money is what Austin actually built and should be happening." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 21:42 (95.5%)

> "And her coming back is the reason I'm still alive." — *Others (1x)*, `after/04-pov-ai` "" @ 7:02 (39.8%)

**Do.** Adam: end-card mission gratitude.

**Don't.** Do not grovel.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.04/1k words; PASS if 0-1 per 1k words; it is optional (21% weighted coverage) — only use with a reason.


---

## N. Humor timing

### A082. Humor/aside lexicon

**Definition.** Weird/wild/literally/joke words per 1k.

**Detector.** function `humor_per_k` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.7 | 0.2 | 1.5 |
| Gen (4x) | 0.9 | 0.0 | 1.8 |
| Especially (3x) | 0.4 | 0.0 | 0.6 |
| Oil (5x) | 1.5 | 1.5 | 1.5 |
| Others (1x) | 0.6 | 0.0 | 1.7 |
| **weighted** | median 0.7 (IQR 0.4–1.1) | | |

**How each creator does it (verbatim anchor lines):**

> "After the February and May scandals, that wasn't a crazy theory to entertain." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 21:02 (53.5%) — value here: **1.5**

> "Each time we do that, we'll be hoping that their weird internals continue to work the same way in those new environments, or that they shift in ways that are harmless and easily found." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:17 (47.4%) — value here: **0.6**

> "Look, Coca-Cola's recipe, this is the original here, is one of the most famous secrets in the world, and they literally keep it like in this vault in Atlanta." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 5:03 (24.8%) — value here: **1.3**

> "But also, it's probably more weird that you've never heard of them, considering that they're the second most subscribed YouTube channel on Earth with 120 million subscribers." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 16:34 (76.2%) — value here: **1.0**

> "In today's money, they were just giving land away, literally." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 7:10 (28.8%) — value here: **0.4**

> "(tense orchestral music) So here again, here's that route, and this is crazy." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 16:28 (46.4%) — value here: **1.5**

> "Literally, whatever it took to juice the numbers, that's what they would do." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 20:46 (62.2%) — value here: **0.7**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=1.5, `adam/02-bestselling-book`=0.6, `adam/03-no-longer-in-control`=1.1, `adam/04-superintelligence`=0.7, `adam/05-sam-altman`=0.2, `gen/1`=1.3, `gen/2`=1.0, `gen/3`=1.8, `gen/4`=1.0, `gen/5`=0.0, `gen/6`=1.1, `gen/7`=0.5, `gen/8`=0.9, `gen/9`=0.7, `gen/10`=0.3, `esp/01-spacex`=0.4, `esp/02-ai-paradox`=0.0, `esp/06-data-centers`=0.6, `esp/03-oil-apocalypse`=1.5, `after/01-dark-side-data-centers`=0.0, `after/02-greed`=0.7, `after/03-recycling`=1.6, `after/04-pov-ai`=0.0, `after/05-middle-class`=0.8, `after/06-diamonds`=1.1, `after/07-trump-family`=0.0, `after/08-tokens`=1.7, `after/09-microchip-war`=0.5, `after/10-water`=0.0, `after/11-anthropic-ipo`=0.4, `after/12-data-centres-not-working`=0.6

</details>

**Do.** Insert lightness after heavy beats.

**Don't.** Do not joke about victims.

**Checklist test.** Compute `humor_per_k` on your outline/draft. PASS if inside the weighted IQR 0.4–1.1, or inside the chosen mode's min–max range (see table).

### A083. Ironic understatement

**Definition.** "pretty harmless / not great / a little".

**Detector.** regex `\b(not great|pretty (harmless|bad|wild)|a (little|bit) (much|concerning|awkward)|which is fine)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.1 | 20.4 |
| Gen (4x) | 1/10 | 0.02 | 0.6 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 9.7 |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 30% of weight | 0.05 | 9.7 |

**How each creator does it (verbatim):**

> "So that's a pretty wild thing to hear from a state-of-the-art AI system on the public internet." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 2:38 (6.7%)

> "This is where things start to get a little concerning." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 8:50 (25.9%)

> "What if I told you that right now, stocks are priced even more expensive than they were right before, let's say a pretty bad crash." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 0:08 (0.6%)

> "Okay, so all of this is not great, you probably noticed it making your power bill more expensive, flights getting canceled, price of gas, but it's not like post-apocalyptic dystopia." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 3:26 (9.7%)

**Do.** Undercut drama with understatement.

**Don't.** Do not use for tragedies.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.05/1k words; PASS if 0-1 per 1k words; it is optional (30% weighted coverage) — only use with a reason.

### A084. Callback humor

**Definition.** Reusing a phrase from earlier ("MechaHitler week").

**Detector.** regex `\b(again|remember|as I said|like I said|back to)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.61 | 18.9 |
| Gen (4x) | 10/10 | 2.79 | 16.9 |
| Especially (3x) | 3/3 | 0.74 | 12.4 |
| Oil (5x) | 1/1 | 2.81 | 0.0 |
| Others (1x) | 12/12 | 1.42 | 13.2 |
| **weighted** | 100% of weight | 1.73 | 15.6 |

**How each creator does it (verbatim):**

> "And then it uses that intelligence to increase its own abilities again and again and again." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 32:37 (76.1%)

> "Sam, for his part, gets on a flight back to San Francisco." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 5:53 (14.7%)

> "And again, the easiest way to explain what he actually did is with this bottle of Coke." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 4:59 (24.5%)

> "Because maybe a crash will put everything on sale and just maybe you could actually afford it all again." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 0:37 (2.8%)

> "Hasn't been opened in more than 100 years, going all the way back to the plane." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 3:05 (12.4%)

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%)

> "It comes back to how they lean on the tech being inevitable, that someone's going to do it." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 10:09 (71.7%)

**Do.** Callback an earlier odd detail.

**Don't.** Do not explain the joke.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 1.73/1k words; PASS if ≥1 hit (corpus uses it in 100% of weighted videos) and rate ≤ 3.5/1k.

### A085. Parenthetical aside

**Definition.** "which, honestly…/ and yes…".

**Detector.** regex `\b(and yes|which,? (honestly|frankly|by the way)|by the way)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.23 | 42.6 |
| Gen (4x) | 3/10 | 0.14 | 43.8 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 1.4 |
| Others (1x) | 2/12 | 0.07 | 57.7 |
| **weighted** | 47% of weight | 0.15 | 29.4 |

**How each creator does it (verbatim):**

> "This isn't about any one country being evil, by the way." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 19:01 (55.8%)

> "Just doing that took them three days, by the way." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 24:11 (73.7%)

> "And yes, this connects to the whole housing thing we've been talking about." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 18:29 (81.4%)

> "Remember this word for later, by the way." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 5:02 (24.5%)

> "By the way, this was posted by an Iranian political leader." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:29 (1.4%)

> "Oh, and by the way, this was with the help of the Japanese government who's like subsidizing this, governments love microchips." — *Others (1x)*, `after/09-microchip-war` "USA vs China: The Microchip War" @ 8:55 (28.2%)

**Do.** Aside then return.

**Don't.** Do not chain asides.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.15/1k words; PASS if 0-1 per 1k words; it is optional (47% weighted coverage) — only use with a reason.


---

## O. Information density control

### A086. Plain-language gloss

**Definition.** "basically / in other words / which means".

**Detector.** regex `\b(basically|in other words|which means|that means|so,? essentially|in plain)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.0 | 15.4 |
| Gen (4x) | 8/10 | 0.69 | 23.9 |
| Especially (3x) | 2/3 | 0.34 | 32.8 |
| Oil (5x) | 1/1 | 4.13 | 5.2 |
| Others (1x) | 11/12 | 0.81 | 29.2 |
| **weighted** | 88% of weight | 0.95 | 19.5 |

**How each creator does it (verbatim):**

> "You basically have the same entity underneath, you're just asking it to show different sides of its personality." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 6:03 (15.4%)

> "Well, for several years now, there's basically been one recipe for training up in advanced cutting edge AI." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 2:20 (6.8%)

> "Everything is endto-end encrypted, which means only you and the person you're emailing can actually read it." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:33 (48.5%)

> "So AI spending, which means borrowed money, is what's growing the economy right now." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 6:13 (27.5%)

> "By 1881, railroads were basically the US stock market, 63% of the whole thing." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 7:59 (32.1%)

> "It's all one unified global market, which means all the world's producers sell into the same big supply, which all the world's consumers buy from." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:50 (5.2%)

> "The possibilities were endless, and the best part is that it would last forever because plastics basically last forever." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 3:56 (12.8%)

**Do.** Gloss after every dense line.

**Don't.** Do not gloss the obvious.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.95/1k words; PASS if ≥1 hit (corpus uses it in 88% of weighted videos) and rate ≤ 1.9/1k.

### A087. Analogy device

**Definition.** "It's like / think of it as".

**Detector.** regex `\b(it'?s like|think of (it|this)|kind of like|like a|imagine)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.71 | 13.0 |
| Gen (4x) | 10/10 | 1.02 | 21.1 |
| Especially (3x) | 3/3 | 0.81 | 36.1 |
| Oil (5x) | 1/1 | 0.33 | 50.8 |
| Others (1x) | 10/12 | 0.81 | 12.8 |
| **weighted** | 98% of weight | 0.87 | 13.1 |

**How each creator does it (verbatim):**

> "It was like a civil war within the company." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 5:14 (13.1%)

> "Hypothetically, as the hulking gay powerlifter, I'd scoop Will up like a featherweight, pin him against the wall with one meaty paw, rip off his policy wonk khakis." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 10:30 (26.7%)

> "were you like a social guy I was incredibly social um and and part of" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 7:33 (22.9%)

> "After buying enterprise AI licenses, Coinbase's CEO Brian Armstrong was told that adoption was going to take like a quarter or two." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 3:58 (19.3%)

> "I imagine these guys have to tell their wives this plan." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 17:06 (68.8%)

> "So it's like the shipping crunch took everything we talked about from the oil shock over here, and then doubled it, doubled the price spike, doubled the shortages, because countries can't get oil in time, or can't find spare ships, and it did something else, […]" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 18:01 (50.8%)

> "Summertime is more of a during the winter it's like almost like an engine trying to start." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 1:08 (3.7%)

**Do.** One analogy per concept.

**Don't.** Do not mix metaphors.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.87/1k words; PASS if ≥1 hit (corpus uses it in 98% of weighted videos) and rate ≤ 1.7/1k.

### A088. Recap micro-summary

**Definition.** "So, to recap / so basically / in short".

**Detector.** regex `\b(so,? to recap|so basically|in short|long story short|so,? again|to put it simply)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 38.9 |
| Gen (4x) | 4/10 | 0.12 | 40.9 |
| Especially (3x) | 1/3 | 0.07 | 42.8 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.02 | 27.6 |
| **weighted** | 27% of weight | 0.07 | 38.9 |

**How each creator does it (verbatim):**

> "And so basically, it tried to convince me to leave my wife and be with it, Bing Sydney." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 15:18 (38.9%)

> "So again, instead of betting on one provider, this empowers your own creativity, and so you control AI instead of AI controlling you." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 6:24 (38.7%)

> "preponderance of evidence to put it simply what this means is that unlike" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 14:12 (43.1%)

> "And in short, sending a signal back and forth will only take a few milliseconds." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:38 (42.8%)

> "So again, if you want to check it out, you can get $40 when you sign up and make your first purchase." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 7:31 (27.6%)

**Do.** Micro-recap before each new act.

**Don't.** Do not recap every minute.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.07/1k words; PASS if 0-1 per 1k words; it is optional (27% weighted coverage) — only use with a reason.

### A089. Definition on first use

**Definition.** "called / known as / what's called".

**Detector.** regex `\b(called|known as|what'?s called|stands for)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.77 | 7.9 |
| Gen (4x) | 10/10 | 0.71 | 22.0 |
| Especially (3x) | 3/3 | 0.47 | 30.8 |
| Oil (5x) | 1/1 | 0.83 | 14.8 |
| Others (1x) | 7/12 | 0.7 | 5.6 |
| **weighted** | 95% of weight | 0.75 | 13.1 |

**How each creator does it (verbatim):**

> "Murati had called them mere minutes before the public announcement went out." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 4:10 (10.4%)

> "But regardless, one of the main things we're baking in at this point is that the model should follow instructions from something called a system prompt." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 5:10 (13.1%)

> "I mean, it's literally called the Great Depression and ain't no other crash with a cool name like that." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 4:38 (20.8%)

> "in campus wise I had started a group called overheard at Yale it it was a" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 8:02 (24.4%)

> "And the MIT writing study we saw called this out as their most interesting result." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 13:18 (81.7%)

> "(tense piano music) There she is, runs East to West, and that's why it's called "The East-West Pipeline."" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 5:14 (14.8%)

> "This is Lowden County, Virginia, otherwise known as data center alley." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 1:42 (5.6%)

**Do.** Define jargon.

**Don't.** Do not define twice.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.75/1k words; PASS if ≥1 hit (corpus uses it in 95% of weighted videos) and rate ≤ 1.5/1k.


---

## P. Stakes for "you"

### A090. Personal consequence line

**Definition.** "you'll pay / your job / your money".

**Detector.** regex `\b(you'?ll|you will|you could|you might|you'?re going to)\b.*\b(pay|lose|job|money|afford|bill|price|future|life)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 2/10 | 0.07 | 5.4 |
| Especially (3x) | 2/3 | 0.2 | 50.6 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 4/12 | 0.11 | 40.3 |
| **weighted** | 18% of weight | 0.06 | 8.0 |

**How each creator does it (verbatim):**

> "Because maybe a crash will put everything on sale and just maybe you could actually afford it all again." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 0:37 (2.8%)

> "But no matter what they pick, there's one thing that you will lose either way." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 1:38 (8.0%)

> "Like using GPS every day in your own neighborhood, you'll lose the map in your head." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 13:50 (85.0%)

> "They can train an algorithm to charge you the maximum price they think you'll pay at any given moment." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 29:52 (89.5%)

**Do.** One personal consequence per act.

**Don't.** Do not threaten.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.06/1k words; PASS if 0-1 per 1k words; it is rare (18% weighted coverage) — only use with a reason.

### A091. Future-you projection

**Definition.** "In 5 years you…/ your kids".

**Detector.** regex `\b(your kids|your children|in (\d+|a few|ten|five) years|by 20\d\d)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.19 | 16.7 |
| Gen (4x) | 6/10 | 0.17 | 46.4 |
| Especially (3x) | 1/3 | 0.13 | 59.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 8/12 | 0.31 | 67.8 |
| **weighted** | 55% of weight | 0.18 | 33.8 |

**How each creator does it (verbatim):**

> "By 2003, he was convinced that if anyone succeeded in doing so, everyone on Earth would die." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:04 (0.2%)

> "You could parachute him into an island full of cannibals, come back in 5 years, and he'd be the king." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 29:04 (72.6%)

> "So all they really care about is whether Meta still exists in 10 years." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 5:27 (24.1%)

> "Home sales just hit their lowest level in 30 years." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 0:21 (1.5%)

> "By 2030, the US barely generates more." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 20:21 (59.0%)

> "By 2010, they're now getting a billion transistors onto a piece of silicon the size of your fingernail." — *Others (1x)*, `after/09-microchip-war` "USA vs China: The Microchip War" @ 13:40 (43.2%)

**Do.** Project the stakes forward.

**Don't.** Do not predict certainty.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.18/1k words; PASS if ≥1 hit (corpus uses it in 55% of weighted videos) and rate ≤ 1/1k.

### A092. Agency for you

**Definition.** "What you can do / you can".

**Detector.** regex `\b(what you can do|you can (help|do|join|call|sign|check|start)|get involved)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 98.4 |
| Gen (4x) | 4/10 | 0.1 | 31.3 |
| Especially (3x) | 1/3 | 0.07 | 47.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 4/12 | 0.15 | 27.9 |
| **weighted** | 30% of weight | 0.07 | 43.9 |

**How each creator does it (verbatim):**

> "If you work in policy, you can sign up for one-on-one advising with us." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 39:23 (98.4%)

> "But, where you get involved is that this whole bet is being funded with your retirement." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 1:05 (5.3%)

> "So anyways, even without that third criteria, you can start to see what private equity firms are looking for when they decide what channels to invest in." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 4:04 (18.7%)

> "Welcome to Wealthfront, a leading fintech platform to help manage and grow your money through sophisticated, easy to use products powerful products that let you be in control of your finances while handling the fine tuning you want but do not want to stress over, […]" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 11:41 (47.0%)

> "The more pulses of electricity you can control, the more you can do with technology." — *Others (1x)*, `after/09-microchip-war` "USA vs China: The Microchip War" @ 5:18 (16.8%)

**Do.** Give one concrete action.

**Don't.** Do not leave viewers helpless.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.07/1k words; PASS if 0-1 per 1k words; it is optional (30% weighted coverage) — only use with a reason.


---

## Q. Sponsor & mid-roll retention

### A093. Pre-sponsor cliffhanger

**Definition.** Question or "but" within 3 sentences before the sponsor block.

**Detector.** regex `\?$|^but\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 5.39 | 2.7 |
| Gen (4x) | 10/10 | 10.07 | 0.8 |
| Especially (3x) | 3/3 | 6.8 | 1.9 |
| Oil (5x) | 1/1 | 4.79 | 0.0 |
| Others (1x) | 12/12 | 8.11 | 1.6 |
| **weighted** | 100% of weight | 7.86 | 1.1 |

**How each creator does it (verbatim):**

> "But in fact, for those 16 hours, no one at the company could explain why their AI system was going rogue." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:23 (1.0%)

> "We've obviously been talking about AI for a while now as a society, but all of a sudden the questions are now, could this stuff actually kill me?" — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 0:00 (0.0%)

> "but just how you might doubt me saying that I also have doubts about Saif so" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 6:21 (19.3%)

> "But, with my new AI employee, he'll never complain, never take breaks, and most importantly, never ask me for a raise." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 0:12 (1.0%)

> "My first thought was, if you have this magic machine, what do you need me for?" — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:19 (1.9%)

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%)

> "Okay, am I crazy or is it really starting to smell a lot like robot apocalypse in here?" — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 0:00 (0.0%)

**Do.** Leave an open question right before the read.

**Don't.** Do not resolve the loop before the read.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 7.86/1k words; PASS if ≥1 hit (corpus uses it in 100% of weighted videos) and rate ≤ 15.7/1k.

### A094. Post-sponsor re-entry hook

**Definition.** "So back to it, because…" with a question.

**Detector.** regex `^(so,? )?back to (it|the)|^anyway\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 21.3 |
| Gen (4x) | 3/10 | 0.1 | 44.8 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.33 | 65.3 |
| Others (1x) | 3/12 | 0.09 | 84.5 |
| **weighted** | 27% of weight | 0.07 | 44.8 |

**How each creator does it (verbatim):**

> "Anyway, back to the scenario." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 7:16 (21.3%)

> "So back to it because a whole generation is now convinced that after each crash a bounce is guaranteed." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 9:59 (44.8%)

> "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:15 (45.5%)

> "Anyway, got a lot worse when our old pals, Iran and Saudi Arabia also got into a refinery war." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 23:10 (65.3%)

> "Anyway, Anthropic also points to their own constitution when asked about their trustworthiness." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 7:08 (50.4%)

**Do.** Re-enter with the loop you left open.

**Don't.** Do not re-enter with recap.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.07/1k words; PASS if 0-1 per 1k words; it is optional (27% weighted coverage) — only use with a reason.


---

## R. Comparative & contrast devices

### A095. Then-vs-now contrast

**Definition.** "Back in / used to / now".

**Detector.** regex `\b(used to|back in|years ago|nowadays|today,? )\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.58 | 14.0 |
| Gen (4x) | 10/10 | 0.95 | 33.0 |
| Especially (3x) | 3/3 | 1.28 | 4.9 |
| Oil (5x) | 1/1 | 0.83 | 6.4 |
| Others (1x) | 11/12 | 0.92 | 30.6 |
| **weighted** | 99% of weight | 0.82 | 18.9 |

**How each creator does it (verbatim):**

> "Same sort of reply you're probably used to if you chat with products like ChatGPT." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 2:22 (6.0%)

> "We used to build AI with rigid if-then rules that we fully understood." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 6:00 (14.0%)

> "And neither time did it end with this quick recovery that we all got used to." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 1:05 (4.9%)

> "That extra day that we used to give to make the videos better or cut." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 6:34 (30.2%)

> "You get bubbles, inflation, and you can look around right now and be like, that's today, right?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 9:24 (37.8%)

> "And if you didn't, I'm gonna try to TLDR you up to today in personal challenge here, 60 seconds." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:17 (6.4%)

> "It might not seem impressive today, but at the time, plastic was viewed like the material of the gods." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 2:12 (7.1%)

**Do.** Contrast past and present.

**Don't.** Do not over-romanticize the past.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.82/1k words; PASS if ≥1 hit (corpus uses it in 99% of weighted videos) and rate ≤ 1.6/1k.

### A096. Expectation-vs-reality

**Definition.** "You'd think / you'd expect / supposed to".

**Detector.** regex `\b(you'?d (think|expect|assume)|supposed to|on paper|in theory)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.65 | 18.4 |
| Gen (4x) | 7/10 | 0.36 | 59.0 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 6/12 | 0.22 | 32.3 |
| **weighted** | 61% of weight | 0.42 | 26.2 |

**How each creator does it (verbatim):**

> "And then you just continue on with your day because what else are you supposed to do?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 41:29 (96.8%)

> "Now, due to a previous scandal, Grok is supposed to have a 24/7 monitoring team." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 1:39 (4.2%)

> "We just spent this entire video on how on paper they seem to be like the biggest losers here." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 12:42 (62.4%)

> "Look, all that makes sense on paper, but underneath all of it is a hidden mechanism." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 0:35 (3.5%)

> "like its incredible ability to handle extremely high voltages, which could, in theory, mean really good diamond transistors." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 15:18 (92.1%)

**Do.** Set the expectation, break it.

**Don't.** Do not break it twice in one breath.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.42/1k words; PASS if ≥1 hit (corpus uses it in 61% of weighted videos) and rate ≤ 1/1k.

### A097. Binary choice framing

**Definition.** "Either… or / two options".

**Detector.** regex `\beither\b.*\bor\b|\btwo (options|choices|paths|possibilities)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 67.9 |
| Gen (4x) | 5/10 | 0.12 | 61.4 |
| Especially (3x) | 2/3 | 0.2 | 32.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 3/12 | 0.13 | 15.0 |
| **weighted** | 43% of weight | 0.1 | 61.3 |

**How each creator does it (verbatim):**

> "Either go do something on your own or continue with OpenAI as a nonprofit."" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 29:30 (75.0%)

> "We just knew it was either a hacker with a very, very automated process or system or most likely a fully, fully automated AI attack." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 19:57 (60.8%)

> "Either we own it outright 100% or a majority stake acquisition of 50 to 80% where the original creator remains." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:42 (40.0%)

> "To survive, they'll either need to pay the money back or get a new loan to replace the old one." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 10:26 (61.3%)

> "Either that or it might kill you." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 11:57 (34.7%)

> "These are the facilities either already built or approved for construction at the end of 2024." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 7:27 (24.4%)

**Do.** Use for scenario forks.

**Don't.** Do not make false binaries.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.1/1k words; PASS if 0-1 per 1k words; it is optional (43% weighted coverage) — only use with a reason.


---

## S. Viewer-role casting

### A098. Viewer as investor/owner

**Definition.** "If you own / your 401k / your stocks".

**Detector.** regex `\b(401\s?k|your (stocks?|portfolio|savings|retirement|investments?))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 5/10 | 0.17 | 59.3 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.02 | 93.5 |
| **weighted** | 21% of weight | 0.08 | 59.3 |

**How each creator does it (verbatim):**

> "But, where you get involved is that this whole bet is being funded with your retirement." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 1:05 (5.3%)

> "You too already should have a retirement fund like your 401k and it's buying the same stocks these pensions are." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 20:25 (90.2%)

> "No one wants to throttle a company whose value is tied to their 401k." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 13:14 (93.5%)

**Do.** Gen finance topics.

**Don't.** Do not give financial advice.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (21% weighted coverage) — only use with a reason.

### A099. Viewer as citizen

**Definition.** "Call your representative / vote / Congress".

**Detector.** regex `\b(congress|representative|senator|vote|lawmakers|policy|regulat\w*)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.52 | 34.8 |
| Gen (4x) | 5/10 | 0.33 | 49.6 |
| Especially (3x) | 2/3 | 0.13 | 54.8 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 6/12 | 0.44 | 50.8 |
| **weighted** | 59% of weight | 0.4 | 42.8 |

**How each creator does it (verbatim):**

> "Congress started asking questions, one of which was, any more of these rogue incidents y'all haven't told us about yet?" — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 24:41 (75.2%)

> "I don't think the Volkswagen Group is alive, but I do think it wants less regulation." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 14:36 (42.8%)

> "Department of Education to investigate Yale and they came up with a policy of" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 12:49 (38.9%)

> "Among the listeners who said podcast influenced their vote, 54% went for Trump." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 18:44 (86.2%)

> "And suddenly, all of these weird Electric States we just looked at—systems built differently, regulated differently, priced differently— have been dropped into the same experiment." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 27:41 (80.3%)

> "There were certainly some Democratic lawmakers who tried to unearth what was actually going on." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 8:53 (52.5%)

**Do.** Adam civic stakes.

**Don't.** Do not partisan-bait.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.4/1k words; PASS if ≥1 hit (corpus uses it in 59% of weighted videos) and rate ≤ 1/1k.

### A100. Viewer as consumer

**Definition.** "You're paying / your subscription".

**Detector.** regex `\byou'?re (paying|buying|using)|your (subscription|account|data|order)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 99.1 |
| Gen (4x) | 6/10 | 0.17 | 44.0 |
| Especially (3x) | 1/3 | 0.13 | 81.3 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.02 | 73.1 |
| **weighted** | 35% of weight | 0.1 | 46.5 |

**How each creator does it (verbatim):**

> "We don't sell your data or anything like that." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:28 (99.1%)

> "It's a private email service built on the idea that your data belongs to you and nobody else." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:06 (46.5%)

> "ProtonMail is a private encrypted alternative to services like Gmail, designed to give you more control over your data." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 9:56 (43.7%)

> "Launch the chips from Earth, catch the solar panels, attach them together, your data centers in space." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 20:12 (81.3%)

> "Doesn't the community have a right to say, hold on – [crosstalk] – before we say yes, tell us how much water you're using." — *Others (1x)*, `after/10-water` "We Calculated How Much Water Data Centers Actually Use. The " @ 9:43 (73.1%)

**Do.** Gen default casting.

**Don't.** Do not shame purchases.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.1/1k words; PASS if 0-1 per 1k words; it is optional (35% weighted coverage) — only use with a reason.


---

## T. Narrative suspense

### A101. Countdown/time pressure

**Definition.** "Within days / by Friday / 16 hours".

**Detector.** regex `\b(within (hours|days|weeks)|(\d+|sixteen|four) (hours|days)|by (monday|friday|the end))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.84 | 5.2 |
| Gen (4x) | 8/10 | 0.31 | 14.4 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.33 | 45.3 |
| Others (1x) | 5/12 | 0.13 | 69.0 |
| **weighted** | 69% of weight | 0.43 | 9.9 |

**How each creator does it (verbatim):**

> "They'll let their AI work for 16 hours straight, uninterrupted, at a cost of something like $10 million." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 4:14 (9.9%)

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%)

> "But by the end, I'll show you what you can take away from all of this." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 1:42 (8.4%)

> "But by the end, I'll show you the one thing that decides which side of it you end up on." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 1:34 (7.0%)

> "The dotted line shows the old route for oil, and it took 19 days to get from the Middle East to say, Taiwan or China." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 16:05 (45.3%)

> "But, in less than a year, the CEO had resigned, then the CFO followed 2 days later." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 22:23 (82.1%)

**Do.** Use real deadlines.

**Don't.** Do not invent urgency.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.43/1k words; PASS if ≥1 hit (corpus uses it in 69% of weighted videos) and rate ≤ 1/1k.

### A102. Cliffhanger "and then"

**Definition.** "And then… / And that's when".

**Detector.** regex `^(and then|and that'?s when|that'?s when|then,)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.77 | 10.7 |
| Gen (4x) | 7/10 | 0.24 | 37.9 |
| Especially (3x) | 2/3 | 0.13 | 76.9 |
| Oil (5x) | 1/1 | 0.5 | 8.1 |
| Others (1x) | 8/12 | 0.35 | 47.0 |
| **weighted** | 81% of weight | 0.45 | 27.1 |

**How each creator does it (verbatim):**

> "And then also, you know, so all these things interact and how do they interact?" — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 3:39 (10.7%)

> "And then, four days later, Sam Altman is apparently back as OpenAI CEO." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:13 (0.5%)

> "And that's when I realized I had to go all in because just buying one channel isn't the play." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 5:10 (23.8%)

> "And then we're going to skip all the way to the dot com crash which took seven." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 7:27 (33.4%)

> "And then when evaluators looked at the essays, the AI assisted essays were technically proficient, grammatically correct, structurally sound, but they were consistently described as hollow or soulless." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 9:07 (56.0%)

> "And then add on top of that emergency oil stockpiles that add back another two and a half million barrels." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:52 (8.1%)

> "And then if we overlay the map we've built, you can see the mega thirsty data centers moving in." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 18:32 (60.7%)

**Do.** Use at story peaks.

**Don't.** Do not drain with overuse.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.45/1k words; PASS if ≥1 hit (corpus uses it in 81% of weighted videos) and rate ≤ 1/1k.

### A103. Foreshadowing

**Definition.** "Little did / this would turn out / would later".

**Detector.** regex `\b(would (later|turn out|soon|eventually)|little did|this (would|will) (become|matter))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 18.4 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.02 | 20.6 |
| **weighted** | 15% of weight | 0.02 | 20.6 |

**How each creator does it (verbatim):**

> "Stancil would eventually report seeing hundreds of posts by Grok about himself." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 11:13 (28.5%)

> "It's the AI that would eventually power the first version of ChatGPT." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 2:52 (8.4%)

> "Lots of this action was happening right here in central California in a valley that would soon take on the name of the material that enabled all this magic to happen." — *Others (1x)*, `after/09-microchip-war` "USA vs China: The Microchip War" @ 6:30 (20.6%)

**Do.** Foreshadow once per act.

**Don't.** Do not spoil the reveal.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.02/1k words; PASS if 0-1 per 1k words; it is rare (15% weighted coverage) — only use with a reason.


---

## U. Empathy & tone

### A104. Validation line

**Definition.** "That makes sense / you can't blame".

**Detector.** regex `\b(that makes sense|you can'?t blame|it'?s (understandable|natural|fair))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 1.6 |
| Gen (4x) | 2/10 | 0.05 | 3.2 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 15% of weight | 0.04 | 2.9 |

**How each creator does it (verbatim):**

> "If you're wondering how we got here, that makes sense." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 0:32 (1.6%)

> "Look, all that makes sense on paper, but underneath all of it is a hidden mechanism." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 0:35 (3.5%)

> "And it's a natural cycle that when things get this bad, you can't blame people for wanting to get right back on the pirate ship." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:36 (2.9%)

**Do.** Validate before challenging.

**Don't.** Do not patronize.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.04/1k words; PASS if 0-1 per 1k words; it is rare (15% weighted coverage) — only use with a reason.

### A105. Reassurance

**Definition.** "Don't worry / not for you, at least for now".

**Detector.** regex `\b(don'?t worry|not (for )?you|at least for now|you'?re (fine|safe))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.1 | 70.3 |
| Gen (4x) | 2/10 | 0.05 | 45.6 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.33 | 24.9 |
| Others (1x) | 2/12 | 0.04 | 56.8 |
| **weighted** | 36% of weight | 0.08 | 70.3 |

**How each creator does it (verbatim):**

> "But as long as your AIs are good at following instructions, then you're fine." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 2:45 (8.4%)

> "They admitted that Grok's outputs were, quote, questionable, but basically said, don't worry, literally all of the AI systems that we're using are questionable." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 33:36 (85.5%)

> "No, like not for you, well, at least for now, but for the companies that make them because AI can now basically pirate them for free." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:01 (0.1%)

> "Well, at least for now." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 21:03 (91.1%)

> "(tense music) So three big pumping stations down, which means, (somber music) no more East-West pipeline, at least for now, and the world down five and a half million barrels, including a lot of that oil that would have gone to Europe." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 8:49 (24.9%)

> "To large water users like Meta, they're saying, “Don't worry, we have plenty of water.”" — *Others (1x)*, `after/10-water` "We Calculated How Much Water Data Centers Actually Use. The " @ 5:21 (40.3%)

**Do.** Calibrate fear down after a scare.

**Don't.** Do not dismiss real risk.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (36% weighted coverage) — only use with a reason.

### A106. Moral clarity line

**Definition.** "That's not okay / this is wrong".

**Detector.** regex `\b(that'?s (not okay|wrong|unacceptable)|this is (wrong|insane|unacceptable)|shouldn'?t be)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 91.5 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 3/12 | 0.13 | 33.2 |
| **weighted** | 10% of weight | 0.02 | 91.5 |

**How each creator does it (verbatim):**

> "I think that basically companies shouldn't be allowed to build superhuman AI systems, you know, super broadly superhuman super intelligence until they figure out how to make it safe." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 31:11 (91.5%)

> "Economic prosperity should be shared and this shouldn't be an arms race." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 4:30 (31.8%)

**Do.** One clear moral line.

**Don't.** Do not moralize repeatedly.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.02/1k words; PASS if 0-1 per 1k words; it is rare (10% weighted coverage) — only use with a reason.
