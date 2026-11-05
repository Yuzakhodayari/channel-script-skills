import re
ANCH={
 'hook_sec':lambda v,b:b['hook_end'],'hook_words':lambda v,b:b['hook_end'],'hook_pct':lambda v,b:b['hook_end'],
 'first_sentence_words':lambda v,b:0,'hook_sent_words':lambda v,b:0,'dur_min':lambda v,b:0,'words_total':lambda v,b:0,'wpm':lambda v,b:0,'title_words':lambda v,b:0,'title_in_hook':lambda v,b:0,'title_how_why':lambda v,b:0,'title_question':lambda v,b:0,'title_number':lambda v,b:0,'q_per_min_open':lambda v,b:0,'num_per_min_open':lambda v,b:0,'you_open':lambda v,b:0,
 'thesis_sec':lambda v,b:b['thesis'],
 'sponsor_pct':lambda v,b:b['spblocks'][0][0] if b['spblocks'] else None,'sponsor_bridge':lambda v,b:b['spblocks'][0][0] if b['spblocks'] else None,'has_midroll':lambda v,b:b['spblocks'][0][0] if b['spblocks'] else None,
 'sponsor_sec_len':lambda v,b:(b['spblocks'][0][1]+1 if b['spblocks'][0][1]+1<len(v['sents']) else None) if b['spblocks'] else None,
 'conc_pct':lambda v,b:b['conc'],'recap_end':lambda v,b:b['conc'],'callback_end':lambda v,b:len(v['sents'])-1,'end_sent_words':lambda v,b:len(v['sents'])-1,
 'cta_count':lambda v,b:b['ctas'][0] if b['ctas'] else None,'outro_sec':lambda v,b:b['ctas'][0] if b['ctas'] else None,
}
QRX={'q_per_min':r'\?$','q_per_min_end':r'\?$','density_curve_q':r'\?$','num_per_min':r'\d','year_mentions':r'\b(19|20)\d\d\b',
 'story_ratio':r'\b(was|were|had|said|told)\b','explain_ratio':r'\b(which means|basically|because)\b','you_all':r'\byou\b','i_all':r'\bI\b',
 'mean_sent_words':r'.','section_gap_pct':r'^(so|now|but then|but here)','n_sections':r'^(so|now|but then|but here)','sections_per_10min':r'^(so|now|but then|but here)','question_turn_share':r'^(so,? )?(what|why|how).*\?$',
 'rehook_gap':r"^but\b|\bturns out\b",'q_gap':r'\?$','but_gap':r'^but\b','you_per_k':r'\byou\b','you_close':r'\byou\b','we_per_k':r'\bwe\b','i_per_k':r'\bI\b','they_per_k':r'\bthey\b',
 'hedge_per_k':r'\b(I think|probably|kind of|sort of)\b','fear_per_k':r'\b(danger\w*|threat\w*|catastroph\w*|disaster|collapse|extinct\w*)\b','fear_open':r'\b(danger\w*|threat\w*|disaster|collapse|risk)\b',
 'outrage_per_k':r'\b(greed\w*|scam\w*|corrupt\w*|slop|cooked|insane)\b','hope_per_k':r'\b(hope\w*|good news|we can|solution)\b','hope_close':r'\b(hope\w*|good news|we can|better|possible)\b',
 'profanity_per_k':r'\b(hell|damn|shit|ass|sucks)\b','money_per_k':r'\$','credibility_per_k':r'\b(according to|report|study|documents?)\b','humor_per_k':r'\b(wild|crazy|weird|literally)\b',
 'short_punch_share':r'^\S+(\s\S+){0,4}$','imperative_share':r'^(look|think|imagine|take|picture|remember|let\'?s)\b'}
