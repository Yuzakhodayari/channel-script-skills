import re
from corpus import *
R=lambda p: re.compile(p,re.I)
PROMISE=R(r"\b(in this video|today,? (we|I)|I want to (take|tell|walk|show|explain|talk)|I'?m going to|we'?re going to|let'?s (talk|break|dive|get|start|look|figure|find|go)|by the end of|here'?s (what|how|why)|to answer (that|this)|to understand (this|that|why|how)|the full story|what (no one|nobody) is talking about|so how (did|do|does)|so why|the question is|I wanted to)\b")
THESIS=R(r"\b(the (real|bigger|actual) (problem|question|story|reason)|what'?s (actually|really) (happening|going on)|the truth is|this is (why|how|what)|wake-up call|is (going|about) to|might be (cooked|over)|will (break|end|destroy|change|kill)|nobody knows how|the problem is|which is why)\b")
SPON=R(r"\b(sponsor|sponsored|brought to you by|use code|promo code|link in (the|my) description|scan the QR|percent off|% off|free trial|for free|go to \S+\.(com|me|dev|io)|\.(com|me|dev)/\S*|encrypted email|today\'?s video sponsor)\b")
SPON_END=R(r"(^back to it|^so,? now let\'?s|^so,? back|\bback to (the|our)|anyway,|now,? back|so,? back|where were we|okay,? so)\b")
TRANS=R(r"^(so,? (now|then|what|why|how|let'?s|here'?s|where|if|that)|now,? |but here'?s|but (then|now|that'?s not)|which brings|first,|second(ly)?,|third,|finally,|next,|the (next|second|third|first|last|other) (thing|reason|problem|part|piece|step|big)|okay,? so|alright|let'?s (move|go|look|talk|get|start|turn)|and (that|this) (is|brings) |part (one|two|three|\d)|chapter|step (one|two|\d)|meanwhile|fast[- ]forward|back (in|to) |to understand|which (means|leads)|in (19|20)\d\d,)",)
CONC=R(r"\b(at the end of the day|in the end|ultimately|so where does (this|that) leave|so what (does|do|happens|can)|the (big|real) (lesson|takeaway)|what (this|it) all (means|comes down)|so,? is (this|it|AI)|I think (the|we|that'?s)|to (wrap|sum)|in conclusion|here'?s the thing|where (we|this) go(es)? from here)\b")
CTA=R(r"\b(subscribe|like (this|the) video|hit the (like|bell)|comment (below|down)|let me know in the comments|thanks for watching|thank you (so much )?for watching|patreon|newsletter|see you (in the|next)|share (this|it) with)\b")
def beatmap(v):
    S=v['sents']; n=len(S); D=v['dur']
    ev=[]
    # hook end = first promise in first 25%
    hook_end=None
    for i,s in enumerate(S):
        if s['pct']>25: break
        if PROMISE.search(s['text']) and s['t']>=5: hook_end=i; break
    if hook_end is None:
        hook_end=next((i for i,s in enumerate(S) if s['pct']>=6),min(5,n-1))
    thesis=None
    for i,s in enumerate(S[:hook_end+12]):
        if THESIS.search(s['text']): thesis=i; break
    ev.append(('COLD OPEN / HOOK',0))
    if thesis is not None and thesis<hook_end: ev.append(('THESIS / STAKES',thesis))
    ev.append(('PROMISE / ROADMAP',hook_end))
    if thesis is not None and thesis>hook_end: ev.append(('THESIS / STAKES',thesis))
    sp=[i for i,s in enumerate(S) if SPON.search(s['text'])]
    spblocks=[]
    for i in sp:
        if spblocks and i-spblocks[-1][1]<=14: spblocks[-1][1]=i
        else: spblocks.append([i,i])
    # sponsor block start: back up to sentence 'that's where/why' up to 3 before
    CORE=R(r'sponsor|use code|description|QR|promo')
    spblocks=[b for b in spblocks if any(CORE.search(S[k]['text']) for k in range(b[0],b[1]+1))]
    for b in spblocks:
        st=b[0]
        for j in range(b[0]-1,max(b[0]-4,-1),-1):
            if re.search(r"(that'?s (exactly )?(where|why)|speaking of|which is why I|this (video|episode) is)",S[j]['text'],re.I): st=j
        b[0]=st
        lt=S[b[1]]['t']; end=None
        for j in range(b[0]+1,min(n,b[0]+40)):
            if S[j]['t']>S[st]['t']+20 and SPON_END.search(S[j]['text']): end=j; break
        if end is None:
            end=next((j for j in range(b[1]+1,n) if S[j]['t']>=lt+4),n-1)
        if S[end]['t']-S[st]['t']<20 and not re.search(r'sponsored by|thanks to',S[st]['text'],re.I):
            end=next((j for j in range(st+1,n) if S[j]['t']>=S[st]['t']+50),n-1)
        b[1]=end-1
        ev.append(('SPONSOR READ',st)); 
        if end<n: ev.append(('RETURN FROM SPONSOR',end))
    inside=lambda i: any(b[0]<=i<=b[1] for b in spblocks)
    # sections: transitions spaced >=6% apart after hook
    last=S[hook_end]['pct']
    conc=None
    for i in range(n-1,int(n*0.75),-1):
        if CONC.search(S[i]['text']) and not inside(i) and not CTA.search(S[i]['text']): conc=i
    for i in range(hook_end+1,n):
        s=S[i]
        if inside(i): continue
        if conc is not None and i>=conc: break
        if TRANS.search(s['text']) and s['pct']-last>=6:
            ev.append(('SECTION TURN',i)); last=s['pct']
        elif s['text'].endswith('?') and len(s['text'].split())>=6 and s['pct']-last>=9:
            ev.append(('QUESTION TURN (re-hook)',i)); last=s['pct']
    if conc is not None: ev.append(('CONCLUSION',conc))
    ctas=[i for i,s in enumerate(S) if CTA.search(s['text']) and not inside(i) and (s['pct']>=90 or re.search(r'subscribe|patreon|newsletter|like this video|comment',s['text'],re.I))]
    for i in ctas: ev.append(('CTA',i))
    ev.append(('FINAL LINE',n-1))
    ev=sorted(set(ev),key=lambda e:(e[1],e[0]))
    out=[]
    for lab,i in ev:
        s=S[i]; out.append(dict(beat=lab,i=i,t=s['t'],pct=s['pct'],text=s['text']))
    return dict(events=out,hook_end=hook_end,thesis=thesis,spblocks=spblocks,conc=conc,ctas=ctas)
if __name__=='__main__':
    for v in all_videos()[:3]+all_videos()[5:7]:
        b=beatmap(v); print('##',v['key'],v['title'])
        for e in b['events']: print(f"{e['pct']:5}% {fmt(e['t'])} {e['beat']}: {e['text'][:90]}")
