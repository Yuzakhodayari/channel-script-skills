import os
# The pre-improvement storytelling rules (final folded state of the old harness), for an apples-to-apples "before" score.
import re, json, math, sys
import importlib.util as _u
_sp=_u.spec_from_file_location('c1',os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','v1-build','corpus.py')); C1=_u.module_from_spec(_sp); _sp.loader.exec_module(C1)
_ST=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','v1-build','stats.json')))['story']
_CR=[(re.compile(c['rx']),math.log((c['pct_first10']+2)/12),math.log((c['pct_last10']+2)/12)) for c in _ST if c['pos'] is None and c['files_with']>=5]
def nb(t):
    o=c=0.
    for s in C1.sents(t):
        l=s.lower()
        for rx,a,b in _CR:
            if rx.search(l): o+=a;c+=b
    return o,c
def W(t): return re.findall(r"[a-z0-9']+",t.lower())
def f1(a,b):
    A=set(W(a));B=set(W(b));
    if not A or not B: return 0
    i=len(A&B); return 2*i/(len(A)+len(B))
def sOpen(t):
    l=t.lower();v=0
    v-=2*bool(re.match(r"(he|she|they|it|that|this|also|again|these|those|and|but|so)\b",l)) + 2*bool(re.search(r"\b(again|also|like i said|remember|as i mentioned|back to)\b",l))
    v+=0.5*nb(t)[0]; return v
def sPlace(t):
    l=t.lower();sc={'open':0.,'middle':0.5,'close':0.}
    if re.search(r"\b(thanks for watching|thank you for|subscribe|see you|let me know in)\b",l): sc['close']+=2
    if re.search(r"\b(this is the story|in this video|today we|what no one|i want to tell you)\b",l): sc['open']+=2
    sc['open']-=1.0*len(re.findall(r"\b(remember|like i said|back to|that's why|again|earlier)\b",l)); sc['middle']+=0.3
    o,c=nb(t);sc['open']+=0.5*o+0.3;sc['close']+=0.5*c+0.3
    return max(sc,key=sc.get)
def ents(t): return set(re.findall(r"(?<![.?!] )\b[A-Z][a-zA-Z]{2,}",t))-{'The','And','But','So','This','That','It','They','He','She','We','You','In','On','Now','What','I','If','There','Because','When','Like','Well','Okay'}
def sNext(ctx,c): return f1(ctx,c)+0.15*len(ents(ctx)&ents(c))
def answer(it):
    if it['type']=='A': s=[sOpen(o) for o in it['options']]; return max(range(4),key=lambda i:(s[i],-i))
    if it['type']=='B': return sPlace(it['text'])
    s=[sNext(it['passage'],o) for o in it['options']]; return max(range(3),key=lambda i:s[i])
