import numpy as np, re
from feats import feats, NAMES, ents
def first_sent(t):
    m=re.split(r'(?<=[.!?])\s+',t.strip(),maxsplit=1); return m[0]
_FC={}
def fvec(t,names):
    if t not in _FC: _FC[t]=feats(t,first_sent(t))
    d=_FC[t]; return np.array([d[k] for k in names])
def logreg(X,y,l2=0.5,it=600,lr=0.3):
    w=np.zeros(X.shape[1]); b=0.
    for _ in range(it):
        p=1/(1+np.exp(-(X@w+b))); g=X.T@(p-y)/len(y)+l2*w/len(y); w-=lr*g; b-=lr*np.mean(p-y)
    return w,b
def fit_choice(items,names,fx):
    """pairwise ranker: gold option vs each distractor (contrastive pairs)."""
    X=[];y=[]
    for it in items:
        V=[fx(it,i,names) for i in range(len(it['options']))]
        for j in range(len(V)):
            if j==it['gold']: continue
            X.append(V[it['gold']]-V[j]); y.append(1); X.append(V[j]-V[it['gold']]); y.append(0)
    X=np.array(X); w,_=logreg(X,np.array(y,float)); return w
def pred_choice(it,w,names,fx):
    s=[fx(it,i,names)@w for i in range(len(it['options']))]; return int(np.argmax(s))
def fit_multi(items,names,classes,fx):
    W={}
    X=np.array([fx(it,names) for it in items])
    for c in classes:
        y=np.array([1. if it['gold']==c else 0. for it in items]); W[c]=logreg(X,y)
    return W
def pred_multi(it,W,names,fx):
    x=fx(it,names); return max(W,key=lambda c:x@W[c][0]+W[c][1])
def acc(items,pred,wt=True):
    s=[(float(pred(it)==it['gold']),it['w'] if wt else 1) for it in items]
    return sum(a*b for a,b in s)/sum(b for _,b in s)
def forward_select(train,val,cands,fit,predf,start=(),min_gain=0.005,log=None):
    sel=list(start); best=acc(val,lambda it:predf(it,fit(train,sel) if sel else None,sel)) if sel else 0.0
    if log is not None: log.append(('start',tuple(sel),round(best,3)))
    while True:
        trials=[]
        for c in cands:
            if c in sel: continue
            s2=sel+[c]; m=fit(train,s2); a=acc(val,lambda it:predf(it,m,s2)); trials.append((a,c))
        if not trials: break
        trials.sort(reverse=True); a,c=trials[0]
        for a2,c2 in trials[1:]:
            if log is not None and a2-best<min_gain: log.append(('reject',c2,round(a2-best,3)))
        if a-best>=min_gain:
            sel.append(c); best=a
            if log is not None: log.append(('accept',c,round(best,3)))
        else:
            if log is not None: log.append(('reject',c,round(a-best,3)))
            break
    return sel,best
