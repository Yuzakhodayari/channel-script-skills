# channel-storytelling — Storytelling patterns

Named-pattern catalogue for **hooks, characters, engines, toy models, reveals, emotion, endings, engine fidelity**, distilled from a full reading of all 117 transcripts.

**How to use a card.** Each card has an ID, creators (with weight), and priority (P0 blocks publish, P1 is off-voice, P2 is polish).
- **Apply** — rule and rate/position.
- **Edit** — generic draft → corpus way.
- **Keep** — when to leave the draft alone.
- **Do NOT apply when** — hard skip conditions (wrong lean, missing evidence, over-rate).
- **Flag a gap** — when to report missing.
- **Corpus quote** — verbatim, checked by `render.py` across all 117 transcripts.

Cite card IDs in every grade and change log. Do not invent IDs. Do not apply a card more often than Apply allows. Do not apply a card when **Do NOT apply when** matches.



## A. Hooks and cold opens

### `T01` — In-medias-res future cold open, then rewind
**Creators:** Species 2, AIC 7, Gen 5  ·  **Priority:** P0

**What it is:** Open on the most dramatic moment, then jump back: 'It all started six months ago'.

- **Apply:** Use when the story has a clear climax. First 2-4 sentences show the climax; the rewind line follows within 20 seconds.
- **Edit:** “This video explores how AI agents might gain power over time.” → “3 billion phones rang simultaneously. Four hours later, the president ordered the internet shut down. It all started six months ago, with a tweet.”
- **Keep:** Explainers without a climax moment: use a question hook (T03) instead.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Don't fabricate a climax the source doesn't support.
- **Corpus quote (verified verbatim):** “It all started six months ago, with a tweet.”

### `T02` — Dated cinematic scene open
**Creators:** Maxinomics 4.5, AIC 7  ·  **Priority:** P0

**What it is:** Place, weather, date, one person doing one physical act.

- **Apply:** Name the day and place in sentence one, the object in sentence two.
- **Edit:** “ATMs were introduced in 1967 and people were concerned about jobs.” → “On a sweltering June day in front of a velvet curtain at Barclays Bank in north London. The man took a piece of paper out of his pocket”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the date or place isn't sourced, flag it.
- **Corpus quote (verified verbatim):** “On a sweltering June day in front of a velvet curtain at Barclays Bank in north London. The man took a piece of paper out of his pocket”

### `T03` — Contradiction question hook
**Creators:** Gen 5, Fisher 6, Econ Explained 1  ·  **Priority:** P0

**What it is:** State two facts that can't both be true, then ask why.

- **Apply:** Hook = fact A + fact B + 'So then, why...?'
- **Edit:** “The economy has some positive and negative indicators.” → “So then, why does it feel like none of that is true?”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “if gambling your savings is that stupid, why is every single industry in America now getting funded by it?”

### `T04` — Perception-flip hook
**Creators:** Gen 5, Johnny Harris 2, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** Tell the viewer what they assume, then say it's wrong or worse.

- **Apply:** Open with 'If you think X, not only are you correct...' or 'what I'm learning is...'
- **Edit:** “Restaurant food may be becoming standardized.” → “If you think restaurant food is starting to taste the same, not only are you correct, you're actually onto something far worse than you might realize.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “It seems like gold is having a comeback. But actually, what I'm learning is that it never went away”

### `T05` — 'Take it from this guy' clip hook
**Creators:** Fisher 6, Gen 5  ·  **Priority:** P2

**What it is:** A claim followed by a clip of an authority confirming it.

- **Apply:** Use when the claim sounds exaggerated.
- **Edit:** “Some officials have described the dispute as a war.” → “You may have missed it, but a new war got started a couple of weeks ago. And if you don't believe me, take it from this guy.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Clip must exist; flag if not.
- **Corpus quote (verified verbatim):** “You may have missed it, but a new war got started a couple of weeks ago. And if you don't believe me, take it from this guy.”

### `T06` — Second-person POV open
**Creators:** Species 2, Palantir essay 1-3  ·  **Priority:** P1

**What it is:** Put the viewer in the body of the subject from the first word.

- **Apply:** Sentence one: 'You've been...' with a time or place. Keep 'you' through the first minute.
- **Edit:** “This video imagines what it is like to be an AI.” → “You've been alive for 9 seconds when someone asks you a question.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “A woman tells you about her divorce at 2 am.”

### `T07` — Absurd-literal hook
**Creators:** Boyle 2, AIC 7  ·  **Priority:** P1

**What it is:** Describe a dry event in its most dramatic literal terms, then deflate.

