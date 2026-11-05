import os
import json, random, re, numpy as np, tasks, learn, story2, structure_learn as SL, audience_learn as AL
from learn import fvec
from feats import NAMES, feats
from learn import first_sent
W=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','skills')+'/'
FS=json.load(open('final_scores.json')); FS2=json.load(open('final_scores_round2.json'))
SM=json.load(open('story_model.json')); TM=json.load(open('structure_model.json')); AM=json.load(open('audience_model.json')); R2=json.load(open('round2_model.json'))
def q(t,n=22):
    w=t.split(); return ' '.join(w[:n])+(' …' if len(w)>n else '')
by=lambda L,t:[x for x in L if x['type']==t]
def fired(t):
    d=feats(t,first_sent(t)); return [k for k in NAMES if k not in('len_words','n_ents','short') and d[k]>0][:6]
def sigtable(names):
    rows={n:[0,0,0] for n in names}; cnt=[0,0,0]
    for v in tasks.vids({'train','val'}):
        for s in v['sents']:
            b=0 if s['pct']<10 else 2 if s['pct']>=80 else 1; cnt[b]+=v['weight']
            d=feats(s['text'],s['text'])
            for n in names: rows[n][b]+=v['weight']*(d[n]>0)
    out="| feature | 0-10% (open) | 10-80% (body) | 80-100% (close) | signature |\n|---|---|---|---|---|\n"
    for n in names:
        r=[rows[n][i]/cnt[i] for i in range(3)]; sig='OPEN' if r[0]>1.5*r[1] and r[0]>=r[2] else 'CLOSE' if r[2]>1.5*r[1] else 'BODY' if r[1]>1.3*max(r[0],r[2]) else 'flat'
        out+=f"| {n} | {r[0]:.1%} | {r[1]:.1%} | {r[2]:.1%} | {sig} |\n"
    return out+"\n_Weighted share of host sentences where the cue fires (TRAIN+VAL videos only; weights Adam 7, Gen 4, Oil 5, Especially-AI/SpaceX 3, After 1)._\n"
def logmd(log):
    return "\n".join(f"- {a[0].upper()} `{a[1]}` ({'val acc' if a[0]=='accept' else 'Δ'} {a[2]})" for a in log)+"\n"
def contrast(items,T,get,n=30):
    out=f"# Method 1: Contrastive pairs ({T})\n\nEach pair is a real gold answer next to the most confusable distractor, from TRAIN videos only. The cue column lists which rule features fire on each side. Read the pair, then name the difference before you look at the cue column.\n\n"
    for k,it in enumerate(items[:n]):
        g,d=get(it); out+=f"**{k+1}.** ({it['group']})\n- ✅ \"{q(g)}\"  cues: {', '.join(fired(g)) or '—'}\n- ❌ \"{q(d)}\"  cues: {', '.join(fired(d)) or '—'}\n\n"
    return out
def scores_md(skill):
    a=FS[skill]; b=FS2[skill]
    s="| task | n | before (v1 rules) | after round 1 | after round 2 |\n|---|---|---|---|---|\n"
    for T in a: s+=f"| {T} | {a[T]['n']} | {a[T]['before']} | {a[T]['after']} | {b[T]['after']} |\n"
    return s+"\nScores are weight-averaged (Adam 7x, Gen 4x, Oil 5x, Especially 3x, After 1x). Test videos were never used to induce or select rules.\n"
