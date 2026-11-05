import re,json,random,statistics as st,corpus,lang_dims,story_dims
docs=corpus.load()
for d in docs: d['unpunct']= len(d['sents'])<20
G=['adam','gen','especially','oil','after']
RNG=random.Random(7)
VERB=re.compile(r"\b(is|are|was|were|be|been|has|have|had|do|does|did|\w+ed|\w+s|can|will|would|could|should|gets?|got|goes|went|makes?|made|says?|said|think|know|want|need|'s|'re|'ve|'ll|'d|'m)\b")
def wavg(vals):  # list of (w,v)
    vals=[(w,v) for w,v in vals if v is not None]
    return sum(w*v for w,v in vals)/sum(w for w,_ in vals) if vals else 0
def pick_quotes(pairs,per):
    out=[]
    for g,n in per.items():
        c=[(s,d) for s,d in pairs if d['group']==g and 6<=len(s.split())<=40 and corpus.verify(s,d)]
        RNG.shuffle(c)
        seen=set()
        for s,d in c:
            if d['file'] in seen and len(c)>n: continue
            seen.add(d['file']); out.append({'group':g,'file':d['file'],'q':s})
            if sum(1 for o in out if o['group']==g)>=n: break
    return out
PER={'adam':2,'gen':2,'especially':1,'oil':1,'after':1}
# ---- language
L=[]
for dim in lang_dims.D:
    rows=[]
    pairs=[]
    for d in docs:
        sentok=not d['unpunct']
        if dim['scope']=='special':
            if not sentok: rows.append(None); continue
            lens=[len(corpus.words(s)) for s in d['sents']]
            n=dim['name']
            if n.startswith('Mean'): v=st.mean(lens)
            elif n.startswith('Median'): v=st.median(lens)
            elif 'SD' in n: v=st.pstdev(lens)
            elif n.startswith('Short'): v=100*sum(l<=6 for l in lens)/len(lens); pairs+=[(s,d) for s,l in zip(d['sents'],lens) if 3<=l<=6]
            elif n.startswith('Long'): v=100*sum(l>=30 for l in lens)/len(lens)
            elif n.startswith('Frag'):
                fr=[s for s in d['sents'] if not VERB.search(s.lower()) and len(s.split())<=8]; v=100*len(fr)/len(lens); pairs+=[(s,d) for s in fr]
            elif n.startswith('Quest'): q=[s for s in d['sents'] if s.rstrip('"”\'').endswith('?')]; v=100*len(q)/len(lens); pairs+=[(s,d) for s in q]
            else: q=[s for s in d['sents'] if s.rstrip('"”\'').endswith('!')]; v=100*len(q)/len(lens); pairs+=[(s,d) for s in q]
            rows.append(v)
        elif dim['scope'] in('opener','sent'):
            if not sentok: rows.append(None); continue
            rx=re.compile(dim['rx'])
            hit=[s for s in d['sents'] if rx.search(re.sub(r'^["“\'(]+','',s.lower()))]
            rows.append(100*len(hit)/len(d['sents'])); pairs+=[(s,d) for s in hit]
        else:
            rx=re.compile(dim['rx'],re.I)
            c=len(rx.findall(d['text'])); rows.append(1000*c/d['nw'])
            if sentok: pairs+=[(s,d) for s in d['sents'] if rx.search(s)]
    byg={g:wavg([(1,v) for d,v in zip(docs,rows) if d['group']==g]) for g in G}
    unit='per 100 sentences' if dim['scope'] in('opener','sent') else ('value' if dim['scope']=='special' else 'per 1k words')
    if dim['scope']=='special' and not dim['name'].startswith(('Mean','Median','Sentence-length')): unit='% of sentences'
    L.append({**dim,'unit':unit,'weighted':wavg([(d['w'],v) for d,v in zip(docs,rows)]),'by_group':byg,'quotes':pick_quotes(pairs,PER)})
# ---- story
S=[]
for c in story_dims.C:
    rx=re.compile(c['rx'])
    rows=[];pos=[];pairs=[]
    for d in docs:
        if d['unpunct']: rows.append(None); continue
        n=len(d['sents']); h=0
        for i,s in enumerate(d['sents']):
            f=i/n
            if c['pos']=='open' and f>0.08: continue
            if c['pos']=='close' and f<0.90: continue
            if rx.search(s.lower()):
                h+=1; pos.append((d['w'],f)); pairs.append((s,d))
        rows.append(1000*h/d['nw'])
    byg={g:wavg([(1,v) for d,v in zip(docs,rows) if d['group']==g]) for g in G}
    files_with=sum(1 for v in rows if v); 
    wp=wavg(pos) if pos else None
    first=100*sum(w for w,f in pos if f<0.1)/sum(w for w,_ in pos) if pos else 0
    last=100*sum(w for w,f in pos if f>=0.9)/sum(w for w,_ in pos) if pos else 0
    S.append({**c,'weighted':wavg([(d['w'],v) for d,v in zip(docs,rows)]),'by_group':byg,'mean_pos':wp,'pct_first10':first,'pct_last10':last,'files_with':files_with,'n_files':sum(1 for d in docs if not d['unpunct']),'quotes':pick_quotes(pairs,PER)})
json.dump({'lang':L,'story':S,'docs':[{k:d[k] for k in('group','file','w','nw','unpunct')}|{'dropped':d['info']['dropped']} for d in docs]},open('stats.json','w'),indent=1)
print(len(L),len(S))
for x in L[:8]+L[8:30]: print(x['name'],round(x['weighted'],2),{g:round(v,1) for g,v in x['by_group'].items()})
