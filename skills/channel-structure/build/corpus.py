import re, glob, os, json
W=os.environ.get('CHANNEL_CORPUS_DIR','corpus')
def ts2s(t):
    p=[int(x) for x in t.split(':')]; s=0
    for x in p: s=s*60+x
    return s
VIDEOS=[]
def add(path,group,weight,key):
    VIDEOS.append(dict(path=path,group=group,weight=weight,key=key))
for f in sorted(glob.glob(W+'/adam-transcripts/*.txt')):
    add(f,'Adam',7,'adam/'+os.path.basename(f)[:-4])
for i in range(1,11):
    add(f'{W}/transcripts/{i}.txt','Gen',4,f'gen/{i}')
for n,wt,g in [('01-spacex',3,'Especially'),('02-ai-paradox',3,'Especially'),('03-oil-apocalypse',5,'Oil'),('06-data-centers',3,'Especially')]:
    add(f'{W}/other-transcripts/especially/{n}.txt',g,wt,'esp/'+n)
for f in sorted(glob.glob(W+'/other-transcripts/after/*.txt')):
    add(f,'Others',1,'after/'+os.path.basename(f)[:-4])
GW={'Adam':7,'Gen':4,'Especially':3,'Oil':5,'Others':1}
NOISE=re.compile(r'\[(music|Music|laughter|applause|Applause|Laughter)\]|\((bass noise|upbeat music|music)[^)]*\)',re.I)
HOSTLAB={'Sam','Narrator'}
def norm(s): return re.sub(r'[^a-z0-9]+',' ',s.lower()).strip()
_adamf={}
def adam_filtered(key):
    n=key.split('/')[1]
    if n not in _adamf: _adamf[n]=norm(open(f'{W}/adam-voice-build/filtered-{n}.txt').read())
    return _adamf[n]
def load(v):
    raw=open(v['path']).read().splitlines()
    title=''; units=[]
    for ln in raw:
        if ln.startswith('Title:'): title=ln[6:].strip(); continue
        m=re.match(r'\((\d+:\d+(?::\d+)?)\)\s?(.*)',ln)
        if not m:
            if ln.strip() and not units: units.append([0,ln.strip(),True])
            elif ln.strip() and units: units[-1][1]+=' '+ln.strip()
            continue
        units.append([ts2s(m.group(1)),m.group(2),True])
    if all(u[0]==0 for u in units) and len(units)<=2:
        ws=' '.join(u[1] for u in units).split(); units=[]
        for i in range(0,len(ws),12): units.append([int(i/2.5),' '.join(ws[i:i+12]),True])
    # host filter
    guest=False; prev_end=True
    for u in units:
        t=u[1]; t=re.sub(r'^-\s*','',t)
        lab=re.match(r'\[([A-Z][A-Za-z .]+)\]\s*',t)
        if lab and lab.group(1).lower() not in ('music','laughter','applause'):
            nm=lab.group(1)
            if nm in HOSTLAB: guest=False; t=t[lab.end():]
            else: guest=True; u[2]=False
        elif guest and (u[1].lstrip().startswith('-') or (t[:1].isupper() and prev_end)):
            guest=False
        t=NOISE.sub('',t).replace('>>','').strip()
        u[1]=t
        if guest and not lab: u[2]=False
        if v['group']=='Adam':
            nt=norm(t); u[2]=bool(nt) and nt in adam_filtered(v['key'])
        if not t: u[2]=False
        prev_end=bool(re.search(r'[.!?]["”’)]*$',t))
    host=[(s,t) for s,t,k in units if k]
    dur=max([s for s,_,_ in units]+[1])+3
    # sentences with start times
    text='';starts=[]
    for s,t in host:
        if text: text+=' '
        starts.append((len(text),s)); text+=t
    sents=[]; 
    for m in re.finditer(r'[^.!?]+(?:[.!?]+["”’\')]*|$)',text):
        st=m.group().strip()
        if len(st)<2: continue
        off=m.start(); sec=0
        for o,s in starts:
            if o<=off: sec=s
            else: break
        sents.append(dict(t=sec,text=st,pct=round(100*sec/dur,1)))
    if len(sents)<0.02*len(text.split()):
        sents=[]
        for i,(s0,t0) in enumerate(host):
            if i%2==0: sents.append(dict(t=s0,text=t0,pct=round(100*s0/dur,1)))
            else: sents[-1]['text']+=' '+t0
    words=len(text.split())
    allraw=open(v['path']).read()
    return dict(**v,title=title,dur=dur,sents=sents,words=words,text=text,raw=allraw,host_units=len(host),all_units=len(units))
def all_videos():
    return [load(v) for v in VIDEOS]
def fmt(sec): return f'{int(sec)//60}:{int(sec)%60:02d}'
