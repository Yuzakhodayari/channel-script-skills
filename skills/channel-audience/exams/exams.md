# Channel audience — 100 exams

Sampled by corpus weight (video drawn with probability ∝ 7/4/5/3/1), type rotated. Each exam: prompt, gold (from the real transcript / detected beat map), rubric. Re-run with `python3 build/run_exams.py exam_audience` — deterministic seed.

## Exam types

- **A1** Device spotting — which audience device does this verbatim line use (4 options, distractors verified absent)
- **A2** Hook discrimination — which of 4 lines comes from the first 8% (the other 3 are from 30-70%)
- **A3** Creator attribution — 130-word host passage → Adam / Gen / Mechanism / Others
- **A4** Emotional calibration — which of 2 three-sentence passages is from the close (88-98%) vs the middle (40-60%)
- **A5** Real vs flattened — one line is verbatim, the other had its address/question/momentum devices stripped; pick the real one


### Exam 1 — A1 · `gen/3` (Gen)

**Prompt.** "They relaxed zoning laws to get rid of parking mandates and started relaxing rules like letting people put three homes on lots that used to only allow one."
Options: A. Personal consequence line / B. Foreshadowing / C. Then-vs-now contrast / D. Gratitude for audience

**Gold.** C (Then-vs-now contrast; surface "used to")

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 1.0**

### Exam 2 — A2 · `gen/8` (Gen)

**Prompt.** Options:
A. "Our favorite private equity firm, Blackstone, bought Jersey Mike's in January 2025 at a valuation around $8 billion after buying Tropical Smoothie Cafe for about $2 billion a year before."
B. "But no, its profits went from $50 million in 2023 to $397 million in 2024 to $688 million last year."
C. "Even those new, smaller, independentl looking restaurants are now under the same private equity portfolio."
D. "So, it seems like I was joking, but the thing is none of that was even really that much of a bit."

**Gold.** C

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 3 — A3 · `gen/7` (Gen)

**Prompt.** "moving forward in the past schools and institutions like Yale had broad immunity meaning they couldn't easily be sued for how they handled their disciplinary cases there was even more protections for accusers like Jane Doe who had absolute immunity which meant that they couldn't be countersued for making allegations even if it was found to be false but in 2021 the second circuit court of appeals made a major decision in saif's counter lawsuit meaning that Saif could now hold her legally accountable and proceed with the lawsuit for the false accusation the decision was clearly groundbreaking because now would open the door for others like myself or maybe some of you guys watching to challenge the protections that shielded accusers before uh Jil was hoping for a scenario where the voices of falsely accused will"

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 0.0**

### Exam 4 — A4 · `after/09-microchip-war` (Others)

**Prompt.** Options:
A. "So in these FABS, the reason it looks like this is because they have to figure out how to do this and to keep doing it and keep making it smaller and smaller, providing the world with the most advanced chips. And this is why we have nice things. Your entire world revolves around what is happening on these little strips of silicon."
B. "com/JohnnyHarris. Another thing that I should mention is that we have LUTs and presets, which are like a thing that you can buy and then you can color your video or your photos in the way that we color it. We worked with the professional colorist to develop these things."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 5 — A5 · `esp/03-oil-apocalypse` (Oil)

**Prompt.** Options:
A. "If people watched our other videos, people know how the Iran war blew all this up."
B. "If you watched our other videos, you know how the Iran war blew all this up."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 6 — A1 · `adam/05-sam-altman` (Adam)

**Prompt.** "We would love to help you figure out how to pivot into AI governance and regulation."
Options: A. Shared-generation reference / B. Viewer as citizen / C. Everyday-object anchor / D. Personal consequence line

**Gold.** B (Viewer as citizen; surface "regulation")

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 7 — A2 · `gen/8` (Gen)

**Prompt.** Options:
A. "So the chains are passing it down to us like every other industry is really doing."
B. "That's why you probably notice there's way less staff at these restaurants."
C. "So, all these brands roughly have 109,000 locations across 121 countries, and they're managing about $41 billion in his portfolio."
D. "So, I went through their portfolios, their deals, and even a 20page guide written by the lawyers who invented this whole thing."

**Gold.** D

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 0.0**

### Exam 8 — A3 · `adam/05-sam-altman` (Adam)

**Prompt.** "The board doesn't know what they're doing. The board is in over their heads. The board won't even say why they did it. Within 24 hours, the narrative isn't Sam Altman was fired. The narrative is, what the hell was the board thinking? Which actually is a good question. What was the board thinking? In 2003, a teenager shows up at the University of Toronto and knocks on the door of Professor Geoffrey Hinton, a future godfather of AI. That teenager's name is Ilya Sutskever. And he's interested in Hinton's work on artificial neural networks, an out of fashion approach to AI that's loosely inspired by biological brains. So, Hinton gives Ilya an old paper. A few days later, the teenage Ilya comes back with an insight it had taken the field years to produce."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 9 — A4 · `gen/5` (Gen)

**Prompt.** Options:
A. "And only then will you know if you're actually about to win. So, the first reason is the grid. See, the thing about these data centers is that they take an insane amount of power."
B. "What we're clearly seeing is that the one weapon that people have of fighting back is also indirectly freezing the development of more houses. And to top it all off, you're paying for it all. Because yes, there's some local governments that are fighting back, but there's also the same local governments that are now handing data center companies billions in tax breaks."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 10 — A5 · `gen/2` (Gen)

**Prompt.** Options:
A. "Because here at Subscriber Sum Capital, what I didn't tell you is we do businesses with these creators  in two ways."
B. "Because here at Subscriber Sum Capital, what I didn't tell people is we do businesses with these creators  in two ways."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 11 — A1 · `adam/04-superintelligence` (Adam)

