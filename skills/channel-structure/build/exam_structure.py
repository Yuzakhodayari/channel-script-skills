import random, re, json, copy, statistics as st
import stats
from corpus import fmt
from stats import short, verify
from examlib import wpick, mode
LABELS=['COLD OPEN / HOOK','PROMISE / ROADMAP','SECTION TURN','SPONSOR READ','CONCLUSION','CTA']
class Solver:
    """Executes the SKILL.md checklist as written (v1), then folds lessons after each block of 10."""
    def __init__(s):
        s.cues={'PROMISE / ROADMAP':[r"\bI want to\b",r"\blet'?s\b",r"\bin this video\b"],
                'SPONSOR READ':[r"\bsponsor",r"\bdescription\b"],
                'CTA':[r"\bsubscribe\b",r"thank you for watching",r"\bnewsletter\b"],
                'CONCLUSION':[r"\bultimately\b",r"\bin the end\b",r"at the end of the day"],
                'SECTION TURN':[r"^so,? ",r"^now,? ",r"^but then\b"],
                'COLD OPEN / HOOK':[]}
        s.pos={'COLD OPEN / HOOK':0,'PROMISE / ROADMAP':5,'SECTION TURN':45,'SPONSOR READ':35,'CONCLUSION':85,'CTA':98}
        s.tmpl={'Adam':dict(hook=2.5,spon=None,conc=80,turns=7),'Gen':dict(hook=6,spon=39,conc=85,turns=6),'Mechanism':dict(hook=6,spon=27,conc=90,turns=7),'Others':dict(hook=6,spon=25,conc=86,turns=5)}
        s.cent={'Adam':dict(dur=39,wpm=164,hook=64,you=12),'Gen':dict(dur=22,wpm=190,hook=85,you=21),'Mechanism':dict(dur=30,wpm=190,hook=95,you=17),'Others':dict(dur=17,wpm=166,hook=88,you=12)}
        s.open_w=dict(num=1.0,date=1.0,you=0.5,short=0.5,anaphora=-1.5,so_open=-0.5,question=0.3,name=0.5,meta=-1.0)
        s.seen={k:[] for k in s.pos}; s.lessons=[]
    def label(s,text,pct):
        sc={}
        if pct is None:
            sc={L:sum(1 for c in cs if re.search(c,text,re.I)) for L,cs in s.cues.items()}
            b=max(sc,key=sc.get)
            return b if sc[b]>0 else 'SECTION TURN'
        for L,cs in s.cues.items():
            sc[L]=sum(2 for c in cs if re.search(c,text,re.I))
            sc[L]-=abs(pct-s.pos[L])/25
        return max(sc,key=sc.get)
    def open_score(s,t):
        f=dict(num=bool(re.search(r'\d|million|billion|percent',t,re.I)),date=bool(re.search(r'\b(19|20)\d\d|monday|tuesday|wednesday|thursday|friday|january|february|march|april|may|june|july|august|september|october|november|december|year|hours',t,re.I)),
               you=bool(re.search(r'\byou',t,re.I)),short=len(t.split())<=14,anaphora=bool(re.match(r"(this|that|these|those|he|she|they|it|which|and|but|so|also)\b",t,re.I)),so_open=bool(re.match(r'so,? back|back to',t,re.I)),question=t.endswith('?'),name=bool(re.search(r'\s[A-Z][a-z]+',t)),meta=bool(re.search(r'\b(remember|at this point|also|again|by the way|this whole)\b',t,re.I)))
        return sum(s.open_w[k]*float(v) for k,v in f.items()),f
    def outline(s,m,dur,has_sp):
        t=s.tmpl[m]; return dict(hook=t['hook'],spon=(t['spon'] or 38) if has_sp else None,conc=t['conc'],turns=t['turns'])
    def attribute(s,prof):
        def d(c): return abs(prof['dur']-c['dur'])/8+abs(prof['wpm']-c['wpm'])/15+abs(prof['hook']-c['hook'])/60+abs(prof['you']-c['you'])/6
        return min(s.cent,key=lambda k:d(s.cent[k]))
