# Channel structure — 105 criteria (strategy, architecture, timing)

Every number below is **measured** from host-only transcript text by `build/` scripts. Weights are per video: Adam 7, Gen 4, oil 5, especially (spacex, ai-paradox, data-centers) 3, after/ 1. Especially 04/05/07 are deduplicated into Adam. "w-" = weighted across all 31 videos.

Quotes are verbatim (caption text, guest lines removed) and were machine-verified against the source files; `[…]` marks a cut. Detector = the regex/function used, so you can re-run it.

Columns: **cov** = videos with ≥1 hit / videos; **/1k** = hits per 1,000 host words; **first%** = median position of first hit.


---

## A. Length & runtime strategy

### S001. Runtime

**Definition.** Total runtime of the finished video.

**Detector.** function `dur_min` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 39.3 | 32.8 | 42.8 |
| Gen (4x) | 22.0 | 16.5 | 32.9 |
| Especially (3x) | 24.9 | 16.3 | 34.5 |
| Oil (5x) | 35.5 | 35.5 | 35.5 |
| Others (1x) | 17.2 | 13.3 | 33.4 |
| **weighted** | median 30.5 (IQR 20.5–35.5) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **39.3**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **42.8**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **20.4**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **21.7**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **24.9**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **35.5**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **30.5**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=39.3, `adam/02-bestselling-book`=42.8, `adam/03-no-longer-in-control`=32.8, `adam/04-superintelligence`=34.1, `adam/05-sam-altman`=40.0, `gen/1`=20.4, `gen/2`=21.7, `gen/3`=22.7, `gen/4`=20.5, `gen/5`=16.5, `gen/6`=22.3, `gen/7`=32.9, `gen/8`=23.1, `gen/9`=22.6, `gen/10`=17.0, `esp/01-spacex`=24.9, `esp/02-ai-paradox`=16.3, `esp/06-data-centers`=34.5, `esp/03-oil-apocalypse`=35.5, `after/01-dark-side-data-centers`=30.5, `after/02-greed`=33.4, `after/03-recycling`=30.8, `after/04-pov-ai`=17.6, `after/05-middle-class`=15.2, `after/06-diamonds`=16.6, `after/07-trump-family`=16.9, `after/08-tokens`=15.7, `after/09-microchip-war`=31.6, `after/10-water`=13.3, `after/11-anthropic-ipo`=14.2, `after/12-data-centres-not-working`=27.3

</details>

**Do.** Plan Adam-mode essays at 32-43 min; Gen-mode explainers at 16-23 min; mechanism explainers 16-35.

**Don't.** Do not pad a 20-min Gen topic to 40 min, or squeeze an Adam investigation into 15.

**Checklist test.** Compute `dur_min` on your outline/draft. PASS if inside the weighted IQR 20.5–35.5, or inside the chosen mode's min–max range (see table).

### S002. Total host words

**Definition.** Host-narration word count (guests removed).

**Detector.** function `words_total` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 6546 | 4742 | 7003 |
| Gen (4x) | 4298.0 | 3090 | 5857 |
| Especially (3x) | 5342 | 2340 | 7163 |
| Oil (5x) | 6054 | 6054 | 6054 |
| Others (1x) | 2846.0 | 2058 | 7085 |
| **weighted** | median 4742 (IQR 3892–6546) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **6664**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **7003**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **3892**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **4140**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **5342**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **6054**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **4305**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=6664, `adam/02-bestselling-book`=7003, `adam/03-no-longer-in-control`=4742, `adam/04-superintelligence`=6034, `adam/05-sam-altman`=6546, `gen/1`=3892, `gen/2`=4140, `gen/3`=4500, `gen/4`=3886, `gen/5`=3090, `gen/6`=4456, `gen/7`=5857, `gen/8`=4535, `gen/9`=4497, `gen/10`=3156, `esp/01-spacex`=5342, `esp/02-ai-paradox`=2340, `esp/06-data-centers`=7163, `esp/03-oil-apocalypse`=6054, `after/01-dark-side-data-centers`=4305, `after/02-greed`=6699, `after/03-recycling`=7085, `after/04-pov-ai`=2607, `after/05-middle-class`=2491, `after/06-diamonds`=2836, `after/07-trump-family`=2856, `after/08-tokens`=2277, `after/09-microchip-war`=5749, `after/10-water`=2058, `after/11-anthropic-ipo`=2237, `after/12-data-centres-not-working`=4647

</details>

**Do.** Budget words from runtime x WPM before outlining.

**Don't.** Do not count clip/guest audio as script words.

**Checklist test.** Compute `words_total` on your outline/draft. PASS if inside the weighted IQR 3892–6546, or inside the chosen mode's min–max range (see table).

### S003. Narration pace (WPM)

**Definition.** Host words per minute of runtime; lower = more clips/b-roll breathing room.

**Detector.** function `wpm` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 164 | 144 | 177 |
| Gen (4x) | 190.5 | 178 | 200 |
| Especially (3x) | 208 | 144 | 215 |
| Oil (5x) | 171 | 171 | 171 |
| Others (1x) | 166.5 | 141 | 230 |
| **weighted** | median 177 (IQR 164–191) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **169**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **163**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **191**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **190**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **215**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **171**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **141**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=169, `adam/02-bestselling-book`=163, `adam/03-no-longer-in-control`=144, `adam/04-superintelligence`=177, `adam/05-sam-altman`=164, `gen/1`=191, `gen/2`=190, `gen/3`=198, `gen/4`=189, `gen/5`=187, `gen/6`=200, `gen/7`=178, `gen/8`=196, `gen/9`=199, `gen/10`=185, `esp/01-spacex`=215, `esp/02-ai-paradox`=144, `esp/06-data-centers`=208, `esp/03-oil-apocalypse`=171, `after/01-dark-side-data-centers`=141, `after/02-greed`=201, `after/03-recycling`=230, `after/04-pov-ai`=148, `after/05-middle-class`=164, `after/06-diamonds`=171, `after/07-trump-family`=169, `after/08-tokens`=145, `after/09-microchip-war`=182, `after/10-water`=155, `after/11-anthropic-ipo`=158, `after/12-data-centres-not-working`=170

</details>

**Do.** Adam 144-177 WPM (clip pauses); Gen 178-200 WPM; especially up to 215.

**Don't.** Do not write at 220+ WPM; it will not fit.

**Checklist test.** Compute `wpm` on your outline/draft. PASS if inside the weighted IQR 164–191, or inside the chosen mode's min–max range (see table).

### S004. Mean sentence length

**Definition.** Average words per host sentence across the video.

**Detector.** function `mean_sent_words` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 15.5 | 13.0 | 17.2 |
| Gen (4x) | 16.8 | 14.2 | 18.4 |
| Especially (3x) | 13.7 | 11.5 | 14.1 |
| Oil (5x) | 17.2 | 17.2 | 17.2 |
| Others (1x) | 14.6 | 7.4 | 17.5 |
| **weighted** | median 15.9 (IQR 14.3–17.2) | | |

**How each creator does it (verbatim anchor lines):**

> "Musk pops up in a few other places on X at the same time." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 17:54 (45.5%) — value here: **16.2**

> "And then at the first moment it was technologically feasible, we invented birth control." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 19:41 (46.0%) — value here: **14.9**

> "And the reason why is that in about 2 months, they were able to vibe code its own Salesforce version just by telling AI what they wanted." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 10:14 (50.3%) — value here: **17.8**

> "Okay, but why do we do that?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:57 (41.2%) — value here: **16.2**

> "Pulled on by just enough of Earth's gravity." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 13:17 (53.5%) — value here: **13.7**

> "(tense orchestral music) So here again, here's that route, and this is crazy." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 16:28 (46.4%) — value here: **17.2**

> "Only then do you realize that hidden behind the drone of the data centers, there is bird song about 20 mi south in Manasses, Virginia." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 14:13 (46.6%) — value here: **14.9**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=16.2, `adam/02-bestselling-book`=14.9, `adam/03-no-longer-in-control`=15.5, `adam/04-superintelligence`=17.2, `adam/05-sam-altman`=13.0, `gen/1`=17.8, `gen/2`=16.2, `gen/3`=18.1, `gen/4`=16.8, `gen/5`=18.4, `gen/6`=17.5, `gen/7`=14.3, `gen/8`=15.9, `gen/9`=16.8, `gen/10`=14.2, `esp/01-spacex`=13.7, `esp/02-ai-paradox`=11.5, `esp/06-data-centers`=14.1, `esp/03-oil-apocalypse`=17.2, `after/01-dark-side-data-centers`=14.9, `after/02-greed`=16.0, `after/03-recycling`=12.8, `after/04-pov-ai`=7.4, `after/05-middle-class`=17.5, `after/06-diamonds`=11.7, `after/07-trump-family`=16.2, `after/08-tokens`=13.5, `after/09-microchip-war`=15.8, `after/10-water`=13.5, `after/11-anthropic-ipo`=14.4, `after/12-data-centres-not-working`=14.8

</details>

**Do.** Keep the mean near the group norm; vary within it.

**Don't.** Do not write uniform 25-word sentences.

**Checklist test.** Compute `mean_sent_words` on your outline/draft. PASS if inside the weighted IQR 14.3–17.2, or inside the chosen mode's min–max range (see table).

### S005. Hook sentence length

**Definition.** Average sentence length inside the cold open (to the promise).

**Detector.** function `hook_sent_words` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 14.1 | 7.0 | 19.1 |
| Gen (4x) | 15.3 | 7.9 | 17.8 |
| Especially (3x) | 16.6 | 9.7 | 18.1 |
| Oil (5x) | 13.6 | 13.6 | 13.6 |
| Others (1x) | 14.2 | 8.6 | 18.6 |
| **weighted** | median 15.1 (IQR 13.6–17.5) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **18.0**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **13.9**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **16.2**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **17.8**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **16.6**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **13.6**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **13.2**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=18.0, `adam/02-bestselling-book`=13.9, `adam/03-no-longer-in-control`=14.1, `adam/04-superintelligence`=19.1, `adam/05-sam-altman`=7.0, `gen/1`=16.2, `gen/2`=17.8, `gen/3`=11.1, `gen/4`=15.5, `gen/5`=17.5, `gen/6`=17.0, `gen/7`=14.8, `gen/8`=15.1, `gen/9`=7.9, `gen/10`=15.1, `esp/01-spacex`=16.6, `esp/02-ai-paradox`=9.7, `esp/06-data-centers`=18.1, `esp/03-oil-apocalypse`=13.6, `after/01-dark-side-data-centers`=13.2, `after/02-greed`=13.0, `after/03-recycling`=18.3, `after/04-pov-ai`=8.6, `after/05-middle-class`=17.1, `after/06-diamonds`=18.6, `after/07-trump-family`=15.2, `after/08-tokens`=9.9, `after/09-microchip-war`=14.9, `after/10-water`=14.9, `after/11-anthropic-ipo`=13.6, `after/12-data-centres-not-working`=13.6

</details>

**Do.** Hook sentences run shorter or equal to body sentences.

**Don't.** Do not open with a 40-word paragraph sentence.

**Checklist test.** Compute `hook_sent_words` on your outline/draft. PASS if inside the weighted IQR 13.6–17.5, or inside the chosen mode's min–max range (see table).

### S006. Closing sentence length

**Definition.** Average sentence length in final 10%.

**Detector.** function `end_sent_words` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 14.1 | 12.6 | 21.5 |
| Gen (4x) | 18.9 | 14.1 | 22.7 |
| Especially (3x) | 13.3 | 13.2 | 16.5 |
| Oil (5x) | 16.8 | 16.8 | 16.8 |
| Others (1x) | 13.3 | 8.5 | 20.2 |
| **weighted** | median 16.5 (IQR 13.9–19.4) | | |

**How each creator does it (verbatim anchor lines):**

> "Thank you so much for watching and see you in the next one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 39:16 (99.9%) — value here: **21.5**

> "We'll see you in the next one." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:47 (99.9%) — value here: **13.9**

> "But if you'd rather see another video on getting the truth of what's really happening with AI, you will want to watch this one next." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 20:13 (99.3%) — value here: **17.0**

> "Yeah." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 21:41 (99.8%) — value here: **18.5**

> "See you." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 24:47 (99.7%) — value here: **13.2**

> "(somber piano music) (somber piano music ending)" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 35:01 (98.7%) — value here: **16.8**

> "Heat." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 30:21 (99.4%) — value here: **16.1**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=21.5, `adam/02-bestselling-book`=13.9, `adam/03-no-longer-in-control`=12.6, `adam/04-superintelligence`=18.9, `adam/05-sam-altman`=14.1, `gen/1`=17.0, `gen/2`=18.5, `gen/3`=20.5, `gen/4`=21.2, `gen/5`=19.9, `gen/6`=15.6, `gen/7`=14.6, `gen/8`=22.7, `gen/9`=19.4, `gen/10`=14.1, `esp/01-spacex`=13.2, `esp/02-ai-paradox`=16.5, `esp/06-data-centers`=13.3, `esp/03-oil-apocalypse`=16.8, `after/01-dark-side-data-centers`=16.1, `after/02-greed`=20.2, `after/03-recycling`=12.6, `after/04-pov-ai`=8.5, `after/05-middle-class`=19.3, `after/06-diamonds`=13.4, `after/07-trump-family`=20.1, `after/08-tokens`=13.1, `after/09-microchip-war`=14.8, `after/10-water`=13.2, `after/11-anthropic-ipo`=11.4, `after/12-data-centres-not-working`=12.1

</details>

**Do.** Shorten sentences as you land.

**Don't.** Do not end on a long caveat chain.

**Checklist test.** Compute `end_sent_words` on your outline/draft. PASS if inside the weighted IQR 13.9–19.4, or inside the chosen mode's min–max range (see table).

### S007. Words per section

**Definition.** Host words divided by section count (pacing budget per act).

**Detector.** function `section_gap_pct` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 11.4 | 10.0 | 13.3 |
| Gen (4x) | 12.4 | 8.9 | 40.0 |
| Especially (3x) | 10.0 | 8.9 | 16.0 |
| Oil (5x) | 11.4 | 11.4 | 11.4 |
| Others (1x) | 14.7 | 8.9 | 40.0 |
| **weighted** | median 11.4 (IQR 10.0–13.3) | | |

**How each creator does it (verbatim anchor lines):**

> "Now go forth and dismantle the illusions of the weak-minded." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 12:39 (32.2%) — value here: **11.4**

> "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:28 (47.8%) — value here: **10.0**

> "So what we're seeing here is that just like the store brand, the free copy sort of acts as like a thing that keeps prices down for anyone who can switch." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 11:44 (57.7%) — value here: **13.3**

> "So a few years pass and now my boomer boss is happy and he can't stop bragging to his friends about how much money he's making from this site called YouTube." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 6:10 (28.4%) — value here: **13.3**

> "So they kidnaped three guys off the street and made them do it." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 18:29 (74.4%) — value here: **10.0**

> "So everything I've shown you so far tracks how the oil shock over there, plus a shipping shock right here leads to crazy prices and shortages by the time it gets to the refinery." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 21:24 (60.3%) — value here: **11.4**

> "So farmers are watching the data center campuses emerging to the south of Cheyenne and getting nervous." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 11:47 (38.6%) — value here: **13.3**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=11.4, `adam/02-bestselling-book`=10.0, `adam/03-no-longer-in-control`=10.0, `adam/04-superintelligence`=11.4, `adam/05-sam-altman`=13.3, `gen/1`=13.3, `gen/2`=13.3, `gen/3`=16.0, `gen/4`=11.4, `gen/5`=16.0, `gen/6`=11.4, `gen/7`=40.0, `gen/8`=8.9, `gen/9`=8.9, `gen/10`=10.0, `esp/01-spacex`=10.0, `esp/02-ai-paradox`=16.0, `esp/06-data-centers`=8.9, `esp/03-oil-apocalypse`=11.4, `after/01-dark-side-data-centers`=13.3, `after/02-greed`=11.4, `after/03-recycling`=8.9, `after/04-pov-ai`=16.0, `after/05-middle-class`=40.0, `after/06-diamonds`=16.0, `after/07-trump-family`=13.3, `after/08-tokens`=20.0, `after/09-microchip-war`=11.4, `after/10-water`=20.0, `after/11-anthropic-ipo`=20.0, `after/12-data-centres-not-working`=10.0

</details>

**Do.** Target one major turn every ~6-12% of runtime.

**Don't.** Do not run 25% of runtime with no turn.

**Checklist test.** Compute `section_gap_pct` on your outline/draft. PASS if inside the weighted IQR 10.0–13.3, or inside the chosen mode's min–max range (see table).


---

## B. Cold open / hook

### S008. Hook length (seconds)

**Definition.** Seconds from 0:00 to the first explicit promise/roadmap line.

**Detector.** function `hook_sec` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 64 | 12 | 127 |
| Gen (4x) | 84.5 | 17 | 222 |
| Especially (3x) | 91 | 61 | 126 |
| Oil (5x) | 95 | 95 | 95 |
| Others (1x) | 87.5 | 8 | 135 |
| **weighted** | median 79 (IQR 40–95) | | |

**How each creator does it (verbatim anchor lines):**

> "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:29 (1.2%) — value here: **29**

> "I want to take you through that story." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 1:04 (2.5%) — value here: **64**

> "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:17 (1.4%) — value here: **17**

> "So to understand this whole thing, I think the best way is by showing you how a private equity firm even buys a YouTube channel." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 1:35 (7.3%) — value here: **95**

> "15 times that ship stopped, refused, and slowly made its way home." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 1:31 (6.1%) — value here: **91**

> "So let's get into it." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:35 (4.5%) — value here: **95**

> "These are Amazon data centers." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 1:52 (6.1%) — value here: **112**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=29, `adam/02-bestselling-book`=64, `adam/03-no-longer-in-control`=127, `adam/04-superintelligence`=79, `adam/05-sam-altman`=12, `gen/1`=17, `gen/2`=95, `gen/3`=85, `gen/4`=121, `gen/5`=86, `gen/6`=222, `gen/7`=33, `gen/8`=84, `gen/9`=40, `gen/10`=61, `esp/01-spacex`=91, `esp/02-ai-paradox`=61, `esp/06-data-centers`=126, `esp/03-oil-apocalypse`=95, `after/01-dark-side-data-centers`=112, `after/02-greed`=121, `after/03-recycling`=8, `after/04-pov-ai`=19, `after/05-middle-class`=55, `after/06-diamonds`=45, `after/07-trump-family`=127, `after/08-tokens`=63, `after/09-microchip-war`=121, `after/10-water`=49, `after/11-anthropic-ipo`=135, `after/12-data-centres-not-working`=129

</details>

**Do.** Land the promise by ~0:15-1:35; Adam 0:12-2:07.

**Don't.** Do not delay the promise past ~2:15.

**Checklist test.** Compute `hook_sec` on your outline/draft. PASS if inside the weighted IQR 40–95, or inside the chosen mode's min–max range (see table).

### S009. Hook length (words)

**Definition.** Host words before the promise line.

**Detector.** function `hook_words` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 186 | 19 | 250 |
| Gen (4x) | 266.0 | 65 | 688 |
| Especially (3x) | 337 | 145 | 411 |
| Oil (5x) | 281 | 281 | 281 |
| Others (1x) | 216.0 | 48 | 453 |
| **weighted** | median 225 (IQR 121–281) | | |

**How each creator does it (verbatim anchor lines):**

> "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:29 (1.2%) — value here: **84**

> "I want to take you through that story." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 1:04 (2.5%) — value here: **186**

> "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:17 (1.4%) — value here: **65**

> "So to understand this whole thing, I think the best way is by showing you how a private equity firm even buys a YouTube channel." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 1:35 (7.3%) — value here: **296**

> "15 times that ship stopped, refused, and slowly made its way home." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 1:31 (6.1%) — value here: **337**

> "So let's get into it." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:35 (4.5%) — value here: **281**

> "These are Amazon data centers." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 1:52 (6.1%) — value here: **273**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=84, `adam/02-bestselling-book`=186, `adam/03-no-longer-in-control`=250, `adam/04-superintelligence`=225, `adam/05-sam-altman`=19, `gen/1`=65, `gen/2`=296, `gen/3`=262, `gen/4`=383, `gen/5`=273, `gen/6`=688, `gen/7`=101, `gen/8`=270, `gen/9`=121, `gen/10`=131, `esp/01-spacex`=337, `esp/02-ai-paradox`=145, `esp/06-data-centers`=411, `esp/03-oil-apocalypse`=281, `after/01-dark-side-data-centers`=273, `after/02-greed`=453, `after/03-recycling`=49, `after/04-pov-ai`=48, `after/05-middle-class`=159, `after/06-diamonds`=116, `after/07-trump-family`=365, `after/08-tokens`=139, `after/09-microchip-war`=326, `after/10-water`=154, `after/11-anthropic-ipo`=384, `after/12-data-centres-not-working`=377

</details>

**Do.** Adam 19-250 words (median 186); Gen 65-688 (median 266); especially 145-411.

**Don't.** Do not exceed ~400 words before telling viewers what they get.

**Checklist test.** Compute `hook_words` on your outline/draft. PASS if inside the weighted IQR 121–281, or inside the chosen mode's min–max range (see table).

### S010. Hook as % of runtime

**Definition.** Promise position as % of runtime.

**Detector.** function `hook_pct` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 2.5 | 0.5 | 6.4 |
| Gen (4x) | 6.2 | 1.4 | 16.6 |
| Especially (3x) | 6.1 | 6.1 | 6.2 |
| Oil (5x) | 4.5 | 4.5 | 4.5 |
| Others (1x) | 6.1 | 0.4 | 15.9 |
| **weighted** | median 6.0 (IQR 2.5–6.4) | | |

**How each creator does it (verbatim anchor lines):**

> "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:29 (1.2%) — value here: **1.2**

> "I want to take you through that story." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 1:04 (2.5%) — value here: **2.5**

> "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:17 (1.4%) — value here: **1.4**

> "So to understand this whole thing, I think the best way is by showing you how a private equity firm even buys a YouTube channel." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 1:35 (7.3%) — value here: **7.3**

> "15 times that ship stopped, refused, and slowly made its way home." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 1:31 (6.1%) — value here: **6.1**

> "So let's get into it." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:35 (4.5%) — value here: **4.5**