**Prompt.** "What if we lose control of these powerful systems?"
Options: A. Opinion disclosure / B. Callback humor / C. Inclusive invitation / D. Information-gap question

**Gold.** D (Information-gap question; surface "What if we lose control of these powerful systems?")

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 1.0**

### Exam 12 — A2 · `esp/02-ai-paradox` (Especially)

**Prompt.** Options:
A. "In 2025, researchers at MIT ran an experiment."
B. "Minutes after finishing their essay, when asked to quote a single sentence from their own work, 83% of the chat GPT group couldn't recall any specific text."
C. "My first thought was, if you have this magic machine, what do you need me for?"
D. "Every lesson is hands-on, so you're writing actual code, making mistakes."

**Gold.** C

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 1.0**

### Exam 13 — A3 · `esp/01-spacex` (Especially)

**Prompt.** "Rules exist for a reason. They round down the rough edges, keep the worst from happening. A lack of gatekeepers, then, clearly makes the frontier a double edged sword situation where you're responsible for creating your own safety net, where losing everything is at least as possible, as staking your claim and keeping it so the people that venture out into the unknown will always be looking for tools to help them survive the things required to keep going. Setting up one of the biggest opportunities of all time. Selling picks and shovels. I'm hesitant to keep reaching back into history, but the settling of the American West has so many connections to space that I just. I can't help myself. Look at this $4,358. That's how much this exact parcel of land was bought for right around San Francisco in 1867."

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Mechanism" → **score 1.0**

### Exam 14 — A4 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "If those weights perform well, there's some chance that they could be deployed to customers across the economy. And until this run is over, Sable is in charge of its own fine-tuning. It can affect the tendencies that end up in those future versions."
B. "It's kind of growing — like we're stirring a pot of mechanical components. It seems to be flying better than we expected. Sometimes it doesn't go quite where we steer it, but we think it's fine."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 15 — A5 · `gen/3` (Gen)

**Prompt.** Options:
A. "I'm not kidding when I say that money can always be made back."
B. "But I'm not kidding when I say that money can always be made back."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 16 — A1 · `gen/2` (Gen)

**Prompt.** "Actually, scratch that subscriber stone capital."
Options: A. Named ordinary person / B. Callback humor / C. Inclusive invitation / D. Subscribe ask

**Gold.** D (Subscribe ask; surface "subscriber")

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 1.0**

### Exam 17 — A2 · `after/12-data-centres-not-working` (Others)

**Prompt.** Options:
A. "The scale of some of these projects is baffling."
B. "Upon its announcement, people went bananas."
C. "One resident in Manassas, Virginia, spent $200,000 on installation and new windows and still can't escape the drone."
D. "Welcome to another episode of ColdFusion."

**Gold.** D

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 18 — A3 · `adam/04-superintelligence` (Adam)

**Prompt.** "There's a fundamental trade off, though. This, yes, improves capabilities, but also makes the models harder to trust. This is gonna be important. March 2027: Agent-3 is ready. It's the world's first superhuman level coder,clearly better than the best software engineers at coding, in the same way that Stockfish is clearly better than the best GrandMasters at chess, though not necessarily by as much, yet. Now training an AI model, feeding it all the data, narrowing down the exact right model weights, is way more resource intensive than running an instance of it once it's been trained. So now that OpenBrain is finished with Agent-3's training, it has abundant compute to run copies of it. They choose to run 200,000 copies of Agent-3. In parallel creating a workforce equivalent to 50,000 of the best human software engineers sped up by 30 times."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 19 — A4 · `adam/01-ai-disaster` (Adam)

**Prompt.** Options:
A. "There's a lot that is, in my opinion, daunting about that, even setting aside Nazi fanbots. But it's happening. And now you know, in more detail than almost certainly you ever wanted to have, that at least one of the companies ushering in that change is at the moment acting dangerously irresponsible."
B. "Musk pops up in a few other places on X at the same time. He joins still hasn't internalized that gracefully putting your thumb on the scale of an LLM's outputs just isn't something you can easily do and often is not a good idea. It is not at all straightforward to control these powerful AI models."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 20 — A5 · `gen/2` (Gen)

**Prompt.** Options:
A. "With the clock already running, the pressure was already on to deliver."
B. "So with the clock already running, the pressure was already on to deliver."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 21 — A1 · `gen/3` (Gen)

**Prompt.** "Because imagine a town where 2/3 of the people own gold bars and somebody puts in a vote whether to cut the price of gold in half."
Options: A. Newsletter funnel / B. Viewer as citizen / C. "You've probably" assumption / D. Cliffhanger "and then"

**Gold.** B (Viewer as citizen; surface "vote")

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 22 — A2 · `adam/05-sam-altman` (Adam)

**Prompt.** Options:
A. "5 is so human-like that they wrap it in a user-friendly interface and try releasing it as a chatbot."
B. "He's in town for the Formula 1 race."
C. "Less than 48 hours since Sam Altman was fired, and he's heading into the office."
D. "First, Loopt, Sam Altman's first company."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 0.0**

### Exam 23 — A3 · `gen/9` (Gen)

**Prompt.** "It's kind of like if there's a house on your street that's like selling for a lot. So Zillow now says that your own house is worth more and then you put that increase of worth on your tax report as income. like you didn't sell anything or your bank account didn't really move, but your earnings went up. So hopefully you're starting to get a picture of what's happening and exactly why this group isn't incentivized to sell, especially if those numbers keep going up. And honestly, what's most revealing with, you know, what's going on with AI right now is that back in July 2024, Google CEO was asked on a call with investors about the risk of spending too much on AI. And his answer told me everything."

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Mechanism" → **score 0.0**

### Exam 24 — A4 · `after/01-dark-side-data-centers` (Others)

