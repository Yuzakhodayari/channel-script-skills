import re, json, glob, os
from pathlib import Path
W=os.environ.get('CHANNEL_CORPUS_DIR','corpus')
FILES=[]
for f in sorted(glob.glob(W+'/adam-voice-build/filtered-*.txt')): FILES.append(('adam',f,7.0,f.replace('adam-voice-build/filtered-','adam-transcripts/')))
for i in range(1,11): FILES.append(('gen',f'{W}/transcripts/{i}.txt',4.0,f'{W}/transcripts/{i}.txt'))
for n in ['01-spacex','02-ai-paradox','06-data-centers']: FILES.append(('especially',f'{W}/other-transcripts/especially/{n}.txt',3.0,f'{W}/other-transcripts/especially/{n}.txt'))
FILES.append(('oil',f'{W}/other-transcripts/especially/03-oil-apocalypse.txt',5.0,f'{W}/other-transcripts/especially/03-oil-apocalypse.txt'))
for f in sorted(glob.glob(W+'/other-transcripts/after/*.txt')): FILES.append(('after',f,1.0,f))
KEEP_LABELS={'Max','Narrator','Music'}
CUE=re.compile(r'\((?:[a-z][a-z ,\-]*music|music|laughs?|laughter|applause|upbeat[^)]*|tense[^)]*|dramatic[^)]*|[a-z ]*sound[^)]*|[a-z ]*playing[^)]*)\)|\[(?:music|Music|laughter|applause|Applause|Laughter)\]|>>',re.I)
def norm(s): return re.sub(r'\s+',' ',s).strip()
def raw_plain(path):
    t=Path(path).read_text(errors='ignore')
    t=re.sub(r'^Title:.*$','',t,flags=re.M)
    t=re.sub(r'\(\d+:\d+(?::\d+)?\)','',t)
    return norm(t)
def clean(group,path):
    t=Path(path).read_text(errors='ignore')
    if group=='adam':
        return norm(re.sub(r'^Title:.*$','',t,flags=re.M)), {'dropped':'pre-filtered (speaker-filter.md)'}
    t=re.sub(r'^Title:.*$','',t,flags=re.M)
    lines=[re.sub(r'^\(\d+:\d+(?::\d+)?\)\s*','',l) for l in t.splitlines()]
    dash=sum(1 for l in lines if l.startswith('- '))>5
    text='\n'.join(lines)
    drops=[]
    if dash:
        turns=re.split(r'(?:^|\n|\s)- (?=[\[A-Z"\'0-9(])',text)
        keep=[]
        for tu in turns:
            tu2=CUE.sub(' ',tu); s=norm(tu2)
            if not s: continue
            m=re.match(r'\[([^\]]+)\]\s*',s)
            if m and m.group(1).split(',')[0] not in KEEP_LABELS:
                drops.append(('label',s[:80])); continue
            if m: s=s[m.end():]
            if len(s.split())<=6:
                drops.append(('micro',s[:80])); continue
            keep.append(s)
        out=' '.join(keep)
    else:
        s=norm(CUE.sub(' ',text))
        # drop labeled guest segment: label up to end of 2nd sentence or next label
        def rep(m):
            drops.append(('label',m.group(0)[:80])); return ' '
        s=re.sub(r'\[(?!Max\]|Narrator\])[A-Z][^\]]{0,40}\][^\[]*?(?:[.!?]["”]?\s+[^\[]*?[.!?]["”]?(?=\s|$)|(?=\[)|$)',rep,s)
        s=re.sub(r'\[(Max|Narrator)\]\s*','',s)
        out=norm(s)
    return out,{'dropped':len(drops),'samples':drops[:8]}
SPLIT=re.compile(r'(?<=[.!?])["”\']?\s+(?=["“\'(]?[A-Z0-9$])')
def sents(t): return [x.strip() for x in SPLIT.split(t) if x.strip()]
def words(t): return re.findall(r"[A-Za-z0-9$%']+",t)
def load():
    docs=[]
    for g,f,w,src in FILES:
        txt,info=clean(g,f)
        ss=sents(txt)
        docs.append({'group':g,'file':os.path.basename(f).replace('filtered-',''),'path':f,'src':src,'w':w,'text':txt,'sents':ss,'nw':len(words(txt)),'info':info})
    return docs
RAW={}
def verify(q,doc):
    k=doc['src']
    if k not in RAW: RAW[k]=raw_plain(k).lower()
    qq=norm(q).lower()
    if qq in RAW[k]: return True
    # caption joins may have stripped cues mid-quote; tolerate by removing cue text in raw
    r2=norm(CUE.sub(' ',RAW[k]))
    r2=re.sub(r'\s*- \[[^\]]+\]\s*',' ',r2); r2=re.sub(r'\[(max|narrator)\]\s*','',r2)
    r2=re.sub(r'(^|\s)- ',' ',r2); r2=norm(r2)
    return qq in r2