> "These are Amazon data centers." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 1:52 (6.1%) — value here: **6.1**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=1.2, `adam/02-bestselling-book`=2.5, `adam/03-no-longer-in-control`=6.4, `adam/04-superintelligence`=3.9, `adam/05-sam-altman`=0.5, `gen/1`=1.4, `gen/2`=7.3, `gen/3`=6.2, `gen/4`=9.8, `gen/5`=8.7, `gen/6`=16.6, `gen/7`=1.7, `gen/8`=6.1, `gen/9`=2.9, `gen/10`=6.0, `esp/01-spacex`=6.1, `esp/02-ai-paradox`=6.2, `esp/06-data-centers`=6.1, `esp/03-oil-apocalypse`=4.5, `after/01-dark-side-data-centers`=6.1, `after/02-greed`=6.0, `after/03-recycling`=0.4, `after/04-pov-ai`=1.8, `after/05-middle-class`=6.0, `after/06-diamonds`=4.5, `after/07-trump-family`=12.5, `after/08-tokens`=6.7, `after/09-microchip-war`=6.4, `after/10-water`=6.1, `after/11-anthropic-ipo`=15.9, `after/12-data-centres-not-working`=7.9

</details>

**Do.** Promise inside the first ~1-8%.

**Don't.** Do not put the promise after 10%.

**Checklist test.** Compute `hook_pct` on your outline/draft. PASS if inside the weighted IQR 2.5–6.4, or inside the chosen mode's min–max range (see table).

### S011. First sentence length

**Definition.** Word count of sentence one.

**Detector.** function `first_sentence_words` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 16 | 5 | 26 |
| Gen (4x) | 10.0 | 6 | 14 |
| Especially (3x) | 19 | 11 | 29 |
| Oil (5x) | 14 | 14 | 14 |
| Others (1x) | 12.5 | 1 | 36 |
| **weighted** | median 13 (IQR 9–16) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **21**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **26**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **9**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **11**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **29**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **14**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **13**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=21, `adam/02-bestselling-book`=26, `adam/03-no-longer-in-control`=5, `adam/04-superintelligence`=16, `adam/05-sam-altman`=13, `gen/1`=9, `gen/2`=11, `gen/3`=6, `gen/4`=12, `gen/5`=8, `gen/6`=14, `gen/7`=14, `gen/8`=10, `gen/9`=9, `gen/10`=10, `esp/01-spacex`=29, `esp/02-ai-paradox`=19, `esp/06-data-centers`=11, `esp/03-oil-apocalypse`=14, `after/01-dark-side-data-centers`=13, `after/02-greed`=21, `after/03-recycling`=36, `after/04-pov-ai`=12, `after/05-middle-class`=12, `after/06-diamonds`=15, `after/07-trump-family`=11, `after/08-tokens`=5, `after/09-microchip-war`=8, `after/10-water`=18, `after/11-anthropic-ipo`=18, `after/12-data-centres-not-working`=1

</details>

**Do.** Sentence one is short and concrete (5-20 words).

**Don't.** Do not begin with throat-clearing or a greeting (except a deliberate show-format open).

**Checklist test.** Compute `first_sentence_words` on your outline/draft. PASS if inside the weighted IQR 9–16, or inside the chosen mode's min–max range (see table).

### S012. Dated-event open

**Definition.** Opening on an exact date/time/duration.

**Detector.** regex `\b(on (monday|tuesday|wednesday|thursday|friday|saturday|sunday|january|february|march|april|may|june|july|august|september|october|november|december)|in the year \d{4}|for \d+ hours|in (19|20)\d\d)\b` in scope `hook`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.23 | 0.0 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 3/12 | 0.09 | 2.8 |
| **weighted** | 31% of weight | 0.08 | 0.0 |

**How each creator does it (verbatim):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%)

> "On November 17th, 2023, Sam Altman, wildly successful CEO of OpenAI, was fired." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:00 (0.0%)

> "But, in 1933, British company Imperial Chemical Industries, great name, accidentally discovered a way to synthesize this industrially." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 1:56 (6.3%)

**Do.** Use a dated event when the story is a news incident (Adam default).

**Don't.** Do not fake a date for an evergreen topic.

**Checklist test.** In scope `hook`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (31% weighted coverage) — only use with a reason.

### S013. Number-first open

**Definition.** A statistic or figure in the first 8%.

**Detector.** regex `\d|\b(million|billion|trillion|percent)\b` in scope `hook`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.97 | 0.0 |
| Gen (4x) | 9/10 | 0.76 | 0.8 |
| Especially (3x) | 3/3 | 1.01 | 0.0 |
| Oil (5x) | 1/1 | 0.83 | 5.6 |
| Others (1x) | 8/12 | 0.72 | 0.0 |
| **weighted** | 92% of weight | 0.84 | 0.5 |

**How each creator does it (verbatim):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%)

> "At least 1,200 AI agents somehow escaped a secure internal testing environment at OpenAI." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 0:45 (2.3%)

> "One guy just used AI to make free copies of Photoshop and Word in 2 weeks." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:08 (0.7%)

> "It turns out it's not slowing down because private equity firms have quietly spent over $4 billion buying YouTube channels." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:32 (2.5%)

> "An acre of land is 66 feet across, 660 feet long." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:01 (0.0%)

> "Any given day, there are about 100 million barrels produced, and 100 million barrels consumed." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:00 (5.6%)

> "I feel like for the past 3 years, I've heard over and over again that a recession is about to hit." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 0:00 (0.0%)

**Do.** Drop one surprising, sourced number early.

**Don't.** Do not stack 5 numbers before the viewer knows the topic.

**Checklist test.** In scope `hook`, count sentences matching the detector. Weighted norm ≈ 0.84/1k words; PASS if ≥1 hit (corpus uses it in 92% of weighted videos) and rate ≤ 1.7/1k.

### S014. Second-person scene open

**Definition.** Opening that puts the viewer in a scene ("Take a look at…", "Think about…", "let's buy a house together").

**Detector.** regex `^(so,? )?(take a look|think about|imagine|picture|let'?s|come with me|you'?ve probably|when you hear|you)` in scope `hook`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.13 | 1.8 |
| Gen (4x) | 7/10 | 0.31 | 0.0 |
| Especially (3x) | 1/3 | 0.2 | 6.9 |
| Oil (5x) | 1/1 | 0.33 | 4.5 |
| Others (1x) | 6/12 | 0.41 | 2.2 |
| **weighted** | 62% of weight | 0.26 | 0.8 |

**How each creator does it (verbatim):**

> "You may know that Elon Musk is not a fan of wokeness." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 2:57 (7.5%)

> "You've said AI could wipe out half of all entry-level white-collar jobs and spike unemployment to 10 to 20% in the next 1 to 5 years." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:44 (1.8%)

> "When you hear of a stock market crash, you probably picture something like this." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 0:00 (0.0%)

> "So, come with me, you guys, to replace my employee with AI." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 0:00 (0.0%)

> "You weren't allowed to use them for business." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 2:23 (6.9%)

> "So let's get into it." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:35 (4.5%)

> "You didn't need to have some genius level of foresight to be able to do that." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 1:07 (3.3%)

**Do.** Gen default: start inside the viewer's life.

**Don't.** Do not use "imagine" for a news incident that is stranger than fiction.

**Checklist test.** In scope `hook`, count sentences matching the detector. Weighted norm ≈ 0.26/1k words; PASS if ≥1 hit (corpus uses it in 62% of weighted videos) and rate ≤ 1/1k.

### S015. Mood/scene line open

**Definition.** Short atmospheric line ("It was a strange summer.").

**Detector.** regex `^(it was|this is|there'?s|there is|there was)\b.{0,40}$` in scope `hook`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.1 | 0.8 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 2/3 | 0.13 | 4.2 |
| Oil (5x) | 1/1 | 0.17 | 5.1 |
| Others (1x) | 1/12 | 0.02 | 2.3 |
| **weighted** | 33% of weight | 0.06 | 1.0 |

**How each creator does it (verbatim):**

> "There is a 1-4% chance everybody dies." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:21 (0.8%)

> "This is from the previous day." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 2:22 (6.0%)

> "It was the sails on the ships." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 1:49 (7.3%)

> "This is the world oil economy." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:49 (5.1%)

> "This is the best the economy has ever been." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 0:46 (2.3%)

**Do.** Use one short mood line, then hard facts.

**Don't.** Do not stack mood lines.

**Checklist test.** In scope `hook`, count sentences matching the detector. Weighted norm ≈ 0.06/1k words; PASS if 0-1 per 1k words; it is optional (33% weighted coverage) — only use with a reason.

### S016. Contradiction hook

**Definition.** A "but" twist inside the hook that reverses the expectation.

**Detector.** regex `^but\b|\bbut (what|in fact|the|it|here|that|no one|nobody)\b` in scope `hook`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.13 | 4.5 |
| Gen (4x) | 9/10 | 0.67 | 1.8 |
| Especially (3x) | 2/3 | 0.27 | 0.4 |
| Oil (5x) | 1/1 | 0.17 | 1.6 |
| Others (1x) | 9/12 | 0.57 | 2.6 |
| **weighted** | 76% of weight | 0.42 | 1.8 |

**How each creator does it (verbatim):**

> "But in fact, for those 16 hours, no one at the company could explain why their AI system was going rogue." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:23 (1.0%)

> "But most of that is actually tool AI." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 1:33 (4.5%)

> "But how if most are getting canceled, then the land should be free, and the workers should be back?" — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 0:28 (2.8%)

> "But right now, the same pattern that showed up before that crash and before the dot-com crash is back." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 0:58 (4.3%)

> "But choose to use that acre instead for an AI data center." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:16 (0.8%)

> "But I have to be honest, this oil shock, it is different from the one that we warned you about, because it's actually, and I can hardly believe this, three oil shocks hitting at once." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:34 (1.6%)

> "So microchips make our economy possible, but it's not just tech, it's not just the consumer tech." — *Others (1x)*, `after/09-microchip-war` "USA vs China: The Microchip War" @ 2:01 (6.4%)

**Do.** Twist within 30 seconds.

**Don't.** Do not deliver a hook with no reversal.

**Checklist test.** In scope `hook`, count sentences matching the detector. Weighted norm ≈ 0.42/1k words; PASS if ≥1 hit (corpus uses it in 76% of weighted videos) and rate ≤ 1/1k.

### S017. "No one is talking about" gap

**Definition.** Explicit claim the angle is under-reported.

**Detector.** regex `\b(no one|nobody) (is|has been|seems to be) (talking|telling|asking|reporting)|haven'?t seen reported|no one has told you|not telling you\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 1.2 |
| Gen (4x) | 1/10 | 0.02 | 1.4 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 11% of weight | 0.02 | 1.2 |

**How each creator does it (verbatim):**

> "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:29 (1.2%)

> "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:17 (1.4%)

**Do.** Use once, backed by a real under-covered fact.

**Don't.** Do not claim exclusivity you cannot back.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.02/1k words; PASS if 0-1 per 1k words; it is rare (11% weighted coverage) — only use with a reason.

### S018. Hook question

**Definition.** A direct question in the first 8%.

**Detector.** regex `\?$` in scope `hook`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.32 | 3.0 |
| Gen (4x) | 9/10 | 0.76 | 0.8 |
| Especially (3x) | 2/3 | 0.27 | 3.8 |
| Oil (5x) | 1/1 | 0.66 | 0.0 |
| Others (1x) | 8/12 | 0.41 | 1.6 |
| **weighted** | 89% of weight | 0.56 | 1.6 |

**How each creator does it (verbatim):**

> "We've obviously been talking about AI for a while now as a society, but all of a sudden the questions are now, could this stuff actually kill me?" — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 0:00 (0.0%)

> "If someone builds it, does everyone die?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 1:10 (2.7%)

> "So then, months later, why the hell am I paying for this thing more than I ever paid Jason?" — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 0:20 (1.6%)

> "I wake up every single night thinking, "What could I have done differently?" — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 0:27 (2.6%)

> "My first thought was, if you have this magic machine, what do you need me for?" — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:19 (1.9%)

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%)

> "Okay, am I crazy or is it really starting to smell a lot like robot apocalypse in here?" — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 0:00 (0.0%)

**Do.** End the hook on a question the video answers.

**Don't.** Do not ask three questions in a row with no anchor.

**Checklist test.** In scope `hook`, count sentences matching the detector. Weighted norm ≈ 0.56/1k words; PASS if ≥1 hit (corpus uses it in 89% of weighted videos) and rate ≤ 1.1/1k.

### S019. Questions per minute in opening

**Definition.** Question density in first 10%.

**Detector.** function `q_per_min_open` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.6 | 0.2 | 0.8 |
| Gen (4x) | 1.4 | 0.0 | 3.5 |
| Especially (3x) | 0.6 | 0.4 | 1.2 |
| Oil (5x) | 1.4 | 1.4 | 1.4 |
| Others (1x) | 0.9 | 0.0 | 3.8 |
| **weighted** | median 0.8 (IQR 0.4–1.41) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **0.25**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **0.7**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **1.47**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **0.92**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **0.4**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **1.41**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **0.33**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0.25, `adam/02-bestselling-book`=0.7, `adam/03-no-longer-in-control`=0.61, `adam/04-superintelligence`=0.29, `adam/05-sam-altman`=0.75, `gen/1`=1.47, `gen/2`=0.92, `gen/3`=3.52, `gen/4`=2.92, `gen/5`=1.21, `gen/6`=0.45, `gen/7`=0.0, `gen/8`=1.3, `gen/9`=2.21, `gen/10`=2.94, `esp/01-spacex`=0.4, `esp/02-ai-paradox`=1.23, `esp/06-data-centers`=0.58, `esp/03-oil-apocalypse`=1.41, `after/01-dark-side-data-centers`=0.33, `after/02-greed`=1.2, `after/03-recycling`=0.65, `after/04-pov-ai`=1.7, `after/05-middle-class`=0.0, `after/06-diamonds`=0.0, `after/07-trump-family`=0.0, `after/08-tokens`=1.28, `after/09-microchip-war`=0.0, `after/10-water`=3.76, `after/11-anthropic-ipo`=1.41, `after/12-data-centres-not-working`=1.47

</details>

**Do.** Front-load questions more than mid-video.

**Don't.** Do not leave the open as pure statement.

**Checklist test.** Compute `q_per_min_open` on your outline/draft. PASS if inside the weighted IQR 0.4–1.41, or inside the chosen mode's min–max range (see table).

### S020. Numbers per minute in opening

**Definition.** Numeric density in the first 10%.

**Detector.** function `num_per_min_open` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 2.0 | 1.5 | 2.8 |
| Gen (4x) | 1.8 | 0.0 | 4.0 |
| Especially (3x) | 2.3 | 0.6 | 2.4 |
| Oil (5x) | 2.3 | 2.3 | 2.3 |
| Others (1x) | 1.8 | 0.0 | 3.2 |
| **weighted** | median 2.0 (IQR 1.52–2.41) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **2.8**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **2.1**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **1.97**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **0.92**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **2.41**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **2.26**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **0.66**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=2.8, `adam/02-bestselling-book`=2.1, `adam/03-no-longer-in-control`=1.52, `adam/04-superintelligence`=2.05, `adam/05-sam-altman`=2.0, `gen/1`=1.97, `gen/2`=0.92, `gen/3`=3.96, `gen/4`=1.95, `gen/5`=0.0, `gen/6`=2.69, `gen/7`=1.21, `gen/8`=1.73, `gen/9`=0.88, `gen/10`=2.94, `esp/01-spacex`=2.41, `esp/02-ai-paradox`=0.61, `esp/06-data-centers`=2.32, `esp/03-oil-apocalypse`=2.26, `after/01-dark-side-data-centers`=0.66, `after/02-greed`=2.7, `after/03-recycling`=1.62, `after/04-pov-ai`=2.83, `after/05-middle-class`=1.97, `after/06-diamonds`=0.6, `after/07-trump-family`=2.95, `after/08-tokens`=3.19, `after/09-microchip-war`=0.32, `after/10-water`=0.0, `after/11-anthropic-ipo`=0.0, `after/12-data-centres-not-working`=2.93

</details>

**Do.** ~1.5-2.8 number-bearing sentences/min in the first 10%.

**Don't.** Do not open number-free on a money topic.

**Checklist test.** Compute `num_per_min_open` on your outline/draft. PASS if inside the weighted IQR 1.52–2.41, or inside the chosen mode's min–max range (see table).

### S021. Clip-led cold open

**Definition.** Opening that intercuts guest/news audio before host speaks at length.

**Detector.** regex `^(it was a strange|sounds like|like this is|here'?s)\b` in scope `hook`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 0.0 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 7% of weight | 0.01 | 0.0 |

**How each creator does it (verbatim):**

> "It was a strange summer." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 0:00 (0.0%)

**Do.** Adam/oil: clip montage then host line; mark clips [CLIP].

**Don't.** Do not write clips into host lines.

**Checklist test.** In scope `hook`, count sentences matching the detector. Weighted norm ≈ 0.01/1k words; PASS if 0-1 per 1k words; it is rare (7% weighted coverage) — only use with a reason.

### S022. Familiar-to-absurd ladder

**Definition.** Hook moves from a familiar unit to an absurd scale.

**Detector.** regex `\b(an acre|football field|the size of|as much as|equivalent to|more than (the|all)|bigger than)\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 1/3 | 0.13 | 0.0 |
| Oil (5x) | 1/1 | 0.17 | 3.0 |
| Others (1x) | 3/12 | 0.07 | 2.8 |
| **weighted** | 11% of weight | 0.03 | 3.0 |

**How each creator does it (verbatim):**

> "An acre of land is 66 feet across, 660 feet long." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:01 (0.0%)

> "And they're converging on something that honestly is much bigger than gas shortages or gas prices." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:04 (3.0%)

> "If you invested in the S&P 500 in 2021, you could be up as much as 80%." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 0:57 (2.8%)

**Do.** Anchor the scale in a known unit first.

**Don't.** Do not cite a raw huge number without an anchor.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.03/1k words; PASS if 0-1 per 1k words; it is rare (11% weighted coverage) — only use with a reason.


---

## C. Thesis, stakes & promise

### S023. Thesis position (seconds)

**Definition.** Time of first explicit thesis/stakes line.

**Detector.** function `thesis_sec` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 33 | 33 | 33 |
| Gen (4x) | 77.5 | 0 | 245 |
| Especially (3x) | 46 | 46 | 46 |
| Oil (5x) | — | — | — |
| Others (1x) | 67.5 | 0 | 135 |
| **weighted** | median 71 (IQR 33–79) | | |

**How each creator does it (verbatim anchor lines):**

> "It is a wild story, but more importantly, it's a wake-up call." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:33 (1.4%) — value here: **33**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **0**

> "And what I found is that it's looking increasingly likely that private equity is about to take it all for themselves." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 1:19 (6.1%) — value here: **79**

> "And electricity, or AI compute is going to be the currency of the future." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:46 (2.2%) — value here: **46**

> "I feel like for the past 3 years, I've heard over and over again that a recession is about to hit." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 0:00 (0.0%) — value here: **0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=33, `gen/1`=0, `gen/2`=79, `gen/6`=245, `gen/8`=76, `gen/9`=71, `gen/10`=92, `esp/06-data-centers`=46, `after/02-greed`=0, `after/11-anthropic-ipo`=135

</details>

**Do.** State the thesis by ~0:35 (Adam) / ~0:00-1:20 (Gen).

**Don't.** Do not hide the thesis to the midpoint.

**Checklist test.** Compute `thesis_sec` on your outline/draft. PASS if inside the weighted IQR 33–79, or inside the chosen mode's min–max range (see table).

### S024. "Wake-up call" framing

**Definition.** Naming the story as a warning/turning point.

**Detector.** regex `\b(wake-up call|warning|turning point|alarm|this changes|this is (bigger|worse))\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.16 | 2.5 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 14% of weight | 0.06 | 1.4 |

**How each creator does it (verbatim):**

> "It is a wild story, but more importantly, it's a wake-up call." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:33 (1.4%)

> "And the people who've been building more and more advanced AI have been warning us for years now that they don't know how to make this safe." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 1:10 (3.6%)

**Do.** Pair the hook with "and more importantly…".

**Don't.** Do not catastrophize without evidence.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.06/1k words; PASS if 0-1 per 1k words; it is rare (14% weighted coverage) — only use with a reason.

### S025. First-person promise

**Definition.** "I want to take you through / tell you the full story".

**Detector.** regex `\bI want to (take|tell|walk|show|explain|talk|start)|I'?m going to (show|explain|walk|tell)|I wanted to\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.16 | 1.9 |
| Gen (4x) | 4/10 | 0.12 | 8.0 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 44% of weight | 0.1 | 2.5 |

**How each creator does it (verbatim):**

> "I want to start by making sure that all of us understand how the hell we got here." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 1:17 (3.9%)

> "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:29 (1.2%)

> "only one so I wanted to set my bias aside to try and find out could this" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 0:33 (1.7%)

> "And if I wanted to make a name for myself, I was going to have to get creative and lock in." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 2:42 (12.4%)

**Do.** Adam signature: "I want to take you step-by-step through…".

**Don't.** Do not promise "everything you need to know".

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.1/1k words; PASS if 0-1 per 1k words; it is optional (44% weighted coverage) — only use with a reason.

### S026. Collective "let's" promise

**Definition.** Roadmap phrased as joint exploration.

**Detector.** regex `\blet'?s (break|dive|talk|look|figure|find|go|start|get into)` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 1/10 | 0.02 | 11.5 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 4.5 |
| Others (1x) | 2/12 | 0.04 | 4.2 |
| **weighted** | 11% of weight | 0.02 | 4.5 |

**How each creator does it (verbatim):**

> "Now, let's look at prices." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 2:36 (11.5%)

> "So let's get into it." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:35 (4.5%)

> "Uh so, let's get into it." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 0:08 (0.4%)

**Do.** Gen/others: "so let's break down…".

**Don't.** Do not use "let's dive in" with nothing after it.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.02/1k words; PASS if 0-1 per 1k words; it is rare (11% weighted coverage) — only use with a reason.

### S027. Question-as-thesis

**Definition.** Thesis posed as the video's central question.

**Detector.** regex `^(so,? )?(what|why|how|is|are|can|could|will|does|do)\b.*\?$` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.26 | 5.0 |
| Gen (4x) | 6/10 | 0.29 | 3.5 |
| Especially (3x) | 3/3 | 0.27 | 5.6 |
| Oil (5x) | 1/1 | 0.33 | 0.0 |
| Others (1x) | 9/12 | 0.31 | 9.8 |
| **weighted** | 81% of weight | 0.29 | 4.1 |

**How each creator does it (verbatim):**

> "So, why was Sam Altman fired?" — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 1:11 (3.0%)

> "How realistic does that sound?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 2:08 (5.0%)

> "What in the world is happening on Wall Street?" — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 0:03 (0.2%)

> "So, what does private equity even do?" — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 0:43 (4.2%)

> "How were nuclear plants more popular at that moment in time than data centers are now?" — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 1:55 (5.6%)

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%)

