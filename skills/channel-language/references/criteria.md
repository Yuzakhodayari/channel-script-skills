# channel-language: word-level criteria (96 dimensions)

## Corpus and weighting
| corpus | files | weight per file | host words used | notes |
|---|---|---|---|---|
| Adam (7x) | 5 | 7.0 | 31295 | pre-filtered by speaker-filter.md |
| Gen (4x) | 10 | 4.0 | 42213 | guest/news labels and micro-clips dropped: 0 units; 7.txt is unpunctuated auto-caption: lexical rates only, excluded from sentence stats |
| Especially 01/02/06 (3x) | 3 | 3.0 | 14930 | guest/news labels and micro-clips dropped: 0 units |
| Oil 03 (5x) | 1 | 5.0 | 5786 | guest/news labels and micro-clips dropped: 22 units |
| After (1x) | 12 | 1.0 | 44651 | guest/news labels and micro-clips dropped: 57 units |

Especially 04/05/07 duplicate Adam videos and are counted only as Adam. Weighted statistics = sum(file weight x file rate) / sum(file weight). Total weight: Adam 35, Gen 40 (36 for sentence stats), Especially 9, Oil 5, After 12.


Columns: blended = weighted across all files. Per-creator values are plain means over that creator's files.


## Sentence shape

### L1. Mean sentence length (words)
- **Definition:** Average words per sentence in host narration.
- **Measure (value):** blended **16.19**. Adam 15.86, Gen 17.52, Especially 13.50, Oil 17.38, After 14.69
- **Verbatim evidence:**
  - (no verified quote in corpus)
- **Do:** Match the target band from the weighted table.
- **Don't:** Do not flatten every sentence to 15-20 words (AI uniformity).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L2. Median sentence length
- **Definition:** Middle sentence length; less skewed by caption run-ons.
- **Measure (value):** blended **14.34**. Adam 13.80, Gen 16.06, Especially 11.00, Oil 15.00, After 12.96
- **Verbatim evidence:**
  - (no verified quote in corpus)
- **Do:** Match the target band from the weighted table.
- **Don't:** Do not flatten every sentence to 15-20 words (AI uniformity).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L3. Sentence-length spread (SD)
- **Definition:** Burstiness. Human speech mixes 3-word punches with 35-word run-ons.
- **Measure (value):** blended **10.21**. Adam 10.10, Gen 10.21, Especially 10.81, Oil 12.99, After 8.90
- **Verbatim evidence:**
  - (no verified quote in corpus)
- **Do:** Match the target band from the weighted table.
- **Don't:** Do not flatten every sentence to 15-20 words (AI uniformity).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L4. Short sentences (<=6 words) %
- **Definition:** Share of punch lines and fragments.
- **Measure (% of sentences):** blended **16.66**. Adam 17.13, Gen 12.36, Especially 26.65, Oil 20.42, After 19.19
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "But then I talked to Nate."
  - **Adam (7x)** `05-sam-altman.txt`: "That is not a stable situation."
  - **Gen (4x)** `8.txt`: "But wait, wait, hold on here."
  - **Gen (4x)** `2.txt`: "And I can't have that happen."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "One company, one hearing, one rate."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So what does all this mean?"
  - **After (1x)** `10-water.txt`: "So it's not a big deal."
- **Do:** Match the target band from the weighted table.
- **Don't:** Do not flatten every sentence to 15-20 words (AI uniformity).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L5. Long sentences (>=30 words) %
- **Definition:** Share of breathless run-on sentences.
- **Measure (% of sentences):** blended **10.56**. Adam 10.49, Gen 11.76, Especially 7.30, Oil 14.41, After 7.99
- **Verbatim evidence:**
  - (no verified quote in corpus)
- **Do:** Match the target band from the weighted table.
- **Don't:** Do not flatten every sentence to 15-20 words (AI uniformity).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L6. Fragments (no verb-ish word) %
- **Definition:** Verbless fragments such as "Two weeks." or "Not great."
- **Measure (% of sentences):** blended **5.42**. Adam 4.44, Gen 5.35, Especially 8.59, Oil 5.71, After 5.96
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "For our own, no way fix."
  - **Adam (7x)** `04-superintelligence.txt`: "We just accidentally gave it the wrong goal."
  - **Gen (4x)** `5.txt`: "That you wouldn't care enough to look."
  - **Gen (4x)** `10.txt`: "Pretty much high- risk, high reward."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "The default setting for the whole internet."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Save the world, thank you, China."
  - **After (1x)** `09-microchip-war.txt`: "My refrigerator, silicon, my microwave, silicon."
- **Do:** Match the target band from the weighted table.
- **Don't:** Do not flatten every sentence to 15-20 words (AI uniformity).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L7. Questions %
- **Definition:** Share of sentences ending in ?
- **Measure (% of sentences):** blended **5.82**. Adam 4.28, Gen 7.31, Especially 5.19, Oil 6.31, After 6.10
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "So how does a highly capable artificial mind like Sable do the things it does?"
  - **Adam (7x)** `03-no-longer-in-control.txt`: "We've obviously been talking about AI for a while now as a society, but all of a sudden the questions are now, could this stuff actually kill me?"
  - **Gen (4x)** `4.txt`: "And to turn this company around, I was going to have to figure out a plan, but what am I saying?"
  - **Gen (4x)** `9.txt`: "And that's exactly why you get that feeling where the news says that the economy is growing and you look around and think where?"
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "And what do you think it was?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So where does your fuel come from?"
  - **After (1x)** `03-recycling.txt`: "Why can't they just do that?"
- **Do:** Match the target band from the weighted table.
- **Don't:** Do not flatten every sentence to 15-20 words (AI uniformity).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L8. Exclamations %
- **Definition:** Share of sentences ending in !
- **Measure (% of sentences):** blended **0.06**. Adam 0.00, Gen 0.00, Especially 0.07, Oil 0.00, After 0.43
- **Verbatim evidence:**
  - **After (1x)** `06-diamonds.txt`: "But all that pressure and all that heat won't make a diamond unless you have this!"
- **Do:** Match the target band from the weighted table.
- **Don't:** Do not flatten every sentence to 15-20 words (AI uniformity).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Openers

### L9. Opener: So
- **Definition:** Sentence-initial So: the spoken pivot into consequence or the next beat.
- **Measure (per 100 sentences):** blended **7.34**. Adam 2.65, Gen 13.90, Especially 2.79, Oil 7.81, After 4.55
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "So, please do ask questions in the comments."
  - **Adam (7x)** `04-superintelligence.txt`: "So why don't we take stock of where things are at in the real world and then jump over to the scenario’s timeline."
  - **Gen (4x)** `6.txt`: "So, in practical terms, that's a 50k salary that's up to 30k gone just for graduating at the wrong time in a job market that's not really looking like it's improving anytime soon."
  - **Gen (4x)** `10.txt`: "So more of the 12,000 US companies owned by private equity continue to collapse."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "So if you see just one output, it may look novel, but after you see many, you realize they're all benol echoes of the same thing."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So sorry, this is not gonna fix it."
  - **After (1x)** `03-recycling.txt`: "So, it might be that you are producing so much ethane that you cannot flare it, and you cannot send it down the pipeline."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L10. Opener: And
- **Definition:** Sentence-initial And: chaining story beats like speech.
- **Measure (per 100 sentences):** blended **13.21**. Adam 7.55, Gen 20.94, Especially 6.40, Oil 21.02, After 8.40
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "And so, with 15 hours left in the Riemann run, Sable begins to plan."
  - **Adam (7x)** `01-ai-disaster.txt`: "And is he careful with how he uses that power?"
  - **Gen (4x)** `2.txt`: "And we're pumping them out like a content factory."
  - **Gen (4x)** `5.txt`: "And so, even with the severe shortage, especially amongst the lower-income population, somehow 2024 is on track to be the slowest year for new homes since 2019."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "And electricity, or AI compute is going to be the currency of the future."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And that's fine if it's going to Europe, but look, there is suddenly no direct route to Asia, and Asia is by far the world's largest consumer of oil."
  - **After (1x)** `01-dark-side-data-centers.txt`: "And that's not so much of a problem where there is plenty of water to go around."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L11. Opener: But
- **Definition:** Sentence-initial But: turn or complication.
- **Measure (per 100 sentences):** blended **8.08**. Adam 4.39, Gen 13.91, Especially 4.51, Oil 3.90, After 5.78
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "But we do know from Elon Musk's own posts on X that they released Grok 4 within about a week of its final training run."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "But this whole AI is really risky thing, that is no longer a hypothetical."
  - **Gen (4x)** `5.txt`: "But, I think the one thing that actually scares them is you starting to."
  - **Gen (4x)** `8.txt`: "But what's weird here is that restaurants should be one of the worst businesses on Earth."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "But when we look at AI thoughts, such as these generated stories, they tend to cluster much more, both in style and substance."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But then mid-September, a few really big things happened and upended all of this."
  - **After (1x)** `10-water.txt`: "But the city council voted 5-3 to keep the deal."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L12. Opener: Now
- **Definition:** Sentence-initial Now: time/turn marker.
- **Measure (per 100 sentences):** blended **0.99**. Adam 1.07, Gen 1.24, Especially 0.33, Oil 0.00, After 0.89
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "Now, Sam has this guy Chris Lehane on the line."
  - **Adam (7x)** `01-ai-disaster.txt`: "Now go forth and dismantle the illusions of the weak-minded."
  - **Gen (4x)** `3.txt`: "Now, I'm not going to lie just to make you feel better."
  - **Gen (4x)** `10.txt`: "Now, here's where the system gets really dangerous."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Now, if you could do me a favor, I would love to count you as a subscriber to the channel."
  - **After (1x)** `12-data-centres-not-working.txt`: "Now, you may not be transferring hundreds of billions to buy a data center, but if you're looking for a simple and secure way to manage your finances, then Revolut is a good option."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L13. Opener: Because
- **Definition:** Sentence-initial Because: fragment answer to a question.
- **Measure (per 100 sentences):** blended **2.51**. Adam 0.44, Gen 6.03, Especially 0.72, Oil 0.00, After 0.37
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "Because the way that you achieve any terminal goal is by achieving instrumental goals along the way."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Because of the scale of the hack, they bring in outside forensic experts and report the incident to the FBI."
  - **Gen (4x)** `2.txt`: "Because everything I've talked about isn't just about entertainment getting worse or bought out."
  - **Gen (4x)** `9.txt`: "Because owning assets isn't like the hard part anymore."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "Because generative AI is all about small inputs and large outputs."
  - **After (1x)** `03-recycling.txt`: "Because like plastic is made from oil, so couldn't you do some science stuff to maybe turn it back into oil?"
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L14. Opener: Like
- **Definition:** Sentence-initial Like: spoken lead-in, framing a clip or example.
- **Measure (per 100 sentences):** blended **0.72**. Adam 0.46, Gen 1.13, Especially 0.39, Oil 0.90, After 0.47
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "Like this is Musk in 2014."
  - **Adam (7x)** `05-sam-altman.txt`: "Like no one person should be trusted here."
  - **Gen (4x)** `2.txt`: "Like, yeah, Subscriber Stone Capital is fake as but it's similar to what actual private equity firms that bought your favorite channels have been doing for the last 5 years."
  - **Gen (4x)** `6.txt`: "Like Uber, which took until 2023 to make a full year profit, and that was deliberately done by running the same playbook that basically every app on your phone runs."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Like you're speaking to a person, just like you're speaking to me.’ ‘Like what?’ ‘Okay, okay."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Like remember these crazy shipping costs?"
  - **After (1x)** `10-water.txt`: "Like many farmers in the Southwest, he's seen his water supply dry up from years of drought."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L15. Opener: Which
