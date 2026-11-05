import os
import re,random,json,statistics as st,collections,corpus,pool
TELLS=re.compile(r"\b(?:delve|tapestry|testament|landscape|crucial|pivotal|robust|leverage|seamless|multifaceted|intricate|realm|underscore[sd]?|showcase|foster|vibrant|navigate|ever-evolving|moreover|furthermore|additionally|consequently|nevertheless|in conclusion|notably|ultimately|it is important to note|interplay|far-reaching|serves as|highlights|significant|numerous|utilize|obtain|individuals?|commence|facilitate|demonstrates?|approximately|unprecedented|considerable|substantial|cost-effective|therefore|however|indeed|currently|as a result)\b",re.I)
FILLERS=re.compile(r"\b(?:just|really|actually|basically|literally|kind of|sort of|you know|i mean|honestly|probably|pretty|like,)\b",re.I)
CONTR=re.compile(r"\b\w+'(?:s|re|ve|ll|d|t|m)\b")
def W(t): return re.findall(r"[a-z0-9']+",t.lower())
def sd(t):
    l=[len(s.split()) for s in corpus.sents(t)]; return st.pstdev(l) if len(l)>1 else 0
def f1(a,b):
    A=collections.Counter(W(a));B=collections.Counter(W(b));o=sum((A&B).values())
    return 0 if not o else 2*o/(sum(A.values())+sum(B.values()))

def do_fold(rows,k,pairs,fold,LES):
    added=[];notes=[]
    for ty,(F,Cands) in pairs.items():
        past=[r for r in rows if r['type']==ty]
        if not past: continue
        base=sum(r['_ev'](F) for r in past)
        best=None;bg=0
        for c in Cands:
            if c in F: continue
            g=sum(r['_ev'](F+[c]) for r in past)-base
            if g>bg+1e-9: best,bg=c,g
            elif g<0: notes.append(f"tried {c} on type {ty}: rejected (would lose {-g:.2f} on {len(past)} past items)")
        if best: F.append(best);added.append(best);fold.apply(k,LES[best]+f" [validated: +{bg:.2f} on {len(past)} past type-{ty} items]")
    return added,notes
class Fold:
    def __init__(s,skill,lessons,targets): s.skill=skill;s.lessons=lessons;s.targets=targets;s.log=[]
    def apply(s,k,text):
        s.log.append((k,text))
        for path,section in s.targets:
            body=open(path).read()
            if section not in body: body+=f"\n\n{section}\n"
            body=body.replace(section,section+f"\n- (fold {k}) {text}",1)
            open(path,'w').write(body)
