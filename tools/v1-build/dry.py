import exams,pool,random,statistics as st
P=pool.passages()
open('/tmp/a.md','w').write('# x\n## L\n');open('/tmp/b.md','w').write('# x\n## L\n')
for fn,name in((exams.run_lang,'lang'),(exams.run_story,'story')):
    f=exams.Fold(name,{},[('/tmp/a.md','## L')])
    r=fn(P,random.Random(11 if name=='lang' else 12),f)
    for t in 'ABC':
        s=[x['score'] for x in r if x['type']==t]; print(name,t,len(s),round(st.mean(s),3))
    print([round(st.mean(x['score'] for x in r[i:i+10]),2) for i in range(0,100,10)])
    print(f.log)