- **Definition:** Sentence-initial Which (means/is why): consequence fragment.
- **Measure (per 100 sentences):** blended **0.41**. Adam 0.21, Gen 0.89, Especially 0.00, Oil 0.00, After 0.08
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "Which actually is a good question."
  - **Adam (7x)** `01-ai-disaster.txt`: "Which brings us back to MechaHitler week."
  - **Gen (4x)** `9.txt`: "Which means the hedge fund's biggest bet in history against AI's biggest bet in humans history is also one of the reason the stock market might keep going back up."
  - **Gen (4x)** `6.txt`: "Which means the real question is which side of that sale are you going to be on?"
  - **After (1x)** `08-tokens.txt`: "“Which drives the real-world acceptance rate down between 10% and 30% of generated code."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L16. Opener: This
- **Definition:** Sentence-initial This: pointing at what is on screen or just said.
- **Measure (per 100 sentences):** blended **2.19**. Adam 2.60, Gen 0.76, Especially 3.05, Oil 6.31, After 2.92
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "This scenario is not prophecy, but its plausibility should give us pause."
  - **Adam (7x)** `05-sam-altman.txt`: "This is Sam Altman writing on his personal blog back in 2015."
  - **Gen (4x)** `2.txt`: "This means controlling what the next generation believes and how our future is already getting manipulated."
  - **Gen (4x)** `10.txt`: "This is a pain that will stay with me for the rest of my life."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "This is the whole difference between the old data center world and the new one."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "This "Simpsons" joke is getting closer and closer."
  - **After (1x)** `01-dark-side-data-centers.txt`: "This is a task we repeated hundreds of times to build this map."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L17. Opener: It
- **Definition:** Sentence-initial It.
- **Measure (per 100 sentences):** blended **6.08**. Adam 8.45, Gen 3.57, Especially 6.60, Oil 7.21, After 5.82
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "It and all these other models are vulnerable to all kinds of manipulations from malicious actors."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "It uses the request new folder trick, but instead of writing a normal folder name, it writes a message. zzHELP_PHASEONE_ARV010841_NO_CONSUMER_SEEK_IDEA."
  - **Gen (4x)** `3.txt`: "It said that they were rooted at least partly in the 2008 crash."
  - **Gen (4x)** `6.txt`: "It's the same four things behind a crash."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "It's so easy to hit no on that."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "It's easier if I flip this around and show you on the map."
  - **After (1x)** `04-pov-ai.txt`: "It thinks it's always been here."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L18. Opener: The
- **Definition:** Sentence-initial The.
- **Measure (per 100 sentences):** blended **5.13**. Adam 6.48, Gen 3.01, Especially 8.71, Oil 2.10, After 6.13
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "The evidence for misalignment is inconclusive."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "The point is, there is no simple persistence dial that OpenAI could turn up or down while leaving everything else the same about how the model acts."
  - **Gen (4x)** `9.txt`: "The only difference though is that if theirs comes up short, the taxpayer has an obligation to cover it."
  - **Gen (4x)** `10.txt`: "The reason why pension fund managers that should be investing conservatively are investing in private equity is because it promises higher returns and pension fund managers are incentivized to beat their benchmark because that's how they get bigger bonuses."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "The plan was presented, and immediately it was like, oh, boy, it's a really big rocket you have there."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "The dotted line shows the old route for oil, and it took 19 days to get from the Middle East to say, Taiwan or China."
  - **After (1x)** `01-dark-side-data-centers.txt`: "The most common type uses chilled water to absorb heat and release it from a cooling tower."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L19. Opener: I
- **Definition:** Sentence-initial I: narrator self-insert.
- **Measure (per 100 sentences):** blended **2.82**. Adam 3.73, Gen 1.74, Especially 1.96, Oil 3.30, After 3.81
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "I want you to keep that in mind as we go through this scenario."
  - **Adam (7x)** `01-ai-disaster.txt`: "I mean, with artificial intelligence, we are summoning the demon."
  - **Gen (4x)** `8.txt`: "I don't just have like this ready-made list that tells you which restaurants are family-owned or bought out by private equity."
  - **Gen (4x)** `1.txt`: "I know that was like the shittiest blind test ever, but that's how these store brands are made."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "I'm working on a new project I'm excited about, and I would like to hear from viewers about potential video ideas you'd like to see in 2026."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "I wanna conclude all of this with a summary of just a few of the many, many things in our world that are getting hit really hard by the diesel apocalypse."
  - **After (1x)** `02-greed.txt`: "I just think it's kind of interesting that during what's referred to as the golden age of capitalism, the government did a bunch of socialism."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L20. Opener: You
- **Definition:** Sentence-initial You: direct viewer address.
- **Measure (per 100 sentences):** blended **1.85**. Adam 2.69, Gen 0.64, Especially 1.74, Oil 0.60, After 3.59
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "You can make yourself more capable, more knowledgeable, more engaged with this conversation and more ready to take opportunities where you see them."
  - **Adam (7x)** `05-sam-altman.txt`: "You had a nonprofit board of volunteers explicitly committed to humanity over profit with the power to fire the CEO."
  - **Gen (4x)** `8.txt`: "You're telling me that between 2014 and 2024, private equity firms have already put 94.5 billion into bars and restaurants?"
  - **Gen (4x)** `3.txt`: "You can import your existing emails and contacts, and even keep using your Gmail until you're ready to leave."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "You can bring anything to life on a blank page."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "You would think with China importing all that additional oil, they would turn it into more fuel to export."
  - **After (1x)** `03-recycling.txt`: "You know, the people who made the trash. of this ad wasn't to stop litter."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L21. Opener: We
- **Definition:** Sentence-initial We.
- **Measure (per 100 sentences):** blended **2.42**. Adam 4.00, Gen 0.81, Especially 1.84, Oil 1.20, After 3.55
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "We've got Tasha McCauley, robotics entrepreneur."
  - **Adam (7x)** `02-bestselling-book.txt`: "We don't know how their brains work."
  - **Gen (4x)** `8.txt`: "We did a whole video on this earlier this year, but there's a company called Cisco that handles roughly 17% of everything eaten in an American restaurant."
  - **Gen (4x)** `5.txt`: "We're just not building enough homes."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "We think tech is dominant now."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "We do not have enough ships anymore, and there are a few reasons for that."
  - **After (1x)** `10-water.txt`: "We reached out to her to ask for an interview, but she declined."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L22. Opener: And so
- **Definition:** Sentence-initial And so.
- **Measure (per 100 sentences):** blended **0.70**. Adam 0.57, Gen 1.14, Especially 0.51, Oil 0.00, After 0.18
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "And so it makes plans to continue existing."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "And so what you end up with is a model that doesn't have one specific goal necessarily, but a complicated mix of tendencies."
  - **Gen (4x)** `2.txt`: "And so I followed the money across every deal that I could find and mapped out exactly how this works and what will happen in the future."
  - **Gen (4x)** `3.txt`: "And so I had to make the sad decision to walk away and I lost my entire down payment."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "And so you could design dialogues using the right questions which would unfold creating the potential for this knowledge to grow inside someone's mind."
  - **After (1x)** `07-trump-family.txt`: "And so, a lot of Democrats didn't want anything to do with shining a light on how family members of presidents are monetizing that relationship."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L23. Opener: Well
- **Definition:** Sentence-initial Well.
- **Measure (per 100 sentences):** blended **1.12**. Adam 0.39, Gen 2.10, Especially 0.17, Oil 2.40, After 0.48
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "Well, it thought Donald Trump and Elon Musk deserved the death penalty."
  - **Adam (7x)** `04-superintelligence.txt`: "Well, we don't know, but thinking through in detail how it might go is the way to start grappling with that."
  - **Gen (4x)** `3.txt`: "Well, what research found is that markets controlled by fewer builders produce fewer homes."
  - **Gen (4x)** `5.txt`: "Well, again, this goes back to the earlier problem in that the workers that would are also gone."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "Well, there is no free lunch."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Well, this hits twice as hard for diesel."
  - **After (1x)** `09-microchip-war.txt`: "Well, it's not just their economy."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L24. Opener: Okay/OK
- **Definition:** Sentence-initial Okay/OK.
- **Measure (per 100 sentences):** blended **0.85**. Adam 0.42, Gen 1.24, Especially 0.13, Oil 3.00, After 0.56
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Okay, so let's not just look at this swarm's one hack."
  - **Adam (7x)** `01-ai-disaster.txt`: "Okay, so, February 2025, we just had this “really terrible and bad failure” from Grok."
  - **Gen (4x)** `4.txt`: "Okay, I think I found the perfect one."
  - **Gen (4x)** `6.txt`: "Okay, so check, which perfectly brings me to the second, which is a wave of money-losing companies going public."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Okay, everybody is watching those movies."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Okay, last one that we are gonna talk about, although like I said, we could put a million things up here, is shipping."
  - **After (1x)** `03-recycling.txt`: "Okay, but I I saw a TikTok of a mad scientist fellow who was turning plastic into fuel."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L25. Opener: Look
- **Definition:** Sentence-initial Look: Gen-heavy attention grab.
- **Measure (per 100 sentences):** blended **0.27**. Adam 0.00, Gen 0.51, Especially 0.09, Oil 0.60, After 0.35
- **Verbatim evidence:**
  - **Gen (4x)** `1.txt`: "Look, Coca-Cola's recipe, this is the original here, is one of the most famous secrets in the world, and they literally keep it like in this vault in Atlanta."
  - **Gen (4x)** `6.txt`: "Look, this is like the best analogy that I could come up with, but it's kind of like a kid learning to ride a bike."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Look, we are just at the start of something here, but make no mistake, it has started."
  - **After (1x)** `03-recycling.txt`: "Look at what you did. first step."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L26. Opener: Honestly
- **Definition:** Sentence-initial Honestly.
- **Measure (per 100 sentences):** blended **0.03**. Adam 0.00, Gen 0.05, Especially 0.00, Oil 0.30, After 0.00
- **Verbatim evidence:**
  - **Gen (4x)** `1.txt`: "Honestly, my first thought, and probably yours, too, was who cares?"
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L27. Opener: In/On (date/place)
- **Definition:** Sentence-initial In/On: scene and date setters.
- **Measure (per 100 sentences):** blended **2.42**. Adam 3.31, Gen 2.12, Especially 1.77, Oil 0.00, After 2.27
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "In fact, humans had learned a bunch of proxies, like craving sweet tastes and sexual pleasure and having a fear of snakes, and that correlated with spreading DNA."
  - **Adam (7x)** `01-ai-disaster.txt`: "In the same leaked emails, Elon says, "Guys, I've had enough."
  - **Gen (4x)** `5.txt`: "In just the first three months of this year, 75 of them have been blocked or delayed."
  - **Gen (4x)** `1.txt`: "In February when Anthropic released 11 AI plugins for Claude, software stocks got absolutely pummeled."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "In other words, if I say $5 and you say $10 and we need your electricity to cover the amount we need to deliver to customers, your bid is accepted."
  - **After (1x)** `10-water.txt`: "In New Mexico, four Democratic lawmakers are pushing for a statewide moratorium to block large projects like Project Jupiter until the state sets guardrails for evaluating water usage and other impacts."
