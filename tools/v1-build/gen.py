import json,re,random,collections,statistics as st,os,csv,corpus,pool,exams,antipat
S=json.load(open('stats.json'));L=S['lang'];T=S['story'];DOCS=S['docs']
WF=os.environ.get('CHANNEL_SKILLS_DIR',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','skills'))
G=['adam','gen','especially','oil','after'];GN={'adam':'Adam (7x)','gen':'Gen (4x)','especially':'Especially 01/02/06 (3x)','oil':'Oil 03 (5x)','after':'After (1x)'}
P=pool.passages()
def wr(p,s):
    os.makedirs(os.path.dirname(p),exist_ok=True);open(p,'w').write(s)
def f(x): return f"{x:.2f}" if isinstance(x,float) else str(x)
def gtab(byg): return ' | '.join(f(byg[g]) for g in G)
def qblock(qs):
    return '\n'.join(f"  - **{GN[q['group']]}** `{q['file']}`: \"{q['q']}\"" for q in qs) or '  - (no verified quote in corpus)'
CORPUS_TABLE="| corpus | files | weight per file | host words used | notes |\n|---|---|---|---|---|\n"
for g in G:
    ds=[d for d in DOCS if d['group']==g]
    CORPUS_TABLE+=f"| {GN[g]} | {len(ds)} | {ds[0]['w']} | {sum(d['nw'] for d in ds)} | {'pre-filtered by speaker-filter.md' if g=='adam' else 'guest/news labels and micro-clips dropped: '+str(sum(d['dropped'] for d in ds if isinstance(d['dropped'],int)))+' units'}{'; 7.txt is unpunctuated auto-caption: lexical rates only, excluded from sentence stats' if g=='gen' else ''} |\n"
CORPUS_TABLE+="\nEspecially 04/05/07 duplicate Adam videos and are counted only as Adam. Weighted statistics = sum(file weight x file rate) / sum(file weight). Total weight: Adam 35, Gen 40 (36 for sentence stats), Especially 9, Oil 5, After 12.\n"
def mkpass(rng,k,excl):
    return pool.sample_by_weight(P,k,rng,excl)
# ---------------- shared helpers
def ex_label(t):
    l=t.lower();lab=[]
    for c in T:
        if c['pos'] is None and re.search(c['rx'],l): lab.append(c['cat'])
    return ', '.join(sorted(set(lab))[:4]) or 'narration'
def lang_dim_lookup(name): return next(x for x in L if x['name']==name)
def by(name,g): return lang_dim_lookup(name)['by_group'][g]
def wt(name): return lang_dim_lookup(name)['weighted']
conn={g:by('Opener: And',g)+by('Opener: But',g)+by('Opener: So',g) for g in G};conn['w']=wt('Opener: And')+wt('Opener: But')+wt('Opener: So')
# ================= SKILL 1: LANGUAGE
def lang_skill():
    R=f'{WF}/channel-language'
    def row(n): x=lang_dim_lookup(n); return f"| {n} | **{f(x['weighted'])}** | {gtab(x['by_group'])} |"
    keys=['Mean sentence length (words)','Median sentence length','Sentence-length spread (SD)','Short sentences (<=6 words) %','Long sentences (>=30 words) %','Questions %','Exclamations %','Opener: So','Opener: And','Opener: But','Opener: Because','Opener: It','Opener: The','Opener: I','Opener: We','Opener: You','Opener: Well','Opener: Okay/OK','just','really','actually','basically','kind of','sort of','you know','I think','I mean','probably','a lot','which means','in other words','turns out','you/your','I/me/my','we/us/our','contractions','swearing','slang (cooked/insane/crazy/wild/huge)','gonna/wanna/gotta','numerals','money','percent','years','em/en dashes','semicolons','AI-tell vocabulary','essay connectors']
    TAB="| dimension | blended (weighted) | Adam | Gen | Especially | Oil | After |\n|---|---|---|---|---|---|---|\n"+'\n'.join(row(k) for k in keys)
    skill=f"""---
name: channel-language
description: Write or humanize YouTube script narration in the user's channel voice, a word-level blend of Adam (7x), Gen (4x), Oil (5x), the Especially set (3x) and After (1x). Use when the user asks to write, rewrite, punch up, de-AI, or humanize a script, voiceover, hook, or narration line for the channel; when text "sounds like AI"; or when they ask for Adam-lean, Gen-lean, or oil-lean wording. Not for story structure (use channel-storytelling).
---

# Channel language: blended voice and humanizer

## Purpose
Make every sentence of a channel script sound like these hosts talking: spoken rhythm, fillers at the real rate, contractions, exact numbers, plain words, and none of the machine tells. This skill works at the word and sentence level. For beats, hooks, and arcs use `channel-storytelling`, then come back here for the line-by-line pass.

## When to use
- "Write the narration / voiceover / script for ..." (after the story beats exist)
- "Humanize this", "make it sound less AI", "make it sound like the channel"
- "Make it more Adam / more Gen / more like the oil video"
- Checking a draft for AI tells before recording

Do not use it for factual research. Never invent facts or quotes to make a line sound real.

## Mode switch (set this first)
| mode | when | target table column | one-line feel |
|---|---|---|---|
| **blended** (default) | no lean named | blended (weighted) | Calm explainer with spoken glue: Adam's dated, earnest precision plus Gen's So/And/But momentum |
| **adam-lean** | "more Adam", AI-risk, long-form investigation | Adam | Earnest, dated, documentary. It/The/We openers. Few So/But openers (about 15% And+But+So). No swearing. "I think", "sort of", research-frame "As I researched this video" |
| **gen-lean** | "more Gen", tech-economy explainers, piracy/markets | Gen | Fast, argumentative, viewer-first. About half of sentences open And/But/So/Because. "Honestly", "look", "cooked", "what the hell" are allowed, rarely |
| **oil-lean** | "like the oil video", news-shock topics, geopolitics | Oil | Team "we", dry jokes after big facts ("It's a nice bit of trolling."), footage pointers ("Here's another."), And-chains (21% And openers), "Okay," resets |

Dial: say "blend 70/30 adam/gen" and interpolate the two columns linearly.

## Weighted targets (measured on host-only text; full detail in references/criteria.md)
{TAB}

Units: sentence rows are % of sentences or words. Opener rows are per 100 sentences. Other rows are per 1,000 words. And+But+So openers combined: blended {conn['w']:.1f}%, Adam {conn['adam']:.1f}%, Gen {conn['gen']:.1f}%, Oil {conn['oil']:.1f}%, Especially {conn['especially']:.1f}%, After {conn['after']:.1f}%.

## Workflow A: writing narration
1. Set the mode. If none is given, use blended.
2. Get the beats from `channel-storytelling` or the user. Do not decide structure here.
3. Draft each beat out loud in your head. Write the way you would say it to one friend across a table.
4. Facts first: every claim gets a number, a date, a name, or a source in the same sentence ("For 16 hours on Tuesday, July 8th, ...").
5. Rhythm pass: mix 3-6-word punches with 25-35-word run-ons. Target the mode's mean and SD. Never let five sentences in a row sit within 4 words of each other.
6. Glue pass: use spoken openers at the mode's rate (And/But/So/Now/Because/Like/Well/Okay). Replace every essay connector.
7. Texture pass: fillers and hedges at the mode's rate (just, really, actually, basically, kind of, I think, I mean, probably). Hedge, then land on a plain claim.
8. Plain-word pass: contractions everywhere ("it's", "don't", "they're", "gonna" in gen/oil), plain verbs (get, use, buy, show), casual quantities ("a lot", "a bunch of").
9. Tell sweep: run the checklist in references/anti-patterns.md. Zero AI-tell vocabulary, zero essay connectors, about zero semicolons, almost no exclamation marks.
10. Read it aloud. If you would not say a sentence, rewrite it.

## Workflow B: humanizing AI text
1. Lock the facts: list every number, name, date, and claim. They must survive unchanged.
2. Delete AI framing: "In this video we will explore", "It is important to note", "In conclusion", closing morals, "testament", "landscape", "delve".
3. Map essay openers to spoken ones: Therefore/As a result -> So. However -> But. Additionally/Moreover/Furthermore -> And. For example -> Like. Currently -> Now.
4. Re-contract everything.
5. Break semicolon and ", and it is" merges back into separate sentences so short punches return.
6. Swap formal words for plain ones (utilize->use, obtain->get, significant->big or the actual number, numerous->a lot of, individuals->people, approximately->about, purchase->buy).
7. Put back one hedge or filler about every 2-3 sentences at the mode's rate. Then land each hedge on a firm claim.
8. Add one concrete physical picture or exact number per abstract claim (from the facts list; never invented).
9. Re-measure against the target table (mean length, And/But/So %, contractions/1k, fillers/1k).
10. Run the self-check rubric. Fix anything under 4.

## Core rules (exam-tested)
1. Contractions are the strongest single signal. Host text averages {wt('contractions'):.0f} contractions per 1k words. Expanded "it is / do not" reads as AI.
2. Spoken openers: about {conn['w']:.0f}% of blended sentences start with And/But/So. Adam-lean about {conn['adam']:.0f}%, Gen-lean about {conn['gen']:.0f}%. Never Moreover/Furthermore/Additionally.
3. Burstiness: blended sentence-length SD is about {wt('Sentence-length spread (SD)'):.0f} words around a mean of {wt('Mean sentence length (words)'):.0f}. About {wt('Short sentences (<=6 words) %'):.0f}% of sentences are 6 words or fewer, and about {wt('Long sentences (>=30 words) %'):.0f}% are 30 or more.
4. Fillers are part of the voice: "just" about {wt('just'):.1f}/1k, "really" {wt('really'):.1f}/1k, "actually" {wt('actually'):.1f}/1k. Zero fillers reads as essay. Three in one sentence reads as parody.
5. Exact numbers: about {wt('numerals'):.0f} numerals per 1k words, plus dollar amounts, years, and named days. Never "a significant amount".
6. Questions about {wt('Questions %'):.0f}% of sentences, usually answered in the next line. Exclamation marks almost never ({wt('Exclamations %'):.2f}%).
7. Punctuation: commas and periods. Semicolons {wt('semicolons'):.2f}/1k (effectively none). Dashes are caption artefacts, not style.
8. Talk to one viewer: "you" about {wt('you/your'):.0f}/1k, "I" about {wt('I/me/my'):.0f}/1k. The narrator has opinions and says so ("I think", "honestly").
9. AI-tell vocabulary rate in the corpus: {wt('AI-tell vocabulary'):.2f}/1k (practically zero). Essay connectors: {wt('essay connectors'):.2f}/1k.
10. Lean hygiene: no Gen tics (look, cooked, what the hell, swearing) in adam-lean. No Adam earnestness stacked in gen-lean. Oil-lean gets one dry joke after a big fact.

## Self-check rubric (score 0-5 each; ship only at 4+ on every line)
| # | check | 5 looks like |
|---|---|---|
| 1 | Contractions | Every possible contraction taken. No "it is" unless stressed |
| 2 | Openers | And/But/So share within +/-5 points of the mode target. No essay connectors |
| 3 | Rhythm | Mean within +/-2 of target, SD 8+, at least one <=6-word punch per 5 sentences |
| 4 | Fillers/hedges | Mode rate. Hedges followed by a landing |
| 5 | Specificity | Every claim has a number/date/name/source. No vague quantities |
| 6 | Plain words | No formal synonyms. No AI-tell vocabulary |
| 7 | Viewer address | "you" present at stakes beats. Narrator opinion flagged as opinion |
| 8 | Punctuation | No semicolons, no em-dash chains, no exclamation hype |
| 9 | Lean fidelity | Matches the mode column. No cross-lean tics |
| 10 | Read-aloud | Every sentence is something a person would actually say |

## Standing lessons from exams
(Added automatically every 10 exams from real misses. See exams/exam-log.md.)

## References
- `references/criteria.md`: all {len(L)} word-level dimensions with definitions, weighted and per-creator values, verified verbatim quotes, do and don't, and a test for each
- `references/examples.md`: verbatim host passages in weight proportion, labeled by creator, file, and function
- `references/anti-patterns.md`: {len(antipat.LANG)} AI tells and wrong-lean failures, each with a before/after
- `training/`: the curriculum. Run it before first real use (see training/CURRICULUM.md)
- `exams/`: 100-exam set, gold references, rubric, exam-log.md, scores.csv
- `sample.md`: an original ~400-word demonstration
- Related skills (read-only inputs): `workflows/adam-voice`, `workflows/gen-voice`, `workflows/script-voice`, `workflows/humanizer`, `workflows/avoid-ai-writing`, `workflows/anti-ai-slop-writing`

## Source honesty
All quotes in this skill were checked against the source transcripts with whitespace normalized and timestamps stripped. Host-only filtering is heuristic: labeled guests, news clips, and micro-clips are dropped, but some unlabeled clip audio may remain (for example Musk quotes inside Adam's 01 file). Gen 7.txt has no punctuation, so it counts only for word rates.
"""
    wr(f'{R}/SKILL.md',skill)
    # criteria
    out=[f"# channel-language: word-level criteria ({len(L)} dimensions)\n\n## Corpus and weighting\n{CORPUS_TABLE}\n\nColumns: blended = weighted across all files. Per-creator values are plain means over that creator's files.\n"]
    cur=None
    for x in L:
        if x['group']!=cur: cur=x['group'];out.append(f"\n## {cur}\n")
        out.append(f"### L{x['id']}. {x['name']}\n- **Definition:** {x['defn']}\n- **Measure ({x['unit']}):** blended **{f(x['weighted'])}**. Adam {f(x['by_group']['adam'])}, Gen {f(x['by_group']['gen'])}, Especially {f(x['by_group']['especially'])}, Oil {f(x['by_group']['oil'])}, After {f(x['by_group']['after'])}\n- **Verbatim evidence:**\n{qblock(x['quotes'])}\n- **Do:** {x['do']}\n- **Don't:** {x['dont']}\n- **Test:** Measure your draft in the same unit. It should land within +/-25% of the mode column (for near-zero rows, at most 1 per draft).\n")
    out.append("\n## Exam-derived lessons\n(Appended during the 100-exam run.)\n")
    wr(f'{R}/references/criteria.md','\n'.join(out))
    # examples
    rng=random.Random(101);E=[]
    alloc={'adam':50,'gen':52,'especially':13,'oil':7,'after':17}
    o=["# channel-language: verbatim examples\n\nAll passages are copied from host-only text and verified against the source file. Count per creator follows weight: Adam 50, Gen 52, Especially 13, Oil 7, After 17 (total 139). Read them aloud. Notice openers, fillers, contractions, and where the short sentences fall.\n"]
    for g in G:
        o.append(f"\n## {GN[g]}\n")
        cand=[p for p in P if p['group']==g];rng.shuffle(cand)
        for i,p in enumerate(cand[:alloc[g]],1):
            o.append(f"**{g.upper()}-{i}** `{p['file']}` (position {p['pos']*100:.0f}% · {ex_label(p['text'])})\n> {p['text']}\n")
    wr(f'{R}/references/examples.md','\n'.join(o))
    # anti
    o=["# channel-language: anti-patterns\n\nEach item: the AI or wrong-lean pattern, a before line, and an after line. After lines are illustrative rewrites in the channel voice, not corpus quotes. Corpus rates for the tells are in criteria.md (AI-tell vocabulary and essay connectors are practically zero in host speech).\n\n## Quick sweep regex\n```\n\\b(delve|tapestry|testament|landscape|crucial|pivotal|robust|leverage|seamless|multifaceted|intricate|realm|underscore|showcase|foster|vibrant|navigate|moreover|furthermore|additionally|consequently|nevertheless|in conclusion|notably|it is important to note)\\b\n```\nAlso flag: `;` · `—` chains · `!` · \"it is / do not / cannot\" · zero fillers in 60+ words · five sentences of similar length in a row.\n"]
    for i,(n,b,a) in enumerate(antipat.LANG,1): o.append(f"### A{i}. {n}\n- Before: \"{b}\"\n- After: \"{a}\"\n")
    wr(f'{R}/references/anti-patterns.md','\n'.join(o))
    return R
# ================= SKILL 2: STORY
def story_skill():
    R=f'{WF}/channel-storytelling'
    cats=list(dict.fromkeys(c['cat'] for c in T))
    top=sorted(T,key=lambda c:-c['weighted'])[:25]
    TOPT="| # | criterion | weighted /1k words | Adam | Gen | Esp | Oil | After | mean position | in first 10% | in last 10% |\n|---|---|---|---|---|---|---|---|---|---|---|\n"+'\n'.join(f"| S{c['id']} | {c['name']} | {c['weighted']:.2f} | {gtab(c['by_group'])} | {(c['mean_pos'] or 0)*100:.0f}% | {c['pct_first10']:.0f}% | {c['pct_last10']:.0f}% |" for c in top)
    opens='\n'.join(f"- **{GN[d['group']]}** `{d['file']}`: \"{' '.join(d['sents'][:2])}\"" for d in pool.docs)
    skill=f"""---
name: channel-storytelling
description: Plan, write, or critique the storytelling of a YouTube script for the user's channel (blend of Adam 7x, Gen 4x, Oil 5x, Especially 3x, After 1x). Use when the user asks for a cold open, hook, story beats, outline-to-script, tension, open loops, reveals, characters, villains, callbacks, or an ending; or when they ask why a script feels flat or how these creators would tell a story. Use channel-language afterwards for word-level voice.
---

# Channel storytelling

## Purpose
Turn a topic and its facts into a story the way these channels tell it: a cold open dropped into a dated moment or an absurd number, a person before the system, stakes in the viewer's own life, open loops paid on schedule, reveals carried by evidence, a narrator with opinions, a zoom from one person out to the whole system and back, and a short ending. This skill covers {len(T)} criteria, each measured on host-only transcripts and weighted by corpus.

## When to use
- "Write a cold open / hook for ..."
- "Outline / beat out / script a video on ..."
- "Why does this script feel flat?", "add tension", "where's the payoff?"
- Reviewing a draft before recording

Pair with `channel-language` for the sentence pass. Never invent events, quotes, or numbers to make a story beat work. Use [NEED SOURCE] placeholders instead.

## Workflow
1. **Facts and evidence list.** Collect dated events, named people, numbers with sources, documents, and on-the-ground footage. A story beat without a fact gets [NEED SOURCE].
2. **Pick the cold-open type** (see S1-S10): dated moment, absurd number, in-medias-res event, viewer-assumption flip, or "what no one is talking about". The first 2 sentences carry a number, a date, or an event in motion, and no background.
3. **Scope interrupt and central question.** Narrow the claim ("No, like not for you, well, at least for now, but for the companies...") and end the open on the question the video answers.
4. **Cast.** One ordinary person or proxy (S13), one or two powerful figures with motives (S14, S16), institutions acting as characters (S18), and the antagonist force (S60-S63).
5. **Stakes ladder.** Viewer stake (S19) -> money (S20) -> deadline (S22) -> who pays (S24). Each big number gets a physical comparison (S23).
6. **Act plan with a tension curve.** Turn every 3-5 sentences with "But" or "the problem is" (S25, S26). Give each act an escalation ("it gets worse", S30) and a release line (S27).
7. **Plant and pay loops.** Write every open loop (S32-S36) into a ledger with the act where it is paid. Pay with "that's why / remember" (S82, S83).
8. **Reveals.** Each reveal is a fact (turns out, number, document), seeded earlier (S37-S41).
9. **Zoom.** After each anecdote, zoom to the system (S77). At each act end, zoom back to the viewer (S78).
10. **Narrator.** Where the narrator gives an opinion, admits uncertainty, gives a fair counterpoint, and reacts once (S48-S54).
11. **Irony and resets.** One dry irony beat after a big fact per act (S64-S68). A comic reset after heavy beats.
12. **Ending.** Callback to the cold-open image, one implication or open question, a forward date to watch, and a sign-off of no more than 3 sentences (S84-S89).
13. **Run the self-check rubric**, then hand to `channel-language`.

## Core rules
1. Open on a fact in motion. Real first lines from every video are listed below. None starts with background.
2. Never use a back-reference in the open (he/they/also/again/"as I said"). Exams showed that pronoun-led and callback lines are mid-video.
3. A person before a system, a system before the viewer's wallet.
4. Every loop opened is paid. Ledger it.
5. Reveals are facts, not adjectives.
6. The narrator owns opinions ("I think"), owns uncertainty ("nobody knows"), and gives one steelman.
7. Mechanism lives in the middle: "which means", "because", numbers. Projections and sign-offs live at the end.
8. One irony beat per act, deadpan, right after the biggest fact.
9. Endings are short and call back to the open.
10. Weight evidence by corpus: Adam's dated, document-led investigations (7x) and the oil video's footage-pointer comedy (5x) count most, then Gen's argument-driven economics (4x).

## Most frequent criteria (weighted, per 1k host words)
{TOPT}

Full {len(T)}-criterion table with quotes: `references/criteria.md`.

## Real cold opens (first two host sentences of every analyzed video, verbatim)
{opens}

## Self-check rubric (0-5 each; ship at 4+ everywhere)
| # | check | 5 looks like |
|---|---|---|
| 1 | Cold open | Number/date/event in sentence 1. Central question by sentence ~6. No background |
| 2 | Scope and promise | Interrupt or flip narrows the claim. Story promise stated plainly once |
| 3 | Characters | One ordinary person, named figures with motives, a vivid detail each |
| 4 | Stakes | Viewer stake in the first third. Every big number compared to something physical |
| 5 | Tension curve | A turn every 3-5 sentences, an escalation per act, short release lines |
| 6 | Loops | Ledger complete. Every loop paid. 2+ sentence gaps |
| 7 | Reveals | Seeded, factual, sourced |
| 8 | Zoom | Anecdote -> system -> viewer at least once per act |
| 9 | Narrator | Opinion, uncertainty, steelman, one reaction |
| 10 | Irony/emotion | One deadpan beat per act. Emotion tied to evidence |
| 11 | Ending | Callback, one implication/question, a dated next step, sign-off of 3 sentences or fewer |
| 12 | Evidence | Every claim has a name/date/number/document, or [NEED SOURCE] |

## Standing lessons from exams
(Added automatically every 10 exams from real misses. See exams/exam-log.md.)

## References
- `references/criteria.md`: all {len(T)} criteria. Definition, how each creator does it with verified quotes, weighted frequency and placement, do, don't, and a checklist test
- `references/examples.md`: verbatim cold opens, endings, and beats from every corpus in weight proportion
- `references/anti-patterns.md`: {len(antipat.STORY)} story failures with before/after
- `training/`: the curriculum (training/CURRICULUM.md)
- `exams/`: 100 exams, gold, rubric, log, scores.csv
- `sample.md`: an original ~400-word demonstration
- Related: `channel-language` (sentences), `workflows/adam-voice`, `gen-voice`, `script-voice`

## Source honesty
Frequencies come from regex detectors over host-only sentences. They are signals, not hand labels, so a "hit" can occasionally be a false positive (for example "will" in a non-projection). Quotes are verified verbatim against the source transcripts. Placement = sentence index / sentences in the video.
"""
    wr(f'{R}/SKILL.md',skill)
    out=[f"# channel-storytelling: {len(T)} criteria\n\n## Corpus and weighting\n{CORPUS_TABLE}\n\nFor each criterion: weighted rate per 1k host words, per-creator rates (plain mean over that creator's files), weighted mean placement in the video, the weighted share of hits in the first 10% and last 10%, and how many of the {T[0]['n_files']} punctuated videos contain it. Criteria marked [open] or [close] are counted only in the first 8% or last 10% of a video.\n"]
    cur=None
    for c in T:
        if c['cat']!=cur: cur=c['cat'];out.append(f"\n## {cur}\n")
        tag=' [open]' if c['pos']=='open' else ' [close]' if c['pos']=='close' else ''
        out.append(f"### S{c['id']}. {c['name']}{tag}\n- **Definition:** {c['defn']}\n- **Weighted frequency:** {c['weighted']:.2f}/1k. Adam {c['by_group']['adam']:.2f}, Gen {c['by_group']['gen']:.2f}, Especially {c['by_group']['especially']:.2f}, Oil {c['by_group']['oil']:.2f}, After {c['by_group']['after']:.2f}. Present in {c['files_with']}/{c['n_files']} videos\n- **Placement:** mean {(c['mean_pos'] or 0)*100:.0f}% through the video. {c['pct_first10']:.0f}% of hits in the first tenth, {c['pct_last10']:.0f}% in the last tenth\n- **How they do it (verbatim):**\n{qblock(c['quotes'])}\n- **Do:** {c['do']}\n- **Don't:** {c['dont']}\n- **Checklist test:** {c['test']}\n")
    out.append("\n## Exam-derived lessons\n(Appended during the 100-exam run.)\n")
    wr(f'{R}/references/criteria.md','\n'.join(out))
    o=["# channel-storytelling: verbatim examples\n\nVerified verbatim host text. Section 1 has every cold open, section 2 every ending, and section 3 weighted beats labeled by story function.\n\n## 1. Cold opens (first ~4 host sentences)\n"]
    for d in pool.docs: o.append(f"**{GN[d['group']]}** `{d['file']}`\n> {' '.join(d['sents'][:4])}\n")
    o.append("\n## 2. Endings (last ~4 host sentences)\n")
    for d in pool.docs: o.append(f"**{GN[d['group']]}** `{d['file']}`\n> {' '.join(d['sents'][-4:])}\n")
    o.append("\n## 3. Beats by function (weighted: Adam 40, Gen 42, Especially 10, Oil 6, After 14)\n")
    rng=random.Random(202);alloc={'adam':40,'gen':42,'especially':10,'oil':6,'after':14}
    for g in G:
        o.append(f"\n### {GN[g]}\n")
        cand=[p for p in P if p['group']==g and 0.1<p['pos']<0.9];rng.shuffle(cand)
        for i,p in enumerate(cand[:alloc[g]],1): o.append(f"**{g.upper()}-B{i}** `{p['file']}` @{p['pos']*100:.0f}% · {ex_label(p['text'])}\n> {p['text']}\n")
    wr(f'{R}/references/examples.md','\n'.join(o))
    o=["# channel-storytelling: anti-patterns\n\nBefore = the failure (often AI default). After = an illustrative fix in channel style (not a corpus quote unless marked). Some after lines paraphrase real corpus beats (Oil 03 gas-station footage, Adam 01 Tuesday July 8th, Gen 1 Photoshop piracy, After 02 dentist credit card) to show the pattern.\n"]
    for i,(n,b,a) in enumerate(antipat.STORY,1): o.append(f"### X{i}. {n}\n- Before: \"{b}\"\n- After: \"{a}\"\n")
    wr(f'{R}/references/anti-patterns.md','\n'.join(o))
    return R
# ================= TRAINING
def training(R,kind):
    rng=random.Random(303 if kind=='lang' else 404);used=set()
    def take(k): 
        ps=mkpass(rng,k,used);[used.add(p['id']) for p in ps];return ps
    T_=f'{R}/training'
    cur=f"""# Training curriculum ({'channel-language' if kind=='lang' else 'channel-storytelling'})

Learn it, don't just read it. Run this before the first real writing task in a new session, and again after any long break.

## Protocol (follow exactly)
1. Read SKILL.md, then references/criteria.md (skim), then 10 examples per creator from references/examples.md, out loud in your head.
2. For each level L1 to L5: **write all your answers first** in a scratch block without looking at the answer key. Then open `answer-keys.md`, score yourself with `rubric.md`, and write every miss into `lessons-learned.md` as: `date | level | item | what I did | what the real text does | rule I'll follow`.
3. Pass marks: L1 90%, L2 70%, L3 85%, L4 avg 4/5, L5 avg 4/5. If you fail a level, re-read the criteria your misses point to, then redo **only the missed items** plus 5 new items from references/examples.md (mask or transform them yourself the same way).
4. Before writing for real, re-read your last 10 lines of lessons-learned.md.
5. Do not peek. If you saw the answer before answering, mark the item "contaminated" and don't count it.

## Levels
- **L1 Recognition** (`L1-recognition.md`): {'spot every AI tell in transformed sentences' if kind=='lang' else 'name the story criterion each real sentence demonstrates'}
- **L2 Cloze** (`L2-cloze.md`): {'restore the masked opener/filler in real host passages' if kind=='lang' else 'restore the masked story-move sentence (hinge, reveal, loop) in real passages'}
- **L3 Discrimination** (`L3-discrimination.md`): {'which version is the real creator and which is AI' if kind=='lang' else 'which is the real cold open / which line is the real next beat'}
- **L4 Rewrite** (`L4-rewrite.md`): {'humanize AI-ified passages, gold originals in the key' if kind=='lang' else 'reorder shuffled beats and restore AI-flattened passages, gold originals in the key'}
- **L5 Production** (`L5-production.md`): write from briefs, score with the rubric, and compare against the cited real passages

Items are sampled by corpus weight (Adam 7x, Gen 4x, Oil 5x, Especially 3x, After 1x per file). Training passages are disjoint from the exam passages.
"""
    wr(f'{T_}/CURRICULUM.md',cur)
    wr(f'{T_}/lessons-learned.md',"# Lessons learned (append-only)\n\n`date | level | item | what I did | what the real text does | rule I'll follow`\n\n")
    key=["# Answer keys (do not open before answering)\n"]
    # L1
    if kind=='lang':
        ps=take(20);l1=["# L1 Recognition: spot the AI tells\n\nFor each item, list every AI tell (vocabulary, essay connector, expanded contraction, semicolon splice, closing moral, formal synonym). Then say which creator lean the original probably was.\n"];key.append("## L1\n")
        for i,p in enumerate(ps,1):
            ai=pool.aiify(p['text'],rng,'heavy');l1.append(f"**L1.{i}**\n> {ai}\n")
            tl=sorted(set(m.group(0) for m in exams.TELLS.finditer(ai)))
            ex=re.findall(r"\b(?:it is|do not|that is|I am|does not|did not|cannot|there is|they are|you are|we are|is not|was not)\b",ai)
            key.append(f"**L1.{i}** tells: {', '.join(tl) or '-'}; expanded contractions: {', '.join(sorted(set(ex))) or '-'}; semicolons: {ai.count(';')}. Source: {GN[p['group']]} `{p['file']}`. Original:\n> {p['text']}\n")
    else:
        l1=["# L1 Recognition: name the story criterion\n\nFor each real sentence, name the criterion it demonstrates (S-number and name from references/criteria.md). More than one can apply.\n"];key.append("## L1\n")
        rng2=random.Random(5);cs=[c for c in T if c['quotes']]
        for i in range(1,26):
            c=rng2.choice(cs);q=rng2.choice(c['quotes']);l1.append(f"**L1.{i}** \"{q['q']}\"\n")
            key.append(f"**L1.{i}** S{c['id']} {c['name']} ({c['cat']}). Source: {GN[q['group']]} `{q['file']}`\n")
    wr(f'{T_}/L1-recognition.md','\n'.join(l1))
    # L2
    l2=["# L2 Cloze\n"];key.append("## L2\n")
    OPS=['So','And','But','Now','Because','Like','Well','Okay','It','The','This','I','We','You']
    ps=take(25)
    for i,p in enumerate(ps,1):
        if kind=='lang':
            c=[(j,s) for j,s in enumerate(p['sents']) if s.split()[0].rstrip(',') in OPS] or [(0,p['sents'][0])]
            j,s=rng.choice(c);w0=s.split()[0]
            m=' '.join(p['sents'][:j]+['____ '+s.split(' ',1)[1] if ' ' in s else '____']+p['sents'][j+1:])
            l2.append(f"**L2.{i}** [{p['group']}-lean] Fill the blank (one word).\n> {m}\n");key.append(f"**L2.{i}** `{w0}`. Source {GN[p['group']]} `{p['file']}`\n")
        else:
            j=rng.randrange(1,len(p['sents'])) if len(p['sents'])>1 else 0
            m=' '.join(p['sents'][:j]+['[MISSING BEAT]']+p['sents'][j+1:])
            l2.append(f"**L2.{i}** Write the missing beat (one sentence), then name its function.\n> {m}\n");key.append(f"**L2.{i}** Gold: \"{p['sents'][j]}\" (function: {ex_label(p['sents'][j])}). Score: 5 = same function and same information slot, 3 = right function but wrong information, 0 = breaks the flow. Source {GN[p['group']]} `{p['file']}` @{p['pos']*100:.0f}%\n")
    wr(f'{T_}/L2-cloze.md','\n'.join(l2))
    # L3
    l3=["# L3 Discrimination\n"];key.append("## L3\n")
    ps=take(25)
    for i,p in enumerate(ps,1):
        if kind=='lang':
            opts=[p['text'],pool.aiify(p['text'],rng,'subtle' if i%2 else 'heavy')];o=[0,1];rng.shuffle(o)
            l3.append(f"**L3.{i}** Which is the real host line? Explain the deciding signal.\nA) {opts[o[0]]}\n\nB) {opts[o[1]]}\n");key.append(f"**L3.{i}** {'AB'[o.index(0)]} is real ({GN[p['group']]} `{p['file']}`). AI version type: {'subtle (contractions expanded, fillers and spoken openers removed, short sentences merged)' if i%2 else 'heavy (essay connectors, formal synonyms, AI closer)'}\n")
        else:
            d=p['doc'];real=' '.join(d['sents'][:2]);oth=[x for x in P if x['file']!=p['file'] and 0.25<x['pos']<0.75];ds=[' '.join(x['sents'][:2]) for x in rng.sample(oth,2)]
            opts=[real]+ds;o=[0,1,2];rng.shuffle(o)
            l3.append(f"**L3.{i}** Which is a real cold open?\n"+'\n'.join(f"{'ABC'[k]}) {opts[o[k]]}" for k in range(3))+'\n');key.append(f"**L3.{i}** {'ABC'[o.index(0)]} ({GN[p['group']]} `{p['file']}` first lines). The others are mid-video lines.\n")
    wr(f'{T_}/L3-discrimination.md','\n'.join(l3))
    # L4
    l4=["# L4 Rewrite (gold originals in the key)\n\nScore 0-5 with rubric.md. Facts must be unchanged.\n"];key.append("## L4\n")
    ps=take(15)
    for i,p in enumerate(ps,1):
        if kind=='lang':
            l4.append(f"**L4.{i}** [{p['group']}-lean] Humanize:\n> {pool.aiify(p['text'],rng,'heavy')}\n")
        else:
            ss=p['sents'][:];sh=ss[:];rng.shuffle(sh)
            l4.append(f"**L4.{i}** (a) Put these real sentences back in order. (b) Then name the story moves.\n"+'\n'.join(f"  {k+1}. {s}" for k,s in enumerate(sh))+'\n')
        key.append(f"**L4.{i}** Gold ({GN[p['group']]} `{p['file']}`):\n> {p['text']}\n")
    wr(f'{T_}/L4-rewrite.md','\n'.join(l4))
    # L5
    briefs=["Why your electricity bill rose after a data center moved in nearby","How a single shipping chokepoint can double the price of something you buy weekly","A company claims its AI agent replaced 700 support staff, then quietly rehires humans","Why helium shortages hit MRI scans and party balloons at the same time","The fight over who owns the songs AI models were trained on"]
    l5=["# L5 Production\n\nFor each brief, write a ~200-word "+("narration beat in blended mode, then the same beat in adam-lean and gen-lean" if kind=='lang' else "cold open plus first beat (open, scope interrupt, central question, first character)")+". Use [NEED SOURCE] for any fact you don't have. Score with rubric.md, then compare against the cited real passages in references/examples.md and log the differences.\n"]
    for i,b in enumerate(briefs,1): l5.append(f"**L5.{i}** {b}. Compare with: "+(", ".join(f"{GN[d['group']]} `{d['file']}`" for d in random.Random(i).sample(pool.docs,3)))+"\n")
    key.append("## L5\nNo single gold. Use rubric.md and compare line by line with the cited passages.\n")
    wr(f'{T_}/L5-production.md','\n'.join(l5))
    wr(f'{T_}/answer-keys.md','\n'.join(key))
    rub=("# Scoring rubric\n\n- L1: 1 point per tell found, -0.5 per false flag. % = found/total.\n- L2: exact word = 1, same function class (connector vs content) = 0.5.\n- L3: correct with the right signal named = 1, correct without a reason = 0.5.\n- L4/L5 (0-5 each, average): contractions, openers at mode rate, rhythm (SD 8+), fillers/hedges, specificity, plain words, viewer address, punctuation, lean fidelity, read-aloud. 5 = indistinguishable from the gold when read aloud.\n" if kind=='lang' else "# Scoring rubric\n\n- L1: right criterion = 1, right category = 0.5.\n- L2: 5/3/0 as in the key.\n- L3: correct with the signal named (no back-reference, event in motion, number/date) = 1.\n- L4: (a) Kendall-style score = share of sentence pairs in the correct order. (b) 1 point per correctly named move.\n- L5 (0-5 each): the 12 checks of the SKILL.md self-check rubric.\n")
    wr(f'{T_}/rubric.md',rub)
    return used
# ================= EXAMS
def run_exams(R,kind,used):
    rng=random.Random(11 if kind=='lang' else 12)
    PP=[p for p in P if p['id'] not in used]
    fold=exams.Fold(kind,{},[(f'{R}/SKILL.md','## Standing lessons from exams\n(Added automatically every 10 exams from real misses. See exams/exam-log.md.)'),(f'{R}/references/criteria.md','## Exam-derived lessons\n(Appended during the 100-exam run.)')])
    rows=(exams.run_lang if kind=='lang' else exams.run_story)(PP,rng,fold)
    E=f'{R}/exams'
    tnames={'lang':{'A':'real-vs-AI discrimination (3 options)','B':'masked opener cloze (4 options)','C':'humanize AI-ified passage (scored 0-1 vs gold)'},'story':{'A':'real cold open identification (4 options)','B':'placement: open / middle / close','C':'real next beat (3 options)'}}[kind]
    ex=[f"# 100 exams ({kind})\n\nTypes: "+'; '.join(f"{k} = {v}" for k,v in tnames.items())+".\nSampled by weight from passages not used in training. Gold answers follow each prompt. To re-run on a fresh model, hide the gold lines and answer.\n"]
    for r in rows: ex.append(f"## Exam {r['n']} · type {r['type']} · {GN[r['group']]} `{r['file']}`\n{r['prompt']}\n\n<details><summary>gold</summary>\n\n{r['gold']}\n</details>\n")
    wr(f'{E}/exams.md','\n'.join(ex))
    wr(f'{E}/rubric.md',"# Exam rubric\n\n"+('- A, B: 1 if correct, else 0.\n- C: score = 0.35 x tell-free (1/(1+tells)) + 0.35 x token-F1 vs gold + 0.30 x fingerprint (contraction count and sentence-length SD vs gold). Pass at 0.85 or above.\n' if kind=='lang' else '- A, B, C: 1 if correct, else 0. Chance: A 25%, B 33%, C 33%.\n')+"- Every 10 exams: the dominant miss types activate a new rule. The rule's lesson is written into SKILL.md (Standing lessons) and references/criteria.md (Exam-derived lessons).\n")
    with open(f'{E}/scores.csv','w',newline='') as fh:
        w=csv.writer(fh);w.writerow(['exam','type','group','file','weight','gold','answer','score','miss','rules_active'])
        for r in rows: w.writerow([r['n'],r['type'],r['group'],r['file'],r['weight'],(r['gold'] if r['type']!='C' or kind=='story' else 'gold passage'),(r['answer'] if r['type']!='C' or kind=='story' else 'humanized text'),r['score'],r.get('miss',''),r['rules']])
    sc=[r['score'] for r in rows]
    def m(a,b,t=None):
        x=[r['score'] for r in rows[a:b] if t is None or r['type']==t];return st.mean(x) if x else float('nan')
    log=[f"# Exam log ({kind})\n\n## How these exams were run (read this)\nThe exams were run by a deterministic harness that implements this skill's rules as code: feature scorers for discrimination and placement, and a rule-based humanizer for rewrites. It does not use an independent model's free judgement. The harness started with one base rule per exam type. Every 10 exams, the miss types that a still-inactive rule would have fixed switched that rule on, and its lesson was written into SKILL.md and references/criteria.md. So the curve measures how much the folded rules help on new, unseen passages.\n\n**Contamination notes:** (1) The AI versions come from my own transformer (pool.aiify), and the humanizer knows the general shape of those transforms. That makes type C easier than real-world AI text. (2) Opener statistics are rebuilt without the exam's own file, but the same creator's other files stay in. (3) The rules were designed by the same author who wrote the skill. (4) Training passages were excluded from the exam pool.\n\n## Curve\n| window | all | "+' | '.join(f'type {t}' for t in 'ABC')+" |\n|---|---|---|---|---|\n"]
    for a in range(0,100,10): log.append(f"| {a+1}-{a+10} | {m(a,a+10):.3f} | "+' | '.join(f"{m(a,a+10,t):.3f}" for t in 'ABC')+" |")
    early,late=m(0,20),m(80,100);E30,L30=m(0,30),m(70,100)
    log.append(f"\n**Early (1-20) avg {early:.3f} vs late (81-100) avg {late:.3f}.** 1-30 {E30:.3f} vs 71-100 {L30:.3f}. Overall {st.mean(sc):.3f}. By type: "+', '.join(f"{t} {m(0,100,t):.3f}" for t in 'ABC')+".\n\n## Folds\n")
    for k,t in fold.log: log.append(f"- after exam {k}: {t}")
    log.append("\n## Per-exam record\n| # | type | source | gold | answer | score | miss -> rule |\n|---|---|---|---|---|---|---|")
    for r in rows:
        g=r['gold'] if r['type']!='C' or kind=='story' else '(gold passage in exams.md)';a=r['answer'] if r['type']!='C' or kind=='story' else '(humanized)'
        if kind=='story' and r['type']=='B': pass
        log.append(f"| {r['n']} | {r['type']} | {r['group']} `{r['file']}` | {str(g)[:20]} | {str(a)[:20]} | {r['score']} | {r.get('miss','')} |"+(f" **FOLD:** {', '.join(r['fold'])}" if r.get('fold') else ''))
    wr(f'{E}/exam-log.md','\n'.join(log))
    return dict(early=early,late=late,overall=st.mean(sc),bytype={t:m(0,100,t) for t in 'ABC'},folds=fold.log,curve=[m(a,a+10) for a in range(0,100,10)])
if __name__=='__main__':
    res={}
    for kind,fn in(('lang',lang_skill),('story',story_skill)):
        R=fn();used=training(R,kind);res[kind]=run_exams(R,kind,used)
    json.dump(res,open('results.json','w'),indent=1);print(json.dumps(res,indent=1)[:3000])
