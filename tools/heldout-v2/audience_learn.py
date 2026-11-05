import os
import sys, json, numpy as np, re, collections, tasks, learn, nbpos as N
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','skills','channel-audience','build'))
import story2
from feats import NAMES
from learn import fvec
from examlib import mode
import exam_audience as EA
RX=EA.RX
by=lambda L,t:[x for x in L if x['type']==t]
def gen(split,seeds): return sum([tasks.audience_items(split,100,s,RX) for s in seeds],[])
LEXSPLIT=('train',)
def ofx(it,i,names):
    t=it['options'][i]; excl=it['video'] if it.get('_inner') else None
    lex=story2.lex_for(excl,LEXSPLIT); s=N.score(t,lex); nt=max(1,len(N.toks(t)))
    ex={'lex_open':(s['open']-s['middle'])/nt*10,'lex_close':(s['close']-s['middle'])/nt*10}
    return np.array([ex[n] if n in ex else fvec(t,[n])[0] for n in names])
CAND=NAMES+['lex_open','lex_close']
# A3 mode: one-vs-rest on rate features
MODES=['Adam','Gen','Mechanism','Others']
def mfx(it,names): return fvec(it['text'],names)
if __name__=='__main__':
    TR=gen({'train'},range(12)); VA=gen({'val'},range(100,106))
    for it in TR: it['_inner']=1
    out={}
    for T in ('A2','A4'):
        fit=lambda tr,names,T=T: learn.fit_choice(by(tr,T),names,ofx)
        pred=lambda it,w,names: learn.pred_choice(it,w,names,ofx)
        log=[]; sel,b=learn.forward_select(TR,by(VA,T),CAND,fit,pred,log=log); w=fit(TR,sel)
        out[T]=dict(sel=sel,val=b,w=w.tolist(),log=log); print(T,round(b,3),sel,np.round(w,2))
    fit=lambda tr,names: learn.fit_multi(by(tr,'A3'),names,MODES,mfx)
    pred=lambda it,W,names: learn.pred_multi(it,W,names,mfx)
    log=[]; sel,b=learn.forward_select(TR,by(VA,'A3'),NAMES,fit,pred,log=log)
    W=fit(TR,sel); out['A3']=dict(sel=sel,val=b,W={k:[v[0].tolist(),v[1]] for k,v in W.items()},log=log); print('A3',round(b,3),sel)
    json.dump(out,open('audience_model.json','w'),indent=1)