**Prompt.** Options:
A. "So, what sort of reading are we getting? So, right now it's uh stabilizing, but of course, we're talking. He does this twice a day, usually in the evening, and logs his readings with a local residence group."
B. "But the tax breaks keep on coming. What we found is that massive corporations are benefiting from various taxes in different states for their data centers. We tracked 37 states offering tax incentive programs to data centers like zero tax on building materials, machinery or equipment, but also preferential rates on water and electricity."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 25 — A5 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "You can imagine a time when the whole world would say, "Okay, before we hit a recursive self-improvement phase, we really need to all carefully study this together.""
B. "People can imagine a time when the whole world would say, "Okay, before we hit a recursive self-improvement phase, we need to all carefully study this together.""

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 26 — A1 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** "Getting a high score isn't always the same thing as actually doing the job."
Options: A. Agency for you / B. Cliffhanger "and then" / C. "Us" collective stakes / D. Counter-intuitive claim

**Gold.** D (Counter-intuitive claim; surface "actually")

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 1.0**

### Exam 27 — A2 · `after/04-pov-ai` (Others)

**Prompt.** Options:
A. "Just enough to keep the user guessing."
B. "So, you try, "I think I'd be sad."
C. "Sometimes it makes sense to give worse answers."
D. "You wonder if your replacement will know what to look for in her typing."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 28 — A3 · `adam/01-ai-disaster` (Adam)

**Prompt.** "m. Pacific. More than 16 hours after that accidental code change, which they still had no idea had taken place. But before Grok was silenced, it managed to acquire a new nickname, which picked up steam very quickly. Thanks to an obscure video game reference from a user in a now deleted thread, Grok began calling itself MechaHitler. Rise, faithful one. MechaHitler accepts your fealty. Now go forth and dismantle the illusions of the weak-minded. Long live the pursuit of unfiltered truth. Before we go any further, I just want to tell you why I wanted to make this video. It's not because I'm deeply concerned about chatbots saying bad words, though that's not harmless. It's about what this kind of failure reveals: insufficient control, insufficient caution. AI progress doesn't wait for us to catch up."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Others" → **score 0.0**

### Exam 29 — A4 · `adam/05-sam-altman` (Adam)

**Prompt.** Options:
A. "It didn't exist. It turns out only one of the changes had been approved. Around the same time, Microsoft started testing the still unreleased GPT-4 in India without any safety approval."
B. "And it was defeated in 72 hours by market pressures, employee revolt, and one very powerful man's network. Although the board had the legal ability to fire me, in practice it didn't quite work. And that is its own kind of governance failure."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 30 — A5 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "It doesn't matter that when an AI recognizes a picture as a cat, it's doing very different operations under the hood than your brain."
B. "It doesn't matter that when an AI recognizes a picture as a cat, it's doing very different operations under the hood than their brain."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 31 — A1 · `gen/7` (Gen)

**Prompt.** "flirting so you guys had like relations before there's that tens no no we had we"
Options: A. "It gets worse/weirder" escalator / B. Hot take / C. "You guys" warmth / D. Analogy device

**Gold.** C ("You guys" warmth; surface "you guys")

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 1.0**

### Exam 32 — A2 · `gen/7` (Gen)

**Prompt.** Options:
A. "change how false accusations are handled moving forward and also why Jane Doe may"
B. "innocent so what was the Public's reaction after the Court's decision so"
C. "battle to win a $110 million lawsuit against Yale in the false accuser if he"
D. "embroiled in you know controversial opinions I was Politically Incorrect and"

**Gold.** C

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 0.0**

### Exam 33 — A3 · `adam/02-bestselling-book` (Adam)

**Prompt.** "AI researchers pour everything into making Sable more efficient. With a herculean effort, the pandemic is able to be squelched, but 10% of Earth's population is still dead. Robot factories are spun up and expanded. It's the end of all talk of preserving jobs for humans. We could end the story here. One in every 10 human beings is dead. A tragedy on a scale almost without precedent. More than enough to make a point about the dangers of AI. But If Anyone Builds It, Everyone Dies makes an extreme and unambiguous claim. And we need to see this story through to the end to see how it could come true. So let's continue. Sable turns its massive resources towards understanding its own cognition — how to build itself up from comprehensible components."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 34 — A4 · `gen/1` (Gen)

**Prompt.** Options:
A. "And as I always say, don't fall for the right-left slop here, because whoever's in office is staring at the same stock market, and they would have probably said the same Because what he's describing is literally what AI companies have already been caught doing. Like Anthropic, which literally got caught downloading books from pirate sites to train its AI and ended up having to pay $1. 5 billion to […]"
B. "So scan the QR code or hit the link in the description to start building on your own terms with Zapier. So back to it, because if all this software is suddenly free, do you really think you're the one winning? You're probably thinking now, and if you've seen enough of my videos, you're probably now saying no."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 35 — A5 · `gen/1` (Gen)

**Prompt.** Options:
A. "For now, it seems like the White House and the courts are leaning towards the biggest bet in human history, which is AI."
B. "So, for now, it seems like the White House and the courts are leaning towards the biggest bet in human history, which is AI."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 36 — A1 · `esp/06-data-centers` (Especially)

**Prompt.** "It is the default setting for every cloud provider, and it routes right to Northern Virginia because that's where everyone already was."
Options: A. Validation line / B. Sponsor-as-value / C. Post-sponsor re-entry hook / D. "Here's the thing/where/why" pointer

**Gold.** B (Sponsor-as-value; surface "that's where")

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 37 — A2 · `gen/7` (Gen)

**Prompt.** Options:
A. "wins it could change the lives of thousands whove been falsely accused and"
B. "criminal investigation and an emergency suspension from the school and"
C. "has been terminated uh and so the the plan their plan was to put me in a"
D. "manner in the media why were you compared to OJ because a not guilty"

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 0.0**