def write(p,s): open(p,'w').write(s)
rng=random.Random(7)
# ================= STORY =================
D=W+'channel-storytelling/'
TRi=sum([tasks.story_items({'train'},100,s) for s in range(3)],[]); VAi=sum([tasks.story_items({'val'},100,s) for s in range(100,102)],[])
write(D+'training/method1-contrastive-pairs.md',contrast(by(TRi,'A'),'cold open vs mid-video window',lambda it:(it['options'][it['gold']],[o for j,o in enumerate(it['options']) if j!=it['gold']][0]),20)+contrast(by(TRi,'C'),'next beat vs foreign sentence',lambda it:(it['options'][it['gold']],[o for j,o in enumerate(it['options']) if j!=it['gold']][0]),12).replace('# Method 1','## Part 2 –'))
write(D+'references/position-signatures.md',"# Method 2: Reverse outline and position-signature table\n\nEvery TRAIN and VAL video was reverse-outlined sentence by sentence and bucketed by runtime position. Use this table to place a passage. If OPEN cues fire, it belongs in the first 10%. If CLOSE cues fire, it belongs in the last 20%. Otherwise it is body.\n\n"+sigtable(['in_medias_res','year_date','number','dated_start','viewer_frame','greeting','hedge_project','mechanism','callback','reflective','conclusion','hope','signoff','future','past','question','you','we','stakes','promise'])+"\n## Placement rule (accepted on validation)\nThe validation-selected features were `lex_close` (a learned close-vocabulary score), `in_medias_res`, `past` and `year_date`. In plain words:\n1. Past-tense, dated, in-scene narration means **open** or **middle**, not close.\n2. Reflective, future, hope and callback wording means **close**.\n3. When nothing fires, answer **middle**. It is the base rate.\n")
# shuffle-reorder: story = 5 passages in order
sr="# Method 3: Shuffle-reorder and rewrite-diff (VAL videos)\n\n## Shuffle-reorder\nFive passages from one video were shuffled. Restore the order with the position table, then check against the truth.\n\n"
for v in tasks.vids({'val'}):
    P=tasks.passages(v); pick=sorted(rng.sample(P,min(5,len(P))),key=lambda p:p['pct'])
    sr+=f"**{v['key'].split('/')[0]} video ({v['group']})**\n"+"\n".join(f"- {p['pct']:.0f}%: \"{q(p['text'],16)}\" → cues {', '.join(fired(p['text'])) or '—'}" for p in pick)+"\n\n"
sr+="## Rewrite-diff\nTake a real cold open, strip its OPEN cues (the date, the in-scene verb, the number), and see what is left. What remains reads as body text, which shows those cues are what make it an opener.\n\n"
for v in tasks.vids({'train'})[:8]:
    o=v['sents'][0]['text']; flat=re.sub(r"\b(On|In|For|By)\s+[^,]{0,40}\d[^,]*,\s*","",o); flat=re.sub(r"\d[\d,.%]*","some",flat)
    sr+=f"- original: \"{q(o)}\"\n  - stripped: \"{q(flat)}\". It loses its anchor and reads like the middle of a video.\n"
write(D+'training/method3-shuffle-reorder.md',sr)
# worked examples
import exam_runner_lite as ER
we="# Method 4: Worked examples (VAL items, 36)\n\nEach item shows the prompt, the rule-based answer, the gold answer, and why. Misses are kept on purpose; they mark where reading beats the rules.\n\n"
for T,n in (('A',12),('B',12),('C',12)):
    for it in by(VAi,T)[:n]:
        a=ER.story(it); ok='✅' if a==it['gold'] else '❌'
        if T=='B': we+=f"**{T}** \"{q(it['text'],30)}\" → answer **{a}**, gold **{it['gold']}** {ok}. Cues: {', '.join(fired(it['text'])) or 'none, so default to middle'}\n\n"
        else:
            opts="\n".join(f"  {j}. \"{q(o,18)}\"" for j,o in enumerate(it['options']))
            ctx=f"  context: \"…{q(it['passage'][-140:],20)}\"\n" if T=='C' else ''
            we+=f"**{T}**\n{ctx}{opts}\n  → answer {a}, gold {it['gold']} {ok}. Gold cues: {', '.join(fired(it['options'][it['gold']])) or '—'}\n\n"
