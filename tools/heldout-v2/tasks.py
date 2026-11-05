import random, re, stats, beats
from split import part
from examlib import mode
from stats import short
VS=stats.vids()
LABELS=['COLD OPEN / HOOK','PROMISE / ROADMAP','SECTION TURN','SPONSOR READ','CONCLUSION','CTA']
def vids(split): return [v for v in VS if part(v['key']) in split]
def wpick(rng,vs):
    tot=sum(v['weight'] for v in vs); x=rng.uniform(0,tot)
    for v in vs:
        x-=v['weight']
        if x<=0: return v
    return vs[-1]
def ok_s(s,lo=6,hi=35): return lo<=len(s['text'].split())<=hi
def passages(v,minw=55,maxw=120):
    S=v['sents'];P=[];i=0
    while i<len(S):
        j=i;w=0
        while j<len(S) and w<minw: w+=len(S[j]['text'].split()); j+=1
        if minw<=w<=maxw: P.append(dict(i=i,j=j,pct=S[i]['pct'],text=' '.join(s['text'] for s in S[i:j]),first=S[i]['text']))
        i=j
    return P
def win(S,i,k=2): return ' '.join(s['text'] for s in S[i:i+k])
# ---------------- storytelling ----------------
def story_items(split,n,seed):
    rng=random.Random(seed); vs=vids(split); out=[]
    types=(['A']*35+['B']*35+['C']*30)[:n] if n==100 else [rng.choice('ABC') for _ in range(n)]
    rng.shuffle(types)
    for k,T in enumerate(types):
        v=wpick(rng,vs); S=v['sents']
        if T=='A':
            real=win(S,0)
            same=[x for x in vs if x['key']!=v['key'] and x['group']==v['group']] or [x for x in vs if x['key']!=v['key']]
            dist=[]
            while len(dist)<3:
                o=rng.choice(same); OS=o['sents']; i=rng.randrange(int(len(OS)*.15),int(len(OS)*.85))
                t=win(OS,i)
                # realistic: half the distractors must not begin on an obvious connector/pronoun
                if len(dist)%2==0 and re.match(r"\W*(and|but|so|he|she|they|it|this|that|also|because|which)\b",t,re.I): continue
                if 8<=len(t.split())<=70: dist.append(t)
            opts=[real]+dist; rng.shuffle(opts)
            out.append(dict(type='A',video=v['key'],group=v['group'],w=v['weight'],options=opts,gold=opts.index(real)))
        elif T=='B':
            want=['open','middle','close'][k%3]; P=passages(v)
            cand=[p for p in P if (p['pct']<12 if want=='open' else p['pct']>85 if want=='close' else 30<p['pct']<70)]
            if not cand: continue
            p=rng.choice(cand)
            out.append(dict(type='B',video=v['key'],group=v['group'],w=v['weight'],text=p['text'],gold=want,pct=p['pct']))
        else:
            P=[p for p in passages(v) if p['j']<len(S)-1 and 10<p['pct']<90]; p=rng.choice(P)
            nxt=S[p['j']]['text']
            same=[x for x in vs if x['key']!=v['key'] and x['group']==v['group']] or [x for x in vs if x['key']!=v['key']]
            dist=[]
            while len(dist)<2:
                o=rng.choice(same); s=rng.choice(o['sents'][5:-5])
                if ok_s(s,6,40): dist.append(s['text'])
            opts=[nxt]+dist; rng.shuffle(opts)
            out.append(dict(type='C',video=v['key'],group=v['group'],w=v['weight'],passage=p['text'],options=opts,gold=opts.index(nxt)))
    return out
# ---------------- structure ----------------
def events(v):
    ev=[dict(e) for e in stats.BM[v['key']]['events'] if e['beat'] in LABELS or e['beat'].startswith('QUESTION')]
    for e in ev:
        if e['beat'].startswith('QUESTION'): e['beat']='SECTION TURN'
    return ev
