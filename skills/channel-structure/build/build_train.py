import os
import json, random, stats, exam_structure as ES, exam_audience as EA
from corpus import fmt
W=os.environ.get('CHANNEL_SKILLS_DIR',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
def L(x): return chr(65+x)
def mk(skill,mod,plan):
    D=f'{W}/{skill}/training'; keys=['# Answer keys (all levels)\n','Gold comes from the real transcripts (host-only) and the detector beat maps in `references/beat-maps.md`. Do the drill first; only then open this file.\n']
    for lvl,fname,title,types,n,seed in plan:
        items=[it for it in mod.gen_items(400,seed) if it['type'] in types][:n]
        o=[f'# {title}\n',f'Level {lvl}. {n} items. Answer on paper/in a scratch file **before** opening `answer-keys.md#{fname.lower()}`. Score with `rubric.md`; record misses in `lessons-learned.md`.\n']
        keys.append(f'\n## {fname}\n')
        for k,it in enumerate(items,1):
            T=it['type']; o.append(f'\n**{fname}.{k}** ({T}, `{it["video"]}`)')
            if T in('T1',): o.append(f'Line at {it["pct"]}%: "{it["prompt_text"]}" — label it ({" / ".join(ES.LABELS)}).'); g=it['gold']
            elif T=='T2': o.append(f'Where (%) does this sit? "{it["prompt_text"]}"'); g=f'{it["gold"]}% ({it["beat"]})'
            elif T in('T3','A2','A4','A5'):
                q={'T3':'Which is the real first line of the video?','A2':'Which line is from the hook (first 8%)?','A4':'Which passage is from the close (88-98%)?','A5':'Which line is the real (un-flattened) one?'}[T]
                o.append(q+'\n'+'\n'.join(f'  {L(i)}. "{x}"' for i,x in enumerate(it['options']))); g=L(it['gold'])
            elif T=='T4': o.append(f'Reconstruct the outline: {json.dumps(it["facts"])}. Give hook-end %, sponsor %, conclusion %, # turns, then compare with the gold map for `{it["video"]}` in beat-maps.md.'); g=json.dumps(it['gold'])
            elif T=='T5': o.append(f'Which mode? profile {json.dumps(it["profile"])}'); g=it['gold']
            elif T=='T6': o.append('Put in runtime order:\n'+'\n'.join(f'  {i}. "{x}"' for i,x in enumerate(it['shuffled']))); g=' → '.join(map(str,it['gold']))+f'  (positions of listed lines: {it["gold_pcts"]})'
            elif T=='A1': o.append(f'"{it["text"]}"\n'+'\n'.join(f'  {L(i)}. {x}' for i,x in enumerate(it['options']))); g=f'{L(it["gold"])} — {it["gold_name"]} (surface: "{it["match"]}")'
            elif T=='A3': o.append(f'Who wrote this (Adam / Gen / Mechanism / Others)?\n> {it["text"]}'); g=it['gold']
            keys.append(f'- {fname}.{k}: **{g}**')
        open(f'{D}/{fname}.md','w').write('\n'.join(o))
    open(f'{D}/answer-keys.md','w').write('\n'.join(keys))
mk('channel-structure',ES,[(1,'L1-recognition','Beat recognition',{'T1'},30,101),(2,'L2-position','Beat position estimation',{'T2','T6'},24,202),(3,'L3-discrimination','Openers & mode discrimination',{'T3','T5'},24,303),(4,'L4-reconstruction','Outline reconstruction vs gold beat maps',{'T4'},12,404)])
mk('channel-audience',EA,[(1,'L1-recognition','Device spotting',{'A1'},30,101),(2,'L2-placement','Hook vs middle / close vs middle',{'A2','A4'},24,202),(3,'L3-discrimination','Real vs flattened, creator attribution',{'A5','A3'},24,303)])
