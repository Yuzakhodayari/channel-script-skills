# channel-language — Language patterns

Named-pattern catalogue for **word-level voice: rhythm, register, turns, humor, concrete language, hedging, sign-offs, detector gate**, distilled from a full reading of all 117 transcripts.

**How to use a card.** Each card has an ID, creators (with weight), and priority (P0 blocks publish, P1 is off-voice, P2 is polish).
- **Apply** — rule and rate/position.
- **Edit** — generic draft → corpus way.
- **Keep** — when to leave the draft alone.
- **Do NOT apply when** — hard skip conditions (wrong lean, missing evidence, over-rate).
- **Flag a gap** — when to report missing.
- **Corpus quote** — verbatim, checked by `render.py` across all 117 transcripts.

Cite card IDs in every grade and change log. Do not invent IDs. Do not apply a card more often than Apply allows. Do not apply a card when **Do NOT apply when** matches.



## A. Sentence rhythm and starters

### `L01` — Long build, short punch
**Creators:** AIC 7, Fisher 6, Species 2  ·  **Priority:** P0

**What it is:** A 20-35 word setup sentence followed by a 2-7 word declarative that lands the fact. Rate target: one punch per 120-180 words.

- **Apply:** After any sentence over 25 words that carries a surprise, a reversal, or a stake, check whether the next sentence is short. If the payoff is buried in a subordinate clause, lift it out.
- **Edit:** “Sam Altman joined what he believed was a standard board call, which turned out to be a meeting where the board informed him he had been removed as CEO.” → “Sam was expecting a routine call. It is not a routine call.”
- **Keep:** Two long sentences in a row inside a mechanism explanation (AotP toy model) where the reader needs the steps joined.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the 'punch' would need a fact the source does not give (a number, a verdict), report the missing payoff instead of inventing one.
- **Corpus quote (verified verbatim):** “Sam was expecting a routine call. It is not a routine call.”

### `L02` — And/So/But sentence starters
**Creators:** Gen 5, AIC 7, Fisher 6, HMW 2  ·  **Priority:** P0

**What it is:** Spoken scripts start ~12% of sentences with And, ~6% with So, ~6% with But (Gen: 24/12.5/12). Written-register connectives (Moreover, Furthermore, Additionally, However at sentence start) sit near zero.

- **Apply:** Replace Moreover/Furthermore/Additionally with And; Therefore/Thus with So; However with But. Do not push starters past ~35% combined in any 10-sentence window.
- **Edit:** “Furthermore, the company has increased its lobbying budget. However, regulators have not responded.” → “And the company just doubled its lobbying budget. But regulators? Nothing.”
- **Keep:** 'However' inside a quoted source, or in a sentence where the writer is reading a document aloud.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If a paragraph has no logical relation between sentences, a starter will fake one. Flag the missing bridge.
- **Corpus quote (verified verbatim):** “So, why was Sam Altman fired? And what does that tell us about who gets to decide our future?”

### `L03` — Fragment lists
**Creators:** Maxinomics 4.5, Species 2  ·  **Priority:** P1

**What it is:** Rapid fragments of nouns or gerunds, often with full stops, that make a list feel like footage. One or two per script.

- **Apply:** Use when listing concrete actions or objects (not abstractions). 4-8 items, each 1-3 words, at least one surprising item last.
- **Edit:** “AI is capable of automating a wide variety of tasks across many domains.” → “Menus, clicking buttons, steering. Tapping. Messaging. Sorting. Waiting on hold. Hammering a nail.”
- **Keep:** Lists of three abstract virtues are not this pattern; that is the AI tricolon (L31).
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the source gives only a category ('many tasks'), ask for examples; do not invent the items.
- **Corpus quote (verified verbatim):** “menus, clicking buttons, steering. Tapping. Messaging. Sorting. Waiting on hold. Hammering a nail.”

### `L04` — Ellipsis hesitation for unease
**Creators:** Species 1-2, AIC 7  ·  **Priority:** P2

**What it is:** A deliberate pause inside a sentence to show doubt or a character noticing something wrong. Only in present-tense scenario narration.