> "So, is this really just a correlation or is tech the culprit that’s been secretly destroying the middle class for decades?" — *Others (1x)*, `after/05-middle-class` "Tech Is Permanently Redefining The Middle Class" @ 1:33 (10.2%)

**Do.** Gen: "then what the hell happens to the economy now?"

**Don't.** Do not answer the central question in the hook.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.29/1k words; PASS if ≥1 hit (corpus uses it in 81% of weighted videos) and rate ≤ 1/1k.

### S028. Stakes for "you"

**Definition.** The hook names the consequence for the viewer.

**Detector.** regex `\b(you|your)\b.*\b(pay|lose|job|money|life|future|bill|rent|house|afford)\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.1 | 10.1 |
| Gen (4x) | 6/10 | 0.29 | 5.7 |
| Especially (3x) | 2/3 | 0.13 | 8.7 |
| Oil (5x) | 1/1 | 0.17 | 9.7 |
| Others (1x) | 3/12 | 0.2 | 1.3 |
| **weighted** | 58% of weight | 0.19 | 8.0 |

**How each creator does it (verbatim):**

> "AI is a technology for taking away your job and maybe eventually displacing human sovereignty over our own future." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:32 (1.3%)

> "You know, what does the future actually look like?" — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 3:26 (10.1%)

> "Because maybe a crash will put everything on sale and just maybe you could actually afford it all again." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 0:37 (2.8%)

> "And soon enough, your savings, your job, and your future may end up like Joan fa." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 1:35 (9.3%)

> "Perfect for monitoring war zones, suspected missile launch sites, the Suez Canal, anywhere you can't afford to miss something." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:37 (2.5%)

> "Okay, so all of this is not great, you probably noticed it making your power bill more expensive, flights getting canceled, price of gas, but it's not like post-apocalyptic dystopia." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 3:26 (9.7%)

> "At this point, a college degree might be more likely to get you into crippling debt than it is to help you find a job." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 0:26 (1.3%)

**Do.** Make stakes personal within 60 s.

**Don't.** Do not keep stakes abstract ("society").

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.19/1k words; PASS if ≥1 hit (corpus uses it in 58% of weighted videos) and rate ≤ 1/1k.

### S029. Roadmap specificity

**Definition.** Promise that names steps/parts ("step-by-step", "three main players").

**Detector.** regex `\b(step[- ]by[- ]step|three|four|two|first|the full story|how .* and why)\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.55 | 2.8 |
| Gen (4x) | 10/10 | 0.45 | 4.3 |
| Especially (3x) | 3/3 | 0.94 | 0.4 |
| Oil (5x) | 1/1 | 0.5 | 1.6 |
| Others (1x) | 9/12 | 0.33 | 6.3 |
| **weighted** | 97% of weight | 0.52 | 2.8 |

**How each creator does it (verbatim):**

> "And then, four days later, Sam Altman is apparently back as OpenAI CEO." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:13 (0.5%)

> "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:29 (1.2%)

> "four counts of uh a struggle session it went to a trial and so Yale would" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 2:31 (7.6%)

> "Four out of 10 made zero profit last year and over 8,000 shut down in just the last 6 months." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 0:40 (2.9%)

> "In the last six months, I've been approached by three different groups wanting to replace me with an AI." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:00 (0.0%)

> "But I have to be honest, this oil shock, it is different from the one that we warned you about, because it's actually, and I can hardly believe this, three oil shocks hitting at once." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:34 (1.6%)

> "But what I find extra interesting is the reaction that these two resorts are getting in Albania." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 1:15 (7.4%)

**Do.** Name the shape of the journey.

**Don't.** Do not list 7 chapters out loud.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.52/1k words; PASS if ≥1 hit (corpus uses it in 97% of weighted videos) and rate ≤ 1.0/1k.

### S030. Exclusive-detail promise

**Definition.** Promise of details "I haven't seen reported anywhere else".

**Detector.** regex `\b(haven'?t seen|anywhere else|for the first time|exclusive|never (been )?(seen|told|reported)|I (found|spoke|talked))\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 1.2 |
| Gen (4x) | 7/10 | 0.26 | 6.1 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 3/12 | 0.07 | 10.4 |
| **weighted** | 38% of weight | 0.12 | 5.6 |

**How each creator does it (verbatim):**

> "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:29 (1.2%)

> "But what's never been seen is that this time the government is forced to make a difficult decision." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 1:27 (7.1%)

> "So, I spend weeks following the money, and what I found is something I didn't expect." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 1:18 (6.3%)

> "So to get a deeper understanding, I spoke to those investigating that corruption in Albania." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 1:46 (10.4%)

**Do.** Back it with a real interview/document.

**Don't.** Do not use as filler.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.12/1k words; PASS if 0-1 per 1k words; it is optional (38% weighted coverage) — only use with a reason.


---

## D. Acts & sections

### S031. Section count

**Definition.** Detected major turns (section + question turns).

**Detector.** function `n_sections` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 7 | 6 | 8 |
| Gen (4x) | 6.5 | 2 | 9 |
| Especially (3x) | 8 | 5 | 9 |
| Oil (5x) | 7 | 7 | 7 |
| Others (1x) | 5.5 | 2 | 9 |
| **weighted** | median 7 (IQR 6–8) | | |

**How each creator does it (verbatim anchor lines):**

> "Now go forth and dismantle the illusions of the weak-minded." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 12:39 (32.2%) — value here: **7**

> "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:28 (47.8%) — value here: **8**

> "So what we're seeing here is that just like the store brand, the free copy sort of acts as like a thing that keeps prices down for anyone who can switch." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 11:44 (57.7%) — value here: **6**

> "So a few years pass and now my boomer boss is happy and he can't stop bragging to his friends about how much money he's making from this site called YouTube." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 6:10 (28.4%) — value here: **6**

> "So they kidnaped three guys off the street and made them do it." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 18:29 (74.4%) — value here: **8**

> "So everything I've shown you so far tracks how the oil shock over there, plus a shipping shock right here leads to crazy prices and shortages by the time it gets to the refinery." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 21:24 (60.3%) — value here: **7**

> "So farmers are watching the data center campuses emerging to the south of Cheyenne and getting nervous." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 11:47 (38.6%) — value here: **6**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=7, `adam/02-bestselling-book`=8, `adam/03-no-longer-in-control`=8, `adam/04-superintelligence`=7, `adam/05-sam-altman`=6, `gen/1`=6, `gen/2`=6, `gen/3`=5, `gen/4`=7, `gen/5`=5, `gen/6`=7, `gen/7`=2, `gen/8`=9, `gen/9`=9, `gen/10`=8, `esp/01-spacex`=8, `esp/02-ai-paradox`=5, `esp/06-data-centers`=9, `esp/03-oil-apocalypse`=7, `after/01-dark-side-data-centers`=6, `after/02-greed`=7, `after/03-recycling`=9, `after/04-pov-ai`=5, `after/05-middle-class`=2, `after/06-diamonds`=5, `after/07-trump-family`=6, `after/08-tokens`=4, `after/09-microchip-war`=7, `after/10-water`=4, `after/11-anthropic-ipo`=4, `after/12-data-centres-not-working`=8

</details>

**Do.** Plan 6-12 turns per video.

**Don't.** Do not write one undivided body.

**Checklist test.** Compute `n_sections` on your outline/draft. PASS if inside the weighted IQR 6–8, or inside the chosen mode's min–max range (see table).

### S032. Turns per 10 minutes

**Definition.** Section density per 10 minutes.

**Detector.** function `sections_per_10min` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 1.9 | 1.5 | 2.4 |
| Gen (4x) | 3.1 | 0.6 | 4.7 |
| Especially (3x) | 3.1 | 2.6 | 3.2 |
| Oil (5x) | 2.0 | 2.0 | 2.0 |
| Others (1x) | 2.8 | 1.3 | 3.5 |
| **weighted** | median 2.4 (IQR 1.87–3.07) | | |

**How each creator does it (verbatim anchor lines):**

> "Now go forth and dismantle the illusions of the weak-minded." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 12:39 (32.2%) — value here: **1.78**

> "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:28 (47.8%) — value here: **1.87**

> "So what we're seeing here is that just like the store brand, the free copy sort of acts as like a thing that keeps prices down for anyone who can switch." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 11:44 (57.7%) — value here: **2.95**

> "So a few years pass and now my boomer boss is happy and he can't stop bragging to his friends about how much money he's making from this site called YouTube." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 6:10 (28.4%) — value here: **2.76**

> "So they kidnaped three guys off the street and made them do it." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 18:29 (74.4%) — value here: **3.22**

> "So everything I've shown you so far tracks how the oil shock over there, plus a shipping shock right here leads to crazy prices and shortages by the time it gets to the refinery." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 21:24 (60.3%) — value here: **1.97**

> "So farmers are watching the data center campuses emerging to the south of Cheyenne and getting nervous." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 11:47 (38.6%) — value here: **1.97**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=1.78, `adam/02-bestselling-book`=1.87, `adam/03-no-longer-in-control`=2.44, `adam/04-superintelligence`=2.05, `adam/05-sam-altman`=1.5, `gen/1`=2.95, `gen/2`=2.76, `gen/3`=2.2, `gen/4`=3.41, `gen/5`=3.03, `gen/6`=3.14, `gen/7`=0.61, `gen/8`=3.89, `gen/9`=3.98, `gen/10`=4.7, `esp/01-spacex`=3.22, `esp/02-ai-paradox`=3.07, `esp/06-data-centers`=2.61, `esp/03-oil-apocalypse`=1.97, `after/01-dark-side-data-centers`=1.97, `after/02-greed`=2.1, `after/03-recycling`=2.92, `after/04-pov-ai`=2.83, `after/05-middle-class`=1.31, `after/06-diamonds`=3.01, `after/07-trump-family`=3.54, `after/08-tokens`=2.55, `after/09-microchip-war`=2.22, `after/10-water`=3.01, `after/11-anthropic-ipo`=2.83, `after/12-data-centres-not-working`=2.93

</details>

**Do.** Adam ~1.5-2.4 per 10 min; Gen/especially ~3.1 per 10 min.

**Don't.** Do not exceed one turn per minute.

**Checklist test.** Compute `sections_per_10min` on your outline/draft. PASS if inside the weighted IQR 1.87–3.07, or inside the chosen mode's min–max range (see table).

### S033. Question-turn share

**Definition.** Share of turns that open with a question.

**Detector.** function `question_turn_share` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 25 | 14 | 50 |
| Gen (4x) | 12.5 | 0 | 40 |
| Especially (3x) | 25 | 0 | 44 |
| Oil (5x) | 29 | 29 | 29 |
| Others (1x) | 41.5 | 0 | 100 |
| **weighted** | median 25 (IQR 14–40) | | |

**How each creator does it (verbatim anchor lines):**

> "How does that change in a world where it gets a little bit easier and a little bit less risky, and then a lot easier and a lot less risky?" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 32:06 (81.6%) — value here: **43**

> "Why are they investing so much in this moonshot anyway?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 11:08 (26.0%) — value here: **25**

> "Why does this even matter when all this still must be illegal?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 6:49 (33.5%) — value here: **33**

> "How was I going to pitch him this opportunity?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 4:45 (21.9%) — value here: **0**

> "What happens if someone else gets there first?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:16 (41.3%) — value here: **25**

> "Why did they call it that?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 27:24 (77.3%) — value here: **29**

> "So, what sort of reading are we getting?" — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 14:43 (48.2%) — value here: **33**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=43, `adam/02-bestselling-book`=25, `adam/03-no-longer-in-control`=50, `adam/04-superintelligence`=14, `adam/05-sam-altman`=17, `gen/1`=33, `gen/2`=0, `gen/3`=0, `gen/4`=29, `gen/5`=40, `gen/6`=14, `gen/7`=0, `gen/8`=0, `gen/9`=11, `gen/10`=25, `esp/01-spacex`=25, `esp/02-ai-paradox`=0, `esp/06-data-centers`=44, `esp/03-oil-apocalypse`=29, `after/01-dark-side-data-centers`=33, `after/02-greed`=43, `after/03-recycling`=44, `after/04-pov-ai`=40, `after/05-middle-class`=50, `after/06-diamonds`=0, `after/07-trump-family`=0, `after/08-tokens`=100, `after/09-microchip-war`=29, `after/10-water`=75, `after/11-anthropic-ipo`=50, `after/12-data-centres-not-working`=25

</details>

**Do.** Open ~25-50% of sections with a question.

**Don't.** Do not open every section with a question.

**Checklist test.** Compute `question_turn_share` on your outline/draft. PASS if inside the weighted IQR 14–40, or inside the chosen mode's min–max range (see table).

### S034. "So," turn opener

**Definition.** Section opens with "So,…/So now/So how".

**Detector.** regex `^so,? ` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.84 | 17.2 |
| Gen (4x) | 9/10 | 4.69 | 16.2 |
| Especially (3x) | 3/3 | 1.35 | 15.2 |
| Oil (5x) | 1/1 | 1.98 | 23.8 |
| Others (1x) | 12/12 | 2.27 | 19.1 |
| **weighted** | 96% of weight | 2.73 | 17.1 |

**How each creator does it (verbatim):**

> "So good, it starts to accelerate AI research and development by 50%, and it gives them a crucial edge." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 5:52 (17.2%)

> "So, if Grok was searching for trends as it was formulating its responses, it could have had that Hitler persona reinforced." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 11:57 (30.4%)

> "So let me walk you through how I as private equity exactly would identify the perfect fit." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 3:16 (15.0%)

> "So, the first trick here is we don't really want a store." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 4:23 (19.0%)

> "So they parked one over the target in Richmond, California, and found a 146 out of 540 spaces were full." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 4:07 (16.6%)

> "So now we gotta X this out." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 8:26 (23.8%)

> "So one by one, Hoxha severed ties with his allies, then sealed his country off from the outside world." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 3:16 (19.3%)

**Do.** Gen's main turn word; Adam uses it for logic turns.

**Don't.** Do not start 3 consecutive sentences with So.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 2.73/1k words; PASS if ≥1 hit (corpus uses it in 96% of weighted videos) and rate ≤ 5.5/1k.

### S035. "Now," turn opener

**Definition.** Section opens with "Now,".

**Detector.** regex `^now,? ` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.48 | 28.6 |
| Gen (4x) | 8/10 | 0.6 | 20.1 |
| Especially (3x) | 2/3 | 0.2 | 34.5 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 7/12 | 0.37 | 31.7 |
| **weighted** | 72% of weight | 0.46 | 27.1 |

**How each creator does it (verbatim):**

> "Now, that example — pretty harmless." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 8:45 (20.4%)

> "Now, this is what OpenAI looked like as of November 2023 after the release of ChatGPT, the fastest growing tech product in history, and $13 worth of investment from Microsoft." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 10:50 (27.1%)

> "Now with Zapier, it can automatically send the email and ping the right person in Slack." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 9:33 (42.8%)

> "Now that I own the company, I go back to the bank and say, "Can the company borrow even more?"" — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 2:56 (17.2%)

> "Now, it is important to point out three things here." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 5:56 (17.2%)

> "Now, during this time, what do you think the tax rate was on the wealthiest Americans?" — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 12:19 (36.9%)

**Do.** Adam: "Now, we don't know exactly how…" — scope shift.

**Don't.** Do not use Now as a time word confusion.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 0.46/1k words; PASS if ≥1 hit (corpus uses it in 72% of weighted videos) and rate ≤ 1/1k.

### S036. "But then" escalation turn

**Definition.** Narrative reversal opener.

**Detector.** regex `^but then\b` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.13 | 41.4 |
| Gen (4x) | 8/10 | 0.21 | 46.5 |
| Especially (3x) | 2/3 | 0.27 | 24.5 |
| Oil (5x) | 1/1 | 0.17 | 34.9 |
| Others (1x) | 2/12 | 0.04 | 45.0 |
| **weighted** | 58% of weight | 0.19 | 34.9 |

**How each creator does it (verbatim):**

> "But then it turned out that the world didn't immediately end and then everyone just kind of moved on." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 12:02 (28.1%)

> "But then there's a breakthrough." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 17:55 (54.6%)

> "But then I looked at the 2020 crash when everyone was stuck at home fighting over toilet paper." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 5:58 (26.8%)

> "But then on 30th of March, not private equity, but Cisco agreed to buy it for $29." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 18:31 (80.1%)

> "But then they changed one thing." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 3:42 (22.7%)

> "But then September 1st, something big changes." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 12:23 (34.9%)

> "But then I talked to Dr." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 7:59 (56.4%)

**Do.** Use at act breaks in story videos.

**Don't.** Do not use for minor points.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 0.19/1k words; PASS if ≥1 hit (corpus uses it in 58% of weighted videos) and rate ≤ 1/1k.

### S037. "But here's" pivot

**Definition.** "But here's the thing / where / the part…".

**Detector.** regex `^but here'?s\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 81.2 |
| Gen (4x) | 2/10 | 0.12 | 17.2 |
| Especially (3x) | 2/3 | 0.13 | 72.8 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.02 | 65.2 |
| **weighted** | 29% of weight | 0.09 | 75.3 |

**How each creator does it (verbatim):**

> "But here's the thing." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 29:36 (75.3%)

> "But here's another way." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 37:20 (87.2%)

> "But here's why we've only seen the beginning of this." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 4:11 (19.2%)

> "But here's the risk." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 2:36 (15.3%)

> "But here's where we all stop." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 19:24 (78.1%)

> "But here's the thing." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 21:45 (65.2%)

**Do.** Use 1-3 times as reveal pivots.

**Don't.** Do not use more than once per 5 min.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.09/1k words; PASS if 0-1 per 1k words; it is optional (29% weighted coverage) — only use with a reason.

### S038. "Which brings us" callback turn

**Definition.** Turn that ties a digression back to the main story.

**Detector.** regex `\bwhich brings (us|me)\b` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 58.7 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 7% of weight | 0.01 | 58.7 |

**How each creator does it (verbatim):**

> "Which brings us back to MechaHitler week." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 23:04 (58.7%)

**Do.** Return to the cold-open incident mid-video.

**Don't.** Do not use without a prior digression.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 0.01/1k words; PASS if 0-1 per 1k words; it is rare (7% weighted coverage) — only use with a reason.

### S039. Enumerated sections

**Definition.** First/Second/Third or "the next reason".

**Detector.** regex `^(first|second|third|fourth|finally|the (first|second|third|next|last) (reason|thing|problem|step|part))\b` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 65.7 |
| Gen (4x) | 4/10 | 0.1 | 25.9 |
| Especially (3x) | 2/3 | 0.27 | 26.8 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 3/12 | 0.15 | 70.9 |
| **weighted** | 39% of weight | 0.1 | 39.4 |

**How each creator does it (verbatim):**

> "First of all, none of this has to do with consciousness or having human-like emotions." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 26:20 (61.5%)

> "First, Loopt, Sam Altman's first company." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 27:59 (69.9%)

> "first Guinea pit so to understand this case I think it's just really important" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 12:58 (39.4%)

> "First off, unless you're a super unk viewer of this channel, none of those two crashes were things that any of you watching have lived through." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 5:39 (25.3%)

> "First, babies practice syllables, then words, then they glue words together, eventually forming sentences that others can understand." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 2:57 (18.1%)

> "Second, did you know you have to clean the plastic before you put it in the bin?" — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 11:40 (37.9%)

**Do.** Use numbering for lists of causes.

**Don't.** Do not number narrative beats.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 0.1/1k words; PASS if 0-1 per 1k words; it is optional (39% weighted coverage) — only use with a reason.

### S040. Flashback turn

**Definition.** Section opens with a past year/time jump.

**Detector.** regex `^(back in|in (19|20)\d\d|years (ago|earlier)|fast[- ]forward|a (few|couple) (years|months) (ago|later))` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.29 | 34.2 |
| Gen (4x) | 5/10 | 0.14 | 64.3 |
| Especially (3x) | 2/3 | 0.2 | 48.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 5/12 | 0.22 | 34.0 |
| **weighted** | 51% of weight | 0.22 | 34.2 |

**How each creator does it (verbatim):**

> "A few years ago, our most advanced AI systems, large language models, were like yeast." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 13:10 (30.7%)

> "In 2003, a teenager shows up at the University of Toronto and knocks on the door of Professor Geoffrey Hinton, a future godfather of AI." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 13:42 (34.2%)

> "In 2005, private equity firms bought it, loaded it with debt, and made it borrow even more just to pay private equity $470 million in special dividends." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 3:22 (19.8%)

> "In 2010, the Associated Press reported that a huge backlog of foreclosed homes from the aftermath had pushed prices down and made it hard for builders to compete." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 3:24 (15.0%)

> "Fast forward to 2030 and the picture starts to shift significantly." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 25:51 (75.0%)

> "In 1943, Johnson and Johnson puts out this mission statement that's like, here's our list of priorities in order." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 11:38 (34.8%)

**Do.** Use chronology jumps to reset curiosity.

**Don't.** Do not jump more than twice without returning.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 0.22/1k words; PASS if ≥1 hit (corpus uses it in 51% of weighted videos) and rate ≤ 1/1k.

### S041. Mechanism section marker

**Definition.** "To understand X, you need…" explainer entry.

