import random, re, stats, json
from corpus import fmt
from stats import short
def wpick(rng,vs): 
    tot=sum(v['weight'] for v in vs); x=rng.uniform(0,tot)
    for v in vs:
        x-=v['weight']
        if x<=0: return v
    return vs[-1]
def mode(v): return {'Adam':'Adam','Gen':'Gen','Especially':'Mechanism','Oil':'Mechanism','Others':'Others'}[v['group']]
