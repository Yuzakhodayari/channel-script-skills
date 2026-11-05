# Anti-patterns — audience engineering

Same format as the structure anti-patterns: why it fails (measured norm), **Before** (invented, labelled), **After** (invented rewrite), **Corpus model** (verbatim, machine-verified). Draft topic: a fictional "lithium shortage" video.

## AP-A01 Sixty seconds with no re-hook
**Why it fails.** The weighted median gap between re-hooks (question, "But…", "here's…", "turns out") is ≈26 s (IQR 17-33). Gen sits at ≈14-18 s.
**Before (invented).** A 200-word block of declarative facts.
**After (invented).** A "But…" or a question every 3-5 sentences.
**Corpus model.** {{adam/01-ai-disaster|But Elon Musk being Elon Musk was not afraid to tweet about it.}}

## AP-A02 Lecturing "people" instead of "you"
**Why it fails.** Gen's "you" density is about 2x Adam's, and every group uses "you" in the open. Third-person framing cuts off the stakes for "you".
**Before (invented).** "Consumers may see increased costs."
**After (invented).** "You're going to see this on your next car quote."
**Corpus model.** {{gen/1|So back to it, because if all this software is suddenly free, do you really think you're the one winning?}}

## AP-A03 Fake curiosity gap
**Why it fails.** Corpus gaps point at a specific, answerable thing ("details I haven't seen reported"). "You won't believe what happens next" names nothing.
**Before (invented).** "What happened next will shock you."
**After (invented).** "And the email that ended it was three lines long. We'll get to what it said."
**Corpus model.** {{adam/01-ai-disaster|including some details I haven't seen reported on anywhere else}}

## AP-A04 Fear with no exit
**Why it fails.** Fear words are densest in the open and middle. Hope and agency words rise in the last 10-15% (criteria "Hope in the close", "Agency for you"). A doom-only close drives clicks away from the channel.
**Before (invented).** The last line is "we're all doomed."
**After (invented).** "But this is still a choice somebody makes, and for once that somebody includes you."
**Corpus model.** {{gen/5|But, I think the one thing that actually scares them is you starting to.}}

## AP-A05 Outrage without a named actor
**Why it fails.** Corpus outrage targets an institution or a named person with a motive. Diffuse anger at "the system" gives the viewer no "them".
**Before (invented).** "The system is rigged."
**After (invented).** "Three trading houses set the price, and one of them sat on the committee that wrote the rules."
**Corpus model.** {{gen/9|Back to it because hedge funds, basically private firms that manage money for the very rich}}

## AP-A06 Credibility by adjective
**Why it fails.** Corpus credibility comes from documents, dates, and named sources ("In leaked emails from 2017…"). "Experts agree" is a red flag.
**Before (invented).** "Experts say this is very serious."
**After (invented).** "In the company's own 2024 filing, page 41, they call it a 'material risk'."
**Corpus model.** {{adam/01-ai-disaster|In leaked emails from 2017, Ilya Sutskever of OpenAI says to Elon}}

## AP-A07 Humor that undercuts the stakes
**Why it fails.** Corpus humor is a short aside after a fact ("I swear to God", "by the way"), never a bit that runs longer than the fact it follows.
**Before (invented).** A 40-second sketch about a lithium mine mascot.
**After (invented).** One deadpan aside, then straight back to the fact.
**Corpus model.** {{adam/03-no-longer-in-control|They call this, I swear to God, permadeath.}}

## AP-A08 Pattern interrupts with no content
**Why it fails.** Corpus interrupts ("Okay, so, …", "Wait") reset attention *and* deliver the next dated fact.
**Before (invented).** "OK! Let's keep going, guys!"
**After (invented).** "Okay, so, March 2025, the first warehouse runs dry."
**Corpus model.** {{adam/01-ai-disaster|Okay, so, February 2025, we just had this}}

## AP-A09 Comment bait as a generic ask
**Why it fails.** Explicit comment asks are rare in the corpus. When they show up, they are opinion questions tied to the thesis.
**Before (invented).** "Comment below, like and subscribe!"
**After (invented).** "Would you pay 20% more for a car that's never built with Chinese lithium? Genuinely want to know."
**Corpus model.** {{after/03-recycling|Am I the only one that peeped that?}}

## AP-A10 Subscribe ask in the hook
**Why it fails.** Subscribe and CTA asks cluster at 90-100%. An early ask spends trust before any value is delivered.
**Before (invented).** 0:15: "Before we start, subscribe."
**After (invented).** Ask once, after the payoff, in a single line.
**Corpus model.** {{adam/02-bestselling-book|We'll see you in the next one.}}

## AP-A11 Objection left unanswered
**Why it fails.** The host voices the viewer's doubt and answers it ("surely some of them might…"). Unanswered objections show up as comment-section rebuttals.
**Before (invented).** The claim is made and the obvious counter is ignored.
**After (invented).** "Now you're probably thinking: just recycle the batteries. Here's why that doesn't work yet."
**Corpus model.** {{gen/3|So, surely some of them might give me grants or tax breaks}}

## AP-A12 Relatability by generic "we all"
**Why it fails.** Corpus relatability uses concrete shared experience ("our wells have pretty much dried up") and an everyday-object anchor.
**Before (invented).** "We all use technology."
**After (invented).** "If your phone's battery dies by 3 p.m. now, this is part of why."
**Corpus model.** {{after/10-water|We've all noticed our wells have pretty much dried up.}}

## AP-A13 Big number with no anchor
**Why it fails.** Exact numbers come with a physical or wallet comparison (criteria "Wallet anchor", "Physical-scale anchor").
**Before (invented).** "Production fell by 2.3 million tonnes."
**After (invented).** "That's enough lithium for every car sold in America for two years, gone."
**Corpus model.** {{esp/01-spacex|But of course, adding more fuel means that you need to add even more fuel to carry that fuel.}}

## AP-A14 Parasocial over-share
**Why it fails.** Host-"I" presence is steady but light. Opinions are flagged ("I think", "if I had to guess"), and the life story never takes over the video.
**Before (invented).** A 3-minute personal story unrelated to lithium.
**After (invented).** One line of a flagged opinion: "If I had to guess, they knew."
**Corpus model.** {{esp/03-oil-apocalypse|But if I had to guess, it's because they know something a lot bigger}}

## AP-A15 Absolute certainty
**Why it fails.** Corpus hosts hedge where the evidence is thin ("I think", "if I had to guess"). Overclaiming invites debunks.
**Before (invented).** "This will 100% crash the market next year."
**After (invented).** "I think the window is closing, and here's the one number that would prove me wrong."
**Corpus model.** {{adam/04-superintelligence|So I think the window that we have to act is narrowing quickly.}}

## AP-A16 Monotone density
**Why it fails.** Short punch lines break up dense passages (criterion "Short punch sentence share"). Without them, viewers lose the thread.
**Before (invented).** Three dense 30-word sentences in a row about refining chemistry.
**After (invented).** Insert "Just that took three weeks." after the setup.
**Corpus model.** {{adam/03-no-longer-in-control|Just doing that took them three days, by the way.}}

## AP-A17 "Us vs them" with no "us"
**Why it fails.** Corpus antagonist framing is paired with viewer-as-victim or citizen ("somebody actually has to pay for it").
**Before (invented).** "Big companies are bad."
**After (invented).** "And when the price shifts, it's not the trading house that pays for it."
**Corpus model.** {{gen/9|Whenever it shifts, somebody actually has to pay for it.}}

## AP-A18 Sponsor read that breaks trust
**Why it fails.** Corpus sponsor reads are framed as personal use and tied to the topic ("that's why I use today's sponsor").
**Before (invented).** "Buy this VPN, it's the best."
**After (invented).** "And honestly, that's why I use today's sponsor."
**Corpus model.** {{gen/6|And that's why I personally use today's sponsor, Zapier.}}

## AP-A19 Re-entry after sponsor with no hook
**Why it fails.** Post-sponsor re-entry restates the stakes as a question. "And now back to the video" alone is the weaker variant.
**Before (invented).** "Anyway."
**After (invented).** "So back to it, because if the mines are full, who's hoarding?"
**Corpus model.** {{gen/5|So, back at it, if 90% of data centers are never going to be built}}

## AP-A20 Persona inconsistency
**Why it fails.** Gen's persona plays along ("I'm going to stop playing CEO now"), and Adam stays a measured narrator. Switching persona mid-video confuses the parasocial cue.
**Before (invented).** A calm narrator suddenly screams.
**After (invented).** Keep one persona and let it play: "OK, I'm going to stop playing mine owner now and follow the money."
**Corpus model.** {{gen/4|So, I'm going to stop playing CEO now and follow the money}}

## AP-A21 Stakes for nobody in particular
**Why it fails.** Stakes have to land on "you" (criteria "Personal consequence line", "Future-you projection").
**Before (invented).** "This could have impacts."
**After (invented).** "Your next phone, your next car, your next electricity bill."
**Corpus model.** {{gen/3|which brings up a pretty important question of what this all means for you}}

## AP-A22 Over-hyped verdict line
**Why it fails.** Corpus verdicts are blunt and colloquial ("the economy is cooked"), short, and backed by the metric just shown.
**Before (invented).** "This is the most catastrophic, unprecedented event in human history!!!"
**After (invented).** "Every number says the same thing: the supply is gone."
**Corpus model.** {{gen/9|Every single metric says that the economy is cooked.}}

## AP-A23 Wake-up framing without evidence
**Why it fails.** Corpus warnings name the warner and what they said ("He was out there warning…").
**Before (invented).** "Wake up, people."
**After (invented).** "Their own chief geologist was warning about this in 2019."
**Corpus model.** {{adam/01-ai-disaster|He was out there warning that we were about to build something uncontrollable}}

## AP-A24 Comment-noticing beat skipped
**Why it fails.** Gen uses audience reaction as evidence ("comments now really start noticing"). This builds community proof.
**Before (invented).** Viewer reactions are never mentioned.
**After (invented).** "And this is when people on forums started posting the receipts."
**Corpus model.** {{gen/2|But thing is, comments now really start noticing.}}

## AP-A25 Mood whiplash at the close
**Why it fails.** The close moves from fear to agency over 2-4 sentences. It does not snap from horror to "anyway, thanks for watching".
**Before (invented).** "…and millions could lose their jobs. Thanks for watching!"
**After (invented).** Agency line, then verdict, then the thank-you.
**Corpus model.** {{gen/8|But what will at the end of the day is your choice.}}