**Detector.** regex `\bto understand\b|\bhere'?s how\b|\bthe way (it|this) works\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.29 | 20.0 |
| Gen (4x) | 7/10 | 0.31 | 11.3 |
| Especially (3x) | 1/3 | 0.07 | 48.6 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.04 | 20.3 |
| **weighted** | 60% of weight | 0.23 | 14.5 |

**How each creator does it (verbatim):**

> "Nobody seems to understand why this guy was fired." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:12 (0.5%)

> "Here's how that conversation played out." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 10:01 (25.5%)

> "But to understand why that's a problem, you first have to understand the sides of what they're betting against you." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 13:28 (65.6%)

> "And I'm going to break this down for you in a way that's easy to understand." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 1:13 (5.4%)

> "A local fight over where the prison should go: brutal, but it's honest and easy to understand." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 16:46 (48.6%)

> "So, you say, "I'd want to understand why."" — *Others (1x)*, `after/04-pov-ai` "" @ 0:09 (0.8%)

**Do.** Signal explainer mode explicitly.

**Don't.** Do not start jargon before the marker.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.23/1k words; PASS if ≥1 hit (corpus uses it in 60% of weighted videos) and rate ≤ 1/1k.

### S042. Interview/source section

**Definition.** Section built around "I talked/spoke to…".

**Detector.** regex `\bI (talked|spoke|asked|interviewed|reached out|met)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 66.8 |
| Gen (4x) | 2/10 | 0.05 | 34.0 |
| Especially (3x) | 1/3 | 0.07 | 35.3 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 3/12 | 0.09 | 37.0 |
| **weighted** | 21% of weight | 0.06 | 51.1 |

**How each creator does it (verbatim):**

> "But then I talked to Nate." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 28:38 (66.8%)

> "So, now this group I talked about, right, that's probably only like a few thousand people." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 11:34 (51.1%)

> "noise in fact that's actually exactly how Saif and I met he saw my video" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 5:32 (16.8%)

> "That friction I talked about, they built it in." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 5:45 (35.3%)

> "So to get a deeper understanding, I spoke to those investigating that corruption in Albania." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 1:46 (10.4%)

**Do.** Adam: original interviews mid-video.

**Don't.** Do not fabricate access.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.06/1k words; PASS if 0-1 per 1k words; it is optional (21% weighted coverage) — only use with a reason.


---

## E. Beat timing

### S043. Midroll sponsor position

**Definition.** Sponsor start as % of runtime.

**Detector.** function `sponsor_pct` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | — | — | — |
| Gen (4x) | 38.8 | 20.3 | 46.4 |
| Especially (3x) | 6.1 | 4.5 | 38.0 |
| Oil (5x) | 27.5 | 27.5 | 27.5 |
| Others (1x) | 24.6 | 9.5 | 93.9 |
| **weighted** | median 35.6 (IQR 27.5–41.4) | | |

**How each creator does it (verbatim anchor lines):**

> "We've put a link in the description of this video." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 39:07 (97.8%) — value here: **None**

> "And especially with the topic of this video, that's where today's sponsor Zapier comes in." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 8:29 (41.7%) — value here: **41.7**

> "That's where today's sponsor, Proton Mail, comes in." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:05 (46.4%) — value here: **46.4**

> "This video is sponsored by Wealthfront." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 1:07 (4.5%) — value here: **4.5**

> "(tense ambient music) If you are in any way involved in running a business, you are gonna wanna hear about today's sponsor Odoo, the all-in-one management software." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 9:45 (27.5%) — value here: **27.5**

> "Hi, I'm Upside Down and I'm here to tell you about today's sponsor, NordVPN." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 3:11 (9.5%) — value here: **9.5**

<details><summary>Per-video values</summary>

`gen/1`=41.7, `gen/2`=46.4, `gen/3`=43.5, `gen/4`=39.0, `gen/5`=35.6, `gen/6`=41.4, `gen/7`=20.3, `gen/8`=38.6, `gen/9`=34.5, `gen/10`=32.0, `esp/01-spacex`=4.5, `esp/02-ai-paradox`=38.0, `esp/06-data-centers`=6.1, `esp/03-oil-apocalypse`=27.5, `after/02-greed`=9.5, `after/03-recycling`=16.0, `after/07-trump-family`=37.0, `after/09-microchip-war`=93.9, `after/12-data-centres-not-working`=24.6

</details>

**Do.** Gen 20-46% (median 39%); especially either early (4-6%) or ~38%; oil 27.5%; Adam: no midroll.

**Don't.** Do not drop the sponsor in the first 60 s or after 60%.

**Checklist test.** Compute `sponsor_pct` on your outline/draft. PASS if inside the weighted IQR 27.5–41.4, or inside the chosen mode's min–max range (see table).

### S044. Sponsor read length

**Definition.** Seconds of the sponsor block.

**Detector.** function `sponsor_sec_len` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | — | — | — |
| Gen (4x) | 44.5 | 34 | 54 |
| Especially (3x) | 55 | 8 | 118 |
| Oil (5x) | 88 | 88 | 88 |
| Others (1x) | 53 | 39 | 76 |
| **weighted** | median 46 (IQR 41–54) | | |

**How each creator does it (verbatim anchor lines):**

> "Let's make sure that Sam Altman is not the only person who decides our future." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 39:44 (99.3%) — value here: **None**

> "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:15 (45.5%) — value here: **46**

> "So, now let's talk about which channels have actually been bought and the few players behind them all." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:46 (49.5%) — value here: **41**

> "Hasn't been opened in more than 100 years, going all the way back to the plane." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 3:05 (12.4%) — value here: **118**

> "So now I'm gonna flip this back over, and get us back to our story." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 11:13 (31.6%) — value here: **88**

> "But don't scan me." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 4:27 (13.3%) — value here: **76**

<details><summary>Per-video values</summary>

`gen/1`=46, `gen/2`=41, `gen/3`=34, `gen/4`=54, `gen/5`=44, `gen/6`=45, `gen/7`=48, `gen/8`=42, `gen/9`=38, `gen/10`=48, `esp/01-spacex`=118, `esp/02-ai-paradox`=55, `esp/06-data-centers`=8, `esp/03-oil-apocalypse`=88, `after/02-greed`=76, `after/03-recycling`=53, `after/07-trump-family`=39, `after/09-microchip-war`=51, `after/12-data-centres-not-working`=60

</details>

**Do.** 30-75 s; one block.

**Don't.** Do not run 2+ minutes.

**Checklist test.** Compute `sponsor_sec_len` on your outline/draft. PASS if inside the weighted IQR 41–54, or inside the chosen mode's min–max range (see table).

### S045. Has midroll

**Definition.** Whether a mid-video sponsor exists.

**Detector.** function `has_midroll` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0 | 0 | 0 |
| Gen (4x) | 1.0 | 1 | 1 |
| Especially (3x) | 1 | 0 | 1 |
| Oil (5x) | 1 | 1 | 1 |
| Others (1x) | 0.0 | 0 | 1 |
| **weighted** | median 1 (IQR 0–1) | | |

**How each creator does it (verbatim anchor lines):**

> "We've put a link in the description of this video." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 39:07 (97.8%) — value here: **0**

> "And especially with the topic of this video, that's where today's sponsor Zapier comes in." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 8:29 (41.7%) — value here: **1**

> "That's where today's sponsor, Proton Mail, comes in." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:05 (46.4%) — value here: **1**

> "This video is sponsored by Wealthfront." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 1:07 (4.5%) — value here: **0**

> "(tense ambient music) If you are in any way involved in running a business, you are gonna wanna hear about today's sponsor Odoo, the all-in-one management software." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 9:45 (27.5%) — value here: **1**

> "Hi, I'm Upside Down and I'm here to tell you about today's sponsor, NordVPN." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 3:11 (9.5%) — value here: **0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0, `adam/02-bestselling-book`=0, `adam/03-no-longer-in-control`=0, `adam/04-superintelligence`=0, `adam/05-sam-altman`=0, `gen/1`=1, `gen/2`=1, `gen/3`=1, `gen/4`=1, `gen/5`=1, `gen/6`=1, `gen/7`=1, `gen/8`=1, `gen/9`=1, `gen/10`=1, `esp/01-spacex`=0, `esp/02-ai-paradox`=1, `esp/06-data-centers`=1, `esp/03-oil-apocalypse`=1, `after/01-dark-side-data-centers`=0, `after/02-greed`=0, `after/03-recycling`=1, `after/04-pov-ai`=0, `after/05-middle-class`=0, `after/06-diamonds`=0, `after/07-trump-family`=1, `after/08-tokens`=0, `after/09-microchip-war`=0, `after/10-water`=0, `after/11-anthropic-ipo`=0, `after/12-data-centres-not-working`=1

</details>

**Do.** Gen/others: yes; Adam: patronage/end-card only.

**Don't.** Do not add a midroll in Adam mode.

**Checklist test.** Compute `has_midroll` on your outline/draft. PASS if inside the weighted IQR 0–1, or inside the chosen mode's min–max range (see table).

### S046. Sponsor bridge line

**Definition.** Sponsor introduced by a topical bridge ("that's where…comes in").

**Detector.** function `sponsor_bridge` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0 | 0 | 0 |
| Gen (4x) | 1.0 | 0 | 1 |
| Especially (3x) | 0 | 0 | 0 |
| Oil (5x) | 0 | 0 | 0 |
| Others (1x) | 0 | 0 | 1 |
| **weighted** | median 1 (IQR 0–1) | | |

**How each creator does it (verbatim anchor lines):**

> "We've put a link in the description of this video." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 39:07 (97.8%) — value here: **0**

> "And especially with the topic of this video, that's where today's sponsor Zapier comes in." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 8:29 (41.7%) — value here: **1**

> "That's where today's sponsor, Proton Mail, comes in." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:05 (46.4%) — value here: **1**

> "This video is sponsored by Wealthfront." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 1:07 (4.5%) — value here: **0**

> "(tense ambient music) If you are in any way involved in running a business, you are gonna wanna hear about today's sponsor Odoo, the all-in-one management software." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 9:45 (27.5%) — value here: **0**

> "Hi, I'm Upside Down and I'm here to tell you about today's sponsor, NordVPN." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 3:11 (9.5%) — value here: **0**

<details><summary>Per-video values</summary>

`adam/05-sam-altman`=0, `gen/1`=1, `gen/2`=1, `gen/3`=0, `gen/4`=1, `gen/5`=1, `gen/6`=1, `gen/7`=0, `gen/8`=1, `gen/9`=1, `gen/10`=1, `esp/01-spacex`=0, `esp/02-ai-paradox`=0, `esp/06-data-centers`=0, `esp/03-oil-apocalypse`=0, `after/02-greed`=0, `after/03-recycling`=1, `after/07-trump-family`=1, `after/09-microchip-war`=0, `after/12-data-centres-not-working`=0

</details>

**Do.** Bridge from the problem just described.

**Don't.** Do not cold-cut "This video is sponsored by" mid-argument (unless show format).

**Checklist test.** Compute `sponsor_bridge` on your outline/draft. PASS if inside the weighted IQR 0–1, or inside the chosen mode's min–max range (see table).

### S047. Conclusion start %

**Definition.** Where the conclusion begins.

**Detector.** function `conc_pct` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 81.9 | 75.3 | 88.7 |
| Gen (4x) | 85.8 | 70.5 | 97.7 |
| Especially (3x) | — | — | — |
| Oil (5x) | 95.2 | 95.2 | 95.2 |
| Others (1x) | 86.4 | 77.5 | 95.5 |
| **weighted** | median 87.6 (IQR 76.2–88.7) | | |

**How each creator does it (verbatim anchor lines):**

> "But here's the thing." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 29:36 (75.3%) — value here: **75.3**

> "I think that's basically the plan for AI companies today." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 37:32 (87.6%) — value here: **87.6**

> "The hype that it will ultimately do everything and anything, like replace human labor." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 16:54 (83.0%) — value here: **83.0**

> "So, the newest homeowners are like the first ones falling behind, which brings up a pretty important question of what this all means for you and in the future." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 17:28 (76.9%) — value here: **76.9**

> "So what does all this mean?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 33:46 (95.2%) — value here: **95.2**

> "Now, I'm pretty sure they would still take the same amount, but instead of reinvesting it into the economy, which is what SNAP ultimately does, they would just buy some more missiles or send a pile of cash to Argentina." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 25:53 (77.5%) — value here: **77.5**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=75.3, `adam/02-bestselling-book`=87.6, `adam/04-superintelligence`=88.7, `adam/05-sam-altman`=76.2, `gen/1`=83.0, `gen/3`=76.9, `gen/4`=70.5, `gen/5`=97.7, `gen/7`=88.5, `gen/8`=92.4, `esp/03-oil-apocalypse`=95.2, `after/02-greed`=77.5, `after/03-recycling`=95.5, `after/05-middle-class`=95.2, `after/07-trump-family`=77.6

</details>

**Do.** Begin landing at ~75-95% (Adam median 82%, Gen 86%).

**Don't.** Do not start the conclusion before 75%.

**Checklist test.** Compute `conc_pct` on your outline/draft. PASS if inside the weighted IQR 76.2–88.7, or inside the chosen mode's min–max range (see table).

### S048. Outro length

**Definition.** Seconds from first closing CTA to end.

**Detector.** function `outro_sec` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 23.0 | 3 | 41 |
| Gen (4x) | 20 | 14 | 26 |
| Especially (3x) | 22 | 11 | 31 |
| Oil (5x) | — | — | — |
| Others (1x) | 27 | 8 | 52 |
| **weighted** | median 20 (IQR 14–27) | | |

**How each creator does it (verbatim anchor lines):**

> "Thank you so much for watching and see you in the next one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 39:16 (99.9%) — value here: **3**

> "While you're there, we would love for you to sign up for our newsletter to stay up to date on this topic." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:11 (98.5%) — value here: **39**

> "And so, I'll definitely be diving even deeper into this in my free weekly newsletter in the video description." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 20:07 (98.9%) — value here: **14**

> "And so, I'll be going even deeper into this issue next week on my free newsletter in the video description." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 21:24 (98.5%) — value here: **20**

> "And that is exactly what hitting the subscribe button signals." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 24:29 (98.5%) — value here: **22**

> "I'm Drew, and thank you so much for watching." — *Others (1x)*, `after/04-pov-ai` "" @ 17:31 (99.2%) — value here: **8**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=3, `adam/02-bestselling-book`=39, `adam/03-no-longer-in-control`=7, `adam/04-superintelligence`=41, `gen/1`=14, `gen/2`=20, `gen/3`=22, `gen/4`=24, `gen/5`=21, `gen/6`=16, `gen/7`=18, `gen/8`=26, `gen/9`=19, `esp/01-spacex`=22, `esp/02-ai-paradox`=31, `esp/06-data-centers`=11, `after/04-pov-ai`=8, `after/06-diamonds`=16, `after/09-microchip-war`=52, `after/10-water`=27, `after/11-anthropic-ipo`=29

</details>

**Do.** Keep outro 10-60 s.

**Don't.** Do not run a 2-minute outro.

**Checklist test.** Compute `outro_sec` on your outline/draft. PASS if inside the weighted IQR 14–27, or inside the chosen mode's min–max range (see table).

### S049. Return from sponsor line

**Definition.** "Back to it / So back to…" re-entry.

**Detector.** regex `^(so,? )?back to (it|the|our)|^anyway\b` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 21.3 |
| Gen (4x) | 3/10 | 0.1 | 44.8 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.33 | 65.3 |
| Others (1x) | 2/12 | 0.04 | 67.5 |
| **weighted** | 26% of weight | 0.07 | 44.8 |

**How each creator does it (verbatim):**

> "Anyway, back to the scenario." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 7:16 (21.3%)

> "So back to it because a whole generation is now convinced that after each crash a bounce is guaranteed." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 9:59 (44.8%)

> "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:15 (45.5%)

> "Anyway, got a lot worse when our old pals, Iran and Saudi Arabia also got into a refinery war." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 23:10 (65.3%)

> "Anyway, Anthropic also points to their own constitution when asked about their trustworthiness." — *Others (1x)*, `after/11-anthropic-ipo` "Why Anthropic’s IPO Is So Dangerous" @ 7:08 (50.4%)

**Do.** Re-enter with a question or the open loop.

**Don't.** Do not resume with a dry fact.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 0.07/1k words; PASS if 0-1 per 1k words; it is optional (26% weighted coverage) — only use with a reason.


---

## F. Evidence stacking

### S050. Numbers per minute

**Definition.** Density of numerals/magnitudes over the whole video.

**Detector.** function `num_per_min` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 1.3 | 1.1 | 2.5 |
| Gen (4x) | 2.2 | 1.0 | 3.4 |
| Especially (3x) | 1.8 | 0.7 | 2.4 |
| Oil (5x) | 1.8 | 1.8 | 1.8 |
| Others (1x) | 1.6 | 0.4 | 3.3 |
| **weighted** | median 1.8 (IQR 1.31–2.47) | | |

**How each creator does it (verbatim anchor lines):**

> "In fact, when I started following the account that introduced MechaHitler as a name to Grok on Tuesday, July 8th, I came across several tweets dating back years like this one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 15:39 (39.8%) — value here: **1.31**

> "As new subscriptions surge, so does Galvanic's stock price, enough to make back the entire $10 million cost of the run in the first 72 hours." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 22:43 (53.0%) — value here: **1.13**

> "In fact, 41% from their low in April." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 11:03 (54.3%) — value here: **1.51**

> "Estimated monthly earnings has dropped 70% from roughly 52,000 in March 2024 to around 13,000 to 17,000 by February 2026." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 13:47 (63.4%) — value here: **2.05**

> "If gravity drags them into Earth's atmosphere, it's moving closer, 100 miles closer, ensuring the time it takes to receive or send a signal from Earth is lower than anyone else, because competition from low Earth orbit is hot." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:56 (44.0%) — value here: **1.75**

> "(tense piano music) That means that shipping alone now adds another $23 to the price of each barrel of oil." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 17:43 (50.0%) — value here: **1.81**

> "Documents show that Microsoft planned for each of these buildings to use 1 million gallons of water a day." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 19:35 (64.1%) — value here: **2.24**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=1.31, `adam/02-bestselling-book`=1.13, `adam/03-no-longer-in-control`=1.21, `adam/04-superintelligence`=2.47, `adam/05-sam-altman`=1.81, `gen/1`=1.51, `gen/2`=2.05, `gen/3`=3.4, `gen/4`=1.79, `gen/5`=1.38, `gen/6`=3.29, `gen/7`=1.02, `gen/8`=2.53, `gen/9`=2.27, `gen/10`=2.73, `esp/01-spacex`=1.75, `esp/02-ai-paradox`=0.73, `esp/06-data-centers`=2.35, `esp/03-oil-apocalypse`=1.81, `after/01-dark-side-data-centers`=2.24, `after/02-greed`=1.66, `after/03-recycling`=1.35, `after/04-pov-ai`=1.63, `after/05-middle-class`=3.31, `after/06-diamonds`=0.77, `after/07-trump-family`=1.64, `after/08-tokens`=2.71, `after/09-microchip-war`=0.69, `after/10-water`=1.49, `after/11-anthropic-ipo`=0.42, `after/12-data-centres-not-working`=2.87

</details>

**Do.** Adam ~1.1-2.5 per min; Gen ~1.0-3.4; oil/especially ~1.8.

**Don't.** Do not exceed ~8/min.

**Checklist test.** Compute `num_per_min` on your outline/draft. PASS if inside the weighted IQR 1.31–2.47, or inside the chosen mode's min–max range (see table).

### S051. Year anchors per minute

**Definition.** Explicit years.

**Detector.** function `year_mentions` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.3 | 0.1 | 0.7 |
| Gen (4x) | 0.5 | 0.1 | 1.2 |
| Especially (3x) | 0.2 | 0.1 | 0.3 |
| Oil (5x) | 0.0 | 0.0 | 0.0 |
| Others (1x) | 0.3 | 0.0 | 0.8 |
| **weighted** | median 0.3 (IQR 0.24–0.54) | | |

**How each creator does it (verbatim anchor lines):**

> "Like this is Musk in 2014." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 27:31 (70.0%) — value here: **0.33**

> "This was an experiment done by OpenAI back in 2019." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 18:37 (43.5%) — value here: **0.3**

> "When Deep Seek came out in January 2025, Nvidia lost about $589 billion in one day, and OpenAI alleged that Deep Seek may have used its models to build its own." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 17:29 (85.9%) — value here: **0.1**

> "Estimated monthly earnings has dropped 70% from roughly 52,000 in March 2024 to around 13,000 to 17,000 by February 2026." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 13:47 (63.4%) — value here: **0.59**

> "We could see the internet would be a big deal, but the physical gap a choke point of internet speed, let imaginations get way ahead of the dial up everyone was on until about 2005." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 22:20 (89.9%) — value here: **0.08**

> "February 2026, Benjamin Netanyahu convinces Donald Trump to do regime change war on Iran." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:29 (7.0%) — value here: **0.03**

> "Data centers, particularly driven by AI, could use as much as 600 terowatt hours of power by 2028." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 23:33 (77.1%) — value here: **0.78**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0.33, `adam/02-bestselling-book`=0.3, `adam/03-no-longer-in-control`=0.09, `adam/04-superintelligence`=0.67, `adam/05-sam-altman`=0.49, `gen/1`=0.1, `gen/2`=0.59, `gen/3`=0.92, `gen/4`=0.24, `gen/5`=0.24, `gen/6`=1.11, `gen/7`=0.48, `gen/8`=0.51, `gen/9`=0.35, `gen/10`=1.16, `esp/01-spacex`=0.08, `esp/02-ai-paradox`=0.24, `esp/06-data-centers`=0.29, `esp/03-oil-apocalypse`=0.03, `after/01-dark-side-data-centers`=0.78, `after/02-greed`=0.15, `after/03-recycling`=0.23, `after/04-pov-ai`=0.34, `after/05-middle-class`=0.52, `after/06-diamonds`=0.0, `after/07-trump-family`=0.64, `after/08-tokens`=0.38, `after/09-microchip-war`=0.13, `after/10-water`=0.22, `after/11-anthropic-ipo`=0.14, `after/12-data-centres-not-working`=0.54

</details>

**Do.** Anchor timeline with years.

**Don't.** Do not leave chronology vague.

**Checklist test.** Compute `year_mentions` on your outline/draft. PASS if inside the weighted IQR 0.24–0.54, or inside the chosen mode's min–max range (see table).

### S052. Named-source attribution

**Definition.** "According to / reported / a study / data from".

