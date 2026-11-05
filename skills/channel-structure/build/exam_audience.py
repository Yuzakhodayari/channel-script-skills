import random, re, json
import stats, crit_audience as CA
from stats import short
from examlib import wpick, mode
RX=[c for c in CA.C if c['kind']=='rx']
for c in RX: c['re']=re.compile(c['spec'][0],re.I)
FEAR=r"\b(die|dead|death|collapse|crisis|catastroph|danger|threat|risk|lose|lost|kill|extinct|disaster|scary|terrif|crash|broke|debt|fail)"
HOPE=r"\b(hope|can|could|better|future|choose|choice|build|fix|solution|chance|still|together|matter|power)\b"
def feats(t):
    w=max(len(t.split()),1)
    return dict(you=len(re.findall(r"\byou",t,re.I))/w*100, i=len(re.findall(r"\b(I|I'm|I've|my|me)\b",t))/w*100,
        q=t.count('?')/w*100, num=len(re.findall(r"\d",t))/w*100, fear=len(re.findall(FEAR,t,re.I))/w*100,
        hope=len(re.findall(HOPE,t,re.I))/w*100, so=len(re.findall(r"(^|[.?!]\s)(So|And|But)\b",t))/w*100,
        sl=w/max(len(re.findall(r'[.?!]',t)),1), prof=len(re.findall(r"\b(hell|damn|shit|fuck|crap|ass)\w*",t,re.I))/w*100)
def _head(rx):
    # headline surface form = first top-level alternative (what device-catalog.md lists first)
    depth=0
    for i,ch in enumerate(rx):
        if ch=='(' : depth+=1
        elif ch==')': depth-=1
        elif ch=='|' and depth==0: return rx[:i]
    return rx
class Solver:
    def __init__(s):
        s.cue={c['name']:[re.compile(_head(c['spec'][0]),re.I)] for c in RX}
        s.hw=dict(you=0.3,q=0.3,num=0.3,fear=0.3,hope=0,i=0,so=-0.2,sl=0,prof=0)
        s.cw=dict(you=0,q=0,num=0,fear=-0.3,hope=0.3,i=0.2,so=0,sl=0,prof=0)
        s.cent={'Adam':dict(you=1.0,i=2.0,sl=16,q=0.4,prof=0.05),'Gen':dict(you=3.0,i=2.0,sl=14,q=0.8,prof=0.2),'Mechanism':dict(you=2.0,i=1.5,sl=15,q=0.6,prof=0.1),'Others':dict(you=2.0,i=3.0,sl=13,q=0.6,prof=0.1)}
        s.realw=dict(you=0.5,q=0.5,so=0.3,num=0.2,fear=0.1,hope=0.1,i=0.1,sl=0,prof=0.1)
    def spot(s,t,opts):
        sc=[sum(1 for k in s.cue[o] if k.search(t)) for o in opts]; return sc.index(max(sc))
    def lin(s,w,t): f=feats(t); return sum(w[k]*f[k] for k in w)
    def attr(s,t):
        f=feats(t)
        def d(c): return sum(abs(f[k]-c[k])/(1 if k!='sl' else 4) for k in c)
        return min(s.cent,key=lambda k:d(s.cent[k]))
def flatten(t):
    u=re.sub(r"\byou're\b","people are",t,flags=re.I); u=re.sub(r"\byour\b","their",u,flags=re.I); u=re.sub(r"\byou\b","people",u,flags=re.I)
    u=re.sub(r"^(So|And|But|Now),?\s+","",u); u=u.replace('?','.'); u=re.sub(r"\b(literally|actually|really|just)\s+","",u)
    return u[0].upper()+u[1:] if u else u
