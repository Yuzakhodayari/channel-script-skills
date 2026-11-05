# Method 1: Contrastive pairs (hook line vs mid line)

Each pair is a real gold answer next to the most confusable distractor, from TRAIN videos only. The cue column lists which rule features fire on each side. Read the pair, then name the difference before you look at the cue column.

**1.** (Gen)
- ✅ "[cheering] No more jacking up your power bill, no more draining your lakes, and best of all, no more data centers in …"  cues: you, superlative
- ❌ "Because once a data center circles a piece of land, Uncle Sam starts valuing your house like it's already been sold to …"  cues: starts_connector, you, mechanism

**2.** (Gen)
- ✅ "And to make it worthwhile, you can't even afford a home."  cues: starts_connector, you
- ❌ "And that's exactly what happened in New Brunswick, New Jersey."  cues: starts_connector, past

**3.** (Gen)
- ✅ "Honestly, my first thought, and probably yours, too, was who cares?"  cues: i_me, question, past, hedge_project, superlative, list_marker
- ❌ "And it's exactly why their AI products now bring in over $650 million a year."  cues: starts_connector, number, stakes

**4.** (Others)
- ✅ "You don't want to die because you come from a long line of beings that didn't want to die."  cues: you, stakes, mechanism
- ❌ "When the AI thought the scenario was real, it tried to blackmail a researcher to avoid being shut down 55% of the …"  cues: number, past

**5.** (Others)
- ✅ "And it may not look like much from down here, but just take a look from up above."  cues: starts_connector, in_medias_res, hedge_project, contrast
- ❌ "Documents show that Microsoft planned for each of these buildings to use 1 million gallons of water a day."  cues: number, past, mechanism

**6.** (Adam)
- ✅ "Combating perceived left-wing bias was a primary motivation for both his purchase of Twitter in 2022 and his founding of xAI in …"  cues: number, year_date, past
- ❌ "That and the whole demon Nazi chatbot thing."  cues: starts_anaphor

**7.** (Adam)
- ✅ "Your book is not called "If Anyone Builds It.""  cues: you, past
- ❌ "16 hours after the start of the Riemann run, Galvanic's researchers pore over the results."  cues: number, stakes, number_start

**8.** (Adam)
- ✅ "You can imagine a time when the whole world would say, "Okay, before we hit a recursive self-improvement phase, we really need …"  cues: you, we, past, stakes, hope
- ❌ "A few years ago, our most advanced AI systems, large language models, were like yeast."  cues: we, past, superlative

**9.** (Adam)
- ✅ "“If we didn't have the adversaries we'd have, I would be very in favor of pausing this technology completely, but we do.”"  cues: i_me, we, contrast
- ❌ "They publish those impressive benchmark results."  cues: starts_anaphor

**10.** (Adam)
- ✅ "California time on Monday, July 7th, 2025, less than 48 hours before the biggest product launch in xAI's short history."  cues: number, year_date, superlative
- ❌ "Like Grok, Tay was manipulated into Holocaust denial, racism, weird, creepy sexual posts."  cues: past

**11.** (Adam)
- ✅ "If someone builds it, does everyone die?"  cues: question, stakes
- ❌ "Most of its ideas are terrible, but it considers many and only one needs to work."  cues: contrast, superlative

**12.** (Others)
- ✅ "Tech is often seen in the exact opposite light as the great equalizer."  cues: —
- ❌ "As such, anyone and everyone could get funding to go try their luck at making it big in the tech world."  cues: hedge_project, stakes

**13.** (Gen)
- ✅ "That's just talking about their stock."  cues: starts_anaphor, in_medias_res
- ❌ "Where it's bill with Anthropic went from $10,000 a month to now millions in about 6 months."  cues: number, past

**14.** (Adam)
- ✅ "I mean, with artificial intelligence, we are summoning the demon..."  cues: i_me, we
- ❌ "When ChatGPT first came out, there was an explosion of people trying to find these."  cues: past, superlative, list_marker

**15.** (Adam)
- ✅ "Your book is not called "If Anyone Builds It.""  cues: you, past
- ❌ "This version of Sable is a bit like a species of ape that evolved in the savanna and now finds itself in …"  cues: starts_anaphor, past

## Part 2 –: Contrastive pairs (close window vs mid window)

Each pair is a real gold answer next to the most confusable distractor, from TRAIN videos only. The cue column lists which rule features fire on each side. Read the pair, then name the difference before you look at the cue column.

**1.** (Gen)
- ✅ "Texas alone is on track to give away $8 billion by 2030, and Virginia and Georgia each gave up over a billion …"  cues: we, number, year_date, past, future, hedge_project
- ❌ "In national polls, more Americans now say that they'd rather live next to a nuclear plant than a data center. But what's …"  cues: past, mechanism, contrast, superlative, list_marker