def gen_items(n=100,seed=7):
    rng=random.Random(seed); vs=stats.vids(); items=[]
    types=['T1','T2','T3','T4','T5','T6']
    for k in range(n):
        T=types[k%6]; v=wpick(rng,vs); b=stats.BM[v['key']]; S=v['sents']
        ev=[e for e in b['events'] if e['beat'] in LABELS or e['beat'].startswith('QUESTION')]
        for e in ev:
            if e['beat'].startswith('QUESTION'): e['beat']='SECTION TURN'
        if T in('T1','T2'):
            pool=[e for e in ev if e['beat']!='COLD OPEN / HOOK' and (T=='T1' or e['beat']!='SECTION TURN')]
            e=rng.choice(pool or ev)
            items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],prompt_text=short(e['text'],40),pct=e['pct'],beat=e['beat'],gold=e['beat'] if T=='T1' else e['pct'],t=e['t']))
        elif T=='T3':
            others=rng.sample([s for s in S if 20<=s['pct']<=90 and 6<=len(s['text'].split())<=35],3)
            opts=[S[0]]+others; rng.shuffle(opts)
            items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],options=[short(o['text'],40) for o in opts],gold=opts.index(S[0])))
        elif T=='T4':
            secs=[e for e in b['events'] if e['beat'] in('SECTION TURN','QUESTION TURN (re-hook)')]
            sp=[S[x[0]]['pct'] for x in b['spblocks'] if S[x[0]]['pct']<90]
            items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],facts=dict(title=v['title'],mode=mode(v),runtime=fmt(v['dur']),has_sponsor=bool(sp)),
               gold=dict(hook=S[b['hook_end']]['pct'],spon=sp[0] if sp else None,conc=S[b['conc']]['pct'] if b['conc'] is not None else None,turns=len(secs))))
        elif T=='T5':
            prof=dict(dur=round(v['dur']/60,1),wpm=round(v['words']/(v['dur']/60)),hook=S[b['hook_end']]['t'],you=round(1000*sum(len(re.findall(r"\byou(r|'re|'ll|'ve)?\b",s['text'],re.I)) for s in S)/v['words'],1))
            items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],profile=prof,gold=mode(v)))
        else:
            cand=[e for e in ev if e['beat']!='COLD OPEN / HOOK']
            pick=sorted(rng.sample(cand,min(4,len(cand))),key=lambda e:e['pct'])
            sh=pick[:]; rng.shuffle(sh)
            items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],shuffled=[short(e['text'],30) for e in sh],gold=[sh.index(e) for e in pick],gold_pcts=[e['pct'] for e in sh]))
    return items
def answer(sol,it):
    T=it['type']
    if T=='T1': return sol.label(it['prompt_text'],it['pct'])
    if T=='T2': L=sol.label(it['prompt_text'],None); return sol.pos[L] if L!='SECTION TURN' else 45
    if T=='T3': sc=[sol.open_score(o)[0] for o in it['options']]; return sc.index(max(sc))
    if T=='T4': f=it['facts']; return sol.outline(f['mode'],f['runtime'],f['has_sponsor'])
    if T=='T5': return sol.attribute(it['profile'])
    if T=='T6':
        p=[]
        for t in it['shuffled']:
            L=sol.label(t,None); p.append(sol.pos[L])
        return sorted(range(len(p)),key=lambda i:p[i])
def score(it,a):
    T=it['type'];g=it['gold']
    if T=='T1': return 1.0 if a==g else 0.0
    if T=='T2': d=abs(a-g); return 1.0 if d<=10 else 0.5 if d<=20 else 0.0
    if T in('T3','T5'): return 1.0 if a==g else 0.0
    if T=='T4':
        pts=0; pts+= 1 if abs(a['hook']-g['hook'])<=3 else 0
        pts+= 1 if (a['spon'] is None and g['spon'] is None) or (a['spon'] is not None and g['spon'] is not None and abs(a['spon']-g['spon'])<=10) else 0
        pts+= 1 if g['conc'] is None or abs(a['conc']-g['conc'])<=8 else 0
        pts+= 1 if abs(a['turns']-g['turns'])<=2 else 0
        return pts/4
    if T=='T6':
        n=len(g); pr=[(i,j) for i in range(n) for j in range(i+1,n)]
        pos={x:k for k,x in enumerate(a)}; gp={x:k for k,x in enumerate(g)}
        ok=sum(1 for i,j in pr if (pos[i]<pos[j])==(gp[i]<gp[j])); return round(ok/max(len(pr),1),2)
