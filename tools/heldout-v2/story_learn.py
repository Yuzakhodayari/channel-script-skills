import numpy as np, re, json, tasks, learn
from feats import NAMES, ents
from learn import fvec
TR=sum([tasks.story_items({'train'},100,s) for s in range(30)],[])
VA=sum([tasks.story_items({'val'},100,s) for s in range(100,110)],[])
by=lambda L,t:[x for x in L if x['type']==t]
# A: cold open
fxA=lambda it,i,names: fvec(it['options'][i],names)
fitA=lambda tr,names: learn.fit_choice(by(tr,'A'),names,fxA)
predA=lambda it,w,names: learn.pred_choice(it,w,names,fxA)
# B: placement
fxB=lambda it,names: fvec(it['text'],names)
fitB=lambda tr,names: learn.fit_multi(by(tr,'B'),names,['open','middle','close'],fxB)
predB=lambda it,W,names: learn.pred_multi(it,W,names,fxB)
# C: next beat (pair features)
def W_(t): return set(re.findall(r"[a-z0-9']+",t.lower()))
PAIR=['overlap','ent_overlap','num_thread','pronoun_start','qa','cand_new_ent','len','content_overlap']
STOP=set("the a an and or but so to of in on at for is are was were it this that i you we they he she be have has had do not with as just like what".split())
def pairf(ctx,c,names):
    A=W_(ctx);B=W_(c); d={}
    d['overlap']=len(A&B)/max(1,len(B))
    d['content_overlap']=len((A-STOP)&(B-STOP))/max(1,len(B-STOP))
    ec=ents(c); ea=ents(ctx); d['ent_overlap']=len(ea&ec); d['cand_new_ent']=len(ec-ea)
    d['num_thread']=float(bool(re.search(r"\d",ctx[-120:])) and bool(re.search(r"\d|that's|which",c.lower())))
    d['pronoun_start']=float(bool(re.match(r"\W*(It|That|This|They|He|She|And|But|So|Which|Now|Then)\b",c)))
    d['qa']=float(ctx.rstrip().endswith('?') and bool(re.match(r"\W*(Because|So|Well|The answer|It's|It|Yes|No)\b",c)))
    d['len']=len(c.split())/30
    return np.array([d[k] for k in names])
fxC=lambda it,i,names: pairf(it['passage'],it['options'][i],names)
fitC=lambda tr,names: learn.fit_choice(by(tr,'C'),names,fxC)
predC=lambda it,w,names: learn.pred_choice(it,w,names,fxC)
if __name__=='__main__':
    out={}
    for T,fit,pred,c in [('A',fitA,predA,NAMES),('B',fitB,predB,NAMES),('C',fitC,predC,PAIR)]:
        log=[]; sel,best=learn.forward_select(TR,by(VA,T),c,fit,pred,log=log)
        m=fit(TR+VA,sel)
        out[T]=dict(sel=sel,val=best,log=log,model=(m.tolist() if not isinstance(m,dict) else {k:(v[0].tolist(),v[1]) for k,v in m.items()}))
        print(T,round(best,3),sel)
    json.dump(out,open('story_model.json','w'),indent=1)
