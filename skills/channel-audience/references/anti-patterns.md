# Anti-patterns — audience engineering

Same format as the structure anti-patterns: why it fails (measured norm), **Before** (invented, labelled), **After** (invented rewrite), **Corpus model** (verbatim, machine-verified). Draft topic: a fictional "lithium shortage" video.

## AP-A01 Sixty seconds with no re-hook
**Why it fails.** The weighted median gap between re-hooks (question, "But…", "here's…", "turns out") is ≈26 s (IQR 17-33). Gen sits at ≈14-18 s.
**Before (invented).** A 200-word block of declarative facts.
**After (invented).** A "But…" or a question every 3-5 sentences.
**Corpus model.** "But Elon Musk being Elon Musk was not afraid to tweet about it." — *Adam*, `adam/01-ai-disaster` @ 17:25 (44.3%)

## AP-A02 Lecturing "people" instead of "you"
**Why it fails.** Gen's "you" density is about 2x Adam's, and every group uses "you" in the open. Third-person framing cuts off the stakes for "you".
**Before (invented).** "Consumers may see increased costs."
**After (invented).** "You're going to see this on your next car quote."
**Corpus model.** "So back to it, because if all this software is suddenly free, do you really think you're the one winning?" — *Gen*, `gen/1` @ 9:15 (45.5%)

## AP-A03 Fake curiosity gap
**Why it fails.** Corpus gaps point at a specific, answerable thing ("details I haven't seen reported"). "You won't believe what happens next" names nothing.
**Before (invented).** "What happened next will shock you."
**After (invented).** "And the email that ended it was three lines long. We'll get to what it said."
**Corpus model.** "I want to take you step-by-step through the MechaHitler meltdown and explain what happened, including some details I haven't seen reported on anywhere else." — *Adam*, `adam/01-ai-disaster` @ 0:29 (1.2%)

## AP-A04 Fear with no exit
**Why it fails.** Fear words are densest in the open and middle. Hope and agency words rise in the last 10-15% (criteria "Hope in the close", "Agency for you"). A doom-only close drives clicks away from the channel.
**Before (invented).** The last line is "we're all doomed."
**After (invented).** "But this is still a choice somebody makes, and for once that somebody includes you."
**Corpus model.** "But, I think the one thing that actually scares them is you starting to." — *Gen*, `gen/5` @ 16:08 (97.7%)

## AP-A05 Outrage without a named actor
**Why it fails.** Corpus outrage targets an institution or a named person with a motive. Diffuse anger at "the system" gives the viewer no "them".
**Before (invented).** "The system is rigged."
**After (invented).** "Three trading houses set the price, and one of them sat on the committee that wrote the rules."
**Corpus model.** "Back to it because hedge funds, basically private firms that manage money for the very rich, are now specifically betting against big tech stocks." — *Gen*, `gen/9` @ 8:26 (37.3%)

