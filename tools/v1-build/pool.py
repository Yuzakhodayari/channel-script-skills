import re,random,corpus
docs=[d for d in corpus.load() if len(d['sents'])>=20]
def passages(minw=55,maxw=120):
    P=[]
    for d in docs:
        ss=d['sents'];n=len(ss);i=0
        while i<n:
            j=i;w=0
            while j<n and w<minw: w+=len(ss[j].split()); j+=1
            if minw<=w<=maxw:
                t=' '.join(ss[i:j])
                if corpus.verify(t,d): P.append({'id':f"{d['file']}#{i}",'group':d['group'],'file':d['file'],'w':d['w'],'i':i,'j':j,'pos':i/n,'text':t,'sents':ss[i:j],'doc':d})
            i=j
    return P
def sample_by_weight(P,k,rng,exclude=set()):
    P=[p for p in P if p['id'] not in exclude]
    out=[];used=set()
    while len(out)<k:
        p=rng.choices(P,weights=[x['w'] for x in P])[0]
        if p['id'] in used: continue
        used.add(p['id']); out.append(p)
    return out
CONTR={"it's":"it is","don't":"do not","can't":"cannot","won't":"will not","that's":"that is","there's":"there is","they're":"they are","you're":"you are","we're":"we are","i'm":"I am","isn't":"is not","doesn't":"does not","didn't":"did not","wasn't":"was not","aren't":"are not","what's":"what is","here's":"here is","i've":"I have","you've":"you have","we've":"we have","they've":"they have","let's":"let us","he's":"he is","she's":"she is","wouldn't":"would not","couldn't":"could not","i'd":"I would","you'll":"you will","i'll":"I will","gonna":"going to","kinda":"somewhat","wanna":"want to"}
FILL=[r'\bbasically,? ',r'\bactually,? ',r'\bliterally ',r'\bkind of ',r'\bsort of ',r',? you know,? ',r'\bhonestly,? ',r'\bjust ',r'\breally ',r'\bpretty ',r'\blike, ',r'\bI mean,? ',r'\bprobably ']
CASUAL={'big':['substantial','significant'],'huge':['significant','considerable'],'a lot of':['a significant amount of','numerous'],'crazy':['remarkable','unprecedented'],'insane':['extraordinary'],'get':['obtain'],'gets':['obtains'],'stuff':['materials'],'guy':['individual'],'guys':['individuals'],'wild':['notable'],'show':['demonstrate'],'shows':['demonstrates'],'use':['utilize'],'help':['facilitate'],'kids':['children'],'money':['capital'],'cheap':['cost-effective'],'buy':['purchase'],'start':['commence'],'need':['require'],'about':['approximately']}
OPEN={'So':['Therefore,','Consequently,','As a result,'],'And':['Additionally,','Furthermore,','Moreover,'],'But':['However,','Nevertheless,'],'Now':['Currently,'],'Because':['This is because'],'Like':['For example,'],'Well':['Indeed,'],'Okay':['Notably,']}
CLOSERS=["This highlights the crucial role these dynamics play in today's rapidly evolving landscape.","Ultimately, this serves as a powerful testament to the complex interplay of forces at work.","It is important to note that the implications of this are multifaceted and far-reaching.","In conclusion, this underscores the pivotal challenges ahead."]
def _case(m,rep):
    s=m.group(0); return rep[0].upper()+rep[1:] if s[0].isupper() else rep
def aiify(text,rng,level='heavy'):
    t=text
    for k,v in CONTR.items(): t=re.sub(r'\b'+re.escape(k)+r'\b',lambda m,v=v:_case(m,v),t,flags=re.I)
    for f in FILL: t=re.sub(f,'',t,flags=re.I)
    ss=corpus.sents(t);out=[]
    for s in ss:
        fw=s.split(' ',1)
        if level=='heavy' and fw[0].rstrip(',') in OPEN and len(fw)>1:
            s=rng.choice(OPEN[fw[0].rstrip(',')])+' '+fw[1][0].lower()+fw[1][1:]
        elif level=='subtle' and fw[0].rstrip(',') in ('So','And','But','Like','Okay','Well') and len(fw)>1:
            s=fw[1][0].upper()+fw[1][1:]
        out.append(s)
    # uniformize: merge short sentences into previous
    merged=[]
    for s in out:
        if merged and len(s.split())<=6: merged[-1]=merged[-1].rstrip('.?!')+(', and ' if level=='subtle' else '; ')+s[0].lower()+s[1:]
        else: merged.append(s)
    t=' '.join(merged)
    if level=='heavy':
        for k,v in CASUAL.items(): t=re.sub(r'\b'+re.escape(k)+r'\b',lambda m,v=v:_case(m,rng.choice(v)),t)
        t+=' '+rng.choice(CLOSERS)
    t=re.sub(r'\s+',' ',t).strip()
    return ' '.join(x[0].upper()+x[1:] for x in corpus.sents(t))