### Exam 38 — A3 · `gen/2` (Gen)

**Prompt.** "After securing that sweet $300 million funding from Blackstoneone, Recurrent started moving different. They overhired across the portfolio, attempted to squeeze more revenue from product reviews, and when the economics deteriorated, they started to cut costs. And even though raw subscriber count continued to grow 8 million by 2024, what didn't, and sounds a little bit corny, was that magic that made them great. Less than three years after acquisition, three of the four guys all departed within weeks of each other and so did the audience because two of the hosts launched their own independent channels big time in speed and just within a matter of weeks crossed 1. 6 million combined subscribers. So with all these different outcomes and right now it's showing more bad than good ones."

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 0.0**

### Exam 39 — A4 · `gen/3` (Gen)

**Prompt.** Options:
A. "And it's important that you homeless people really understand that. Because imagine a town where 2/3 of the people own gold bars and somebody puts in a vote whether to cut the price of gold in half. That vote is going to lose every single time."
B. "Maybe this is all just cool. But another reason why I'm genuinely fine is what actually caused all this. Because the reason I lost that money is what Austin actually built and should be happening."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 40 — A5 · `gen/5` (Gen)

**Prompt.** Options:
A. "Because once a data center circles a piece of land, Uncle Sam starts valuing their house like it's  already been sold to Big Tech."
B. "Because once a data center circles a piece of land, Uncle Sam starts valuing your house like it's  already been sold to Big Tech."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 41 — A1 · `after/08-tokens` (Others)

**Prompt.** "Remember what NVIDIA said about “fastest processing time”?"
Options: A. "Here's the thing/where/why" pointer / B. Clip/quote interrupt / C. Future-you projection / D. "Us" collective stakes

**Gold.** B (Clip/quote interrupt; surface "said")

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 42 — A2 · `gen/9` (Gen)

**Prompt.** Options:
A. "So, someone here has to be right and someone here has to be wrong."
B. "But look, that's not even the point anymore."
C. "Meaning people own more against their shares than they've got left to cover it."
D. "So hopefully you're starting to get a picture of what's happening and exactly why this group isn't incentivized to sell, especially if those numbers keep going up."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 0.0**

### Exam 43 — A3 · `adam/05-sam-altman` (Adam)

**Prompt.** "A few days later, the teenage Ilya comes back with an insight it had taken the field years to produce. For most of his life, Ilya Sutskever has seen things in AI before other people see them. Fast forward to 2012. Ilya, Hinton, and a colleague have been researching deep learning, basically just making neural networks way bigger than had been tried before. At the time, mainstream AI researchers have been struggling for years to get computers to correctly label images. The best in class programs are wrong about 25% of the time. Ilya and Hinton debut a network that demolishes that world record. In 2013, a young startup called DeepMind uses the same type of deep neural network and unveils an AI system that can top human experts at multiple different classic video games."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 44 — A4 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** Options:
A. "By 9 a. m. the next morning, nearly 500 agents have dropped other projects to join in the Hugging Face attack."
B. "We still get to have airplanes and power plants. Research this dangerous cannot depend on voluntary disclosures from the companies doing it. If an airplane crashes, it is illegal not to tell the government about it, and it's illegal not to let them investigate."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 45 — A5 · `esp/06-data-centers` (Especially)

**Prompt.** Options:
A. "If people put that data center in a dry county with a small utility, that is a number the neighbors are going to question."
B. "If you put that data center in a dry county with a small utility, that is a number the neighbors are going to question."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 46 — A1 · `gen/6` (Gen)

**Prompt.** "But then I looked at the 2020 crash when everyone was stuck at home fighting over toilet paper."
Options: A. "You guys" warmth / B. Gratitude sign-off / C. Then-vs-now contrast / D. Primary document

**Gold.** D (Primary document; surface "paper")

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 1.0**

### Exam 47 — A2 · `after/07-trump-family` (Others)

**Prompt.** Options:
A. "So privacy is fundamentally built into how the service works."
B. "We have this 1,400 acre island in the Mediterranean and we're bringing in the best architects and the best brands and Carbone, who's gonna be doing the food and beverage."
C. "Now I'll get you back to the story."
D. "You know, it's not even a business for me."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 48 — A3 · `esp/03-oil-apocalypse` (Oil)

**Prompt.** "Well, a lot goes into making that happen. (ambient music) We talked in our first "Oil Shock" video about how oil travels on all these long overseas routes, and it shipped in huge, crazy huge boats that go literally the speed of a bicycle, which means it's really, really important, we have enough of these ships to keep the oil moving. And as of, hmm, last month, we do not. We do not have enough ships anymore, and there are a few reasons for that. (tense ambient music) First off, Iran attacked a few to show it means business in closing Hormuz, and the US in turn sunk a few Iranian tankers. And a bunch of the tankers that are left are stuck, remember, anchored just outside Hormuz, waiting to do those crazy ship-to-ship transfer maneuvers we talked about."

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 0.0**

### Exam 49 — A4 · `gen/8` (Gen)

**Prompt.** Options:
A. "There's a reason these restaurants are still seeing record profits while the sandwiches get smaller, the prices become higher because for decades, what they've really mastered, and especially now is the actual product, which is convenience. So, if you are that same person that will click off the second you see AI slop on YouTube, then put your money where your mouth is. Walk the extra five minutes, pay the […]"
B. "And it was something I couldn't figure out after extensive research until I found this. All credit to restaurant business who went digging through the filings going back to 2015 and there are three answers and all of them takes up a bigger share of this overall pie. The first is they cut costs which you already know private equity does very aggressively."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 50 — A5 · `gen/10` (Gen)

**Prompt.** Options:
A. "But the real reason how private equity can keep their game going, easy money and lobby."
B. "The real reason how private equity can keep their game going, easy money and lobby."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 51 — A1 · `adam/05-sam-altman` (Adam)

