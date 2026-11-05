# Method 2 product: position-signature lexicon learned from TRAIN videos only (reverse outline of every passage).
import re, math, collections, tasks
CL=['open','middle','close']
def cls(p): return 'open' if p<12 else 'close' if p>85 else 'middle' if 30<p<70 else None
def toks(t):
    w=re.findall(r"[a-z']+",t.lower()); return set(w)|{a+' '+b for a,b in zip(w,w[1:])}
def train(split,minvids=4):
    df={c:collections.Counter() for c in CL}; vids={}; n={c:0 for c in CL}
    for v in tasks.vids(split):
        for p in tasks.passages(v,40,90):
            c=cls(p['pct'])
            if not c: continue
            n[c]+=1
            for t in toks(p['text']):
                df[c][t]+=1; vids.setdefault(t,set()).add(v['key'])
    lex={}
    for t,vs in vids.items():
        if len(vs)<minvids: continue
        lex[t]={c:math.log((df[c][t]+0.5)/(n[c]+1)) - math.log((sum(df[k][t] for k in CL)+1.5)/(sum(n.values())+3)) for c in CL}
    return lex,n
def score(t,lex):
    s={c:0. for c in CL}
    for w in toks(t):
        if w in lex:
            for c in CL: s[c]+=lex[w][c]
    return s