def run_lang(P,rng,fold,N=100):
    feats_A=['tells'];FA=['contr','fill','burst','semi','opener']
    feats_B=['global'];FB=['group','prevq','bigram']
    tr_C=['detell'];TC=['openers','contract','split','casual','hedge']
    LES={'contr':'Real lines are dense with contractions (it\'s, that\'s, don\'t). Expanded forms ("it is", "do not") are the single most reliable subtle AI tell. Re-contract everything except deliberate emphasis.',
      'fill':'Real narration keeps fillers (just, actually, really, kind of, I mean). A passage with zero fillers over 60+ words is almost always the AI version. Keep about 1 per 2-3 sentences.',
      'burst':'Human passages have high sentence-length spread (corpus SD 10.2). AI rewrites merge fragments into even 18-25-word sentences. Keep 3-6-word punches beside 30-word run-ons.',
      'semi':'Semicolons and ", and it is" splices are machine merges. Corpus host speech has close to zero semicolons. Split into separate sentences.',
      'opener':'Spoken openers (And/But/So) begin about 28% of weighted sentences (Gen about 49%, Adam about 15%). A passage with none is suspicious.',
      'group':'The opener depends on the lean: Gen favors So/And/But/Because, Adam favors It/The/We/This, oil favors And/This/Okay. Use the lean table before the global prior.',
      'prevq':'After a rhetorical question the next opener is usually Because/So/Well (Gen) or a flat answer starting It/The (Adam). Read the previous sentence before choosing.',
      'bigram':'The word right after the opener decides it: "So what/now/if", "But what/here\'s/the", "And then/so/that\'s", "Because if/the". Check the following word.',
      'openers':'Humanizer step: map essay openers back to spoken ones. Therefore/As a result -> So, However -> But, Additionally/Moreover -> And, For example -> Like, Currently -> Now.',
      'contract':'Humanizer step: re-contract (it is -> it\'s, do not -> don\'t, I am -> I\'m) everywhere.',
      'split':'Humanizer step: break semicolon and ", and" merges back into separate sentences so short punches come back.',
      'casual':'Humanizer step: swap formal vocabulary back to plain words (utilize->use, obtain->get, significant->big, numerous->a lot of, individuals->people, approximately->about, purchase->buy).',
      'hedge':'Humanizer step: put back one spoken hedge per 3 sentences (just / actually / kind of / I think). Real host lines are never hedge-free.'}
    def scoreA(t,fe):
        n=max(1,len(corpus.sents(t)));v=0
        if 'tells' in fe: v-=3*len(TELLS.findall(t))
        if 'contr' in fe: v+=2*len(CONTR.findall(t))/n - 2*len(re.findall(r"\b(?:it is|do not|that is|I am|does not|did not|cannot|there is|they are|you are|we are)\b",t))/n
        if 'fill' in fe: v+=len(FILLERS.findall(t))/n
        if 'burst' in fe: v+=sd(t)/6
        if 'semi' in fe: v-=2*t.count(';')-1.5*len(re.findall(r", and (?:it|this|that|there|they|we|he|she) ",t))
        if 'opener' in fe: v+=2*sum(1 for s in corpus.sents(t) if re.match(r"(?:And|But|So)\b",s))/n
        return v
    docs=pool.docs
    OPS=['So','And','But','Now','Because','Like','Well','Okay','The','It','This','I','We','You']
    glob=collections.Counter();grp=collections.defaultdict(collections.Counter);big=collections.defaultdict(collections.Counter);pq=collections.Counter()
    def build(excl):
        g0=collections.Counter();gr=collections.defaultdict(collections.Counter);bg=collections.defaultdict(collections.Counter);q=collections.Counter()
        for d in docs:
            if d['file']==excl: continue
            prev=''
            for s in d['sents']:
                m=s.split()
                if m and m[0].rstrip(',') in OPS:
                    o=m[0].rstrip(',');g0[o]+=d['w'];gr[d['group']][o]+=1
                    if len(m)>1: bg[(m[1].lower().strip(','))][o]+=1
                    if prev.endswith('?'): q[o]+=1
                prev=s
        return g0,gr,bg,q
    cache={}
    def solveB(item,fe):
        if item['file'] not in cache: cache[item['file']]=build(item['file'])
        g0,gr,bg,q=cache[item['file']]
        sc={}
        for o in item['options']:
            v=g0[o]/sum(g0.values())
            if 'group' in fe: v=gr[item['group']][o]/max(1,sum(gr[item['group']].values()))
            if 'prevq' in fe and item['prev'].endswith('?'): v+=0.5*q[o]/max(1,sum(q.values()))
            if 'bigram' in fe and item['next'] in bg: v+=1.0*bg[item['next']][o]/max(1,sum(bg[item['next']].values()))
            sc[o]=v
        return max(sc,key=sc.get)
    CAS={'utilize':'use','obtain':'get','obtains':'gets','significant':'big','substantial':'big','considerable':'big','numerous':'a lot of','a significant amount of':'a lot of','individuals':'people','individual':'guy','commence':'start','purchase':'buy','approximately':'about','demonstrate':'show','demonstrates':'shows','facilitate':'help','remarkable':'crazy','unprecedented':'crazy','extraordinary':'insane','notable':'wild','materials':'stuff','children':'kids','capital':'money','cost-effective':'cheap','require':'need'}
    UNC={v.lower():k for k,v in pool.CONTR.items() if "'" in k}
    def humanize(t,tr,group):
        if 'detell' in tr:
            for c in pool.CLOSERS: t=t.replace(c,'')
            t=re.sub(r"\b(?:Moreover|Furthermore|Additionally|Consequently|Nevertheless|Indeed|Notably|Currently|Therefore|However|As a result|For example|This is because),\s*","",t)
        if 'openers' in tr:
            pass
        t=t.strip()
        return t
    def humanize2(t0,tr,group):
        t=t0
        for c in pool.CLOSERS: t=t.replace(c,'')
        if 'openers' in tr:
            for a,b in [('Therefore,','So'),('Consequently,','So'),('As a result,','So'),('Additionally,','And'),('Furthermore,','And'),('Moreover,','And'),('However,','But'),('Nevertheless,','But'),('Currently,','Now'),('This is because','Because'),('For example,','Like'),('Indeed,','Well'),('Notably,','Okay')]:
                t=t.replace(a+' ',b+' ')
            t=re.sub(r"(?<=[.?!] )(So|And|But|Now|Because|Like|Well|Okay) ([A-Z])(?![A-Z])",lambda m:m.group(1)+' '+(m.group(2).lower() if m.group(2) not in 'I' else m.group(2)),t)
        elif 'detell' in tr:
            t=re.sub(r"\b(?:Moreover|Furthermore|Additionally|Consequently|Nevertheless|Indeed|Notably|Currently|Therefore|However|As a result|For example),\s*","",t)
        if 'contract' in tr:
            for k,v in UNC.items(): t=re.sub(r'\b'+re.escape(k)+r'\b',lambda m,k=k,v=v:(v[0].upper()+v[1:]) if m.group(0)[0].isupper() else v,t,flags=re.I)
        if 'split' in tr:
            t=re.sub(r';\s*(\w)',lambda m:'. '+m.group(1).upper(),t)
            t=re.sub(r', and (it|this|that|there|they|we|he|she|i) ',lambda m:'. '+m.group(1).capitalize()+' ',t)
        if 'casual' in tr:
            for k,v in CAS.items(): t=re.sub(r'\b'+re.escape(k)+r'\b',lambda m,v=v:(v[0].upper()+v[1:]) if m.group(0)[0].isupper() else v,t)
        if 'hedge' in tr:
            ss=corpus.sents(t)
            for i in range(1,len(ss),3):
                ss[i]=re.sub(r'\b(is|was|are) ',r'\1 actually ' if group in('gen','oil') else r'\1 just ',ss[i],count=1)
            t=' '.join(ss)
        t=re.sub(r'\s+',' ',t).strip()
        return t
    def scoreC(out,gold):
        tellfree=1/(1+len(TELLS.findall(out)))
        fp=1-min(1,abs(len(CONTR.findall(out))-len(CONTR.findall(gold)))/max(3,len(CONTR.findall(gold))))*0.5-min(1,abs(sd(out)-sd(gold))/10)*0.5
        return round(0.35*tellfree+0.35*f1(out,gold)+0.30*fp,3)
    PAIRS={'A':(feats_A,FA),'B':(feats_B,FB),'C':(tr_C,TC)}
    items=pool.sample_by_weight(P,N,rng)
    types=(['A']*40+['B']*30+['C']*30);rng.shuffle(types)
    rows=[];bank=[]
    for k,(p,ty) in enumerate(zip(items,types),1):
        rec={'n':k,'type':ty,'group':p['group'],'file':p['file'],'weight':p['w']}
        if ty=='A':
            opts=[p['text'],pool.aiify(p['text'],rng,'heavy'),pool.aiify(p['text'],rng,'subtle')]
            idx=[0,1,2];rng.shuffle(idx);O=[opts[i] for i in idx];gold='ABC'[idx.index(0)]
            ans='ABC'[max(range(3),key=lambda i:scoreA(O[i],feats_A))]
            rec['_ev']=lambda fe,O=O,gold=gold:float('ABC'[max(range(3),key=lambda i:scoreA(O[i],fe))]==gold)
            ok=ans==gold;rec.update(prompt='Which version is the real host line? A) '+O[0]+'\nB) '+O[1]+'\nC) '+O[2],gold=gold,answer=ans,score=1.0 if ok else 0.0)
            if not ok:
                for f in FA:
                    if f not in feats_A and 'ABC'[max(range(3),key=lambda i:scoreA(O[i],feats_A+[f]))]==gold: rec['miss']=f;break
                else: rec['miss']='subtle-variant tie'
        elif ty=='B':
            cands=[(i,s) for i,s in enumerate(p['sents']) if s.split()[0].rstrip(',') in OPS and i>0]
            if not cands: cands=[(i,s) for i,s in enumerate(p['sents']) if s.split()[0].rstrip(',') in OPS] or [(0,'So '+p['sents'][0])]
            i,s=rng.choice(cands);tw=s.split()[0].rstrip(',')
            opts=[tw]+rng.sample([o for o in OPS if o!=tw],3);rng.shuffle(opts)
            item={'file':p['file'],'group':p['group'],'options':opts,'prev':p['sents'][i-1] if i>0 else '','next':(s.split()[1].lower().strip(',') if len(s.split())>1 else '')}
            masked=' '.join(p['sents'][:i]+['____ '+s.split(' ',1)[1] if ' ' in s else '____']+p['sents'][i+1:])
            ans=solveB(item,feats_B);ok=ans==tw
            rec['_ev']=lambda fe,item=item,tw=tw:float(solveB(item,fe)==tw)
            rec.update(prompt=f'[{p["group"]}-lean] Fill the blank opener. Options: {", ".join(opts)}\n{masked}',gold=tw,answer=ans,score=1.0 if ok else 0.0)
            if not ok:
                for f in FB:
                    if f not in feats_B and solveB(item,feats_B+[f])==tw: rec['miss']=f;break
                else: rec['miss']='no-rule-fixes'
        else:
            ai=pool.aiify(p['text'],rng,'heavy');out=humanize2(ai,tr_C,p['group']);sc=scoreC(out,p['text'])
            rec['_ev']=lambda fe,ai=ai,g=p['group'],gold=p['text']:scoreC(humanize2(ai,fe,g),gold)
            rec.update(prompt=f'[{p["group"]}-lean] Humanize into channel voice:\n{ai}',gold=p['text'],answer=out,score=sc)
            if sc<0.85:
                best=None;bs=sc
                for f in TC:
                    if f in tr_C: continue
                    s2=scoreC(humanize2(ai,tr_C+[f],p['group']),p['text'])
                    if s2>bs+0.005: best,bs=f,s2
                rec['miss']=best or 'residual (lost fillers/wording cannot be recovered)'
        rec['rules']='|'.join(feats_A+feats_B+tr_C)
        rows.append(rec);bank.append(rec)
        if k%10==0:
            added,notes=do_fold(rows,k,PAIRS,fold,LES)
            rec['fold']=(added or ['no rule passed validation'])+notes[:3]
    return rows