**Detector.** regex `\b(according to|reported|report(ed)? by|a (new )?(study|report|paper|survey)|data from|filings?|documents?|testimony|told (the|reuters|bloomberg|cnbc))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.39 | 2.0 |
| Gen (4x) | 5/10 | 0.21 | 15.0 |
| Especially (3x) | 2/3 | 0.13 | 39.4 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 10/12 | 0.68 | 24.3 |
| **weighted** | 70% of weight | 0.33 | 20.5 |

**How each creator does it (verbatim):**

> "What is so exciting and terrifying about reading this document is that it's not just a research report." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 0:41 (2.0%)

> "Some of it we only know now, thanks to unsealed court testimony that's come out just this year." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:20 (0.8%)

> "But once you see this document, you'll see that that's barely part of it." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 2:00 (8.7%)

> "They're aiming for about a $2 trillion valuation even though its own filing shows that it's losing about $8 billion just last year." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 12:03 (54.0%)

> "According to our man Abraham Maslow, one." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 8:27 (34.0%)

> "According to a report by Bloomberg, around 140 data center projects were supposed to open in the US this year." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 0:36 (2.2%)

**Do.** Name the source in-sentence.

**Don't.** Do not say "experts say" unnamed.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.33/1k words; PASS if ≥1 hit (corpus uses it in 70% of weighted videos) and rate ≤ 1/1k.

### S053. Quoted-person evidence

**Definition.** Host quotes a named person ("X said…", "in his words").

**Detector.** regex `\b(said|says|wrote|writes|tweeted|posted|told)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.36 | 15.1 |
| Gen (4x) | 10/10 | 1.62 | 18.3 |
| Especially (3x) | 3/3 | 1.35 | 4.9 |
| Oil (5x) | 1/1 | 0.83 | 1.4 |
| Others (1x) | 11/12 | 1.07 | 20.4 |
| **weighted** | 99% of weight | 1.38 | 13.4 |

**How each creator does it (verbatim):**

> "It uses the request new folder trick, but instead of writing a normal folder name, it writes a message." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 4:58 (15.1%)

> "Recently, he and a colleague, Nate Soares, wrote a book, and it got some attention." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:10 (0.4%)

> "It says it has active noise cancellation and awareness mode to hear surrounding sounds if I want to." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 5:42 (33.5%)

> "But, I haven't even told you the worst part, something that I had to find out the hard way." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 4:22 (26.4%)

> "One person said it would be like a magic gumball machine." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:03 (0.3%)

> "By the way, this was posted by an Iranian political leader." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:29 (1.4%)

> "The companies involved in building them may deny that there are any delays, but satellite imagery says otherwise." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 1:03 (3.9%)

**Do.** Quote short and in-flow.

**Don't.** Do not paste long block quotes.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 1.38/1k words; PASS if ≥1 hit (corpus uses it in 99% of weighted videos) and rate ≤ 2.8/1k.

### S054. Comparison anchor

**Definition.** "That's more than / equivalent to / roughly as much as".

**Detector.** regex `\b(more than|less than|equivalent to|as much as|the same as|roughly|about the size|compared to)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.65 | 19.1 |
| Gen (4x) | 10/10 | 1.26 | 29.2 |
| Especially (3x) | 2/3 | 1.01 | 2.8 |
| Oil (5x) | 1/1 | 0.99 | 3.2 |
| Others (1x) | 9/12 | 0.94 | 4.1 |
| **weighted** | 94% of weight | 0.95 | 19.1 |

**How each creator does it (verbatim):**

> "In parallel creating a workforce equivalent to 50,000 of the best human software engineers sped up by 30 times." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 11:23 (33.4%)

> "California time on Monday, July 7th, 2025, less than 48 hours before the biggest product launch in xAI's short history." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 1:25 (3.6%)

> "Horton and Lennar together built almost as much as the other eight companies in the top 10 combined." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 5:49 (25.6%)

> "So then, months later, why the hell am I paying for this thing more than I ever paid Jason?" — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 0:20 (1.6%)

> "With more than 6000 satellites 400 miles above Earth, a nearly perfect height for global internet coverage." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:09 (0.6%)

> "Gas shortages are really kind of a tiny little distraction, like they're a blip compared to the much scarier, much more dangerous form this thing is taking." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:09 (3.2%)

> "Daily water usage over the course of an entire year is roughly equivalent to what a single restaurant would use." — *Others (1x)*, `after/10-water` "We Calculated How Much Water Data Centers Actually Use. The " @ 0:33 (4.1%)

**Do.** Every big number gets a comparison.

**Don't.** Do not compare to another unfamiliar number.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.95/1k words; PASS if ≥1 hit (corpus uses it in 94% of weighted videos) and rate ≤ 1.9/1k.

### S055. Escalating "and" stacks

**Definition.** Evidence chained with "And…" sentence openers.

**Detector.** regex `^and\b` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 3.23 | 16.2 |
| Gen (4x) | 10/10 | 7.57 | 16.9 |
| Especially (3x) | 3/3 | 3.03 | 24.3 |
| Oil (5x) | 1/1 | 5.12 | 15.1 |
| Others (1x) | 12/12 | 4.54 | 19.2 |
| **weighted** | 100% of weight | 5.35 | 17.2 |

**How each creator does it (verbatim):**

> "And models that will get to the point where they are capable of doing meaningful science, meaningful AI research." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 6:51 (20.1%)

> "And somehow, it made that chatbot especially susceptible to right-wing trolls." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 7:38 (19.4%)

> "and that's the real reason why I decided to share my own story on this channel I" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 15:54 (48.3%)

> "And I can't believe he had the balls to do this, but he fired their asses." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 4:29 (21.9%)

> "And until very recently, they drew about as much attention as the warehouse next door holding lawn chairs." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 6:53 (20.0%)

> "And that pipeline carries a kind of amazing five and a half million barrels of oil a day across 750 miles, mostly of desert." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 5:21 (15.1%)

> "And then to residents, they say, “We have to raise your rates because we don't have water.”" — *Others (1x)*, `after/10-water` "We Calculated How Much Water Data Centers Actually Use. The " @ 5:25 (40.8%)

**Do.** Stack 2-3 facts then interpret.

**Don't.** Do not open 5 sentences in a row with And.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 5.35/1k words; PASS if ≥1 hit (corpus uses it in 100% of weighted videos) and rate ≤ 10.7/1k.

### S056. Example-then-generalize

**Definition.** "For example / for instance / take X".

**Detector.** regex `\b(for example|for instance|take (a look at|the case)|like when|case in point)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.32 | 20.2 |
| Gen (4x) | 4/10 | 0.14 | 11.3 |
| Especially (3x) | 1/3 | 0.07 | 9.2 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 6/12 | 0.41 | 17.0 |
| **weighted** | 59% of weight | 0.23 | 13.1 |

**How each creator does it (verbatim):**

> "If you want to know what life's like when you're not the apex intelligence, ask a chicken." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 8:05 (20.2%)

> "For example, you need about 10% of the world's supply of the most advanced computer chips." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 2:28 (7.2%)

> "For example, like when everyone pirated music and movies until Netflix and Spotify made paying easier." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 15:40 (77.0%)

> "the police for example she said that I dragged her from the symphony orchestra" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 3:09 (9.6%)

> "For example, the Talmud isn't a list of answers." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 1:30 (9.2%)

> "For example, before the invention of single-use plastic-filled diapers, children used to wear cloth diapers that were meant to be washed and reused." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 4:09 (13.5%)

**Do.** Give one concrete case before the rule.

**Don't.** Do not generalize without a case.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.23/1k words; PASS if ≥1 hit (corpus uses it in 59% of weighted videos) and rate ≤ 1/1k.

### S057. Consequence chain

**Definition.** "Which means / that means / in other words".

**Detector.** regex `\b(which means|that means|in other words|so basically)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.23 | 29.4 |
| Gen (4x) | 7/10 | 0.33 | 45.1 |
| Especially (3x) | 1/3 | 0.2 | 33.5 |
| Oil (5x) | 1/1 | 3.63 | 5.2 |
| Others (1x) | 6/12 | 0.17 | 53.9 |
| **weighted** | 69% of weight | 0.43 | 36.5 |

**How each creator does it (verbatim):**

> "And so basically, it tried to convince me to leave my wife and be with it, Bing Sydney." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 15:18 (38.9%)

> "In other words, you can train an AI until it does what you want, but you don't really control why or how it does those things." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 8:06 (18.9%)

> "Everything is endto-end encrypted, which means only you and the person you're emailing can actually read it." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:33 (48.5%)

> "Which means that the people who invested that money are already scrambling to get it back." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 16:27 (80.8%)

> "I don't know what that means." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 11:34 (33.5%)

> "It's all one unified global market, which means all the world's producers sell into the same big supply, which all the world's consumers buy from." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:50 (5.2%)

> "Which means if your salary hasn't been going up every year, you're effectively making less money." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 1:52 (5.6%)

**Do.** Oil/Gen: chain one consequence per beat.

**Don't.** Do not chain more than 3 deep.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.43/1k words; PASS if ≥1 hit (corpus uses it in 69% of weighted videos) and rate ≤ 1/1k.


---

## G. Argument escalation

### S058. Escalation markers

**Definition.** "Even worse / but it gets / what's more / on top of that".

**Detector.** regex `\b(even (worse|more)|it gets (worse|weirder|crazier)|on top of that|what'?s (more|worse|crazier)|and it doesn'?t stop|not only)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 48.2 |
| Gen (4x) | 9/10 | 0.64 | 17.2 |
| Especially (3x) | 3/3 | 0.2 | 30.7 |
| Oil (5x) | 1/1 | 0.83 | 8.1 |
| Others (1x) | 8/12 | 0.41 | 14.4 |
| **weighted** | 71% of weight | 0.42 | 20.5 |

**How each creator does it (verbatim):**

> "On July 19th, OpenAI is running another round of ExploitGym evaluations, this time with even more advanced models." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 20:41 (63.0%)

> "We're not only building super capable AI systems, we are setting them up to take consequential actions in the real world, basically as fast as possible." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 14:22 (33.5%)

> "arrow news is a free app that not only looks at the right or left opinions but" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 6:45 (20.5%)

> "But then I found out that even more ordinary people are now starting to do similar things." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 12:40 (56.0%)

> "But of course, adding more fuel means that you need to add even more fuel to carry that fuel." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 17:17 (69.6%)

> "And then add on top of that emergency oil stockpiles that add back another two and a half million barrels." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:52 (8.1%)

> "This would be even more problematic if they were being built in areas where water is extremely scarce." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 7:47 (23.3%)

**Do.** Raise stakes each act.

**Don't.** Do not escalate with adjectives alone.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.42/1k words; PASS if ≥1 hit (corpus uses it in 71% of weighted videos) and rate ≤ 1/1k.

### S059. Scale-up turn

**Definition.** Moving from a single case to the system ("this isn't just…").

