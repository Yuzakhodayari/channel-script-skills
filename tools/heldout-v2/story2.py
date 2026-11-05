import numpy as np, re, math, collections, tasks, learn, nbpos
from feats import NAMES, ents
from learn import fvec
def stem(w): return re.sub(r"(ing|ed|es|s|'s)$","",w)
def build_idf(split):
    dfs=collections.Counter(); N=0
    for v in tasks.vids(split):
        for s in v['sents']:
            N+=1
            for w in set(stem(w) for w in re.findall(r"[a-z0-9']+",s['text'].lower()) if len(w)>2): dfs[w]+=1
    return lambda w: math.log((N+1)/(dfs[w]+1))
def vec(t): return collections.Counter(stem(w) for w in re.findall(r"[a-z0-9']+",t.lower()) if len(w)>2)
def cos(a,b,idf):
    A=vec(a);B=vec(b); num=sum(A[w]*B[w]*idf(w)**2 for w in A if w in B)
    da=math.sqrt(sum((A[w]*idf(w))**2 for w in A)); db=math.sqrt(sum((B[w]*idf(w))**2 for w in B)); return num/(da*db+1e-9)
def fmt(t):
    return (bool(re.match(r"\W*[a-z]",t)), bool(re.search(r"[.!?]['\"”]?\s*$",t.strip())), '[ __ ]' in t or bool(re.search(r"\b(uh|um)\b",t)))
PAIR=['cos','ent_overlap','fmt_match','pronoun_start','len','cand_new_ent','qa']
def pairf(ctx,c,idf,names):
    d={}; d['cos']=cos(ctx,c,idf)
    ec=ents(c); ea=ents(ctx); d['ent_overlap']=len(ea&ec); d['cand_new_ent']=len(ec-ea)
    fc=fmt(c); sents=re.split(r'(?<=[.!?])\s+',ctx); lower_ctx=sum(bool(re.match(r"\W*[a-z]",s)) for s in sents)/max(1,len(sents))
    noisy_ctx=fmt(ctx)[2]
    d['fmt_match']=-(abs(float(fc[0])-lower_ctx)) - float(fc[2]!=noisy_ctx)
    d['pronoun_start']=float(bool(re.match(r"\W*(It|That|This|They|He|She|And|But|So|Which|Now|Then)\b",c)))
    d['qa']=float(ctx.rstrip().endswith('?') and bool(re.match(r"\W*(Because|So|Well|The answer|It's|It|Yes|No)\b",c)))
    d['len']=len(c.split())/30
    return np.array([d[k] for k in names])
# ---- B placement: hand features + cross-fitted position lexicon (method 2 signature table) ----
_LEX={}
def lex_for(excl_key,split=('train',)):
    k=(excl_key,split)
    if k not in _LEX:
        import nbpos as N
        keys=[v['key'] for v in tasks.vids(set(split)) if v['key']!=excl_key]
        _LEX[k]=train_lex(keys)
    return _LEX[k]
def train_lex(keys,minvids=3):
    import nbpos as N
    df={c:collections.Counter() for c in N.CL}; vids={}; n={c:0 for c in N.CL}
    for v in tasks.VS:
        if v['key'] not in keys: continue
        for p in tasks.passages(v,40,90):
            c=N.cls(p['pct'])
            if not c: continue
            n[c]+=1
            for t in N.toks(p['text']): df[c][t]+=1; vids.setdefault(t,set()).add(v['key'])
    lex={}
    for t,vs in vids.items():
        if len(vs)<minvids: continue
        lex[t]={c:math.log((df[c][t]+0.5)/(n[c]+1)) - math.log((sum(df[k][t] for k in N.CL)+1.5)/(sum(n.values())+3)) for c in N.CL}
    return lex
def bfeat(it,names,lexsplit):
    import nbpos as N
    excl=it['video'] if it.get('_inner') else None
    lex=lex_for(excl,lexsplit); s=N.score(it['text'],lex); nt=max(1,len(N.toks(it['text'])))
    extra={'lex_open':(s['open']-s['middle'])/nt*10,'lex_close':(s['close']-s['middle'])/nt*10}
    base=[n for n in names if n not in extra]
    v=list(fvec(it['text'],base)) if base else []
    return np.array(v+[extra[n] for n in names if n in extra])
