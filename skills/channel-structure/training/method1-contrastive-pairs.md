# Method 1: Contrastive pairs (real first sentence vs mid sentence)

Each pair is a real gold answer next to the most confusable distractor, from TRAIN videos only. The cue column lists which rule features fire on each side. Read the pair, then name the difference before you look at the cue column.

**1.** (Gen)
- ✅ "Ladies and gentlemen, data centers are getting canceled."  cues: past, greeting
- ❌ "Well, again, this goes back to the earlier problem in that the workers that would are also gone."  cues: callback

**2.** (Gen)
- ✅ "So, come with me, you guys, to replace my employee with AI."  cues: starts_connector, you, i_me, greeting
- ❌ "Imagine that you're one of 10 shop owners in a small town and every one of your workers spends their paycheck at …"  cues: you, number, imperative_open, superlative

**3.** (Gen)
- ✅ "Take a look at the YouTube channels that you're subscribed to."  cues: you, past, viewer_frame
- ❌ "The thing is, every deal that I've showed you so far are only the ones that we know about."  cues: callback, you, i_me, we, past, definite_unest

**4.** (Gen)
- ✅ "Take a look at the YouTube channels that you're subscribed to."  cues: you, past, viewer_frame
- ❌ "The FTC updated their endorsement rules in 2023 that if a creator gets paid to promote a product, they have to tell …"  cues: you, number, year_date, past, definite_unest, meta_video

**5.** (Adam)
- ✅ "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being …"  cues: number, year_date, past, hope, superlative, dated_start
- ❌ "It convinces an impressionable researcher that this virus contains beneficial gene therapies, that it needs to be spread."  cues: starts_anaphor

**6.** (Others)
- ✅ "You've been alive for 9 seconds when someone asks you a question."  cues: you, number, viewer_frame
- ❌ "You know that Apollo research caught a model attempting to build self-propagating worms and leaving hidden notes to future copies of itself."  cues: you, future, hope

**7.** (Adam)
- ✅ "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown."  cues: number, year_date, past, superlative, dated_start
- ❌ "In the dim lit xAI lair, Will Stancil knelt, whimpering about lawsuits and violent fantasies."  cues: future

**8.** (Gen)
- ✅ "Ladies and gentlemen, data centers are getting canceled."  cues: past, greeting
- ❌ "But, Zappier's SDK is built around the opposite idea."  cues: starts_connector, contrast

**9.** (Gen)
- ✅ "Take a look at the YouTube channels that you're subscribed to."  cues: you, past, viewer_frame
- ❌ "The thing is, every deal that I've showed you so far are only the ones that we know about."  cues: callback, you, i_me, we, past, definite_unest

**10.** (Gen)
- ✅ "Ladies and gentlemen, data centers are getting canceled."  cues: past, greeting
- ❌ "A home builder in Texas said that it now takes him two extra months to finish a house just because so many …"  cues: in_medias_res, past, mechanism

**11.** (Adam)
- ✅ "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being …"  cues: number, year_date, past, hope, superlative, dated_start
- ❌ "All this effort, to what end?"  cues: callback, question

**12.** (Others)
- ✅ "You've been alive for 9 seconds when someone asks you a question."  cues: you, number, viewer_frame
- ❌ "About to be inherited by something that will think it was the one who lived through it."  cues: past, future

**13.** (Others)
- ✅ "Giant warehouses are popping up across the US, more than two every week."  cues: we, superlative
- ❌ "And in many parts of the state, there's little to stop companies from sinking their own wells."  cues: starts_connector

**14.** (Gen)
- ✅ "So, let's buy a house together."  cues: starts_connector, hope, greeting
- ❌ "I mean the last year alone there's been three real attempts at fixing housing."  cues: i_me

**15.** (Gen)
- ✅ "Take a look at the YouTube channels that you're subscribed to."  cues: you, past, viewer_frame
- ❌ "After securing that sweet $300 million funding from Blackstoneone, Recurrent started moving different."  cues: number, past

**16.** (Others)
- ✅ "THE MIDDLE CLASS: I’m sure you’ve heard about the middle class shrinking."  cues: you, i_me, definite_unest
- ❌ "It was the same thing with Intel and AT&T and Xerox and basically every other big tech giant of the era."  cues: starts_anaphor, past, mechanism, superlative

**17.** (Gen)
- ✅ "So, come with me, you guys, to replace my employee with AI."  cues: starts_connector, you, i_me, greeting
- ❌ "A company that AI was in the middle of killing got paid for announcing AI, which means the thing being measured was …"  cues: you, past, mechanism, contrast, superlative

**18.** (Gen)
- ✅ "So, let's buy a house together."  cues: starts_connector, hope, greeting
- ❌ "Horton and Lennar together built almost as much as the other eight companies in the top 10 combined."  cues: number, past, hope

**19.** (Adam)
- ✅ "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being …"  cues: number, year_date, past, hope, superlative, dated_start
- ❌ "They trained an AI system to navigate platformer levels and collect coins."  cues: starts_anaphor, past

**20.** (Gen)
- ✅ "So, come with me, you guys, to replace my employee with AI."  cues: starts_connector, you, i_me, greeting
- ❌ "Before you even have to worry about all the switching, it's simple."  cues: you


## Part 2: Beat label pairs (same video, different beat)

- **SECTION TURN** @ 14%: "So, if you're Elon Musk and you're not happy with the outputs that your model is generating, you have a few different …"
- **CONCLUSION** @ 75%: "But here's the thing."
- **SECTION TURN** @ 52%: "Will this be bad or good for humanity?"
- **SECTION TURN** @ 53%: "So now especially, these software companies must be cooked, right?"
- **CTA** @ 98%: "If you believe in optimistic science and tech stories, subscribe."
- **SECTION TURN** @ 50%: "So, now let's talk about which channels have actually been bought and the few players behind them all."
- **SECTION TURN** @ 91%: "In 2017, a littleknown LLC called Sidecat went to the city of New Albany in Ohio and said, "We are going to …"
- **CTA** @ 98%: "Anyways, I'll be diving even deeper into this next week in my free newsletter in the video description, so would love to …"
- **SECTION TURN** @ 23%: "Grok, I've been wondering as an AI, are you able to worship any God?"
- **CTA** @ 100%: "We'll see you in the next one."
- **CTA** @ 98%: "While you're there, we would love for you to sign up for our newsletter to stay up to date on this topic."
- **CTA** @ 98%: "While you're there, we would love for you to sign up for our newsletter to stay up to date on this topic."
- **SECTION TURN** @ 53%: "So now especially, these software companies must be cooked, right?"
- **SPONSOR READ** @ 44%: "And that's one of the reasons I switched to today's sponsor, ProtonMail."