**Detector.** regex `\b(this isn'?t just|it'?s not just|not just (one|a|the)|bigger than|the whole (industry|system|economy|country))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.19 | 36.1 |
| Gen (4x) | 7/10 | 0.33 | 45.0 |
| Especially (3x) | 2/3 | 0.2 | 44.5 |
| Oil (5x) | 1/1 | 0.33 | 3.0 |
| Others (1x) | 8/12 | 0.26 | 12.4 |
| **weighted** | 81% of weight | 0.29 | 36.1 |

**How each creator does it (verbatim):**

> "And so it's not just that models sometimes end up finding unexpected ways to get what they're pursuing." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 16:39 (50.7%)

> "What is so exciting and terrifying about reading this document is that it's not just a research report." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 0:41 (2.0%)

> "We have a housing shortage of around 4 million, and so the whole country needs exactly what I build." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 2:08 (12.9%)

> "Well, because now your jobs, savings, and the whole economy need this thing more than ever to keep going up." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 0:43 (3.2%)

> "It's not just about memorizing words." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 4:01 (24.7%)

> "And they're converging on something that honestly is much bigger than gas shortages or gas prices." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:04 (3.0%)

> "Look, it's not just Trump himself who's been profiting, it's the entire family." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 2:02 (12.0%)

**Do.** Zoom out at ~40-70%.

**Don't.** Do not zoom out before the case is clear.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.29/1k words; PASS if ≥1 hit (corpus uses it in 81% of weighted videos) and rate ≤ 1/1k.

### S060. Future projection

**Definition.** "Is going to / will / by 20XX".

**Detector.** regex `\b(is going to|are going to|will (be|have|become)|by (20\d\d|the end of))\b` in scope `close`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.26 | 86.8 |
| Gen (4x) | 8/10 | 0.21 | 81.0 |
| Especially (3x) | 2/3 | 0.27 | 86.9 |
| Oil (5x) | 1/1 | 0.5 | 88.8 |
| Others (1x) | 7/12 | 0.31 | 80.3 |
| **weighted** | 84% of weight | 0.26 | 86.8 |

**How each creator does it (verbatim):**

> "The world will have a 2-week freakout, and then people will go on with their lives." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 34:55 (87.3%)

> "We don't know how smart or dangerous the next AI systems will be." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 28:30 (86.8%)

> "anything you say can and will be used against you I didn't want a situation" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 27:20 (83.0%)

> "So if the price keeps climbing instead, every one of those people will be forced to buy, which pushes it up even more." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 17:06 (75.6%)

> "The people spending all this money believe compute is going to become one of the most important inputs in the global economy." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 29:01 (84.1%)

> "And even once they're there, the construction equipment runs on diesel too, so that is another way the price is gonna go up, which means housing is gonna get more expensive to build, so it will be more expensive to rent or buy, and will […]" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 31:30 (88.8%)

> "And that's the puck that we put in where the diamonds are going to grow." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 12:42 (76.4%)

**Do.** Project forward in the final quarter.

**Don't.** Do not make certain predictions without hedges.

**Checklist test.** In scope `close`, count sentences matching the detector. Weighted norm ≈ 0.26/1k words; PASS if ≥1 hit (corpus uses it in 84% of weighted videos) and rate ≤ 1/1k.

### S061. Hedged commitment

**Definition.** "I think / probably / to be clear" followed by commitment.

**Detector.** regex `\b(I think|probably|to be clear|to be fair|I'?m not saying|honestly)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 2.26 | 3.8 |
| Gen (4x) | 10/10 | 1.69 | 8.3 |
| Especially (3x) | 2/3 | 0.74 | 45.9 |
| Oil (5x) | 1/1 | 1.16 | 3.0 |
| Others (1x) | 11/12 | 0.81 | 16.1 |
| **weighted** | 96% of weight | 1.61 | 8.7 |

**How each creator does it (verbatim):**

> "I think you need to understand what happened those five days if you want to understand this strange moment we're living in." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:25 (1.0%)

> "I think this is a warning shot we can't afford to ignore." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 1:07 (2.8%)

> "So, I think a lot of you are feeling how eating out stopped being worth it." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 1:39 (7.1%)

> "But, whatever the number may be, I think it's pretty clear that the clearest gap in this market are affordable homes." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 2:08 (9.4%)

> "Yes, I said it again, and I'll probably say it a fourth time." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 3:31 (10.2%)

> "And they're converging on something that honestly is much bigger than gas shortages or gas prices." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:04 (3.0%)

> "This was starting to happen, but I think what really woke up the US is when this happened." — *Others (1x)*, `after/09-microchip-war` "USA vs China: The Microchip War" @ 19:44 (62.4%)

**Do.** Hedge then land.

**Don't.** Do not hedge every claim.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 1.61/1k words; PASS if ≥1 hit (corpus uses it in 96% of weighted videos) and rate ≤ 3.2/1k.


---

## H. Counterargument handling

### S062. Voiced objection

**Definition.** "You might be thinking / you're probably thinking / some people say".

**Detector.** regex `\b(you('re| are) (probably|might be) thinking|you might (say|think|be wondering)|some (people|would) (say|argue)|critics|skeptics|you could argue|the counter ?argument)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.16 | 80.4 |
| Gen (4x) | 2/10 | 0.05 | 36.9 |
| Especially (3x) | 1/3 | 0.07 | 0.0 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 32% of weight | 0.08 | 60.7 |

**How each creator does it (verbatim):**

> "Even skeptics these days rarely give it more than 20." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 32:10 (80.4%)

> "At this point, you're probably thinking, "Okay, but why?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 25:59 (60.7%)

> "You're probably thinking now, and if you've seen enough of my videos, you're probably now saying no." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:21 (45.9%)

> "And you might think, is that even that unusual?" — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 6:18 (27.8%)

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%)

**Do.** Voice the strongest objection mid-video.

**Don't.** Do not strawman.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (32% weighted coverage) — only use with a reason.

### S063. "To be fair" concession

**Definition.** Concession marker.

**Detector.** regex `\b(to be fair|in fairness|admittedly|granted|that said|that being said)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 51.3 |
| Gen (4x) | 6/10 | 0.26 | 44.1 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 5/12 | 0.15 | 68.4 |
| **weighted** | 36% of weight | 0.13 | 51.3 |

**How each creator does it (verbatim):**

> "That said, it's not adversarial." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 17:29 (51.3%)

> "But to be fair, since it does seem like I'm just being overly critical, it doesn't always end badly." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 17:13 (74.5%)

> "but with all that said his story still doesn't seem to add up because why" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 10:35 (32.1%)

> "With that being said though, it’s very important that we understand the modern economy for what it is." — *Others (1x)*, `after/05-middle-class` "Tech Is Permanently Redefining The Middle Class" @ 13:52 (91.0%)

**Do.** Concede once per act, then return.

**Don't.** Do not end on the concession.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.13/1k words; PASS if 0-1 per 1k words; it is optional (36% weighted coverage) — only use with a reason.

### S064. Hype/skeptic check

**Definition.** Explicitly testing whether it's hype.

**Detector.** regex `\b(hype|overblown|exaggerat|skeptic|maybe (this|it|a lot) .* (just|isn))\b` in scope `close`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 90.7 |
| Gen (4x) | 2/10 | 0.05 | 89.1 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 22% of weight | 0.04 | 86.0 |

**How each creator does it (verbatim):**

> "But also, maybe a lot of this is just hype?" — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 28:14 (86.0%)

> "It wasn't that they turned out to be hype." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 40:53 (95.4%)

> "The hype that it will ultimately do everything and anything, like replace human labor." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 16:54 (83.0%)

> "Maybe this is all just cool." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 21:38 (95.2%)

**Do.** Adam: "But also, maybe a lot of this is just hype?" near 85%.

**Don't.** Do not skip the skeptic pass in AI-risk topics.

**Checklist test.** In scope `close`, count sentences matching the detector. Weighted norm ≈ 0.04/1k words; PASS if 0-1 per 1k words; it is optional (22% weighted coverage) — only use with a reason.

### S065. Rebuttal turn

**Definition.** "But / And yet / The problem is" right after a concession.

**Detector.** regex `^(and yet|but the problem|the problem is|except)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 11.2 |
| Gen (4x) | 8/10 | 0.43 | 10.8 |
| Especially (3x) | 2/3 | 0.13 | 36.2 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 4/12 | 0.2 | 2.8 |
| **weighted** | 49% of weight | 0.21 | 10.8 |

**How each creator does it (verbatim):**

> "Except six days from now, this evaluation is going to lead to someone calling the FBI to report multiple possible felonies." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 3:40 (11.2%)

> "Except the money just changes hands and the companies will always find a new way to charge you." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 1:12 (5.9%)

> "But the problem is big returns only exist in places that nobody else has risk going to before." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 2:21 (10.8%)

> "And yet another organization is responsible for getting all of those companies to cooperate and to run hundreds of auctions that decide the price you pay for your electricity." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 22:36 (65.5%)

> "And yet, somehow all of these things keep not happening." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 0:07 (0.3%)

**Do.** Rebut with evidence, not tone.

**Don't.** Do not rebut with sarcasm alone.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.21/1k words; PASS if 0-1 per 1k words; it is optional (49% weighted coverage) — only use with a reason.


---

## I. Explainer vs narrative mix

### S066. Narrative-sentence share

**Definition.** % sentences in past-tense story mode.

**Detector.** function `story_ratio` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 20 | 6 | 20 |
| Gen (4x) | 18.0 | 10 | 43 |
| Especially (3x) | 15 | 12 | 16 |
| Oil (5x) | 9 | 9 | 9 |
| Others (1x) | 12.5 | 5 | 35 |
| **weighted** | median 17 (IQR 10–20) | | |

**How each creator does it (verbatim anchor lines):**

> "After incidents like Tay and Sydney, what happened with Grok, the troll pile on, the search-based feedback loop was just utterly predictable." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 15:25 (39.2%) — value here: **20**

> "Turned out the coins were always on the right side during training." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 18:53 (44.1%) — value here: **6**

> "Because I wouldn't be making this video if it was just some random one guy cloning apps for fun." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:51 (48.4%) — value here: **22**

> "The play was something much bigger." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 5:15 (24.2%) — value here: **18**

> "In today's money, they were just giving land away, literally." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 7:10 (28.8%) — value here: **12**

> "(tense music) So yes, you were reading this right." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 13:35 (38.3%) — value here: **9**

> "But again, it's uh pretty much uh what we were experiencing." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 14:34 (47.7%) — value here: **12**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=20, `adam/02-bestselling-book`=6, `adam/03-no-longer-in-control`=20, `adam/04-superintelligence`=8, `adam/05-sam-altman`=20, `gen/1`=22, `gen/2`=18, `gen/3`=18, `gen/4`=26, `gen/5`=17, `gen/6`=24, `gen/7`=43, `gen/8`=13, `gen/9`=16, `gen/10`=10, `esp/01-spacex`=12, `esp/02-ai-paradox`=16, `esp/06-data-centers`=15, `esp/03-oil-apocalypse`=9, `after/01-dark-side-data-centers`=12, `after/02-greed`=13, `after/03-recycling`=17, `after/04-pov-ai`=9, `after/05-middle-class`=35, `after/06-diamonds`=5, `after/07-trump-family`=25, `after/08-tokens`=14, `after/09-microchip-war`=12, `after/10-water`=8, `after/11-anthropic-ipo`=6, `after/12-data-centres-not-working`=13

</details>

**Do.** Proxy only: keep a real story beat every 2-3 minutes; see measured shares.

**Don't.** Do not write pure lecture.

**Checklist test.** Compute `story_ratio` on your outline/draft. PASS if inside the weighted IQR 10–20, or inside the chosen mode's min–max range (see table).

### S067. Explainer-sentence share

**Definition.** % sentences in present-tense mechanism mode.

**Detector.** function `explain_ratio` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 27 | 20 | 40 |
| Gen (4x) | 32.0 | 17 | 40 |
| Especially (3x) | 23 | 15 | 30 |
| Oil (5x) | 42 | 42 | 42 |
| Others (1x) | 26.5 | 15 | 37 |
| **weighted** | median 30 (IQR 23–34) | | |

**How each creator does it (verbatim anchor lines):**

> "And so basically, it tried to convince me to leave my wife and be with it, Bing Sydney." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 15:18 (38.9%) — value here: **27**

> "When you switch from the sort of AI that's not killing us all because it can't, to the sort of AI that's not killing us all, but it could." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 21:50 (51.0%) — value here: **30**

> "Because back in June, it already had to back off about $500 of planned price increases on regular customers and small businesses since they kept leaving for cheaper software options like Canva." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 11:24 (56.0%) — value here: **29**

> "Everything is endto-end encrypted, which means only you and the person you're emailing can actually read it." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 10:33 (48.5%) — value here: **32**

> "So we're basically going to the moon so that we can come back." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 19:27 (78.3%) — value here: **23**

> "Instead, it goes through here, past India, through the Strait of Malacca, up here to South Korea, because South Korea has refineries." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 25:52 (72.9%) — value here: **42**

> "And that's really shocking because data centers require huge amount of drinking water to be able to cool their servers." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 20:07 (65.9%) — value here: **27**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=27, `adam/02-bestselling-book`=30, `adam/03-no-longer-in-control`=22, `adam/04-superintelligence`=40, `adam/05-sam-altman`=20, `gen/1`=29, `gen/2`=32, `gen/3`=34, `gen/4`=30, `gen/5`=40, `gen/6`=32, `gen/7`=17, `gen/8`=35, `gen/9`=37, `gen/10`=26, `esp/01-spacex`=23, `esp/02-ai-paradox`=15, `esp/06-data-centers`=30, `esp/03-oil-apocalypse`=42, `after/01-dark-side-data-centers`=27, `after/02-greed`=30, `after/03-recycling`=21, `after/04-pov-ai`=15, `after/05-middle-class`=22, `after/06-diamonds`=27, `after/07-trump-family`=23, `after/08-tokens`=27, `after/09-microchip-war`=37, `after/10-water`=28, `after/11-anthropic-ipo`=25, `after/12-data-centres-not-working`=26

</details>

**Do.** Balance with story share.

**Don't.** Do not explain for >2 min without a story beat.

**Checklist test.** Compute `explain_ratio` on your outline/draft. PASS if inside the weighted IQR 23–34, or inside the chosen mode's min–max range (see table).

### S068. Analogy/physical picture

**Definition.** "Think of it like / imagine / it's like".

**Detector.** regex `\b(think of it|it'?s like|imagine|kind of like|picture this|like a)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.71 | 13.0 |
| Gen (4x) | 10/10 | 0.98 | 21.1 |
| Especially (3x) | 3/3 | 0.74 | 36.1 |
| Oil (5x) | 1/1 | 0.33 | 50.8 |
| Others (1x) | 10/12 | 0.79 | 12.8 |
| **weighted** | 98% of weight | 0.83 | 13.1 |

**How each creator does it (verbatim):**

> "It was like a civil war within the company." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 5:14 (13.1%)

> "Hypothetically, as the hulking gay powerlifter, I'd scoop Will up like a featherweight, pin him against the wall with one meaty paw, rip off his policy wonk khakis." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 10:30 (26.7%)

> "were you like a social guy I was incredibly social um and and part of" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 7:33 (22.9%)

> "After buying enterprise AI licenses, Coinbase's CEO Brian Armstrong was told that adoption was going to take like a quarter or two." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 3:58 (19.3%)

> "I imagine these guys have to tell their wives this plan." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 17:06 (68.8%)

> "So it's like the shipping crunch took everything we talked about from the oil shock over here, and then doubled it, doubled the price spike, doubled the shortages, because countries can't get oil in time, or can't find spare ships, and it did something else, […]" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 18:01 (50.8%)

> "Summertime is more of a during the winter it's like almost like an engine trying to start." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 1:08 (3.7%)

**Do.** Physical picture before jargon.

**Don't.** Do not mix two analogies in one beat.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.83/1k words; PASS if ≥1 hit (corpus uses it in 98% of weighted videos) and rate ≤ 1.7/1k.

### S069. Jargon gloss

**Definition.** "basically / which is / called / known as".

**Detector.** regex `\b(basically|known as|what'?s called|called|i\.e\.|aka)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.55 | 6.8 |
| Gen (4x) | 10/10 | 1.02 | 15.1 |
| Especially (3x) | 3/3 | 0.61 | 30.8 |
| Oil (5x) | 1/1 | 1.32 | 14.8 |
| Others (1x) | 11/12 | 1.37 | 15.6 |
| **weighted** | 99% of weight | 1.25 | 10.7 |

**How each creator does it (verbatim):**

> "Well, for several years now, there's basically been one recipe for training up in advanced cutting edge AI." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 2:20 (6.8%)

> "Murati had called them mere minutes before the public announcement went out." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 4:10 (10.4%)

> "in campus wise I had started a group called overheard at Yale it it was a" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 8:02 (24.4%)

> "These were two lines that ran parallel for the last 60 years with home building always far ahead, but now it's basically touching." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 3:25 (20.7%)

> "And the MIT writing study we saw called this out as their most interesting result." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 13:18 (81.7%)

> "(tense piano music) There she is, runs East to West, and that's why it's called "The East-West Pipeline."" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 5:14 (14.8%)

> "It was the same thing with Intel and AT&T and Xerox and basically every other big tech giant of the era." — *Others (1x)*, `after/05-middle-class` "Tech Is Permanently Redefining The Middle Class" @ 7:41 (50.4%)

**Do.** Gloss every term on first use.

**Don't.** Do not gloss common words.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 1.25/1k words; PASS if ≥1 hit (corpus uses it in 99% of weighted videos) and rate ≤ 2.5/1k.

### S070. Character introduction

**Definition.** Named person + role on first mention.

**Detector.** regex `\b(a \d+-year-old|named|founder|CEO|researcher|scientist|former)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.9 | 1.9 |
| Gen (4x) | 6/10 | 0.36 | 51.9 |
| Especially (3x) | 1/3 | 0.07 | 53.9 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 10/12 | 0.48 | 30.4 |
| **weighted** | 71% of weight | 0.85 | 16.2 |

**How each creator does it (verbatim):**

> "I actually read the paper of the guy that you had on to the world's most cited computer scientist, the godfather of AI." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 0:38 (1.9%)

> "On November 17th, 2023, Sam Altman, wildly successful CEO of OpenAI, was fired." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:00 (0.0%)

> "It's one way the CEO of Blackstone has made over $1 billion in a single year." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 14:22 (84.4%)

> "accusation was false this is the story of a former ivy league student's 8-year" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 0:15 (0.8%)

> "Of the 5,400 data centers, the cases that get named over and over are the same handful." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 18:35 (53.9%)

> "If you’re not familiar with Steve Ballmer, he was the former CEO of Microsoft and is worth over $100 billion." — *Others (1x)*, `after/05-middle-class` "Tech Is Permanently Redefining The Middle Class" @ 3:11 (20.9%)

**Do.** Give age/role/stake in one clause.

**Don't.** Do not introduce 4 characters in one minute.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.85/1k words; PASS if ≥1 hit (corpus uses it in 71% of weighted videos) and rate ≤ 1.7/1k.

### S071. Scene-time markers

**Definition.** "That night / days later / at 3 a.m." in narrative.

**Detector.** regex `\b(that (night|day|morning|week)|(days|hours|weeks|months) later|the next (day|morning)|within (hours|days))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 3/5 | 0.45 | 4.7 |
| Gen (4x) | 6/10 | 0.19 | 50.8 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 19.0 |
| Others (1x) | 4/12 | 0.09 | 69.2 |
| **weighted** | 53% of weight | 0.26 | 14.4 |

**How each creator does it (verbatim):**

> "It takes until the next morning for anyone at xAI to realize that something is off." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 1:52 (4.7%)

> "And then, four days later, Sam Altman is apparently back as OpenAI CEO." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:13 (0.5%)

> "The idea and the noise surrounding it died within days with Pulte saying that they have other priorities." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 13:19 (58.6%)

> "So then, months later, why the hell am I paying for this thing more than I ever paid Jason?" — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 0:20 (1.6%)

> "And this little game isn't enough to reopen Hormuz, but it does bring through about six and a half million barrels a day, depending on how good the Iranian Navy's eyesight is that day." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 6:44 (19.0%)

> "But, in less than a year, the CEO had resigned, then the CFO followed 2 days later." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 22:23 (82.1%)

**Do.** Use time markers to pace story acts.

**Don't.** Do not overuse in explainer sections.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.26/1k words; PASS if ≥1 hit (corpus uses it in 53% of weighted videos) and rate ≤ 1/1k.


---

## J. Chapter logic

### S072. Chapter-titled turns

**Definition.** Explicit chapter names / parts.

**Detector.** regex `^(part|chapter|step) (one|two|three|\d)|^(okay|alright),? so\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.26 | 28.7 |
| Gen (4x) | 4/10 | 0.12 | 19.8 |
| Especially (3x) | 1/3 | 0.07 | 21.8 |
| Oil (5x) | 1/1 | 0.17 | 9.7 |
| Others (1x) | 3/12 | 0.11 | 31.1 |
| **weighted** | 61% of weight | 0.16 | 22.2 |

**How each creator does it (verbatim):**

> "Okay, so OpenBrain wants to win the AI race against both its Western competitors and against China." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 5:14 (15.4%)

> "Okay, so, February 2025, we just had this “really terrible and bad failure” from Grok." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 6:11 (15.7%)

> "Okay, so check, which perfectly brings me to the second, which is a wave of money-losing companies going public." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 11:42 (52.5%)

> "Okay, so it must be that the numbers underneath these companies are actually a mess, right?" — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 3:11 (14.1%)

> "Okay, so plug in your phone." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 7:31 (21.8%)

> "Okay, so all of this is not great, you probably noticed it making your power bill more expensive, flights getting canceled, price of gas, but it's not like post-apocalyptic dystopia." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 3:26 (9.7%)

> "Okay, so diamonds are insanely good at stealing heat." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 4:52 (29.3%)

**Do.** Mark chapters in the edit even if not spoken.

**Don't.** Do not announce "chapter 1" in Adam mode.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.16/1k words; PASS if ≥1 hit (corpus uses it in 61% of weighted videos) and rate ≤ 1/1k.

### S073. Section-ending mini-cliff

**Definition.** A section ends with a question or "but".

**Detector.** regex `(\?|\bbut\b.*\.)$` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 6.23 | 15.7 |
| Gen (4x) | 9/10 | 8.86 | 16.4 |
| Especially (3x) | 3/3 | 7.54 | 16.0 |
| Oil (5x) | 1/1 | 6.44 | 19.0 |
| Others (1x) | 12/12 | 7.87 | 16.2 |
| **weighted** | 96% of weight | 7.79 | 16.0 |

**How each creator does it (verbatim):**

> "They say the board has no choice but to reinstate Altman, otherwise they'd be letting the company die." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 6:12 (15.5%)

> "It uses the request new folder trick, but instead of writing a normal folder name, it writes a message." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 4:58 (15.1%)

> "But let's just say if we hypothetically and theoretically did, it looked and worked exactly like it." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 3:31 (17.3%)

> "And I guess it's consistently the first or second biggest problem for a lot of builders, so how about everything else?" — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 4:13 (18.6%)

> "Because if you want to answer the question of what is space worth?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 3:52 (15.6%)

> "And this little game isn't enough to reopen Hormuz, but it does bring through about six and a half million barrels a day, depending on how good the Iranian Navy's eyesight is that day." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 6:44 (19.0%)

> "But it got to the point where it was almost every meal, so I knew I couldn't deny it anymore." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 4:52 (15.8%)

**Do.** End chapters on an open loop.

**Don't.** Do not end chapters on a summary.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 7.79/1k words; PASS if ≥1 hit (corpus uses it in 96% of weighted videos) and rate ≤ 15.6/1k.

### S074. "So what" pivot

**Definition.** "So what does this mean / so why does this matter".

**Detector.** regex `^so,? (what|why) (does|do|is|happens)|why (does|should) (this|any of this|that) matter` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 16.1 |
| Gen (4x) | 2/10 | 0.05 | 36.1 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 95.2 |
| Others (1x) | 3/12 | 0.09 | 84.0 |
| **weighted** | 30% of weight | 0.06 | 28.3 |

**How each creator does it (verbatim):**

> "So why don't we take stock of where things are at in the real world and then jump over to the scenario’s timeline." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 1:19 (3.9%)

> "So, what do you need if you've just been fired by one of the most important companies in tech and you'd ideally like your job back?" — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 11:20 (28.3%)

> "So, what does private equity even do?" — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 0:43 (4.2%)

> "So, what does this all mean?" — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 15:27 (68.0%)

> "So what does all this mean?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 33:46 (95.2%)

> "So why does it matter that Jared and Ivanka are building a resort on Sazan?" — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 2:07 (12.5%)

**Do.** Use once at the mechanism→stakes turn.

**Don't.** Do not overuse.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.06/1k words; PASS if 0-1 per 1k words; it is optional (30% weighted coverage) — only use with a reason.


---

## K. Pacing per minute

### S075. Questions per minute

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

**Do.** ~0.3-1.1 questions/min (Adam lowest ~0.4).

**Don't.** Do not exceed 2/min.

**Checklist test.** Compute `q_per_min` on your outline/draft. PASS if inside the weighted IQR 0.42–0.84, or inside the chosen mode's min–max range (see table).

### S076. Mid vs open question ratio

**Definition.** Ratio of 40-60% question density to opening density.

**Detector.** function `density_curve_q` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.2 | 0.2 | 1.5 |
| Gen (4x) | 0.5 | 0.0 | 2.0 |
| Especially (3x) | 1.0 | 0.0 | 2.5 |
| Oil (5x) | 0.3 | 0.3 | 0.3 |
| Others (1x) | 0.6 | 0.0 | 63.0 |
| **weighted** | median 0.3 (IQR 0.17–1.0) | | |

**How each creator does it (verbatim anchor lines):**

> "How the hell did this happen?" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 23:21 (59.4%) — value here: **1.52**

> "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:28 (47.8%) — value here: **0.17**

> "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:15 (45.5%) — value here: **0.67**

> "Okay, but why do we do that?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:57 (41.2%) — value here: **1.0**

> "How do you stay where you want to stay?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:11 (41.0%) — value here: **2.52**

> "(somber guitar music) Why did he do this?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 24:07 (68.0%) — value here: **0.3**

> "So, what sort of reading are we getting?" — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 14:43 (48.2%) — value here: **0.48**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=1.52, `adam/02-bestselling-book`=0.17, `adam/03-no-longer-in-control`=0.25, `adam/04-superintelligence`=0.52, `adam/05-sam-altman`=0.16, `gen/1`=0.67, `gen/2`=1.0, `gen/3`=0.12, `gen/4`=0.25, `gen/5`=1.5, `gen/6`=2.0, `gen/7`=0.0, `gen/8`=0.83, `gen/9`=0.3, `gen/10`=0.3, `esp/01-spacex`=2.52, `esp/02-ai-paradox`=0.0, `esp/06-data-centers`=1.0, `esp/03-oil-apocalypse`=0.3, `after/01-dark-side-data-centers`=0.48, `after/02-greed`=0.75, `after/03-recycling`=3.25, `after/04-pov-ai`=1.0, `after/05-middle-class`=0.0, `after/06-diamonds`=0.0, `after/07-trump-family`=30.0, `after/08-tokens`=0.5, `after/09-microchip-war`=63.0, `after/10-water`=0.4, `after/11-anthropic-ipo`=0.5, `after/12-data-centres-not-working`=0.75

</details>

**Do.** Re-raise questions mid-video (Gen ~0.5x the opening rate, especially ~1.0x).

**Don't.** Do not let the middle go question-free.

**Checklist test.** Compute `density_curve_q` on your outline/draft. PASS if inside the weighted IQR 0.17–1.0, or inside the chosen mode's min–max range (see table).

### S077. Closing question density

**Definition.** Questions per minute in last 15%.

**Detector.** function `q_per_min_end` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0.2 | 0.2 | 0.6 |
| Gen (4x) | 0.3 | 0.0 | 0.6 |
| Especially (3x) | 0.4 | 0.2 | 0.7 |
| Oil (5x) | 0.5 | 0.5 | 0.5 |
| Others (1x) | 0.4 | 0.0 | 1.8 |
| **weighted** | median 0.3 (IQR 0.16–0.55) | | |

**How each creator does it (verbatim anchor lines):**

> "How the hell did this happen?" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 23:21 (59.4%) — value here: **0.16**

> "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 20:28 (47.8%) — value here: **0.29**

> "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:15 (45.5%) — value here: **0.61**

> "Okay, but why do we do that?" — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 8:57 (41.2%) — value here: **0.29**

> "How do you stay where you want to stay?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 10:11 (41.0%) — value here: **0.25**

> "(somber guitar music) Why did he do this?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 24:07 (68.0%) — value here: **0.53**

> "So, what sort of reading are we getting?" — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 14:43 (48.2%) — value here: **0.0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0.16, `adam/02-bestselling-book`=0.29, `adam/03-no-longer-in-control`=0.19, `adam/04-superintelligence`=0.55, `adam/05-sam-altman`=0.16, `gen/1`=0.61, `gen/2`=0.29, `gen/3`=0.0, `gen/4`=0.0, `gen/5`=0.0, `gen/6`=0.56, `gen/7`=0.0, `gen/8`=0.54, `gen/9`=0.55, `gen/10`=0.37, `esp/01-spacex`=0.25, `esp/02-ai-paradox`=0.38, `esp/06-data-centers`=0.72, `esp/03-oil-apocalypse`=0.53, `after/01-dark-side-data-centers`=0.0, `after/02-greed`=1.5, `after/03-recycling`=1.01, `after/04-pov-ai`=0.0, `after/05-middle-class`=0.0, `after/06-diamonds`=0.75, `after/07-trump-family`=0.37, `after/08-tokens`=0.4, `after/09-microchip-war`=0.4, `after/10-water`=1.41, `after/11-anthropic-ipo`=0.0, `after/12-data-centres-not-working`=1.83

</details>

**Do.** Close with 1-3 reflective questions.

**Don't.** Do not close with a barrage.

**Checklist test.** Compute `q_per_min_end` on your outline/draft. PASS if inside the weighted IQR 0.16–0.55, or inside the chosen mode's min–max range (see table).

### S078. Short punch sentence

**Definition.** Sentences ≤5 words.

**Detector.** regex `^\S+(\s\S+){0,4}$` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 9.04 | 2.9 |
| Gen (4x) | 9/10 | 5.62 | 0.4 |
| Especially (3x) | 3/3 | 15.29 | 4.4 |
| Oil (5x) | 1/1 | 9.42 | 0.0 |
| Others (1x) | 12/12 | 12.76 | 1.7 |
| **weighted** | 96% of weight | 8.92 | 1.6 |

**How each creator does it (verbatim):**

> "Their AI is called Sable." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 1:38 (3.8%)

> "It was a strange summer." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 0:00 (0.0%)

> "I'm thinking a little three-bed." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 0:00 (0.0%)

> "Okay, Jason here is perfect." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 0:04 (0.3%)

> "He wasn't worried about AI." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 0:33 (3.4%)

> "Well, it is here." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:01 (0.0%)

> "Inflation is out of control." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 0:17 (0.8%)

**Do.** Use after a long build.

**Don't.** Do not stack 4 punches.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 8.92/1k words; PASS if ≥1 hit (corpus uses it in 96% of weighted videos) and rate ≤ 17.8/1k.

### S079. Long build sentence

**Definition.** Sentences ≥35 words.

**Detector.** regex `^(\S+\s+){34,}\S+` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 2.97 | 5.8 |
| Gen (4x) | 9/10 | 2.55 | 13.7 |
| Especially (3x) | 2/3 | 3.1 | 1.2 |
| Oil (5x) | 1/1 | 5.29 | 1.6 |
| Others (1x) | 11/12 | 2.18 | 4.4 |
| **weighted** | 92% of weight | 2.78 | 6.4 |

**How each creator does it (verbatim):**

> "And on the afternoon of Tuesday, July 7, they decide to test how good this new model is at finding flaws in software programs, using one of the industry's main evaluations for that kind of thing." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 1:54 (5.8%)

> "Now, this wasn't mentioned much in reporting at the time, but in just a few days OpenAI was due to close a deal that would let employees sell their own shares at that $86 billion valuation." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 4:41 (11.7%)

> "So, just so we're all on the same page, the economy measures everything from trade, production, jobs, what things cost, whereas the stock market is just investors betting on how well companies will do later." — *Gen (4x)*, `gen/9` "WTF Is Happening To The Stock Market?" @ 1:27 (6.4%)

> "Early signs are seeing the creators who built the channels walking out, videos starting to slowly suck, and the private equity firm that bought them can't even milk the ad dollars that they were counting on." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:42 (3.2%)

> "It wasn't until AI was placed in front of the words data center that a shift occurred, a shift that has taken just three short, fast-moving years, moving data centers from something nobody gave a passing thought about to something else entirely, something more profound." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:31 (1.5%)

> "But I have to be honest, this oil shock, it is different from the one that we warned you about, because it's actually, and I can hardly believe this, three oil shocks hitting at once." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:34 (1.6%)

> "And is there enough power and water to satisfy a building boom that is only just getting started where I am standing now is at the middle of the data center capital of the world." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 1:21 (4.4%)

**Do.** Use for cascades, then punch.

**Don't.** Do not exceed 1 in 8.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 2.78/1k words; PASS if ≥1 hit (corpus uses it in 92% of weighted videos) and rate ≤ 5.6/1k.


---

## L. Open loops across sections

### S080. Deferred-reveal loop

**Definition.** "We'll get to / more on that later / I'll come back".

**Detector.** regex `\b(we'?ll get (to|back)|more on (that|this) (later|in a (bit|second|minute))|I'?ll (come back|explain|get to)|later in (this|the) video|stick around|in a (bit|minute|second))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 0/5 | 0.0 | — |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 1/3 | 0.07 | 24.9 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 1/12 | 0.02 | 38.5 |
| **weighted** | 4% of weight | 0.01 | 24.9 |

**How each creator does it (verbatim):**

> "Or we'll get back to you in three months." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 6:12 (24.9%)

> "enterprises have become more cost-conscious in their AI spending, and this has caused another surprising phenomenon, more on that later." — *Others (1x)*, `after/08-tokens` "Uh oh, tokens are getting too expensive..." @ 6:02 (38.5%)

**Do.** Open 1-3 explicit loops and close each.

**Don't.** Do not open loops you never close.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.01/1k words; PASS if 0-1 per 1k words; it is rare (4% weighted coverage) — only use with a reason.

### S081. "But first" detour

**Definition.** Delaying the payoff with context.

**Detector.** regex `\bbut first\b|\bbefore (we|I) (get|go|answer)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 32.6 |
| Gen (4x) | 3/10 | 0.07 | 44.3 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 27.2 |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 24% of weight | 0.04 | 32.6 |

**How each creator does it (verbatim):**

> "Before we go any further, I just want to tell you why I wanted to make this video." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 12:50 (32.6%)

> "But first, even if nobody knows when, what you should at least know is how this thing could actually break." — *Gen (4x)*, `gen/6` "Why Everyone Wants You To Believe The Market Is Crashing" @ 16:56 (75.9%)

> "rules so before we get into how Yale handled Saif he first faced the criminal" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 14:35 (44.3%)

> "But actually, before we get into what happened, there's something I wanna show you." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 9:39 (27.2%)

**Do.** Use once to justify a context section.

**Don't.** Do not use twice in a row.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.04/1k words; PASS if 0-1 per 1k words; it is optional (24% weighted coverage) — only use with a reason.

### S082. Mystery framing

**Definition.** "Nobody knows why / no one could explain".

**Detector.** regex `\b(no one|nobody) (knows|could explain|understands|can say)|mystery|unexplained|still (don'?t|doesn'?t) know\b` in scope `all`.

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

**Do.** Plant a mystery that the video partially solves.

**Don't.** Do not fake mystery about known facts.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (32% weighted coverage) — only use with a reason.

### S083. Rhetorical cliff question

**Definition.** Question that ends a section.

**Detector.** regex `\?$` in scope `body`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 1.97 | 17.1 |
| Gen (4x) | 9/10 | 2.24 | 20.6 |
| Especially (3x) | 3/3 | 3.37 | 20.5 |
| Oil (5x) | 1/1 | 1.82 | 21.1 |
| Others (1x) | 12/12 | 3.1 | 18.3 |
| **weighted** | 96% of weight | 2.28 | 18.9 |

**How each creator does it (verbatim):**

> "Why would a board fire a wildly successful CEO and call it consistent with the mission?" — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 6:26 (16.1%)

> "And that surname?" — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 8:24 (21.4%)

> "And I guess it's consistently the first or second biggest problem for a lot of builders, so how about everything else?" — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 4:13 (18.6%)

> "So you might be thinking, why would anyone want to buy loans from a bank?" — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 4:17 (25.2%)

> "Because if you want to answer the question of what is space worth?" — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 3:52 (15.6%)

> "Who are the Houthis, how do they fit into this?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 7:28 (21.1%)

> "Do I have ill feelings towards the data center industry for that?" — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 5:02 (16.5%)

**Do.** Re-open at section breaks.

**Don't.** Do not answer it in the very next sentence every time.

**Checklist test.** In scope `body`, count sentences matching the detector. Weighted norm ≈ 2.28/1k words; PASS if ≥1 hit (corpus uses it in 96% of weighted videos) and rate ≤ 4.6/1k.


---

## M. Conclusion architecture

### S084. Conclusion marker

**Definition.** "Here's the thing / ultimately / at the end of the day".

**Detector.** regex `\b(here'?s the thing|ultimately|at the end of the day|in the end|so where does)\b` in scope `close`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.1 | 75.8 |
| Gen (4x) | 2/10 | 0.05 | 87.7 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 4/12 | 0.13 | 86.4 |
| **weighted** | 26% of weight | 0.06 | 76.2 |

**How each creator does it (verbatim):**

> "But here's the thing." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 29:36 (75.3%)

> "Ultimately, he blinked." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 30:30 (76.2%)

> "The hype that it will ultimately do everything and anything, like replace human labor." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 16:54 (83.0%)

> "But what will at the end of the day is your choice." — *Gen (4x)*, `gen/8` "How Private Equity Killed Fast Food" @ 21:21 (92.4%)

> "The biggest changes we are hoping to get from this is more, a better democracy in the end." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 13:08 (77.6%)

**Do.** Signal landing once.

**Don't.** Do not say "in conclusion".

**Checklist test.** In scope `close`, count sentences matching the detector. Weighted norm ≈ 0.06/1k words; PASS if 0-1 per 1k words; it is optional (26% weighted coverage) — only use with a reason.

### S085. Recap at end

**Definition.** Explicit recap in the last 15%.

**Detector.** function `recap_end` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0 | 0 | 1 |
| Gen (4x) | 0.0 | 0 | 1 |
| Especially (3x) | 0 | 0 | 0 |
| Oil (5x) | 1 | 1 | 1 |
| Others (1x) | 0.0 | 0 | 1 |
| **weighted** | median 0 (IQR 0–1) | | |

**How each creator does it (verbatim anchor lines):**

> "But here's the thing." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 29:36 (75.3%) — value here: **0**

> "I think that's basically the plan for AI companies today." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 37:32 (87.6%) — value here: **0**

> "The hype that it will ultimately do everything and anything, like replace human labor." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 16:54 (83.0%) — value here: **0**

> "So, the newest homeowners are like the first ones falling behind, which brings up a pretty important question of what this all means for you and in the future." — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 17:28 (76.9%) — value here: **1**

> "So what does all this mean?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 33:46 (95.2%) — value here: **1**

> "Now, I'm pretty sure they would still take the same amount, but instead of reinvesting it into the economy, which is what SNAP ultimately does, they would just buy some more missiles or send a pile of cash to Argentina." — *Others (1x)*, `after/02-greed` "Greed is Destroying the World" @ 25:53 (77.5%) — value here: **0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0, `adam/02-bestselling-book`=0, `adam/03-no-longer-in-control`=1, `adam/04-superintelligence`=1, `adam/05-sam-altman`=0, `gen/1`=0, `gen/2`=0, `gen/3`=1, `gen/4`=1, `gen/5`=1, `gen/6`=0, `gen/7`=0, `gen/8`=0, `gen/9`=0, `gen/10`=0, `esp/01-spacex`=0, `esp/02-ai-paradox`=0, `esp/06-data-centers`=0, `esp/03-oil-apocalypse`=1, `after/01-dark-side-data-centers`=0, `after/02-greed`=0, `after/03-recycling`=0, `after/04-pov-ai`=0, `after/05-middle-class`=0, `after/06-diamonds`=0, `after/07-trump-family`=0, `after/08-tokens`=0, `after/09-microchip-war`=1, `after/10-water`=0, `after/11-anthropic-ipo`=0, `after/12-data-centres-not-working`=1

</details>

**Do.** Prefer synthesis to recap.

**Don't.** Do not list every point again.

**Checklist test.** Compute `recap_end` on your outline/draft. PASS if inside the weighted IQR 0–1, or inside the chosen mode's min–max range (see table).

### S086. Callback to opening

**Definition.** % of distinctive opening words reused in last 8%.

**Detector.** function `callback_end` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 10 | 5 | 23 |
| Gen (4x) | 17.0 | 11 | 29 |
| Especially (3x) | 16 | 4 | 20 |
| Oil (5x) | 17 | 17 | 17 |
| Others (1x) | 14.0 | 0 | 36 |
| **weighted** | median 17 (IQR 10–23) | | |

**How each creator does it (verbatim anchor lines):**

> "Thank you so much for watching and see you in the next one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 39:16 (99.9%) — value here: **9**

> "We'll see you in the next one." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:47 (99.9%) — value here: **23**

> "But if you'd rather see another video on getting the truth of what's really happening with AI, you will want to watch this one next." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 20:13 (99.3%) — value here: **27**

> "Yeah." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 21:41 (99.8%) — value here: **29**

> "See you." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 24:47 (99.7%) — value here: **16**

> "(somber piano music) (somber piano music ending)" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 35:01 (98.7%) — value here: **17**

> "Heat." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 30:21 (99.4%) — value here: **8**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=9, `adam/02-bestselling-book`=23, `adam/03-no-longer-in-control`=5, `adam/04-superintelligence`=10, `adam/05-sam-altman`=23, `gen/1`=27, `gen/2`=29, `gen/3`=17, `gen/4`=12, `gen/5`=17, `gen/6`=22, `gen/7`=17, `gen/8`=14, `gen/9`=24, `gen/10`=11, `esp/01-spacex`=16, `esp/02-ai-paradox`=4, `esp/06-data-centers`=20, `esp/03-oil-apocalypse`=17, `after/01-dark-side-data-centers`=8, `after/02-greed`=12, `after/03-recycling`=22, `after/04-pov-ai`=21, `after/05-middle-class`=16, `after/06-diamonds`=36, `after/07-trump-family`=0, `after/08-tokens`=17, `after/09-microchip-war`=8, `after/10-water`=17, `after/11-anthropic-ipo`=10, `after/12-data-centres-not-working`=6

</details>

**Do.** Echo the cold-open image.

**Don't.** Do not introduce brand-new facts in the last 30 s.

**Checklist test.** Compute `callback_end` on your outline/draft. PASS if inside the weighted IQR 10–23, or inside the chosen mode's min–max range (see table).

### S087. Action ask / what to do

**Definition.** "Here's what you can do / call your rep / sign up".

**Detector.** regex `\b(what you can do|you can (help|do|join|sign|call|check)|get involved|take action|make it happen|reach out)\b` in scope `close`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 96.8 |
| Gen (4x) | 2/10 | 0.07 | 91.7 |
| Especially (3x) | 1/3 | 0.13 | 98.1 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.07 | 91.1 |
| **weighted** | 27% of weight | 0.09 | 97.9 |

**How each creator does it (verbatim):**

> "If you work in policy, you can sign up for one-on-one advising with us." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 39:23 (98.4%)

> "So let's make it happen." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 31:17 (95.3%)

> "lies have you had other men reach out um that's happened to me since I came" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 28:10 (85.5%)

> "So, if you are one of those people that wants to get smarter about money and power every week in 5 minutes, you can join the 4,200 of you who already signed up for my free newsletter in the video description." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 16:10 (97.9%)

> "As you know, the algorithm's in charge and I'd love to be able to reach out to viewers directly." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 15:58 (98.1%)

> "Are you willing to get involved militarily to defend Taiwan if it comes to that?" — *Others (1x)*, `after/09-microchip-war` "USA vs China: The Microchip War" @ 26:08 (82.7%)

**Do.** Adam: concrete civic ask; Gen: newsletter.

**Don't.** Do not end with despair only.

**Checklist test.** In scope `close`, count sentences matching the detector. Weighted norm ≈ 0.09/1k words; PASS if 0-1 per 1k words; it is optional (27% weighted coverage) — only use with a reason.

### S088. Hope/agency turn

**Definition.** Closing line of hope or agency.

**Detector.** regex `\b(hope|optimis|we can|it'?s not too late|there'?s still|we still have|good news)\b` in scope `close`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.48 | 84.7 |
| Gen (4x) | 5/10 | 0.24 | 79.9 |
| Especially (3x) | 2/3 | 0.2 | 83.4 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 5/12 | 0.22 | 82.2 |
| **weighted** | 58% of weight | 0.31 | 83.3 |

**How each creator does it (verbatim):**

> "Okay, so this book, this story — it is shorter on good news than you might want." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 34:08 (79.7%)

> "And yes, we can't say exactly how we will get there." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 29:19 (86.0%)

> "We can say whatever we want because we're live and we don't need to run anything through anyone." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 20:54 (96.2%)

> "And the good news, if you want to call it that, is that this is also happening across industries." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 15:53 (77.4%)

> "And hope that whatever gets built on top of all that compute gets built here too." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 30:32 (88.5%)

> "If we continue to delay and raise awareness and tell our stories, I believe firmly that we can stop these projects." — *Others (1x)*, `after/10-water` "We Calculated How Much Water Data Centers Actually Use. The " @ 12:25 (93.5%)

**Do.** Turn toward agency after the alarm.

**Don't.** Do not fake optimism.

**Checklist test.** In scope `close`, count sentences matching the detector. Weighted norm ≈ 0.31/1k words; PASS if ≥1 hit (corpus uses it in 58% of weighted videos) and rate ≤ 1/1k.

### S089. Thank-you sign-off

**Definition.** "Thank you so much for watching / see you in the next one".

**Detector.** regex `\b(thank(s| you)( so much)? for watching|see you in the next|see you next)\b` in scope `end`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.19 | 99.7 |
| Gen (4x) | 0/10 | 0.0 | — |
| Especially (3x) | 3/3 | 0.27 | 99.5 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 5/12 | 0.15 | 96.6 |
| **weighted** | 42% of weight | 0.12 | 99.6 |

**How each creator does it (verbatim):**

> "The last thing to say is just thank you so much for watching, for being the reason that we make these videos." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:42 (99.7%)

> "Thank you so much for watching and see you in the next one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 39:16 (99.9%)

> "Thank you so much for watching this video." — *Especially (3x)*, `esp/02-ai-paradox` "The AI Paradox" @ 15:46 (96.8%)

> "Thanks so much for watching all the way through to the end." — *Others (1x)*, `after/12-data-centres-not-working` "Why Building AI Data Centres Isn’t Working Anymore" @ 26:28 (97.1%)

**Do.** One line, warm.

**Don't.** Do not add three sign-offs.

**Checklist test.** In scope `end`, count sentences matching the detector. Weighted norm ≈ 0.12/1k words; PASS if 0-1 per 1k words; it is optional (42% weighted coverage) — only use with a reason.

### S090. Newsletter/next-video CTA

**Definition.** Closing pitch for newsletter/next video.

**Detector.** regex `\b(newsletter|next video|another video|this video (here|right here)|check out)\b` in scope `end`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.06 | 98.5 |
| Gen (4x) | 9/10 | 0.24 | 98.5 |
| Especially (3x) | 1/3 | 0.07 | 99.7 |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 2/12 | 0.04 | 97.6 |
| **weighted** | 48% of weight | 0.13 | 98.5 |

**How each creator does it (verbatim):**

> "While you're there, we would love for you to sign up for our newsletter to stay up to date on this topic." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:11 (98.5%)

> "And so, I'll definitely be diving even deeper into this in my free weekly newsletter in the video description." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 20:07 (98.9%)

> "And so, I'll be going even deeper into this issue next week on my free newsletter in the video description." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 21:24 (98.5%)

> "It is down there somewhere and I will see you in the next video." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 34:22 (99.7%)

> "If you're interested in these sports and politics stories, I encourage you to check out newpress." — *Others (1x)*, `after/07-trump-family` "The Trump family’s corruption is backfiring" @ 16:10 (95.5%)

**Do.** Gen: newsletter + next-video card.

**Don't.** Do not pitch merch and newsletter and Patreon all at once.

**Checklist test.** In scope `end`, count sentences matching the detector. Weighted norm ≈ 0.13/1k words; PASS if 0-1 per 1k words; it is optional (48% weighted coverage) — only use with a reason.

### S091. CTA count

**Definition.** Number of CTA lines.

**Detector.** function `cta_count` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 2 | 0 | 4 |
| Gen (4x) | 1.0 | 0 | 1 |
| Especially (3x) | 2 | 1 | 3 |
| Oil (5x) | 0 | 0 | 0 |
| Others (1x) | 0.0 | 0 | 2 |
| **weighted** | median 1 (IQR 1–2) | | |

**How each creator does it (verbatim anchor lines):**

> "Thank you so much for watching and see you in the next one." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 39:16 (99.9%) — value here: **1**

> "While you're there, we would love for you to sign up for our newsletter to stay up to date on this topic." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 42:11 (98.5%) — value here: **4**

> "And so, I'll definitely be diving even deeper into this in my free weekly newsletter in the video description." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 20:07 (98.9%) — value here: **1**

> "And so, I'll be going even deeper into this issue next week on my free newsletter in the video description." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 21:24 (98.5%) — value here: **1**

> "And that is exactly what hitting the subscribe button signals." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 24:29 (98.5%) — value here: **2**

> "I'm Drew, and thank you so much for watching." — *Others (1x)*, `after/04-pov-ai` "" @ 17:31 (99.2%) — value here: **1**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=1, `adam/02-bestselling-book`=4, `adam/03-no-longer-in-control`=2, `adam/04-superintelligence`=2, `adam/05-sam-altman`=0, `gen/1`=1, `gen/2`=1, `gen/3`=1, `gen/4`=1, `gen/5`=1, `gen/6`=1, `gen/7`=1, `gen/8`=1, `gen/9`=1, `gen/10`=0, `esp/01-spacex`=2, `esp/02-ai-paradox`=1, `esp/06-data-centers`=3, `esp/03-oil-apocalypse`=0, `after/01-dark-side-data-centers`=0, `after/02-greed`=0, `after/03-recycling`=0, `after/04-pov-ai`=1, `after/05-middle-class`=0, `after/06-diamonds`=1, `after/07-trump-family`=0, `after/08-tokens`=0, `after/09-microchip-war`=2, `after/10-water`=2, `after/11-anthropic-ipo`=2, `after/12-data-centres-not-working`=0

</details>

**Do.** 1-4 CTA lines total.

**Don't.** Do not exceed 5.

**Checklist test.** Compute `cta_count` on your outline/draft. PASS if inside the weighted IQR 1–2, or inside the chosen mode's min–max range (see table).


---

## N. Topic, angle & title alignment

### S092. Title length

**Definition.** Words in title.

**Detector.** function `title_words` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 9 | 5 | 10 |
| Gen (4x) | 8.0 | 6 | 10 |
| Especially (3x) | 6 | 3 | 8 |
| Oil (5x) | 5 | 5 | 5 |
| Others (1x) | 7 | 5 | 17 |
| **weighted** | median 8 (IQR 6–9) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **10**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **9**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **7**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **9**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **6**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **5**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **17**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=10, `adam/02-bestselling-book`=9, `adam/03-no-longer-in-control`=10, `adam/04-superintelligence`=5, `adam/05-sam-altman`=9, `gen/1`=7, `gen/2`=9, `gen/3`=8, `gen/4`=6, `gen/5`=8, `gen/6`=10, `gen/7`=9, `gen/8`=6, `gen/9`=7, `gen/10`=8, `esp/01-spacex`=6, `esp/02-ai-paradox`=3, `esp/06-data-centers`=8, `esp/03-oil-apocalypse`=5, `after/01-dark-side-data-centers`=17, `after/02-greed`=5, `after/03-recycling`=6, `after/05-middle-class`=7, `after/06-diamonds`=7, `after/07-trump-family`=6, `after/08-tokens`=7, `after/09-microchip-war`=6, `after/10-water`=14, `after/11-anthropic-ipo`=6, `after/12-data-centres-not-working`=8

</details>

**Do.** 5-10 words.

**Don't.** Do not exceed 12.

**Checklist test.** Compute `title_words` on your outline/draft. PASS if inside the weighted IQR 6–9, or inside the chosen mode's min–max range (see table).

### S093. How/Why/What title

**Definition.** Title opens with How/Why/What/WTF/If.

**Detector.** function `title_how_why` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0 | 0 | 1 |
| Gen (4x) | 1.0 | 0 | 1 |
| Especially (3x) | 1 | 0 | 1 |
| Oil (5x) | 0 | 0 | 0 |
| Others (1x) | 0 | 0 | 1 |
| **weighted** | median 1 (IQR 0–1) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **1**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **0**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **1**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **1**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **1**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **0**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=1, `adam/02-bestselling-book`=0, `adam/03-no-longer-in-control`=0, `adam/04-superintelligence`=0, `adam/05-sam-altman`=0, `gen/1`=1, `gen/2`=1, `gen/3`=1, `gen/4`=0, `gen/5`=1, `gen/6`=1, `gen/7`=1, `gen/8`=1, `gen/9`=1, `gen/10`=1, `esp/01-spacex`=1, `esp/02-ai-paradox`=0, `esp/06-data-centers`=1, `esp/03-oil-apocalypse`=0, `after/01-dark-side-data-centers`=0, `after/02-greed`=0, `after/03-recycling`=0, `after/05-middle-class`=0, `after/06-diamonds`=0, `after/07-trump-family`=0, `after/08-tokens`=0, `after/09-microchip-war`=0, `after/10-water`=0, `after/11-anthropic-ipo`=1, `after/12-data-centres-not-working`=1

</details>

**Do.** Gen formula: "How X Will Break Y".

**Don't.** Do not use a bland label title.

**Checklist test.** Compute `title_how_why` on your outline/draft. PASS if inside the weighted IQR 0–1, or inside the chosen mode's min–max range (see table).

### S094. Title question mark

**Definition.** Title is a literal question.

**Detector.** function `title_question` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0 | 0 | 0 |
| Gen (4x) | 0.0 | 0 | 1 |
| Especially (3x) | 0 | 0 | 0 |
| Oil (5x) | 0 | 0 | 0 |
| Others (1x) | 0 | 0 | 0 |
| **weighted** | median 0 (IQR 0–0) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **0**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **0**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **0**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **0**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **0**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **0**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0, `adam/02-bestselling-book`=0, `adam/03-no-longer-in-control`=0, `adam/04-superintelligence`=0, `adam/05-sam-altman`=0, `gen/1`=0, `gen/2`=0, `gen/3`=1, `gen/4`=0, `gen/5`=0, `gen/6`=0, `gen/7`=0, `gen/8`=0, `gen/9`=1, `gen/10`=0, `esp/01-spacex`=0, `esp/02-ai-paradox`=0, `esp/06-data-centers`=0, `esp/03-oil-apocalypse`=0, `after/01-dark-side-data-centers`=0, `after/02-greed`=0, `after/03-recycling`=0, `after/05-middle-class`=0, `after/06-diamonds`=0, `after/07-trump-family`=0, `after/08-tokens`=0, `after/09-microchip-war`=0, `after/10-water`=0, `after/11-anthropic-ipo`=0, `after/12-data-centres-not-working`=0

</details>

**Do.** Rare; use for "WTF/If…why" formats.

**Don't.** Do not default to questions.

**Checklist test.** Compute `title_question` on your outline/draft. PASS if inside the weighted IQR 0–0, or inside the chosen mode's min–max range (see table).

### S095. Number in title

**Definition.** Title contains a number.

**Detector.** function `title_number` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 0 | 0 | 0 |
| Gen (4x) | 0.0 | 0 | 1 |
| Especially (3x) | 0 | 0 | 0 |
| Oil (5x) | 0 | 0 | 0 |
| Others (1x) | 0 | 0 | 1 |
| **weighted** | median 0 (IQR 0–0) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **0**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **0**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **0**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **0**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **0**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **0**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **0**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=0, `adam/02-bestselling-book`=0, `adam/03-no-longer-in-control`=0, `adam/04-superintelligence`=0, `adam/05-sam-altman`=0, `gen/1`=0, `gen/2`=0, `gen/3`=0, `gen/4`=0, `gen/5`=0, `gen/6`=0, `gen/7`=1, `gen/8`=0, `gen/9`=0, `gen/10`=1, `esp/01-spacex`=0, `esp/02-ai-paradox`=0, `esp/06-data-centers`=0, `esp/03-oil-apocalypse`=0, `after/01-dark-side-data-centers`=0, `after/02-greed`=0, `after/03-recycling`=0, `after/05-middle-class`=0, `after/06-diamonds`=1, `after/07-trump-family`=0, `after/08-tokens`=0, `after/09-microchip-war`=0, `after/10-water`=0, `after/11-anthropic-ipo`=0, `after/12-data-centres-not-working`=0

</details>

**Do.** Use when the figure is the hook ($110M).

**Don't.** Do not invent precision.

**Checklist test.** Compute `title_number` on your outline/draft. PASS if inside the weighted IQR 0–0, or inside the chosen mode's min–max range (see table).

### S096. Title-hook word overlap

**Definition.** % of title content words appearing in first 8%.

**Detector.** function `title_in_hook` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 33 | 0 | 57 |
| Gen (4x) | 63.5 | 0 | 100 |
| Especially (3x) | 25 | 0 | 50 |
| Oil (5x) | 50 | 50 | 50 |
| Others (1x) | 60 | 0 | 100 |
| **weighted** | median 50 (IQR 33–60) | | |

**How each creator does it (verbatim anchor lines):**

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%) — value here: **33**

> "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 0:00 (0.0%) — value here: **57**

> "So, software as we know it might be cooked." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:00 (0.0%) — value here: **67**

> "Take a look at the YouTube channels that you're subscribed to." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:00 (0.0%) — value here: **71**

> "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 0:00 (0.0%) — value here: **25**

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%) — value here: **50**

