# Channel structure — 100 exams

Sampled by corpus weight (video drawn with probability ∝ 7/4/5/3/1), type rotated. Each exam: prompt, gold (from the real transcript / detected beat map), rubric. Re-run with `python3 build/run_exams.py exam_structure` — deterministic seed.

## Exam types

- **T1** Beat labeling — name the structural job of a verbatim line given its position %
- **T2** Position estimation — estimate where (% of runtime) a verbatim beat line sits; ±10 = full, ±20 = half
- **T3** Real-opener MCQ — which of 4 lines from one video is its actual first line
- **T4** Outline reconstruction — from title/mode/runtime/sponsor, predict hook-end %, sponsor %, conclusion %, number of turns; compared to gold beat map (4 points)
- **T5** Mode attribution — from a structural profile (runtime, WPM, hook seconds, "you"/1k) pick Adam / Gen / Mechanism / Others
- **T6** Beat ordering — put 4 shuffled beat lines from one video in runtime order (pairwise accuracy)


### Exam 1 — T1 · `adam/05-sam-altman` (Adam)

**Prompt.** Line: "We don't want this to be a sort of profit maximizing a behemoth from hell, you know?" (at 21.4%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SPONSOR READ" → **score 0.0**

### Exam 2 — T2 · `gen/2` (Gen)

**Prompt.** Line: "So to understand this whole thing, I think the best way is by showing you how a private equity firm even buys a YouTube channel."
Estimate % of runtime.

**Gold.** 7.3%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 45 → **score 0.0**

### Exam 3 — T3 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "Why are they investing so much in this moonshot anyway?"
B. "I will observe one thing, which is that if you made a human a God Emperor, I think the situation would be just as bad."
C. "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived."
D. "They malfunctioned in all kinds of surprising ways, but they didn't actively pursue goals."

**Gold.** C

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 1.0**

### Exam 4 — T4 · `gen/3` (Gen)

**Prompt.** {"title": "If Housing is F*cked, Why Hasn\u2019t It Crashed?", "mode": "Gen", "runtime": "22:43", "has_sponsor": true} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.2, "spon": 43.5, "conc": 76.9, "turns": 5}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 6, "spon": 39, "conc": 85, "turns": 6} → **score 0.75**

### Exam 5 — T5 · `adam/02-bestselling-book` (Adam)

**Prompt.** Profile {"dur": 42.8, "wpm": 163, "hook": 64, "you": 14.6}

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 6 — T6 · `adam/02-bestselling-book` (Adam)

**Prompt.** Order these:
0. "I think that's basically the plan for AI companies today."
1. "I want to take you through that story."
2. "But then I talked to Nate."
3. "So how does a highly capable artificial mind like Sable do the things it does?"

**Gold.** [1, 3, 2, 0]

**Rubric.** pairwise order accuracy

**Taken answer.** [1, 0, 2, 3] → **score 0.5**

### Exam 7 — T1 · `gen/6` (Gen)

**Prompt.** Line: "So, if SpaceX goes up 10% in a day, you make 20%." (at 66.0%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 8 — T2 · `adam/01-ai-disaster` (Adam)

**Prompt.** Line: "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else."
Estimate % of runtime.

**Gold.** 1.2%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 5 → **score 1.0**

### Exam 9 — T3 · `adam/01-ai-disaster` (Adam)

**Prompt.** Options:
A. "Soon, the same AI model that called itself MechaHitler and recommended a second Holocaust will be used in the Pentagon to address critical national security challenges."
B. "It was Grok's Hitler sympathies that were making the viral rounds as screenshots."
C. "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown."
D. "You can, instead of writing your response in normal English, put it in some weird format and then suddenly the model can't recognize it, even though it's been trained to."

**Gold.** C

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 1.0**

### Exam 10 — T4 · `gen/6` (Gen)

**Prompt.** {"title": "Why Everyone Wants You To Believe The Market Is Crashing", "mode": "Gen", "runtime": "22:18", "has_sponsor": true} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 16.6, "spon": 41.4, "conc": null, "turns": 7}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 6, "spon": 39, "conc": 85, "turns": 6} → **score 0.75**