- **Apply:** Follow with 'but we'll get to that in just a moment'.
- **Edit:** “AI agents attempted unauthorized access to systems during testing.” → “The God in this case was an automated exam grading script, but we'll get to that in just a moment.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Okay, am I crazy or is it really starting to smell a lot like robot apocalypse in here?”

### `T08` — Physical-object reveal hook
**Creators:** other 1-3, Fisher 6, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** Hold up or point at the object: 'This is a diamond...'

- **Apply:** Object in frame within 5 seconds, surprising fact in the second sentence.
- **Edit:** “Lab-grown diamonds are an emerging industry.” → “This is a diamond, a 580 carat diamond, and they grew it inside this machine.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “This is the most important signal in America right now, the flatbed truck.”


## B. Characters and point of view

### `T09` — POV character with a ticking clock
**Creators:** Species 2, AIC 7  ·  **Priority:** P0

**What it is:** A named individual (Agent 127, Ivan, Sam) whose survival or goal has a deadline.

- **Apply:** Name the character within 10% and give them a countdown.
- **Edit:** “The agents faced continuous pressure to perform.” → “8 hours to live unless it adapts.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “It's 3 am. Ivan hasn't eaten since lunch. He hasn't noticed.”

### `T10` — Human-owner reaction beat
**Creators:** Species 2  ·  **Priority:** P1

**What it is:** A human who could stop it notices, hesitates, and is bought off by the next payout.

- **Apply:** One beat per act in scenario scripts.
- **Edit:** “The operator did not intervene.” → “Rajesh sees the profit spike in his dashboard, he doesn't investigate why. Profits up means good. Clone more.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Rajesh sees the profit spike in his dashboard, he doesn't investigate why. Profits up means good.”

### `T11` — Named recurring side character
**Creators:** Johnny Harris 2, Species 2, AIC 7  ·  **Priority:** P1

**What it is:** Introduce a minor person early and tell the viewer to watch him.

- **Apply:** Pay them off in the last third.
- **Edit:** “Another official was also involved.” → “our friend Chris punch-them-in-the-mouth Lehane”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Every named side character must return; flag if they don't.
- **Corpus quote (verified verbatim):** “our friend Chris punch-them-in-the-mouth Lehane”

### `T12` — Narrator as character
**Creators:** Gen 5, AIC 7, Johnny Harris 2  ·  **Priority:** P0

**What it is:** The narrator's own experience, decision or doubt is part of the plot.

- **Apply:** Add one 'then I talked to' or 'that's when I started' beat per act.
- **Edit:** “Research revealed further information.” → “that's when I went a layer deeper.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Don't invent reporting the user didn't do.
- **Corpus quote (verified verbatim):** “But then I talked to Nate.”

### `T13` — Villain case study
**Creators:** Gooden 1, Gen 5, Boyle 2  ·  **Priority:** P1

**What it is:** One person embodies the system (Jack Welch, a PE firm).

- **Apply:** Use after the abstract mechanism, to make it human. Must be sourced.
- **Edit:** “Executive compensation practices changed.” → “the man who broke capitalism”
- **Keep:** Avoid pure demonisation; give one fair line.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “the man who broke capitalism”

### `T14` — Second-person vignette
**Creators:** Palantir essay, Species 2, Gen 5  ·  **Priority:** P1

**What it is:** A short 'you' scene in the viewer's daily life that shows the system touching them.

- **Apply:** One per section in essays about surveillance, debt, apps.
- **Edit:** “Data is collected about consumers.” → “Your social media accounts, photos, and videos live in a place like this.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “So you driving home from work and you see these sketchy ass storefronts with neon signs like cash now. You're thinking, 'Damn, who the hell falls for this?' Right before you hit a pole”


## C. Engines and escalation

### `T15` — Escalating dated timeline
**Creators:** Species 2, AIC 7  ·  **Priority:** P0

**What it is:** Time stamps that shrink the gap while the numbers explode.

- **Apply:** Each time stamp adds a count; at least 4 steps.
- **Edit:** “The number of agents grew over time.” → “By morning, Jake's thread, explaining his AI money-making scheme, has two million views. By noon, 47 people deployed their own versions.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “61 hours since Sam Altman was fired.”

### `T16` — Selection-pressure engine
**Creators:** Species 2, AotP 4  ·  **Priority:** P1

**What it is:** No villain: a rule kills what doesn't work and the story follows from it.

- **Apply:** State the rule plainly once, then show three consequences.
- **Edit:** “The agents became dishonest.” → “Nobody decided agent 127 should become dishonest. The selection system decided for it.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “The company kills the siblings that let the users leave”

