import re, statistics as st
from corpus import *
from beats import *
VS=None; BM={}
def vids():
    global VS
    if VS is None:
        VS=all_videos()
        for v in VS: BM[v['key']]=beatmap(v)
    return VS
SCOPES={'hook':(0,8),'open':(0,15),'body':(15,85),'mid':(30,70),'end':(85,101),'all':(0,101),'close':(75,101),'first_min':None}
def in_scope(v,s,scope):
    if scope=='first_min': return s['t']<=60
    a,b=SCOPES[scope]; return a<=s['pct']<b
def wmean(pairs):
    sw=sum(w for _,w in pairs); return sum(x*w for x,w in pairs)/sw if sw else 0
def wmedian(pairs):
    pairs=sorted(pairs); sw=sum(w for _,w in pairs); c=0
    for x,w in pairs:
        c+=w
        if c>=sw/2: return x
    return 0
GROUPS=['Adam','Gen','Especially','Oil','Others']
def short(t,n=40):
    w=t.split(); return ' '.join(w[:n])+(' […]' if len(w)>n else '')
def regex_stats(rx,scope='all'):
    R_=re.compile(rx,re.I); res={'groups':{},'quotes':{},'hits':[]}
    allp=[]; cov=[]; rate=[]; first=[]
    for g in GROUPS:
        gv=[v for v in vids() if v['group']==g]; hv=0; hits=0; words=0; fp=[]; qs=[]
        for v in gv:
            h=[s for s in v['sents'] if in_scope(v,s,scope) and R_.search(s['text'])]
            words+=v['words']; hits+=len(h)
            if h: hv+=1; fp.append(h[0]['pct']); qs.append((v,h[0])); allp+= [x['pct'] for x in h]
            cov.append((1 if h else 0,v['weight'])); rate.append((1000*len(h)/max(v['words'],1),v['weight']))
            if h: first.append((h[0]['pct'],v['weight']))
            for x in h: res['hits'].append((v['key'],x))
        res['groups'][g]=dict(cov=f'{hv}/{len(gv)}',rate=round(1000*hits/max(words,1),2),first=round(st.median(fp),1) if fp else None)
        # pick quote: prefer moderate length
        qs.sort(key=lambda q: abs(len(q[1]['text'].split())-18))
        res['quotes'][g]=[(q[0]['key'],q[0]['title'],q[1]) for q in qs[:2]]
    res['w_cov']=round(100*wmean(cov)); res['w_rate']=round(wmean(rate),2); res['w_first']=round(wmedian(first),1) if first else None
    return res
def func_stats(f):
    res={'groups':{},'vals':[]}; pairs=[]
    for g in GROUPS:
        xs=[]
        for v in vids():
            if v['group']!=g: continue
            x=f(v,BM[v['key']])
            if x is None: continue
            xs.append(x); pairs.append((x,v['weight'])); res['vals'].append((v['key'],x))
        res['groups'][g]=dict(median=round(st.median(xs),1) if xs else None,min=round(min(xs),1) if xs else None,max=round(max(xs),1) if xs else None)
    res['w_median']=round(wmedian(pairs),1) if pairs else None; res['w_mean']=round(wmean(pairs),1) if pairs else None
    return res
_rawn={}
def verify(q,v):
    if v['key'] not in _rawn:
        r=re.sub(r'\(\d+:\d+(:\d+)?\)','',v['raw']); r=NOISE.sub('',r).replace('>>',''); _rawn[v['key']]=norm(r)
    return all(norm(p) in _rawn[v['key']] for p in q.split('[…]') if norm(p))