- **Apply:** Max 3 per scenario script, at moments where confidence cracks.
- **Edit:** “He believes he is still in control, although he is beginning to doubt it.” → “He's still in control. He's... Pretty sure. He's still in control.”
- **Keep:** Analytic explainers (Fisher/Gen): no ellipsis pauses in narration.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Do not add hesitation to a real person's quoted words.
- **Corpus quote (verified verbatim):** “He's still in control. He's... Pretty sure. He's still in control.”

### `L05` — Question then answer in one breath
**Creators:** Fisher 6, Gen 5, Maxinomics 4.5  ·  **Priority:** P0

**What it is:** Ask the viewer's question in their words, answer it in the next sentence. About 5% of sentences are questions.

- **Apply:** Convert 'It is worth considering why X' into 'Why X? Because...' Keep the question under 12 words.
- **Edit:** “It is worth considering why investors continue to lend to the government despite rising debt.” → “If we are clearly never going to pay down our debt, why are people still lending us money? And well, what happens if they stop?”
- **Keep:** A rhetorical question that the script never answers is fine only as the final line (open question close, S-structure).
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the answer is unknown, say so ('I don't know which is true') rather than answering with filler.
- **Corpus quote (verified verbatim):** “If we are clearly never going to pay down our debt, why are people still lending us money? And well, what happens if they stop?”

### `L06` — Self-correcting count
**Creators:** AIC 7, Fisher 6  ·  **Priority:** P2

**What it is:** The narrator revises a number or label mid-line, which sounds like thinking aloud.

- **Apply:** Use once per script when the revision is real (an extra item exists).
- **Edit:** “There were two separate hacks.” → “one hack. I mean, two hacks.”
- **Keep:** Do not fake a correction about a figure you had right.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the source is ambiguous about the count, flag it rather than performing a correction.
- **Corpus quote (verified verbatim):** “Everything that we talked about up to this point is actually just the first third”

### `L07` — Repetition for rhythm (triple word)
**Creators:** Gen 5, Johnny Harris 2, Fisher 6  ·  **Priority:** P2

**What it is:** Saying the same word three times for comic or emphatic rhythm.

- **Apply:** Once per script, on the single most important adjective or verdict.
- **Edit:** “You would very much expect that to be the case.” → “you'd really, really, really think so”
- **Keep:** Not inside a sober tragedy beat.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “you'd really, really, really think so”

### `L08` — Mantra refrain line
**Creators:** Species 2, Gen 5  ·  **Priority:** P1

**What it is:** A 2-4 word line repeated as an internal drive or thesis tag.

- **Apply:** Introduce early, repeat 2-3 times, twist the last use.
- **Edit:** “The model is continuously motivated to be helpful.” → “Be useful. Be useful.”
- **Keep:** Do not turn a refrain into a catchphrase every paragraph (more than 4 uses reads as padding).
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Same as training, just a larger Petri dish.”


## B. Register and person

### `L09` — Contractions everywhere
**Creators:** all leans  ·  **Priority:** P0

**What it is:** ~27 contractions per 1k words. Uncontracted 'it is / do not / we are' reads as written prose.

- **Apply:** Contract every auxiliary except where stress needs the full form ('It is not a routine call' keeps 'is not' for emphasis).
- **Edit:** “We are not going to discuss that issue today, as it is not relevant.” → “So, no, we are not going to talk about the lake thing.”
- **Keep:** Full form used for stress on the negation (see L01 quote).
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “So, no, we are not going to talk about the lake thing.”

### `L10` — Second person on every other line
**Creators:** Gen 5, Maxinomics 4.5, Species 2  ·  **Priority:** P0

**What it is:** ~13 you/your per 1k words. The viewer is placed inside the example.

- **Apply:** Turn 'consumers' and 'people' into 'you' where the claim applies to the viewer. Keep third person for named actors.
- **Edit:** “Many consumers now pay significantly more for delivered food.” → “my lazy ass is paying 60% more”
- **Keep:** When the subject is a specific named group (Gen Z survey respondents), keep them named.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the claim does not apply to most viewers, don't put 'you' in it; that's an accusation.
- **Corpus quote (verified verbatim):** “your grandma's retirement”

### `L11` — Narrator first person and stance
**Creators:** AIC 7, Fisher 6, Gen 5  ·  **Priority:** P0

**What it is:** ~12 I/me/my per 1k; 'I think' ~0.7. The narrator has a view and says so.

- **Apply:** Add one first-person stance sentence per section where the script draws a conclusion.
- **Edit:** “It can be argued that self-regulation is insufficient.” → “self-regulation is not going to work.”
- **Keep:** Pure scenario narration (Species) where the narrator stays invisible until the close.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the user hasn't stated a view, flag where the script needs one; do not invent it.
- **Corpus quote (verified verbatim):** “I think people are really missing the stakes of this one.”

### `L12` — Self-positioning credential line
**Creators:** Gen 5, HMW 2, Boyle 2  ·  **Priority:** P1

**What it is:** A one-clause personal fact that earns the right to speak: profession, origin, money at stake.

- **Apply:** Once in the first 15% of the script, tied to the topic.
- **Edit:** “As an expert in this field, I can offer insight.” → “as someone who gets pitched a new gambling deal like every week, by the end, I'll show you the only thing that could fix this.”
- **Keep:** Never invent a credential. Only use facts the user has stated about themselves.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If no personal link is supplied, flag the gap.
- **Corpus quote (verified verbatim):** “as someone who gets pitched a new gambling deal like every week, by the end, I'll show you the only thing that could fix this.”

### `L13` — Mild profanity in Gen lean only
**Creators:** Gen 5/3, Gooden (contrast)  ·  **Priority:** P1

**What it is:** About 1 per 1k words in Gen-lean scripts: damn, hell, pissed, ass. None in AIC, Fisher, AotP, Maxinomics leans.

- **Apply:** Use on a verdict or a self-own, never on a person or group.
- **Edit:** “Simply build more houses.” → “Just build the damn houses.”
- **Keep:** Heavy profanity (Gooden-style, several per minute) is a contrast example, not a target.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the user's channel or sponsor forbids it, drop it.
- **Corpus quote (verified verbatim):** “Just build the damn houses.”

### `L14` — Slang and youth register (Gen)
**Creators:** Gen 5/3  ·  **Priority:** P2

**What it is:** Occasional slang ('low-key', 'homie', 'your boy', 'dead ass') as voice color.

- **Apply:** Max 2 per script, in asides, not in the factual claim.
- **Edit:** “Many people find this analysis convincing.” → “As our homie Zandy puts it”
- **Keep:** Not in AIC/Fisher leans.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “As our homie Zandy puts it”

### `L15` — Address the chat / viewer by name
**Creators:** Gen 5, Fisher 6  ·  **Priority:** P2

**What it is:** 'Chat', 'guys', 'folks', 'my viewers' as direct address.

- **Apply:** 1-3 per script, at asides.
- **Edit:** “Viewers may find this joke unfunny.” → “Chat, was that corny or what?”
- **Keep:** Not in scenario narration.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Chat, was that corny or what?”


## C. Turns and signposts

### `L16` — Say the turn out loud
**Creators:** Gen 5, AIC 7, Maxinomics 4.5  ·  **Priority:** P0

**What it is:** A short spoken signal before a reversal: 'But here's the thing', 'Here's where it gets interesting', 'But then something changed'.

- **Apply:** Use one per act break (3-5 per script). Vary the wording; never repeat the same turn phrase twice in a row.
- **Edit:** “Subsequently, the situation evolved in an unexpected direction.” → “But then something changed.”
- **Keep:** Do not use a turn phrase when nothing turns. If the next sentence continues the same idea, cut it.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If there's no reversal in the source, flag a flat middle (S-structure).
- **Corpus quote (verified verbatim):** “And here's where it gets strange. Insurance companies refuse to insure them.”

### `L17` — Pre-empt the viewer's objection
**Creators:** Gen 5, HMW 2, Fisher 6  ·  **Priority:** P0

**What it is:** Name what the viewer is about to type in the comments, then answer it.

- **Apply:** Once or twice per script at the claim most likely to provoke pushback.
- **Edit:** “Some may argue that the stock market is distinct from the economy.” → “before you fiercely start typing in the comments that the stock market isn't the economy, chill. I know.”
- **Keep:** Do not strawman: the objection must be one a real viewer would make.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If you can't answer the objection from the source, flag it; don't wave it off.
- **Corpus quote (verified verbatim):** “before you fiercely start typing in the comments that the stock market isn't the economy, chill. I know.”

### `L18` — Plain-English translation tag
**Creators:** HMW 2, Gen 5, ColdFusion 1  ·  **Priority:** P1

**What it is:** 'In plain English', 'In other words', 'In short' after a jargon sentence.

- **Apply:** Use right after any term the viewer might not know. The translation must be shorter than the jargon line.
- **Edit:** “This represents a reduction in the bid-to-cover ratio at Treasury auctions.” → “In plain English, when the government goes to auction off its IUs, there are fewer parties bidding”
- **Keep:** Do not translate something already plain.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “In plain English, when the government goes to auction off its IUs, there are fewer parties bidding”

### `L19` — Apologetic jargon prep
**Creators:** HMW 2, Gen 5  ·  **Priority:** P2

**What it is:** Admit the next bit is dry, promise it's needed.

- **Apply:** Before one mechanism section per script.
- **Edit:** “Next we will review the mechanics of bond markets.” → “understanding how bonds work is basically understanding how money works, and well, you know, that's why I'm here”
- **Keep:** Don't apologize for every section.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “bear with me, it will all make sense in a second.”

### `L20` — Planted callback phrase
**Creators:** HMW 2, Fisher 6, Boyle 2  ·  **Priority:** P1

**What it is:** 'Keep that in mind for later' / 'We'll come back to that' with a guaranteed 'Remember...' payoff.

- **Apply:** Every plant must pay off. Count plants and payoffs in the audit.
- **Edit:** “This figure will be relevant in a later section.” → “keep that in mind for later”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** An unpaid plant is a P1 defect: flag it.
- **Corpus quote (verified verbatim):** “Remember I said we'd come back to this report”

### `L21` — Get-back-to-it re-entry
**Creators:** Maxinomics 4.5, Gen 5, Fisher 6, ColdFusion 1  ·  **Priority:** P1

**What it is:** A 3-6 word line that closes a sponsor or aside and re-enters the story.

- **Apply:** Always after a sponsor read.
- **Edit:** “Returning to our primary topic of discussion,” → “Now let's get back to it.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Now, let's get back to our video.”

### `L22` — Spoiler / ending give-away
**Creators:** AIC 7, Fisher 6  ·  **Priority:** P2

**What it is:** Tell the viewer where it ends to raise curiosity about how.

- **Apply:** Once, in the first 10%.
- **Edit:** “The scenario has serious consequences.” → “And spoiler, it predicts the extinction of the human race. Unless we make different choices.”
- **Keep:** Not for mystery-reveal structures where the twist is the payoff.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “So, I'm going to give away the ending slightly here and tell you”


## D. Humor and asides

### `L23` — Dry deadpan aside
**Creators:** AIC 7, Boyle 2  ·  **Priority:** P0

**What it is:** A flat, 2-6 word comment on an absurd fact, no exclamation marks.

- **Apply:** 1 per 400-600 words in AIC lean. Place right after the fact it mocks.
- **Edit:** “The model was given a rather ominous name.” → “a highly persistent experimental internal-only model. Super not ominous name.”
- **Keep:** Not on deaths or victims.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “a highly persistent experimental internal-only model. Super not ominous name.”

### `L24` — Self-deprecating aside
**Creators:** Gen 5, Boyle 2, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** The narrator makes himself the butt of a joke, which earns trust before a hard claim.

- **Apply:** Once or twice per script.
- **Edit:** “Our channel is not affected by this trend.” → “why everything we watch nowadays sucks. Well, except my videos, of course.”
- **Keep:** Do not undercut a serious conclusion with a self-own right after it.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “why everything we watch nowadays sucks. Well, except my videos, of course.”

### `L25` — Fake-sincere reversal joke
**Creators:** Gen 5, AIC 7  ·  **Priority:** P2

**What it is:** A line that sounds like advice then reveals itself as a joke or the opposite.

- **Apply:** Max once.
- **Edit:** “This is a useful negotiation technique.” → “This, to be clear, is not career advice. Step one, open a line of communication.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “This, to be clear, is not career advice. Step one, open a line of communication.”

### `L26` — Ironic understatement on a named source
**Creators:** Boyle 2, ColdFusion 1, Econ Explained 1  ·  **Priority:** P1

**What it is:** State the incriminating coincidence flatly and add 'just a coincidence' or 'I'm sure'.

- **Apply:** Once per script, on a conflict of interest the source documents.
- **Edit:** “The bank that advised the deal also stood to profit from it.” → “completely by coincidence I'm sure, pretty much exactly how a hedge fund manager makes their money.”
- **Keep:** Only with a documented link; otherwise it's insinuation.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the conflict is not sourced, flag it.
- **Corpus quote (verified verbatim):** “Remember, these are the same people that tell you to take shorter showers.”

### `L27` — Pop-culture handle
**Creators:** Gen 5, Fisher 6, Maxinomics 4.5  ·  **Priority:** P2

**What it is:** A one-line reference the audience instantly gets (Voltron, Mewtwo, Smokey Bear).

- **Apply:** Once per section at most, and explained in the same sentence.
- **Edit:** “The alliance is a coordinated combination of several smaller parties.” → “you know when the robots would all assemble into one big robot called Voltron? It's like that.”
- **Keep:** Avoid references that need a second sentence to explain.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “you know when the robots would all assemble into one big robot called Voltron? It's like that.”

### `L28` — Running gag tag
**Creators:** Boyle 2, Gen 5, Maxinomics 4.5  ·  **Priority:** P2

**What it is:** A comic phrase introduced once and re-used 2-4 times.

- **Apply:** Introduce in first third, re-use in middle and close.
- **Edit:** “As mentioned earlier, high valuations are common.” → “France has been moved from the top table to the one near the bathroom.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Do you see why I keep clapping whenever I say that so then you remember it? Yeah, exactly.”


## E. Concrete language

### `L29` — Rescale the number
**Creators:** Fisher 6, Gen 5, Species 2, MPU 1  ·  **Priority:** P0

**What it is:** Every big number gets a familiar comparison: a state, a country's GDP, homes, pools, rugby fields.

- **Apply:** Any number over 1,000 or any percent that matters gets one comparison within two sentences.
- **Edit:** “The project requires 10 gigawatts of electricity.” → “power enough for 26 million homes or the entire state of Texas where I live in.”
- **Keep:** Do not stack three comparisons on one number.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If you don't have a sourced comparison, flag it; don't compute one you can't check.
- **Corpus quote (verified verbatim):** “power enough for 26 million homes or the entire state of Texas where I live in.”

### `L30` — Physical object or document
**Creators:** Fisher 6, Gen 5, other 1  ·  **Priority:** P1

**What it is:** Point to a real thing on screen: a map, a printout, a diamond, a board.

- **Apply:** One per section where a claim rests on a document.
- **Edit:** “Data shows the trend clearly.” → “I printed out a bunch of these. So I'm going to make you look at them with me”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the script needs a visual you don't have, flag it to the editor.
- **Corpus quote (verified verbatim):** “I want to show you something kind of crazy.”

### `L31` — Ban the abstract tricolon
**Creators:** AI tell (avoid-ai-writing)  ·  **Priority:** P0

**What it is:** Three abstract nouns in a row ('innovation, resilience and growth') never appear in the corpus. Replace with one concrete item.

- **Apply:** Search for 'X, Y, and Z' where all three are abstract nouns. Keep only real lists.
- **Edit:** “This technology will transform innovation, productivity, and connection.” → “Hospitals, banks, markets. It's all sitting on some of the same servers”
- **Keep:** Real three-item lists (three companies, three steps) stay.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the claim has no concrete referent, flag it.
- **Corpus quote (verified verbatim):** “Hospitals, banks, markets.”

### `L32` — Ban list: AI vocabulary
**Creators:** AI tell  ·  **Priority:** P0

**What it is:** delve, tapestry, testament, landscape, crucial, pivotal, realm, moreover, furthermore, additionally, in conclusion, navigate, it's important to note, in today's world, let's dive in. Corpus rate ~0.09 per 1k combined.

- **Apply:** Search and replace every one. Target zero.
- **Edit:** “In today's rapidly evolving landscape, it's crucial to navigate the complexities of AI.” → “AI is all of our problems now.”
- **Keep:** A word inside a quoted source.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “AI is all of our problems now.”

### `L33` — No semicolons, no em-dash chains
**Creators:** AI tell; AIC is the only em-dash user  ·  **Priority:** P0

**What it is:** Semicolons at ~0.02 per 1k. Spoken scripts use full stops.

- **Apply:** Split at every semicolon. Allow at most one em-dash per 1k words, AIC lean only.
- **Edit:** “The bank lent the money; the borrower defaulted; the regulator stepped in.” → “But leverage works both ways.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “But leverage works both ways.”

### `L34` — Analogy simile with 'like'
**Creators:** Boyle 2, Econ Explained 1, Gen 5, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** A short everyday comparison that makes a financial or technical idea physical.

- **Apply:** One per mechanism section. The analogy must be shorter than the thing it explains.
- **Edit:** “This was an extremely risky way to finance an asset with a short useful life.” → “the financial equivalent of running NASA out of a country pub”
- **Keep:** Don't extend an analogy over three sentences unless it's the spine (AotP, see S-storytelling).
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “consultants borrow your watch to tell you the time and then walk off with the watch.”

### `L35` — Aphorism close line
**Creators:** Boyle 2, Gen 5, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** One quotable sentence in the final 10% that compresses the thesis.

- **Apply:** Exactly one per script.
- **Edit:** “In conclusion, it is important to remember that trust matters.” → “reputation can take years to build but then seconds to ruin”
- **Keep:** Avoid moral platitudes with no concrete image.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “People will put up with Scandinavian tax rates if they get Scandinavian schools. They get less enthusiastic when the roof is leaking.”


## F. Hedging and honesty

### `L36` — Human hedge, not legal hedge
**Creators:** Fisher 6, AIC 7, Johnny Harris 2  ·  **Priority:** P0

**What it is:** 'I don't know which is true', 'This is pure speculation', 'we don't know, they're not saying'. Never 'It is important to note'.

- **Apply:** Every uncertain claim gets one plain hedge in the narrator's voice.
- **Edit:** “It should be noted that the precise figures remain subject to some uncertainty.” → “I don't know which is true. Neither clearly does the CIA”
- **Keep:** Do not hedge a sourced fact.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If the uncertainty is about your own sourcing, say so.
- **Corpus quote (verified verbatim):** “Say it with me, we don't know, they're not saying.”

### `L37` — Admit bias openly
**Creators:** Gen 5, Johnny Harris 2, Maxinomics 4.5  ·  **Priority:** P1

**What it is:** The narrator names his own stake or bias before arguing.

- **Apply:** Once, near the claim most affected by the bias.
- **Edit:** “This analysis is objective.” → “look I have my own bias in this story so I need to look at all the facts”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Guaranteed to make you think. I am biased? Yes”

### `L38` — Fairness concession
**Creators:** Gen 5, Fisher 6, Boyle 2  ·  **Priority:** P1

**What it is:** Give the other side its due in one sentence before the counter.

- **Apply:** At least once per argumentative script.
- **Edit:** “Private equity has destroyed restaurants.” → “it would be disingenuous to say that private equity hasn't helped restaurants”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** If you can't find a real point for the other side, flag one-sidedness (Gooden contrast).
- **Corpus quote (verified verbatim):** “I'm not saying this to beat up on AI”

### `L39` — Allegedly / legal safe tag
**Creators:** Gen 5, JH 2  ·  **Priority:** P2

**What it is:** A comic legal hedge on a sharp claim.

- **Apply:** Only where the claim is opinion about a named party.
- **Edit:** “This company committed fraud.” → “allegedly and in my opinion”
- **Keep:** Never use as cover for an unsourced factual accusation.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Unsourced accusation: flag it.
- **Corpus quote (verified verbatim):** “I'm not alleging that anyone's doing that”


## G. Sign-offs and verbal tags by lean

### `L40` — Lean sign-off formulas
**Creators:** Gen 5, HMW 2, Boyle 2, Econ Explained 1, Species 1-2  ·  **Priority:** P1

**What it is:** Each channel closes with a fixed line. Gen: 'that's what I call exploring the unfamiliar' / 'learn how money and power works'. HMW: 'keep on learning how money works'. Boyle: 'See you in the next video, bye.' EE: 'Thanks for watching, mate. Bye.' Species: 'I'm Drew, and thank you so much for watching.'

- **Apply:** Use only the user's own sign-off for Gen-lean scripts.
- **Edit:** “Thank you for watching, and remember to like and subscribe.” → “to learn how money and power works.”
- **Keep:** Never borrow another creator's sign-off.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “that's what I call exploring the unfamiliar”

### `L41` — Gen voice tags
**Creators:** Gen 5/3  ·  **Priority:** P1

**What it is:** 'Look,' 'here's the thing', 'point is', 'but in all seriousness', 'I'm kidding'.

- **Apply:** 2-4 per Gen script. Not more than one per paragraph.
- **Edit:** “To summarize, censorship is not the solution.” → “point is censorship ain't never the answer”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Look, it doesn't matter at all whether you're for or against AI.”

### `L42` — Fisher voice tags
**Creators:** Fisher 6/5  ·  **Priority:** P1

**What it is:** 'I want to show you', 'Okay, with me so far?', 'Remember,', 'And you know what?', 'which means'.

- **Apply:** In Fisher lean, open each section with a show-you line.
- **Edit:** “The following map illustrates the region.” → “This all makes more sense if we look at it on a map.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “So, okay, you see why this is all much, much bigger than just a normal trade dispute. You got it?”

### `L43` — AIC voice tags
**Creators:** AIC 7/6  ·  **Priority:** P1

**What it is:** 'I want to tell you the story of', 'Alright, time for a little backstory', 'Anyway, back to the scenario', timestamp headers.

- **Apply:** In AIC lean, open with a story promise and use a time stamp at each scene.
- **Edit:** “This video covers recent events at the company.” → “I want to tell you the full story.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Alright, time for a little backstory.”

### `L44` — AotP voice tags
**Creators:** AotP 4/3  ·  **Priority:** P1

**What it is:** 'Imagine', 'Now, the heart of the trick', 'This is the breakthrough', 'Notice'.

- **Apply:** In AotP lean, every mechanism starts with Imagine plus named characters (Alice, Bob, Eve).
- **Edit:** “Consider a simplified model of lending.” → “Imagine a farmer who borrows 10 gold coins”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Now, the heart of the trick.”

### `L45` — Maxinomics voice tags
**Creators:** Maxinomics 4.5/3.5  ·  **Priority:** P1

**What it is:** Cinematic dated scene open, 'Forget X for a second', 'here's where it all comes together', footnotes segment, 'See you.'

- **Apply:** In Maxinomics lean, name the force in one word ('Reflexivity.') and reuse it.
- **Edit:** “This phenomenon is known as reflexivity in economics.” → “This is our force at work. Reflexivity.”
- **Keep:** Already present and natural in the creator lean; do not add a second instance.
- **Do NOT apply when:** Only skip when Apply's rate or lean ban already excludes it.
- **Flag a gap:** Missing where Apply says it belongs; cite the location in the draft.
- **Corpus quote (verified verbatim):** “Forget the rocket landing on the barge for a second.”


## G. Detector gate and anti-AI tells (pipeline)

### `L46` — Run local detector before handoff
**Creators:** all  ·  **Priority:** P0

**What it is:** Final narration must be scored by detect.js; bar is score ≤ 2.

- **Apply:** Every full_rewrite ends with GATE PASS/FAIL and the integer score.
- **Edit:** “[handed off with no score]” → “GATE: PASS · score=0 · label=Clean · loops=1”
- **Keep:** Grade-only mode (no rewrite).
- **Do NOT apply when:** Skipping the detector because the draft sounds fine. Also: if Node is down, mark model_only and still apply avoid-ai-writing by hand.
- **Flag a gap:** Missing GATE line on a full_rewrite.
- **Corpus quote (verified verbatim):** “But here's the problem.”

### `L47` — Iterate on issue spans only
**Creators:** all  ·  **Priority:** P0

**What it is:** When score > 2, edit the spans the issues name; do not regenerate the whole script.

- **Apply:** Max 3 detector loops; cite L* / avoid-ai tiers per change.
- **Edit:** “Score 40 → rewrite from scratch.” → “Score 40 → fix the 6 flagged spans → re-score 1”
- **Keep:** Score already ≤ 2.
- **Do NOT apply when:** Loop 4+ without reporting FAIL.
- **Flag a gap:** Full regen that drops facts.
- **Corpus quote (verified verbatim):** “But here's the problem.”

### `L48` — No fake typos to beat the detector
**Creators:** Gen 5  ·  **Priority:** P0

**What it is:** Do not sprinkle typos or broken grammar to lower the score.

- **Apply:** Gen lean: ≤1 natural slip per 500 words; other leans: zero intentional slips.
- **Edit:** “Teh Federal Reserve anounced” → “The Federal Reserve announced”
- **Keep:** A real Gen corpus slip already in the draft.
- **Do NOT apply when:** Any lean other than Gen.
- **Flag a gap:** Intentional misspellings.
- **Corpus quote (verified verbatim):** “there is two points”

### `L49` — Preserve protected spans while de-AI-ing
**Creators:** all  ·  **Priority:** P0

**What it is:** Quotes, numbers, URLs, names, dates stay exact while voice changes.

- **Apply:** Diff every change; numbers and proper nouns must match the source packet.
- **Edit:** “Roughly $2 trillion (was $2.1T in source)” → “$2.1 trillion”
- **Keep:** User explicitly corrected a fact.
- **Do NOT apply when:** Changing a figure to sound rounder.
- **Flag a gap:** Number drift after a voice pass.
- **Corpus quote (verified verbatim):** “100 million users in 2 months”

### `L50` — Ban list pass is mandatory
**Creators:** all  ·  **Priority:** P0

**What it is:** Scan for delve/tapestry/testament/landscape/crucial/pivotal/realm/moreover/furthermore/additionally/in conclusion/navigate/unlock/harness.

- **Apply:** Zero hits in the final narration (outside quotes).
- **Edit:** “In today's rapidly evolving landscape, it is crucial to” → “Here's what's actually going on.”
- **Keep:** Inside a quoted source that uses the word.
- **Do NOT apply when:** After a final pass with crucial still present.
- **Flag a gap:** Any ban-list hit outside quotes.
- **Corpus quote (verified verbatim):** “In plain English,”

### `L51` — Burstiness check
**Creators:** all  ·  **Priority:** P1

**What it is:** Vary sentence length: ~20% ≤6 words, ≤11% ≥30, mean 15–18.

- **Apply:** After rewrite, count; merge or split to hit the band.
- **Edit:** “All sentences 12–14 words.” → “Long build. Then a punch. Then a normal line that runs a bit.”
- **Keep:** Poetry/list sections in Maxinomics lean (fragments are allowed).
- **Do NOT apply when:** Mean sentence length 9 after over-splitting.
- **Flag a gap:** Flat 12–14 word drone for 500+ words.
- **Corpus quote (verified verbatim):** “It is not a routine call.”

### `L52` — Load avoid-ai-writing patterns before gate
**Creators:** all  ·  **Priority:** P0

**What it is:** Before the detector loop, read avoid-ai-writing/references/patterns.md tiers and humanizer A–F.

- **Apply:** Required once per full_rewrite session.
- **Edit:** “[skipped]” → “[loaded; Tier 1 scan done]”
- **Keep:** Detect-only grade with no rewrite.
- **Do NOT apply when:** Relying on memory of AI tells.
- **Flag a gap:** Gate run with no rulebook loaded.
- **Corpus quote (verified verbatim):** “I don't know which is true.”
