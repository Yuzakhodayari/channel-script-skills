import os
import re,sys,stats
from corpus import fmt
from stats import short,verify
LAB={'Adam':'Adam','Gen':'Gen','Especially':'Especially','Oil':'Oil','Others':'Others'}
V={v['key']:v for v in stats.vids()}
def res(m):
    k,sub=m.group(1),m.group(2); v=V[k]
    from corpus import norm; s=next((s for s in v['sents'] if norm(sub) in norm(s['text'])),None)
    assert s,(k,sub); t=short(s['text'],60); assert verify(t,v),(k,t)
    return f'"{t}" — *{v["group"]}*, `{k}` @ {fmt(s["t"])} ({s["pct"]}%)'
for a,b in [('src/ap-structure.md','channel-structure'),('src/ap-audience.md','channel-audience')]:
    t=re.sub(r'\{\{([^|]+)\|([^}]+)\}\}',res,open(a).read())
    open(f'{W}/{b}/references/anti-patterns.md','w').write(t)
print('ok')
