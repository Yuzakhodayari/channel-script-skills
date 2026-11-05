import re, json
import stats
from corpus import fmt, GW
from stats import GROUPS, short, verify
LAB={'Adam':'Adam (7x)','Gen':'Gen (4x)','Especially':'Especially (3x)','Oil':'Oil (5x)','Others':'Others (1x)'}
def wq(pairs,q):
    pairs=sorted(pairs); sw=sum(w for _,w in pairs); c=0
    for x,w in pairs:
        c+=w
        if c>=sw*q: return x
    return None
VERIFY_LOG=[]
def vid(key): return next(v for v in stats.vids() if v['key']==key)
def qline(g,key,title,s):
    t=short(s['text'],45); ok=verify(t,vid(key)); VERIFY_LOG.append((key,t,ok))
    return f'> "{t}" — *{LAB[g]}*, `{key}` "{title[:60]}" @ {fmt(s["t"])} ({s["pct"]}%)' if ok else None
def render(C,F,title,prefix):
    out=[f'# {title}\n','Every number below is **measured** from host-only transcript text by `build/` scripts. Weights are per video: Adam 7, Gen 4, oil 5, especially (spacex, ai-paradox, data-centers) 3, after/ 1. Especially 04/05/07 are deduplicated into Adam. "w-" = weighted across all 31 videos.\n',
         'Quotes are verbatim (caption text, guest lines removed) and were machine-verified against the source files; `[…]` marks a cut. Detector = the regex/function used, so you can re-run it.\n','Columns: **cov** = videos with ≥1 hit / videos; **/1k** = hits per 1,000 host words; **first%** = median position of first hit.\n']
    cats=[]
    for i,cr in enumerate(C,1):
        if cr['cat'] not in cats: cats.append(cr['cat']); out.append(f'\n---\n\n## {cr["cat"]}\n')
        cid=f'{prefix}{i:03d}'; cr['id']=cid
        out.append(f'### {cid}. {cr["name"]}\n\n**Definition.** {cr["defi"]}\n')
        if cr['kind']=='rx':
            rx,scope=cr['spec']; r=stats.regex_stats(rx,scope); cr['stats']=r
            out.append(f'**Detector.** regex `{rx}` in scope `{scope}`.\n\n| group | cov | /1k | first% |\n|---|---|---|---|')
            for g in GROUPS:
                d=r['groups'][g]; out.append(f'| {LAB[g]} | {d["cov"]} | {d["rate"]} | {d["first"] if d["first"] is not None else "—"} |')
            out.append(f'| **weighted** | {r["w_cov"]}% of weight | {r["w_rate"]} | {r["w_first"]} |\n')
            out.append('**How each creator does it (verbatim):**\n')
            n=0
            for g in GROUPS:
                for key,tt,s in r['quotes'][g][:1 if g in ('Others','Especially') else 2]:
                    q=qline(g,key,tt,s)
                    if q: out.append(q+'\n'); n+=1
            if n==0: out.append('> *No hits in corpus: this device is essentially absent. Treat as a DON\'T unless a topic demands it.*\n')
            band='present' if r['w_cov']>=50 else ('optional' if r['w_cov']>=20 else 'rare')
            cr['test']=(f"In scope `{scope}`, count sentences matching the detector. Weighted norm ≈ {r['w_rate']}/1k words; "
                        + (f"PASS if ≥1 hit (corpus uses it in {r['w_cov']}% of weighted videos) and rate ≤ {round(max(r['w_rate']*2,1),1)}/1k." if band=='present'
                           else f"PASS if 0-{max(1,round(r['w_rate']*2))} per 1k words; it is {band} ({r['w_cov']}% weighted coverage) — only use with a reason."))
            cr['band']=band
        else:
            r=stats.func_stats(F[cr['spec']]); cr['stats']=r
            vals=[(x,vid(k)['weight']) for k,x in r['vals']]
            p25,p75=wq(vals,.25),wq(vals,.75); cr['p25'],cr['p75']=p25,p75
            out.append(f'**Detector.** function `{cr["spec"]}` (see `build/crit_*.py`).\n\n| group | median | min | max |\n|---|---|---|---|')
            for g in GROUPS:
                d=r['groups'][g]; out.append(f'| {LAB[g]} | {d["median"] if d["median"] is not None else "—"} | {d["min"] if d["min"] is not None else "—"} | {d["max"] if d["max"] is not None else "—"} |')
            out.append(f'| **weighted** | median {r["w_median"]} (IQR {p25}–{p75}) | | |\n')
            per=', '.join(f'`{k}`={x}' for k,x in r['vals'])
            out.append('**How each creator does it (verbatim anchor lines):**\n')
            from anchors import ANCH,QRX
            for g in GROUPS:
                gv=[v for v in stats.vids() if v['group']==g]
                lim=1 if g in ('Others','Especially') else 2; got=0
                for v in gv:
                    if got>=lim: break
                    b=stats.BM[v['key']]; idx=None
                    if cr['spec'] in ANCH:
                        try: idx=ANCH[cr['spec']](v,b)
                        except Exception: idx=None
                    elif cr['spec'] in QRX:
                        R=re.compile(QRX[cr['spec']],re.I); cand=[i for i,s in enumerate(v['sents']) if R.search(s['text']) and 6<=len(s['text'].split())<=40]
                        idx=cand[len(cand)//2] if cand else None
                    if idx is None: continue
                    s=v['sents'][idx]; val=dict(r['vals']).get(v['key'])
                    q=qline(g,v['key'],v['title'],s)
                    if q: out.append(q+f' — value here: **{val}**\n'); got+=1
            out.append(f'<details><summary>Per-video values</summary>\n\n{per}\n\n</details>\n')
            cr['test']=f"Compute `{cr['spec']}` on your outline/draft. PASS if inside the weighted IQR {p25}–{p75}, or inside the chosen mode's min–max range (see table)."
        out.append(f'**Do.** {cr["do"]}\n\n**Don\'t.** {cr["dont"]}\n\n**Checklist test.** {cr["test"]}\n')
    return '\n'.join(out)
