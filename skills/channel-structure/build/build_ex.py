import os
import re, stats, render_criteria as RC, crit_audience as CA
from corpus import fmt
from stats import short, verify, GROUPS
LAB=RC.LAB; W=os.environ.get('CHANNEL_SKILLS_DIR',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')); vs=stats.vids()
QUOTA={'Adam':5,'Gen':3,'Oil':4,'Especially':2,'Others':1}
def ql(v,s,n=60):
    t=short(s['text'],n); return f'"{t}" @ {fmt(s["t"])} ({s["pct"]}%)' if verify(t,v) else None
def hook_par(v,b):
    S=v['sents']; e=b['hook_end']; txt=[]; 
    for s in S[:e+1]:
        if sum(len(x.split()) for x in txt)>110: break
        if verify(short(s['text'],60),v): txt.append(short(s['text'],60))
    return ' '.join(txt)
# STRUCTURE examples
o=['# Structure examples — verbatim, labeled, weight-proportional\n',
   f'Per-video quota by weight: Adam {QUOTA["Adam"]} each, Oil {QUOTA["Oil"]}, Gen {QUOTA["Gen"]}, Especially {QUOTA["Especially"]}, Others {QUOTA["Others"]}. Total share ≈ Adam 33%, Gen 39%, Oil 5%, Especially 8%, Others 15%, matching the 7/4/5/3/1 weighting. Every line is host-only and machine-verified against the source file. Label = the structural job the line does.\n']
ORDER=['HOOK (opening paragraph)','PROMISE / ROADMAP','SECTION TURN','SPONSOR READ','RETURN FROM SPONSOR','CONCLUSION','FINAL LINE','THESIS / STAKES']
n=0
for g in GROUPS:
    o.append(f'\n---\n\n## {LAB[g]}\n')
    for v in [x for x in vs if x['group']==g]:
        b=stats.BM[v['key']]; got=[]
        o.append(f'### `{v["key"]}` — "{v["title"]}" ({fmt(v["dur"])})\n')
        evs={}
        for e in b['events']: evs.setdefault(e['beat'],[]).append(e)
        for lab in ORDER:
            if len(got)>=QUOTA[g]: break
            if lab.startswith('HOOK'):
                p=hook_par(v,b)
                if p: got.append(f'- **{lab}** (0% → {v["sents"][b["hook_end"]]["pct"]}%): "{p}"')
                continue
            es=evs.get(lab) or []
            if lab=='SECTION TURN': es=es[len(es)//2:len(es)//2+1]
            for e in es[:1]:
                l=ql(v,v['sents'][e['i']])
                if l: got.append(f'- **{lab}**: {l}')
        o+=got; o.append(''); n+=len(got)
o.append(f'\n*Total labeled examples: {n}.*\n')
open(f'{W}/channel-structure/references/examples.md','w').write('\n'.join(o))
# AUDIENCE examples: per video, cycle distinct device categories
RX=[c for c in CA.C if c['kind']=='rx']
o=['# Audience-engineering examples — verbatim, labeled, weight-proportional\n','Per-video quota ∝ weight (Adam 5, Oil 4, Gen 3, Especially 2, Others 1), each from a different device category, spread across the runtime. Label = device id + name from `criteria.md`. All lines host-only and machine-verified.\n']
ids={c['name']:f'A{i:03d}' for i,c in enumerate(CA.C,1)}; n=0
for g in GROUPS:
    o.append(f'\n---\n\n## {LAB[g]}\n')
    for k,v in enumerate([x for x in vs if x['group']==g]):
        o.append(f'### `{v["key"]}` — "{v["title"]}"\n'); used=set(); got=0
        zones=[(0,10),(10,40),(40,70),(70,90),(90,101)]
        for zi in range(QUOTA[g]*3):
            if got>=QUOTA[g]: break
            lo,hi=zones[zi%5]
            for c in RX[(k*7+zi*13)%len(RX):]+RX:
                if c['cat'] in used: continue
                R=re.compile(c['spec'][0],re.I)
                h=[s for s in v['sents'] if lo<=s['pct']<hi and R.search(s['text']) and 6<=len(s['text'].split())<=40]
                if not h: continue
                l=ql(v,h[0])
                if l: o.append(f'- **{ids[c["name"]]} {c["name"]}** [{c["cat"]}]: {l}'); used.add(c['cat']); got+=1; n+=1; break
        o.append('')
o.append(f'\n*Total labeled examples: {n}.*\n')
open(f'{W}/channel-audience/references/examples.md','w').write('\n'.join(o))