def fold(sol,block,results):
    les=[]
    for it,a,scv in results:
        T=it['type']
        if T in('T1','T2','T6'):
            pass
        if (T=='T1' or T=='T2') and scv<1:
            g=it['beat']; m=re.match(r"\W*(\w+(?:'\w+)?(?:,)?\s+\w+)",it['prompt_text'])
            key=re.escape(m.group(1).split()[0].rstrip(',')) if m else None
            sol.seen[g].append(it['pct'])
            if g=='SECTION TURN' and key and len(key)<=8:
                c=r'^'+key.lower()+r'\b'
                if c not in sol.cues[g]: sol.cues[g].append(c); les.append(f'Exam {it["id"]}: section turns also open with "{key}" — added opener cue.')
            elif g=='CTA':
                for c in [r'\bsee you\b',r'\bthank',r'\bpatreon\b',r'\bcomment']:
                    if c not in sol.cues[g]: sol.cues[g].append(c)
                les.append(f'Exam {it["id"]}: CTA lines include "thanks/see you/comment" sign-offs, not just "subscribe".')
            elif g=='CONCLUSION':
                for c in [r"here'?s the thing",r'\bI think\b',r'so where does']:
                    if c not in sol.cues[g]: sol.cues[g].append(c)
                les.append(f'Exam {it["id"]}: conclusions open with "But here\'s the thing" / "I think…" / "So where does this leave" — added.')
            elif g=='PROMISE / ROADMAP':
                for c in [r'\bto understand\b',r"no one is talking",r'\bhere\'?s (what|how|why)\b',r'\bthe question\b',r'\bstory\b']:
                    if c not in sol.cues[g]: sol.cues[g].append(c)
                les.append(f'Exam {it["id"]}: promise lines often are "to understand…", "what no one is talking about", "the full story" — added.')
            elif g=='SPONSOR READ':
                for c in [r"that'?s (exactly )?where",r'\bgo to\b',r'\.com|\.me']:
                    if c not in sol.cues[g]: sol.cues[g].append(c)
                les.append(f'Exam {it["id"]}: sponsor blocks start on the bridge ("that\'s where … comes in") — added bridge cues.')
        if T=='T2':
            L=it['beat']
            if L!='SECTION TURN':
                sol.pos[L]=round(0.7*sol.pos[L]+0.3*it['gold'],1)
            if scv<1: les.append(f'Exam {it["id"]}: position miss ({a}% vs gold {it["gold"]}%) — shifted the {L} prior toward gold.')
        if T=='T3' and scv<1:
            _,fg=sol.open_score(it['options'][it['gold']]); _,fa=sol.open_score(it['options'][a])
            for k in sol.open_w:
                sol.open_w[k]+=0.5*(float(fg[k])-float(fa[k]))
            les.append(f'Exam {it["id"]}: picked a mid-video line as the opener; reweighted opener features (now {json.dumps({k:round(x,1) for k,x in sol.open_w.items()})}).')
        if T=='T4':
            m=it['facts']['mode']; g=it['gold']; t=sol.tmpl[m]
            t['hook']=round(0.6*t['hook']+0.4*g['hook'],1)
            if g['spon'] is not None: t['spon']=round(0.6*(t['spon'] or g['spon'])+0.4*g['spon'],1)
            if g['conc'] is not None: t['conc']=round(0.6*t['conc']+0.4*g['conc'],1)
            t['turns']=round(0.6*t['turns']+0.4*g['turns'])
            if scv<1: les.append(f'Exam {it["id"]}: outline for {m} off (score {scv}); template moved toward gold → {t}.')
        if T=='T5':
            g=it['gold']; c=sol.cent[g]; p=it['profile']
            for k in c: c[k]=round(0.75*c[k]+0.25*p[k],1)
            if scv<1: les.append(f'Exam {it["id"]}: profile was {g}, answered {a}; moved {g} centroid → {c}.')
    return les
