# Anti-patterns — structure

Each failure has: why it fails (with the measured norm), a **Before** (invented bad draft, labelled), an **After** (rewrite in house structure, also invented — no fake quotes), and a **Corpus model** (a real verbatim line, machine-verified). Topic for before/after drafts: a fictional "lithium shortage" video, so nothing gets confused with real transcript text.

## AP-S01 Background-first open
**Why it fails.** Every corpus video starts on an event, a number, or a scene. The weighted hook is about 79 s and has no history lesson in it (S001-S010).
**Before (invented).** "Lithium was discovered in 1817 by Johan August Arfwedson. Since then it has become an important element…"
**After (invented).** "Last Thursday, one mine in Chile stopped shipping for six hours, and battery prices in three countries moved before lunch."
**Corpus model.** "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived." — *Adam*, `adam/02-bestselling-book` @ 0:00 (0.0%)

## AP-S02 No promise line
**Why it fails.** Corpus videos state what the video will do near the end of the hook: weighted ≈6% in, Adam ≈2.5% (S011-S015). Without it, the viewer has no contract.
**Before (invented).** The open goes straight from the cold-open fact into chapter one.
**After (invented).** "I want to walk you through how one shipping delay became a pricing panic, including the part nobody in the industry wants on the record."
**Corpus model.** "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam*, `adam/01-ai-disaster` @ 0:29 (1.2%)

## AP-S03 Promise buried at minute five
**Why it fails.** The promise lands at a median of 1:19 (IQR 2.5-6.4%). At 15% or later, the hook has already lost the people it was built for.
**Before (invented).** Four minutes of context, then "so in this video we'll look at…"
**After (invented).** Promise by 1:00-1:30, then context.
**Corpus model.** "So to understand this whole thing, I think the best way is by showing you how a private equity firm even buys a YouTube channel." — *Gen*, `gen/2` @ 1:35 (7.3%)

## AP-S04 Hook that is all adjectives
**Why it fails.** Corpus hooks carry dated or numbered facts (S006). "Shocking", "insane", and "crazy" with no number do no work.
**Before (invented).** "What's happening with lithium is absolutely insane and nobody is ready."
**After (invented).** "A metal that cost $6,000 a ton three years ago hit $80,000, and the cars it goes into got cheaper anyway."
**Corpus model.** "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown." — *Adam*, `adam/01-ai-disaster` @ 0:00 (0.0%)

## AP-S05 Sponsor with no bridge
**Why it fails.** Gen-mode sponsor reads open with "that's where/why today's sponsor…", tying the sponsor to the problem just raised (criterion `sponsor_bridge`). A cold "this video is sponsored by" is the less common, mechanism-mode form, and it sits at the very top.
**Before (invented).** Mid-explanation: "Anyway, this video is sponsored by X."
**After (invented).** "And if your money is sitting in one bank while all this happens, that's exactly where today's sponsor comes in."
**Corpus model.** "And that's exactly where today's sponsor, Zappier, comes in." — *Gen*, `gen/5` @ 5:53 (35.6%)

## AP-S06 Sponsor return that resets to zero
**Why it fails.** Gen returns from the sponsor with a question or a loop ("So back to it, because…"). A plain "anyway" loses the momentum.
**Before (invented).** "OK, anyway, where were we. So, lithium."
**After (invented).** "So back to it, because if prices doubled, why did the miners just lay off a third of their staff?"
**Corpus model.** "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen*, `gen/1` @ 9:15 (45.5%)

## AP-S07 Sponsor too early in Gen mode
**Why it fails.** Gen sponsors sit at a median of ≈38.6% (IQR 34.5-41.7%), after the problem is fully stated. Mechanism mode is the exception: some reads come at 4-6%, flagged at the top.
**Before (invented).** Sponsor at 0:40 in a 20-minute explainer, before the central question.
**After (invented).** Sponsor after the first big mechanism reveal (~35-42%).
**Corpus model.** "And that's exactly where today's sponsor, Zapier, comes in." — *Gen*, `gen/8` @ 8:55 (38.6%)

## AP-S08 Sponsor read too long
**Why it fails.** The measured Gen sponsor length is about 45 s. Two minutes reads as an ad break.
**Before (invented).** A 6-paragraph feature list.
**After (invented).** Problem bridge, then 2 concrete features, then the offer and link. 35-60 s.
**Corpus model.** "And that's why I use today's sponsor, Proton Mail." — *Gen*, `gen/9` @ 7:48 (34.5%)

