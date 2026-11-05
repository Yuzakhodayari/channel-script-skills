import os
"""Final held-out exams: 100 TEST items per skill (seed 2026), before (v1 solver) vs after (v2 rules)."""
import sys, json, importlib.util, numpy as np, tasks, learn, story2, nbpos as N, structure_learn as SL
from learn import fvec
def load(name,path):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
SEED=2026; TRS=range(20); OUT={}
def wmean(rows):
    return sum(s*w for s,w in rows)/sum(w for _,w in rows)
def report(skill,items,ans_old,ans_new,score):
    per={}
    for it in items:
        o=score(it,ans_old(it)); n=score(it,ans_new(it)); per.setdefault(it['type'],[]).append((o,n,it['w']))
    res={T:dict(n=len(v),before=round(wmean([(o,w) for o,_,w in v]),3),after=round(wmean([(n,w) for _,n,w in v]),3)) for T,v in sorted(per.items())}
    allv=sum(per.values(),[])
    res['overall']=dict(n=len(allv),before=round(wmean([(o,w) for o,_,w in allv]),3),after=round(wmean([(n,w) for _,n,w in allv]),3),
        before_unweighted=round(np.mean([o for o,_,_ in allv]),3),after_unweighted=round(np.mean([n for _,n,_ in allv]),3))
    OUT[skill]=res; print(skill,json.dumps(res))
# ---------- STORY ----------
by=lambda L,t:[x for x in L if x['type']==t]
SM=json.load(open('story_model.json'))
TR=sum([tasks.story_items({'train'},100,s) for s in range(30)],[])
for it in TR: it['_inner']=1
TE=tasks.story_items({'test'},100,SEED)
R2=json.load(open('round2_model.json')) if len(sys.argv)>1 else None
selA=R2['story_A']['sel'] if R2 else SM['A']['sel']; TR=TR+[x for x in sum([tasks.story_items({'val'},100,s) for s in range(100,110)],[]) if R2 and x['type']=='A']; fxA=lambda it,i,n: fvec(it['options'][i],n); wA=learn.fit_choice(by(TR,'A'),selA,fxA)
selB=['lex_close','in_medias_res','past','year_date']; LS=('train','val')
fxB=lambda it,n: story2.bfeat(it,n,LS)
WB=learn.fit_multi(by(TR,'B'),selB,['open','middle','close'],lambda it,n: story2.bfeat(it,n,('train',)))
idf=story2.build_idf({'train','val'}); selC=['cos','cand_new_ent','ent_overlap','len']
fxC=lambda it,i,n: story2.pairf(it['passage'],it['options'][i],idf,n); wC=learn.fit_choice(by(TR,'C'),selC,fxC)
def story_new(it):
    if it['type']=='A': return learn.pred_choice(it,wA,selA,fxA)
    if it['type']=='B': return learn.pred_multi(it,WB,selB,fxB)
    return learn.pred_choice(it,wC,selC,fxC)
import baseline_story as BS
report('channel-storytelling',TE,BS.answer,story_new,lambda it,a:float(a==it['gold']))
# ---------- STRUCTURE ----------
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','skills','channel-structure','build'))
ES=load('es_v1',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','skills','channel-structure','build','exam_structure.py')); sol=ES.Solver()
SMd=json.load(open('structure_model.json'))
TRs=sum([tasks.structure_items({'train'},120,s) for s in TRS],[]); TEs=tasks.structure_items({'test'},100,SEED)
for it in TEs: it['prompt_text']=it.get('text')
sel3=R2['struct_T3']['sel'] if R2 else SMd['T3']['sel']; TRs=TRs+([x for x in sum([tasks.structure_items({'val'},120,s) for s in range(100,106)],[]) if x['type']=='T3'] if R2 else []); fx3=lambda it,i,n: fvec(it['options'][i],n); w3=learn.fit_choice(by(TRs,'T3'),sel3,fx3)
P=SMd['T2']['P']; LP=SMd['T2']['LP']
def struct_new(it):
    T=it['type']
    if T=='T1': return SL.label(it['text'],it['pct'])
    if T=='T2': return SL.place(it['text'],P,LP)
    if T=='T3': return learn.pred_choice(it,w3,sel3,fx3)
    if T=='T6':
        p=[SL.place(t,P,LP) for t in it['shuffled']]; return sorted(range(len(p)),key=lambda i:p[i])
    return ES.answer(sol,it)
report('channel-structure',TEs,lambda it:ES.answer(sol,it),struct_new,ES.score)
# ---------- AUDIENCE ----------
import audience_learn as AL
EA=AL.EA; asol=EA.Solver(); AM=json.load(open('audience_model.json'))
TRa=AL.gen({'train'},range(12))
for it in TRa: it['_inner']=1
TEa=tasks.audience_items({'test'},100,SEED,AL.RX)
W={}
for T in('A2','A4'):
    s=(R2['aud_A2']['sel'] if (R2 and T=='A2') else AM[T]['sel']); W[T]=(s,learn.fit_choice(by(TRa,T),s,AL.ofx))
s3=AM['A3']['sel']; W3=learn.fit_multi(by(TRa,'A3'),s3,AL.MODES,AL.mfx)
def aud_new(it):
    T=it['type']
    if T in W: s,w=W[T]; return learn.pred_choice(it,w,s,AL.ofx)
    if T=='A3': return learn.pred_multi(it,W3,s3,AL.mfx)
    return EA.answer(asol,it)
report('channel-audience',TEa,lambda it:EA.answer(asol,it),aud_new,EA.score)
json.dump(OUT,open('final_scores%s.json'%('_round2' if R2 else ''),'w'),indent=1)