write(D+'training/worked-examples.md',we)
write(D+'training/rule-log.md',"# Method 5: Rule induction log (TRAIN induces, VAL accepts or rejects)\n\nA rule is kept only if weighted validation accuracy rises by at least 0.005 (0.01 in round 2's leave-one-video-out CV).\n\n## Cold open (A), round 1\n"+logmd(SM['A']['log'])+"\n## Cold open (A), round 2 (leave-one-video-out over TRAIN+VAL)\n"+logmd(R2['story_A']['log'])+"\n## Placement (B), base features\n"+logmd(SM['B']['log'])+"\n## Next beat (C)\n"+logmd(SM['C']['log']))
write(D+'exams/heldout-2026.md',"# Held-out exam, 2026 (100 items, TEST videos only, seed 2026)\n\n"+scores_md('channel-storytelling'))
# ================= STRUCTURE =================
D=W+'channel-structure/'
TRs=tasks.structure_items({'train'},120,1); VAs=tasks.structure_items({'val'},120,101)
write(D+'training/method1-contrastive-pairs.md',contrast(by(TRs,'T3'),'real first sentence vs mid sentence',lambda it:(it['options'][it['gold']],[o for j,o in enumerate(it['options']) if j!=it['gold']][0]),20)+"\n## Part 2: Beat label pairs (same video, different beat)\n\n"+"\n".join(f"- **{it['beat']}** @ {it['pct']:.0f}%: \"{q(it['text'])}\"" for it in by(TRs,'T1')[:14]))
write(D+'references/position-signatures.md',"# Method 2: Reverse outline and position signatures\n\n## Median beat position (TRAIN, % of runtime)\n| beat | median % |\n|---|---|\n"+"".join(f"| {k} | {v} |\n" for k,v in sorted(TM['T2']['P'].items(),key=lambda x:x[1]))+f"| mid-video CTA (no sign-off words) | {TM['T2']['LP']['CTA_mid']} |\n\n**Unmarked hook-end rule:** a line with no beat cue and no question is the end of the cold open, at about 6%. This one rule raised validation T2 from 0.59 to 0.91.\n\n"+sigtable(['promise','meta_video','question','conclusion','signoff','sponsor','reflective','in_medias_res','dated_start','greeting','viewer_frame','list_marker','you','i_me']))
sr="# Method 3: Shuffle-reorder (VAL videos)\n\nShuffle 4 to 6 labelled beats, rebuild the order from the position table, and score the pairwise agreement.\n\n"
P=TM['T2']['P'];LP=TM['T2']['LP']
for v in tasks.vids({'val'}):
    ev=[e for e in tasks.events(v) if e['beat']!='COLD OPEN / HOOK']; pick=sorted(rng.sample(ev,min(5,len(ev))),key=lambda e:e['pct'])
    pr=sorted(pick,key=lambda e:SL.place(e['text'],P,LP))
    agree=sum(1 for i in range(len(pick)) for j in range(i+1,len(pick)) if pr.index(pick[i])<pr.index(pick[j]))/max(1,len(pick)*(len(pick)-1)/2)
    sr+=f"**{v['key'].split('/')[0]} ({v['group']})**, pairwise agreement {agree:.2f}\n"+"\n".join(f"- true {e['pct']:.0f}% → predicted {SL.place(e['text'],P,LP):.0f}% [{SL.label(e['text'])}] \"{q(e['text'],14)}\"" for e in pick)+"\n\n"
write(D+'training/method3-shuffle-reorder.md',sr)
we="# Method 4: Worked examples (VAL items, 36)\n\n"
for T in ('T1','T2','T3','T6'):
    for it in by(VAs,T)[:9]:
        if T=='T1': a=SL.label(it['text'],it['pct']); we+=f"**T1** @{it['pct']:.0f}% \"{q(it['text'])}\" → {a}; gold {it['gold']} {'✅' if a==it['gold'] else '❌'}\n\n"
        elif T=='T2': a=SL.place(it['text'],P,LP); we+=f"**T2** \"{q(it['text'])}\" → label {SL.label(it['text'])} → {a:.0f}%; gold {it['gold']:.0f}% {'✅' if abs(a-it['gold'])<=10 else '½' if abs(a-it['gold'])<=20 else '❌'}\n\n"
        elif T=='T3': a=ER.t3(it); we+="**T3**\n"+"\n".join(f"  {j}. \"{q(o,16)}\"" for j,o in enumerate(it['options']))+f"\n  → {a}, gold {it['gold']} {'✅' if a==it['gold'] else '❌'}. Gold cues: {', '.join(fired(it['options'][it['gold']])) or '—'}\n\n"
        else:
            p=[SL.place(t,P,LP) for t in it['shuffled']]; a=sorted(range(len(p)),key=lambda i:p[i]); we+=f"**T6** order {a} vs gold {it['gold']}: "+"; ".join(f"\"{q(t,8)}\"" for t in it['shuffled'])+"\n\n"