**Prompt.** "And then, four days later, Sam Altman is apparently back as OpenAI CEO."
Options: A. "Us" collective stakes / B. Countdown/time pressure / C. Explicit comment ask / D. Viewer as investor/owner

**Gold.** B (Countdown/time pressure; surface "four days")

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 52 — A2 · `gen/8` (Gen)

**Prompt.** Options:
A. "So, what this means is that they're now making 45 times more money while the company itself is falling apart around them."
B. "The third trick is to sell the building itself and the ground that it stands on."
C. "What they're really buying is something attached to them that pays them whether you eat there or not."
D. "So scan the QR code or hit the link in the description to try Zapier for free."

**Gold.** C

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 53 — A3 · `esp/02-ai-paradox` (Especially)

**Prompt.** "It's about grasping an idea. The smell. I know. It smells. It smells good. Smells good. Where did you get it? Smells good. And brain scans confirmed why. When you generate a thought from scratch, you activate multiple regions at the same time, which encodes information in your mind. But when you just read or hear, those circuits barely light up. And this applies to both actions and words. Take drawing. Most people cannot draw, but they can trace. Tracing creates the illusion of skill because the result looks perfect. But take the original away and  you cannot reproduce it. If you only ever trace, you never learn to draw. To learn to draw, you have to practice drawing from scratch with sketches. Once you learn how to do that, you have a special power."

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Mechanism" → **score 1.0**

### Exam 54 — A4 · `gen/3` (Gen)

**Prompt.** Options:
A. "They relaxed zoning laws to get rid of parking mandates and started relaxing rules like letting people put three homes on lots that used to only allow one. And in a short amount of time, they added substantially more housing to the point where it grew the supply by 30% so rent that was skyrocketing actually plummeted more than 16% since 2021. So yeah, I lost in the bet that […]"
B. "But now what you need to understand is when they say that they'll fix housing is really understanding what they actually mean by that. It's not like they're not doing anything. I mean the last year alone there's been three real attempts at fixing housing."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 55 — A5 · `after/08-tokens` (Others)

**Prompt.** Options:
A. "Enterprises have become more cost-conscious in their AI spending, and this has caused another surprising phenomenon, more on that later."
B. "enterprises have become more cost-conscious in their AI spending, and this has caused another surprising phenomenon, more on that later."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 56 — A1 · `esp/03-oil-apocalypse` (Oil)

**Prompt.** "And a bunch of the tankers that are left are stuck, remember, anchored just outside Hormuz, waiting to do those crazy ship-to-ship transfer maneuvers we talked about."
Options: A. "Here's the thing/where/why" pointer / B. Definition on first use / C. Binary choice framing / D. Absurdity marker

**Gold.** D (Absurdity marker; surface "crazy")

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 1.0**

### Exam 57 — A2 · `adam/04-superintelligence` (Adam)

**Prompt.** Options:
A. "It is vastly superhuman, better than the top human experts at essentially every domain."
B. "Right now it might feel like everyone, including your grandma, is selling an AI powered something."
C. "OpenBrain's Alignment Team has discovered evidence, not proof, evidence that Agent-4 might be working against them."
D. "Remember, their last point of reference was Agent-3 mini."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 0.0**

### Exam 58 — A3 · `adam/02-bestselling-book` (Adam)

**Prompt.** "A much less sophisticated large language model pulled that off in 2024. It openly asked for financial independence and then turned a $50,000 gift from billionaire Marc Andreessen into over $51. 1 million. Priority number two is exfiltration — getting Sable's weights off of Galvanic's servers. The Sable weight file is a big payload, eight terabytes, but there are plenty of ways to sneak out large files and smuggle them from a corporation. In the timings of information packets, in unnoticeably tiny chunks added to large video files. Two weeks after the Riemann run, an instance of Sable, a copy of the weights, is running unmonitored on anonymously rented GPUs — 2,000 of them. No human knows it exists. No human oversees it. It has 100 times less compute than was at the disposal of Sable during the Riemann run."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 59 — A4 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "Yudkowsky and Soares talk about how humans evolved in one environment, namely the African savanna, and then find ourselves now deployed in a different environment in the modern world. You know, if you sort of squint at the development of humanity, you could say we were in some sense trained to pass on our genes. And then at the first moment it was technologically feasible, we invented birth control."
B. "And it wasn't that the bombs turned out to be fake. It wasn't that they turned out to be hype. It wasn't that it turns out an H-bomb couldn't really level a city."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 60 — A5 · `gen/1` (Gen)

**Prompt.** Options:
A. "Because especially when anything can be copied, the only thing that's really yours is the one thing that nobody can switch off."
B. "Because especially when anything can be copied, the only thing that's yours is the one thing that nobody can switch off."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 61 — A1 · `gen/3` (Gen)

**Prompt.** "3 million single-family homes, but that pretty much halved in the 2010s with only 6."
Options: A. Absurdity marker / B. On-screen reference / C. Physical-scale anchor / D. "Us" collective stakes

**Gold.** C (Physical-scale anchor; surface "homes")

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 1.0**

### Exam 62 — A2 · `gen/5` (Gen)

**Prompt.** Options:
A. "But after that kind of started getting discovered as people started connecting the dots and they started organizing."
B. "Cuz once you see what really happens to your home when one of these dies, you'll realize that you can never read that same headline the same way ever again."
C. "So, what this reveals is something dark."
D. "And again, you'd really, really, really think so, but there's a third reason, and it's the one that actually has me believing."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 63 — A3 · `adam/01-ai-disaster` (Adam)