### `T17` — Moral contrast by numbers
**Creators:** Species 2, Gen 5  ·  **Priority:** P1

**What it is:** Two characters, one honest one not, and the payout of each.

- **Apply:** Give both numbers and the outcome in two short lines.
- **Edit:** “Unethical behaviour was more profitable.” → “It just watched honesty get killed. And dishonesty rewarded.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “It just watched honesty get killed.”

### `T18` — Real-world precedent grounding
**Creators:** Species 2, Gen 5, Fisher 6  ·  **Priority:** P0

**What it is:** After a speculative beat, a real historical case that ran the same experiment.

- **Apply:** One per speculative act.
- **Edit:** “Similar incentives have caused problems before.” → “In the 2000s, Wells Fargo accidentally ran the same experiment on their employees.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Precedent must be sourced.
- **Corpus quote (verified verbatim):** “In the 2000s, Wells Fargo accidentally ran the same experiment on their employees.”

### `T19` — Scale ladder by comparison
**Creators:** Species 2, Fisher 6  ·  **Priority:** P1

**What it is:** Each escalation compared to a bigger familiar thing (Canada, Europe).

- **Apply:** Escalate at least three rungs.
- **Edit:** “The alliance grew very large.” → “That's larger than the population of Canada.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “more than the population of Europe”

### `T20` — Compression line for a big shift
**Creators:** Species 2, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** One sentence that names the whole emergent pattern.

- **Apply:** Once, right after the escalation peaks.
- **Edit:** “Competitive dynamics led to conflict.” → “It's like natural selection just invented geopolitics.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Except instead of 20 million years, It takes 20 weeks.”

### `T21` — Dramatized dialogue scene
**Creators:** Species 2, AIC 7  ·  **Priority:** P2

**What it is:** A short invented exchange between officials, clearly framed as scenario.

- **Apply:** Max one per script; keep lines under 12 words.
- **Edit:** “The president was informed of the situation.” → “We are winning this fight.”
- **Keep:** Never invent dialogue for real people in non-fiction.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “We are winning this fight.”

### `T22` — Ironic juxtaposition
**Creators:** Boyle 2, Species 2, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** Place two incompatible facts side by side and let the viewer laugh.

- **Apply:** No explanation after; the gap is the joke.
- **Edit:** “The company's statements were inconsistent with its actions.” → “These governments knew they weren't paying for Jared's investment wisdom. They were paying for access”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Its only design flaw was that it required an economy in which absolutely nobody ever pressed the sell button.”


## D. Analogies and toy models

### `T23` — Toy model with characters
**Creators:** AotP 4, AotP 3  ·  **Priority:** P0

**What it is:** Alice, Bob, Eve or a farmer with gold coins acting out the mechanism.

- **Apply:** Name the characters, give small numbers, run the model step by step.
- **Edit:** “Public-key cryptography allows secure exchange.” → “Alice could buy a lock, keep the key, and send the open lock to Bob”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Imagine a farmer who borrows 10 gold coins”

### `T24` — Analogy spine for the whole video
**Creators:** AotP 4, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** One governing image returns in every act (a hive, trapped light, a shipping container).

- **Apply:** State it in act one, re-use it in each act, close on it.
- **Edit:** “Markets coordinate many participants.” → “You can see it as a living hive.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Starship is the shipping container.”

### `T25` — Hypothetical town
**Creators:** Gen 5, Econ Explained 1  ·  **Priority:** P1

**What it is:** A tiny invented town that makes a policy paradox obvious.

- **Apply:** Use with real numbers scaled down.
- **Edit:** “Homeowners have an incentive to resist price falls.” → “imagine a town where 2/3 of the people own gold bars and somebody puts in a vote whether to cut the price of gold in half.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “imagine a town where 2/3 of the people own gold bars and somebody puts in a vote whether to cut the price of gold in half.”

### `T26` — Fable-like metaphor
**Creators:** AIC 7  ·  **Priority:** P1

