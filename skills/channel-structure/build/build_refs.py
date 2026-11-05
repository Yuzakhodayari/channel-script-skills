import os, re, json, random, shutil
import stats, render_criteria as RC, render_beats as RB, crit_structure as CS, crit_audience as CA
from corpus import fmt
from stats import short, verify, GROUPS
LAB=RC.LAB
W=os.environ.get('CHANNEL_SKILLS_DIR',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
for sk in ['channel-structure','channel-audience']:
    for d in ['references','training','exams','build']: os.makedirs(f'{W}/{sk}/{d}',exist_ok=True)
t=RC.render(CS.C,CS.F,'Channel structure — 105 criteria (strategy, architecture, timing)','S'); open(f'{W}/channel-structure/references/criteria.md','w').write(t)
json.dump([{k:c.get(k) for k in('id','cat','name','defi','do','dont','test','band','p25','p75')} for c in CS.C],open('/tmp/cs.json','w'),default=str)
t=RC.render(CA.C,CA.F,'Channel audience engineering — 106 criteria (retention, psychology, address)','A'); open(f'{W}/channel-audience/references/criteria.md','w').write(t)
json.dump([{k:c.get(k) for k in('id','cat','name','defi','do','dont','test','band','p25','p75','spec')} for c in CA.C],open('/tmp/ca.json','w'),default=str)
open(f'{W}/channel-structure/references/beat-maps.md','w').write(RB.render())
ok=sum(1 for x in RC.VERIFY_LOG if x[2]); print('verify',ok,len(RC.VERIFY_LOG))
# copy build scripts
for sk in ['channel-structure','channel-audience']:
    for f in os.listdir('.'):
        if f.endswith('.py'): shutil.copy(f,f'{W}/{sk}/build/{f}')
