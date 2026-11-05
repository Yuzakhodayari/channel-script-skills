"""Round 2 (no test access): leave-one-video-out CV over TRAIN+VAL for the opener-type tasks,
to pick a more robust feature set than the single-val forward select (which overfit story A)."""
import json, numpy as np, tasks, learn, audience_learn as AL
from learn import fvec
from feats import NAMES
by=lambda L,t:[x for x in L if x['type']==t]
def cv(items,names,fx):
    keys=sorted({it['video'] for it in items}); tot=0;W=0
    for k in keys:
        tr=[i for i in items if i['video']!=k]; te=[i for i in items if i['video']==k]
        w=learn.fit_choice(tr,names,fx)
        for it in te: tot+=it['w']*(learn.pred_choice(it,w,names,fx)==it['gold']); W+=it['w']
    return tot/W
def select(items,fx,cands,log):
    sel=[];best=0
    while True:
        tr=sorted(((cv(items,sel+[c],fx),c) for c in cands if c not in sel),reverse=True)
        if not tr or tr[0][0]-best<0.01: log.append(('stop',tr[0][1] if tr else None,round(tr[0][0]-best,3) if tr else 0)); break
        best,c=tr[0]; sel.append(c); log.append(('accept',c,round(best,3)))
    return sel,best
fx=lambda it,i,n: fvec(it['options'][i],n)
out={}
SA=by(sum([tasks.story_items({'train','val'},100,s) for s in range(8)],[]),'A')
log=[];s,b=select(SA,fx,NAMES,log); out['story_A']=dict(sel=s,cv=b,log=log); print('story A',b,s)
ST=by(sum([tasks.structure_items({'train','val'},120,s) for s in range(8)],[]),'T3')
log=[];s,b=select(ST,fx,NAMES,log); out['struct_T3']=dict(sel=s,cv=b,log=log); print('T3',b,s)
AA=by(sum([AL.gen({'train','val'},[s]) for s in range(8)],[]),'A2')
log=[];s,b=select(AA,fx,NAMES,log); out['aud_A2']=dict(sel=s,cv=b,log=log); print('A2',b,s)
json.dump(out,open('round2_model.json','w'),indent=1)