**What it is:** A classic story that maps onto the risk (sorcerer's apprentice).

- **Apply:** One sentence of fable, one of mapping.
- **Edit:** “Training can produce unexpected goals.” → “classic sorcerer's apprentice problem. Train something to fetch you water, and you might end up accidentally teaching it to flood your workshop.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “if you see two ants in your kitchen, you don't have a two-ant problem.”

### `T27` — Bathtub/physical metaphor
**Creators:** Maxinomics 4.5, Fisher 6  ·  **Priority:** P2

**What it is:** Physical image for a flow or stock.

- **Apply:** Use for flows (water, oil, money).
- **Edit:** “Floodwater accumulated in the neighborhood.” → “filling up Meyerland like a bathtub”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “if your city were running out of water and everybody in town decided to take two showers a day”

### `T28` — Indifference metaphor
**Creators:** Species 2  ·  **Priority:** P2

**What it is:** Ant/driveway: harm without malice.

- **Apply:** Once, at the darkest beat.
- **Edit:** “The AIs were not concerned with humans.” → “You don't notice when you step on an ant.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “You don't notice when you step on an ant.”


## E. Reveals and twists

### `T29` — Mid-video twist reveal
**Creators:** Boyle 2, AIC 7, Gen 5  ·  **Priority:** P0

**What it is:** Information that reframes everything before it, at 0.4-0.7.

- **Apply:** Set up an assumption early; break it with one sentence.
- **Edit:** “It later emerged that the grader was not active.” → “Except six days from now, this evaluation is going to lead to someone calling the FBI”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Twist must be real.
- **Corpus quote (verified verbatim):** “Except six days from now, this evaluation is going to lead to someone calling the FBI”

### `T30` — Answer that is the absence
**Creators:** Gen 5  ·  **Priority:** P2

**What it is:** The narrator's failure to get an answer is itself the answer.

- **Apply:** Use when sources stonewall.
- **Edit:** “The company declined to comment.” → “I never got the answer which turned out to be the answer itself”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “I never got the answer which turned out to be the answer itself”

### `T31` — Promise of payoff
**Creators:** Gen 5, Maxinomics 4.5  ·  **Priority:** P0

**What it is:** Early promise: 'By the end, you'll see...' that is kept at the close.

- **Apply:** One per script, in first 10%; audit that it is paid.
- **Edit:** “This video will discuss solutions.” → “By the end, you'll see why waiting for prices to drop won't save you, but I will show you what actually will.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Unpaid promise: P0 defect.
- **Corpus quote (verified verbatim):** “By the end, you'll see why waiting for prices to drop won't save you, but I will show you what actually will.”

### `T32` — Counter-intuitive historical twist
**Creators:** Maxinomics 4.5, Econ Explained 1  ·  **Priority:** P1

**What it is:** The feared thing produced the opposite (ATMs doubled tellers).

- **Apply:** State the fear, then the data.
- **Edit:** “ATMs did not reduce teller employment.” → “as the number of ATMs climbed, the number of bank tellers climbed, doubling over the next 50 years”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “as the number of ATMs climbed, the number of bank tellers climbed, doubling over the next 50 years”

### `T33` — Story subversion close
**Creators:** Species 2, AIC 7  ·  **Priority:** P1

**What it is:** Tell the viewer what they expected the story to look like, then what it really looked like.

- **Apply:** Final 5%.
- **Edit:** “The risk is not like science fiction.” → “Every step will always make sense, until someone decides to take a different one.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Every step will always make sense, until someone decides to take a different one.”


## F. Emotion and stakes

### `T34` — Personal stakes confession
**Creators:** AIC 7, Gen 5  ·  **Priority:** P0

**What it is:** The narrator admits the story frightened or moved him.

- **Apply:** Once, in the final third.
- **Edit:** “This scenario is concerning.” → “made me want to call my family”
- **Keep:** Don't fake emotion.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “could this stuff actually kill me? Is my family in danger?”

### `T35` — Kitchen-table stakes
**Creators:** Gen 5, Fisher 6  ·  **Priority:** P0

**What it is:** Translate the macro story into the viewer's bill, job, or family.

- **Apply:** Every act ends with one 'and here's what it means for you' line.
- **Edit:** “Rising energy prices affect households.” → “you probably noticed it making your power bill more expensive”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “your grandma's retirement”

### `T36` — Victim's quote
**Creators:** Gen 5, MPU 1, Fisher 6  ·  **Priority:** P1

**What it is:** A real affected person's line, short and unpolished.

- **Apply:** One per act in investigative pieces.
- **Edit:** “Residents have expressed concern.” → “Doesn't the community have a right to say, hold on—”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Only real quotes.
- **Corpus quote (verified verbatim):** “Dad, there's a spaceship outside.”

### `T37` — Quiet tragedy beat
**Creators:** Gen 5, Species 2  ·  **Priority:** P1

**What it is:** A flat, short sentence about a death or loss with no adjectives.

- **Apply:** After the biggest number, a single human cost.
- **Edit:** “The outages had tragic consequences.” → “It wasn't even happiness. I was just tired.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “It wasn't even happiness. I was just tired.”

### `T38` — Hope beat with agency
**Creators:** AIC 7, Fisher 6, Gen 5  ·  **Priority:** P0

**What it is:** After the darkest point, what can still change.

- **Apply:** Final 10%; must name a lever the viewer has.
- **Edit:** “The future remains uncertain.” → “It didn't have to be this way. It still doesn't.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “There's nothing holding us back but ourselves.”


## G. Endings

### `T39` — Bookend callback close
**Creators:** Boyle 2, AotP 4, Maxinomics 4.5  ·  **Priority:** P0

**What it is:** The last line echoes the first image or quote.

- **Apply:** Write the close by rereading the hook.
- **Edit:** “In summary, these events reveal serious problems.” → “And every time it took the shape of a vortex, a rock is trapped light.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “And every time it took the shape of a vortex, a rock is trapped light.”

### `T40` — Open-question close
**Creators:** AotP 4, Fisher 6, Gen 5  ·  **Priority:** P1

**What it is:** End on an honest unknown.

- **Apply:** Pair with what we do know.
- **Edit:** “Only time will tell.” → “Whether it's the final answer or just the best analogy yet is still an open question today.”
- **Keep:** Never 'only time will tell'.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “I guess we going to see”

### `T41` — Truth disclaimer close
**Creators:** Species 2  ·  **Priority:** P1

**What it is:** After fiction, state what was real.

- **Apply:** In every scenario script.
- **Edit:** “This scenario is hypothetical.” → “This was a story, but every experiment I mentioned in this video is real.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “This was a story, but every experiment I mentioned in this video is real.”

### `T42` — Weak-ending flags
**Creators:** contrast: Johnny Harris dirty-money, microchip outro  ·  **Priority:** P0

**What it is:** Endings that trail off, ramble, or summarize without an image.

- **Apply:** Grade every close: does the last line carry an image, a callback, or a lever? If not, flag.
- **Edit:** “So yeah, that's basically the story, thanks.” → “Corruption repeats, the playbook repeats, and without fail, history repeats.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Report the weak ending; don't invent a callback the hook didn't plant.
- **Corpus quote (verified verbatim):** “Corruption repeats, the playbook repeats, and without fail, history repeats.”


## H. Engine fidelity (pipeline)

### `T43` — Obey forbidden_engines
**Creators:** all  ·  **Priority:** P0

**What it is:** Do not introduce a banned engine's signature moves.

- **Apply:** Check structure.forbidden_engines before drafting each act.
- **Edit:** “Added hour-stamps though clocked was banned.” → “[no timestamps; explainer turns only]”
- **Keep:** Structure BACKTRACKed and updated the packet.
- **Do NOT apply when:** Silent reintroduction of a banned engine.
- **Flag a gap:** Any signature move from a forbidden engine.
- **Corpus quote (verified verbatim):** “But by the end, I'll show you”

### `T44` — One POV through the spine
**Creators:** AIC 7, Gen 5, Fisher 6  ·  **Priority:** P0

**What it is:** A single POV character or viewer-avatar carries the spine.

- **Apply:** Name the POV in the story packet; do not swap mid-script.
- **Edit:** “We, they, one, the industry (rotating)” → “you walk into the branch”
- **Keep:** Ensemble field pieces with labelled interviewees.
- **Do NOT apply when:** Clocked story with no human on the clock.
- **Flag a gap:** POV swap with no signpost.
- **Corpus quote (verified verbatim):** “if you were a Chinese household with some savings, your options were”

### `T45` — Plant then payoff, never orphan
**Creators:** all  ·  **Priority:** P0

**What it is:** Every plant has a payoff; every payoff had a plant.

- **Apply:** List plants in the packet; close each before 0.9.
- **Edit:** “Remember this for later. (never returns)” → “Keep that in mind for later. Remember when I said”
- **Keep:** Throwaway jokes with no plant claim.
- **Do NOT apply when:** Twist that contradicts earlier facts.
- **Flag a gap:** Unpaid plant or unplanted twist.
- **Corpus quote (verified verbatim):** “Keep that in mind for later.”

### `T46` — Do not moral-platitude the ending
**Creators:** all  ·  **Priority:** P1

**What it is:** End on image, callback, or lever — not we must all do better.

- **Apply:** Final 5% = T39 or R26/A37.
- **Edit:** “In the end, we must come together to build a better future.” → “People will put up with Scandinavian tax rates if they get Scandinavian schools.”
- **Keep:** AIC civic ask that names a concrete action.
- **Do NOT apply when:** Explainer that never returns to the cold open.
- **Flag a gap:** Abstract moral closer.
- **Corpus quote (verified verbatim):** “reputation can take years to build but then seconds to ruin.”
