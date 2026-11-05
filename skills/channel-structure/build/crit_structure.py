import re
from corpus import fmt
def S(v): return v['sents']
def wc(t): return len(t.split())
def words_until(v,i): return sum(wc(s['text']) for s in S(v)[:i])
def secs_where(v,pred):
    return [s for s in S(v) if pred(s)]
def per_min(v,rx,a=0,b=101):
    R=re.compile(rx,re.I); ss=[s for s in S(v) if a<=s['pct']<b]
    mins=max(v['dur']*(b-a)/100/60,0.1); return round(sum(1 for s in ss if R.search(s['text']))/mins,2)
def sections(b): return [e for e in b['events'] if e['beat'] in ('SECTION TURN','QUESTION TURN (re-hook)')]
F={
 'dur_min': lambda v,b: round(v['dur']/60,1),
 'words_total': lambda v,b: v['words'],
 'wpm': lambda v,b: round(v['words']/(v['dur']/60)),
 'hook_sec': lambda v,b: S(v)[b['hook_end']]['t'],
 'hook_words': lambda v,b: words_until(v,b['hook_end']),
 'hook_pct': lambda v,b: S(v)[b['hook_end']]['pct'],
 'thesis_sec': lambda v,b: S(v)[b['thesis']]['t'] if b['thesis'] is not None else None,
 'first_sentence_words': lambda v,b: wc(S(v)[0]['text']),
 'n_sections': lambda v,b: len(sections(b)),
 'section_gap_pct': lambda v,b: round(80/max(len(sections(b)),1),1),
 'sections_per_10min': lambda v,b: round(len(sections(b))/(v['dur']/600),2),
 'question_turn_share': lambda v,b: round(100*sum(1 for e in sections(b) if e['beat'].startswith('QUESTION'))/max(len(sections(b)),1)),
 'sponsor_pct': lambda v,b: S(v)[b['spblocks'][0][0]]['pct'] if b['spblocks'] and S(v)[b['spblocks'][0][0]]['pct']<95 else None,
 'sponsor_sec_len': lambda v,b: (S(v)[b['spblocks'][-1][1]+1 if b['spblocks'][-1][1]+1<len(S(v)) else -1]['t']-S(v)[b['spblocks'][-1][0]]['t']) if b['spblocks'] and S(v)[b['spblocks'][0][0]]['pct']<95 else None,
 'has_midroll': lambda v,b: 1 if any(10<S(v)[x[0]]['pct']<90 for x in b['spblocks']) else 0,
 'conc_pct': lambda v,b: S(v)[b['conc']]['pct'] if b['conc'] is not None else None,
 'cta_count': lambda v,b: len(b['ctas']),
 'outro_sec': lambda v,b: round(v['dur']-S(v)[b['ctas'][0]]['t']) if b['ctas'] and S(v)[b['ctas'][0]]['pct']>80 else None,
 'q_per_min': lambda v,b: per_min(v,r'\?$'),
 'q_per_min_open': lambda v,b: per_min(v,r'\?$',0,10),
 'q_per_min_end': lambda v,b: per_min(v,r'\?$',85,101),
 'num_per_min': lambda v,b: per_min(v,r'\d|\b(million|billion|trillion|percent|half|double)\b'),
 'num_per_min_open': lambda v,b: per_min(v,r'\d|\b(million|billion|trillion|percent)\b',0,10),
 'year_mentions': lambda v,b: per_min(v,r'\b(19|20)\d\d\b'),
 'story_ratio': lambda v,b: round(100*sum(1 for s in S(v) if re.search(r"\b(was|were|had|did|said|went|told|came|began|started|decided|found)\b",s['text']) )/max(len(S(v)),1)),
 'explain_ratio': lambda v,b: round(100*sum(1 for s in S(v) if re.search(r"\b(is|are|means|works|because|basically|which means|in other words|so that)\b",s['text']) and not re.search(r"\b(was|were|had|did|said)\b",s['text']))/max(len(S(v)),1)),
 'you_open': lambda v,b: round(1000*sum(len(re.findall(r"\byou(r|'re|'ll|'ve)?\b",s['text'],re.I)) for s in S(v) if s['pct']<10)/max(sum(wc(s['text']) for s in S(v) if s['pct']<10),1),1),
 'you_all': lambda v,b: round(1000*sum(len(re.findall(r"\byou(r|'re|'ll|'ve)?\b",s['text'],re.I)) for s in S(v))/max(v['words'],1),1),
 'i_all': lambda v,b: round(1000*sum(len(re.findall(r"\b(I|I'm|I've|my|me)\b",s['text'])) for s in S(v))/max(v['words'],1),1),
 'mean_sent_words': lambda v,b: round(v['words']/max(len(S(v)),1),1),
 'hook_sent_words': lambda v,b: round(sum(wc(s['text']) for s in S(v)[:b['hook_end']+1])/max(b['hook_end']+1,1),1),
 'end_sent_words': lambda v,b: round(sum(wc(s['text']) for s in S(v) if s['pct']>=90)/max(sum(1 for s in S(v) if s['pct']>=90),1),1),
 'title_words': lambda v,b: wc(v['title']) if v['title'] else None,
 'title_in_hook': lambda v,b: (lambda tw: round(100*len([w for w in tw if w in ' '.join(s['text'].lower() for s in S(v) if s['pct']<8)])/max(len(tw),1)))([w for w in re.findall(r"[a-z']{4,}",v['title'].lower()) if w not in ('this','that','with','your','will','from','they','what','about','really')]) if v['title'] else None,
 'title_question': lambda v,b: (1 if '?' in v['title'] else 0) if v['title'] else None,
 'title_how_why': lambda v,b: (1 if re.match(r"(how|why|what|wtf|if)\b",v['title'],re.I) else 0) if v['title'] else None,
 'title_number': lambda v,b: (1 if re.search(r'\d',v['title']) else 0) if v['title'] else None,
 'recap_end': lambda v,b: 1 if any(re.search(r"\b(so to (recap|sum)|in short|all of this|everything we|so yeah|so basically)\b",s['text'],re.I) for s in S(v) if s['pct']>85) else 0,
 'callback_end': lambda v,b: (lambda op: round(100*len(op & set(w for s in S(v) if s['pct']>92 for w in re.findall(r"[a-z]{6,}",s['text'].lower())))/max(len(op),1)))(set(w for s in S(v) if s['pct']<4 for w in re.findall(r"[a-z]{6,}",s['text'].lower()))),
 'density_curve_q': lambda v,b: round(per_min(v,r'\?$',40,60)/max(per_min(v,r'\?$',0,10),0.01),2),
 'sponsor_bridge': lambda v,b: (1 if b['spblocks'] and re.search(r"that'?s (exactly )?(where|why)|speaking of|especially with",S(v)[b['spblocks'][0][0]]['text'],re.I) else 0) if b['spblocks'] else None,
}
# (category, name, definition, kind, spec, do, dont)
C=[]
def c(cat,name,defi,kind,spec,do,dont): C.append(dict(cat=cat,name=name,defi=defi,kind=kind,spec=spec,do=do,dont=dont))
# --- A. Length & format strategy
c('A. Length & runtime strategy','Runtime','Total runtime of the finished video.', 'fn','dur_min','Plan Adam-mode essays at 32-43 min; Gen-mode explainers at 16-23 min; mechanism explainers 16-35.','Do not pad a 20-min Gen topic to 40 min, or squeeze an Adam investigation into 15.')
c('A. Length & runtime strategy','Total host words','Host-narration word count (guests removed).','fn','words_total','Budget words from runtime x WPM before outlining.','Do not count clip/guest audio as script words.')
c('A. Length & runtime strategy','Narration pace (WPM)','Host words per minute of runtime; lower = more clips/b-roll breathing room.','fn','wpm','Adam 144-177 WPM (clip pauses); Gen 178-200 WPM; especially up to 215.','Do not write at 220+ WPM; it will not fit.')
c('A. Length & runtime strategy','Mean sentence length','Average words per host sentence across the video.','fn','mean_sent_words','Keep the mean near the group norm; vary within it.','Do not write uniform 25-word sentences.')
c('A. Length & runtime strategy','Hook sentence length','Average sentence length inside the cold open (to the promise).','fn','hook_sent_words','Hook sentences run shorter or equal to body sentences.','Do not open with a 40-word paragraph sentence.')
c('A. Length & runtime strategy','Closing sentence length','Average sentence length in final 10%.','fn','end_sent_words','Shorten sentences as you land.','Do not end on a long caveat chain.')
c('A. Length & runtime strategy','Words per section','Host words divided by section count (pacing budget per act).','fn','section_gap_pct','Target one major turn every ~6-12% of runtime.','Do not run 25% of runtime with no turn.')
# --- B. Hook
c('B. Cold open / hook','Hook length (seconds)','Seconds from 0:00 to the first explicit promise/roadmap line.','fn','hook_sec','Land the promise by ~0:15-1:35; Adam 0:12-2:07.','Do not delay the promise past ~2:15.')
c('B. Cold open / hook','Hook length (words)','Host words before the promise line.','fn','hook_words','Adam 19-250 words (median 186); Gen 65-688 (median 266); especially 145-411.','Do not exceed ~400 words before telling viewers what they get.')
c('B. Cold open / hook','Hook as % of runtime','Promise position as % of runtime.','fn','hook_pct','Promise inside the first ~1-8%.','Do not put the promise after 10%.')
c('B. Cold open / hook','First sentence length','Word count of sentence one.','fn','first_sentence_words','Sentence one is short and concrete (5-20 words).','Do not begin with throat-clearing or a greeting (except a deliberate show-format open).')
c('B. Cold open / hook','Dated-event open','Opening on an exact date/time/duration.','rx',(r"\b(on (monday|tuesday|wednesday|thursday|friday|saturday|sunday|january|february|march|april|may|june|july|august|september|october|november|december)|in the year \d{4}|for \d+ hours|in (19|20)\d\d)\b",'hook'),'Use a dated event when the story is a news incident (Adam default).','Do not fake a date for an evergreen topic.')
c('B. Cold open / hook','Number-first open','A statistic or figure in the first 8%.','rx',(r"\d|\b(million|billion|trillion|percent)\b",'hook'),'Drop one surprising, sourced number early.','Do not stack 5 numbers before the viewer knows the topic.')
c('B. Cold open / hook','Second-person scene open','Opening that puts the viewer in a scene ("Take a look at…", "Think about…", "let\'s buy a house together").','rx',(r"^(so,? )?(take a look|think about|imagine|picture|let'?s|come with me|you'?ve probably|when you hear|you)",'hook'),'Gen default: start inside the viewer\'s life.','Do not use "imagine" for a news incident that is stranger than fiction.')
c('B. Cold open / hook','Mood/scene line open','Short atmospheric line ("It was a strange summer.").','rx',(r"^(it was|this is|there'?s|there is|there was)\b.{0,40}$",'hook'),'Use one short mood line, then hard facts.','Do not stack mood lines.')
c('B. Cold open / hook','Contradiction hook','A "but" twist inside the hook that reverses the expectation.','rx',(r"^but\b|\bbut (what|in fact|the|it|here|that|no one|nobody)\b",'hook'),'Twist within 30 seconds.','Do not deliver a hook with no reversal.')
c('B. Cold open / hook','"No one is talking about" gap','Explicit claim the angle is under-reported.','rx',(r"\b(no one|nobody) (is|has been|seems to be) (talking|telling|asking|reporting)|haven'?t seen reported|no one has told you|not telling you\b",'open'),'Use once, backed by a real under-covered fact.','Do not claim exclusivity you cannot back.')
c('B. Cold open / hook','Hook question','A direct question in the first 8%.','rx',(r"\?$",'hook'),'End the hook on a question the video answers.','Do not ask three questions in a row with no anchor.')
c('B. Cold open / hook','Questions per minute in opening','Question density in first 10%.','fn','q_per_min_open','Front-load questions more than mid-video.','Do not leave the open as pure statement.')
c('B. Cold open / hook','Numbers per minute in opening','Numeric density in the first 10%.','fn','num_per_min_open','~1.5-2.8 number-bearing sentences/min in the first 10%.','Do not open number-free on a money topic.')
c('B. Cold open / hook','Clip-led cold open','Opening that intercuts guest/news audio before host speaks at length.','rx',(r"^(it was a strange|sounds like|like this is|here'?s)\b",'hook'),'Adam/oil: clip montage then host line; mark clips [CLIP].','Do not write clips into host lines.')
c('B. Cold open / hook','Familiar-to-absurd ladder','Hook moves from a familiar unit to an absurd scale.','rx',(r"\b(an acre|football field|the size of|as much as|equivalent to|more than (the|all)|bigger than)\b",'open'),'Anchor the scale in a known unit first.','Do not cite a raw huge number without an anchor.')
# --- C. Thesis & promise
c('C. Thesis, stakes & promise','Thesis position (seconds)','Time of first explicit thesis/stakes line.','fn','thesis_sec','State the thesis by ~0:35 (Adam) / ~0:00-1:20 (Gen).','Do not hide the thesis to the midpoint.')
c('C. Thesis, stakes & promise','"Wake-up call" framing','Naming the story as a warning/turning point.','rx',(r"\b(wake-up call|warning|turning point|alarm|this changes|this is (bigger|worse))\b",'open'),'Pair the hook with "and more importantly…".','Do not catastrophize without evidence.')
c('C. Thesis, stakes & promise','First-person promise','"I want to take you through / tell you the full story".','rx',(r"\bI want to (take|tell|walk|show|explain|talk|start)|I'?m going to (show|explain|walk|tell)|I wanted to\b",'open'),'Adam signature: "I want to take you step-by-step through…".','Do not promise "everything you need to know".')
c('C. Thesis, stakes & promise','Collective "let\'s" promise','Roadmap phrased as joint exploration.','rx',(r"\blet'?s (break|dive|talk|look|figure|find|go|start|get into)",'open'),'Gen/others: "so let\'s break down…".','Do not use "let\'s dive in" with nothing after it.')
c('C. Thesis, stakes & promise','Question-as-thesis','Thesis posed as the video\'s central question.','rx',(r"^(so,? )?(what|why|how|is|are|can|could|will|does|do)\b.*\?$",'open'),'Gen: "then what the hell happens to the economy now?"','Do not answer the central question in the hook.')
c('C. Thesis, stakes & promise','Stakes for "you"','The hook names the consequence for the viewer.','rx',(r"\b(you|your)\b.*\b(pay|lose|job|money|life|future|bill|rent|house|afford)\b",'open'),'Make stakes personal within 60 s.','Do not keep stakes abstract ("society").')
c('C. Thesis, stakes & promise','Roadmap specificity','Promise that names steps/parts ("step-by-step", "three main players").','rx',(r"\b(step[- ]by[- ]step|three|four|two|first|the full story|how .* and why)\b",'open'),'Name the shape of the journey.','Do not list 7 chapters out loud.')
c('C. Thesis, stakes & promise','Exclusive-detail promise','Promise of details "I haven\'t seen reported anywhere else".','rx',(r"\b(haven'?t seen|anywhere else|for the first time|exclusive|never (been )?(seen|told|reported)|I (found|spoke|talked))\b",'open'),'Back it with a real interview/document.','Do not use as filler.')
# --- D. Act/section breakdown
c('D. Acts & sections','Section count','Detected major turns (section + question turns).','fn','n_sections','Plan 6-12 turns per video.','Do not write one undivided body.')
c('D. Acts & sections','Turns per 10 minutes','Section density per 10 minutes.','fn','sections_per_10min','Adam ~1.5-2.4 per 10 min; Gen/especially ~3.1 per 10 min.','Do not exceed one turn per minute.')
c('D. Acts & sections','Question-turn share','Share of turns that open with a question.','fn','question_turn_share','Open ~25-50% of sections with a question.','Do not open every section with a question.')
c('D. Acts & sections','"So," turn opener','Section opens with "So,…/So now/So how".','rx',(r"^so,? ",'body'),'Gen\'s main turn word; Adam uses it for logic turns.','Do not start 3 consecutive sentences with So.')
c('D. Acts & sections','"Now," turn opener','Section opens with "Now,".','rx',(r"^now,? ",'body'),'Adam: "Now, we don\'t know exactly how…" — scope shift.','Do not use Now as a time word confusion.')
c('D. Acts & sections','"But then" escalation turn','Narrative reversal opener.','rx',(r"^but then\b",'body'),'Use at act breaks in story videos.','Do not use for minor points.')
c('D. Acts & sections','"But here\'s" pivot','"But here\'s the thing / where / the part…".','rx',(r"^but here'?s\b",'all'),'Use 1-3 times as reveal pivots.','Do not use more than once per 5 min.')
c('D. Acts & sections','"Which brings us" callback turn','Turn that ties a digression back to the main story.','rx',(r"\bwhich brings (us|me)\b",'body'),'Return to the cold-open incident mid-video.','Do not use without a prior digression.')
c('D. Acts & sections','Enumerated sections','First/Second/Third or "the next reason".','rx',(r"^(first|second|third|fourth|finally|the (first|second|third|next|last) (reason|thing|problem|step|part))\b",'body'),'Use numbering for lists of causes.','Do not number narrative beats.')
c('D. Acts & sections','Flashback turn','Section opens with a past year/time jump.','rx',(r"^(back in|in (19|20)\d\d|years (ago|earlier)|fast[- ]forward|a (few|couple) (years|months) (ago|later))",'body'),'Use chronology jumps to reset curiosity.','Do not jump more than twice without returning.')
c('D. Acts & sections','Mechanism section marker','"To understand X, you need…" explainer entry.','rx',(r"\bto understand\b|\bhere'?s how\b|\bthe way (it|this) works\b",'all'),'Signal explainer mode explicitly.','Do not start jargon before the marker.')
c('D. Acts & sections','Interview/source section','Section built around "I talked/spoke to…".','rx',(r"\bI (talked|spoke|asked|interviewed|reached out|met)\b",'all'),'Adam: original interviews mid-video.','Do not fabricate access.')
# --- E. Beat timing
c('E. Beat timing','Midroll sponsor position','Sponsor start as % of runtime.','fn','sponsor_pct','Gen 20-46% (median 39%); especially either early (4-6%) or ~38%; oil 27.5%; Adam: no midroll.','Do not drop the sponsor in the first 60 s or after 60%.')
c('E. Beat timing','Sponsor read length','Seconds of the sponsor block.','fn','sponsor_sec_len','30-75 s; one block.','Do not run 2+ minutes.')
c('E. Beat timing','Has midroll','Whether a mid-video sponsor exists.','fn','has_midroll','Gen/others: yes; Adam: patronage/end-card only.','Do not add a midroll in Adam mode.')
c('E. Beat timing','Sponsor bridge line','Sponsor introduced by a topical bridge ("that\'s where…comes in").','fn','sponsor_bridge','Bridge from the problem just described.','Do not cold-cut "This video is sponsored by" mid-argument (unless show format).')
c('E. Beat timing','Conclusion start %','Where the conclusion begins.','fn','conc_pct','Begin landing at ~75-95% (Adam median 82%, Gen 86%).','Do not start the conclusion before 75%.')
c('E. Beat timing','Outro length','Seconds from first closing CTA to end.','fn','outro_sec','Keep outro 10-60 s.','Do not run a 2-minute outro.')
c('E. Beat timing','Return from sponsor line','"Back to it / So back to…" re-entry.','rx',(r"^(so,? )?back to (it|the|our)|^anyway\b",'body'),'Re-enter with a question or the open loop.','Do not resume with a dry fact.')
# --- F. Evidence stacking
c('F. Evidence stacking','Numbers per minute','Density of numerals/magnitudes over the whole video.','fn','num_per_min','Adam ~1.1-2.5 per min; Gen ~1.0-3.4; oil/especially ~1.8.','Do not exceed ~8/min.')
c('F. Evidence stacking','Year anchors per minute','Explicit years.','fn','year_mentions','Anchor timeline with years.','Do not leave chronology vague.')
c('F. Evidence stacking','Named-source attribution','"According to / reported / a study / data from".','rx',(r"\b(according to|reported|report(ed)? by|a (new )?(study|report|paper|survey)|data from|filings?|documents?|testimony|told (the|reuters|bloomberg|cnbc))\b",'all'),'Name the source in-sentence.','Do not say "experts say" unnamed.')
c('F. Evidence stacking','Quoted-person evidence','Host quotes a named person ("X said…", "in his words").','rx',(r"\b(said|says|wrote|writes|tweeted|posted|told)\b",'all'),'Quote short and in-flow.','Do not paste long block quotes.')
c('F. Evidence stacking','Comparison anchor','"That\'s more than / equivalent to / roughly as much as".','rx',(r"\b(more than|less than|equivalent to|as much as|the same as|roughly|about the size|compared to)\b",'all'),'Every big number gets a comparison.','Do not compare to another unfamiliar number.')
c('F. Evidence stacking','Escalating "and" stacks','Evidence chained with "And…" sentence openers.','rx',(r"^and\b",'body'),'Stack 2-3 facts then interpret.','Do not open 5 sentences in a row with And.')
c('F. Evidence stacking','Example-then-generalize','"For example / for instance / take X".','rx',(r"\b(for example|for instance|take (a look at|the case)|like when|case in point)\b",'all'),'Give one concrete case before the rule.','Do not generalize without a case.')
c('F. Evidence stacking','Consequence chain','"Which means / that means / in other words".','rx',(r"\b(which means|that means|in other words|so basically)\b",'all'),'Oil/Gen: chain one consequence per beat.','Do not chain more than 3 deep.')
# --- G. Argument escalation
c('G. Argument escalation','Escalation markers','"Even worse / but it gets / what\'s more / on top of that".','rx',(r"\b(even (worse|more)|it gets (worse|weirder|crazier)|on top of that|what'?s (more|worse|crazier)|and it doesn'?t stop|not only)\b",'all'),'Raise stakes each act.','Do not escalate with adjectives alone.')
c('G. Argument escalation','Scale-up turn','Moving from a single case to the system ("this isn\'t just…").','rx',(r"\b(this isn'?t just|it'?s not just|not just (one|a|the)|bigger than|the whole (industry|system|economy|country))\b",'all'),'Zoom out at ~40-70%.','Do not zoom out before the case is clear.')
c('G. Argument escalation','Future projection','"Is going to / will / by 20XX".','rx',(r"\b(is going to|are going to|will (be|have|become)|by (20\d\d|the end of))\b",'close'),'Project forward in the final quarter.','Do not make certain predictions without hedges.')
c('G. Argument escalation','Hedged commitment','"I think / probably / to be clear" followed by commitment.','rx',(r"\b(I think|probably|to be clear|to be fair|I'?m not saying|honestly)\b",'all'),'Hedge then land.','Do not hedge every claim.')
# --- H. Counterarguments
c('H. Counterargument handling','Voiced objection','"You might be thinking / you\'re probably thinking / some people say".','rx',(r"\b(you('re| are) (probably|might be) thinking|you might (say|think|be wondering)|some (people|would) (say|argue)|critics|skeptics|you could argue|the counter ?argument)\b",'all'),'Voice the strongest objection mid-video.','Do not strawman.')
c('H. Counterargument handling','"To be fair" concession','Concession marker.','rx',(r"\b(to be fair|in fairness|admittedly|granted|that said|that being said)\b",'all'),'Concede once per act, then return.','Do not end on the concession.')
c('H. Counterargument handling','Hype/skeptic check','Explicitly testing whether it\'s hype.','rx',(r"\b(hype|overblown|exaggerat|skeptic|maybe (this|it|a lot) .* (just|isn))\b",'close'),'Adam: "But also, maybe a lot of this is just hype?" near 85%.','Do not skip the skeptic pass in AI-risk topics.')
c('H. Counterargument handling','Rebuttal turn','"But / And yet / The problem is" right after a concession.','rx',(r"^(and yet|but the problem|the problem is|except)\b",'all'),'Rebut with evidence, not tone.','Do not rebut with sarcasm alone.')
# --- I. Explainer vs narrative
c('I. Explainer vs narrative mix','Narrative-sentence share','% sentences in past-tense story mode.','fn','story_ratio','Proxy only: keep a real story beat every 2-3 minutes; see measured shares.','Do not write pure lecture.')
c('I. Explainer vs narrative mix','Explainer-sentence share','% sentences in present-tense mechanism mode.','fn','explain_ratio','Balance with story share.','Do not explain for >2 min without a story beat.')
c('I. Explainer vs narrative mix','Analogy/physical picture','"Think of it like / imagine / it\'s like".','rx',(r"\b(think of it|it'?s like|imagine|kind of like|picture this|like a)\b",'all'),'Physical picture before jargon.','Do not mix two analogies in one beat.')
c('I. Explainer vs narrative mix','Jargon gloss','"basically / which is / called / known as".','rx',(r"\b(basically|known as|what'?s called|called|i\.e\.|aka)\b",'all'),'Gloss every term on first use.','Do not gloss common words.')
c('I. Explainer vs narrative mix','Character introduction','Named person + role on first mention.','rx',(r"\b(a \d+-year-old|named|founder|CEO|researcher|scientist|former)\b",'all'),'Give age/role/stake in one clause.','Do not introduce 4 characters in one minute.')
c('I. Explainer vs narrative mix','Scene-time markers','"That night / days later / at 3 a.m." in narrative.','rx',(r"\b(that (night|day|morning|week)|(days|hours|weeks|months) later|the next (day|morning)|within (hours|days))\b",'all'),'Use time markers to pace story acts.','Do not overuse in explainer sections.')
# --- J. Chapter logic
c('J. Chapter logic','Chapter-titled turns','Explicit chapter names / parts.','rx',(r"^(part|chapter|step) (one|two|three|\d)|^(okay|alright),? so\b",'all'),'Mark chapters in the edit even if not spoken.','Do not announce "chapter 1" in Adam mode.')
c('J. Chapter logic','Section-ending mini-cliff','A section ends with a question or "but".','rx',(r"(\?|\bbut\b.*\.)$",'body'),'End chapters on an open loop.','Do not end chapters on a summary.')
c('J. Chapter logic','"So what" pivot','"So what does this mean / so why does this matter".','rx',(r"^so,? (what|why) (does|do|is|happens)|why (does|should) (this|any of this|that) matter",'all'),'Use once at the mechanism→stakes turn.','Do not overuse.')
# --- K. Pacing
c('K. Pacing per minute','Questions per minute','Overall question density.','fn','q_per_min','~0.3-1.1 questions/min (Adam lowest ~0.4).','Do not exceed 2/min.')
c('K. Pacing per minute','Mid vs open question ratio','Ratio of 40-60% question density to opening density.','fn','density_curve_q','Re-raise questions mid-video (Gen ~0.5x the opening rate, especially ~1.0x).','Do not let the middle go question-free.')
c('K. Pacing per minute','Closing question density','Questions per minute in last 15%.','fn','q_per_min_end','Close with 1-3 reflective questions.','Do not close with a barrage.')
c('K. Pacing per minute','Short punch sentence','Sentences ≤5 words.','rx',(r"^\S+(\s\S+){0,4}$",'all'),'Use after a long build.','Do not stack 4 punches.')
c('K. Pacing per minute','Long build sentence','Sentences ≥35 words.','rx',(r"^(\S+\s+){34,}\S+",'all'),'Use for cascades, then punch.','Do not exceed 1 in 8.')
# --- L. Open loops
c('L. Open loops across sections','Deferred-reveal loop','"We\'ll get to / more on that later / I\'ll come back".','rx',(r"\b(we'?ll get (to|back)|more on (that|this) (later|in a (bit|second|minute))|I'?ll (come back|explain|get to)|later in (this|the) video|stick around|in a (bit|minute|second))\b",'all'),'Open 1-3 explicit loops and close each.','Do not open loops you never close.')
c('L. Open loops across sections','"But first" detour','Delaying the payoff with context.','rx',(r"\bbut first\b|\bbefore (we|I) (get|go|answer)\b",'all'),'Use once to justify a context section.','Do not use twice in a row.')
c('L. Open loops across sections','Mystery framing','"Nobody knows why / no one could explain".','rx',(r"\b(no one|nobody) (knows|could explain|understands|can say)|mystery|unexplained|still (don'?t|doesn'?t) know\b",'all'),'Plant a mystery that the video partially solves.','Do not fake mystery about known facts.')
c('L. Open loops across sections','Rhetorical cliff question','Question that ends a section.','rx',(r"\?$",'body'),'Re-open at section breaks.','Do not answer it in the very next sentence every time.')
# --- M. Conclusion architecture
c('M. Conclusion architecture','Conclusion marker','"Here\'s the thing / ultimately / at the end of the day".','rx',(r"\b(here'?s the thing|ultimately|at the end of the day|in the end|so where does)\b",'close'),'Signal landing once.','Do not say "in conclusion".')
c('M. Conclusion architecture','Recap at end','Explicit recap in the last 15%.','fn','recap_end','Prefer synthesis to recap.','Do not list every point again.')
c('M. Conclusion architecture','Callback to opening','% of distinctive opening words reused in last 8%.','fn','callback_end','Echo the cold-open image.','Do not introduce brand-new facts in the last 30 s.')
c('M. Conclusion architecture','Action ask / what to do','"Here\'s what you can do / call your rep / sign up".','rx',(r"\b(what you can do|you can (help|do|join|sign|call|check)|get involved|take action|make it happen|reach out)\b",'close'),'Adam: concrete civic ask; Gen: newsletter.','Do not end with despair only.')
c('M. Conclusion architecture','Hope/agency turn','Closing line of hope or agency.','rx',(r"\b(hope|optimis|we can|it'?s not too late|there'?s still|we still have|good news)\b",'close'),'Turn toward agency after the alarm.','Do not fake optimism.')
c('M. Conclusion architecture','Thank-you sign-off','"Thank you so much for watching / see you in the next one".','rx',(r"\b(thank(s| you)( so much)? for watching|see you in the next|see you next)\b",'end'),'One line, warm.','Do not add three sign-offs.')
c('M. Conclusion architecture','Newsletter/next-video CTA','Closing pitch for newsletter/next video.','rx',(r"\b(newsletter|next video|another video|this video (here|right here)|check out)\b",'end'),'Gen: newsletter + next-video card.','Do not pitch merch and newsletter and Patreon all at once.')
c('M. Conclusion architecture','CTA count','Number of CTA lines.','fn','cta_count','1-4 CTA lines total.','Do not exceed 5.')
# --- N. Topic / angle / title
c('N. Topic, angle & title alignment','Title length','Words in title.','fn','title_words','5-10 words.','Do not exceed 12.')
c('N. Topic, angle & title alignment','How/Why/What title','Title opens with How/Why/What/WTF/If.','fn','title_how_why','Gen formula: "How X Will Break Y".','Do not use a bland label title.')
c('N. Topic, angle & title alignment','Title question mark','Title is a literal question.','fn','title_question','Rare; use for "WTF/If…why" formats.','Do not default to questions.')
c('N. Topic, angle & title alignment','Number in title','Title contains a number.','fn','title_number','Use when the figure is the hook ($110M).','Do not invent precision.')
c('N. Topic, angle & title alignment','Title-hook word overlap','% of title content words appearing in first 8%.','fn','title_in_hook','Pay off the title words in the cold open.','Do not bait-and-switch.')
c('N. Topic, angle & title alignment','Villain/institution angle','Topic framed around an actor (private equity, big tech, Musk, OpenAI).','rx',(r"\b(private equity|big tech|wall street|openai|musk|altman|billionaire|corporations?|the government|china)\b",'open'),'Pick an angle with an accountable actor.','Do not make the villain cartoonish.')
c('N. Topic, angle & title alignment','Viewer-life angle','Topic tied to viewer\'s spending/job/home.','rx',(r"\b(your (job|money|bills?|rent|house|subscriptions?|electricity|kids|favorite))\b",'open'),'Gen: always route through your wallet.','Do not stay abstract.')
c('N. Topic, angle & title alignment','Timeliness peg','"Just / this week / right now / recently".','rx',(r"\b(just (announced|released|happened|used)|this (week|year|month)|right now|recently|last (week|month))\b",'open'),'Peg evergreen analysis to a fresh event.','Do not date-stamp evergreen essays needlessly.')
# --- O. Voice-in-structure
c('O. Structural voice signals','"You" density in open','Second-person per 1k words in first 10%.','fn','you_open','Gen median ~28/1k in the open; Adam ~13; oil ~28; especially ~9.','Do not write "you" in every clause.')
c('O. Structural voice signals','"You" density overall','Second-person per 1k words.','fn','you_all','Match group norm.','Do not drop to 0.')
c('O. Structural voice signals','First-person density','I/me/my per 1k words.','fn','i_all','Adam uses "I" as investigator.','Do not make it a vlog.')
c('O. Structural voice signals','Self-research disclosure','"As I researched / what I found".','rx',(r"\b(as I (researched|dug|looked)|what I found|I (found|discovered|noticed|realized))\b",'all'),'Use once per act to frame discoveries.','Do not narrate your process at length.')
c('O. Structural voice signals','Clip framing line','Host line introducing archival/guest audio.','rx',(r"\b(here'?s (what|how) (he|she|they)|this is (him|her|musk|altman)|in (his|her) words|listen to)\b",'all'),'Frame every clip in one line.','Do not drop unexplained clips.')
c('O. Structural voice signals','Mid-script direct question to viewer','"Do you really think…?", "you know what?".','rx',(r"\b(do you (really )?(think|know|remember)|have you (ever|noticed))\b",'all'),'1-3 times per video.','Do not interrogate.')
