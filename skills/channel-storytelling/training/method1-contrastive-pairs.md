# Method 1: Contrastive pairs (cold open vs mid-video window)

Each pair is a real gold answer next to the most confusable distractor, from TRAIN videos only. The cue column lists which rule features fire on each side. Read the pair, then name the difference before you look at the cue column.

**1.** (Adam)
- ✅ "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown. Elon …"  cues: number, year_date, past, superlative, dated_start
- ❌ "And Sable was designed to do every cognitive thing that humans can do. It designs a very complicated virus."  cues: starts_connector, past, superlative

**2.** (Gen)
- ✅ "So, let's buy a house together. I'm thinking a little three-bed."  cues: starts_connector, i_me, past, hope, greeting
- ❌ "After buying enterprise AI licenses, Coinbase's CEO Brian Armstrong was told that adoption was going to take like a quarter or two. …"  cues: you, question, past, future, contrast

**3.** (Adam)
- ✅ "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown. Elon …"  cues: number, year_date, past, superlative, dated_start
- ❌ "Not because this is the moment in a Hollywood plot where the AI suddenly wakes up or becomes an evil genius. This …"  cues: in_medias_res, past, mechanism

**4.** (Adam)
- ✅ "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown. Elon …"  cues: number, year_date, past, superlative, dated_start
- ❌ "1 million. Priority number two is exfiltration — getting Sable's weights off of Galvanic's servers."  cues: number, list_marker, number_start

**5.** (Adam)
- ✅ "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being …"  cues: number, year_date, past, future, stakes, hope
- ❌ "m. Pacific on July 8th and an account by the name of Cindy Steinberg starts this next round."  cues: year_date, list_marker

**6.** (Adam)
- ✅ "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being …"  cues: number, year_date, past, future, stakes, hope
- ❌ "Screenshots are circulating of it calling Elon Musk and Donald Trump deserving of the death penalty. xAI decides to just try asking …"  cues: in_medias_res, stakes

**7.** (Gen)
- ✅ "So, software as we know it might be cooked. And hold on."  cues: starts_connector, we, past, hedge_project, stakes
- ❌ "This deal was actually announced a few years ago in April 2023. But hold on, take a look at that date."  cues: starts_anaphor, number, year_date, past, contrast, viewer_frame

**8.** (Adam)
- ✅ "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being …"  cues: number, year_date, past, future, stakes, hope
- ❌ "Changing the system prompt doesn't change anything about the model's internals. You basically have the same entity underneath, you're just asking it …"  cues: you, in_medias_res, mechanism

**9.** (Others)
- ✅ "This is a diamond, a 580 carat diamond, and they grew it inside this machine. Most people think about diamonds for jewelry, …"  cues: starts_anaphor, number, in_medias_res, demonstrative_def, contrast, superlative
- ❌ "We contacted dozens asking for a tour. Eventually, a small company called Lunavi in Wyoming said yes."  cues: we, past

**10.** (Gen)
- ✅ "So, come with me, you guys, to replace my employee with AI. So, let's see who I should choose."  cues: starts_connector, you, i_me, hope, greeting
- ❌ "And I'm sorry to keep saying this, but it's only going to get worse cuz what we're already seeing is that even …"  cues: starts_connector, callback, i_me, we, in_medias_res, past

**11.** (Adam)
- ✅ "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown. Elon …"  cues: number, year_date, past, superlative, dated_start
- ❌ "There will be powerful models, they will be agentic. If such a model wanted to wreak havoc and destroy humanity or whatever, …"  cues: we, past, future, stakes, mechanism

**12.** (Gen)
- ✅ "So, software as we know it might be cooked. And hold on."  cues: starts_connector, we, past, hedge_project, stakes
- ❌ "Not one of these is a technology decision. Nobody in those rooms had to prove the thing work or made anyone faster …"  cues: past, stakes, superlative

**13.** (Adam)
- ✅ "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being …"  cues: number, year_date, past, future, stakes, hope
- ❌ "Even if it wasn't going to be good, I'd at least like to be alive to see it happen, so you know. …"  cues: callback, you, i_me, year_date, past, future

**14.** (Adam)
- ✅ "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown. Elon …"  cues: number, year_date, past, superlative, dated_start
- ❌ "To state the obvious, though, most human beings are a lot more chill about pursuing their goals than Sable is in the …"  cues: i_me, in_medias_res, future, superlative, profanity, list_marker

**15.** (Gen)
- ✅ "Take a look at the YouTube channels that you're subscribed to. There's a good chance at least one of them was quietly …"  cues: you, past, hope, viewer_frame
- ❌ "Horton and Lennar together built almost as much as the other eight companies in the top 10 combined. But then, the question …"  cues: question, number, past, hope, contrast