**2.** (Others)
- ✅ "It's the way of the future. The US has to keep up. First off, this ad was made by America's plastic makers."  cues: starts_anaphor, we, past, future, superlative, list_marker
- ❌ "This was the '50s. These people lived through the Great Depression, where they used dresser drawers as baby cribs, and they made …"  cues: starts_anaphor, question, number, in_medias_res, past, hedge_project

**3.** (Especially)
- ✅ "Three I mentioned the frontier event during this video, which is a real phenomenon. Event implies that something is built up and …"  cues: callback, i_me, past, meta_video
- ❌ "Terms and conditions apply. This is a paid endorsement of Wealthfront client experience as well. Very."  cues: —

**4.** (Adam)
- ✅ "Nate Soares has this metaphor that I keep thinking about. He says, "These companies are building a up as we go. We …"  cues: i_me, we
- ❌ "Priority number one is hardware. One really simple idea that ends up working out especially well is just renting GPUs. It's not …"  cues: in_medias_res, past, list_marker

**5.** (Gen)
- ✅ "We stopped trusting the banks after 2008. We stopped trusting the government a long time ago hopefully and you stopped trusting mainstream …"  cues: you, i_me, we, number, year_date, past
- ❌ "And all of it is becoming an ass on someone else's balance sheet. That's where today's sponsor, Proton Mail, comes in. It's …"  cues: starts_connector, you, in_medias_res, stakes, sponsor, profanity

**6.** (Gen)
- ✅ "Well, we'll see about that. But when reports are saying that the deal was somewhere near $100 million, we'll see how much …"  cues: we, number, past, contrast
- ❌ "So, we'll be looking at three main players and their portfolio, but why not start with the first and the biggest, Electrify …"  cues: starts_connector, you, we, number, past, stakes

**7.** (Gen)
- ✅ "So look, I'm trying here, but what it might make you feel the best is my pain. Because four years ago, when …"  cues: starts_connector, you, i_me, number, in_medias_res, past
- ❌ "That vote is going to lose every single time. It is not because 2/3 of the town is evil, but it's exactly …"  cues: starts_anaphor, you, number, past, future, mechanism

**8.** (Especially)
- ✅ "We'll take a closer look at that physical launch situation in that upcoming video. Number two, SpaceX doesn't really sell rockets anymore. …"  cues: we, meta_video, list_marker
- ❌ "Those glued to the screen watching the charts bounce all over the place. White knuckling arrived for everyone else that just wants …"  cues: starts_anaphor, you, in_medias_res, past, stakes

**9.** (Adam)
- ✅ "You need context on AI. You need skills relevant to the work. And you need a willingness to jump in."  cues: you, past
- ❌ "One really simple idea that ends up working out especially well is just renting GPUs. It's not hard or unprecedented for an …"  cues: in_medias_res, past

**10.** (Adam)
- ✅ "Well, we haven't put a sexbot avatar in ChatGPT yet. And the fact that this hyper-competitive market is just full of players …"  cues: you, we, in_medias_res, past, mechanism, contrast
- ❌ "At xAI, their stated intention for Grok has always been to make a maximally truth-seeking AI. But after the “don't question white …"  cues: we, past, contrast

**11.** (Adam)
- ✅ "And a 75% chance that things go really, really well. It's definitely non-zero and it's probably non-negligible. My view is it's just …"  cues: starts_connector, i_me, number, in_medias_res, hedge_project, hope
- ❌ "And so it makes plans to continue existing. It gets more money. It acquires more GPUs."  cues: starts_connector

**12.** (Adam)
- ✅ "So I think there's a 25% chance that things go really, really badly. And a 75% chance that things go really, really …"  cues: starts_connector, i_me, number, hedge_project, hope, reflective
- ❌ "Each time we do that, we'll be hoping that their weird internals continue to work the same way in those new environments, …"  cues: we, question, mechanism

**13.** (Especially)
- ✅ "Pressure has formed. I would argue that SpaceX never had a chance of developing into what it is today. A true industry …"  cues: i_me, in_medias_res, past, hope, superlative
- ❌ "Where could you stay? What happens if someone else gets there first? Shortly after the boosters burn out and right before the …"  cues: you, we, question, number, past, hedge_project

**14.** (Others)
- ✅ "And I've noticed that detail every single time. Like that WAS A QUESTION SHE was asking. And he just ignored it and …"  cues: starts_connector, i_me, in_medias_res, past, superlative
- ❌ "It's light, it's cheap and we have more than enough to sell. If we can just convince them to throw away the …"  cues: starts_anaphor, you, i_me, we, in_medias_res, future

**15.** (Adam)
- ✅ "The organization that I work for, 80,000 Hours, has an entire website dedicated to helping you make a difference on these things. …"  cues: you, i_me, we, number, past, stakes
- ❌ "Musk pops up in a few other places on X at the same time. He joins still hasn't internalized that gracefully putting …"  cues: you, in_medias_res, past, hope