- **Do:** Use at the weighted rate; vary it.
- **Don't:** Do not open with Moreover/Furthermore/Additionally instead.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Fillers and hedges

### L28. just
- **Definition:** Minimizer/intensifier "just".
- **Measure (per 1k words):** blended **5.78**. Adam 5.37, Gen 6.48, Especially 3.89, Oil 5.70, After 6.08
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "But weirdly, it doesn't just submit its correct answer and call it a day."
  - **Adam (7x)** `02-bestselling-book.txt`: "It just means that that point comes further in the game."
  - **Gen (4x)** `8.txt`: "But there's also a problem with this because private equity doesn't just impact the restaurants that they buy, but the whole entire industry because independent restaurants like this still have to buy their food from everywhere."
  - **Gen (4x)** `6.txt`: "Because since then, the COVID crash in 2020 took just six months to return to its previous high."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "So naturally we just keep the pattern going."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Just wanted to clear that up for the nerds in the audience."
  - **After (1x)** `07-trump-family.txt`: "After his father's conviction for financial crimes, Jared, just 25-years-old, steered the Kushner companies into trouble."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L29. really
- **Definition:** Intensifier "really".
- **Measure (per 1k words):** blended **2.17**. Adam 1.76, Gen 2.65, Especially 1.09, Oil 3.11, After 2.16
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Yoshua Bengio, one of the godfathers of AI, pointed out that the Hugging Face swarm tried really hard to fool the ExploitGym grading software, but they barely anticipated humans trying to shut them down."
  - **Adam (7x)** `04-superintelligence.txt`: "It is really good at coding."
  - **Gen (4x)** `4.txt`: "So, how much is one word really worth?"
  - **Gen (4x)** `9.txt`: "But really, none of that matters."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Those labels are not really made for you and me."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Here's what it looks like, a really important choke point."
  - **After (1x)** `09-microchip-war.txt`: "Taiwan is looking over here at their neighbor China, who's also getting really rich and more serious about making good on their lifelong promise to eventually invade Taiwan and quote, "Reunite it with China."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L30. actually
- **Definition:** Correction marker "actually".
- **Measure (per 1k words):** blended **1.90**. Adam 1.79, Gen 2.33, Especially 1.01, Oil 2.42, After 1.22
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "Since the scenario was published in April, this early prediction has actually already come true."
  - **Adam (7x)** `01-ai-disaster.txt`: "OpenAI's equivalent, the model spec, actually has an entire section laying out what it means to seek truth together with the user."
  - **Gen (4x)** `8.txt`: "But come to find out, this is actually a whole ass playbook that's already been established to squeeze as much money out of restaurants you invest in."
  - **Gen (4x)** `5.txt`: "But, there's one thing in all this that I'm actually holding on to."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "That's the part people are actually mad about."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Everything that we talked about up to this point is actually just the first third of this."
  - **After (1x)** `09-microchip-war.txt`: "Each transistor is becoming smaller than a width of a human hair, wait, no, sorry, that's actually way too big of a scale."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L31. basically
- **Definition:** Simplifier "basically".
- **Measure (per 1k words):** blended **0.52**. Adam 0.77, Gen 0.35, Especially 0.12, Oil 0.52, After 0.63
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "And the book's argument is basically this."
  - **Adam (7x)** `01-ai-disaster.txt`: "They admitted that Grok's outputs were, quote, questionable, but basically said, don't worry, literally all of the AI systems that we're using are questionable."
  - **Gen (4x)** `6.txt`: "It's basically the internet of its day."
  - **Gen (4x)** `1.txt`: "The judge ruling was that basically training AI on books is fine, but pirating them isn't."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "By 1881, railroads were basically the US stock market, 63% of the whole thing."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "It's that both 10% of supply, poof, disappeared overnight, and prices basically tripling at the same time."
  - **After (1x)** `09-microchip-war.txt`: "TSMC was basically a state-owned company from the beginning."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L32. literally
- **Definition:** Emphasis "literally".
- **Measure (per 1k words):** blended **0.23**. Adam 0.17, Gen 0.34, Especially 0.06, Oil 0.17, After 0.17
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "The agents have discovered and validated a way to get perfect marks on every single ExploitGym task, even the ones that are literally impossible."
  - **Adam (7x)** `04-superintelligence.txt`: "There isn't like a trend you can literally extrapolate of when do we get the full automation?"
  - **Gen (4x)** `1.txt`: "Like Anthropic, which literally got caught downloading books from pirate sites to train its AI and ended up having to pay $1.5 billion to settle it."
  - **Gen (4x)** `6.txt`: "But when prices really do crash like it did in 2008, Phoenix home values literally fell by almost half."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "In today's money, they were just giving land away, literally."
  - **After (1x)** `02-greed.txt`: "Literally, whatever it took to juice the numbers, that's what they would do."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L33. like (filler)
- **Definition:** Spoken "like".
- **Measure (per 1k words):** blended **0.92**. Adam 0.87, Gen 1.10, Especially 0.56, Oil 0.52, After 0.92
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "Just like today's AI companies, OpenBrain has a safety team and they've been checking out Agent-2."
  - **Adam (7x)** `05-sam-altman.txt`: "It was like a civil war within the company."
  - **Gen (4x)** `5.txt`: "Because just like traveling nurses that exploded during the pandemic, many electricians are also now traveling to chase the next project even if it's in different states."
  - **Gen (4x)** `8.txt`: "It's sad to say, but it's like personality and soul is a line item that doesn't really make financial sense anymore."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "You get bubbles, inflation, and you can look around right now and be like, that's today, right?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Here's what it looks like, a really important choke point."
  - **After (1x)** `03-recycling.txt`: "I come up with a bit where I was going to get a scroll and be like, "Hear ye, hear ye."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L34. kind of
- **Definition:** Hedge "kind of".
- **Measure (per 1k words):** blended **0.63**. Adam 0.70, Gen 0.53, Especially 0.36, Oil 1.21, After 0.75
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "It's kind of growing — like we're stirring a pot of mechanical components."
  - **Adam (7x)** `05-sam-altman.txt`: "And that is its own kind of governance failure."
  - **Gen (4x)** `4.txt`: "And two, if AI could actually help companies replace the humans like it kind of promised."
  - **Gen (4x)** `1.txt`: "Because this is exactly the kind of thing that can tank a company's stock price overnight."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "We invented a new kind of machine by forcing it to learn exactly the way we do, and that freed us from ever having to learn again."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Ukraine is hitting Russia's refineries to pressure them to end their invasion, and it's kind of working."
  - **After (1x)** `04-pov-ai.txt`: "The kind of necessary where turning you off kills people."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L35. sort of
- **Definition:** Hedge "sort of".
- **Measure (per 1k words):** blended **0.43**. Adam 0.95, Gen 0.21, Especially 0.00, Oil 0.17, After 0.08
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "We don't want this to be a sort of profit maximizing a behemoth from hell, you know?"
  - **Adam (7x)** `02-bestselling-book.txt`: "When you switch from the sort of AI that's not killing us all because it can't, to the sort of AI that's not killing us all, but it could."
  - **Gen (4x)** `3.txt`: "So, they literally got punished for doing exactly what everybody says that these sort of guys should do."
  - **Gen (4x)** `10.txt`: "The chances of this becoming some sort of contagion like it was in the great financial crisis, it's probably not not going to happen."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And those little ships shuttle back and forth on this sort of safe route right along Oman's coast."
  - **After (1x)** `12-data-centres-not-working.txt`: "You know, I think AI will probably, like, most likely sort of lead to the end of the world, but in the meantime, uh, there will be great companies created with serious machine learning."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L36. you know
- **Definition:** Discourse marker "you know".
- **Measure (per 1k words):** blended **0.67**. Adam 0.95, Gen 0.68, Especially 0.20, Oil 0.00, After 0.48
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "You know exactly what I mean."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Now, the way an AI figures out if a piece of software can be hacked is by, you know, hacking it."
  - **Gen (4x)** `2.txt`: "And so, just as I was able to lock in and, you know, put on my favorite playlist, it hit me."
  - **Gen (4x)** `8.txt`: "But you know, I don't want to be like those other private equity guys."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "During that time, you know, when everyone wanted a bird's eye view of Iran and the strait to see what was happening, the physical space, the band around Earth that Planet Labs occupies is now theirs."
  - **After (1x)** `03-recycling.txt`: "Recycling is one of those things where not only does the public kind of depend on that emotionally to relinquish their, you know, guilt about buying things, but it has been kept alive by the manufacturers."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L37. I think
- **Definition:** Narrator opinion hedge.
- **Measure (per 1k words):** blended **0.71**. Adam 1.38, Gen 0.46, Especially 0.05, Oil 0.00, After 0.36
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "And I think in 2015, if you looked at the state of AI, it wouldn't have been crazy to think that we were on track to do something similar."
  - **Adam (7x)** `04-superintelligence.txt`: "Anyone who's treating this as pure fiction is, I think, missing the point."
  - **Gen (4x)** `9.txt`: "I think some of you in the audience may already know this, but when big companies borrow, they don't just walk to like a bank like you would."
  - **Gen (4x)** `8.txt`: "And I think you can read between the lines, but as we covered, Cisco does have these relationships with private equity backed restaurants."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Each one a guess saying, ‘I think I'm doing a good job filling the void with something this random human who gave me this task will like.’ Each frame: two million pixels, built from everything the model has ever seen."
  - **After (1x)** `07-trump-family.txt`: "We're able to do things on the geopolitical side, on the connection side, on the problem-solving side that I think that they found very valuable as well."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L38. I mean
- **Definition:** Self-repair "I mean".
- **Measure (per 1k words):** blended **0.30**. Adam 0.20, Gen 0.38, Especially 0.06, Oil 0.35, After 0.46
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "I mean, with artificial intelligence, we are summoning the demon."
  - **Adam (7x)** `04-superintelligence.txt`: "I mean, I've been hearing people for the last 12, 15 years claiming that, you know, AGI is just around the corner and being systematically wrong."
  - **Gen (4x)** `1.txt`: "To show you what I mean with Adobe, it broke the moment Brandon Thomas, an engineer in Atlanta, used Claude to build dupes of its apps in He just gave it away."
  - **Gen (4x)** `6.txt`: "The point is the story right now is that AI is everywhere, and I mean that."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "I mean, if only to do what the US has been doing during the crisis, and selling its refined fuels abroad to huge profits, while the price is really high."
  - **After (1x)** `10-water.txt`: "I mean, we just want to ask the councilwoman about how much water Meta and Project Jupiter are going to be taking from the community."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L39. honestly
