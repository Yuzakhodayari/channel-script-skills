import os
import json, csv, importlib, sys
from collections import defaultdict
W=os.environ.get('CHANNEL_SKILLS_DIR',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
DESC={'T1':'Beat labeling — name the structural job of a verbatim line given its position %','T2':'Position estimation — estimate where (% of runtime) a verbatim beat line sits; ±10 = full, ±20 = half','T3':'Real-opener MCQ — which of 4 lines from one video is its actual first line','T4':'Outline reconstruction — from title/mode/runtime/sponsor, predict hook-end %, sponsor %, conclusion %, number of turns; compared to gold beat map (4 points)','T5':'Mode attribution — from a structural profile (runtime, WPM, hook seconds, "you"/1k) pick Adam / Gen / Mechanism / Others','T6':'Beat ordering — put 4 shuffled beat lines from one video in runtime order (pairwise accuracy)',
 'A1':'Device spotting — which audience device does this verbatim line use (4 options, distractors verified absent)','A2':'Hook discrimination — which of 4 lines comes from the first 8% (the other 3 are from 30-70%)','A3':'Creator attribution — 130-word host passage → Adam / Gen / Mechanism / Others','A4':'Emotional calibration — which of 2 three-sentence passages is from the close (88-98%) vs the middle (40-60%)','A5':'Real vs flattened — one line is verbatim, the other had its address/question/momentum devices stripped; pick the real one'}
def run(modname,skill,title):
    mod=importlib.import_module(modname); items=mod.gen_items(); sol=mod.Solver(); rows=[]; log=[]; blk=[]
    for it in items:
        a=mod.answer(sol,it); s=mod.score(it,a); rows.append((it,a,s)); blk.append((it,a,s))
        if len(blk)==10: les=mod.fold(sol,None,blk); log.append((it['id'],sum(x[2] for x in blk)/10,les)); blk=[]
    D=f'{W}/{skill}/exams'
    with open(f'{D}/scores.csv','w',newline='') as f:
        w=csv.writer(f); w.writerow(['exam','type','video','group','score','block'])
        for it,a,s in rows: w.writerow([it['id'],it['type'],it['video'],it['group'],s,(it['id']-1)//10+1])
    E=[f'# {title} — 100 exams\n','Sampled by corpus weight (video drawn with probability ∝ 7/4/5/3/1), type rotated. Each exam: prompt, gold (from the real transcript / detected beat map), rubric. Re-run with `python3 build/run_exams.py {}` — deterministic seed.\n'.format(modname),'## Exam types\n']+[f'- **{k}** {v}' for k,v in DESC.items() if k[0]==('T' if skill=='channel-structure' else 'A')]+['']
    for it,a,s in rows:
        T=it['type']; E.append(f'\n### Exam {it["id"]} — {T} · `{it["video"]}` ({it["group"]})\n')
        if T in('T1','T2'): E.append(f'**Prompt.** Line: "{it["prompt_text"]}"'+(f' (at {it["pct"]}%)' if T=='T1' else '')+('\nOptions: '+' / '.join(mod.LABELS) if T=='T1' else '\nEstimate % of runtime.'))
        elif T in('T3','A2','A4','A5'): E.append('**Prompt.** Options:\n'+'\n'.join(f'{chr(65+i)}. "{o}"' for i,o in enumerate(it['options'])))
        elif T=='T4': E.append(f'**Prompt.** {json.dumps(it["facts"])} → give hook-end %, first sponsor %, conclusion %, turns.')
        elif T=='T5': E.append(f'**Prompt.** Profile {json.dumps(it["profile"])}')
        elif T=='T6': E.append('**Prompt.** Order these:\n'+'\n'.join(f'{i}. "{o}"' for i,o in enumerate(it['shuffled'])))
        elif T=='A1': E.append(f'**Prompt.** "{it["text"]}"\nOptions: '+' / '.join(f'{chr(65+i)}. {o}' for i,o in enumerate(it['options'])))
        elif T=='A3': E.append(f'**Prompt.** "{it["text"]}"')
        g=it['gold']
        gs={'T1':g,'T2':f'{g}%','T3':chr(65+g) if isinstance(g,int) else g,'A1':(f'{chr(65+g)} ({it.get("gold_name")}; surface "{it.get("match")}")' if T=='A1' else ''),'A2':chr(65+g) if isinstance(g,int) else g,'A4':chr(65+g) if isinstance(g,int) else g,'A5':chr(65+g) if isinstance(g,int) else g}.get(T,json.dumps(g))
        ans=chr(65+a) if isinstance(a,int) and T in('T3','A1','A2','A4','A5') else json.dumps(a)
        rub={'T2':'1.0 if |Δ|≤10, 0.5 if ≤20, else 0','T4':'1 pt each: hook ±3, sponsor ±10 (or both none), conclusion ±8, turns ±2','T6':'pairwise order accuracy'}.get(T,'1 if exact, else 0')
        E.append(f'\n**Gold.** {gs}\n\n**Rubric.** {rub}\n\n**Taken answer.** {ans} → **score {s}**')
    open(f'{D}/exams.md','w').write('\n'.join(E))
    sc=[r[2] for r in rows]; bl=[round(sum(sc[i:i+10])/10,2) for i in range(0,100,10)]
    bt=defaultdict(list)
    for it,a,s in rows: bt[it['type']].append(s)
    L=[f'# Exam log — {skill}\n','## Honest note on who took these\nThe exams were taken by a **codified solver** (`build/{}.py`, class `Solver`) that executes this skill\'s checklist rules as written at v1, not by a free-form model reading. After every 10 exams its misses were folded back: cue lists, position priors, mode templates, feature weights. The same lessons were written into `SKILL.md` ("Lessons from the exams") and `training/lessons-learned.md`. Gold answers come from the real transcripts and detector beat maps, so the remaining error is partly the solver\'s and partly detector noise.\n'.format(modname),
       f'## Curve\n\nBlock averages (10 exams each): {bl}\n\n- Early (exams 1-50): **{round(sum(sc[:50])/50,3)}**\n- Late (exams 51-100): **{round(sum(sc[50:])/50,3)}**\n- First 20: {round(sum(sc[:20])/20,3)} · Last 20: {round(sum(sc[80:])/20,3)}\n- Overall: {round(sum(sc)/100,3)}\n',
       '## By type\n\n| type | n | mean | first half | second half |\n|---|---|---|---|---|']
    for k,v in sorted(bt.items()):
        h=len(v)//2; L.append(f'| {k} | {len(v)} | {round(sum(v)/len(v),2)} | {round(sum(v[:h])/max(h,1),2)} | {round(sum(v[h:])/max(len(v)-h,1),2)} |')
    L.append('\n## Fold-backs (every 10 exams)\n')
    for end,avg,les in log:
        L.append(f'### After exam {end} — block average {round(avg,2)}\n'+('\n'.join('- '+x for x in les) if les else '- No misses to fold.')+'\n')
    open(f'{D}/exam-log.md','w').write('\n'.join(L))
    return bl,sc,log,bt
if __name__=='__main__':
    for m,sk,t in [('exam_structure','channel-structure','Channel structure'),('exam_audience','channel-audience','Channel audience')]:
        bl,sc,log,bt=run(m,sk,t); print(sk,bl,round(sum(sc[:50])/50,3),round(sum(sc[50:])/50,3),{k:round(sum(v)/len(v),2) for k,v in bt.items()})
