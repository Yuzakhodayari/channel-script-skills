import numpy as np, re, json, statistics as st, tasks, learn, beats, stats
from feats import NAMES
from learn import fvec
from examlib import mode
by=lambda L,t:[x for x in L if x['type']==t]
def gen(split,seeds): return sum([tasks.structure_items(split,120,s) for s in seeds],[])
# label definitions = the skill's beat taxonomy (references/beat-maps.md); same regexes the beat maps were built with
DEF=[('SPONSOR READ',beats.SPON),('CTA',beats.CTA),('CONCLUSION',beats.CONC),('PROMISE / ROADMAP',beats.PROMISE),('SECTION TURN',beats.TRANS)]
BRIDGE=re.compile(r"(that'?s (exactly )?(where|why)|speaking of|which is why I|this (video|episode) is)",re.I)
def label(text,pct=None):
    hits=[L for L,rx in DEF if rx.search(text)]
    if BRIDGE.search(text) and (pct is None or 15<pct<90): hits.insert(0,'SPONSOR READ')
    if pct is not None:
        if pct>=90 and 'CTA' in hits: return 'CTA'
        if pct<=25 and 'PROMISE / ROADMAP' in hits: return 'PROMISE / ROADMAP'
        if pct>=75 and 'CONCLUSION' in hits: return 'CONCLUSION'
    if hits: return hits[0]
    if text.rstrip().endswith('?') and len(text.split())>=6: return 'SECTION TURN'
    if pct is None: return 'HOOK END (unmarked)'
    if pct is not None:
        return 'PROMISE / ROADMAP' if pct<12 else 'CONCLUSION' if pct>80 else 'SECTION TURN'
    return 'SECTION TURN'
def pos_table(items):
    d={}
    for it in items: d.setdefault(it['beat'],[]).append(it['pct'])
    return {k:round(st.median(v),1) for k,v in d.items()}
def place(text,P,LP):
    L=label(text); p=P.get(L,50) if L!='HOOK END (unmarked)' else P.get('PROMISE / ROADMAP',6)
    if L=='CTA' and not re.search(r"thank|see you|watching|bye|next (one|video)",text,re.I): p=LP.get('CTA_mid',p)
    if L=='SPONSOR READ': p=LP.get('SPON',p)
    return p
if __name__=='__main__':
    TR=gen({'train'},range(20)); VA=gen({'val'},range(100,106))
    out={}
    # T3 opener
    fx=lambda it,i,names: fvec(it['options'][i],names)
    fit=lambda tr,names: learn.fit_choice(by(tr,'T3'),names,fx)
    pred=lambda it,w,names: learn.pred_choice(it,w,names,fx)
    log=[]; sel,b=learn.forward_select(TR,by(VA,'T3'),NAMES,fit,pred,log=log); w=fit(TR+VA,sel)
    out['T3']=dict(sel=sel,val=b,w=w.tolist(),log=log); print('T3',b,sel,np.round(w,2))
    # T1 label accuracy with definitions
    print('T1 val',learn.acc(by(VA,'T1'),lambda it:label(it['text'],it['pct'])))
    # T2 position table from train beats; CTA split
    ev=[it for it in TR if it['type'] in('T1','T2')]
    P=pos_table(ev)
    cm=[it['pct'] for it in ev if it['beat']=='CTA' and not re.search(r"thank|see you|watching|bye|next (one|video)",it['text'],re.I)]
    sp=[it['pct'] for it in ev if it['beat']=='SPONSOR READ']
    LP={'CTA_mid':round(st.median(cm),1) if cm else 95,'SPON':round(st.median(sp),1)}
    def sc2(it,a): d=abs(a-it['gold']); return 1.0 if d<=10 else 0.5 if d<=20 else 0.0
    v2=by(VA,'T2'); print('T2 val',sum(sc2(it,place(it['text'],P,LP)) for it in v2)/len(v2),P,LP)
    out['T2']=dict(P=P,LP=LP)
    json.dump(out,open('structure_model.json','w'),indent=1)