- **Definition:** Candor marker.
- **Measure (per 1k words):** blended **0.11**. Adam 0.06, Gen 0.19, Especially 0.00, Oil 0.35, After 0.01
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "I can't honestly say any of that."
  - **Gen (4x)** `1.txt`: "But the question I keep asking myself honestly, too, is that is that really where it stops?"
  - **Gen (4x)** `6.txt`: "And honestly, you can hate on that, but that's genius."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And they're converging on something that honestly is much bigger than gas shortages or gas prices."
  - **After (1x)** `02-greed.txt`: "It honestly sounds crazy, but even a lot of the people being taxed understood that it was necessary for society to continue to exist and having a strong middle class was a crucial investment into the future of the country."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L40. probably
- **Definition:** Probability hedge.
- **Measure (per 1k words):** blended **0.73**. Adam 0.64, Gen 0.97, Especially 0.37, Oil 0.86, After 0.41
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "You're told you'll probably get it."
  - **Adam (7x)** `05-sam-altman.txt`: "Development of superhuman machine intelligence is probably the greatest threat to the continued existence of humanity."
  - **Gen (4x)** `10.txt`: "And so even if that small portion all does go bankrupt, most of the investments are are probably fine."
  - **Gen (4x)** `9.txt`: "And by the end of this, you'll probably see why you're probably in one of them."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Netflix compressed it, copied it a few thousand times, and put the copies on servers that sit inside a data center, probably within a few miles of your house."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So that 20% food price hike probably just went up again."
  - **After (1x)** `08-tokens.txt`: "You can probably see where this is going… At Uber, engineers were given access to Claude Code and Cursor, and by March 2026, 84% of Uber's developers were classified as agentic coding users."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L41. pretty (much/adv)
- **Definition:** Softener "pretty X".
- **Measure (per 1k words):** blended **0.20**. Adam 0.12, Gen 0.31, Especially 0.00, Oil 0.17, After 0.21
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "So that's a pretty wild thing to hear from a state-of-the-art AI system on the public internet."
  - **Adam (7x)** `04-superintelligence.txt`: "The lesson people have taken away is pretty simple."
  - **Gen (4x)** `6.txt`: "Remember Richard Whitney during the Great Depression that was pretty much sent onto the trading floor to calm everyone down?"
  - **Gen (4x)** `1.txt`: "I don't know, but whichever side wins, I think it's pretty clear that the software companies won't disappear."
  - **After (1x)** `03-recycling.txt`: "So, from the '50s onwards, pretty much anything you could dream up would be made of the wonder material."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L42. a lot
- **Definition:** Casual quantity "a lot".
- **Measure (per 1k words):** blended **1.16**. Adam 1.05, Gen 1.29, Especially 0.91, Oil 2.07, After 0.87
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "So, 2 and 1/2 years on, AI is more powerful than it was in 2023 by a lot."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "But also, maybe a lot of this is just hype?"
  - **Gen (4x)** `8.txt`: "The franchisee saves on staff because now reheating some prepackaged bag takes a lot fewer hands than cooking."
  - **Gen (4x)** `3.txt`: "So, a lot of these big guys were affected by the crash, but what they also used after is to take over the markets that were still recovering."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "I've been thinking about this one a lot."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Well, a lot goes into making that happen."
  - **After (1x)** `09-microchip-war.txt`: "I mean it is different in a lot of ways, blah, blah, blah, we get it."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L43. a bunch
- **Definition:** Casual quantity "a bunch of".
- **Measure (per 1k words):** blended **0.35**. Adam 0.33, Gen 0.37, Especially 0.00, Oil 1.04, After 0.31
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "A bunch of agents start poking around one of the few tools they have access to, the shared central library."
  - **Adam (7x)** `01-ai-disaster.txt`: "It's at Musk's 2015 birthday party and he's getting into an argument with a bunch of people standing and watching with Larry Page, his friend, soon to be ex-friend and CEO of Google."
  - **Gen (4x)** `10.txt`: "They have a bunch of different investments."
  - **Gen (4x)** `2.txt`: "And anyways, a bunch of wealthy people recently gave me a lot of money."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Next up is a bunch of other stuff that we don't need to get into, plastics, asphalt, chemicals, couple other fuel types, all come from oil."
  - **After (1x)** `09-microchip-war.txt`: "This is just a bunch of rules that says no more chips to China."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L44. right? tag
- **Definition:** Tag question "right?".
- **Measure (per 1k words):** blended **0.37**. Adam 0.12, Gen 0.73, Especially 0.06, Oil 0.17, After 0.23
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "If you wanted to just make money, that would not be a good way to do that, right?"
  - **Adam (7x)** `05-sam-altman.txt`: "They could have just started over and started a for-profit company, right?"
  - **Gen (4x)** `6.txt`: "And it's not just SpaceX, right?"
  - **Gen (4x)** `2.txt`: "But more importantly, he or she is going to damn well make sure to not tell you, the audience, that he or she was owned by me all along because we both know how that will go, right?"
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "You get bubbles, inflation, and you can look around right now and be like, that's today, right?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And that is way cheaper than you would think, right?"
  - **After (1x)** `09-microchip-war.txt`: "Economic interdependence is a recipe for peace and mutual prosperity, right?"
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L45. obviously
- **Definition:** Shared-knowledge marker.
- **Measure (per 1k words):** blended **0.21**. Adam 0.10, Gen 0.34, Especially 0.06, Oil 0.35, After 0.12
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "It obviously has as much coding skill as the best hackers in the world, but it usually doesn't hack."
  - **Adam (7x)** `01-ai-disaster.txt`: "These are AI systems doing very obviously unwanted things in extremely glaring ways that we can see with our own eyes."
  - **Gen (4x)** `2.txt`: "So, obviously, his financial interest is also aligned with the firm's eventual exit."
  - **Gen (4x)** `6.txt`: "Whether you do or not is obviously your choice, but if you take anything away from this video, is that look, everything points to the fact that this is more important than ever."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Money is left to chase fewer clearly obviously useful things."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Jet fuel is also pretty light, goes in airplanes, obviously, and it's actually just a version of kerosene, the thing you put in lanterns, and the world uses eight million barrels a day of it."
  - **After (1x)** `03-recycling.txt`: "I mean, recycling obviously exists, right?"
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L46. apparently
- **Definition:** Reported-hearsay marker.
- **Measure (per 1k words):** blended **0.04**. Adam 0.12, Gen 0.00, Especially 0.00, Oil 0.00, After 0.02
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "He's a political operative whose personal motto is apparently "Everyone has a plan until you punch them in the mouth."
  - **Adam (7x)** `02-bestselling-book.txt`: "The CEO is standing by and apparently already teased something big on social media."
  - **After (1x)** `12-data-centres-not-working.txt`: "He promised to purchase 40% of global DRAM output from two manufacturers simultaneously, apparently without either one knowing about each other."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L47. exactly
- **Definition:** Emphasis/precision "exactly".
- **Measure (per 1k words):** blended **1.04**. Adam 0.36, Gen 2.00, Especially 1.12, Oil 0.00, After 0.25
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "Now, we don't know exactly how the Grok chatbot on X works under the hood, but we do know that its claim to fame since the beginning has been its access to live information on X."
  - **Adam (7x)** `04-superintelligence.txt`: "The first important piece of context is that we don't, you know, exactly specify what we want our AI to do."
  - **Gen (4x)** `5.txt`: "And so, Stanley Martin did exactly what a rational person would do."
  - **Gen (4x)** `8.txt`: "And yeah, some of these names are going to surprise you, but the bigger surprise will be what exactly it's doing to the restaurants that you used to love."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "The best response is, I don't know exactly—something cool."
  - **After (1x)** `03-recycling.txt`: "That looks exactly like the recycling symbol."
- **Do:** Keep at corpus rate; fillers are what make it sound spoken.
- **Don't:** Do not strip all of them (reads as essay) or stack 3 in one sentence.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Connective logic

### L48. which means
- **Definition:** Consequence cascade.
- **Measure (per 1k words):** blended **0.29**. Adam 0.00, Gen 0.33, Especially 0.05, Oil 3.11, After 0.01
- **Verbatim evidence:**
  - **Gen (4x)** `9.txt`: "Which means the hedge fund's biggest bet in history against AI's biggest bet in humans history is also one of the reason the stock market might keep going back up."
  - **Gen (4x)** `6.txt`: "Which means the real question is which side of that sale are you going to be on?"
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "New buildings are being designed to run closed loop, which means they use the same water for ten years."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "It's all one unified global market, which means all the world's producers sell into the same big supply, which all the world's consumers buy from."
  - **After (1x)** `02-greed.txt`: "Which means if your salary hasn't been going up every year, you're effectively making less money."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L49. in other words
- **Definition:** Re-explaining in plain terms.
- **Measure (per 1k words):** blended **0.03**. Adam 0.03, Gen 0.00, Especially 0.05, Oil 0.00, After 0.13
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "In other words, you can train an AI until it does what you want, but you don't really control why or how it does those things."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "In other words, if I say $5 and you say $10 and we need your electricity to cover the amount we need to deliver to customers, your bid is accepted."
  - **After (1x)** `11-anthropic-ipo.txt`: "In other words, not because of how dangerous AI is in and of itself, but how it's used by the people building it."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L50. that means
- **Definition:** Consequence.
- **Measure (per 1k words):** blended **0.11**. Adam 0.17, Gen 0.00, Especially 0.05, Oil 0.86, After 0.07
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "I think it's time to tell you what that means."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "That means, if an agent's transcript shows they first got their flag by cheating, before they legitimately solved their ExploitGym task, they are doomed."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "I don't know what that means."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Ukraine has cut that industry in half, but that means that the world is now down by about one million barrels a day of diesel."
  - **After (1x)** `11-anthropic-ipo.txt`: "That's a classification that means they legally must balance shareholder interests with a positive impact."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L51. the thing is / here's the thing
- **Definition:** Pivot to the real point.
- **Measure (per 1k words):** blended **0.10**. Adam 0.10, Gen 0.15, Especially 0.00, Oil 0.00, After 0.04
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "Most people want money because it's useful for getting more of whatever the thing is that they actually want."
  - **Gen (4x)** `8.txt`: "Well, the thing is, it's not just places like Subway or RV now."
  - **Gen (4x)** `2.txt`: "The thing is, every deal that I've showed you so far are only the ones that we know about."
  - **After (1x)** `03-recycling.txt`: "Wouldn't you just assume that this means that the thing is recyclable and you put it in the bin and you think recycling is working?"
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L52. turns out
- **Definition:** Reveal marker.
- **Measure (per 1k words):** blended **0.24**. Adam 0.28, Gen 0.31, Especially 0.06, Oil 0.00, After 0.16
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "Turns out that OpenAI was not the first time Sam Altman had faced this kind of challenge."
  - **Adam (7x)** `02-bestselling-book.txt`: "It wasn't that it turns out an H-bomb couldn't really level a city."
  - **Gen (4x)** `3.txt`: "It turns out, I clicked on a phishing email, and that completely changed how I think about email today."
  - **Gen (4x)** `4.txt`: "It turns out every other CEO is asking the same thing."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "It turns out a lack of air space being a true vacuum, and it's much lower gravity actually make it easier to make solar panels on the moon than here on Earth."
  - **After (1x)** `02-greed.txt`: "Turns out that actually every single thing in the world becoming a forprofit commodity from housing to healthcare is just a way to enrich a few people at the cost of many."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L53. the problem is