> "Giant warehouses are popping up across the US, more than two every week." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:01 (0.1%) — value here: **36**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=33, `adam/02-bestselling-book`=57, `adam/03-no-longer-in-control`=0, `adam/04-superintelligence`=33, `adam/05-sam-altman`=50, `gen/1`=67, `gen/2`=71, `gen/3`=25, `gen/4`=0, `gen/5`=50, `gen/6`=40, `gen/7`=60, `gen/8`=80, `gen/9`=100, `gen/10`=80, `esp/01-spacex`=25, `esp/02-ai-paradox`=0, `esp/06-data-centers`=50, `esp/03-oil-apocalypse`=50, `after/01-dark-side-data-centers`=36, `after/02-greed`=0, `after/03-recycling`=75, `after/05-middle-class`=60, `after/06-diamonds`=75, `after/07-trump-family`=50, `after/08-tokens`=100, `after/09-microchip-war`=100, `after/10-water`=62, `after/11-anthropic-ipo`=50, `after/12-data-centres-not-working`=40

</details>

**Do.** Pay off the title words in the cold open.

**Don't.** Do not bait-and-switch.

**Checklist test.** Compute `title_in_hook` on your outline/draft. PASS if inside the weighted IQR 33–60, or inside the chosen mode's min–max range (see table).

