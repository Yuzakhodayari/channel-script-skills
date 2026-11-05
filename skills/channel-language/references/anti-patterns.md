# channel-language: anti-patterns

Each item: the AI or wrong-lean pattern, a before line, and an after line. After lines are illustrative rewrites in the channel voice, not corpus quotes. Corpus rates for the tells are in criteria.md (AI-tell vocabulary and essay connectors are practically zero in host speech).

## Quick sweep regex
```
\b(delve|tapestry|testament|landscape|crucial|pivotal|robust|leverage|seamless|multifaceted|intricate|realm|underscore|showcase|foster|vibrant|navigate|moreover|furthermore|additionally|consequently|nevertheless|in conclusion|notably|it is important to note)\b
```
Also flag: `;` · `—` chains · `!` · "it is / do not / cannot" · zero fillers in 60+ words · five sentences of similar length in a row.

### A1. Essay connector opener
- Before: "Moreover, the company lost $2 trillion in market value."
- After: "And the company lost about $2 trillion in market value. Just on paper."

### A2. 'Furthermore' chain
- Before: "Furthermore, analysts expect further declines. Additionally, investors are concerned."
- After: "And analysts think it gets worse. Investors are kind of freaking out."

### A3. 'In conclusion' ending
- Before: "In conclusion, the future of AI remains uncertain."
- After: "So where does that leave us? Honestly, nobody knows yet."

### A4. 'It is important to note'
- Before: "It is important to note that these figures are estimates."
- After: "To be clear, these are estimates."

### A5. Delve / tapestry vocabulary
- Before: "Let's delve into the rich tapestry of the oil market."
- After: "So let's get into how the oil market actually works."

### A6. 'Landscape' / 'realm'
- Before: "In today's rapidly evolving AI landscape, companies must adapt."
- After: "AI is moving so fast right now that companies basically have to keep up or die."

### A7. 'Crucial' / 'pivotal'
- Before: "This was a pivotal moment that played a crucial role."
- After: "This is the moment everything changed."

### A8. Expanded contractions
- Before: "It is not clear what they are going to do, and we do not know."
- After: "It's not clear what they're gonna do. We don't know."

### A9. Zero fillers (sterile)
- Before: "The price increased because demand exceeded supply."
- After: "The price went up because, basically, everyone wanted it at the same time."

### A10. Uniform sentence length
- Before: "The company built a data center. It used a lot of water. Residents complained about it. The city approved it anyway."
- After: "The company built a data center. It drank a lot of water, like, millions of gallons a day in a town that was already in a drought. Residents complained. The city approved it anyway."

### A11. Semicolon splice
- Before: "The rocket launched; it reached orbit; it landed."
- After: "The rocket launched. It hit orbit. And then it landed itself."

### A12. Em-dash chain
- Before: "The plan — ambitious, costly, risky — failed."
- After: "The plan was ambitious. Expensive. Risky. And it failed."

### A13. Rule-of-three flourish
- Before: "It is faster, cheaper, and more efficient."
- After: "It's faster. It's also way cheaper."

### A14. 'Not X, but Y' every paragraph
- Before: "It is not just a product; it is a revolution."
- After: "It's a product. A really good one. But calling it a revolution is a stretch."

### A15. Vague quantity
- Before: "A significant number of people were affected."
- After: "About 40,000 people lost power."

### A16. 'Numerous studies show'
- Before: "Numerous studies show that AI may displace workers."
- After: "A 2025 Stanford paper found employment for 22-to-25-year-olds in the most AI-exposed jobs fell about 13%."

### A17. Passive voice hiding the actor
- Before: "Mistakes were made and the model was released."
- After: "xAI pushed the update out anyway."

### A18. Hedge stack
- Before: "It could potentially perhaps suggest that maybe prices might rise."
- After: "Prices will probably go up."

### A19. Over-hedging, no landing
- Before: "It's possible that this may or may not matter."
- After: "I think this matters. Here's why."

### A20. Corporate 'leverage'
- Before: "Companies leverage AI to unlock value."
- After: "Companies use AI to cut costs. Mostly that means people."

### A21. 'Serves as a testament'
- Before: "This serves as a testament to human ingenuity."
- After: "Which is honestly kind of amazing."

### A22. Exclamation hype
- Before: "This is huge! You won't believe it!"
- After: "This is a big deal. And it's not even the craziest part."

### A23. Formal synonym swap
- Before: "Individuals utilize the platform to obtain information."
- After: "People use it to look stuff up."

### A24. Gen tic in Adam-lean
- Before: "Look, this is lowkey cooked."
- After: "I think this is a real problem."

### A25. Adam-earnest in Gen-lean
- Before: "I think it's important that we think carefully about this."
- After: "So yeah, that's a problem. Because if this breaks, the whole thing breaks."

### A26. Oil-lean without the dry joke
- Before: "Gas prices rose sharply across the country."
- After: "Gas prices went up everywhere. Here's a station in Texas that just ran out."

### A27. Listicle headers in narration
- Before: "First and foremost, let's examine the key factors."
- After: "So there are basically three things going on here."

### A28. 'Dear viewers' / syllabus intro
- Before: "In this video, we will explore the history and implications of chip manufacturing."
- After: "This is the story of how one island ended up making almost every advanced chip on Earth."

### A29. Generic closing moral
- Before: "Only time will tell what the future holds."
- After: "And the next earnings call is in three weeks. So we're gonna find out."

### A30. Sycophantic / chatbot voice
- Before: "Great question! Let's break it down."
- After: "So why is this happening? Because..."

### A31. Synonym cycling
- Before: "The firm... the company... the organization... the enterprise..."
- After: "OpenAI... OpenAI... they..."

### A32. Title Case and bold in spoken script
- Before: "**Key Takeaway:** The Market Is Shifting."
- After: "The market's shifting. And fast."

### A33. Unanchored superlative
- Before: "This is the most important event in history."
- After: "Some researchers call it the most important event since the industrial revolution. That's their phrase, not mine."

### A34. Abstract noun pileup
- Before: "The commodification of attention drives the monetization of engagement."
- After: "They sell your attention. That's the business."

### A35. Perfectly balanced 'both sides' close
- Before: "There are valid arguments on both sides."
- After: "To be fair, the other side has a point. But the numbers don't really back it up."
