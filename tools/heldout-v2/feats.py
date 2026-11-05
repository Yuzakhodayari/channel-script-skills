import re
R=lambda p: re.compile(p,re.I)
STOPCAP={'The','And','But','So','This','That','It','They','He','She','We','You','In','On','Now','What','I','If','There','Because','When','Like','Well','Okay','And','Or','Then','Just','Here','Why','How','Who','Which','A','An','My','Our','Your','Their','His','Her','Its','Yes','No','Oh','Right','Imagine','Let','Let\'s','Today','Not','All','One','As','At','For','To','Of','With','By','From','Also','Even','Every','Some','These','Those','Do','Does','Did','Is','Are','Was','Were','Maybe','Of','After','Before','Once','While','Since','Instead','Meanwhile'}
F={
 # (pattern, applies to) -- every feature is a count normalised later
 'starts_connector': R(r"^\W*(and|but|so|or|because|which|also|then|plus)\b"),
 'starts_anaphor':   R(r"^\W*(he|she|they|it|this|that|these|those|his|her|their|its|him|them)\b"),
 'callback':         R(r"\b(remember|like i said|as i said|as i mentioned|i mentioned|we talked about|we saw|earlier|back to|again|once again|we've seen|we just|that's why|so far|at this point|by now|all of this|all this|this whole)\b"),
 'you':              R(r"\byou(r|'re|'ll|'ve|'d|rself)?\b"),
 'i_me':             R(r"\b(i|i'm|i've|i'd|i'll|me|my|myself)\b"),
 'we':               R(r"\b(we|we're|we've|we'll|us|our)\b"),
 'question':         R(r"\?"),
 'number':           R(r"\b\d[\d,.]*\b|\b(million|billion|trillion|percent|hundred|thousand)\b|%|\$"),
 'year_date':        R(r"\b(1[89]\d\d|20\d\d)\b|\b(january|february|march|april|june|july|august|september|october|november|december|monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b"),
 'in_medias_res':    R(r"\b(just|right now|this week|last week|yesterday|today|this morning|a few (days|weeks|months) ago|recently|one (guy|day|morning|night))\b"),
 'past':             R(r"\b(was|were|had|did|said|went|came|became|told|\w+ed)\b"),
 'future':           R(r"\b(will|won't|going to|gonna|future|next (year|decade|few)|years from now|by 20\d\d|coming)\b"),
 'hedge_project':    R(r"\b(might|may|could|maybe|perhaps|probably|i think|i believe|i hope|hopefully)\b"),
 'promise':          R(r"\b(in this video|today,? (we|i)|i want to (take|tell|walk|show|explain|talk)|i'?m going to|we'?re going to|let'?s (talk|break|dive|get|start|look|figure|find|go)|by the end of|here'?s (what|how|why)|the full story|what (no one|nobody) is talking about|this is the story|story of)\b"),
 'stakes':           R(r"\b(everything|nobody|no one|everyone|entire|whole world|end of|collapse|crisis|disaster|catastroph|die|death|dead|kill|destroy|threat|danger|terrif|scar(y|ed)|apocalypse|cooked|over)\b"),
 'hope':             R(r"\b(hope|better|choose|choice|build|solution|chance|together|matter|power to|can still|still)\b"),
 'conclusion':       R(r"\b(at the end of the day|in the end|ultimately|so where does|so what (does|do|happens|can)|the (big|real) (lesson|takeaway)|what (this|it) all (means|comes down)|to (wrap|sum)|in conclusion|here'?s the thing|from here|the bottom line|long run|the answer is)\b"),
 'signoff':          R(r"\b(subscribe|thanks for watching|thank you (so much )?for watching|thank you|thanks|patreon|newsletter|see you|next video|comment|let me know|link (below|in)|description|channel|bye|take care|until next time)\b"),
 'sponsor':          R(r"\b(sponsor|use code|promo code|free trial|\.com|\.me|% off|percent off|brought to you)\b"),
 'mechanism':        R(r"\b(which means|because|in other words|so that|the reason|basically|that means|this means|per|each|cost|costs|price|revenue|profit)\b"),
 'imperative_open':  R(r"^\W*(imagine|picture|think about|look at|listen|consider|meet|let me)\b"),
 'definite_unest':   R(r"^\W*the\b"),
 'demonstrative_def':R(r"^\W*(this|that) (is|was)\b"),
 'contrast':         R(r"\b(but|however|yet|instead|actually)\b"),
 'superlative':      R(r"\b(biggest|largest|most|worst|best|first|only|never|ever|every|single)\b"),
 'profanity':        R(r"\b(hell|damn|shit|fuck|crap|ass)\w*"),
 'meta_video':       R(r"\b(this video|video|episode|channel|today's)\b"),
 'list_marker':      R(r"\b(first|second|third|finally|next|another|number (one|two|three))\b"),
 'greeting':         R(r"^\W*(ladies and gentlemen|real quick|so,? (let'?s|come with me))\b"),
 'viewer_frame':     R(r"\b(take a look at|i'?m sure you'?ve|you might think|you'?ve been alive|if you were going to)\b"),
 'dated_start':      R(r"^\W*(on|in|for|by|back in|at)\s+(the year\s+)?(\d|(january|february|march|april|may|june|july|august|september|october|november|december|monday|tuesday|wednesday|thursday|friday|saturday|sunday))"),
 'number_start':     R(r"^\W*\$?\d"),
 'reflective':       R(r"\b(i think|i believe|to me|for me|honestly|personally|i don't know|the truth is|in my opinion)\b"),
}
def ents(t):
    out=set()
    toks=re.findall(r"(?:^|(?<=[\s\"“(]))([A-Z][a-zA-Z'\-]+)",t)
    for i,w in enumerate(toks):
        if w not in STOPCAP and w.rstrip("'s") not in STOPCAP: out.add(w)
    return out
def feats(t,first_sent=None):
    w=max(len(t.split()),1); l=t
    d={}
    for k,rx in F.items():
        if k.startswith('starts_') or k in('imperative_open','definite_unest','demonstrative_def','greeting','dated_start','number_start'):
            d[k]=1.0 if rx.search(first_sent if first_sent is not None else t) else 0.0
        else:
            d[k]=min(len(rx.findall(l)),6)/ (1+w/25)   # rate per ~25 words
    d['n_ents']=len(ents(t))/(1+w/25)
    d['len_words']=w/40
    d['short']=1.0 if w<=12 else 0.0
    return d
NAMES=list(feats('x').keys())