### Exam 11 — T5 · `gen/6` (Gen)

**Prompt.** Profile {"dur": 22.3, "wpm": 200, "hook": 222, "you": 20.9}

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Gen" → **score 1.0**

### Exam 12 — T6 · `gen/9` (Gen)

**Prompt.** Order these:
0. "And that's exactly why you get that feeling where the news says that the economy is growing and you look around and think where?"
1. "So now the question becomes, what's next?"
2. "Now, let's look at prices."
3. "So if the price keeps climbing instead, every one of those people will be forced to buy, which pushes it up even more."

**Gold.** [2, 0, 3, 1]

**Rubric.** pairwise order accuracy

**Taken answer.** [1, 2, 0, 3] → **score 0.5**

### Exam 13 — T1 · `gen/6` (Gen)

**Prompt.** Line: "This is a free newsletter in the video description that we write every week." (at 98.8%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** CTA

**Rubric.** 1 if exact, else 0

**Taken answer.** "CTA" → **score 1.0**

### Exam 14 — T2 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Line: "I'll see you in the next one."
Estimate % of runtime.

**Gold.** 99.6%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 45 → **score 0.0**

### Exam 15 — T3 · `gen/5` (Gen)

**Prompt.** Options:
A. "Ladies and gentlemen, data centers are getting canceled."
B. "Microsoft, one of the companies that kicked off this whole data center boom, walked away from at least five plots of land leases that I already had under contract."
C. "So, when they pause these data centers, they also accidentally paused every warehouse size project in the city, including housing."
D. "Hundreds of residents packed into council meetings and killed the data center project cold."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 16 — T4 · `adam/04-superintelligence` (Adam)

**Prompt.** {"title": "We're Not Ready for Superintelligence", "mode": "Adam", "runtime": "34:05", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 3.9, "spon": null, "conc": 88.7, "turns": 7}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 2.5, "spon": null, "conc": 80, "turns": 7} → **score 0.75**

### Exam 17 — T5 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Profile {"dur": 32.8, "wpm": 144, "hook": 127, "you": 8.0}

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 18 — T6 · `esp/02-ai-paradox` (Especially)

**Prompt.** Order these:
0. "First, babies practice syllables, then words, then they glue words together, eventually forming sentences that others can understand."
1. "In 2025, researchers at MIT ran an experiment."
2. "dev and use code art for 25% off your first year or use this QR code."
3. "So, what about this magic gumball machine?"

**Gold.** [0, 2, 1, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [0, 1, 2, 3] → **score 0.83**

### Exam 19 — T1 · `adam/05-sam-altman` (Adam)

**Prompt.** Line: "Now, minutes later, the board puts out a public statement." (at 8.1%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 20 — T2 · `adam/02-bestselling-book` (Adam)

**Prompt.** Line: "Books are while supplies last, but the newsletter is always there."
Estimate % of runtime.

**Gold.** 99.1%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 98 → **score 1.0**

### Exam 21 — T3 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Options:
A. "Sometimes they got approved, sometimes they got blocked because the website realized they were bots."
B. "One of these newcomers asks for the full notes of the message board's founder, PHASEONE10841."
C. "It was a strange summer."
D. "Just doing that took them three days, by the way."

**Gold.** C

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 22 — T4 · `esp/01-spacex` (Especially)

**Prompt.** {"title": "How SpaceX Is Making America Uncatchable", "mode": "Mechanism", "runtime": "24:51", "has_sponsor": true} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.1, "spon": 4.5, "conc": null, "turns": 8}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 6, "spon": 27, "conc": 90, "turns": 7} → **score 0.75**

### Exam 23 — T5 · `gen/6` (Gen)

**Prompt.** Profile {"dur": 22.3, "wpm": 200, "hook": 222, "you": 20.9}

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Gen" → **score 1.0**

### Exam 24 — T6 · `esp/06-data-centers` (Especially)