def structure_items(split,n,seed):
    rng=random.Random(seed); vs=vids(split); out=[]
    for k in range(n):
        T=['T1','T2','T3','T4','T5','T6'][k%6]; v=wpick(rng,vs); b=stats.BM[v['key']]; S=v['sents']; ev=events(v)
        if T in('T1','T2'):
            pool=[e for e in ev if e['beat']!='COLD OPEN / HOOK' and (T=='T1' or e['beat']!='SECTION TURN')]
            e=rng.choice(pool or ev)
            out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],text=short(e['text'],40),pct=e['pct'],beat=e['beat'],gold=e['beat'] if T=='T1' else e['pct']))
        elif T=='T3':
            pool=[s for s in S if 20<=s['pct']<=90 and ok_s(s)]
            # realistic: at least two distractors do not open on a connector/pronoun
            clean=[s for s in pool if not re.match(r"\W*(and|but|so|he|she|they|it|this|that|also|because|which)\b",s['text'],re.I)]
            others=rng.sample(clean,2)+rng.sample([s for s in pool if s not in clean] or pool,1)
            opts=[S[0]]+others; rng.shuffle(opts)
            out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],options=[short(o['text'],40) for o in opts],gold=opts.index(S[0])))
        elif T=='T4':
            secs=[e for e in b['events'] if e['beat'] in('SECTION TURN','QUESTION TURN (re-hook)')]
            sp=[S[x[0]]['pct'] for x in b['spblocks'] if S[x[0]]['pct']<90]
            out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],facts=dict(title=v['title'],mode=mode(v),runtime=v['dur'],has_sponsor=bool(sp)),
               gold=dict(hook=S[b['hook_end']]['pct'],spon=sp[0] if sp else None,conc=S[b['conc']]['pct'] if b['conc'] is not None else None,turns=len(secs))))
        elif T=='T5':
            prof=dict(dur=round(v['dur']/60,1),wpm=round(v['words']/(v['dur']/60)),hook=S[b['hook_end']]['t'],you=round(1000*sum(len(re.findall(r"\byou(r|'re|'ll|'ve)?\b",s['text'],re.I)) for s in S)/v['words'],1))
            out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],profile=prof,gold=mode(v)))
        else:
            cand=[e for e in ev if e['beat']!='COLD OPEN / HOOK']
            pick=sorted(rng.sample(cand,min(4,len(cand))),key=lambda e:e['pct']); sh=pick[:]; rng.shuffle(sh)
            out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],shuffled=[short(e['text'],30) for e in sh],gold=[sh.index(e) for e in pick],gold_pcts=[e['pct'] for e in sh]))
    return out
def flatten(t):
    u=re.sub(r"\byou're\b","people are",t,flags=re.I); u=re.sub(r"\byour\b","their",u,flags=re.I); u=re.sub(r"\byou\b","people",u,flags=re.I)
    u=re.sub(r"^(So|And|But|Now),?\s+","",u); u=u.replace('?','.'); u=re.sub(r"\b(literally|actually|really|just)\s+","",u)
    return u[0].upper()+u[1:] if u else u
# ---------------- audience ----------------
def audience_items(split,n,seed,RX):
    rng=random.Random(seed); vs=vids(split); out=[]
    for k in range(n):
        T=['A1','A2','A3','A4','A5'][k%5]
        for _ in range(80):
            v=wpick(rng,vs); S=v['sents']
            if T=='A1':
                c=rng.choice(RX); hits=[x for x in S if c['re'].search(x['text']) and 5<=len(x['text'].split())<=40]
                if not hits: continue
                x=rng.choice(hits); ds=[d for d in RX if not d['re'].search(x['text']) and d['cat']!=c['cat']]
                opts=[c['name']]+[d['name'] for d in rng.sample(ds,3)]; rng.shuffle(opts)
                out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],text=short(x['text'],45),options=opts,gold=opts.index(c['name']))); break
            if T=='A2':
                h=[x for x in S if x['pct']<=8 and ok_s(x)]; m=[x for x in S if 30<=x['pct']<=70 and ok_s(x)]
                if not h or len(m)<3: continue
                g=rng.choice(h); opts=[g]+rng.sample(m,3); rng.shuffle(opts)
                out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],options=[short(o['text'],40) for o in opts],gold=opts.index(g))); break
            if T=='A3':
                i=rng.randrange(int(len(S)*0.15),int(len(S)*0.8)); seg=[]; j=i
                while j<len(S) and sum(len(x['text'].split()) for x in seg)<130: seg.append(S[j]); j+=1
                out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],text=' '.join(x['text'] for x in seg),gold=mode(v))); break
            if T=='A4':
                close=[i for i,x in enumerate(S) if 88<=x['pct']<=98]; mid=[i for i,x in enumerate(S) if 40<=x['pct']<=60]
                if len(close)<4 or len(mid)<4: continue
                a=rng.choice(close[:-3]); b=rng.choice(mid[:-3]); P=[' '.join(S[q]['text'] for q in range(a,a+3)),' '.join(S[q]['text'] for q in range(b,b+3))]
                o=[0,1]; rng.shuffle(o)
                out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],options=[short(P[q],70) for q in o],gold=o.index(0))); break
            if T=='A5':
                c=[x for x in S if 8<=len(x['text'].split())<=35 and flatten(x['text'])!=x['text']]
                if not c: continue
                x=rng.choice(c); opts=[x['text'],flatten(x['text'])]; o=[0,1]; rng.shuffle(o)
                out.append(dict(type=T,video=v['key'],group=v['group'],w=v['weight'],options=[opts[q] for q in o],gold=o.index(0))); break
    return out