## AP-S09 Flat middle with no turns
**Why it fails.** The corpus has about 7 major turns, spread fairly evenly from 10% to 70% (turn density peaks at 20-30% and 50-60%). Stretches of 5+ minutes without a turn are rare.
**Before (invented).** 8 minutes of chronological facts.
**After (invented).** A turn every 3-5 minutes: "Now, …", "But then…", or a question turn.
**Corpus model.** "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam*, `adam/02-bestselling-book` @ 20:28 (47.8%)

## AP-S10 Turn without a question
**Why it fails.** Section turns in the corpus often take the form of a question the next section answers (QUESTION TURN). A label like "Part 3: Supply" is not a turn.
**Before (invented).** "Section three. Supply chains."
**After (invented).** "So if the mines are full, why can't anyone buy the stuff?"
**Corpus model.** "What's important is what really does have to be true for any of this to make sense." — *Gen*, `gen/9` @ 15:56 (70.4%)

## AP-S11 Conclusion that only recaps
**Why it fails.** Corpus conclusions (≈82-88%) move to the viewer or the future: "what this means for you", "your choice". A bullet recap drops the stakes.
**Before (invented).** "So to sum up: lithium is mined, refined, and shipped."
**After (invented).** "So what does this actually mean for you, the next time you're quoted a price for a car battery?"
**Corpus model.** "So, the newest homeowners are like the first ones falling behind, which brings up a pretty important question of what this all means for you and in the future." — *Gen*, `gen/3` @ 17:28 (76.9%)

## AP-S12 Conclusion arriving too early
**Why it fails.** The weighted conclusion starts at ≈87.6% (Adam ≈76-82%, earlier because the essays run long). At 60%, the back third has nothing to do.
**Before (invented).** "In conclusion…" at minute 11 of 22.
**After (invented).** The last escalation goes at 70-80%, then the conclusion pivot.
**Corpus model.** "I think that's basically the plan for AI companies today." — *Adam*, `adam/02-bestselling-book` @ 37:32 (87.6%)

## AP-S13 Long outro / CTA stack
**Why it fails.** The corpus closes with 1-3 lines in the last 1-3%. Adam's whole sign-off is one line.
**Before (invented).** 90 s of subscribe, bell, Patreon, merch, socials, and next-video plugs.
**After (invented).** One line of thanks, one handoff.
**Corpus model.** "Thank you so much for watching and see you in the next one." — *Adam*, `adam/01-ai-disaster` @ 39:16 (99.9%)

## AP-S14 Wrong mode for the runtime
**Why it fails.** Adam-mode essays run ≈34-40 min and need 7 sections with dated narrative. Gen-mode explainers run ≈20-23 min. A 12-minute "Adam" piece cannot fit the evidence stack.
**Before (invented).** A 12-minute investigative timeline with 14 dated events.
**After (invented).** Either cut to a Gen-mode explainer with 6 turns, or expand to 35 min.
**Corpus model.** "Now, Sam tells him he's in." — *Adam*, `adam/05-sam-altman` @ 20:03 (50.1%)

## AP-S15 Thesis never stated
**Why it fails.** Where detected, the thesis or stakes line sits at about 5% (Gen 5.5%). Gen videos open with a stakes claim such as "what no one is talking about…".
**Before (invented).** Facts accumulate and the viewer never learns why they matter.
**After (invented).** "And what nobody in the car industry is saying out loud is that the shortage was manufactured."
**Corpus model.** "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?" — *Gen*, `gen/1` @ 0:17 (1.4%)

## AP-S16 Explainer-tone in a narrative video
**Why it fails.** Adam-mode middles run on scene verbs ("Sam tells him he's in"). Gen-mode middles run on mechanism ("here's how it works"). Mixing them inside one act blurs the mode.
**Before (invented).** A scene that stops for a 2-minute definition with no return to the scene.
**After (invented).** A one-line gloss ("basically, X"), then straight back into the scene.
**Corpus model.** "Back to it because hedge funds, basically private firms that manage money for the very rich, are now specifically betting against big tech stocks." — *Gen*, `gen/9` @ 8:26 (37.3%)