def gen_items(n=100,seed=11):
    rng=random.Random(seed); vs=stats.vids(); items=[]
    for k in range(n):
        T=['A1','A2','A3','A4','A5'][k%5]
        for _ in range(50):
            v=wpick(rng,vs); S=v['sents']
            if T=='A1':
                c=rng.choice(RX); hits=[x for x in S if c['re'].search(x['text']) and 5<=len(x['text'].split())<=40]
                if not hits: continue
                x=rng.choice(hits); ds=[d for d in RX if not d['re'].search(x['text']) and d['cat']!=c['cat']]
                opts=[c['name']]+[d['name'] for d in rng.sample(ds,3)]; rng.shuffle(opts)
                items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],text=short(x['text'],45),options=opts,gold=opts.index(c['name']),gold_name=c['name'],match=c['re'].search(x['text']).group(0))); break
            if T=='A2':
                h=[x for x in S if x['pct']<=8 and 6<=len(x['text'].split())<=35]; m=[x for x in S if 30<=x['pct']<=70 and 6<=len(x['text'].split())<=35]
                if not h or len(m)<3: continue
                g=rng.choice(h); opts=[g]+rng.sample(m,3); rng.shuffle(opts)
                items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],options=[short(o['text'],40) for o in opts],gold=opts.index(g))); break
            if T=='A3':
                i=rng.randrange(int(len(S)*0.15),int(len(S)*0.8)); seg=[]; j=i
                while j<len(S) and sum(len(x['text'].split()) for x in seg)<130: seg.append(S[j]); j+=1
                items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],text=' '.join(x['text'] for x in seg),gold=mode(v))); break
            if T=='A4':
                close=[i for i,x in enumerate(S) if x['pct']>=88 and x['pct']<=98]; mid=[i for i,x in enumerate(S) if 40<=x['pct']<=60]
                if len(close)<4 or len(mid)<4: continue
                a=rng.choice(close[:-3]); b=rng.choice(mid[:-3]); P=[' '.join(S[q]['text'] for q in range(a,a+3)),' '.join(S[q]['text'] for q in range(b,b+3))]
                order=[0,1]; rng.shuffle(order)
                items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],options=[short(P[o],70) for o in order],gold=order.index(0))); break
            if T=='A5':
                c=[x for x in S if 8<=len(x['text'].split())<=35 and flatten(x['text'])!=x['text']]
                if not c: continue
                x=rng.choice(c); opts=[x['text'],flatten(x['text'])]; o=[0,1]; rng.shuffle(o)
                items.append(dict(id=k+1,type=T,video=v['key'],group=v['group'],options=[opts[q] for q in o],gold=o.index(0))); break
    return items
def answer(sol,it):
    T=it['type']
    if T=='A1': return sol.spot(it['text'],it['options'])
    if T=='A2': sc=[sol.lin(sol.hw,o) for o in it['options']]; return sc.index(max(sc))
    if T=='A3': return sol.attr(it['text'])
    if T=='A4': sc=[sol.lin(sol.cw,o) for o in it['options']]; return sc.index(max(sc))
    if T=='A5': sc=[sol.lin(sol.realw,o) for o in it['options']]; return sc.index(max(sc))
def score(it,a): return 1.0 if a==it['gold'] else 0.0
def _perc(w,good,bad,lr=0.6):
    fg,fb=feats(good),feats(bad)
    for k in w: w[k]=round(w[k]+lr*(fg[k]-fb[k])/max(1,abs(fg[k])+abs(fb[k])),3)
def fold(sol,_,block):
    les=[]
    for it,a,s in block:
        T=it['type']
        if T=='A1' and s<1:
            m=it['match'].lower().strip()
            if m: sol.cue[it['gold_name']].append(re.compile(r'\b'+re.escape(m)+r'\b',re.I))
            les.append(f'Exam {it["id"]}: missed "{it["gold_name"]}"; learned its surface form "{it["match"]}".')
        if T in('A2','A4','A5') and s<1:
            w={'A2':sol.hw,'A4':sol.cw,'A5':sol.realw}[T]
            _perc(w,it['options'][it['gold']],it['options'][a])
            les.append(f'Exam {it["id"]} ({T}): wrong pick; reweighted features → {json.dumps({k:round(x,2) for k,x in w.items()})}.')
        if T=='A3':
            f=feats(it['text']); c=sol.cent[it['gold']]
            for k in c: c[k]=round(0.8*c[k]+0.2*f[k],2)
            if s<1: les.append(f'Exam {it["id"]}: passage was {it["gold"]}, answered {a}; moved {it["gold"]} centroid → {c}.')
    return les
