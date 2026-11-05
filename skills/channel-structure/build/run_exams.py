import sys, json, csv, importlib
mod=importlib.import_module(sys.argv[1]); out=sys.argv[2]
items=mod.gen_items(); sol=mod.Solver(); rows=[]; log=[]; block=[]
for it in items:
    a=mod.answer(sol,it); s=mod.score(it,a); rows.append((it,a,s)); block.append((it,a,s))
    if len(block)==10:
        les=mod.fold(sol,None,block); avg=sum(x[2] for x in block)/10
        log.append((it['id'],avg,les)); block=[]
json.dump(dict(items=items,answers=[r[1] for r in rows],scores=[r[2] for r in rows],log=log),open(out,'w'),default=str,indent=1)
sc=[r[2] for r in rows]
print([round(sum(sc[i:i+10])/10,2) for i in range(0,100,10)])
from collections import defaultdict
d=defaultdict(list)
for it,a,s in rows: d[it['type']].append(s)
print({k:round(sum(v)/len(v),2) for k,v in d.items()})