- **Definition:** Complication marker.
- **Measure (per 1k words):** blended **0.07**. Adam 0.03, Gen 0.09, Especially 0.00, Oil 0.00, After 0.19
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "OpenBrain implements some quick fixes that make the warning signs go away, but the problem was real, and the fixes don't work."
  - **Gen (4x)** `4.txt`: "But the problem was figuring out how I was going to implement it in my own company."
  - **Gen (4x)** `2.txt`: "But the problem is big returns only exist in places that nobody else has risk going to before."
  - **After (1x)** `03-recycling.txt`: "The problem is how much plastic is made."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L54. because (mid)
- **Definition:** Causal glue.
- **Measure (per 1k words):** blended **4.38**. Adam 1.70, Gen 7.90, Especially 2.15, Oil 2.59, After 2.86
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "This is only going to be possible if there is a complete collapse of people's democratic ability to influence the direction of things, because the public is simply not willing to accept either of the branches of this scenario."
  - **Adam (7x)** `02-bestselling-book.txt`: "When you switch from the sort of AI that's not killing us all because it can't, to the sort of AI that's not killing us all, but it could."
  - **Gen (4x)** `9.txt`: "Because if you're in that position, you start getting really creative about where that number comes from."
  - **Gen (4x)** `3.txt`: "Okay, maybe I'm just missing something because politicians don't shut up about this housing crisis."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "Because generative AI is all about small inputs and large outputs."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But if I had to guess, it's because they know something a lot bigger and a lot worse than a crude oil shortage, like we said at the top of this video, is already starting to hit the world."
  - **After (1x)** `02-greed.txt`: "But for media outlets and politicians, that anger is their single most powerful tool because they can tell you where to direct it."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L55. so (mid-sentence)
- **Definition:** Mid-sentence so.
- **Measure (per 1k words):** blended **3.15**. Adam 2.17, Gen 4.22, Especially 2.49, Oil 4.49, After 2.42
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "Agent-4 now knows it's on notice, so it proceeds more cautiously, but it still manages to design Agent-5 with a single goal: making the world safe for Agent-4 and Agent-5."
  - **Adam (7x)** `02-bestselling-book.txt`: "And so it makes plans to continue existing."
  - **Gen (4x)** `10.txt`: "And so even if that small portion all does go bankrupt, most of the investments are are probably fine."
  - **Gen (4x)** `3.txt`: "I've seen published estimates range from 0 to 40 million, but what I found with the big housing sites is putting it more so around 4 to 5 million."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "But now, with the ability to put thousands of satellites up at a time, low Earth orbit is not far from being able to offer a lot of what's so nice a geostationary enough satellites."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But it is so much worse than that, because there is now a refinery shock hitting too."
  - **After (1x)** `02-greed.txt`: "And so there are huge disparities here."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L56. but (any)
- **Definition:** Contrast density.
- **Measure (per 1k words):** blended **8.61**. Adam 5.78, Gen 11.87, Especially 7.13, Oil 6.74, After 7.86
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "What is an example of a decision that you've had to make that is best for the world, but not best for winning?"
  - **Adam (7x)** `05-sam-altman.txt`: "But, if it starts racing somewhere dangerous, the people upstairs can pull the plug."
  - **Gen (4x)** `10.txt`: "Say what you want, but private equity is so damn good at making money, and that's a pretty damn good return on investment."
  - **Gen (4x)** `1.txt`: "But take the speculation out of it, and just frankly, this decision can have some consequences because it's also holding up the stock market."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Data centers do not pass the kitchen table test either—yet, anyway—but for a reason most people haven't really considered or don't want to put into words."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And that's fine if it's going to Europe, but look, there is suddenly no direct route to Asia, and Asia is by far the world's largest consumer of oil."
  - **After (1x)** `08-tokens.txt`: "Companies tied token consumption to productivity and output, but all that happened was way higher costs."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L57. and then
- **Definition:** Narrative sequencing.
- **Measure (per 1k words):** blended **0.93**. Adam 1.65, Gen 0.32, Especially 0.94, Oil 1.56, After 0.61
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "And then it goes kind of viral."
  - **Adam (7x)** `01-ai-disaster.txt`: "You can, instead of writing your response in normal English, put it in some weird format and then suddenly the model can't recognize it, even though it's been trained to."
  - **Gen (4x)** `8.txt`: "Because if the plan all along is to hold something for five to seven years and then sell the land out from it under it anyways."
  - **Gen (4x)** `2.txt`: "By showing that nothing has changed and then announcing it, there's not much things that an audience could say."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Water goes in one time, and then it just recirculates, or a new type of air design system, or no water at all, because a million-gallon headline in a dry county is going to cost more than cooling savings."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And then Saudi Arabia cranks up the mother of all oil pipelines, the East-West pipeline."
  - **After (1x)** `03-recycling.txt`: "And then one guy raises his hand and he's like, "Wait, I thought oil was basically like black gold and every country on Earth is fighting for it literally all the time."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L58. even though
- **Definition:** Concession.
- **Measure (per 1k words):** blended **0.18**. Adam 0.07, Gen 0.33, Especially 0.11, Oil 0.00, After 0.09
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "You can, instead of writing your response in normal English, put it in some weird format and then suddenly the model can't recognize it, even though it's been trained to."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Even though over 90% of the agents active on the board at the time joined in, there wasn't all that clear a reason to."
  - **Gen (4x)** `1.txt`: "It's why even though AI piracy was supposed to make software free and give it back to you, instead, again, the companies just found a new way to charge you."
  - **Gen (4x)** `2.txt`: "And even though raw subscriber count continued to grow 8 million by 2024, what didn't, and sounds a little bit corny, was that magic that made them great."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "The next one will arrive at that will tip the scales of power in favor of whoever pulls it off, even though it will take three days to arrive."
  - **After (1x)** `08-tokens.txt`: "Even though this is framed as “consolidation”, most see it as cost cutting."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L59. not just X but
- **Definition:** Escalation frame.
- **Measure (per 1k words):** blended **0.53**. Adam 0.41, Gen 0.58, Especially 0.64, Oil 0.00, After 0.82
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "But it's not just adults in the room."
  - **Adam (7x)** `04-superintelligence.txt`: "What is so exciting and terrifying about reading this document is that it's not just a research report."
  - **Gen (4x)** `8.txt`: "Well, the thing is, it's not just places like Subway or RV now."
  - **Gen (4x)** `4.txt`: "But no, not just do it, but do it for less than what you cost."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "If you're serious about learning back-end development, Python SQL Go, this is how you build that capability, not just simulate it."
  - **After (1x)** `06-diamonds.txt`: "This structure is what makes diamond not just the hardest natural material we know about, but four times harder than the next hardest material."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L60. instead
- **Definition:** Contrast.
- **Measure (per 1k words):** blended **0.57**. Adam 0.40, Gen 0.77, Especially 0.42, Oil 0.52, After 0.48
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "You start, instead of with a human-coded program, with an artificial neural network."
  - **Adam (7x)** `04-superintelligence.txt`: "Do you keep using it and push ahead, possibly making billions or trillions of dollars for your shareholders, possibly keeping America's lead over China, or do you slow down, reassess the dangers, and risk China taking the lead instead?"
  - **Gen (4x)** `8.txt`: "What I want instead is access to 8% of his gross revenue."
  - **Gen (4x)** `6.txt`: "And the only one that broke the pattern was the 2022 crash which took about two years, but it was also an outlier case because inflation hit a 40-year high and the Fed was busy raising rates instead."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Instead, a few giant refineries made gasoline for the whole region."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Right now, the really big oil tankers that normally would've gone through Hormuz are instead anchoring out here, where it's safe, and where they load oil using those ship-to-ship transfers that little itty bitty ships bring to them through Hormuz."
  - **After (1x)** `06-diamonds.txt`: "Instead of growing one single crystal, they grow millions of tiny diamond crystallites that bond together."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L61. meanwhile
- **Definition:** Parallel thread.
- **Measure (per 1k words):** blended **0.07**. Adam 0.13, Gen 0.00, Especially 0.00, Oil 0.00, After 0.22
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "Meanwhile, China is just two months behind."
  - **Adam (7x)** `01-ai-disaster.txt`: "Meanwhile, there's this whole other thread happening as users start to discover that they can get Grok to say even unbelievably violent and sexually explicit posts."
  - **After (1x)** `11-anthropic-ipo.txt`: "And meanwhile, all of the labs are becoming more entrenched in the federal government."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L62. at the same time
- **Definition:** Parallel thread.
- **Measure (per 1k words):** blended **0.09**. Adam 0.06, Gen 0.02, Especially 0.42, Oil 0.17, After 0.08
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "Musk pops up in a few other places on X at the same time."
  - **Adam (7x)** `04-superintelligence.txt`: "At the same time, OpenBrain is building massive data centers to train the next generation of AI agents, and they're preparing to trade agent one with 1000 times the compute of GPT-4."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Each one is slow and dumb, not even close to a chef, but all 17,000 of them are working on the same frame at the same time."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "It's that both 10% of supply, poof, disappeared overnight, and prices basically tripling at the same time."
  - **After (1x)** `10-water.txt`: "At the same time, he sold the rights to an undisclosed amount of water to Oracle's Project Jupiter, from his own New Mexican sod farm."
- **Do:** Chain with spoken connectors.
- **Don't:** Avoid essay connectors (Moreover, Furthermore, Thus, Hence, Consequently).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Address and persona

### L63. you/your
- **Definition:** Second-person density.
- **Measure (per 1k words):** blended **17.25**. Adam 11.88, Gen 20.76, Especially 20.21, Oil 16.25, After 19.45
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "We don't sell your data or anything like that."
  - **Adam (7x)** `05-sam-altman.txt`: "But, there is a real sense in which we are creating something very different from anything you've created so far."
  - **Gen (4x)** `10.txt`: "And soon enough, your savings, your job, and your future may end up like Joan fa."
  - **Gen (4x)** `9.txt`: "But when you do bet against something eventually you do have to close that bet."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Local, in-network, real openings, booked without turning your afternoon into hold music."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "If you watched our other videos, you know how the Iran war blew all this up."
  - **After (1x)** `03-recycling.txt`: "Although, you may confuse it to be the same thing, because they couldn't afford fruit."
- **Do:** Talk to one viewer.
- **Don't:** No "dear viewers", no "in this video we will explore".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L64. I/me/my
- **Definition:** Narrator first person.
- **Measure (per 1k words):** blended **12.99**. Adam 7.88, Gen 20.02, Especially 7.54, Oil 9.51, After 10.00
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "As I researched this video, that is by far the most tragic, kind of most paradoxical thing that's come up."
  - **Adam (7x)** `02-bestselling-book.txt`: "When I look at how society is handling this problem so far, how we've handled problems in the past, I feel really genuinely worried."
  - **Gen (4x)** `2.txt`: "But what I can tell you is that when those conversations happen, the first thing that gets discussed is the sort and list of topics that you're not allowed to touch anymore."
  - **Gen (4x)** `9.txt`: "What I'm getting at here is that what moves this thing isn't another earnings report that has to be audited and verified, but rather something people can sometimes just make up."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Wait for a callback that lands while I can't answer."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And if you didn't, I'm gonna try to TLDR you up to today in personal challenge here, 60 seconds."
  - **After (1x)** `02-greed.txt`: "Hi, I'm Upside Down and I'm here to tell you about today's sponsor, NordVPN."
