import re
from crit_structure import per_min, S, wc
def dens(v,rx,a=0,b=101):
    R=re.compile(rx,re.I); ss=[s for s in S(v) if a<=s['pct']<b]; w=sum(wc(s['text']) for s in ss)
    return round(1000*sum(len(R.findall(s['text'])) for s in ss)/max(w,1),1)
def gaps(v,rx):
    R=re.compile(rx,re.I); ts=[s['t'] for s in S(v) if R.search(s['text'])]
    if len(ts)<2: return None
    g=sorted(b-a for a,b in zip(ts,ts[1:])); return g[len(g)//2]
REHOOK=r"\?$|^but\b|\bhere'?s (the|where|what|why)\b|\b(but|and) (then|now)\b|\bit gets\b|\bwait\b|\bturns out\b"
F={
 'rehook_gap': lambda v,b: gaps(v,REHOOK),
 'q_gap': lambda v,b: gaps(v,r"\?$"),
 'but_gap': lambda v,b: gaps(v,r"^but\b"),
 'you_per_k': lambda v,b: dens(v,r"\byou(r|'re|'ll|'ve|rself)?\b"),
 'you_open': lambda v,b: dens(v,r"\byou(r|'re|'ll|'ve|rself)?\b",0,10),
 'you_close': lambda v,b: dens(v,r"\byou(r|'re|'ll|'ve|rself)?\b",85,101),
 'we_per_k': lambda v,b: dens(v,r"\b(we|us|our|we're|we've)\b"),
 'i_per_k': lambda v,b: dens(v,r"\b(I|I'm|I've|I'd|my|me)\b"),
 'they_per_k': lambda v,b: dens(v,r"\b(they|them|their|they're)\b"),
 'hedge_per_k': lambda v,b: dens(v,r"\b(I think|probably|kind of|sort of|maybe|might|seems)\b"),
 'fear_per_k': lambda v,b: dens(v,r"\b(danger\w*|threat\w*|catastroph\w*|disaster\w*|collapse\w*|crash\w*|die|death|kill\w*|extinct\w*|terrif\w*|scar\w+|risk\w*|worst)\b"),
 'outrage_per_k': lambda v,b: dens(v,r"\b(greed\w*|scam\w*|rip\w* off|corrupt\w*|exploit\w*|lie[sd]?|lying|fraud\w*|screw\w*|slop|shady|insane|ridiculous|cooked)\b"),
 'hope_per_k': lambda v,b: dens(v,r"\b(hope\w*|optimis\w*|good news|solution\w*|fix\w*|better|we can|possible)\b"),
 'hope_close': lambda v,b: dens(v,r"\b(hope\w*|optimis\w*|good news|solution\w*|fix\w*|better|we can|possible)\b",85,101),
 'fear_open': lambda v,b: dens(v,r"\b(danger\w*|threat\w*|catastroph\w*|disaster\w*|collapse\w*|crash\w*|die|death|kill\w*|extinct\w*|risk\w*|worst)\b",0,10),
 'profanity_per_k': lambda v,b: dens(v,r"\b(hell|damn|shit|f\*?ck\w*|ass|crap|sucks?)\b"),
 'money_per_k': lambda v,b: dens(v,r"\$|\b(dollars?|money|pay|price|cost|bill|salary|rent)\b"),
 'q_per_min': lambda v,b: per_min(v,r"\?$"),
 'num_per_min': lambda v,b: per_min(v,r"\d"),
 'credibility_per_k': lambda v,b: dens(v,r"\b(according to|report\w*|study|studies|data|documents?|filings?|research\w*|analysis|testimony|interview\w*)\b"),
 'humor_per_k': lambda v,b: dens(v,r"\b(lol|joke|kidding|funny|hilarious|weird\w*|wild|crazy|literally)\b|\bwhich,? (honestly|frankly)\b"),
 'short_punch_share': lambda v,b: round(100*sum(1 for s in S(v) if wc(s['text'])<=5)/max(len(S(v)),1),1),
 'imperative_share': lambda v,b: round(100*sum(1 for s in S(v) if re.match(r"(look|think|imagine|take|picture|remember|consider|let'?s|go|check|hold on|wait)\b",s['text'],re.I))/max(len(S(v)),1),1),
}
C=[]
def c(cat,name,defi,kind,spec,do,dont): C.append(dict(cat=cat,name=name,defi=defi,kind=kind,spec=spec,do=do,dont=dont))
# A Retention devices
A='A. Retention & re-hooks'
c(A,'Re-hook interval (median s)','Median seconds between re-hook sentences (question, "But…", "here\'s", "turns out", "it gets").','fn','rehook_gap','Plant a re-hook every ~10-30 s of narration.','Do not let 60 s pass without a turn.')
c(A,'Question interval (median s)','Median seconds between host questions.','fn','q_gap','Cluster questions at section turns.','Do not space evenly like a metronome.')
c(A,'"But" sentence interval','Median seconds between sentences that open with But.','fn','but_gap','Use "But" as the main micro-reversal.','Do not open 3 sentences in a row with But.')
c(A,'"Turns out" reveal','Reveal marker that pays a micro-gap.','rx',(r"\bturns? out\b",'all'),'Use when the fact contradicts the setup.','Do not use for expected facts.')
c(A,'"Here\'s the thing/where/why" pointer','Pointer phrase that flags the next line as important.','rx',(r"\bhere'?s (the thing|where|why|what|how|the (part|kicker|catch|problem))\b",'all'),'1 per 3-5 min.','Do not use as filler.')
c(A,'"It gets worse/weirder" escalator','Explicit escalation re-hook.','rx',(r"\b(it gets (worse|weirder|crazier|better|stranger)|gets even|and it doesn'?t (stop|end))\b",'all'),'Use once or twice per video.','Do not escalate without new facts.')
c(A,'"Wait/hold on" interrupt','Self-interruption to reset attention.','rx',(r"\b(wait|hold on|hang on)\b",'all'),'Gen tic: "And hold on."','Do not use in Adam mode more than once.')
c(A,'Teaser of later payoff','"We\'ll get to that / more on that later / in a minute".','rx',(r"\b(we'?ll get (to|back to)|more on (that|this)|in a (minute|second|bit)|later (in|on)|come back to)\b",'all'),'Promise a later payoff explicitly.','Do not forget to pay it.')
c(A,'Sentence-opening "And" momentum','Sentences opening with And (momentum chaining).','rx',(r"^and\b",'all'),'Use to keep momentum through lists.','Do not chain 5.')
c(A,'Short punch sentence share','% sentences of ≤5 words.','fn','short_punch_share','Punch after long builds.','Do not exceed ~15%.')
# B Curiosity gaps
B='B. Curiosity gaps & open loops'
c(B,'Information-gap question','Question the viewer cannot yet answer.','rx',(r"^(so,? )?(why|how|what)\b.*\?$",'all'),'Ask, then delay the answer 20-90 s.','Do not ask questions you answer instantly.')
c(B,'Mystery framing','"No one knows why / no one could explain".','rx',(r"\b(no one|nobody) (knows|could explain|understands|knew)|still (don'?t|doesn'?t) know|mystery\b",'all'),'Plant early.','Do not fake.')
c(B,'Counter-intuitive claim','"Actually / in fact / the opposite".','rx',(r"\b(actually|in fact|the opposite|counterintuitive|surprisingly|ironically)\b",'all'),'Tie to a sourced fact.','Do not overuse "actually".')
c(B,'"What no one is telling you"','Hidden-truth gap.','rx',(r"\b(no one|nobody) (is )?(talking|telling|told)|not telling you|what they don'?t|secret\w*|hidden\b",'all'),'Use once in the open.','Do not repeat.')
c(B,'Partial reveal','Naming the answer exists but withholding it ("there\'s one reason…").','rx',(r"\b(one (reason|thing|detail|problem)|the (real|actual) reason|the answer is)\b",'all'),'Name it, then explain.','Do not tease without payoff.')
c(B,'Hypothetical "what if"','"What if / imagine if".','rx',(r"\bwhat if\b|\bimagine (if|that|a)\b",'all'),'Use for future-stakes scenarios.','Do not chain hypotheticals.')
c(B,'Numbered tease','"Three reasons / two problems".','rx',(r"\b(two|three|four|five) (reasons|things|problems|ways|players|steps|questions)\b",'all'),'Number the list in the promise.','Do not exceed 5.')
c(B,'Questions per minute','Overall question density.','fn','q_per_min','Match group norm.','Do not exceed 2/min.')
# C Pattern interrupts
Cc='C. Pattern interrupts'
c(Cc,'Tone shift to casual','Casual aside ("honestly", "like", "you know").','rx',(r"\b(honestly|you know|like,|I mean|okay|alright)\b",'all'),'Drop register after a dense passage.','Do not let it become filler.')
c(Cc,'Profanity/edge spike','Mild profanity as emphasis.','fn','profanity_per_k','Gen: "what the hell"; Adam: rare ("where the hell").','Do not use in Adam mode more than 1-2x.')
c(Cc,'Clip/quote interrupt','Host frames audio or reads a quote.','rx',(r"\b(said|says|wrote|tweeted|posted|in (his|her|their) words|quote)\b",'all'),'Break narration with a voice every 1-3 min.','Do not stack clips.')
c(Cc,'Imperative directive','Sentences opening with Look/Think/Imagine/Take/Remember.','fn','imperative_share','Use to re-engage.','Do not command constantly.')
c(Cc,'On-screen reference','"Take a look / as you can see / this chart".','rx',(r"\b(take a look|as you can see|this (chart|graph|map|is a)|on (the )?screen|look at this)\b",'all'),'Mark [VISUAL] cues.','Do not reference visuals you will not show.')
c(Cc,'Rhetorical one-word answer','Question followed by a one-word answer sentence.','rx',(r"^(yes|no|nope|exactly|right|correct|wrong|nothing)[.!]$",'all'),'Use for rhythm.','Do not overuse.')
# D Direct address
D='D. Direct address & "you"'
c(D,'"You" density','Second-person per 1k words.','fn','you_per_k','Match group norm.','Do not write zero-"you" scripts.')
c(D,'"You" in the open','Second-person density in the first 10%.','fn','you_open','Pull the viewer in early.','Do not accuse the viewer.')
c(D,'"You" in the close','Second-person density in the last 15%.','fn','you_close','Hand agency to the viewer at the end.','Do not lecture.')
c(D,'"You guys" warmth','Plural casual address.','rx',(r"\byou guys\b",'all'),'Gen only.','Do not use in Adam mode.')
c(D,'"You\'ve probably" assumption','Assumed shared experience.','rx',(r"\byou'?ve probably|you probably|you may have|you might have|you'?ve (seen|heard)\b",'all'),'Use to build relatability.','Do not assume niche experiences.')
c(D,'"If you\'re" conditional address','Segmenting the audience ("If you\'re Elon Musk…", "if you\'re watching this").','rx',(r"\bif you'?re\b|\bif you (are|have|want|live|own)\b",'all'),'Put the viewer in a role.','Do not stack conditions.')
c(D,'Collective "we"','We/us/our density.','fn','we_per_k','Use "we" for society-level stakes.','Do not use royal "we" for the channel.')
c(D,'Host "I" presence','I/me/my density.','fn','i_per_k','Use I for investigator and opinion.','Do not center yourself over the story.')
# E Objection pre-emption
E='E. Viewer-objection pre-emption'
c(E,'Voiced viewer thought','"You\'re probably thinking / you might be wondering".','rx',(r"\b(you('re| are) (probably|might be) (thinking|wondering)|you might (say|think|wonder|be wondering)|I know what you'?re thinking|if you'?re wondering)\b",'all'),'Pre-empt the top objection.','Do not misstate the objection.')
c(E,'"My first thought"','Host admits the same initial reaction.','rx',(r"\b(my first thought|I (also )?thought|I used to think|I assumed|at first,? I)\b",'all'),'Gen: "my first thought, and probably yours, too".','Do not fake naivety.')
c(E,'"To be fair" concession','Fairness signal.','rx',(r"\b(to be fair|in fairness|that said|admittedly|to be clear)\b",'all'),'Concede, then rebut.','Do not end on concession.')
c(E,'"I\'m not saying"','Pre-empting misreading.','rx',(r"\b(I'?m not saying|this isn'?t to say|that doesn'?t mean|this doesn'?t mean)\b",'all'),'Narrow your claim.','Do not over-qualify.')
c(E,'Hype check','"Maybe this is just hype".','rx',(r"\b(hype|overblown|exaggerat\w*)\b",'all'),'Give the skeptic case its due.','Do not dismiss it in one line.')
c(E,'Hedge density','I think/probably/kind of/maybe per 1k.','fn','hedge_per_k','Hedge on predictions, not facts.','Do not hedge every sentence.')
# F Relatability
F_='F. Relatability anchors'
c(F_,'Wallet anchor','Money/price/bill words per 1k.','fn','money_per_k','Route stakes through money.','Do not lose the person in the macro.')
c(F_,'Everyday-object anchor','Subscriptions, games, rent, groceries, fast food, phone.','rx',(r"\b(subscription\w*|games?|rent|groceries|fast food|phone|netflix|youtube|electricity bill|coffee|burger|car)\b",'all'),'Name a household object.','Do not pick objects your audience does not use.')
c(F_,'Physical-scale anchor','"An acre / football field / the size of".','rx',(r"\b(acre|football field|the size of|as big as|as tall as|swimming pools?|homes?|households?)\b",'all'),'Translate big numbers to physical images.','Do not stack anchors.')
c(F_,'Personal anecdote','Host shares own experience.','rx',(r"\b(when I was|I remember|I'?ve been|I used to|my (friend|family|mom|dad|first))\b",'all'),'Brief, then back to topic.','Do not ramble.')
c(F_,'Named ordinary person','A non-famous person as the story vehicle.','rx',(r"\b(a (\d+-year-old|woman|man|guy|farmer|worker|student|mom|dad)|one (guy|woman|man|user))\b",'all'),'Put a face on the system.','Do not exploit victims.')
c(F_,'Shared-generation reference','"If you grew up / remember when".','rx',(r"\b(remember (when|the)|grew up|back when|as a kid)\b",'all'),'Nostalgia anchors.','Do not date your audience wrongly.')
# G Emotion calibration
G='G. Fear / outrage / hope calibration'
c(G,'Fear lexicon density','Danger/threat/catastrophe words per 1k.','fn','fear_per_k','Adam: high but evidenced.','Do not stack fear words in one sentence.')
c(G,'Fear in the open','Fear density first 10%.','fn','fear_open','Front-load stakes.','Do not open on gore.')
c(G,'Outrage lexicon density','Greed/scam/slop/cooked words per 1k.','fn','outrage_per_k','Gen: higher; Adam: low.','Do not insult viewers\' choices.')
c(G,'Hope lexicon density','Hope/solution/we can per 1k.','fn','hope_per_k','Balance alarm with agency.','Do not toxic-positivity.')
c(G,'Hope in the close','Hope density last 15%.','fn','hope_close','End with agency.','Do not end on doom only.')
c(G,'Sci-fi undercut','"Sounds like sci-fi / like a movie, but it\'s real".','rx',(r"\b(sci-?fi|science fiction|like a movie|plot of|sounds (crazy|insane|like))\b",'all'),'Use once, attributed correctly.','Do not reuse a guest\'s line as your own.')
c(G,'Wake-up framing','"Wake-up call / alarm / warning".','rx',(r"\b(wake-up call|alarm\w*|warning\w*|red flag)\b",'all'),'Pair with evidence.','Do not overuse.')
c(G,'Absurdity marker','"Wild / insane / crazy / weird".','rx',(r"\b(wild|insane|crazy|weird\w*|absurd|bizarre)\b",'all'),'Mark genuine strangeness.','Do not label routine facts wild.')
# H Us vs them
H='H. Us-versus-them framing'
c(H,'"They" density','They/them/their per 1k (actors vs. viewer).','fn','they_per_k','Name who "they" are.','Do not leave "they" undefined.')
c(H,'Institution as antagonist','Private equity, big tech, Wall Street, companies, billionaires.','rx',(r"\b(private equity|big tech|wall street|corporations?|billionaires?|the (companies|banks|government|rich|elites?)|these (companies|firms))\b",'all'),'Specific actor, specific action.','Do not blanket-villainize.')
c(H,'Viewer-as-victim frame','"They\'re charging you / betting that you…".','rx',(r"\b(betting (that )?you|charging you|making you|selling you|your data|at your expense|you'?re (paying|the product))\b",'all'),'Show the mechanism of harm.','Do not imply viewers are stupid.')
c(H,'Insider-vs-outsider','"Insiders / people in the know / employees".','rx',(r"\b(insiders?|employees|people (inside|in the know|close to)|whistleblower\w*|former (employee|staff))\b",'all'),'Use insider testimony for credibility.','Do not anonymize everything.')
c(H,'"Us" collective stakes','"We as a society / all of us".','rx',(r"\b(as a society|all of us|humanity|we all|everyone)\b",'all'),'Adam: civilization-level stakes.','Do not get preachy.')
# I Credibility
I='I. Credibility signals'
c(I,'Source density','Report/study/data/documents per 1k.','fn','credibility_per_k','Cite named sources in-flow.','Do not cite "studies show".')
c(I,'Exact numbers per minute','Digits per minute.','fn','num_per_min','Precise numbers > vague.','Do not use false precision.')
c(I,'Original interview signal','"I talked/spoke to / told me".','rx',(r"\bI (talked|spoke|asked|interviewed|reached out|sat down)\b|told (me|us)\b",'all'),'Highlight first-hand reporting.','Do not imply access you lack.')
c(I,'Research-process signal','"As I researched / I dug into / I read".','rx',(r"\b(as I (researched|dug|read|looked)|I (dug|read|went through|looked into|found))\b",'all'),'One line per act.','Do not narrate tedium.')
c(I,'Named expert','Expert + role.','rx',(r"\b(professor|researcher|scientist|economist|analyst|expert|engineer|former \w+)\b",'all'),'Name + role + why trust.','Do not appeal to anonymous authority.')
c(I,'Primary document','Filings, court docs, testimony, papers.','rx',(r"\b(court|filing\w*|lawsuit|testimony|unsealed|paper|memo|leaked|documents?|transcript)\b",'all'),'Show the document on screen.','Do not paraphrase without citing.')
c(I,'Honest-uncertainty signal','"We don\'t know exactly / it\'s unclear".','rx',(r"\b(we don'?t (know|have)|it'?s (unclear|not clear)|no one knows|hard to say|we can'?t be sure)\b",'all'),'Mark limits of evidence.','Do not hide uncertainty.')
# J Rewatch/share
J='J. Rewatch & share triggers'
c(J,'Quotable maxim','Short general claim ≤12 words with "is/are".','rx',(r"^(\w+\s){1,10}(is|are)\s(\w+\s?){1,6}[.!]$",'all'),'Write 2-4 clip-able lines.','Do not write fortune cookies.')
c(J,'Shocking stat line','Sentence with a number + "more than/every/all".','rx',(r"\d.*\b(more than|every|all|entire|per (day|year|second))\b",'all'),'Make the stat shareable alone.','Do not round dishonestly.')
c(J,'Exclusive-detail claim','"I haven\'t seen reported anywhere".','rx',(r"\b(haven'?t seen (this|it)? ?reported|anywhere else|first time|never before|exclusive)\b",'all'),'Back it up.','Do not overclaim.')
c(J,'Share prompt','"Share this / send this to".','rx',(r"\b(share (this|it)|send (this|it) to|show (this|it) to)\b",'all'),'Rare; only for civic asks.','Do not beg.')
# K Comment bait
K='K. Comment bait'
c(K,'Explicit comment ask','"Let me know in the comments / comment below".','rx',(r"\b(let me know|comment\w*|tell me (in|what|below))\b",'all'),'Ask a specific opinion question.','Do not ask "thoughts?".')
c(K,'Opinion poll question','"Do you think / would you".','rx',(r"\b(do you think|would you|what do you think|are you)\b.*\?$",'all'),'Pose a binary the audience can argue.','Do not ask leading questions.')
c(K,'Hot take','"Honestly / unpopular / I\'d argue".','rx',(r"\b(I'?d argue|unpopular|hot take|controversial|I'?ll say it|honestly,)\b",'all'),'One defensible stance.','Do not troll.')
# L Subscribe/CTA psychology
L='L. Subscribe & CTA psychology'
c(L,'Subscribe ask','Explicit subscribe line.','rx',(r"\bsubscrib\w*\b",'all'),'Tie to value ("if you want more…").','Do not ask in the first 30 s.')
c(L,'Newsletter funnel','Newsletter CTA.','rx',(r"\bnewsletter\b",'all'),'Gen: "free weekly newsletter" at end.','Do not pitch mid-hook.')
c(L,'Gratitude sign-off','Thank-you line.','rx',(r"\bthank(s| you)\b",'end'),'Warm, one line.','Do not grovel.')
c(L,'Patronage/support framing','"Being the reason / supporting the channel".','rx',(r"\b(support(ing)? (the|this|me|us)|being the reason|patreon|members?)\b",'all'),'Frame as shared mission.','Do not guilt-trip.')
c(L,'Sponsor-as-value','Sponsor framed as solving the problem just described.','rx',(r"\b(that'?s (exactly )?(where|why)|which is (exactly )?why I)\b",'all'),'Bridge from the topic.','Do not oversell.')
c(L,'Next-video handoff','"Watch this video next / see you in the next one".','rx',(r"\b(next (one|video)|another video|this video (here|right)|watch (this|next))\b",'end'),'Point at a specific next video.','Do not end abruptly.')
# M Parasocial
M='M. Parasocial cues'
c(M,'Opinion disclosure','"I think / I believe / I feel".','rx',(r"\bI (think|believe|feel|honestly)\b",'all'),'Share stance.','Do not overshare.')
c(M,'Emotional admission','"Honestly, this scared me / I was shocked".','rx',(r"\b(I was (shocked|surprised|scared|stunned|blown)|this (scared|terrified|shocked) me|freaked (me )?out)\b",'all'),'Admit genuine reaction once.','Do not perform.')
c(M,'Inclusive invitation','"Come with me / let\'s".','rx',(r"\b(come with me|let'?s|join me|together)\b",'all'),'Invite the viewer along.','Do not overuse.')
c(M,'Gratitude for audience','"you are the reason / thanks for being here".','rx',(r"\b(the reason (we|I)|thank you for (being|supporting)|because of you)\b",'all'),'Adam: end-card mission gratitude.','Do not grovel.')
# N Humor
N='N. Humor timing'
c(N,'Humor/aside lexicon','Weird/wild/literally/joke words per 1k.','fn','humor_per_k','Insert lightness after heavy beats.','Do not joke about victims.')
c(N,'Ironic understatement','"pretty harmless / not great / a little".','rx',(r"\b(not great|pretty (harmless|bad|wild)|a (little|bit) (much|concerning|awkward)|which is fine)\b",'all'),'Undercut drama with understatement.','Do not use for tragedies.')
c(N,'Callback humor','Reusing a phrase from earlier ("MechaHitler week").','rx',(r"\b(again|remember|as I said|like I said|back to)\b",'all'),'Callback an earlier odd detail.','Do not explain the joke.')
c(N,'Parenthetical aside','"which, honestly…/ and yes…".','rx',(r"\b(and yes|which,? (honestly|frankly|by the way)|by the way)\b",'all'),'Aside then return.','Do not chain asides.')
# O Density control
O='O. Information density control'
c(O,'Plain-language gloss','"basically / in other words / which means".','rx',(r"\b(basically|in other words|which means|that means|so,? essentially|in plain)\b",'all'),'Gloss after every dense line.','Do not gloss the obvious.')
c(O,'Analogy device','"It\'s like / think of it as".','rx',(r"\b(it'?s like|think of (it|this)|kind of like|like a|imagine)\b",'all'),'One analogy per concept.','Do not mix metaphors.')
c(O,'Recap micro-summary','"So, to recap / so basically / in short".','rx',(r"\b(so,? to recap|so basically|in short|long story short|so,? again|to put it simply)\b",'all'),'Micro-recap before each new act.','Do not recap every minute.')
c(O,'Definition on first use','"called / known as / what\'s called".','rx',(r"\b(called|known as|what'?s called|stands for)\b",'all'),'Define jargon.','Do not define twice.')
# P Stakes for you
P='P. Stakes for "you"'
c(P,'Personal consequence line','"you\'ll pay / your job / your money".','rx',(r"\b(you'?ll|you will|you could|you might|you'?re going to)\b.*\b(pay|lose|job|money|afford|bill|price|future|life)\b",'all'),'One personal consequence per act.','Do not threaten.')
c(P,'Future-you projection','"In 5 years you…/ your kids".','rx',(r"\b(your kids|your children|in (\d+|a few|ten|five) years|by 20\d\d)\b",'all'),'Project the stakes forward.','Do not predict certainty.')
c(P,'Agency for you','"What you can do / you can".','rx',(r"\b(what you can do|you can (help|do|join|call|sign|check|start)|get involved)\b",'all'),'Give one concrete action.','Do not leave viewers helpless.')
Q='Q. Sponsor & mid-roll retention'
c(Q,'Pre-sponsor cliffhanger','Question or "but" within 3 sentences before the sponsor block.','rx',(r"\?$|^but\b",'all'),'Leave an open question right before the read.','Do not resolve the loop before the read.')
c(Q,'Post-sponsor re-entry hook','"So back to it, because…" with a question.','rx',(r"^(so,? )?back to (it|the)|^anyway\b",'all'),'Re-enter with the loop you left open.','Do not re-enter with recap.')
R_='R. Comparative & contrast devices'
c(R_,'Then-vs-now contrast','"Back in / used to / now".','rx',(r"\b(used to|back in|years ago|nowadays|today,? )\b",'all'),'Contrast past and present.','Do not over-romanticize the past.')
c(R_,'Expectation-vs-reality','"You\'d think / you\'d expect / supposed to".','rx',(r"\b(you'?d (think|expect|assume)|supposed to|on paper|in theory)\b",'all'),'Set the expectation, break it.','Do not break it twice in one breath.')
c(R_,'Binary choice framing','"Either… or / two options".','rx',(r"\beither\b.*\bor\b|\btwo (options|choices|paths|possibilities)\b",'all'),'Use for scenario forks.','Do not make false binaries.')
S_='S. Viewer-role casting'
c(S_,'Viewer as investor/owner','"If you own / your 401k / your stocks".','rx',(r"\b(401\s?k|your (stocks?|portfolio|savings|retirement|investments?))\b",'all'),'Gen finance topics.','Do not give financial advice.')
c(S_,'Viewer as citizen','"Call your representative / vote / Congress".','rx',(r"\b(congress|representative|senator|vote|lawmakers|policy|regulat\w*)\b",'all'),'Adam civic stakes.','Do not partisan-bait.')
c(S_,'Viewer as consumer','"You\'re paying / your subscription".','rx',(r"\byou'?re (paying|buying|using)|your (subscription|account|data|order)\b",'all'),'Gen default casting.','Do not shame purchases.')
T_='T. Narrative suspense'
c(T_,'Countdown/time pressure','"Within days / by Friday / 16 hours".','rx',(r"\b(within (hours|days|weeks)|(\d+|sixteen|four) (hours|days)|by (monday|friday|the end))\b",'all'),'Use real deadlines.','Do not invent urgency.')
c(T_,'Cliffhanger "and then"','"And then… / And that\'s when".','rx',(r"^(and then|and that'?s when|that'?s when|then,)\b",'all'),'Use at story peaks.','Do not drain with overuse.')
c(T_,'Foreshadowing','"Little did / this would turn out / would later".','rx',(r"\b(would (later|turn out|soon|eventually)|little did|this (would|will) (become|matter))\b",'all'),'Foreshadow once per act.','Do not spoil the reveal.')
U_='U. Empathy & tone'
c(U_,'Validation line','"That makes sense / you can\'t blame".','rx',(r"\b(that makes sense|you can'?t blame|it'?s (understandable|natural|fair))\b",'all'),'Validate before challenging.','Do not patronize.')
c(U_,'Reassurance','"Don\'t worry / not for you, at least for now".','rx',(r"\b(don'?t worry|not (for )?you|at least for now|you'?re (fine|safe))\b",'all'),'Calibrate fear down after a scare.','Do not dismiss real risk.')
c(U_,'Moral clarity line','"That\'s not okay / this is wrong".','rx',(r"\b(that'?s (not okay|wrong|unacceptable)|this is (wrong|insane|unacceptable)|shouldn'?t be)\b",'all'),'One clear moral line.','Do not moralize repeatedly.')