## AP-A06 Credibility by adjective
**Why it fails.** Corpus credibility comes from documents, dates, and named sources ("In leaked emails from 2017…"). "Experts agree" is a red flag.
**Before (invented).** "Experts say this is very serious."
**After (invented).** "In the company's own 2024 filing, page 41, they call it a 'material risk'."
**Corpus model.** "In leaked emails from 2017, Ilya Sutskever of OpenAI says to Elon, "You are concerned that Demis, (that's Demis Hassabis, the head of Google DeepMind), could create an AGI dictatorship."" — *Adam*, `adam/01-ai-disaster` @ 28:47 (73.2%)

## AP-A07 Humor that undercuts the stakes
**Why it fails.** Corpus humor is a short aside after a fact ("I swear to God", "by the way"), never a bit that runs longer than the fact it follows.
**Before (invented).** A 40-second sketch about a lithium mine mascot.
**After (invented).** One deadpan aside, then straight back to the fact.
**Corpus model.** "They call this, I swear to God, permadeath." — *Adam*, `adam/03-no-longer-in-control` @ 13:19 (40.6%)

## AP-A08 Pattern interrupts with no content
**Why it fails.** Corpus interrupts ("Okay, so, …", "Wait") reset attention *and* deliver the next dated fact.
**Before (invented).** "OK! Let's keep going, guys!"
**After (invented).** "Okay, so, March 2025, the first warehouse runs dry."
**Corpus model.** "Okay, so, February 2025, we just had this “really terrible and bad failure” from Grok." — *Adam*, `adam/01-ai-disaster` @ 6:11 (15.7%)

## AP-A09 Comment bait as a generic ask
**Why it fails.** Explicit comment asks are rare in the corpus. When they show up, they are opinion questions tied to the thesis.
**Before (invented).** "Comment below, like and subscribe!"
**After (invented).** "Would you pay 20% more for a car that's never built with Chinese lithium? Genuinely want to know."
**Corpus model.** "Am I the only one that peeped that?" — *Others*, `after/03-recycling` @ 27:38 (89.7%)

## AP-A10 Subscribe ask in the hook
**Why it fails.** Subscribe and CTA asks cluster at 90-100%. An early ask spends trust before any value is delivered.
**Before (invented).** 0:15: "Before we start, subscribe."
**After (invented).** Ask once, after the payoff, in a single line.
**Corpus model.** "We'll see you in the next one." — *Adam*, `adam/02-bestselling-book` @ 42:47 (99.9%)

## AP-A11 Objection left unanswered
**Why it fails.** The host voices the viewer's doubt and answers it ("surely some of them might…"). Unanswered objections show up as comment-section rebuttals.
**Before (invented).** The claim is made and the obvious counter is ignored.
**After (invented).** "Now you're probably thinking: just recycle the batteries. Here's why that doesn't work yet."
**Corpus model.** "So, surely some of them might give me grants or tax breaks if I if I ask for some." — *Gen*, `gen/3` @ 8:02 (35.4%)

## AP-A12 Relatability by generic "we all"
**Why it fails.** Corpus relatability uses concrete shared experience ("our wells have pretty much dried up") and an everyday-object anchor.
**Before (invented).** "We all use technology."
**After (invented).** "If your phone's battery dies by 3 p.m. now, this is part of why."
**Corpus model.** "We've all noticed our wells have pretty much dried up." — *Others*, `after/10-water` @ 0:49 (6.1%)

## AP-A13 Big number with no anchor
**Why it fails.** Exact numbers come with a physical or wallet comparison (criteria "Wallet anchor", "Physical-scale anchor").
**Before (invented).** "Production fell by 2.3 million tonnes."
**After (invented).** "That's enough lithium for every car sold in America for two years, gone."
**Corpus model.** "But of course, adding more fuel means that you need to add even more fuel to carry that fuel." — *Especially*, `esp/01-spacex` @ 17:17 (69.6%)

## AP-A14 Parasocial over-share
**Why it fails.** Host-"I" presence is steady but light. Opinions are flagged ("I think", "if I had to guess"), and the life story never takes over the video.
**Before (invented).** A 3-minute personal story unrelated to lithium.
**After (invented).** One line of a flagged opinion: "If I had to guess, they knew."
**Corpus model.** "But if I had to guess, it's because they know something a lot bigger and a lot worse than a crude oil shortage, like we said at the top of this video, is already starting to hit the world." — *Oil*, `esp/03-oil-apocalypse` @ 13:17 (37.5%)

## AP-A15 Absolute certainty
**Why it fails.** Corpus hosts hedge where the evidence is thin ("I think", "if I had to guess"). Overclaiming invites debunks.
**Before (invented).** "This will 100% crash the market next year."
**After (invented).** "I think the window is closing, and here's the one number that would prove me wrong."
**Corpus model.** "So I think the window that we have to act is narrowing quickly." — *Adam*, `adam/04-superintelligence` @ 30:14 (88.7%)

## AP-A16 Monotone density
**Why it fails.** Short punch lines break up dense passages (criterion "Short punch sentence share"). Without them, viewers lose the thread.
**Before (invented).** Three dense 30-word sentences in a row about refining chemistry.
**After (invented).** Insert "Just that took three weeks." after the setup.
**Corpus model.** "Just doing that took them three days, by the way." — *Adam*, `adam/03-no-longer-in-control` @ 24:11 (73.7%)

## AP-A17 "Us vs them" with no "us"
**Why it fails.** Corpus antagonist framing is paired with viewer-as-victim or citizen ("somebody actually has to pay for it").
**Before (invented).** "Big companies are bad."
**After (invented).** "And when the price shifts, it's not the trading house that pays for it."
**Corpus model.** "Whenever it shifts, somebody actually has to pay for it." — *Gen*, `gen/9` @ 17:27 (77.1%)

## AP-A18 Sponsor read that breaks trust
**Why it fails.** Corpus sponsor reads are framed as personal use and tied to the topic ("that's why I use today's sponsor").
**Before (invented).** "Buy this VPN, it's the best."
**After (invented).** "And honestly, that's why I use today's sponsor."
**Corpus model.** "And that's why I personally use today's sponsor, Zapier." — *Gen*, `gen/6` @ 9:14 (41.4%)

## AP-A19 Re-entry after sponsor with no hook
**Why it fails.** Post-sponsor re-entry restates the stakes as a question. "And now back to the video" alone is the weaker variant.
**Before (invented).** "Anyway."
**After (invented).** "So back to it, because if the mines are full, who's hoarding?"
**Corpus model.** "So, back at it, if 90% of data centers are never going to be built, does not just sound like the best news for more housing?" — *Gen*, `gen/5` @ 6:37 (40.1%)

## AP-A20 Persona inconsistency
**Why it fails.** Gen's persona plays along ("I'm going to stop playing CEO now"), and Adam stays a measured narrator. Switching persona mid-video confuses the parasocial cue.
**Before (invented).** A calm narrator suddenly screams.
**After (invented).** Keep one persona and let it play: "OK, I'm going to stop playing mine owner now and follow the money."
**Corpus model.** "So, I'm going to stop playing CEO now and follow the money to look for whoever that was." — *Gen*, `gen/4` @ 8:54 (43.4%)

## AP-A21 Stakes for nobody in particular
**Why it fails.** Stakes have to land on "you" (criteria "Personal consequence line", "Future-you projection").
**Before (invented).** "This could have impacts."
**After (invented).** "Your next phone, your next car, your next electricity bill."
**Corpus model.** "So, the newest homeowners are like the first ones falling behind, which brings up a pretty important question of what this all means for you and in the future." — *Gen*, `gen/3` @ 17:28 (76.9%)

## AP-A22 Over-hyped verdict line
**Why it fails.** Corpus verdicts are blunt and colloquial ("the economy is cooked"), short, and backed by the metric just shown.
**Before (invented).** "This is the most catastrophic, unprecedented event in human history!!!"
**After (invented).** "Every number says the same thing: the supply is gone."
**Corpus model.** "Every single metric says that the economy is cooked." — *Gen*, `gen/9` @ 0:01 (0.1%)

## AP-A23 Wake-up framing without evidence
**Why it fails.** Corpus warnings name the warner and what they said ("He was out there warning…").
**Before (invented).** "Wake up, people."
**After (invented).** "Their own chief geologist was warning about this in 2019."
**Corpus model.** "He was out there warning that we were about to build something uncontrollable and maybe catastrophically dangerous." — *Adam*, `adam/01-ai-disaster` @ 27:26 (69.8%)

## AP-A24 Comment-noticing beat skipped
**Why it fails.** Gen uses audience reaction as evidence ("comments now really start noticing"). This builds community proof.
**Before (invented).** Viewer reactions are never mentioned.
**After (invented).** "And this is when people on forums started posting the receipts."
**Corpus model.** "But thing is, comments now really start noticing." — *Gen*, `gen/2` @ 8:01 (36.9%)

## AP-A25 Mood whiplash at the close
**Why it fails.** The close moves from fear to agency over 2-4 sentences. It does not snap from horror to "anyway, thanks for watching".
**Before (invented).** "…and millions could lose their jobs. Thanks for watching!"
**After (invented).** Agency line, then verdict, then the thank-you.
**Corpus model.** "But what will at the end of the day is your choice." — *Gen*, `gen/8` @ 21:21 (92.4%)