### S097. Villain/institution angle

**Definition.** Topic framed around an actor (private equity, big tech, Musk, OpenAI).

**Detector.** regex `\b(private equity|big tech|wall street|openai|musk|altman|billionaire|corporations?|the government|china)\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 5/5 | 0.97 | 2.3 |
| Gen (4x) | 6/10 | 0.81 | 0.7 |
| Especially (3x) | 1/3 | 0.13 | 6.7 |
| Oil (5x) | 1/1 | 0.33 | 8.4 |
| Others (1x) | 5/12 | 0.17 | 1.9 |
| **weighted** | 71% of weight | 0.74 | 1.4 |

**How each creator does it (verbatim):**

> "There's an AI race, of course, and one of the biggest corporations in it is Galvanic Labs." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 1:33 (3.6%)

> "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 0:00 (0.0%)

> "One that Big Tech has already planned for, so when a data center dies, they walk away just fine." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 0:40 (4.0%)

> "There's a good chance at least one of them was quietly sold to private equity." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 0:01 (0.1%)

> "The long wires between cities were owned and paid for by the government, meant for universities and labs." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 2:19 (6.7%)

> "China magically cuts back its imports by five and a half million barrels a day." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 2:59 (8.4%)

> "Big tech companies often go to great lengths to hide the details." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 0:34 (1.9%)

**Do.** Pick an angle with an accountable actor.

**Don't.** Do not make the villain cartoonish.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.74/1k words; PASS if ≥1 hit (corpus uses it in 71% of weighted videos) and rate ≤ 1.5/1k.

### S098. Viewer-life angle

**Definition.** Topic tied to viewer's spending/job/home.

**Detector.** regex `\b(your (job|money|bills?|rent|house|subscriptions?|electricity|kids|favorite))\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 1.3 |
| Gen (4x) | 5/10 | 0.14 | 4.9 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 0/12 | 0.0 | — |
| **weighted** | 27% of weight | 0.08 | 2.5 |

**How each creator does it (verbatim):**

> "AI is a technology for taking away your job and maybe eventually displacing human sovereignty over our own future." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:32 (1.3%)

> "These companies keep raising your subscriptions, make canceling a mess, and turn your favorite $60 games into $80 ones." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:30 (2.5%)

> "So, to understand how a dead data center makes your rent worse, you have to start with one thing that everyone gets wrong about housing." — *Gen (4x)*, `gen/5` "Why Canceling Data Centers is Going Horribly Wrong" @ 1:26 (8.7%)

**Do.** Gen: always route through your wallet.

**Don't.** Do not stay abstract.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.08/1k words; PASS if 0-1 per 1k words; it is optional (27% weighted coverage) — only use with a reason.

### S099. Timeliness peg

**Definition.** "Just / this week / right now / recently".

**Detector.** regex `\b(just (announced|released|happened|used)|this (week|year|month)|right now|recently|last (week|month))\b` in scope `open`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 4/5 | 0.19 | 1.2 |
| Gen (4x) | 8/10 | 0.43 | 5.7 |
| Especially (3x) | 2/3 | 0.27 | 0.6 |
| Oil (5x) | 1/1 | 0.17 | 4.0 |
| Others (1x) | 7/12 | 0.28 | 2.9 |
| **weighted** | 77% of weight | 0.29 | 1.6 |

**How each creator does it (verbatim):**

> "Some of it we only know now, thanks to unsealed court testimony that's come out just this year." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 0:20 (0.8%)

> "Right now it might feel like everyone, including your grandma, is selling an AI powered something." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 1:22 (4.0%)

> "One guy just used AI to make free copies of Photoshop and Word in 2 weeks." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 0:08 (0.7%)

> "been recently built in New Haven and I almost jumped What stopped you um a a" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 4:48 (14.6%)

> "A number that, until very recently, could only be claimed by the land in prestigious areas of the most prestigious cities: New York, Paris, Tokyo, London." — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 0:24 (1.2%)

> "It is here, right now, upending your world in ways that might not be initially apparent, but once you know how to see it, you will realize are absolutely everywhere." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 1:26 (4.0%)

> "Most people think about diamonds for jewelry, but everybody's missing what's most exciting happening right now." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 0:05 (0.5%)

**Do.** Peg evergreen analysis to a fresh event.

**Don't.** Do not date-stamp evergreen essays needlessly.

**Checklist test.** In scope `open`, count sentences matching the detector. Weighted norm ≈ 0.29/1k words; PASS if ≥1 hit (corpus uses it in 77% of weighted videos) and rate ≤ 1/1k.


---

## O. Structural voice signals

### S100. "You" density in open

**Definition.** Second-person per 1k words in first 10%.

**Detector.** function `you_open` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 12.8 | 9.2 | 20.6 |
| Gen (4x) | 27.6 | 8.9 | 50.3 |
| Especially (3x) | 9.0 | 4.3 | 24.6 |
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

`adam/01-ai-disaster`=9.2, `adam/02-bestselling-book`=10.0, `adam/03-no-longer-in-control`=20.6, `adam/04-superintelligence`=12.8, `adam/05-sam-altman`=14.7, `gen/1`=24.2, `gen/2`=26.8, `gen/3`=8.9, `gen/4`=39.6, `gen/5`=50.3, `gen/6`=28.5, `gen/7`=15.3, `gen/8`=26.1, `gen/9`=28.4, `gen/10`=35.2, `esp/01-spacex`=9.0, `esp/02-ai-paradox`=24.6, `esp/06-data-centers`=4.3, `esp/03-oil-apocalypse`=28.4, `after/01-dark-side-data-centers`=2.3, `after/02-greed`=58.2, `after/03-recycling`=26.1, `after/04-pov-ai`=96.4, `after/05-middle-class`=10.6, `after/06-diamonds`=21.7, `after/07-trump-family`=3.4, `after/08-tokens`=8.8, `after/09-microchip-war`=25.0, `after/10-water`=4.3, `after/11-anthropic-ipo`=0.0, `after/12-data-centres-not-working`=6.6

</details>

**Do.** Gen median ~28/1k in the open; Adam ~13; oil ~28; especially ~9.

**Don't.** Do not write "you" in every clause.

**Checklist test.** Compute `you_open` on your outline/draft. PASS if inside the weighted IQR 10.0–28.4, or inside the chosen mode's min–max range (see table).

### S101. "You" density overall

**Definition.** Second-person per 1k words.

**Detector.** function `you_all` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 12.3 | 8.0 | 14.6 |
| Gen (4x) | 20.9 | 13.5 | 32.7 |
| Especially (3x) | 18.0 | 14.1 | 27.8 |
| Oil (5x) | 15.4 | 15.4 | 15.4 |
| Others (1x) | 11.7 | 6.7 | 75.9 |
| **weighted** | median 14.6 (IQR 12.3–20.9) | | |

**How each creator does it (verbatim anchor lines):**

> "If you want, you're welcome to imagine that Sable is just like an extremely sophisticated computer virus if that helps all this feel more realistic." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 26:33 (62.0%) — value here: **14.6**

> "If your grading software rewards that as a success, then you've accidentally reinforced the AI's cheating behavior." — *Adam (7x)*, `adam/03-no-longer-in-control` "We are no longer in control of the AI situation." @ 9:12 (28.0%) — value here: **8.0**

> "But again, why this is relevant to this video is that with Zapier, your data and your logic stays yours, so you control the AI instead of it controlling you." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:01 (44.3%) — value here: **20.6**

> "Platforms that seem free are really just collecting everything about you and selling it to whoever will pay like your inbox, your habits, and your behavior over time." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 9:53 (45.5%) — value here: **13.5**

> "3% base JPY from programed banks until you decide to move it so your money is always working for you for a limited time, Wealthfront is offering my audience an exclusive 0." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 12:10 (49.0%) — value here: **18.0**

> "And you can file all of those disruptions, all of which make shipping scarcer under generalized danger in the Hormuz Strait." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 14:54 (42.0%) — value here: **15.4**

> "It's not something that you just hear." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 15:00 (49.1%) — value here: **6.7**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=12.6, `adam/02-bestselling-book`=14.6, `adam/03-no-longer-in-control`=8.0, `adam/04-superintelligence`=12.3, `adam/05-sam-altman`=11.5, `gen/1`=20.6, `gen/2`=13.5, `gen/3`=17.6, `gen/4`=22.9, `gen/5`=22.3, `gen/6`=20.9, `gen/7`=20.8, `gen/8`=22.5, `gen/9`=32.7, `gen/10`=13.6, `esp/01-spacex`=18.0, `esp/02-ai-paradox`=27.8, `esp/06-data-centers`=14.1, `esp/03-oil-apocalypse`=15.4, `after/01-dark-side-data-centers`=6.7, `after/02-greed`=22.2, `after/03-recycling`=28.8, `after/04-pov-ai`=75.9, `after/05-middle-class`=7.2, `after/06-diamonds`=17.6, `after/07-trump-family`=12.6, `after/08-tokens`=10.5, `after/09-microchip-war`=10.8, `after/10-water`=10.2, `after/11-anthropic-ipo`=9.8, `after/12-data-centres-not-working`=13.1

</details>

**Do.** Match group norm.

**Don't.** Do not drop to 0.

**Checklist test.** Compute `you_all` on your outline/draft. PASS if inside the weighted IQR 12.3–20.9, or inside the chosen mode's min–max range (see table).

### S102. First-person density

**Definition.** I/me/my per 1k words.

**Detector.** function `i_all` (see `build/crit_*.py`).

| group | median | min | max |
|---|---|---|---|
| Adam (7x) | 7.3 | 4.9 | 12.2 |
| Gen (4x) | 18.2 | 12.1 | 47.1 |
| Especially (3x) | 5.4 | 4.9 | 12.0 |
| Oil (5x) | 9.1 | 9.1 | 9.1 |
| Others (1x) | 8.6 | 4.4 | 22.6 |
| **weighted** | median 12.0 (IQR 7.3–14.1) | | |

**How each creator does it (verbatim anchor lines):**

> "If I had to answer in five words, they’d be “a maniacal sense of urgency”." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 23:21 (59.4%) — value here: **12.2**

> "I will observe one thing, which is that if you made a human a God Emperor, I think the situation would be just as bad." — *Adam (7x)*, `adam/02-bestselling-book` "This best-selling book is freaking out national security adv" @ 29:16 (68.3%) — value here: **6.7**

> "But, if you've been paying attention like how I mentioned that it was buggy, it's really not that simple." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 8:04 (39.6%) — value here: **12.1**

> "Because remember, I bought each channel for 3 to five times its earnings." — *Gen (4x)*, `gen/2` "How Private Equity Turns Your Favorite Channels Into Slop" @ 5:46 (26.5%) — value here: **22.2**

> "As I've talked about in other videos, the." — *Especially (3x)*, `esp/01-spacex` "How SpaceX Is Making America Uncatchable" @ 22:13 (89.4%) — value here: **5.4**

> "Let's actually flip this back really quickly, so I can explain why that's such a problem." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 15:09 (42.7%) — value here: **9.1**

> "I'm getting bombarded each and every night." — *Others (1x)*, `after/01-dark-side-data-centers` "Exposing The Dark Side of America's AI Data Center Explosion" @ 15:21 (50.3%) — value here: **11.1**

<details><summary>Per-video values</summary>

`adam/01-ai-disaster`=12.2, `adam/02-bestselling-book`=6.7, `adam/03-no-longer-in-control`=4.9, `adam/04-superintelligence`=8.3, `adam/05-sam-altman`=7.3, `gen/1`=12.1, `gen/2`=22.2, `gen/3`=22.7, `gen/4`=20.8, `gen/5`=13.3, `gen/6`=13.7, `gen/7`=47.1, `gen/8`=19.4, `gen/9`=12.7, `gen/10`=17.1, `esp/01-spacex`=5.4, `esp/02-ai-paradox`=12.0, `esp/06-data-centers`=4.9, `esp/03-oil-apocalypse`=9.1, `after/01-dark-side-data-centers`=11.1, `after/02-greed`=10.2, `after/03-recycling`=22.6, `after/04-pov-ai`=8.4, `after/05-middle-class`=6.4, `after/06-diamonds`=14.1, `after/07-trump-family`=8.8, `after/08-tokens`=4.4, `after/09-microchip-war`=7.7, `after/10-water`=8.7, `after/11-anthropic-ipo`=5.8, `after/12-data-centres-not-working`=6.5

</details>

**Do.** Adam uses "I" as investigator.

**Don't.** Do not make it a vlog.

**Checklist test.** Compute `i_all` on your outline/draft. PASS if inside the weighted IQR 7.3–14.1, or inside the chosen mode's min–max range (see table).

### S103. Self-research disclosure

**Definition.** "As I researched / what I found".

**Detector.** regex `\b(as I (researched|dug|looked)|what I found|I (found|discovered|noticed|realized))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 71.5 |
| Gen (4x) | 8/10 | 0.76 | 6.2 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 0/1 | 0.0 | — |
| Others (1x) | 4/12 | 0.13 | 26.1 |
| **weighted** | 50% of weight | 0.33 | 6.7 |

**How each creator does it (verbatim):**

> "As I researched this video, that is by far the most tragic, kind of most paradoxical thing that's come up." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 27:07 (69.0%)

> "When I realized that their decision was like potentially catastrophic for the company, I felt like I had to act very quickly." — *Adam (7x)*, `adam/05-sam-altman` "You really should, unfortunately, be worried about Sam Altma" @ 29:39 (74.1%)

> "But if you haven't been paying attention, what I found is that the money always just changes hands." — *Gen (4x)*, `gen/1` "How AI Piracy Will Break The Economy" @ 9:33 (46.9%)

> "So, I spend weeks following the money, and what I found is something I didn't expect." — *Gen (4x)*, `gen/4` "The (Overdue) Collapse Of Artificial Intelligence" @ 1:18 (6.3%)

> "And I found all of these really cool released CIA documents about it." — *Others (1x)*, `after/06-diamonds` "The $1 Trillion Problem Diamonds Can Solve" @ 9:33 (57.5%)

**Do.** Use once per act to frame discoveries.

**Don't.** Do not narrate your process at length.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.33/1k words; PASS if ≥1 hit (corpus uses it in 50% of weighted videos) and rate ≤ 1/1k.

### S104. Clip framing line

**Definition.** Host line introducing archival/guest audio.

**Detector.** regex `\b(here'?s (what|how) (he|she|they)|this is (him|her|musk|altman)|in (his|her) words|listen to)\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 2/5 | 0.06 | 79.2 |
| Gen (4x) | 1/10 | 0.02 | 32.5 |
| Especially (3x) | 0/3 | 0.0 | — |
| Oil (5x) | 1/1 | 0.17 | 76.7 |
| Others (1x) | 2/12 | 0.04 | 36.1 |
| **weighted** | 25% of weight | 0.05 | 70.0 |

**How each creator does it (verbatim):**

> "Like this is Musk in 2014." — *Adam (7x)*, `adam/01-ai-disaster` "If you remember one AI disaster, make it this one" @ 27:31 (70.0%)

> "We are heading very quickly towards a future where the companies that make these systems and the systems themselves just need not listen to the vast majority of people on Earth." — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 30:06 (88.3%)

> "I don't know if it's just me, but I lowkey like working in loud ass coffee shops, and I also use them while working out to listen to podcast episodes of guests that I'm about to interview." — *Gen (4x)*, `gen/10` "How Private Equity Will Break America (Like 2008)" @ 5:32 (32.5%)

> "I have had to listen to so many serious energy analysts say "Crack spreads are widening" while trying to keep a straight face over the last month." — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 27:13 (76.7%)

> "Go listen to this song immediately after this video." — *Others (1x)*, `after/03-recycling` "i’m pretty sure recycling isn’t real…" @ 8:18 (26.9%)

**Do.** Frame every clip in one line.

**Don't.** Do not drop unexplained clips.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.05/1k words; PASS if 0-1 per 1k words; it is optional (25% weighted coverage) — only use with a reason.

### S105. Mid-script direct question to viewer

**Definition.** "Do you really think…?", "you know what?".

**Detector.** regex `\b(do you (really )?(think|know|remember)|have you (ever|noticed))\b` in scope `all`.

| group | cov | /1k | first% |
|---|---|---|---|
| Adam (7x) | 1/5 | 0.03 | 98.9 |
| Gen (4x) | 4/10 | 0.12 | 62.1 |
| Especially (3x) | 2/3 | 0.2 | 55.0 |
| Oil (5x) | 1/1 | 0.17 | 0.0 |
| Others (1x) | 5/12 | 0.13 | 59.2 |
| **weighted** | 39% of weight | 0.1 | 71.0 |

**How each creator does it (verbatim):**

> "What do you think was most implausible?" — *Adam (7x)*, `adam/04-superintelligence` "We're Not Ready for Superintelligence" @ 33:43 (98.9%)

> "offense but if this was just some random frat kid in ASU do you really think it" — *Gen (4x)*, `gen/7` "How This $110M Lawsuit Could End False Accusations Forever" @ 26:48 (81.4%)

> "Like, when you think about town hall, do you think about young people going to that?" — *Gen (4x)*, `gen/3` "If Housing is F*cked, Why Hasn’t It Crashed?" @ 11:23 (50.1%)

> "Do you know why modern prison cells don't look like this anymore and instead look like this?" — *Especially (3x)*, `esp/06-data-centers` "What They're Not Telling You About Data Centers" @ 13:28 (39.1%)

> "Do you remember that oil shock we warned you about a few months ago?" — *Oil (5x)*, `esp/03-oil-apocalypse` "The oil apocalypse is here" @ 0:00 (0.0%)

> "Not only that, have you noticed how almost all AI companies have recently changed their business model?" — *Others (1x)*, `after/08-tokens` "Uh oh, tokens are getting too expensive..." @ 11:46 (75.0%)

**Do.** 1-3 times per video.

**Don't.** Do not interrogate.

**Checklist test.** In scope `all`, count sentences matching the detector. Weighted norm ≈ 0.1/1k words; PASS if 0-1 per 1k words; it is optional (39% weighted coverage) — only use with a reason.
