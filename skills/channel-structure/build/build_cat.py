import os
import re, json, random
import stats, crit_audience as CA, render_criteria as RC
from corpus import fmt
from stats import short, verify, GROUPS
from exam_audience import _head
LAB=RC.LAB; W=os.environ.get('CHANNEL_SKILLS_DIR',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
vs=stats.vids(); ids={c['name']:f'A{i:03d}' for i,c in enumerate(CA.C,1)}
def q(v,s):
    t=short(s['text'],40)
    return f'"{t}" — *{LAB[v["group"]]}* `{v["key"]}` @ {fmt(s["t"])} ({s["pct"]}%)' if verify(t,v) else None
out=['# Device catalog — audience engineering\n','Every rx device from `criteria.md`, with its **headline surface form** (first alternative of the detector — learn this one first), the full detector, **weighted placement by decile** (share of all weighted hits that fall in each 10% of runtime), the creator who leans on it most (weighted hits/1k), and up to 4 verbatim, machine-verified lines from different groups.\n','Read the decile row like a heat strip: where in a video this device lives. `▇` ≥20%, `▅` 12-19%, `▃` 6-11%, `▁` 1-5%, `·` <1%.\n']
def bar(p): return '▇' if p>=20 else '▅' if p>=12 else '▃' if p>=6 else '▁' if p>=1 else '·'
cats=[]
summary=[]
for c in CA.C:
    if c['kind']!='rx': continue
    rx,scope=c['spec']; R=re.compile(rx,re.I)
    if c['cat'] not in cats: cats.append(c['cat']); out.append(f'\n---\n\n## {c["cat"]}\n')
    dec=[0.0]*10; gr={g:[0,0] for g in GROUPS}; ex={g:[] for g in GROUPS}
    for v in vs:
        h=[s for s in v['sents'] if R.search(s['text'])]
        gr[v['group']][0]+=len(h)*v['weight']; gr[v['group']][1]+=v['words']*v['weight']
        for s in h:
            dec[min(int(s['pct']//10),9)]+=v['weight']
            if 6<=len(s['text'].split())<=40: ex[v['group']].append((v,s))
    tot=sum(dec) or 1; dp=[round(100*d/tot) for d in dec]
    rate={g:(round(1000*a/b,2) if b else 0) for g,(a,b) in gr.items()}
    top=max(rate,key=rate.get)
    out.append(f'### {ids[c["name"]]} {c["name"]}\n\n*{c["defi"]}*\n\n- Headline form: `{_head(rx)}`\n- Full detector: `{rx}`\n- Placement 0→100%: `{"".join(bar(p) for p in dp)}`  ({" ".join(f"{i*10}:{p}" for i,p in enumerate(dp))})\n- Leans on it most: **{LAB[top]}** ({rate[top]}/1k vs ' + ', '.join(f'{g} {rate[g]}' for g in GROUPS if g!=top)+')\n- Use: '+c['do']+'  Avoid: '+c['dont']+'\n')
    n=0
    for g in GROUPS:
        if ex[g] and n<4:
            v,s=ex[g][len(ex[g])//2]; l=q(v,s)
            if l: out.append('> '+l+'\n'); n+=1
    if n==0: out.append('> *(no corpus hits — rare device)*\n')
    peak=max(range(10),key=lambda i:dp[i]); summary.append((ids[c['name']],c['name'],peak*10,top,sum(1 for v in vs if any(R.search(s['text']) for s in v['sents']))))
out.insert(3,'\n## Quick index (device → peak decile, heaviest user, videos using it /31)\n\n| id | device | peak decile | heaviest | videos |\n|---|---|---|---|---|\n'+'\n'.join(f'| {a} | {b} | {p}% | {t} | {n} |' for a,b,p,t,n in summary)+'\n')
# re-hook timeline per video
RH=re.compile(r"\?$|^but\b|here'?s (the|what|why|where|how)|turns? out|it gets (worse|weirder|crazier)|^wait|hold on",re.I)
out.append('\n---\n\n## Re-hook timelines (every video)\n\nGap = seconds between consecutive re-hook sentences (question, "But…", "here\'s…", "turns out", "it gets…", "wait"). Longest gap shows where a video "goes flat"; note where it sits.\n\n| video | group | re-hooks | median gap s | longest gap s @ position |\n|---|---|---|---|---|')
for v in vs:
    ts=[s for s in v['sents'] if RH.search(s['text'].strip())]
    if len(ts)<2: out.append(f'| `{v["key"]}` | {v["group"]} | {len(ts)} | — | — |'); continue
    g=[(ts[i+1]['t']-ts[i]['t'],ts[i]['pct']) for i in range(len(ts)-1)]
    gs=sorted(x for x,_ in g); m=gs[len(gs)//2]; L=max(g)
    out.append(f'| `{v["key"]}` | {v["group"]} | {len(ts)} | {round(m)} | {round(L[0])} @ {L[1]}% |')
open(f'{W}/channel-audience/references/device-catalog.md','w').write('\n'.join(out))
print(len(summary))