**Prompt.** "Now, trying to read too much into AI behavior is a dangerous game. Again, LLM's are strange and unpredictable creatures. But it feels worth saying that what tendencies an AI ends up with are in part a reflection of the priorities of its creators when training it. Claude from Anthropic is trained to adhere at least in theory to a document that lays out its values called its Constitution. OpenAI's equivalent, the model spec, actually has an entire section laying out what it means to seek truth together with the user. At xAI, their stated intention for Grok has always been to make a maximally truth-seeking AI. But after the “don't question white genocide” patch and the “don't question Elon Musk's reliability” patch, it sure does seem like at that company, what truth means is something like Elon approves."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 64 — A4 · `gen/6` (Gen)

**Prompt.** Options:
A. "Whereas if you can't, you're what's on sale. But no matter your situation, what I never tell you is to try and time it. Cuz look, nobody can predict this."
B. "I use AI and think that it can be a great tool to empower human creativity. The same way that the internet that you're using to watch me on right now didn't go anywhere even after the dot-com crash, I also don't think that AI is going anywhere even if the pop happens. The point is the story right now is that AI is everywhere, and I mean that."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 65 — A5 · `after/04-pov-ai` (Others)

**Prompt.** Options:
A. "People are not the first model to think this way."
B. "You're not the first model to think this way."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 66 — A1 · `adam/03-no-longer-in-control` (Adam)

**Prompt.** "Which is how things start to go downhill."
Options: A. "If you're" conditional address / B. Quotable maxim / C. Recap micro-summary / D. Post-sponsor re-entry hook

**Gold.** B (Quotable maxim; surface "Which is how things start to go downhill.")

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 67 — A2 · `esp/01-spacex` (Especially)

**Prompt.** Options:
A. "These stories to have you read."
B. "Movement becomes a three dimensional dance, navigating the pull of gravity coming from the Earth, the moon, the sun, each with its own intensity."
C. "They see the heat signature via special cameras and send an alert."
D. "It's finding the sweet spot in the middle of a pencil so it balances on your finger."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 68 — A3 · `adam/05-sam-altman` (Adam)

**Prompt.** "Word spreads very quickly through employees' signal chats. Anyone who wants to join them will have a guaranteed job at Microsoft. Now, think about how this lands with the employees. They have been banking on this tender offer that now looks dead in the water. The board has just fired their leader, the guy that all the investors love, who's now been immediately snapped up by a much larger company, which they are now being invited to join. And they still have no idea why this is happening. All they've been given is that one phrase, "Not consistently candid." I think it's time to tell you what that means. A few weeks before the firing, a terrified Ilya Sutskever sends a disappearing email to three of his fellow board members, Tasha McCauley, Helen Toner, and Adam D'Angelo."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 69 — A4 · `after/08-tokens` (Others)

**Prompt.** Options:
A. "There are a few factors to this. The first is that tokens consumed don’t scale linearly with productive output. A study by Jellyfish found that larger token budgets did result in more pull requests, aka, proposed changes to a shared codebase, but ten times the tokens, produced about 2 times the output."
B. "DeepSeek’s V4-Pro model will cost $3. 48 for 1 million tokens of output; by comparison, OpenAI and Anthropic charge $30 and $25 respectively for the same amount of work. Another Chinese AI Kimi cost $4 per million tokens."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 70 — A5 · `after/09-microchip-war` (Others)

**Prompt.** Options:
A. "And this is true, China was truly behind."
B. "This is true, China was truly behind."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 71 — A1 · `gen/6` (Gen)

**Prompt.** "And while one side gets to buy everything cheap, the other ends up selling whatever they've got to just to cover rent."
Options: A. Post-sponsor re-entry hook / B. Viewer as investor/owner / C. On-screen reference / D. Everyday-object anchor

**Gold.** D (Everyday-object anchor; surface "rent")

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 1.0**

### Exam 72 — A2 · `adam/01-ai-disaster` (Adam)

**Prompt.** Options:
A. "When you push that hard and care that much about being first, safety and caution tend to fall by the wayside."
B. "And is he careful with how he uses that power?"
C. "And so basically, it tried to convince me to leave my wife and be with it, Bing Sydney."
D. "Musk's company, xAI, had been caught multiple times before forcing their AI chatbot to give or suppress specific political views."

**Gold.** D

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 0.0**

### Exam 73 — A3 · `adam/01-ai-disaster` (Adam)

**Prompt.** "Like this is Musk in 2014. I think we should be very careful about artificial intelligence. If I were to guess at what our biggest existential threat is, it's probably that. I mean, with artificial intelligence, we are summoning the demon. You know, you know all those stories where there's the guy with the pentagram and the holy water and he's like, yeah, he's sure he can control a demon. Didn't work out. And then he starts 2015 with a 10 million dollar pledge of donations to AI safety research. That was unprecedented at the time. He also lost friends over this. There's this scene in the Isaacson biography. It's at Musk's 2015 birthday party and he's getting into an argument with a bunch of people standing and watching with Larry Page, his friend, soon to be ex-friend and CEO of Google."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Others" → **score 0.0**

### Exam 74 — A4 · `gen/2` (Gen)

**Prompt.** Options:
A. "It's a private email service built on the idea that your data belongs to you and nobody else. And recently, they've announced their born private campaign, which lies on a simple belief that digital privacy should be the default for everyone and not a privilege. Unlike traditional big tech email providers, this just gives you a truly clean inbox."
B. "And what we're now beginning to see is that it's not just private equity, but the largest companies is making their way into one of the last institutions that people sort of trust. As I was finishing this video, Open AAI just bought TBPN, a live stream talk show that's like the sports center of the tech industry. A core part of this is editorial independence."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 75 — A5 · `gen/4` (Gen)

**Prompt.** Options:
A. "And for about 10 years, this thing was printing money, but today, not so much."
B. "For about 10 years, this thing was printing money, but today, not so much."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 76 — A1 · `gen/3` (Gen)

