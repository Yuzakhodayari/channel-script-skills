# solvers for worked examples, fit on TRAIN only (no test access)
import json, tasks, learn, story2, audience_learn as AL
from learn import fvec
by=lambda L,t:[x for x in L if x['type']==t]
SM=json.load(open('story_model.json')); TM=json.load(open('structure_model.json')); AM=json.load(open('audience_model.json'))
TR=sum([tasks.story_items({'train'},100,s) for s in range(10)],[])
for it in TR: it['_inner']=1
fxA=lambda it,i,n: fvec(it['options'][i],n); wA=learn.fit_choice(by(TR,'A'),SM['A']['sel'],fxA)
selB=['lex_close','in_medias_res','past','year_date']; WB=learn.fit_multi(by(TR,'B'),selB,['open','middle','close'],lambda it,n: story2.bfeat(it,n,('train',)))
idf=story2.build_idf({'train'}); selC=['cos','cand_new_ent','ent_overlap','len']
fxC=lambda it,i,n: story2.pairf(it['passage'],it['options'][i],idf,n); wC=learn.fit_choice(by(TR,'C'),selC,fxC)
def story(it):
    if it['type']=='A': return learn.pred_choice(it,wA,SM['A']['sel'],fxA)
    if it['type']=='B': return learn.pred_multi(it,WB,selB,lambda i,n: story2.bfeat(i,n,('train',)))
    return learn.pred_choice(it,wC,selC,fxC)
TRs=sum([tasks.structure_items({'train'},120,s) for s in range(8)],[]); w3=learn.fit_choice(by(TRs,'T3'),TM['T3']['sel'],fxA)
def t3(it): return learn.pred_choice(it,w3,TM['T3']['sel'],fxA)
TRa=AL.gen({'train'},range(6))
for it in TRa: it['_inner']=1
AW={T:learn.fit_choice(by(TRa,T),AM[T]['sel'],AL.ofx) for T in('A2','A4')}; W3=learn.fit_multi(by(TRa,'A3'),AM['A3']['sel'],AL.MODES,AL.mfx)
sol=AL.EA.Solver()
def aud(it):
    T=it['type']
    if T in AW: return learn.pred_choice(it,AW[T],AM[T]['sel'],AL.ofx)
    if T=='A3': return learn.pred_multi(it,W3,AM['A3']['sel'],AL.mfx)
    return AL.EA.answer(sol,it)