import json as _j,math as _m
_ST=_j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','v1-build','stats.json')))['story']
_CR=[(re.compile(c['rx']),_m.log((c['pct_first10']+2)/12),_m.log((c['pct_last10']+2)/12)) for c in _ST if c['pos'] is None and c['files_with']>=5]
def nb(t):
    o=c=0.
    for s in corpus.sents(t):
        l=s.lower()
        for rx,a,b in _CR:
            if rx.search(l): o+=a;c+=b
    return o,c
def run_story(P,rng,fold,N=100):
    LES={'backref':'Real cold opens never lean on earlier context: no "he/they/that/also/again" openers without an antecedent. If a line needs a previous sentence, it is mid-video.',
      'q':'Real cold opens often end on the central question ("then what the hell happens to the economy now?"). A question in the first 2 sentences raises the open score.',
      'you':'Cold opens address the viewer or the viewer\'s assumption early ("Do you remember...", "you might think"). Second person in line 1-2 is an open signal.',
      'event':'Cold opens drop into an event in motion ("One guy just used AI...", "For 16 hours on Tuesday, July 8th..."): just / began / had what / a date. Weight in-medias-res verbs.',
      'hooknum':'Number-first openings ("90% of the stuff headed to space...") are a strong open signal across Especially and After corpora.',
      'close_cta':'Close sections carry sign-offs and forward projections (will, next, future, thanks, let me know). Weight them for placement.',
      'open_promise':'Opening sections carry promise/story frames ("this is the story of", "what no one is talking about", "I want to tell you").',
      'callback':'Callbacks ("remember", "like I said", "back to", "that\'s why") belong to the middle and late sections, never the open.',
      'density':'Middle sections are where mechanism language lives (which means, because, in other words, percent and dollar figures). Dense numbers point to the middle.',
      'entity':'The true next beat keeps the same named entities (capitalized names, products, places) as the passage. Weight entity overlap over plain word overlap.',
      'number':'Continuations keep the number thread: if the passage ends on a figure, the next beat compares or consequences it.',
      'pronoun':'The next beat often opens with a pronoun or connector (It/That/This/And/But/So) that points back. A candidate that restarts with a new full subject is often from elsewhere.',
      'nb':'Use the placement table in criteria.md: each criterion has a first-10% and last-10% share. Sum them over a passage (a naive-Bayes vote) to judge whether it reads as an open, a middle, or a close. Hook and stakes moves pull toward the open. Callbacks, projections, and sign-offs pull toward the close.',
      'qa':'If the passage ends on a question, the true next line answers it (Because/So/Well/The answer/It\'s).'}
    O_F=['backref'];O_C=['q','you','event','hooknum','nb']
    P_F=['base'];P_C=['close_cta','open_promise','callback','density','nb']
    N_F=['overlap'];N_C=['entity','number','pronoun','qa']
    def sOpen(t,fe):
        l=t.lower();v=0
        if 'backref' in fe: v-=2*bool(re.match(r"(he|she|they|it|that|this|also|again|these|those|and|but|so)\b",l)) + 2*bool(re.search(r"\b(again|also|like i said|remember|as i mentioned|back to)\b",l))
        if 'q' in fe: v+=1.5*('?' in t)
        if 'you' in fe: v+=1.0*bool(re.search(r"\b(you|your)\b",l))
        if 'event' in fe: v+=1.0*bool(re.search(r"\b(just|began|had what|on (?:mon|tues|wednes|thurs|fri|satur|sun)day|hours|one guy|this is)\b",l))
        if 'hooknum' in fe: v+=1.0*bool(re.match(r"[\"']?\$?\d",t))
        if 'nb' in fe: v+=0.5*nb(t)[0]
        return v
    def sPlace(t,fe):
        l=t.lower();sc={'open':0.,'middle':0.5,'close':0.}
        if re.search(r"\b(thanks for watching|thank you for|subscribe|see you|let me know in)\b",l): sc['close']+=2
        if re.search(r"\b(this is the story|in this video|today we|what no one|i want to tell you)\b",l): sc['open']+=2
        if 'close_cta' in fe: sc['close']+=0.4*len(re.findall(r"\b(will|future|next|going to|in the end|ultimately|hope|question is)\b",l))
        if 'open_promise' in fe: sc['open']+=0.6*len(re.findall(r"\b(story|imagine|you might|you probably|first thought|what if|why|how)\b",l))
        if 'callback' in fe: sc['open']-=1.0*len(re.findall(r"\b(remember|like i said|back to|that's why|again|earlier)\b",l)); sc['middle']+=0.3
        if 'density' in fe: sc['middle']+=0.25*len(re.findall(r"\b(which means|because|in other words|percent|\d)\b",l))
        if 'nb' in fe:
            o,c=nb(t);sc['open']+=0.5*o+0.3;sc['close']+=0.5*c+0.3
        return max(sc,key=sc.get)
    def ents(t): return set(re.findall(r"(?<![.?!] )\b[A-Z][a-zA-Z]{2,}",t))-{'The','And','But','So','This','That','It','They','He','She','We','You','In','On','Now','What','I','If','There','Because','When','Like','Well','Okay'}
    def sNext(ctx,c,fe):
        v=f1(ctx,c)
        if 'entity' in fe: v+=0.15*len(ents(ctx)&ents(c))
        if 'number' in fe and re.search(r"\d",ctx[-80:]): v+=0.1*bool(re.search(r"\d|that's|which",c.lower()))
        if 'pronoun' in fe: v+=0.08*bool(re.match(r"(It|That|This|They|He|She|And|But|So|Which)\b",c))
        if 'qa' in fe and ctx.rstrip().endswith('?'): v+=0.2*bool(re.match(r"(Because|So|Well|The answer|It's|It|Yes|No)\b",c))
        return v
    PAIRS={'A':(O_F,O_C),'B':(P_F,P_C),'C':(N_F,N_C)}
    items=pool.sample_by_weight(P,N,rng)
    types=['A']*35+['B']*35+['C']*30;rng.shuffle(types)
    docs=pool.docs;rows=[]
    bydoc=collections.defaultdict(list)
    for p in P: bydoc[p['file']].append(p)
    for k,(p,ty) in enumerate(zip(items,types),1):
        d=p['doc'];rec={'n':k,'type':ty,'group':p['group'],'file':p['file'],'weight':p['w']}
        if ty=='A':
            real=' '.join(d['sents'][:2])
            others=[x for x in P if x['file']!=p['file'] and 0.2<x['pos']<0.8]
            dist=[' '.join(x['sents'][:2]) for x in rng.sample(others,3)]
            opts=[real]+dist;idx=list(range(4));rng.shuffle(idx);Oo=[opts[i] for i in idx];gold='ABCD'[idx.index(0)]
            f=lambda fe,Oo=Oo:'ABCD'[max(range(4),key=lambda i:(sOpen(Oo[i],fe),-i))]
            ans=f(O_F);ok=ans==gold;rec['_ev']=lambda fe,f=f,gold=gold:float(f(fe)==gold)
            rec.update(prompt='Which is the real cold open (first two sentences of a video)?\n'+'\n'.join(f"{'ABCD'[i]}) {Oo[i]}" for i in range(4)),gold=gold,answer=ans,score=float(ok))
            if not ok: rec['miss']=next((x for x in O_C if x not in O_F and f(O_F+[x])==gold),'no-rule-fixes')
        elif ty=='B':
            want=['open','middle','close'][k%3]
            cand=[x for x in bydoc[p['file']] if (x['pos']<0.12 if want=='open' else x['pos']>0.85 if want=='close' else 0.3<x['pos']<0.7)] or [p]
            x=rng.choice(cand);gold='open' if x['pos']<0.12 else 'close' if x['pos']>0.85 else 'middle'
            ans=sPlace(x['text'],P_F);ok=ans==gold;rec['_ev']=lambda fe,t=x['text'],gold=gold:float(sPlace(t,fe)==gold)
            rec.update(prompt=f'Where in the video does this passage sit (open / middle / close)?\n{x["text"]}',gold=gold,answer=ans,score=float(ok),file=x['file'])
            if not ok: rec['miss']=next((c for c in P_C if c not in P_F and sPlace(x['text'],P_F+[c])==gold),'no-rule-fixes')
        else:
            if p['j']>=len(d['sents'])-2: p=next(x for x in bydoc[p['file']] if x['j']<len(d['sents'])-2)
            nxt=d['sents'][p['j']]
            same=[x for x in P if x['group']==p['group'] and x['file']!=p['file']] or [x for x in P if x['file']!=p['file']]
            dist=[rng.choice(same)['sents'][0] for _ in range(2)]
            opts=[nxt]+dist;idx=[0,1,2];rng.shuffle(idx);Oo=[opts[i] for i in idx];gold='ABC'[idx.index(0)]
            f=lambda fe,Oo=Oo,ctx=p['text']:'ABC'[max(range(3),key=lambda i:sNext(ctx,Oo[i],fe))]
            ans=f(N_F);ok=ans==gold;rec['_ev']=lambda fe,f=f,gold=gold:float(f(fe)==gold)
            rec.update(prompt=f'Pick the real next beat.\nPASSAGE: {p["text"]}\n'+'\n'.join(f"{'ABC'[i]}) {Oo[i]}" for i in range(3)),gold=gold,answer=ans,score=float(ok))
            if not ok: rec['miss']=next((c for c in N_C if c not in N_F and f(N_F+[c])==gold),'no-rule-fixes')
        rec['rules']='|'.join(O_F+P_F+N_F)
        rows.append(rec)
        if k%10==0:
            added,notes=do_fold(rows,k,PAIRS,fold,LES)
            rec['fold']=(added or ['no rule passed validation'])+notes[:3]
    return rows