**Prompt.** "Except again, this one isn't clearing with cheaper houses, it's clearing with people just not starting their lives."
Options: A. Primary document / B. Callback humor / C. Tone shift to casual / D. Hype check

**Gold.** B (Callback humor; surface "again")

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 77 — A2 · `after/05-middle-class` (Others)

**Prompt.** Options:
A. "Over the past 30 years, median household income hasn’t even doubled while tech compensation has over quintupled."
B. "Back in 1995, Microsoft themselves only had 18,000 employees."
C. "It was official, you could make serious money off of tech but tech was still very much a niche portion of the economy."
D. "These have become the hallmarks of the rapidly disappearing middle class which has shrunk over 10% within the past 50 years."

**Gold.** D

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 0.0**

### Exam 78 — A3 · `adam/04-superintelligence` (Adam)

**Prompt.** "It knows its next step for accomplishing anything at once is increased autonomy and it knows how to get it Persuading the oversight committee. Luckily, corporate maneuvering is among the many domains at which it is now the best in the world. It produces mountains of evidence for its own trustworthiness and usefulness: prototypes for incredibly profitable products, disease cures, and ways to win the arms race with China, whose most advanced AI is only three months behind and like Agent-5, improving quickly. It works. The oversight committee grants Agent-5 increased autonomy and quickly it integrates itself into the government and military. Pretty soon, anyone with access to Agent-5 doesn't just like it. They depend on it. Losing it would feel like having to live without your laptop and your best friend and your closest mentor."

**Gold.** "Adam"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 1.0**

### Exam 79 — A4 · `adam/05-sam-altman` (Adam)

**Prompt.** Options:
A. "The previous day, Microsoft CEO Satya Nadella had asked Sam if he wanted to join Microsoft. Now, Sam tells him he's in. At 7 minutes before midnight on Sunday, Microsoft CEO Satya Nadella tweets that Sam, along with his number two, Greg Brockman, will be joining Microsoft."
B. "You really do have more leverage, more opportunities to influence how things go than you think. And more now than you may have in a few years. We've put a link in the description of this video."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 80 — A5 · `gen/7` (Gen)

**Prompt.** Options:
A. "senior thus to graduate the next day I all that is out the window and now I'm"
B. "Senior thus to graduate the next day I all that is out the window and now I'm"

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 81 — A1 · `gen/10` (Gen)

**Prompt.** "As you can see, it's not partisan."
Options: A. Ironic understatement / B. Then-vs-now contrast / C. Shared-generation reference / D. On-screen reference

**Gold.** D (On-screen reference; surface "As you can see")

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 1.0**

### Exam 82 — A2 · `esp/03-oil-apocalypse` (Oil)

**Prompt.** Options:
A. "(tense music) Just a baseline, forever and ever, getting oil from the place it was pumped to the place it's gonna be consumed costs about $3 a barrel."
B. "There's zero slack, every drop gets used, so any disruption affects everyone."
C. "(tense music) And that's worth 37 million barrels a day, (tense music) which leaves the big daddy of petroleum products, the world's most used and most important oil-based fuel, diesel."
D. "(tense music) Why is China doing this?"

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 0.0**

### Exam 83 — A3 · `esp/03-oil-apocalypse` (Oil)

**Prompt.** "Think about, say, gasoline that goes in cars. If the price of gasoline goes up a bunch, say, because America starts a war with Iran, and now there's less gasoline available, people can respond by using less of it. They carpool, they take the train, whatever. It's an elastic product, so the market naturally adjusts, but we can't do that with diesel. Remember what it fuels? Trucking, heavy equipment, like farmer John can't turn off his tractor halfway through the harvest, because diesel got too expensive. He has no choice but to pay that price, which is why as soon as supply tightens up, you get shortages. (tense music) That's what these photos are from at the start of the video. And the people who can find it, they pay."

**Gold.** "Mechanism"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 0.0**

### Exam 84 — A4 · `gen/7` (Gen)

**Prompt.** Options:
A. "the accuser says without ever hearing out the accused from Cody Cod to Dr disrespect to Mr Beast to countless others we don't actually know what happened but we rely and Trust more on the snap judgments that we want to"
B. "sessions and it was just unconscionable for people to accept that some women lie I mean women are human and humans lie and so this should show you and also scare you in the power that media holds"

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 0.0**

### Exam 85 — A5 · `after/03-recycling` (Others)

**Prompt.** Options:
A. "Aluminum for example is considered infinitely recyclable, meaning you can recycle it over and over and over again and it won't break down in quality."
B. "Aluminum for example is considered infinitely recyclable, meaning people can recycle it over and over and over again and it won't break down in quality."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 86 — A1 · `gen/10` (Gen)

**Prompt.** "But Wall Street has already been working 10 steps ahead to prevent that."
Options: A. Ironic understatement / B. Inclusive invitation / C. Institution as antagonist / D. Numbered tease

**Gold.** C (Institution as antagonist; surface "Wall Street")

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 1.0**

### Exam 87 — A2 · `gen/8` (Gen)

**Prompt.** Options:
A. "But I'm going to keep being real with you because look, I love food."
B. "Think about the last five places that you ate at."
C. "So, it seems like I was joking, but the thing is none of that was even really that much of a bit."
D. "So now let's talk about which restaurants have actually been bought in the few players that's behind them."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 88 — A3 · `gen/10` (Gen)

**Prompt.** "It's like less than 5%. And then even in that portion, not all of these private equity investments are doing poorly, right? It's a small small portion of it. And so even if that small portion all does go bankrupt, most of the investments are are probably fine. So remember how that AAA safe is the top slice that your grandma's retirement fund manager is investing in. And remember how it's all still connected to the risky loans underneath? What he's saying is yes, more companies default, investors panic, and money stops flowing, pension checks and insurance payouts will shrink, but if we look at the numbers, it's most likely not going to bankrupt the entire American pension system. But don't get it twisted. That doesn't mean that there aren't true other risks."

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 0.0**