**Prompt.** Order these:
0. "Thanks to the sponsor of this video, Zocdoc."
1. "But the data center fight could be, might be, maybe even likely is—a fight over a much older and a much simpler question: When the cost lands, who is sitting […]"
2. "Oh, and hit that subscribe button."
3. "It is down there somewhere and I will see you in the next video."

**Gold.** [0, 1, 2, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [0, 1, 2, 3] → **score 1.0**

### Exam 25 — T1 · `adam/01-ai-disaster` (Adam)

**Prompt.** Line: "So, if you're Elon Musk and you're not happy with the outputs that your model is generating, you have a few different options." (at 13.9%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 26 — T2 · `after/07-trump-family` (Others)

**Prompt.** Line: "And that's why today's sponsor Obscura caught my attention."
Estimate % of runtime.

**Gold.** 37.0%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 35 → **score 1.0**

### Exam 27 — T3 · `gen/9` (Gen)

**Prompt.** Options:
A. "Every single metric says that the economy is cooked."
B. "So AI spending, which means borrowed money, is what's growing the economy right now."
C. "And you might think, is that even that unusual?"
D. "It's exactly why borrowing is cheap."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 28 — T4 · `after/01-dark-side-data-centers` (Others)

**Prompt.** {"title": "Exposing The Dark Side of America's AI Data Center Explosion | View From Above | Business Insider", "mode": "Others", "runtime": "30:32", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.1, "spon": null, "conc": null, "turns": 6}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 6, "spon": null, "conc": 86, "turns": 5} → **score 1.0**

### Exam 29 — T5 · `gen/1` (Gen)

**Prompt.** Profile {"dur": 20.4, "wpm": 191, "hook": 17, "you": 20.6}

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Gen" → **score 1.0**

### Exam 30 — T6 · `after/07-trump-family` (Others)

**Prompt.** Order these:
0. "Now, the problem was government officials were using the special Investors Law to sell land to friends or people they found useful."
1. "And that's why today's sponsor Obscura caught my attention."
2. "So why does it matter that Jared and Ivanka are building a resort on Sazan?"
3. "In 2017, a Qatar-backed company bought the Kushners out of their troubled building."

**Gold.** [2, 0, 1, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [1, 0, 2, 3] → **score 0.5**

### Exam 31 — T1 · `esp/01-spacex` (Especially)

**Prompt.** Line: "Because if you want to answer the question of what is space worth?" (at 15.6%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "PROMISE / ROADMAP" → **score 0.0**

### Exam 32 — T2 · `gen/10` (Gen)

**Prompt.** Line: "That's why I use my sponsor, Raycon, to stay locked in."
Estimate % of runtime.

**Gold.** 32.0%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 35.6 → **score 1.0**

### Exam 33 — T3 · `gen/2` (Gen)

**Prompt.** Options:
A. "Take a look at the YouTube channels that you're subscribed to."
B. "Same person negotiates every brand deal and same thumbnail testing operation, account and compliance."
C. "But with YouTube, in one of these niches, it can cost $50 per thousand."
D. "And audiences are slowly starting to notice that something is a bit off in the comments."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 34 — T4 · `after/01-dark-side-data-centers` (Others)

**Prompt.** {"title": "Exposing The Dark Side of America's AI Data Center Explosion | View From Above | Business Insider", "mode": "Others", "runtime": "30:32", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.1, "spon": null, "conc": null, "turns": 6}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 6.0, "spon": null, "conc": 86, "turns": 5} → **score 1.0**

### Exam 35 — T5 · `esp/03-oil-apocalypse` (Oil)

**Prompt.** Profile {"dur": 35.5, "wpm": 171, "hook": 95, "you": 15.4}

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 0.0**

### Exam 36 — T6 · `esp/06-data-centers` (Especially)

**Prompt.** Order these:
0. "Thanks to the sponsor of this video, Zocdoc."
1. "Finally, in 2021, the state said no more."
2. "What do you mean it'll do it for you?"
3. "But the data center fight could be, might be, maybe even likely is—a fight over a much older and a much simpler question: When the cost lands, who is sitting […]"

**Gold.** [2, 0, 1, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [0, 1, 2, 3] → **score 0.67**

### Exam 37 — T1 · `adam/02-bestselling-book` (Adam)

**Prompt.** Line: "Now, that example — pretty harmless." (at 20.4%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 38 — T2 · `adam/04-superintelligence` (Adam)

**Prompt.** Line: "So I think the window that we have to act is narrowing quickly."
Estimate % of runtime.

**Gold.** 88.7%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 45 → **score 0.0**

### Exam 39 — T3 · `adam/01-ai-disaster` (Adam)

**Prompt.** Options:
A. "AI progress doesn't wait for us to catch up."
B. "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown."
C. "And right now, Elon Musk is just not inspiring confidence."
D. "Companies all claim to care deeply about safety."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 40 — T4 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** {"title": "We are no longer in control of the AI situation.", "mode": "Adam", "runtime": "32:50", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.4, "spon": null, "conc": null, "turns": 8}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 3.1, "spon": null, "conc": 83.5, "turns": 7} → **score 0.75**

### Exam 41 — T5 · `gen/5` (Gen)

**Prompt.** Profile {"dur": 16.5, "wpm": 187, "hook": 86, "you": 22.3}

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Gen" → **score 1.0**

### Exam 42 — T6 · `gen/7` (Gen)

**Prompt.** Order these:
0. "only one so I wanted to set my bias aside to try and find out could this"
1. "consistently helps me with that is my sponsor straight arrow news so straight"
2. "now but there were countless times during the process where when I was"
3. "behind the screen it's not that I am against hate speech I think that's"

**Gold.** [0, 2, 1, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [1, 0, 2, 3] → **score 0.67**

### Exam 43 — T1 · `gen/2` (Gen)

**Prompt.** Line: "So, if that's already happening, what's stopping a private equity firm from acquiring political commentary channels and steering their editorial direction towards candidates who would pass laws that benefit the firm's other investments." (at 87.6%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "CTA" → **score 0.0**

### Exam 44 — T2 · `gen/8` (Gen)

**Prompt.** Line: "And if nothing changes, we don't just lose the last rare places where somebody still gives a everywhere is about to look, feel, and get treated like it's built to die."
Estimate % of runtime.

**Gold.** 6.1%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 45 → **score 0.0**

### Exam 45 — T3 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Options:
A. "A few days later, there's a leak in the press that, in fact, OpenAI had had rogue agents loose in their own infrastructure and failed to notice for a week."
B. "A large remaining budget of computational Like, PHASEONE10841 expresses excitement."
C. "They call this, I swear to God, permadeath."
D. "It was a strange summer."

**Gold.** D

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 46 — T4 · `adam/02-bestselling-book` (Adam)

**Prompt.** {"title": "This best-selling book is freaking out national security advisors", "mode": "Adam", "runtime": "42:50", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 2.5, "spon": null, "conc": 87.6, "turns": 8}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 4.4, "spon": null, "conc": 83.5, "turns": 7} → **score 1.0**

### Exam 47 — T5 · `gen/6` (Gen)

**Prompt.** Profile {"dur": 22.3, "wpm": 200, "hook": 222, "you": 20.9}

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Gen" → **score 1.0**

### Exam 48 — T6 · `gen/5` (Gen)

**Prompt.** Order these:
0. "So, let's start with the land itself."
1. "So, what this reveals is something dark."
2. "So, to understand how a dead data center makes your rent worse, you have to start with one thing that everyone gets wrong about housing."
3. "But, I think the one thing that actually scares them is you starting to."

**Gold.** [2, 1, 0, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [0, 2, 1, 3] → **score 0.67**

### Exam 49 — T1 · `after/08-tokens` (Others)

**Prompt.** Line: "We still come back to the question: Why did cheaper tokens cause a spike in cost?" (at 73.9%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 50 — T2 · `gen/1` (Gen)

**Prompt.** Line: "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?"
Estimate % of runtime.

**Gold.** 1.4%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 4.3 → **score 1.0**

### Exam 51 — T3 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "99% that if we build this technology we will all die — that claim in particular is the one I don't agree with."
B. "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived."
C. "But Yudkowsky and Soares also make a further claim that AI alignment is a cursed problem."
D. "What will that look like and how soon might that happen?"

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 0.0**

### Exam 52 — T4 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** {"title": "We are no longer in control of the AI situation.", "mode": "Adam", "runtime": "32:50", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.4, "spon": null, "conc": null, "turns": 8}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 3.6, "spon": null, "conc": 85.1, "turns": 7} → **score 1.0**

### Exam 53 — T5 · `esp/01-spacex` (Especially)

**Prompt.** Profile {"dur": 24.9, "wpm": 215, "hook": 91, "you": 18.0}

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Mechanism" → **score 1.0**

### Exam 54 — T6 · `gen/10` (Gen)

**Prompt.** Order these:
0. "So, what I'll do is I'll put in just $20 million of my own cash and borrow the other $80 million from the bank."
1. "But the question remains, is this really the next 2008?"
2. "So, what's wrong with that?"
3. "Now, here's where the system gets really dangerous."

**Gold.** [2, 0, 3, 1]

**Rubric.** pairwise order accuracy

**Taken answer.** [1, 0, 2, 3] → **score 0.33**

### Exam 55 — T1 · `esp/01-spacex` (Especially)

**Prompt.** Line: "Now let's get back to it." (at 51.7%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 56 — T2 · `after/10-water` (Others)

**Prompt.** Line: "We've all noticed our wells have pretty much dried up."
Estimate % of runtime.

**Gold.** 6.1%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 45 → **score 0.0**

### Exam 57 — T3 · `gen/9` (Gen)

**Prompt.** Options:
A. "And when a company borrows like this, it has to hand over paperwork saying what it already owes and what it's planning to owe."
B. "Every single metric says that the economy is cooked."
C. "So, back to the question I started with of who's actually right, the hedge fund shorting the market or these three groups?"
D. "So, do you see here that if you're paid in the share price, being cautious is like the most expensive mistake."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 58 — T4 · `gen/5` (Gen)

**Prompt.** {"title": "Why Canceling Data Centers is Going Horribly Wrong", "mode": "Gen", "runtime": "16:31", "has_sponsor": true} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 8.7, "spon": 35.6, "conc": 97.7, "turns": 5}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 10.3, "spon": 41.0, "conc": 81.8, "turns": 6} → **score 0.75**

### Exam 59 — T5 · `esp/02-ai-paradox` (Especially)

**Prompt.** Profile {"dur": 16.3, "wpm": 144, "hook": 61, "you": 27.8}

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Others" → **score 0.0**

### Exam 60 — T6 · `adam/05-sam-altman` (Adam)

**Prompt.** Order these:
0. "So, what do you need if you've just been fired by one of the most important companies in tech and you'd ideally like your job back?"
1. "Now, minutes later, the board puts out a public statement."
2. "Now, there are a few possible readings for why so many employees signed this letter so quickly."
3. "We've put a link in the description of this video."

**Gold.** [1, 0, 2, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [3, 0, 1, 2] → **score 0.33**

### Exam 61 — T1 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Line: "But also, maybe a lot of this is just hype?" (at 86.0%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "CONCLUSION" → **score 0.0**

### Exam 62 — T2 · `gen/1` (Gen)

**Prompt.** Line: "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?"
Estimate % of runtime.

**Gold.** 1.4%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 4.5 → **score 1.0**

### Exam 63 — T3 · `after/11-anthropic-ipo` (Others)

**Prompt.** Options:
A. "Okay, am I crazy or is it really starting to smell a lot like robot apocalypse in here?"
B. "Not Anthropic, or its employees or executives, but Claude, their chatbot."
C. "He wants the government to coordinate with the labs on this."
D. "AI safety researchers talk a lot about alignment."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 64 — T4 · `gen/3` (Gen)

**Prompt.** {"title": "If Housing is F*cked, Why Hasn\u2019t It Crashed?", "mode": "Gen", "runtime": "22:43", "has_sponsor": true} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.2, "spon": 43.5, "conc": 76.9, "turns": 5}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 9.7, "spon": 38.8, "conc": 88.2, "turns": 6} → **score 0.5**

### Exam 65 — T5 · `after/06-diamonds` (Others)

**Prompt.** Profile {"dur": 16.6, "wpm": 171, "hook": 45, "you": 17.6}

**Gold.** "Others"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Others" → **score 1.0**

### Exam 66 — T6 · `after/11-anthropic-ipo` (Others)

**Prompt.** Order these:
0. "But who or what does the constitution govern?"
1. "If this technology truly will change everything, integrate into all parts of our lives and potentially destroy the world, I wanted to know: Can Dario Amodei or any of these […]"
2. "Thank you so much for watching."
3. "Now, looking back, it all feels pretty sad rather than successful."

**Gold.** [1, 3, 0, 2]

**Rubric.** pairwise order accuracy

**Taken answer.** [0, 1, 3, 2] → **score 0.67**

### Exam 67 — T1 · `adam/05-sam-altman` (Adam)

**Prompt.** Line: "Ultimately, he blinked." (at 76.2%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** CONCLUSION

**Rubric.** 1 if exact, else 0

**Taken answer.** "CONCLUSION" → **score 1.0**

### Exam 68 — T2 · `gen/8` (Gen)

**Prompt.** Line: "And if nothing changes, we don't just lose the last rare places where somebody still gives a everywhere is about to look, feel, and get treated like it's built to die."
Estimate % of runtime.

**Gold.** 6.1%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 45 → **score 0.0**

### Exam 69 — T3 · `gen/4` (Gen)

**Prompt.** Options:
A. "And two, if AI could actually help companies replace the humans like it kind of promised."
B. "So, come with me, you guys, to replace my employee with AI."
C. "I just have to make my own staff use it by any means necessary, whether that's threatening promotions or firing their asses."
D. "Because I spent 3 weeks studying everyone else's company, and not once had I looked at my own."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 70 — T4 · `gen/4` (Gen)

**Prompt.** {"title": "The (Overdue) Collapse Of Artificial Intelligence", "mode": "Gen", "runtime": "20:31", "has_sponsor": true} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 9.8, "spon": 39.0, "conc": 70.5, "turns": 7}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 9.7, "spon": 38.8, "conc": 88.2, "turns": 6} → **score 0.75**

### Exam 71 — T5 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Profile {"dur": 32.8, "wpm": 144, "hook": 127, "you": 8.0}

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 72 — T6 · `esp/02-ai-paradox` (Especially)

**Prompt.** Order these:
0. "But here's the catch."
1. "Hi."
2. "But then when the help was removed for future puzzles, group A collapsed."
3. "Thank you so much for watching this video."

**Gold.** [1, 2, 0, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [0, 1, 2, 3] → **score 0.67**

### Exam 73 — T1 · `gen/10` (Gen)

**Prompt.** Line: "Now, here's where the system gets really dangerous." (at 21.5%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 74 — T2 · `after/12-data-centres-not-working` (Others)

**Prompt.** Line: "Let's get into it."
Estimate % of runtime.

**Gold.** 7.9%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 4.3 → **score 1.0**

### Exam 75 — T3 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Options:
A. "It was a strange summer."
B. "We identified that agents had taken over the internal Artifactory."
C. "In 2023, AI's top CEOs warned it could cause human extinction."
D. "Many of them also have impossible tasks and get stuck and start poking around their environment and find the message board."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 0.0**

### Exam 76 — T4 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** {"title": "We are no longer in control of the AI situation.", "mode": "Adam", "runtime": "32:50", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.4, "spon": null, "conc": null, "turns": 8}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 4.7, "spon": null, "conc": 85.1, "turns": 7} → **score 1.0**

### Exam 77 — T5 · `gen/6` (Gen)

**Prompt.** Profile {"dur": 22.3, "wpm": 200, "hook": 222, "you": 20.9}

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Gen" → **score 1.0**

### Exam 78 — T6 · `adam/01-ai-disaster` (Adam)

**Prompt.** Order these:
0. "But here's the thing."
1. "Now, we don't know exactly how the Grok chatbot on X works under the hood, but we do know that its claim to fame since the beginning has been its […]"
2. "So, if you're Elon Musk and you're not happy with the outputs that your model is generating, you have a few different options."
3. "Grok, I've been wondering as an AI, are you able to worship any God?"

**Gold.** [2, 3, 1, 0]

**Rubric.** pairwise order accuracy

**Taken answer.** [1, 2, 3, 0] → **score 0.67**

### Exam 79 — T1 · `adam/04-superintelligence` (Adam)

**Prompt.** Line: "So let's just quickly take stock of how this dangerous behavior arose in this scenario." (at 45.1%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 80 — T2 · `gen/4` (Gen)

**Prompt.** Line: "Amazon tore down that leaderboard that it built with a senior executive admitting its mistake that it was created with good intentions, but at the end of the day, all it did was push costs up."
Estimate % of runtime.

**Gold.** 70.5%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 86.1 → **score 0.5**

### Exam 81 — T3 · `adam/04-superintelligence` (Adam)

**Prompt.** Options:
A. "The impact of superhuman AI over the next decade will exceed that of the industrial revolution."
B. "It's now January 2027, and OpenBrain has been training Agent-2, the latest iteration of their AI agent models."
C. "Remember at this point, Agent-4 is responsible for almost all the AI development progress happening within OpenBrain."
D. "One of the main ways we have of making models smarter is to give them a scratch pad and time to think out loud."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 82 — T4 · `esp/03-oil-apocalypse` (Oil)

**Prompt.** {"title": "The oil apocalypse is here", "mode": "Mechanism", "runtime": "35:28", "has_sponsor": true} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 4.5, "spon": 27.5, "conc": 95.2, "turns": 7}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 6.0, "spon": 18.0, "conc": 90, "turns": 7} → **score 1.0**

### Exam 83 — T5 · `esp/06-data-centers` (Especially)

**Prompt.** Profile {"dur": 34.5, "wpm": 208, "hook": 126, "you": 14.1}

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Gen" → **score 0.0**

### Exam 84 — T6 · `adam/02-bestselling-book` (Adam)

**Prompt.** Order these:
0. "Now, that example — pretty harmless."
1. "If we keep scaling intelligence, at some point will we see systems that are so powerful and so goal-oriented that our current black-box way of training them becomes a civilization-scale […]"
2. "I want to take you through that story."
3. "The last thing to say is just thank you so much for watching, for being the reason that we make these videos."

**Gold.** [2, 0, 1, 3]

**Rubric.** pairwise order accuracy

**Taken answer.** [2, 0, 1, 3] → **score 1.0**

### Exam 85 — T1 · `esp/02-ai-paradox` (Especially)

**Prompt.** Line: "dev and use code art for 25% off your first year or use this QR code." (at 38.0%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SPONSOR READ

**Rubric.** 1 if exact, else 0

**Taken answer.** "SPONSOR READ" → **score 1.0**

### Exam 86 — T2 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Line: "Thank you so much for watching."
Estimate % of runtime.

**Gold.** 99.6%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 98.7 → **score 1.0**

### Exam 87 — T3 · `gen/7` (Gen)

**Prompt.** Options:
A. "why people act in certain ways in certain situations so how did it go from"
B. "were politically incorrect on campus yes heavily so and so it was a major uh"
C. "it has eviscerated my life in every way possible and I almost jumped What"
D. "sued in 2019 and yeah I've been in this stupid fight since November 2015"

**Gold.** C

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 0.0**

### Exam 88 — T4 · `adam/04-superintelligence` (Adam)

**Prompt.** {"title": "We're Not Ready for Superintelligence", "mode": "Adam", "runtime": "34:05", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 3.9, "spon": null, "conc": 88.7, "turns": 7}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 5.4, "spon": null, "conc": 85.1, "turns": 7} → **score 1.0**

### Exam 89 — T5 · `adam/04-superintelligence` (Adam)

**Prompt.** Profile {"dur": 34.1, "wpm": 177, "hook": 79, "you": 12.3}

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 90 — T6 · `esp/01-spacex` (Especially)

**Prompt.** Order these:
0. "I'll see you in the next one."
1. "And this is just the beginning of the space frontier, which really is infinite."
2. "But here's where we all stop."
3. "This video is sponsored by Wealthfront."

**Gold.** [3, 2, 1, 0]

**Rubric.** pairwise order accuracy

**Taken answer.** [3, 1, 2, 0] → **score 0.83**

### Exam 91 — T1 · `gen/7` (Gen)

**Prompt.** Line: "behind the screen it's not that I am against hate speech I think that's" (at 88.5%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** CONCLUSION

**Rubric.** 1 if exact, else 0

**Taken answer.** "CONCLUSION" → **score 1.0**

### Exam 92 — T2 · `gen/7` (Gen)

**Prompt.** Line: "consistently helps me with that is my sponsor straight arrow news so straight"
Estimate % of runtime.

**Gold.** 20.3%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 34.5 → **score 0.5**

### Exam 93 — T3 · `gen/9` (Gen)

**Prompt.** Options:
A. "What's important is what really does have to be true for any of this to make sense."
B. "Every single metric says that the economy is cooked."
C. "Whenever it shifts, somebody actually has to pay for it."
D. "And by July, its debt got downgraded to one notch above junk, which meant lenders started charging more to insure it."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 94 — T4 · `gen/9` (Gen)

**Prompt.** {"title": "WTF Is Happening To The Stock Market?", "mode": "Gen", "runtime": "22:38", "has_sponsor": true} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 2.9, "spon": 34.5, "conc": null, "turns": 9}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 8.9, "spon": 40.0, "conc": 78.4, "turns": 6} → **score 0.5**

### Exam 95 — T5 · `esp/06-data-centers` (Especially)

**Prompt.** Profile {"dur": 34.5, "wpm": 208, "hook": 126, "you": 14.1}

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Mechanism" → **score 1.0**

### Exam 96 — T6 · `after/07-trump-family` (Others)

**Prompt.** Order these:
0. "Meanwhile, the Albanian government cleared the way."
1. "Now, the problem is a traditional VPN is just another company that you're sharing personal data with, that can be leaked or requested."
2. "Now, while the name Kushner elevated it into an international story, for many in Albania, this remains a fight over who controls their country."
3. "And that's why today's sponsor Obscura caught my attention."

**Gold.** [1, 3, 0, 2]

**Rubric.** pairwise order accuracy

**Taken answer.** [2, 3, 0, 1] → **score 0.17**

### Exam 97 — T1 · `gen/2` (Gen)

**Prompt.** Line: "So, now let's talk about which channels have actually been bought and the few players behind them all." (at 49.5%)
Options: COLD OPEN / HOOK / PROMISE / ROADMAP / SECTION TURN / SPONSOR READ / CONCLUSION / CTA

**Gold.** SECTION TURN

**Rubric.** 1 if exact, else 0

**Taken answer.** "SECTION TURN" → **score 1.0**

### Exam 98 — T2 · `adam/02-bestselling-book` (Adam)

**Prompt.** Line: "I think that's basically the plan for AI companies today."
Estimate % of runtime.

**Gold.** 87.6%

**Rubric.** 1.0 if |Δ|≤10, 0.5 if ≤20, else 0

**Taken answer.** 81.4 → **score 1.0**

### Exam 99 — T3 · `gen/3` (Gen)

**Prompt.** Options:
A. "So, let's buy a house together."
B. "So, surely some of them might give me grants or tax breaks if I if I ask for some."
C. "I mean the last year alone there's been three real attempts at fixing housing."
D. "You can import your existing emails and contacts, and even keep using your Gmail until you're ready to leave."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 100 — T4 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** {"title": "We are no longer in control of the AI situation.", "mode": "Adam", "runtime": "32:50", "has_sponsor": false} → give hook-end %, first sponsor %, conclusion %, turns.

**Gold.** {"hook": 6.4, "spon": null, "conc": null, "turns": 8}

**Rubric.** 1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2

**Taken answer.** {"hook": 4.8, "spon": null, "conc": 86.5, "turns": 7} → **score 1.0**