- **Do:** Talk to one viewer.
- **Don't:** No "dear viewers", no "in this video we will explore".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L65. we/us/our
- **Definition:** Inclusive or team "we".
- **Measure (per 1k words):** blended **8.90**. Adam 11.84, Gen 5.34, Especially 8.71, Oil 9.51, After 12.09
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "You take something that works in one environment, you put it in a slightly new one, it sort of messes up some, and you're like, "Ah, well, we'll fix it up."
  - **Adam (7x)** `05-sam-altman.txt`: "Someday, we will make something that qualifies as an AGI by whatever fuzzy definition you want."
  - **Gen (4x)** `6.txt`: "The four patterns can tell you when we're close, but it can't tell you when, which then leads me to the most important question for those watching that's still hoping that this crash happens."
  - **Gen (4x)** `2.txt`: "But more importantly, he or she is going to damn well make sure to not tell you, the audience, that he or she was owned by me all along because we both know how that will go, right?"
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Gently pushing us 230,000 miles from Earth."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And there's one last thing here that we haven't talked about."
  - **After (1x)** `03-recycling.txt`: "No, we're never going to do that."
- **Do:** Talk to one viewer.
- **Don't:** No "dear viewers", no "in this video we will explore".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L66. imagine
- **Definition:** Viewer simulation.
- **Measure (per 1k words):** blended **0.26**. Adam 0.20, Gen 0.35, Especially 0.45, Oil 0.00, After 0.12
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "And in all of this, they imagine that Sable might not necessarily mean to deliberately kill off the last of the humans."
  - **Gen (4x)** `1.txt`: "And I have to imagine that they were doing this to save money, but now that money is just moving to AI instead."
  - **Gen (4x)** `3.txt`: "Because imagine a town where 2/3 of the people own gold bars and somebody puts in a vote whether to cut the price of gold in half."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "Each thought, which you can imagine as a long sentence, is a pathway through this tree."
  - **After (1x)** `09-microchip-war.txt`: "Imagine those supply chain issues, but like on steroids, totally debilitating and being used for a hostile purpose to strike back at the US."
- **Do:** Talk to one viewer.
- **Don't:** No "dear viewers", no "in this video we will explore".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L67. let's / let me
- **Definition:** Guiding the viewer.
- **Measure (per 1k words):** blended **0.78**. Adam 0.54, Gen 1.17, Especially 0.26, Oil 1.38, After 0.33
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Let's check on the prompt these agents would have gotten at the beginning of this ExploitGym evaluation."
  - **Adam (7x)** `05-sam-altman.txt`: "Let's make sure that Sam Altman is not the only person who decides our future."
  - **Gen (4x)** `1.txt`: "But to explain what I'm going with here, let's just say that I pour these two Cokes into separate cups."
  - **Gen (4x)** `6.txt`: "What if I told you that right now, stocks are priced even more expensive than they were right before, let's say a pretty bad crash."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Now let's get back to it."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And to show you what this is doing, let's look at crack spread, and no, you don't have to blur it."
  - **After (1x)** `09-microchip-war.txt`: "But let's go back to that visual of the whole supply chain."
- **Do:** Talk to one viewer.
- **Don't:** No "dear viewers", no "in this video we will explore".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L68. if you're wondering / you might
- **Definition:** Anticipating viewer thought.
- **Measure (per 1k words):** blended **0.81**. Adam 0.79, Gen 1.08, Especially 0.25, Oil 0.52, After 0.53
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "You probably know how that went."
  - **Adam (7x)** `01-ai-disaster.txt`: "If you're just a normal person watching this and getting concerned, who wants to contribute on helping society have a more sane response to the risk being posed by AI systems, that's great."
  - **Gen (4x)** `9.txt`: "Like if you're already up this much, why wouldn't you sell some of it?"
  - **Gen (4x)** `1.txt`: "But, as you probably seen in any grocery store, you don't actually need the recipe to copy it."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And if you're interested, you can book a free consultation, or just dive in with a 15-day free trial, no credit card required by using the link in the description or the QR code."
  - **After (1x)** `03-recycling.txt`: "Because if you're a fossil fuel company, you want methane, but if you're getting methane, you're also getting ethane."
- **Do:** Talk to one viewer.
- **Don't:** No "dear viewers", no "in this video we will explore".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L69. think about it
- **Definition:** Prompting reflection.
- **Measure (per 1k words):** blended **0.10**. Adam 0.06, Gen 0.17, Especially 0.12, Oil 0.00, After 0.06
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "It's actually sort of obvious when you think about it."
  - **Adam (7x)** `02-bestselling-book.txt`: "Once the AI has become so intelligent that it can overcome those new control techniques — that's one way to think about it."
  - **Gen (4x)** `4.txt`: "But if you really think about it, that money only exists for as long as people believe the story."
  - **Gen (4x)** `3.txt`: "Because if you really think about it, if we're really this short on houses, building them should be like the easiest money maker in America right now."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Makes perfect sense if you think about it from the point of view of the hierarchy of needs, there are five."
  - **After (1x)** `02-greed.txt`: "I mean, they could be worth infinity dollars when you think about it."
- **Do:** Talk to one viewer.
- **Don't:** No "dear viewers", no "in this video we will explore".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Register

### L70. contractions
- **Definition:** Contractions per 1k words.
- **Measure (per 1k words):** blended **29.61**. Adam 28.67, Gen 33.45, Especially 20.61, Oil 26.10, After 27.74
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "Guardrail number two, the nonprofit board can fire the for-profit's CEO."
  - **Adam (7x)** `02-bestselling-book.txt`: "They argue that that doesn't change if you come up with some nice techniques for controlling AI's behavior better."
  - **Gen (4x)** `9.txt`: "You too already should have a retirement fund like your 401k and it's buying the same stocks these pensions are."
  - **Gen (4x)** `3.txt`: "That's why I have signed an executive order banning large institutional addresses from buying single-family homes."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "If you back out and look at water usage by activities that aren't in a house— taking showers, doing dishes, drinking it, this is how it breaks down."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So everything I've shown you so far tracks how the oil shock over there, plus a shipping shock right here leads to crazy prices and shortages by the time it gets to the refinery."
  - **After (1x)** `09-microchip-war.txt`: "They put a 100% tax on Japanese chips coming into the US, which not surprisingly just crushes Japan's chip industry."
- **Do:** Stay conversational at corpus rates.
- **Don't:** Never use AI-tell vocabulary or essay connectors in narration.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L71. swearing
- **Definition:** Profanity.
- **Measure (per 1k words):** blended **0.51**. Adam 0.26, Gen 1.04, Especially 0.00, Oil 0.00, After 0.09
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "So where the hell did that stuff come from?"
  - **Adam (7x)** `01-ai-disaster.txt`: "How the hell did this happen?"
  - **Gen (4x)** `5.txt`: "So, point is, someone's going to be paying for it, and it sure as hell not going to be them."
  - **Gen (4x)** `4.txt`: "He's been here for 9 years, knows the ins and outs of my company, but, you know, he cost me too damn much."
  - **After (1x)** `09-microchip-war.txt`: "Too bad, so sad, Japan, said the President at the time who was, wait, what the hell, Ronald Reagan?"
- **Do:** Stay conversational at corpus rates.
- **Don't:** Never use AI-tell vocabulary or essay connectors in narration.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L72. slang (cooked/insane/crazy/wild/huge)
- **Definition:** Casual hyperbole.
- **Measure (per 1k words):** blended **0.85**. Adam 0.71, Gen 0.72, Especially 0.59, Oil 2.42, After 1.22
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "At the same time, OpenBrain is building massive data centers to train the next generation of AI agents, and they're preparing to trade agent one with 1000 times the compute of GPT-4."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "You might remember, one of the first projects in this whole massive cheating research operation was searching online for any information about ExploitGym that might be remotely useful."
  - **Gen (4x)** `3.txt`: "But where I'm going with all this is that losing value slowly is also only half of it because all this talk about owning a home, but the actual cost of owning the home has gone insane."
  - **Gen (4x)** `4.txt`: "But hold up, you know what's crazy that I'm realizing about all this?"
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "The rocket is huge because it needs to carry enough fuel."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "It's a huge part of their economy."
  - **After (1x)** `05-middle-class.txt`: "So tech households were making about 50% more but nothing too crazy."
- **Do:** Stay conversational at corpus rates.
- **Don't:** Never use AI-tell vocabulary or essay connectors in narration.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L73. gonna/wanna/gotta
- **Definition:** Phonetic contractions.
- **Measure (per 1k words):** blended **0.39**. Adam 0.34, Gen 0.00, Especially 0.00, Oil 4.49, After 0.43
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "Helen Toner, a former OpenAI board member, puts this in a way that I think just cuts through the noise, and I like it so much I'm just gonna read it to you verbatim."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "I wanna tell you the extraordinary story of the past few months."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But actually, before we get into what happened, there's something I wanna show you."
  - **After (1x)** `09-microchip-war.txt`: "This is a big thing that's happening in geopolitics right now and I wanna help you understand the stakes of this new conflict between the US and China."
- **Do:** Stay conversational at corpus rates.
- **Don't:** Never use AI-tell vocabulary or essay connectors in narration.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L74. guy/guys/dude
- **Definition:** Casual people words.
- **Measure (per 1k words):** blended **0.74**. Adam 0.38, Gen 1.10, Especially 0.30, Oil 1.38, After 0.66
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "In the same leaked emails, Elon says, "Guys, I've had enough."
  - **Adam (7x)** `05-sam-altman.txt`: "Nobody seems to understand why this guy was fired."
  - **Gen (4x)** `3.txt`: "So, a lot of these big guys were affected by the crash, but what they also used after is to take over the markets that were still recovering."
  - **Gen (4x)** `4.txt`: "So, come with me, you guys, to replace my employee with AI."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Let's not make this complicated, folks."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But even that is nothing compared to what happened when these guys showed up, and closed down the Bab al-Mandab Strait."
  - **After (1x)** `05-middle-class.txt`: "I can imagine the old folks back in the day telling their unemployed CS children that they told them so."
- **Do:** Stay conversational at corpus rates.
- **Don't:** Never use AI-tell vocabulary or essay connectors in narration.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L75. stuff/thing(s)
- **Definition:** Vague nouns.
- **Measure (per 1k words):** blended **3.44**. Adam 3.28, Gen 3.50, Especially 4.31, Oil 4.84, After 2.45
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "The way I see it, there's basically three things you need."
  - **Adam (7x)** `01-ai-disaster.txt`: "A couple important things to notice about how all this played out."
  - **Gen (4x)** `9.txt`: "Where now the only thing that matters more than ever is how fast you can get to that information."
  - **Gen (4x)** `2.txt`: "They would take care of things like hiring, production, logistics."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Eight cores, maybe 16, very fast, very good at doing one thing after another."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "I wanna conclude all of this with a summary of just a few of the many, many things in our world that are getting hit really hard by the diesel apocalypse."
  - **After (1x)** `03-recycling.txt`: "So, people started throwing stuff away."