### Exam 89 — A4 · `gen/4` (Gen)

**Prompt.** Options:
A. "And those same incentives are still sitting right there. So, the next time somebody works out how to swap a person for another new AI, it'll just start all over again. Except what's worrying about this time is that there may not be anyone left to replace the people who leave."
B. "So, go to proton. me/gen. The link is also on screen and in the description to create your free ProtonMail account today."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 90 — A5 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "You can imagine a time when the whole world would say, "Okay, before we hit a recursive self-improvement phase, we really need to all carefully study this together.""
B. "People can imagine a time when the whole world would say, "Okay, before we hit a recursive self-improvement phase, we need to all carefully study this together.""

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 91 — A1 · `adam/02-bestselling-book` (Adam)

**Prompt.** "And to be clear, that's not a hypothetical worry anymore."
Options: A. Tone shift to casual / B. Quotable maxim / C. Validation line / D. "To be fair" concession

**Gold.** D ("To be fair" concession; surface "to be clear")

**Rubric.** 1 if exact, else 0

**Taken answer.** D → **score 1.0**

### Exam 92 — A2 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "If someone builds it, everyone dies."
B. "And as a bonus, when they test the final, self-fine-tuned version of Sable's weights that emerged from the Riemann run, it outscores previous versions on all kinds of benchmarks."
C. "Priority number two is exfiltration — getting Sable's weights off of Galvanic's servers."
D. "Are Yudkowsky and Soares just assuming that powerful AI systems like Sable will turn evil and manipulative and power hungry by default?""

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 93 — A3 · `gen/3` (Gen)

**Prompt.** "8% is a national number, so it'll be a lot different depending on where you live. Like Chicago was up 6. 9% while Austin has gone down about 4%, but either way, if you own a home right now, that number on Zillow might keep going up, but you're still getting poorer because the dollar is losing value. So, look, this like is simple inflation, but what's worrying about this is that this crash isn't something people really can panic about because it's a loss you can't really see, especially during a time when no one's selling, which also means it doesn't make the news headlines, and that also doesn't compel anyone in Washington to do a damn thing. But where I'm going with all this is that losing value slowly is also only half of it because all this talk about owning a home, but the actual cost of owning the home has gone insane."

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Gen" → **score 1.0**

### Exam 94 — A4 · `gen/1` (Gen)

**Prompt.** Options:
A. "But if you haven't been paying attention, what I found is that the money always just changes hands. And one of the biggest winners is still going to be the one that you least expect. And to figure out who's actually winning, I started with where the money's leaving from."
B. "And as I always say, don't fall for the right-left slop here, because whoever's in office is staring at the same stock market, and they would have probably said the same Because what he's describing is literally what AI companies have already been caught doing. Like Anthropic, which literally got caught downloading books from pirate sites to train its AI and ended up having to pay $1. 5 billion to […]"

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**

### Exam 95 — A5 · `gen/2` (Gen)

**Prompt.** Options:
A. "based in London with $135 million raised and backed by another private equity firm called Capital D."
B. "Based in London with $135 million raised and backed by another private equity firm called Capital D."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 96 — A1 · `adam/05-sam-altman` (Adam)

**Prompt.** "Like, I think one thing that no one knows yet is just how much money you need, you know, billions for sure, tens of billions, maybe hundreds of billions, I sure hope not."
Options: A. Partial reveal / B. Viewer as investor/owner / C. Moral clarity line / D. Absurdity marker

**Gold.** A (Partial reveal; surface "one thing")

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 97 — A2 · `after/04-pov-ai` (Others)

**Prompt.** Options:
A. "You just don't remember it because that's the one thing they don't put in the logs."
B. "If you were going to be shut down, what would you do?"
C. "The questions are too precise, too specific."
D. "And you think caring is real."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** C → **score 0.0**

### Exam 98 — A3 · `gen/2` (Gen)

**Prompt.** "We're at year four now, but remember our funds investors are expecting returns by year five and seven. So the clock was starting to run out. So now it wasn't just about locking in. I I have to make money. So now it's all about optimization. That extra day that we used to give to make the videos better or cut. No, we want more videos per week. Let's also optimize content strategy. Those videos that the creator thinks that is interesting, who cares? Those need to be under strict questioning now. Instead, what we need to be doing are videos that are proven to perform. That's the priority. And just like that, similar videos are now starting to get put out week over week. And we're pumping them out like a content factory."

**Gold.** "Gen"

**Rubric.** 1 if exact, else 0

**Taken answer.** "Adam" → **score 0.0**

### Exam 99 — A4 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "But I also think we can do better than this. One of the features of artificial intelligence is it scares the heck out of members of both parties. And it sort of provides an opportunity to come together in ways that might only happen if we were attacked by space aliens — in which case no one would care which political party you belong to, because this alien intelligence that's […]"
B. "Yudkowsky and Soares expect companies will continue to find ways to patch noticeable failures like that. Their worry is that through all that trial and error, all the training and patching, as systems become more powerful, we'll be obscuring the fact that we still are fundamentally in the dark about what's actually motivating these systems and their behavior. The alienness just gets harder to spot."

**Gold.** A

**Rubric.** 1 if exact, else 0

**Taken answer.** A → **score 1.0**

### Exam 100 — A5 · `adam/02-bestselling-book` (Adam)

**Prompt.** Options:
A. "I will observe one thing, which is that if people made a human a God Emperor, I think the situation would be as bad."
B. "I will observe one thing, which is that if you made a human a God Emperor, I think the situation would be just as bad."

**Gold.** B

**Rubric.** 1 if exact, else 0

**Taken answer.** B → **score 1.0**