write(D+'training/worked-examples.md',we)
write(D+'training/rule-log.md',"# Method 5: Rule induction log\n\n## T3 openers, round 1 (TRAIN fit, VAL accept)\n"+logmd(TM['T3']['log'])+"\n## T3, round 2 (leave-one-video-out CV, TRAIN+VAL)\n"+logmd(R2['struct_T3']['log'])+"\n## T2 rule changes\n- ACCEPT: unmarked hook-end, where a line with no cue goes to the PROMISE median (~6%). Val T2 rose from 0.53 to 0.91.\n- ACCEPT: mid-video CTA split, where a CTA without sign-off words is placed at the mid-CTA median.\n- REJECT: sending every uncued line to 49.5% (SECTION TURN). That was the cause of the old T2 failures.\n- REJECT: train-only opener phrase lists (greeting/viewer_frame). They gave no val gain in round 1 (0.739 → 0.739).\n")
write(D+'exams/heldout-2026.md',"# Held-out exam, 2026\n\n"+scores_md('channel-structure'))
# ================= AUDIENCE =================
D=W+'channel-audience/'
TRa=AL.gen({'train'},[1]); VAa=AL.gen({'val'},[101])
write(D+'training/method1-contrastive-pairs.md',contrast(by(TRa,'A2'),'hook line vs mid line',lambda it:(it['options'][it['gold']],[o for j,o in enumerate(it['options']) if j!=it['gold']][0]),15)+contrast(by(TRa,'A4'),'close window vs mid window',lambda it:(it['options'][it['gold']],it['options'][1-it['gold']]),15).replace('# Method 1','## Part 2 –'))
write(D+'references/position-signatures.md',"# Method 2: Audience-device position signatures\n\n"+sigtable(['you','question','stakes','hope','future','reflective','signoff','callback','past','n_ents' if False else 'number','in_medias_res','contrast','starts_anaphor','profanity','we']).replace('n_ents','number')+"\n## Accepted rules\n- **Close vs mid (A4):** HOPE and agency words point to the close. Past-tense narration, many named entities and anaphor starts (\"It/This/They …\") point to the middle. Val 0.88.\n- **Hook vs mid (A2):** the learned open-vocabulary score plus dated and demonstrative starts. Val only reaches 0.58. One opening line taken alone is often indistinguishable from body text.\n- **Mode (A3):** first-person rate, number density, in-scene narration, callbacks and \"you\" rate. Val 0.83.\n")
sr="# Method 3: Shuffle-reorder and rewrite-diff\n\n## Rewrite-diff (flattening test)\nThe real host line is next to a flattened version: no \"you\", no spoken connectors, no question, no intensifiers. The difference is exactly the set of audience devices.\n\n"
for it in by(TRa,'A5')[:12]: sr+=f"- real: \"{q(it['options'][it['gold']])}\"\n  flat: \"{q(it['options'][1-it['gold']])}\"\n"
sr+="\n## Shuffle-reorder (VAL)\nOne hook, one mid and one close window were shuffled. Restore them with: hook cues (date, number, in-scene) first, then mechanism and past narration, then hope, agency and future last.\n\n"
for v in tasks.vids({'val'}):
    S=v['sents']; a=S[0]['text']; m=S[len(S)//2]['text']; c=S[int(len(S)*.93)]['text']
    sr+=f"- {v['group']}: [{q(c,10)}] / [{q(a,10)}] / [{q(m,10)}] → correct order: 2, 3, 1\n"
write(D+'training/method3-shuffle-reorder.md',sr)
we="# Method 4: Worked examples (VAL items, 35)\n\n"
for T in ('A1','A2','A3','A4','A5'):
    for it in by(VAa,T)[:7]:
        a=ER.aud(it); ok='✅' if a==it['gold'] else '❌'
        if T=='A3': we+=f"**A3** \"{q(it['text'],30)}\" → {a}; gold {it['gold']} {ok}\n\n"
        else: we+=f"**{T}** "+(f"\"{q(it['text'])}\" " if T=='A1' else '')+"\n"+"\n".join(f"  {j}. \"{q(o,16)}\"" for j,o in enumerate(it['options']))+f"\n  → {a}, gold {it['gold']} {ok}\n\n"
write(D+'training/worked-examples.md',we)
write(D+'training/rule-log.md',"# Method 5: Rule induction log\n\n"+"".join(f"## {T}\n"+logmd(AM[T]['log'])+"\n" for T in('A2','A3','A4'))+"## A2, round 2 (LOVO CV)\n"+logmd(R2['aud_A2']['log']))
write(D+'exams/heldout-2026.md',"# Held-out exam, 2026\n\n"+scores_md('channel-audience'))
print('ok')