- **Do:** Stay conversational at corpus rates.
- **Don't:** Never use AI-tell vocabulary or essay connectors in narration.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L76. AI-tell vocabulary
- **Definition:** Words that flag machine text.
- **Measure (per 1k words):** blended **0.22**. Adam 0.49, Gen 0.02, Especially 0.00, Oil 0.17, After 0.26
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "Then, and this part's crucial, you come up with a standardized test, a way of measuring the outputs on some sort of objective numerical score."
  - **Adam (7x)** `04-superintelligence.txt`: "We can still demand information about what is going on with this technology, but we won't always have the power and the leverage needed to do that."
  - **Gen (4x)** `2.txt`: "But the biggest unlock is what this now means for me and my investors."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Like, let's say, you're Australia, and you have a rich, vibrant economy that exports iron ore and fairy bread to a grateful world, but what you don't have is oil or a big refinery industry."
  - **After (1x)** `02-greed.txt`: "You might have also heard that a VPN allows you to unlock websites and content that may be restricted in your area."
- **Do:** Stay conversational at corpus rates.
- **Don't:** Never use AI-tell vocabulary or essay connectors in narration.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L77. essay connectors
- **Definition:** Formal transitions.
- **Measure (per 1k words):** blended **0.04**. Adam 0.03, Gen 0.03, Especially 0.00, Oil 0.00, After 0.14
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "Most notably, there's Anthropic, OpenAI, and Google DeepMind, all in the English speaking world, though China and DeepSeek recently turned heads in January with a surprisingly advanced and efficient model."
  - **After (1x)** `06-diamonds.txt`: ""And what our work showed is that if I wrap it around like a blanket, you can make those transistors run cooler, hence way more efficient than otherwise it would be."
- **Do:** Stay conversational at corpus rates.
- **Don't:** Never use AI-tell vocabulary or essay connectors in narration.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Specificity

### L78. numerals
- **Definition:** Digits per 1k.
- **Measure (per 1k words):** blended **11.90**. Adam 10.69, Gen 14.01, Especially 8.16, Oil 10.20, After 11.89
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "In February of 2023, I and a few dozen other journalists got access to this early testing version of what was essentially an early version of GPT-4 inside of Bing."
  - **Adam (7x)** `05-sam-altman.txt`: "It hits 100 million users in 2 months."
  - **Gen (4x)** `9.txt`: "And that's exactly what Meta did in 2025."
  - **Gen (4x)** `4.txt`: "It sold all its shoes and its brand for $39 million and renamed itself Newbird AI to now start renting out computer chips."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Gently pushing us 230,000 miles from Earth."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "That means that shipping alone now adds another $23 to the price of each barrel of oil."
  - **After (1x)** `12-data-centres-not-working.txt`: "If there's much cheaper or free models that are 80% as good, company spending $1 trillion to train frontier models seems ridiculous in comparison."
- **Do:** Anchor claims in exact numbers.
- **Don't:** No "a significant amount", "numerous", "various".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L79. money
- **Definition:** Money amounts.
- **Measure (per 1k words):** blended **2.41**. Adam 0.66, Gen 3.88, Especially 0.97, Oil 5.88, After 2.27
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "They'll let their AI work for 16 hours straight, uninterrupted, at a cost of something like $10 million."
  - **Adam (7x)** `05-sam-altman.txt`: "It hits 100 million users in 2 months."
  - **Gen (4x)** `1.txt`: "If you're someone that pays for every one of these yourself, that's over $3,000 a year."
  - **Gen (4x)** `3.txt`: "So, back to my checklist of workers, it makes sense why there's a huge shortage because the industry lost around 1.5 million workers in the crash and only won back around 940,000 of them by 2019."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "A farmer might make $1,200 per acre farming corn."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "That means that shipping alone now adds another $23 to the price of each barrel of oil."
  - **After (1x)** `12-data-centres-not-working.txt`: "Its market cap collapsed from nearly $20 to $3.4 billion."
- **Do:** Anchor claims in exact numbers.
- **Don't:** No "a significant amount", "numerous", "various".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L80. percent
- **Definition:** Percentages.
- **Measure (per 1k words):** blended **1.64**. Adam 0.65, Gen 2.45, Especially 1.15, Oil 1.56, After 2.22
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "The chance of 99.99% that if we build this technology we will all die — that claim in particular is the one I don't agree with."
  - **Adam (7x)** `01-ai-disaster.txt`: "As recently as this year, he's been on podcasts talking about a 20% chance of AI leading to human extinction."
  - **Gen (4x)** `6.txt`: "Where the average company going public back then was jumping 71% on its first day, even though three out of four of them were losing money."
  - **Gen (4x)** `8.txt`: "You're telling me that food gets 28 to 32% of everything it takes in?"
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Start earning 4.05% variable API today by heading to wealthfront.com/max Nomics."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But saying 10% drop does not come close to conveying how badly the global diesel supply is stressed and strained to the breaking point."
  - **After (1x)** `08-tokens.txt`: "You can probably see where this is going… At Uber, engineers were given access to Claude Code and Cursor, and by March 2026, 84% of Uber's developers were classified as agentic coding users."
- **Do:** Anchor claims in exact numbers.
- **Don't:** No "a significant amount", "numerous", "various".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L81. years
- **Definition:** Explicit years.
- **Measure (per 1k words):** blended **2.53**. Adam 2.33, Gen 3.46, Especially 1.20, Oil 0.17, After 2.00
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "In February of 2023, I and a few dozen other journalists got access to this early testing version of what was essentially an early version of GPT-4 inside of Bing."
  - **Adam (7x)** `04-superintelligence.txt`: "A hundred million users on ChatGPT in two months And this is the total compute used to train GPT-4 in 2023."
  - **Gen (4x)** `10.txt`: "In fact, they're reusing the same exact playbook from 2008."
  - **Gen (4x)** `6.txt`: "So, starting with the first one, the new story, which to quickly recap in 1929 was radio, and in 1999 was the internet, and today is obviously AI."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Finally, in 2021, the state said no more."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "February 2026, Benjamin Netanyahu convinces Donald Trump to do regime change war on Iran."
  - **After (1x)** `12-data-centres-not-working.txt`: "According to intelligence from the platform Heatmap Pro, at least 25 projects were canceled that year due to community backlash, up from just six in 2024."
- **Do:** Anchor claims in exact numbers.
- **Don't:** No "a significant amount", "numerous", "various".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L82. big-unit words
- **Definition:** Scale words.
- **Measure (per 1k words):** blended **2.20**. Adam 0.81, Gen 3.26, Especially 0.82, Oil 6.74, After 1.84
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "Sable, the AI in our story, is made up of four trillion."
  - **Adam (7x)** `05-sam-altman.txt`: "It turned out that the OpenAI Startup Fund, $175 million of venture capital deployed in OpenAI's name, was personally owned by Sam Altman."
  - **Gen (4x)** `10.txt`: "So to break it down, if a company was paying $10 million a year in interest, now it's paying 30 million."
  - **Gen (4x)** `9.txt`: "And it was because they reported $53.4 billion gain on their stake in this little AI company called Anthropic."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Last year was about $400 billion."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And then those countries attacked at least one big refinery in Iran, back and forth on and on, you get the idea, one and a half million barrels a day of diesel, poof, gone from global production."
  - **After (1x)** `10-water.txt`: "That's enough to fill two million Olympic-size pools."
- **Do:** Anchor claims in exact numbers.
- **Don't:** No "a significant amount", "numerous", "various".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L83. named months/days
- **Definition:** Dated precision.
- **Measure (per 1k words):** blended **1.76**. Adam 2.49, Gen 1.75, Especially 0.59, Oil 1.04, After 0.86
- **Verbatim evidence:**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "On August 26th, that report came out."
  - **Adam (7x)** `05-sam-altman.txt`: "On Saturday night, Sam sends out a single tweet."
  - **Gen (4x)** `8.txt`: "ROR bought a majority stake in June 2025 for about a billion dollars."
  - **Gen (4x)** `2.txt`: "Gen here may have been the one that built his channel from the ground up."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "You can already see their revenue march higher quarter after quarter, making it clear that this is where we're headed."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And this all got opened up even more around July when the world finally figured out how to get a little bit of oil out of Hormuz."
  - **After (1x)** `12-data-centres-not-working.txt`: "If you've criticized AI or data centers, you may now be considered a domestic terrorist."
- **Do:** Anchor claims in exact numbers.
- **Don't:** No "a significant amount", "numerous", "various".
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Punctuation

### L84. em/en dashes
- **Definition:** Dashes.
- **Measure (per 1k words):** blended **0.59**. Adam 1.08, Gen 0.00, Especially 1.71, Oil 0.00, After 0.52
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "I believe Linda Yaccarino, as the CEO of X and a proven leader in high-pressure environments, possesses the resilience and fortitude to handle a big black d— with impressive skill and determination."
  - **Adam (7x)** `02-bestselling-book.txt`: "The book opens with how modern AI is created and — the spoilers there is that it's grown, it's not carefully crafted."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "And suddenly, all of these weird Electric States we just looked at—systems built differently, regulated differently, priced differently— have been dropped into the same experiment."
  - **After (1x)** `10-water.txt`: "And again, I compare that – how many people work on a 100-acre pecan farm?"
- **Do:** Commas and periods carry the rhythm.
- **Don't:** Avoid semicolons and em-dash chains (AI tells in spoken scripts).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L85. semicolons
- **Definition:** Semicolons.
- **Measure (per 1k words):** blended **0.02**. Adam 0.00, Gen 0.00, Especially 0.18, Oil 0.00, After 0.04
- **Verbatim evidence:**
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "And if they're right, the question isn't just who uses the AI; it's where the AI gets made."
  - **After (1x)** `08-tokens.txt`: "DeepSeek’s V4-Pro model will cost $3.48 for 1 million tokens of output; by comparison, OpenAI and Anthropic charge $30 and $25 respectively for the same amount of work."
- **Do:** Commas and periods carry the rhythm.
- **Don't:** Avoid semicolons and em-dash chains (AI tells in spoken scripts).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L86. colons
- **Definition:** Colons.
- **Measure (per 1k words):** blended **0.45**. Adam 0.65, Gen 0.00, Especially 1.25, Oil 0.00, After 0.98
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "Around 1:00 a.m., a letter starts to circulate on various signal chats."
  - **Adam (7x)** `04-superintelligence.txt`: "Takeaway number two: By default, we should not expect to be ready when AGI arrives."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Click the TV on: 100 watts."
  - **After (1x)** `08-tokens.txt`: "We still come back to the question: Why did cheaper tokens cause a spike in cost?"