## AP-S17 No counter-case pass
**Why it fails.** Corpus essays run the skeptic's case around 55-70% ("To be fair…", "Now, do the examples… even apply"). Skipping it reads as propaganda.
**Before (invented).** Only evidence for the thesis.
**After (invented).** "Now, to be fair, the miners have a point, and it goes like this…"
**Corpus model.** "Now, do the examples of CoinRun and evolution even apply to state of the art AI agents?" — *Adam*, `adam/02-bestselling-book` @ 20:28 (47.8%)

## AP-S18 Open loops never closed
**Why it fails.** Loops are planted in the hook ("details I haven't seen reported anywhere else") and paid later. Dropping the payoff breaks the contract.
**Before (invented).** "We'll get to the strangest part later," and later never comes.
**After (invented).** A loop ledger in the outline, with each loop paid by the act named.
**Corpus model.** "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam*, `adam/01-ai-disaster` @ 0:29 (1.2%)

## AP-S19 Escalation that plateaus
**Why it fails.** Turns get bigger in scope toward 60-80%: from a person, to a company, to the system, to "you". A flat sequence of equal-weight facts does not escalate.
**Before (invented).** Five examples of the same size.
**After (invented).** Order examples by scope and end on the one that touches the viewer.
**Corpus model.** "But if I had to guess, it's because they know something a lot bigger and a lot worse than a crude oil shortage, like we said at the top of this video, is already starting to hit the world." — *Oil*, `esp/03-oil-apocalypse` @ 13:17 (37.5%)

## AP-S20 Title-script mismatch
**Why it fails.** The title's key noun shows up in the hook in most corpus videos (S title_in_hook). A title promise paid at minute 15 is clickbait.
**Before (invented).** Title "The lithium lie" is never mentioned until the end.
**After (invented).** The hook names the lie in the first 30 s.
**Corpus model.** "Okay, am I crazy or is it really starting to smell a lot like robot apocalypse in here?" — *Others*, `after/11-anthropic-ipo` @ 0:00 (0.0%)

## AP-S21 Chapters that are topics, not questions
**Why it fails.** Corpus section openers move the story ("Now, …", "So, now let's talk about which…"), and they don't announce a subject.
**Before (invented).** "Chapter 4: Economics."
**After (invented).** "So now let's talk about who actually bought the mines and what they paid."
**Corpus model.** "So, now let's talk about which channels have actually been bought and the few players behind them all." — *Gen*, `gen/2` @ 10:46 (49.5%)

## AP-S22 Final line that trails off
**Why it fails.** The last content line before the sign-off is a short verdict or an agency line ("is your choice").
**Before (invented).** "So yeah, that's basically it, I guess, we'll see."
**After (invented).** "The price was never about the metal. It was about who gets to say no."
**Corpus model.** "But what will at the end of the day is your choice." — *Gen*, `gen/8` @ 21:21 (92.4%)

## AP-S23 Uniform pacing
**Why it fails.** WPM differs by mode (Adam ≈164, Gen ≈190), but every corpus video alternates long build sentences with short punch lines ("It was a strange summer.").
**Before (invented).** Twenty 25-word sentences in a row.
**After (invented).** After a long setup, a 4-6 word line.
**Corpus model.** "It was a strange summer." — *Adam*, `adam/03-no-longer-in-control` @ 0:00 (0.0%)

## AP-S24 Unscoped claim in the hook
**Why it fails.** Corpus openers narrow the claim right away, e.g. "we're not a tech explainer channel, so let's get to the money".
**Before (invented).** "Lithium will destroy the world economy."
**After (invented).** "Not the whole economy, at least not yet, but the part that runs on batteries."
**Corpus model.** "But, obviously we're not a tech explainer channel, so let's get to the money." — *Gen*, `gen/1` @ 7:31 (36.9%)

## AP-S25 No "where does this leave us" pivot
**Why it fails.** Mechanism and oil videos open the conclusion with a meaning question ("So what does all this mean?").
**Before (invented).** The last fact goes straight into the sign-off.
**After (invented).** "So what does all this mean for the next five years?"
**Corpus model.** "So what does all this mean?" — *Oil*, `esp/03-oil-apocalypse` @ 33:46 (95.2%)