**16.** (Gen)
- ✅ "So, come with me, you guys, to replace my employee with AI. So, let's see who I should choose."  cues: starts_connector, you, i_me, hope, greeting
- ❌ "Now, it remains to be seen if they will recover, but for some, they didn't even get that luxury. Which leads us …"  cues: we, future, contrast, list_marker

**17.** (Others)
- ✅ "Giant warehouses are popping up across the US, more than two every week. They feed AI algorithms, store photos, and answer our …"  cues: we, past, superlative
- ❌ "Back in 1995, Microsoft themselves only had 18,000 employees. Today, Microsoft has 221,000, Google has 174,000, Apple has 164,000, Meta has 71,000, …"  cues: number, year_date, in_medias_res, past, superlative, dated_start

**18.** (Others)
- ✅ "THE MIDDLE CLASS: I’m sure you’ve heard about the middle class shrinking. Growing wealth inequality, housing unaffordability, less retirement savings, inaccessible healthcare, …"  cues: you, i_me, definite_unest
- ❌ ""diamonds seems to be the right material." The idea is to grow diamonds right onto chips like a blanket that helps steal …"  cues: —

**19.** (Gen)
- ✅ "So, software as we know it might be cooked. And hold on."  cues: starts_connector, we, past, hedge_project, stakes
- ❌ "See, the thing about these data centers is that they take an insane amount of power. Where like a single big one …"  cues: stakes, superlative

**20.** (Gen)
- ✅ "Take a look at the YouTube channels that you're subscribed to. There's a good chance at least one of them was quietly …"  cues: you, past, hope, viewer_frame
- ❌ "Now, before you get scared, to be fair, if you do own an index fund, then you own both sides. So, when …"  cues: you, we, in_medias_res, past, stakes

## Part 2 –: Contrastive pairs (next beat vs foreign sentence)

Each pair is a real gold answer next to the most confusable distractor, from TRAIN videos only. The cue column lists which rule features fire on each side. Read the pair, then name the difference before you look at the cue column.

**1.** (Especially)
- ✅ "I've been thinking about this one a lot."  cues: i_me
- ❌ "It's kind of crazy how underrated reusing things is."  cues: starts_anaphor, past

**2.** (Especially)
- ✅ "No different than Earth except one major exception."  cues: —
- ❌ "Some people want to ride roller coasters, some people want to start charities."  cues: —

**3.** (Gen)
- ✅ "And this war, if you want to call it that, isn't a fair fight."  cues: starts_connector, you
- ❌ "So, it's no surprise that Recurrent Ventures was all over this to acquire Donut, and they successfully did so in November 2021."  cues: starts_connector, number, year_date, past, stakes

**4.** (Others)
- ✅ "And then drove away."  cues: starts_connector
- ❌ "And this disparity becomes even larger when we compare to household income growth."  cues: starts_connector, we

**5.** (Especially)
- ✅ "A lot of them, I don't think that's going to work."  cues: i_me, future
- ❌ "Musk pops up in a few other places on X at the same time."  cues: —

**6.** (Gen)
- ✅ "And this isn't even mentioning how the big guys have what a guy with a free clone doesn't."  cues: starts_connector
- ❌ "But what I found along the way was exactly why AI only gets more expensive and why humans are suddenly worth keeping …"  cues: starts_connector, callback, i_me, past, contrast, superlative

**7.** (Adam)
- ✅ "If those weights perform well, there's some chance that they could be deployed to customers across the economy."  cues: past, hedge_project, hope
- ❌ "xAI, we're going to be the fastest moving AGI company out there."  cues: we, future, promise

**8.** (Especially)
- ✅ "It's not the going, it's the coming back."  cues: starts_anaphor, future
- ❌ "Now, compare it to the graph about the shrinking middle class."  cues: —

**9.** (Adam)
- ✅ "There's levels of intelligence in the AI, such that if there's any screw up that you first realize after that point, it's …"  cues: you, superlative, list_marker
- ❌ "We call the result a base model."  cues: we

**10.** (Gen)
- ✅ "And to be honest, nor would we want to for some copy with a bunch of bugs."  cues: starts_connector, we
- ❌ "And so, Stanley Martin did exactly what a rational person would do."  cues: starts_connector, past

**11.** (Adam)
- ✅ "Someone tags Grok into a conversation about sexual assault and Will Stancil, a minor left-wing Twitter celebrity."  cues: future, profanity
- ❌ "It's not controversial that we are trying intentionally to make AIs more powerful and more goal-oriented and that we can't directly program …"  cues: starts_anaphor, we, past

**12.** (Gen)
- ✅ "So, back at it, if 90% of data centers are never going to be built, does not just sound like the best …"  cues: starts_connector, question, number, in_medias_res, future, superlative
- ❌ "Because AI as it stands can only ever learn from what already exists."  cues: starts_connector, mechanism, superlative