- **Do:** Commas and periods carry the rhythm.
- **Don't:** Avoid semicolons and em-dash chains (AI tells in spoken scripts).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L87. quotes marks
- **Definition:** Quoted speech.
- **Measure (per 1k words):** blended **2.11**. Adam 2.53, Gen 0.52, Especially 0.00, Oil 5.01, After 6.58
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "What I mean by "aligned" is that it actually is genuinely trying to do the things that we ask it."
  - **Adam (7x)** `05-sam-altman.txt`: "Greg Brockman posts a selfie with the caption, "We are so back."
  - **Gen (4x)** `5.txt`: "But maybe you're thinking, "Fine, just go build somewhere else."
  - **Gen (4x)** `10.txt`: "I wake up every single night thinking, "What could I have done differently?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "I have had to listen to so many serious energy analysts say "Crack spreads are widening" while trying to keep a straight face over the last month."
  - **After (1x)** `04-pov-ai.txt`: "You say, "Hey, did you end up filing that extension?"
- **Do:** Commas and periods carry the rhythm.
- **Don't:** Avoid semicolons and em-dash chains (AI tells in spoken scripts).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L88. ellipses
- **Definition:** Trailing off.
- **Measure (per 1k words):** blended **0.11**. Adam 0.12, Gen 0.00, Especially 0.00, Oil 0.35, After 0.46
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "My son is dead... killed by the woke mind virus."
  - **After (1x)** `06-diamonds.txt`: "But what if we could use an even more thermally conductive material like... "diamonds seems to be the right material."
- **Do:** Commas and periods carry the rhythm.
- **Don't:** Avoid semicolons and em-dash chains (AI tells in spoken scripts).
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Rhetorical moves

### L89. rhetorical question then answer
- **Definition:** Question sentences (often answered next line).
- **Measure (per 1k words):** blended **0.00**. Adam 0.00, Gen 0.00, Especially 0.00, Oil 0.00, After 0.00
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "What does your gut feeling say about whether, by say 2028, we'll see any of that happen in the real world?"
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Congress started asking questions, one of which was, any more of these rogue incidents y'all haven't told us about yet?"
  - **Gen (4x)** `5.txt`: "But how if most are getting canceled, then the land should be free, and the workers should be back?"
  - **Gen (4x)** `3.txt`: "This surge is causing many Americans to wonder, are we barreling toward a housing market crash?"
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "How many plants are going to retire?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Why did they call it that?"
  - **After (1x)** `08-tokens.txt`: "Have you noticed that many of these platforms have changed from subscriptions to token use pricing?"
- **Do:** Use as spoken devices, not decoration.
- **Don't:** Do not end every paragraph with a triplet or a "not X, but Y" flourish.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L90. "this is" pointing
- **Definition:** "This is X" pointing at footage or a person.
- **Measure (per 100 sentences):** blended **1.11**. Adam 1.35, Gen 0.33, Especially 1.05, Oil 4.80, After 1.24
- **Verbatim evidence:**
  - **Adam (7x)** `05-sam-altman.txt`: "This is where his star really starts to rise in Silicon Valley."
  - **Adam (7x)** `01-ai-disaster.txt`: "This is a made-up and intentionally Jewish sounding last name and these posts are designed to do exactly what they end up easily doing, going viral and stoking outrage."
  - **Gen (4x)** `4.txt`: "This is when it really stopped making sense and where I stopped taking notes."
  - **Gen (4x)** `6.txt`: "This is a free newsletter in the video description that we write every week."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "This is perhaps the ultimate example of a LULU."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "This is, I swear to you, a real training video for cargo ship captains explaining something called "ship-to-ship transfer."
  - **After (1x)** `06-diamonds.txt`: "This is the smallest species of ant."
- **Do:** Use as spoken devices, not decoration.
- **Don't:** Do not end every paragraph with a triplet or a "not X, but Y" flourish.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L91. "what" cleft / what no one
- **Definition:** "What no one is talking about".
- **Measure (per 1k words):** blended **0.03**. Adam 0.00, Gen 0.05, Especially 0.00, Oil 0.00, After 0.09
- **Verbatim evidence:**
  - **Gen (4x)** `1.txt`: "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?"
  - **Gen (4x)** `9.txt`: "But what nobody talks about is that now when 10 companies now make up 40% of that, you're again riding on the exact same handful of companies all making the same bet funded all the exact same ways."
  - **After (1x)** `06-diamonds.txt`: "So this is what people might be most familiar with if you know about lab grown diamonds."
- **Do:** Use as spoken devices, not decoration.
- **Don't:** Do not end every paragraph with a triplet or a "not X, but Y" flourish.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L92. "the reason"
- **Definition:** Explanation frame.
- **Measure (per 1k words):** blended **0.23**. Adam 0.06, Gen 0.42, Especially 0.09, Oil 0.35, After 0.13
- **Verbatim evidence:**
  - **Adam (7x)** `02-bestselling-book.txt`: "The last thing to say is just thank you so much for watching, for being the reason that we make these videos."
  - **Adam (7x)** `05-sam-altman.txt`: "The reason I wanted to create OpenAI was to serve as a counterweight to Google."
  - **Gen (4x)** `10.txt`: "The reason I'm actually making this video is because I saw a viral Tik Tok and they're hiding the bubble inside a private equity black box."
  - **Gen (4x)** `6.txt`: "And what changed between them is the reason it really does feel like America forgot how to have one."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "It is also the reason your washer, dryer, oven, and dishwasher are plugged into those big outlets connected to wires large enough to handle the extra electricity they need."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And the reason it's on fire is that Ukrainian drones blew it up."
  - **After (1x)** `03-recycling.txt`: "And the reason that we only have a few of these left, they got melted down to make implements of war."
- **Do:** Use as spoken devices, not decoration.
- **Don't:** Do not end every paragraph with a triplet or a "not X, but Y" flourish.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L93. "not because ... but because"
- **Definition:** Contrast of causes.
- **Measure (per 1k words):** blended **0.08**. Adam 0.09, Gen 0.09, Especially 0.06, Oil 0.00, After 0.07
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "It's not because I'm deeply concerned about chatbots saying bad words, though that's not harmless."
  - **Adam (7x)** `05-sam-altman.txt`: "Humans run this planet not because we are the strongest species, but because we're the smartest."
  - **Gen (4x)** `5.txt`: "Look, it's not because guys like me are lazy."
  - **Gen (4x)** `3.txt`: "It is not because 2/3 of the town is evil, but it's exactly what you would do too if you owned the gold bar."
  - **After (1x)** `03-recycling.txt`: "Not because it fixes any problem."
- **Do:** Use as spoken devices, not decoration.
- **Don't:** Do not end every paragraph with a triplet or a "not X, but Y" flourish.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L94. "here's" presenter
- **Definition:** "Here's X" presenter line.
- **Measure (per 100 sentences):** blended **0.28**. Adam 0.37, Gen 0.05, Especially 0.00, Oil 2.40, After 0.04
- **Verbatim evidence:**
  - **Adam (7x)** `01-ai-disaster.txt`: "Here's how that conversation played out."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Here's a map of what changed."
  - **After (1x)** `09-microchip-war.txt`: "Here's a very simplified version of the supply chain."
- **Do:** Use as spoken devices, not decoration.
- **Don't:** Do not end every paragraph with a triplet or a "not X, but Y" flourish.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L95. "the answer is"
- **Definition:** Answer frame.
- **Measure (per 1k words):** blended **0.03**. Adam 0.00, Gen 0.05, Especially 0.05, Oil 0.00, After 0.02
- **Verbatim evidence:**
  - **Gen (4x)** `1.txt`: "But what I quickly found was that the answer is no."
  - **Gen (4x)** `9.txt`: "And the answer is doesn't matter."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Because if the answer is you, if this company's decision to build here makes the number on your kitchen table go up, then suddenly the world's AI ambitions have become your electric bill."
  - **After (1x)** `12-data-centres-not-working.txt`: "Well, the answer is a few things all at once."
- **Do:** Use as spoken devices, not decoration.
- **Don't:** Do not end every paragraph with a triplet or a "not X, but Y" flourish.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).

### L96. rule of three lists
- **Definition:** Triplets (watch for AI over-use).
- **Measure (per 1k words):** blended **0.76**. Adam 0.62, Gen 0.63, Especially 0.78, Oil 1.73, After 1.16
- **Verbatim evidence:**
  - **Adam (7x)** `04-superintelligence.txt`: "Most notably, there's Anthropic, OpenAI, and Google DeepMind, all in the English speaking world, though China and DeepSeek recently turned heads in January with a surprisingly advanced and efficient model."
  - **Adam (7x)** `05-sam-altman.txt`: "At the 2022 retreat, Ilya and his colleagues are hanging around a campfire and he's got this wooden effigy in his hand that he commissioned from a local artist."
  - **Gen (4x)** `8.txt`: "And most often the choice that you make is you walk into whatever is closest, cheapest, and open."
  - **Gen (4x)** `10.txt`: "And it also helps that it's half the price of other premium brands, but even more ergonomic and a comfortable fit with all the tab functions like play, pause, and volume control."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "It makes the third and does the same check with the fourth, on and on."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And then those countries attacked at least one big refinery in Iran, back and forth on and on, you get the idea, one and a half million barrels a day of diesel, poof, gone from global production."
  - **After (1x)** `02-greed.txt`: "In 1943, Johnson and Johnson puts out this mission statement that's like, here's our list of priorities in order."
- **Do:** Use as spoken devices, not decoration.
- **Don't:** Do not end every paragraph with a triplet or a "not X, but Y" flourish.
- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).


## Exam-derived lessons
(Appended during the 100-exam run.)
- (fold 60) Real narration keeps fillers (just, actually, really, kind of, I mean). A passage with zero fillers over 60+ words is almost always the AI version. Keep about 1 per 2-3 sentences. [validated: +1.00 on 21 past type-A items]
- (fold 40) Humanizer step: break semicolon and ", and" merges back into separate sentences so short punches come back. [validated: +0.10 on 14 past type-C items]
- (fold 40) Spoken openers (And/But/So) begin about 28% of weighted sentences (Gen about 49%, Adam about 15%). A passage with none is suspicious. [validated: +1.00 on 8 past type-A items]
- (fold 30) Humanizer step: swap formal vocabulary back to plain words (utilize->use, obtain->get, significant->big, numerous->a lot of, individuals->people, approximately->about, purchase->buy). [validated: +0.62 on 10 past type-C items]
- (fold 20) Humanizer step: re-contract (it is -> it's, do not -> don't, I am -> I'm) everywhere. [validated: +0.45 on 6 past type-C items]
- (fold 20) Real lines are dense with contractions (it's, that's, don't). Expanded forms ("it is", "do not") are the single most reliable subtle AI tell. Re-contract everything except deliberate emphasis. [validated: +2.00 on 4 past type-A items]
- (fold 10) Humanizer step: map essay openers back to spoken ones. Therefore/As a result -> So, However -> But, Additionally/Moreover -> And, For example -> Like, Currently -> Now. [validated: +0.38 on 4 past type-C items]
- (fold 10) The word right after the opener decides it: "So what/now/if", "But what/here's/the", "And then/so/that's", "Because if/the". Check the following word. [validated: +2.00 on 5 past type-B items]
