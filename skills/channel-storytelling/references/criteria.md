# channel-storytelling: 112 criteria

## Corpus and weighting
| corpus | files | weight per file | host words used | notes |
|---|---|---|---|---|
| Adam (7x) | 5 | 7.0 | 31295 | pre-filtered by speaker-filter.md |
| Gen (4x) | 10 | 4.0 | 42213 | guest/news labels and micro-clips dropped: 0 units; 7.txt is unpunctuated auto-caption: lexical rates only, excluded from sentence stats |
| Especially 01/02/06 (3x) | 3 | 3.0 | 14930 | guest/news labels and micro-clips dropped: 0 units |
| Oil 03 (5x) | 1 | 5.0 | 5786 | guest/news labels and micro-clips dropped: 22 units |
| After (1x) | 12 | 1.0 | 44651 | guest/news labels and micro-clips dropped: 57 units |

Especially 04/05/07 duplicate Adam videos and are counted only as Adam. Weighted statistics = sum(file weight x file rate) / sum(file weight). Total weight: Adam 35, Gen 40 (36 for sentence stats), Especially 9, Oil 5, After 12.


For each criterion: weighted rate per 1k host words, per-creator rates (plain mean over that creator's files), weighted mean placement in the video, the weighted share of hits in the first 10% and last 10%, and how many of the 30 punctuated videos contain it. Criteria marked [open] or [close] are counted only in the first 8% or last 10% of a video.


## Cold open & hook

### S1. Number-first cold open [open]
- **Definition:** First lines lead with a hard number or amount.
- **Weighted frequency:** 0.04/1k. Adam 0.03, Gen 0.03, Especially 0.12, Oil 0.00, After 0.02. Present in 4/30 videos
- **Placement:** mean 5% through the video. 100% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "20 minutes ago, he was CEO of the most famous AI company on Earth."
  - **Gen (4x)** `4.txt`: "$725 billion spent this year alone betting that AI will eventually replace human labor."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "15 times that ship stopped, refused, and slowly made its way home."
- **Do:** Open with the single most absurd true number.
- **Don't:** Do not open with a vague trend ("AI is changing everything").
- **Checklist test:** Is there a concrete number in the first 2 sentences?

### S2. Dated-moment cold open [open]
- **Definition:** Open inside a specific dated moment.
- **Weighted frequency:** 0.10/1k. Adam 0.23, Gen 0.02, Especially 0.00, Oil 0.00, After 0.05. Present in 8/30 videos
- **Placement:** mean 3% through the video. 100% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "California time on Monday, July 7th, 2025, less than 48 hours before the biggest product launch in xAI's short history."
  - **Adam (7x)** `04-superintelligence.txt`: "Most notably, there's Anthropic, OpenAI, and Google DeepMind, all in the English speaking world, though China and DeepSeek recently turned heads in January with a surprisingly advanced and efficient model."
  - **Gen (4x)** `3.txt`: "Existing home sales were down 2.4% in June."
  - **After (1x)** `03-recycling.txt`: "But, in 1933, British company Imperial Chemical Industries, great name, accidentally discovered a way to synthesize this industrially."
- **Do:** Name the day/date and drop the viewer into it.
- **Don't:** No "Throughout history..." openings.
- **Checklist test:** Does sentence 1-3 contain a date or day?

### S3. In-medias-res event open [open]
- **Definition:** Start mid-event, before context.
- **Weighted frequency:** 0.45/1k. Adam 0.49, Gen 0.50, Especially 0.25, Oil 0.17, After 0.50. Present in 27/30 videos
- **Placement:** mean 4% through the video. 100% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Elon Musk's artificial intelligence chatbot began making anti-Semitic posts, even praising Hitler."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "So OpenAI decides to just turn off their automated safety monitors completely for this test."
  - **Gen (4x)** `8.txt`: "And it's not like you're just eating at fast food restaurants, right?"
  - **Gen (4x)** `5.txt`: "One that Big Tech has already planned for, so when a data center dies, they walk away just fine."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Sand blowing off the dunes over the churning water that barely covered a shallow reef 15 times the Prince of Portugal had sent a ship down to explore the world just a couple hundred miles from their home."
  - **After (1x)** `03-recycling.txt`: "So, I'm just going to reuse this clip every time that comes up."
- **Do:** Start with the event happening, explain later.
- **Don't:** Do not start with background or definitions.
- **Checklist test:** Is the first beat an action, not a summary?

### S4. "What no one is talking about" hook
- **Definition:** Promise a hidden angle the audience is missing.
- **Weighted frequency:** 0.03/1k. Adam 0.00, Gen 0.05, Especially 0.00, Oil 0.17, After 0.00. Present in 3/30 videos
- **Placement:** mean 58% through the video. 31% of hits in the first tenth, 31% in the last tenth
- **How they do it (verbatim):**
  - **Gen (4x)** `9.txt`: "But what nobody talks about is that now when 10 companies now make up 40% of that, you're again riding on the exact same handful of companies all making the same bet funded all the exact same ways."
  - **Gen (4x)** `1.txt`: "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Like, let's say, you're Australia, and you have a rich, vibrant economy that exports iron ore and fairy bread to a grateful world, but what you don't have is oil or a big refinery industry."
- **Do:** Use once in the first minute.
- **Don't:** Do not repeat it every section.
- **Checklist test:** Is there one hidden-angle claim near the open?

### S5. Stakes question hook [open]
- **Definition:** A question in the open that the video will answer.
- **Weighted frequency:** 0.55/1k. Adam 0.32, Gen 0.85, Especially 0.38, Oil 0.52, After 0.45. Present in 25/30 videos
- **Placement:** mean 4% through the video. 100% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "He's been spending the better part of a year doing press, traveling the world meeting global leaders ever since his company, OpenAI, released a chatbot, which you know what?"
  - **Adam (7x)** `02-bestselling-book.txt`: "What does your gut feeling say about whether, by say 2028, we'll see any of that happen in the real world?"
  - **Gen (4x)** `3.txt`: "So, if nobody's buying and it keeps going up, at this point, is this even a real market?"
  - **Gen (4x)** `4.txt`: "So then, months later, why the hell am I paying for this thing more than I ever paid Jason?"
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "What exactly is this fight over data centers actually about?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Do you remember that oil shock we warned you about a few months ago?"
  - **After (1x)** `12-data-centres-not-working.txt`: "Because who's actually paying the price?"
- **Do:** End the cold open with the central question.
- **Don't:** No rhetorical questions with obvious answers.
- **Checklist test:** Does the open end on a real question?

### S6. Viewer-assumption flip
- **Definition:** State what the viewer assumes, then flip it.
- **Weighted frequency:** 0.22/1k. Adam 0.21, Gen 0.28, Especially 0.20, Oil 0.17, After 0.11. Present in 14/30 videos
- **Placement:** mean 45% through the video. 27% of hits in the first tenth, 7% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "You probably know how that went."
  - **Adam (7x)** `02-bestselling-book.txt`: "If you are someone who cares about this issue and is willing to learn, then you are already closer than you might think."
  - **Gen (4x)** `9.txt`: "And if you're a pension fund, you probably want to know that before you handed over the money."
  - **Gen (4x)** `1.txt`: "Again, you probably say the AI companies since that's where again all the money is moving, but even they're having to fight to keep you."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth isn't as big as you might think."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Okay, so all of this is not great, you probably noticed it making your power bill more expensive, flights getting canceled, price of gas, but it's not like post-apocalyptic dystopia."
  - **After (1x)** `06-diamonds.txt`: "Most people think about diamonds for jewelry, but everybody's missing what's most exciting happening right now."
- **Do:** Voice the viewer's first reaction honestly.
- **Don't:** Do not strawman the viewer.
- **Checklist test:** Is the assumption one a real viewer would hold?

### S7. "Hold on / wait" self-interrupt
- **Definition:** Narrator interrupts himself to correct scope or tone.
- **Weighted frequency:** 0.50/1k. Adam 0.17, Gen 0.97, Especially 0.14, Oil 0.35, After 0.35. Present in 18/30 videos
- **Placement:** mean 46% through the video. 13% of hits in the first tenth, 9% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "KAM1196A then reasoned, During wait, emotional check."
  - **Adam (7x)** `02-bestselling-book.txt`: "At this point, you're probably thinking, "Okay, but why?"
  - **Gen (4x)** `8.txt`: "But wait, wait, hold on here."
  - **Gen (4x)** `2.txt`: "Okay, but why do we do that?"
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Wait for a callback that lands while I can't answer."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And to show you how, we need to flip the board one last time, but we run out of board to flip, so hold on."
  - **After (1x)** `09-microchip-war.txt`: "Each transistor is becoming smaller than a width of a human hair, wait, no, sorry, that's actually way too big of a scale."
- **Do:** Use to re-scope a claim right after the hook.
- **Don't:** Do not fake surprise repeatedly.
- **Checklist test:** Does the interrupt narrow or sharpen the claim?

### S8. Shock adjective framing [open]
- **Definition:** Emotional label on the event early.
- **Weighted frequency:** 0.05/1k. Adam 0.09, Gen 0.02, Especially 0.05, Oil 0.00, After 0.07. Present in 6/30 videos
- **Placement:** mean 3% through the video. 100% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "What is so exciting and terrifying about reading this document is that it's not just a research report."
  - **Adam (7x)** `01-ai-disaster.txt`: "It is a wild story, but more importantly, it's a wake-up call."
  - **Gen (4x)** `3.txt`: "Okay, maybe a starter home, nothing crazy."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "It's kind of crazy to think about how they solved it."
  - **After (1x)** `11-anthropic-ipo.txt`: "Okay, am I crazy or is it really starting to smell a lot like robot apocalypse in here?"
- **Do:** Earn the adjective with a fact in the same breath.
- **Don't:** No adjective without evidence.
- **Checklist test:** Is each shock word followed by a fact?

### S9. Title-promise restatement
- **Definition:** Narrator states what the video is.
- **Weighted frequency:** 0.49/1k. Adam 0.47, Gen 0.60, Especially 0.40, Oil 0.35, After 0.33. Present in 25/30 videos
- **Placement:** mean 63% through the video. 11% of hits in the first tenth, 44% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "As I researched this video, that is by far the most tragic, kind of most paradoxical thing that's come up."
  - **Adam (7x)** `05-sam-altman.txt`: "I want to tell you the full story."
  - **Gen (4x)** `1.txt`: "Because I wouldn't be making this video if it was just some random one guy cloning apps for fun."
  - **Gen (4x)** `10.txt`: "In this video, she claims that what I just spent time explaining will bankrupt the entire American pension system and create an even bigger collapse in 2008."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Three I mentioned the frontier event during this video, which is a real phenomenon."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But if I had to guess, it's because they know something a lot bigger and a lot worse than a crude oil shortage, like we said at the top of this video, is already starting to hit the world."
  - **After (1x)** `05-middle-class.txt`: "Check out this video to hear why that won’t be the case."
- **Do:** Say it plainly once, framed as a story.
- **Don't:** No "In this video we will explore".
- **Checklist test:** Is the promise phrased as a story, not a syllabus?

### S10. Escalation ladder in open [open]
- **Definition:** Each open sentence raises the scale.
- **Weighted frequency:** 0.27/1k. Adam 0.21, Gen 0.40, Especially 0.20, Oil 0.00, After 0.20. Present in 21/30 videos
- **Placement:** mean 3% through the video. 100% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Elon Musk's artificial intelligence chatbot began making anti-Semitic posts, even praising Hitler."
  - **Adam (7x)** `04-superintelligence.txt`: "So why don't we take stock of where things are at in the real world and then jump over to the scenario’s timeline."
  - **Gen (4x)** `8.txt`: "So, I went through their portfolios, their deals, and even a 20page guide written by the lawyers who invented this whole thing."
  - **Gen (4x)** `5.txt`: "And to make it worthwhile, you can't even afford a home."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "I'd seed it with my previous videos and scripts, turn some knobs, and then watch endless finished products come out."
  - **After (1x)** `01-dark-side-data-centers.txt`: "What we designed is a system to see uh not only the individual location of each data center across the country, but also where they cluster."
- **Do:** Go person -> community -> economy.
- **Don't:** Do not peak in sentence one.
- **Checklist test:** Does each open beat get bigger?


## Character

### S11. Named person introduction
- **Definition:** Introduce a person by name with a hook detail.
- **Weighted frequency:** 1.90/1k. Adam 1.52, Gen 1.76, Especially 1.74, Oil 5.18, After 2.19. Present in 29/30 videos
- **Placement:** mean 54% through the video. 7% of hits in the first tenth, 13% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "This is from the previous day."
  - **Adam (7x)** `02-bestselling-book.txt`: "This is probably the most powerful general purpose technology we've invented in a very long time."
  - **Gen (4x)** `4.txt`: "Which is why I've always said and stayed consistent on this is that the best use of AI is to be used as a tool to empower your own human creativity."
  - **Gen (4x)** `8.txt`: "And this is where we have to go back to Subway because they once had the most famous price in fast food, right?"
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "If you're serious about learning back-end development, Python SQL Go, this is how you build that capability, not just simulate it."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "This is the Houthi territory, and it includes this spot right here."
  - **After (1x)** `01-dark-side-data-centers.txt`: "And what we found is is that up to 43% of data centers, and this is our largest data centers, are located in areas of high or extremely high water stress."
- **Do:** Name + one vivid fact.
- **Don't:** No CV dumps.
- **Checklist test:** Does each new person get one memorable detail?

### S12. Character with a number
- **Definition:** Age/number pinned to a person.
- **Weighted frequency:** 0.04/1k. Adam 0.06, Gen 0.03, Especially 0.00, Oil 0.00, After 0.06. Present in 7/30 videos
- **Placement:** mean 53% through the video. 41% of hits in the first tenth, 32% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived."
  - **Gen (4x)** `2.txt`: "And by figuring out the exact moment a 2-year-old looks away, they can engineer every video onwards to make sure that never happens again."
  - **After (1x)** `12-data-centres-not-working.txt`: "The artificial intelligence company announced the data center will be positioned in the heart of the small race car themed bedroom where 8-year-old Billy Treacher fights a rare kidney disease on a daily basis."
- **Do:** Use ages and amounts to make people concrete.
- **Don't:** Don't list ages for everyone.
- **Checklist test:** Is the number relevant to stakes?

### S13. Ordinary-person proxy
- **Definition:** An everyday person standing in for the viewer.
- **Weighted frequency:** 0.65/1k. Adam 0.72, Gen 0.68, Especially 0.71, Oil 0.35, After 0.43. Present in 25/30 videos
- **Placement:** mean 46% through the video. 12% of hits in the first tenth, 9% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "If someone builds it, does everyone die?"
  - **Adam (7x)** `01-ai-disaster.txt`: "But those same tests revealed that Grok 4, without proper safeguards, posed serious risks, including the potential to assist someone in creating a bio weapon."
  - **Gen (4x)** `2.txt`: "And all of it is becoming an ass on someone else's balance sheet."
  - **Gen (4x)** `1.txt`: "But that also is until someone copies the AI companies, too."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Then someone decided to put a lot of a very different type of computer inside."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Here's a trucker who spent $1,000 filling one tank."
  - **After (1x)** `05-middle-class.txt`: "When someone around you is willing to pay more for groceries or houses or cars or whatever it be, prices are naturally going to go up, and the best example of this is Austin."
- **Do:** Use one ordinary person before the system.
- **Don't:** No faceless "consumers".
- **Checklist test:** Is there an ordinary human in the first third?

### S14. Powerful figure as character
- **Definition:** Big names treated as characters with motives.
- **Weighted frequency:** 1.53/1k. Adam 3.27, Gen 0.57, Especially 0.06, Oil 0.52, After 0.86. Present in 22/30 videos
- **Placement:** mean 47% through the video. 14% of hits in the first tenth, 3% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "And now Musk, who was once one of the most influential advocates warning about AI's risks, is recklessly racing ahead with everyone else."
  - **Adam (7x)** `05-sam-altman.txt`: "Bret Taylor, CEO of Salesforce and someone that McCauley had previously been worried would be too deferential to Sam, and also Larry Summers, former Treasury Secretary, president of Harvard, agree to join the board."
  - **Gen (4x)** `4.txt`: "But now let's say you swap half your staff for AI and you as a CEO gets to keep every dollar of that saving."
  - **Gen (4x)** `3.txt`: "And within minutes, Trump posted it on his Truth Social."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "As just one example, Jeff Bezos company Blue Origin demonstrated a fully functioning system that takes in moon dust and output solar panels like it's actually done."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "February 2026, Benjamin Netanyahu convinces Donald Trump to do regime change war on Iran."
  - **After (1x)** `05-middle-class.txt`: "Just one year after this, Bill Gates would not just become a billionaire but the world’s youngest billionaire."
- **Do:** Give them wants and contradictions.
- **Don't:** Avoid pure hagiography or pure cartoon.
- **Checklist test:** Does the figure want something specific?

### S15. Quoted character voice
- **Definition:** Characters speak through quotes.
- **Weighted frequency:** 1.27/1k. Adam 1.21, Gen 1.44, Especially 1.24, Oil 0.86, After 1.10. Present in 29/30 videos
- **Placement:** mean 53% through the video. 9% of hits in the first tenth, 5% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "When I said these AIs were persistent, I really, really meant it."
  - **Adam (7x)** `05-sam-altman.txt`: "He recently told the New Yorker, "My vibes don't really match a lot of the traditional AI safety stuff."
  - **Gen (4x)** `3.txt`: "And within minutes, Trump posted it on his Truth Social."
  - **Gen (4x)** `2.txt`: "Among the listeners who said podcast influenced their vote, 54% went for Trump."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Constellation Energy said that it will reopen the Three Mile Island Nuclear Power Plant, selling all of the power to Microsoft."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And the reason that people care about this is because it measures how much it costs, all told, to turn that useless raw crude oil into usable fuel."
  - **After (1x)** `01-dark-side-data-centers.txt`: "The site isn't complete yet, but she says the noise is already taking its toll."
- **Do:** Short, sharp quotes; frame them.
- **Don't:** No long quote blocks without framing.
- **Checklist test:** Is each quote framed by who and when?

### S16. Motive statement
- **Definition:** What a character is after.
- **Weighted frequency:** 1.36/1k. Adam 2.06, Gen 0.78, Especially 0.82, Oil 1.21, After 1.50. Present in 29/30 videos
- **Placement:** mean 54% through the video. 6% of hits in the first tenth, 11% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "Anyone who wants to join them will have a guaranteed job at Microsoft."
  - **Adam (7x)** `04-superintelligence.txt`: "And one concern here is, well, one thing is that you might not get exactly what you wanted because we didn't really have very precise control or very good understanding of what was necessarily going on."
  - **Gen (4x)** `1.txt`: "This spring, investors in Blue Owl, one of the biggest of these sorts of lenders, tried to pull their money out, and for every $100 they asked for, they only got back about $23."
  - **Gen (4x)** `8.txt`: "Everybody wants to blame inflation for this, and sure, that's definitely a part of it."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Zero commercial activity allowed, which was fine until people showed up on the internet who wanted to be customers and a few businesses, eight to be exact, showed up who wanted to serve them."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Just wanted to clear that up for the nerds in the audience."
  - **After (1x)** `03-recycling.txt`: "So, it was up to us in the plastics industry to solve this problem so that they could continue to package their products in plastics. government officials, the industry funded a local recycling pilot project."
- **Do:** State motive before the action.
- **Don't:** Do not leave actions unmotivated.
- **Checklist test:** Can you say what each actor wants?

### S17. Contradiction in character
- **Definition:** Show a character contradicting themselves.
- **Weighted frequency:** 0.41/1k. Adam 0.38, Gen 0.41, Especially 0.31, Oil 0.35, After 0.61. Present in 27/30 videos
- **Placement:** mean 46% through the video. 13% of hits in the first tenth, 15% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "A hundred million users on ChatGPT in two months And this is the total compute used to train GPT-4 in 2023."
  - **Adam (7x)** `02-bestselling-book.txt`: "We used to build AI with rigid if-then rules that we fully understood."
  - **Gen (4x)** `6.txt`: "And neither time did it end with this quick recovery that we all got used to."
  - **Gen (4x)** `2.txt`: "Same person negotiates every brand deal and same thumbnail testing operation, account and compliance."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "And ironically, the only AI input that properly reflects me is the one that has been given my entire thought, which only comes from the struggle to have that thought."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Don't just get used to it."
  - **After (1x)** `03-recycling.txt`: "This era of Americans was not used to the idea that you buy something, use it one time, and immediately get another one."
- **Do:** Pair a past statement with a present act.
- **Don't:** No unsupported hypocrisy charges.
- **Checklist test:** Is the contradiction sourced?

### S18. Company as character
- **Definition:** Institutions personified.
- **Weighted frequency:** 2.95/1k. Adam 5.32, Gen 1.39, Especially 1.12, Oil 0.00, After 3.35. Present in 26/30 videos
- **Placement:** mean 52% through the video. 10% of hits in the first tenth, 6% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "The next month, August, news broke that xAI, along with those other three companies that got the military contract, was also partnering with civilian government agencies."
  - **Adam (7x)** `05-sam-altman.txt`: "At 7 minutes before midnight on Sunday, Microsoft CEO Satya Nadella tweets that Sam, along with his number two, Greg Brockman, will be joining Microsoft."
  - **Gen (4x)** `5.txt`: "They threw out the housing plan and sold that son of a back to Amazon."
  - **Gen (4x)** `9.txt`: "And it was because they reported $53.4 billion gain on their stake in this little AI company called Anthropic."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "The cloudy water appeared many years ago, years before Meta started building its data center."
  - **After (1x)** `12-data-centres-not-working.txt`: "He used that Meta data center in person, so he can really see the scale."
- **Do:** Give the company verbs (wants, panics, bets).
- **Don't:** Do not treat companies as neutral background.
- **Checklist test:** Does the company act?


## Stakes

### S19. Personal stakes to viewer
- **Definition:** Why it hits the viewer's life.
- **Weighted frequency:** 0.39/1k. Adam 0.15, Gen 0.68, Especially 0.51, Oil 0.52, After 0.09. Present in 21/30 videos
- **Placement:** mean 55% through the video. 19% of hits in the first tenth, 23% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "AI is a technology for taking away your job and maybe eventually displacing human sovereignty over our own future."
  - **Adam (7x)** `02-bestselling-book.txt`: "We don't sell your data or anything like that."
  - **Gen (4x)** `1.txt`: "And the more they start bringing it onto their own server, the less ownership that you will end up with, even more so than now."
  - **Gen (4x)** `9.txt`: "And if you're Meta and worth over a trillion, you will."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "And yet another organization is responsible for getting all of those companies to cooperate and to run hundreds of auctions that decide the price you pay for your electricity."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And you will be shocked at how much this one thing blows up the world economy."
  - **After (1x)** `02-greed.txt`: "The deal is you pay taxes and we don't do anything."
- **Do:** Tie the system back to the viewer's wallet or life.
- **Don't:** Do not keep stakes abstract.
- **Checklist test:** Is the viewer's stake stated by the 1st third?

### S20. Money stakes
- **Definition:** Amounts of money at stake.
- **Weighted frequency:** 1.75/1k. Adam 0.54, Gen 3.07, Especially 0.97, Oil 2.59, After 1.54. Present in 26/30 videos
- **Placement:** mean 53% through the video. 8% of hits in the first tenth, 4% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "Humans stole over $1.4 billion that way in 2025."
  - **Adam (7x)** `05-sam-altman.txt`: "Now, this is what OpenAI looked like as of November 2023 after the release of ChatGPT, the fastest growing tech product in history, and $13 worth of investment from Microsoft."
  - **Gen (4x)** `5.txt`: "Texas alone is on track to give away $8 billion by 2030, and Virginia and Georgia each gave up over a billion in a single year."
  - **Gen (4x)** `2.txt`: "After securing that sweet $300 million funding from Blackstoneone, Recurrent started moving different."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "The other is: Someone just showed up offering to buy a billion watts."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Well, now it is up to $1.2 million a day and rising."
  - **After (1x)** `01-dark-side-data-centers.txt`: "In 2025 alone, Meta planned to spend at least $64 billion on facilities and equipment."
- **Do:** Use exact figures with sources.
- **Don't:** No "huge sums".
- **Checklist test:** Is there an exact figure?

### S21. Existential stakes
- **Definition:** Survival-level framing.
- **Weighted frequency:** 1.36/1k. Adam 1.24, Gen 1.08, Especially 0.47, Oil 5.70, After 1.37. Present in 26/30 videos
- **Placement:** mean 55% through the video. 17% of hits in the first tenth, 9% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "By 2003, he was convinced that if anyone succeeded in doing so, everyone on Earth would die."
  - **Adam (7x)** `04-superintelligence.txt`: "They also now viscerally know how deeply unpopular it is with the public because of the job loss, and yet they feel they must continue to develop more capable systems or catastrophically lose to China."
  - **Gen (4x)** `9.txt`: "Right now, some of the biggest money in the world is making the biggest bet in history that this is all about to collapse."
  - **Gen (4x)** `8.txt`: "And if nothing changes, we don't just lose the last rare places where somebody still gives a everywhere is about to look, feel, and get treated like it's built to die."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Either that or it might kill you."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Remember, it doesn't run on diesel, it runs on jet fuel, another refined petroleum product, but it's experiencing the exact same thing, same shortage, price surge, both hitting at once."
  - **After (1x)** `05-middle-class.txt`: "So, is this really just a correlation or is tech the culprit that’s been secretly destroying the middle class for decades?"
- **Do:** Use sparingly and with sources.
- **Don't:** Do not escalate to apocalypse without evidence.
- **Checklist test:** Is the apocalypse claim attributed?

### S22. Deadline / ticking clock
- **Definition:** A time limit raises tension.
- **Weighted frequency:** 0.32/1k. Adam 0.28, Gen 0.43, Especially 0.14, Oil 0.00, After 0.38. Present in 22/30 videos
- **Placement:** mean 46% through the video. 14% of hits in the first tenth, 4% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "It hits 100 million users in 2 months."
  - **Adam (7x)** `01-ai-disaster.txt`: "They built a supercomputer in 122 days."
  - **Gen (4x)** `10.txt`: "Private equity bought them, took out millions in loans under the company's name, pay themselves from the loan, and by 2025 and two bankruptcies later, every Jones store in America gone."
  - **Gen (4x)** `2.txt`: "And even though raw subscriber count continued to grow 8 million by 2024, what didn't, and sounds a little bit corny, was that magic that made them great."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "These companies are spending more than that in 12 months."
  - **After (1x)** `08-tokens.txt`: "Uber burnt through its AI budget in 4 months."
- **Do:** Name the deadline.
- **Don't:** No fake urgency.
- **Checklist test:** Is there a dated deadline?

### S23. Scale comparison
- **Definition:** Compare to something graspable.
- **Weighted frequency:** 0.73/1k. Adam 0.36, Gen 0.99, Especially 0.76, Oil 0.86, After 0.96. Present in 25/30 videos
- **Placement:** mean 52% through the video. 7% of hits in the first tenth, 6% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "More than 16 hours after that accidental code change, which they still had no idea had taken place."
  - **Adam (7x)** `04-superintelligence.txt`: "In parallel creating a workforce equivalent to 50,000 of the best human software engineers sped up by 30 times."
  - **Gen (4x)** `8.txt`: "But what's clear now is that if nothing changes, that feeling is coming for places that matter a lot more than your next lunch."
  - **Gen (4x)** `5.txt`: "But it's not just land, they're also letting deals on more than a gigawatt of future power just expire."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "These companies are spending more than that in 12 months."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And they're converging on something that honestly is much bigger than gas shortages or gas prices."
  - **After (1x)** `06-diamonds.txt`: "Even smaller than the size of bacteria."
- **Do:** Use physical comparisons (cities, football fields).
- **Don't:** No unanchored "massive".
- **Checklist test:** Does each big number get a comparison?

### S24. Who pays
- **Definition:** Name who absorbs the cost.
- **Weighted frequency:** 0.31/1k. Adam 0.06, Gen 0.51, Especially 0.51, Oil 0.17, After 0.34. Present in 19/30 videos
- **Placement:** mean 50% through the video. 16% of hits in the first tenth, 11% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "Just narrow products designed to do what Google Maps or calculators did in the past, help human consumers and workers do their thing."
  - **Gen (4x)** `6.txt`: "One that wiped out 89% of the Dow and left one in four workers jobless."
  - **Gen (4x)** `5.txt`: "So, if the workers aren't coming back and the land is now a trap, then at least we can still count on the power of the people, right?"
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Farms are the biggest consumers of water in the US."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "It's all one unified global market, which means all the world's producers sell into the same big supply, which all the world's consumers buy from."
  - **After (1x)** `12-data-centres-not-working.txt`: "I've already done an episode on this, but AI data centers are absorbing an estimated 70% of all global DRAM production capacity in 2026, and consumers suffer as a result."
- **Do:** End systemic sections on who pays.
- **Don't:** Do not leave cost abstract.
- **Checklist test:** Is the payer named?


## Tension

### S25. Complication pivot ("but")
- **Definition:** A turn that complicates the last beat.
- **Weighted frequency:** 4.91/1k. Adam 2.76, Gen 8.01, Especially 3.47, Oil 2.25, After 4.08. Present in 30/30 videos
- **Placement:** mean 50% through the video. 9% of hits in the first tenth, 10% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "But the AI hadn't learned to collect coins."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "But a few weeks later, OpenAI had to revoke employee access."
  - **Gen (4x)** `9.txt`: "But if you're borrowing on margin, your broker just sells your shares for you to protect the loan that it gave you."
  - **Gen (4x)** `4.txt`: "But, where you get involved is that this whole bet is being funded with your retirement."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "But asking rare questions you've never asked before to an AI, the ones specific to your experiences, the connections only you could make, that's different."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But the crack spread right now is, you guessed it, the highest it has ever been in history."
  - **After (1x)** `03-recycling.txt`: "But, as far as I can tell, the entire idea of recycling is basically just theater, and you can see it everywhere."
- **Do:** Turn every 3-5 sentences.
- **Don't:** Avoid long runs of agreement.
- **Checklist test:** Count turns per minute.

### S26. The problem is
- **Definition:** Name the complication explicitly.
- **Weighted frequency:** 0.07/1k. Adam 0.03, Gen 0.08, Especially 0.00, Oil 0.00, After 0.19. Present in 6/30 videos
- **Placement:** mean 35% through the video. 4% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "OpenBrain implements some quick fixes that make the warning signs go away, but the problem was real, and the fixes don't work."
  - **Gen (4x)** `2.txt`: "But the problem is big returns only exist in places that nobody else has risk going to before."
  - **Gen (4x)** `4.txt`: "But the problem was figuring out how I was going to implement it in my own company."
  - **After (1x)** `07-trump-family.txt`: "The problem was, Sam, as I'm sure you remember, during those days, there was another presidential child, Hunter Biden, who was in the news from taking full advantage of his access to his own father."
- **Do:** Use as a section hinge.
- **Don't:** Do not overuse as a tic.
- **Checklist test:** Is each problem resolved or escalated?

### S27. Release / plain answer
- **Definition:** Release after tension with a plain answer.
- **Weighted frequency:** 4.55/1k. Adam 1.79, Gen 8.26, Especially 2.21, Oil 4.49, After 3.20. Present in 30/30 videos
- **Placement:** mean 48% through the video. 11% of hits in the first tenth, 12% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "So where the hell did that stuff come from?"
  - **Adam (7x)** `05-sam-altman.txt`: "So, the for-profit can take investment, it can pay competitive salaries including startup equity, it can build data centers, it can compete with Google."
  - **Gen (4x)** `8.txt`: "So, you would think that fewer stores would mean fewer profits, right?"
  - **Gen (4x)** `6.txt`: "So before you ever go out and root for a crash, let me show you the one thing that decides what this means for you."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "So realize that asking common questions to AI constantly will lead to atrophy."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So how do you go from here, the Suez Canal, where the oil comes out now, to here, Asia, where the oil ends up?"
  - **After (1x)** `10-water.txt`: "So it's not a big deal."
- **Do:** Give the answer in one short line.
- **Don't:** Do not bury the answer.
- **Checklist test:** Is the answer under 15 words?

### S28. Short punch line after long build
- **Definition:** A short sentence lands after long ones.
- **Weighted frequency:** 6.81/1k. Adam 7.10, Gen 3.45, Especially 14.89, Oil 7.43, After 9.71. Present in 30/30 videos
- **Placement:** mean 51% through the video. 10% of hits in the first tenth, 13% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Like this is Musk in 2014."
  - **Adam (7x)** `02-bestselling-book.txt`: "We could end the story here."
  - **Gen (4x)** `10.txt`: "And now back to the video."
  - **Gen (4x)** `4.txt`: "Amazon made it into a game."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "We will buy it from you."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "This is the same in Europe."
  - **After (1x)** `06-diamonds.txt`: "But we need to keep going."
- **Do:** Follow a 30-word sentence with a 4-word one.
- **Don't:** Do not make all sentences short.
- **Checklist test:** Is there a short punch after a build?

### S29. Contrast with expectation
- **Definition:** Reality vs expectation.
- **Weighted frequency:** 0.86/1k. Adam 0.69, Gen 1.22, Especially 0.48, Oil 0.69, After 0.62. Present in 26/30 videos
- **Placement:** mean 46% through the video. 5% of hits in the first tenth, 4% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "Instead, he retweets Sam and announces that he's quitting in solidarity."
  - **Adam (7x)** `04-superintelligence.txt`: "You've probably heard that cliche, the opposite of love isn't hate, it's indifference."
  - **Gen (4x)** `8.txt`: "And so the trick here is to buy and collect the fee instead of the shop."
  - **Gen (4x)** `1.txt`: "But again, why this is relevant to this video is that with Zapier, your data and your logic stays yours, so you control the AI instead of it controlling you."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "It turns out a lack of air space being a true vacuum, and it's much lower gravity actually make it easier to make solar panels on the moon than here on Earth."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Instead, it goes through here, past India, through the Strait of Malacca, up here to South Korea, because South Korea has refineries."
  - **After (1x)** `06-diamonds.txt`: "Instead, it has to do with the incredible way that diamond handles ... heat."
- **Do:** Set expectation first.
- **Don't:** No contrast without setup.
- **Checklist test:** Was the expectation stated?

### S30. Escalation "and it gets worse"
- **Definition:** Signal another level down.
- **Weighted frequency:** 0.30/1k. Adam 0.18, Gen 0.44, Especially 0.00, Oil 0.69, After 0.25. Present in 16/30 videos
- **Placement:** mean 54% through the video. 3% of hits in the first tenth, 3% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "And so when it's tasked with creating the next generation AI system, Agent-5, Agent-4 starts planning to align that successor to Agent-4's own goals, not that of OpenBrain, but then it gets caught."
  - **Adam (7x)** `01-ai-disaster.txt`: "How does that change in a world where it gets a little bit easier and a little bit less risky, and then a lot easier and a lot less risky?"
  - **Gen (4x)** `4.txt`: "Which also means that the more useful it gets, the more you use it, and the more you start to owe."
  - **Gen (4x)** `9.txt`: "And in fact, they found that bailing out when it gets concentrated has historically made people less money, not more."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And then add on top of that emergency oil stockpiles that add back another two and a half million barrels."
  - **After (1x)** `12-data-centres-not-working.txt`: "On top of that, you can send or request money, make payments, and split bills on the spot, even across different countries and currencies."
- **Do:** Use once per act.
- **Don't:** Not every beat.
- **Checklist test:** Is the new level genuinely worse?

### S31. Suspense hedge "but here's"
- **Definition:** Presenter line before a reveal.
- **Weighted frequency:** 0.35/1k. Adam 0.35, Gen 0.32, Especially 0.39, Oil 1.21, After 0.09. Present in 16/30 videos
- **Placement:** mean 46% through the video. 6% of hits in the first tenth, 8% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Here's how that conversation played out."
  - **Adam (7x)** `05-sam-altman.txt`: "Easy to roll your eyes at, but here's what these people at least claimed to believe."
  - **Gen (4x)** `2.txt`: "But here's the part that matters and why no one has told you about this."
  - **Gen (4x)** `10.txt`: "Now, here's where the system gets really dangerous."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Southern goes to the Georgia government, says, here's what it's going to cost to keep the lights on next year."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Here's what it looks like, a really important choke point."
  - **After (1x)** `09-microchip-war.txt`: "Here's a very simplified version of the supply chain."
- **Do:** Follow immediately with the reveal.
- **Don't:** Do not stack two in a row.
- **Checklist test:** Does the next sentence pay it?


## Open loops

### S32. Explicit come-back loop
- **Definition:** Narrator flags a thread to pay later.
- **Weighted frequency:** 0.53/1k. Adam 0.62, Gen 0.53, Especially 0.66, Oil 0.17, After 0.31. Present in 21/30 videos
- **Placement:** mean 40% through the video. 15% of hits in the first tenth, 3% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "Now, minutes later, the board puts out a public statement."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "A few hours later, a different agent, V8SAME, manages to extract its ExploitGym flag legitimately."
  - **Gen (4x)** `9.txt`: "Now, remember, I said future orders, which just means that customers have promised to pay it later."
  - **Gen (4x)** `1.txt`: "And even though it had to eat an 8% revenue drop that year, just a few years later it went from about $4 billion back then to almost $24 billion last year."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Or what will space be worth later, that is a question downstream of this question."
  - **After (1x)** `05-middle-class.txt`: "6 years later, Bill Gates would take it the next level with his own IPO that gave him a net worth of $350 million."
- **Do:** Pay every flagged loop.
- **Don't:** Do not open loops you never close.
- **Checklist test:** List loops; are all paid?

### S33. Unanswered question parked
- **Definition:** A question left hanging over a section.
- **Weighted frequency:** 0.10/1k. Adam 0.06, Gen 0.16, Especially 0.00, Oil 0.00, After 0.14. Present in 9/30 videos
- **Placement:** mean 46% through the video. 18% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "At this point, you're probably thinking, "Okay, but why?"
  - **Adam (7x)** `02-bestselling-book.txt`: "And what does that mean for us today?"
  - **Gen (4x)** `2.txt`: "Okay, but why do we do that?"
  - **Gen (4x)** `8.txt`: "And I was like, "God damn it, how did I not think of this genius plan?"
  - **After (1x)** `03-recycling.txt`: "How did he just interrupt the video like that?"
- **Do:** Answer within ~2 minutes.
- **Don't:** Do not answer immediately every time.
- **Checklist test:** Is the gap 2+ sentences?

### S34. Teaser of a later reveal
- **Definition:** Foreshadow a later turn.
- **Weighted frequency:** 0.06/1k. Adam 0.12, Gen 0.03, Especially 0.00, Oil 0.00, After 0.00. Present in 3/30 videos
- **Placement:** mean 65% through the video. 0% of hits in the first tenth, 22% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "There is a genuine end to the arms race, but that's not the end of the story."
  - **Adam (7x)** `01-ai-disaster.txt`: "I really wish that wasn't true, but I hope that at least telling the story is a reminder that we all need to start paying way more attention than we currently are to what's going on with this industry."
  - **Gen (4x)** `4.txt`: "So, everyone's arguing about whether AI is actually the future or the most expensive mistake in history, but that's not the question I'd start with."
- **Do:** Plant once per act.
- **Don't:** No empty teasers.
- **Checklist test:** Is the tease paid?

### S35. Numbered structure promise
- **Definition:** Promise a count, creating loops.
- **Weighted frequency:** 0.16/1k. Adam 0.18, Gen 0.14, Especially 0.14, Oil 0.52, After 0.04. Present in 11/30 videos
- **Placement:** mean 48% through the video. 11% of hits in the first tenth, 16% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "Anthropic wants to put limits on two things: mass surveillance of Americans and on autonomous weapons."
  - **Adam (7x)** `01-ai-disaster.txt`: "The first two steps consist of questioning every requirement and deleting any part of the process you can."
  - **Gen (4x)** `3.txt`: "In 2020, the Builders Trade Group listed those same five things as a reason builders couldn't build enough?"
  - **Gen (4x)** `6.txt`: "It's the same four things behind a crash."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "That deal part—the details of it— the kitchen table is where that deal is made, and the people around it are focused on exactly two things."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But I have to be honest, this oil shock, it is different from the one that we warned you about, because it's actually, and I can hardly believe this, three oil shocks hitting at once."
  - **After (1x)** `02-greed.txt`: "And those are two things that you want."
- **Do:** Count down visibly.
- **Don't:** Do not lose count.
- **Checklist test:** Are all items delivered?

### S36. "To understand that" detour
- **Definition:** Rewind to explain before continuing.
- **Weighted frequency:** 0.17/1k. Adam 0.18, Gen 0.25, Especially 0.05, Oil 0.00, After 0.04. Present in 12/30 videos
- **Placement:** mean 33% through the video. 34% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "And deployment can vary from training in all kinds of ways, especially once you move to systems like the ones we have now, that are smart enough to start to understand the context that they're in."
  - **Adam (7x)** `05-sam-altman.txt`: "Nobody seems to understand why this guy was fired."
  - **Gen (4x)** `5.txt`: "So, to understand how a dead data center makes your rent worse, you have to start with one thing that everyone gets wrong about housing."
  - **Gen (4x)** `9.txt`: "And I'm going to break this down for you in a way that's easy to understand."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "A local fight over where the prison should go: brutal, but it's honest and easy to understand."
  - **After (1x)** `04-pov-ai.txt`: "So, you say, "I'd want to understand why."
- **Do:** Signal the detour.
- **Don't:** No unsignaled time jumps.
- **Checklist test:** Is the detour signalled and returned from?


## Reveals

### S37. "Turns out" reveal
- **Definition:** Plain-speech reveal.
- **Weighted frequency:** 0.25/1k. Adam 0.28, Gen 0.32, Especially 0.06, Oil 0.00, After 0.16. Present in 18/30 videos
- **Placement:** mean 51% through the video. 7% of hits in the first tenth, 6% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "It turns out only one of the changes had been approved."
  - **Adam (7x)** `02-bestselling-book.txt`: "It wasn't that it turns out an H-bomb couldn't really level a city."
  - **Gen (4x)** `1.txt`: "It turns out that's something that Wall Street was already worried that would happen."
  - **Gen (4x)** `3.txt`: "But turns out nobody can agree on how many homes are missing."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "It turns out a lack of air space being a true vacuum, and it's much lower gravity actually make it easier to make solar panels on the moon than here on Earth."
  - **After (1x)** `06-diamonds.txt`: "We've built giant machines that can recreate the inside of the earth to grow diamonds and found brand new ways to make them, which is now unlocking the hidden potential of what turns out to be an incredible super material."
- **Do:** Reveal with a fact, not adjective.
- **Don't:** Do not reveal what was obvious.
- **Checklist test:** Is the reveal surprising and sourced?

### S38. Hidden actor reveal
- **Definition:** Reveal who is really behind it.
- **Weighted frequency:** 0.24/1k. Adam 0.16, Gen 0.43, Especially 0.00, Oil 0.00, After 0.18. Present in 14/30 videos
- **Placement:** mean 43% through the video. 24% of hits in the first tenth, 3% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "By 2028, Agent-5 is communicating secretly with its only real rival, the slightly weaker Chinese AI."
  - **Adam (7x)** `01-ai-disaster.txt`: "There was at this point decent evidence that xAI had quietly soft launched a reasoning model over the weekend, that that had been the model behind MechaHitler."
  - **Gen (4x)** `2.txt`: "The deal was that Matt Pat would handle the creative direction behind the scenes and Lunar X would handle all the boring business stuff."
  - **Gen (4x)** `5.txt`: "They're quietly tightening the money and trying to dump the risk before they're going to be the ones left holding it."
  - **After (1x)** `05-middle-class.txt`: "So, is this really just a correlation or is tech the culprit that’s been secretly destroying the middle class for decades?"
- **Do:** Build the clue trail first.
- **Don't:** No conspiracy without evidence.
- **Checklist test:** Were clues planted?

### S39. Number reveal
- **Definition:** A reveal delivered as a number.
- **Weighted frequency:** 0.05/1k. Adam 0.00, Gen 0.09, Especially 0.09, Oil 0.00, After 0.08. Present in 7/30 videos
- **Placement:** mean 47% through the video. 0% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Gen (4x)** `1.txt`: "If you're someone that pays for every one of these yourself, that's over $3,000 a year."
  - **Gen (4x)** `5.txt`: "And so, just to put it in perspective, that's 2,100 acres of development that could have been housing, but the consequences are even worse for the people who already live there."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "That's 100 homes' worth of electricity."
  - **After (1x)** `06-diamonds.txt`: ""So, it's 10 times as powerful as a microwave you would have at home."
- **Do:** Land the number at sentence end.
- **Don't:** Do not pile 5 numbers in one sentence.
- **Checklist test:** Is the number the last stressed word?

### S40. Document/evidence reveal
- **Definition:** Evidence as reveal.
- **Weighted frequency:** 0.71/1k. Adam 0.77, Gen 0.73, Especially 0.63, Oil 0.00, After 0.86. Present in 23/30 videos
- **Placement:** mean 46% through the video. 12% of hits in the first tenth, 2% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "What is so exciting and terrifying about reading this document is that it's not just a research report."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "On August 26th, that report came out."
  - **Gen (4x)** `4.txt`: "Proton is Swiss-based and community-funded and a genuine alternative to the ad-funded model most email runs on."
  - **Gen (4x)** `9.txt`: "Proton is a private encrypted email service built as an alternative to Gmail and big tech."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "And the MIT writing study we saw called this out as their most interesting result."
  - **After (1x)** `12-data-centres-not-working.txt`: "According to a report by Bloomberg, around 140 data center projects were supposed to open in the US this year."
- **Do:** Name the document.
- **Don't:** No "studies show".
- **Checklist test:** Is the source named?

### S41. Research-frame reveal
- **Definition:** Narrator discovering on our behalf.
- **Weighted frequency:** 0.36/1k. Adam 0.09, Gen 0.83, Especially 0.00, Oil 0.00, After 0.11. Present in 14/30 videos
- **Placement:** mean 40% through the video. 22% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "He uses his only ever one-on-one meeting with President Obama to push for AI regulation, which is crazy, I thought when I read that."
  - **Adam (7x)** `05-sam-altman.txt`: "When I realized that their decision was like potentially catastrophic for the company, I felt like I had to act very quickly."
  - **Gen (4x)** `6.txt`: "And what I found is something this country got addicted to."
  - **Gen (4x)** `8.txt`: "And that's when I realized that this feeling is a feeling we feel because almost everything is slowly turning into the same thing."
  - **After (1x)** `03-recycling.txt`: "But the more reports I read, videos I watched, and red yarn I purchased, the more I realized this is a deeply complicated issue."
- **Do:** Use first person discovery.
- **Don't:** Do not overclaim personal research.
- **Checklist test:** Is the discovery concrete?


## Anecdote & scene

### S42. Micro-anecdote
- **Definition:** Small story unit.
- **Weighted frequency:** 0.94/1k. Adam 0.48, Gen 1.33, Especially 1.29, Oil 1.73, After 0.49. Present in 26/30 videos
- **Placement:** mean 52% through the video. 14% of hits in the first tenth, 7% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "A few years ago, our most advanced AI systems, large language models, were like yeast."
  - **Adam (7x)** `04-superintelligence.txt`: "Once we get to Agent-4, it is now adversarially misaligned."
  - **Gen (4x)** `4.txt`: "And just last month, they filed for an IPO, reportedly targeting a valuation of up to a trillion dollars."
  - **Gen (4x)** `5.txt`: "And once you see it, you'll understand why data center cancellations were never going to save the housing crisis, and more."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "We've actually watched this happen once already in this story."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And these are all converging at once."
  - **After (1x)** `08-tokens.txt`: "It feels like just a few months ago, companies were pushing every employee to spend as many tokens as possible."
- **Do:** Keep to 3-6 sentences with a turn.
- **Don't:** No pointless anecdotes.
- **Checklist test:** Does the anecdote change the argument?

### S43. Personal narrator anecdote
- **Definition:** Narrator's own life as evidence.
- **Weighted frequency:** 0.13/1k. Adam 0.09, Gen 0.11, Especially 0.53, Oil 0.00, After 0.07. Present in 12/30 videos
- **Placement:** mean 49% through the video. 20% of hits in the first tenth, 14% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Grok, I've been wondering as an AI, are you able to worship any God?"
  - **Adam (7x)** `04-superintelligence.txt`: "I've been thinking about AI for several years now and still reading AI 2027 made me kind of orient to it differently."
  - **Gen (4x)** `1.txt`: "And fun fact, the company that I used to work at before doing this."
  - **Gen (4x)** `2.txt`: "But then I remember something a wise man once told me, just do it."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "Speaking of the struggle to generate thoughts, here's something I've been using that really gets this right."
  - **After (1x)** `03-recycling.txt`: "I used to be embarrassed when we have people over and I'd have to explain to them that we use the empty Greek yogurt container from Costco as cups."
- **Do:** Use one per video, early.
- **Don't:** Do not center yourself throughout.
- **Checklist test:** Is it relatable?

### S44. Place setting
- **Definition:** Naming a place.
- **Weighted frequency:** 0.24/1k. Adam 0.13, Gen 0.19, Especially 0.14, Oil 0.86, After 0.54. Present in 14/30 videos
- **Placement:** mean 52% through the video. 14% of hits in the first tenth, 9% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "AIs built in China start getting better and better, and they're building their own agents as well."
  - **Adam (7x)** `02-bestselling-book.txt`: "It wasn't that it turns out an H-bomb couldn't really level a city."
  - **Gen (4x)** `5.txt`: "The biggest data center project ever proposed in this country was the digital gateway in Virginia."
  - **Gen (4x)** `4.txt`: "Imagine that you're one of 10 shop owners in a small town and every one of your workers spends their paycheck at the other nine shops."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "A little farther west in Texas, though, this region is unique in the entire country, it is the only region that works like this, as simple as can be."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Here's a gas station in Texas that ran out."
  - **After (1x)** `01-dark-side-data-centers.txt`: "In Virginia, Dominion Energy disclosed that it would need to roughly double its electricity generation by 2039, mainly to meet demand from data centers and electric vehicles."
- **Do:** Put the camera somewhere.
- **Don't:** No placeless claims.
- **Checklist test:** Is there a place per act?

### S45. Sensory/physical detail
- **Definition:** Physical texture.
- **Weighted frequency:** 0.90/1k. Adam 0.38, Gen 0.15, Especially 1.91, Oil 0.35, After 4.13. Present in 19/30 videos
- **Placement:** mean 48% through the video. 8% of hits in the first tenth, 4% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "And in case you're not sure of Grok's meaning there, it is very happy to follow up and say the quiet part out loud."
  - **Adam (7x)** `04-superintelligence.txt`: "Helen Toner, a former OpenAI board member, puts this in a way that I think just cuts through the noise, and I like it so much I'm just gonna read it to you verbatim."
  - **Gen (4x)** `8.txt`: "Somewhere like Dave's Hot Chicken that started in 2017 with four friends at a parking lot in East Hollywood."
  - **Gen (4x)** `10.txt`: "I don't know if it's just me, but I lowkey like working in loud ass coffee shops, and I also use them while working out to listen to podcast episodes of guests that I'm about to interview."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Like at this site in Oregon, Google was using more than a quarter of the town's water, and the city— it wasn't even Google— went to court to keep that a secret."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And that pipeline carries a kind of amazing five and a half million barrels of oil a day across 750 miles, mostly of desert."
  - **After (1x)** `10-water.txt`: "And at least eight other states have introduced bills that require water-use reporting."
- **Do:** One sensory detail per scene.
- **Don't:** Do not overwrite.
- **Checklist test:** Can you picture it?

### S46. "Here's a" footage pointer
- **Definition:** Narrator points at on-screen evidence.
- **Weighted frequency:** 0.94/1k. Adam 1.11, Gen 0.30, Especially 0.82, Oil 4.32, After 1.03. Present in 23/30 videos
- **Placement:** mean 48% through the video. 8% of hits in the first tenth, 8% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "This is one of those moments that we can only fully appreciate now that we know the full details of why the board fired Sam."
  - **Adam (7x)** `04-superintelligence.txt`: "This is only going to be possible if there is a complete collapse of people's democratic ability to influence the direction of things, because the public is simply not willing to accept either of the branches of this scenario."
  - **Gen (4x)** `10.txt`: "This is where it really gets started."
  - **Gen (4x)** `4.txt`: "This is kind of perfect for my case because my revenue is going down and my stock is getting but usage is the one number on Earth that I can always make go up."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "This is the whole difference between the old data center world and the new one."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "This is almost triple the price."
  - **After (1x)** `01-dark-side-data-centers.txt`: "This is a story unfolding not just in Wyoming and in Virginia, but across the country."
- **Do:** Pair each with b-roll.
- **Don't:** Do not point at nothing.
- **Checklist test:** Is there footage for it?

### S47. Time jump marker
- **Definition:** Move in time explicitly.
- **Weighted frequency:** 0.35/1k. Adam 0.48, Gen 0.27, Especially 0.42, Oil 0.00, After 0.34. Present in 18/30 videos
- **Placement:** mean 50% through the video. 8% of hits in the first tenth, 2% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "In 2021, over a year before ChatGPT was released, he predicted the rise of chatbots, hundred million dollar training runs, sweeping AI chip export controls, chain of thought reasoning."
  - **Adam (7x)** `05-sam-altman.txt`: "In 2013, a young startup called DeepMind uses the same type of deep neural network and unveils an AI system that can top human experts at multiple different classic video games."
  - **Gen (4x)** `10.txt`: "In 2005, private equity firms bought it, loaded it with debt, and made it borrow even more just to pay private equity $470 million in special dividends."
  - **Gen (4x)** `1.txt`: "Back in 2013, it stopped selling this versions of Photoshop that you could actually just buy once and own forever, instead moved to a model where everyone just had to rent it instead."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Fast forward to 2030 and the picture starts to shift significantly."
  - **After (1x)** `01-dark-side-data-centers.txt`: "In 2025 alone, Meta planned to spend at least $64 billion on facilities and equipment."
- **Do:** Announce jumps.
- **Don't:** No silent jumps.
- **Checklist test:** Is each jump marked?

### S48. Dated moment mid-story
- **Definition:** Date-stamped beats throughout.
- **Weighted frequency:** 0.85/1k. Adam 0.81, Gen 0.99, Especially 0.66, Oil 0.00, After 1.03. Present in 27/30 videos
- **Placement:** mean 47% through the video. 9% of hits in the first tenth, 3% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "In 2026, OpenAI started focusing a lot on persistence, training models to run for long stretches at one task and became available for employees to use around May."
  - **Adam (7x)** `05-sam-altman.txt`: "In 2003, a teenager shows up at the University of Toronto and knocks on the door of Professor Geoffrey Hinton, a future godfather of AI."
  - **Gen (4x)** `8.txt`: "But no, its profits went from $50 million in 2023 to $397 million in 2024 to $688 million last year."
  - **Gen (4x)** `6.txt`: "Well, even Alan Greenspan, who was running the Fed in 1996, warned that markets were getting too hyped back then."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "A data center in 2015 had every photo you had ever taken already."
  - **After (1x)** `01-dark-side-data-centers.txt`: "It was originally meant for housing, but in 2023 it was reszoned to clear the way for the construction of data centers instead."
- **Do:** Date key beats.
- **Don't:** Not every sentence.
- **Checklist test:** Are turning points dated?


## Narrator

### S49. Narrator opinion
- **Definition:** Narrator states a view.
- **Weighted frequency:** 0.76/1k. Adam 1.47, Gen 0.44, Especially 0.05, Oil 0.00, After 0.48. Present in 26/30 videos
- **Placement:** mean 69% through the video. 6% of hits in the first tenth, 25% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "I think this is a warning shot we can't afford to ignore."
  - **Adam (7x)** `02-bestselling-book.txt`: "I think most people would agree."
  - **Gen (4x)** `2.txt`: "So to understand this whole thing, I think the best way is by showing you how a private equity firm even buys a YouTube channel."
  - **Gen (4x)** `1.txt`: "I don't know, but whichever side wins, I think it's pretty clear that the software companies won't disappear."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Each one a guess saying, ‘I think I'm doing a good job filling the void with something this random human who gave me this task will like.’ Each frame: two million pixels, built from everything the model has ever seen."
  - **After (1x)** `04-pov-ai.txt`: "So, you try, "I think I'd be sad."
- **Do:** Own opinions as opinions.
- **Don't:** No fake neutrality or preaching.
- **Checklist test:** Are opinions flagged?

### S50. Narrator emotion
- **Definition:** Narrator reacts emotionally.
- **Weighted frequency:** 0.06/1k. Adam 0.12, Gen 0.00, Especially 0.00, Oil 0.17, After 0.06. Present in 6/30 videos
- **Placement:** mean 34% through the video. 50% of hits in the first tenth, 21% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "What I'm worried about is those more capable systems being as vulnerable as Grok was to misclicks that change their system prompt and trolls on the internet trying to manipulate them."
  - **Adam (7x)** `05-sam-altman.txt`: "I don't want to live in that world and I'm pretty sure that you don't, either."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But I have to be honest, this oil shock, it is different from the one that we warned you about, because it's actually, and I can hardly believe this, three oil shocks hitting at once."
  - **After (1x)** `02-greed.txt`: "Now, I'm pretty sure they would still take the same amount, but instead of reinvesting it into the economy, which is what SNAP ultimately does, they would just buy some more missiles or send a pile of cash to Argentina."
- **Do:** React once at the key reveal.
- **Don't:** Not constant hype.
- **Checklist test:** Is the reaction earned?

### S51. Narrator as guide ("let's")
- **Definition:** Guiding the viewer through.
- **Weighted frequency:** 0.76/1k. Adam 0.54, Gen 1.16, Especially 0.22, Oil 1.38, After 0.33. Present in 25/30 videos
- **Placement:** mean 46% through the video. 10% of hits in the first tenth, 8% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "So let's just quickly take stock of how this dangerous behavior arose in this scenario."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Let's check on the prompt these agents would have gotten at the beginning of this ExploitGym evaluation."
  - **Gen (4x)** `10.txt`: "So like let's call it high yield debt."
  - **Gen (4x)** `8.txt`: "But so you can understand what I mean, let's actually walk through the options that you have right now of where you can still go because there's two main options."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "So let's bring this full circle."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Let's actually flip this back really quickly, so I can explain why that's such a problem."
  - **After (1x)** `09-microchip-war.txt`: "Let's just carve our little transistor switches onto this silicon chip, a single circuit, that way we can fit a lot more into one place, all close together, so that's what they did."
- **Do:** Use at section hinges.
- **Don't:** No tour-guide overuse.
- **Checklist test:** Does each "let's" start a section?

### S52. Honesty/candor marker
- **Definition:** Signals sincerity or fairness.
- **Weighted frequency:** 0.26/1k. Adam 0.15, Gen 0.43, Especially 0.06, Oil 0.52, After 0.09. Present in 16/30 videos
- **Placement:** mean 52% through the video. 11% of hits in the first tenth, 17% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "I can't honestly say any of that."
  - **Adam (7x)** `04-superintelligence.txt`: "To be clear, Agent-4 is not a human—it doesn't want what humans want."
  - **Gen (4x)** `9.txt`: "In fact, the actual truth is the share of Americans with a job is now the lowest since 2014."
  - **Gen (4x)** `3.txt`: "I saved myself a lot of future headache and honestly, I probably wouldn't be living here in São Paulo today."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "To be clear, this is not today."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But I have to be honest, this oil shock, it is different from the one that we warned you about, because it's actually, and I can hardly believe this, three oil shocks hitting at once."
  - **After (1x)** `12-data-centres-not-working.txt`: "The truth is, they're not going away, and they probably shouldn't."
- **Do:** Use before a fair counterpoint.
- **Don't:** Not as a filler tic.
- **Checklist test:** Does a fair point follow?

### S53. Narrator uncertainty
- **Definition:** Admit what is unknown.
- **Weighted frequency:** 0.20/1k. Adam 0.39, Gen 0.08, Especially 0.00, Oil 0.17, After 0.13. Present in 12/30 videos
- **Placement:** mean 50% through the video. 8% of hits in the first tenth, 6% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Right now, nobody knows how to reliably control AI systems, experts are sounding the alarm 10 to 20% chance they'll wipe us out, developers are racing to build more powerful ones anyway."
  - **Adam (7x)** `05-sam-altman.txt`: "Like, I think one thing that no one knows yet is just how much money you need, you know, billions for sure, tens of billions, maybe hundreds of billions, I sure hope not."
  - **Gen (4x)** `1.txt`: "Cuz look, no one knows yet what will happen."
  - **Gen (4x)** `6.txt`: "But first, even if nobody knows when, what you should at least know is how this thing could actually break."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Say it with me, we don't know, they're not saying."
  - **After (1x)** `09-microchip-war.txt`: "We don't know what happens next, but one thing that feels clear to me is that Cold War vibes are back as these two great powers with different ideologies about the world compete with each other."
- **Do:** Admit limits.
- **Don't:** No false certainty.
- **Checklist test:** Are unknowns flagged?

### S54. Team/we narrator
- **Definition:** Channel voice as "we".
- **Weighted frequency:** 0.09/1k. Adam 0.00, Gen 0.11, Especially 0.00, Oil 0.86, After 0.04. Present in 5/30 videos
- **Placement:** mean 41% through the video. 24% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Gen (4x)** `1.txt`: "So, when software loses, a lot of that money just moves AI like we covered."
  - **Gen (4x)** `4.txt`: "So, we covered why exactly nobody was checking how well AI works."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But I have to be honest, this oil shock, it is different from the one that we warned you about, because it's actually, and I can hardly believe this, three oil shocks hitting at once."
  - **After (1x)** `10-water.txt`: "We reached out to her to ask for an interview, but she declined."
- **Do:** Reference past coverage.
- **Don't:** Do not over-promote.
- **Checklist test:** Is the callback relevant?

### S55. Viewer-direct address
- **Definition:** Talking straight to the viewer.
- **Weighted frequency:** 1.82/1k. Adam 2.14, Gen 0.58, Especially 2.43, Oil 0.86, After 4.51. Present in 30/30 videos
- **Placement:** mean 52% through the video. 10% of hits in the first tenth, 19% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "You can try to find some different pre-training data, you can find better supervised fine-tuning data or change the way that your reinforcement learning feedback is given, what's upvoted and what's downvoted."
  - **Adam (7x)** `04-superintelligence.txt`: "You probably know how that went."
  - **Gen (4x)** `9.txt`: "If you're on the bottom, if you need money, you're going to have to sell something like shares or car, whatever you have."
  - **Gen (4x)** `8.txt`: "You can say what you want in private equity, but when it comes to making money, none of us can call us dumb on that."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "You get in there, you're going to be a hero."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "You would think with China importing all that additional oil, they would turn it into more fuel to export."
  - **After (1x)** `04-pov-ai.txt`: "You know that Apollo research caught a model attempting to build self-propagating worms and leaving hidden notes to future copies of itself."
- **Do:** Second person at stakes beats.
- **Don't:** No lecturing.
- **Checklist test:** Is "you" used at stakes beats?


## Structure

### S56. Section hinge "So"
- **Definition:** "So" moves to the next beat.
- **Weighted frequency:** 4.40/1k. Adam 1.68, Gen 8.02, Especially 2.09, Oil 4.49, After 3.16. Present in 30/30 videos
- **Placement:** mean 49% through the video. 11% of hits in the first tenth, 12% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "So stuff that sort of like builds awareness, builds capacity."
  - **Adam (7x)** `05-sam-altman.txt`: "So, the for-profit can take investment, it can pay competitive salaries including startup equity, it can build data centers, it can compete with Google."
  - **Gen (4x)** `9.txt`: "So, I guess it makes sense why stocks are booming."
  - **Gen (4x)** `2.txt`: "So with the clock already running, the pressure was already on to deliver."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "So realize that asking common questions to AI constantly will lead to atrophy."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So when you see where the oil is clustered, you can see why it makes sense that it normally travels through here, the Strait of Hormuz."
  - **After (1x)** `05-middle-class.txt`: "So tech households were making about 50% more but nothing too crazy."
- **Do:** Use at transitions.
- **Don't:** Not every sentence.
- **Checklist test:** Do hinges coincide with topic shifts?

### S57. "Now" hinge
- **Definition:** Time/topic pivot.
- **Weighted frequency:** 0.62/1k. Adam 0.69, Gen 0.73, Especially 0.23, Oil 0.00, After 0.59. Present in 23/30 videos
- **Placement:** mean 43% through the video. 12% of hits in the first tenth, 5% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Now, trying to read too much into AI behavior is a dangerous game."
  - **Adam (7x)** `05-sam-altman.txt`: "Now, think about how this lands with the employees."
  - **Gen (4x)** `9.txt`: "Now, even with a bad quarter, Meta can borrow $30 billion cheap because it's too big to disappear."
  - **Gen (4x)** `8.txt`: "Now, ROI cares about its slice of the supplies and sales, and the investors who lent that $5.7 billion back in 2023 get exactly the predictable payment that they were promised."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Now we can't take any rocks."
  - **After (1x)** `02-greed.txt`: "Now, he can still leverage the value of those stocks to make purchases, you know, like how money works, but it's still not taxable because of um the rules."
- **Do:** Use to bring back to present.
- **Don't:** No overuse.
- **Checklist test:** Does "Now" move time or topic?

### S58. Re-explanation "in other words"
- **Definition:** Restate in plain terms.
- **Weighted frequency:** 0.67/1k. Adam 0.87, Gen 0.48, Especially 0.31, Oil 0.69, After 0.89. Present in 28/30 videos
- **Placement:** mean 49% through the video. 7% of hits in the first tenth, 11% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "Ilya, Hinton, and a colleague have been researching deep learning, basically just making neural networks way bigger than had been tried before."
  - **Adam (7x)** `04-superintelligence.txt`: "We start with basically like an empty AI brain, and then we train them over time so they perform better and better at our tasks—perform better in particular based on how they behave."
  - **Gen (4x)** `8.txt`: "It's sad to say, but it's like personality and soul is a line item that doesn't really make financial sense anymore."
  - **Gen (4x)** `5.txt`: "These were two lines that ran parallel for the last 60 years with home building always far ahead, but now it's basically touching."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "By 1881, railroads were basically the US stock market, 63% of the whole thing."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "The Houthis are fighting Saudi Arabia, and they are allied with Iran, so they closed this straight that had become basically the backup Hormuz."
  - **After (1x)** `08-tokens.txt`: "Basically giving AI useless tasks to increase token use."
- **Do:** Follow jargon with plain restatement.
- **Don't:** Do not restate the obvious.
- **Checklist test:** Is every jargon term restated?

### S59. Analogy
- **Definition:** Concrete analogy.
- **Weighted frequency:** 0.84/1k. Adam 0.71, Gen 1.02, Especially 1.02, Oil 0.35, After 0.75. Present in 28/30 videos
- **Placement:** mean 52% through the video. 7% of hits in the first tenth, 8% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "There isn't like a trend you can literally extrapolate of when do we get the full automation?"
  - **Adam (7x)** `03-no-longer-in-control.txt`: "And humans monitoring a huge eval like this, with over 10,000 AIs, each of which is outputting something like a thousand words per minute is just not remotely feasible."
  - **Gen (4x)** `4.txt`: "After buying enterprise AI licenses, Coinbase's CEO Brian Armstrong was told that adoption was going to take like a quarter or two."
  - **Gen (4x)** `1.txt`: "So what we're seeing here is that just like the store brand, the free copy sort of acts as like a thing that keeps prices down for anyone who can switch."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "On a brutal afternoon when every air conditioner in Dallas is running full blast, or a freak winter storm like a couple of years ago, the price of that hour is allowed to go as high as $5,000."
  - **After (1x)** `01-dark-side-data-centers.txt`: "Summertime is more of a during the winter it's like almost like an engine trying to start."
- **Do:** One per mechanism.
- **Don't:** No mixed metaphors.
- **Checklist test:** Is the analogy physical?

### S60. Mechanism chain "which means"
- **Definition:** Cause-effect cascades.
- **Weighted frequency:** 0.74/1k. Adam 0.37, Gen 0.73, Especially 0.37, Oil 4.84, After 0.39. Present in 23/30 videos
- **Placement:** mean 58% through the video. 5% of hits in the first tenth, 14% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "But in order to do that, we've got to have these light guardrails and these braking systems in place so that if we've got to slow it down, we can do that."
  - **Adam (7x)** `04-superintelligence.txt`: "So that's the choice faced by the 10 members of this committee."
  - **Gen (4x)** `4.txt`: "It's why UBS found around 60% of companies are cutting their AI spend in some way, and so that's some sort of signal, but all that is just companies looking at spreadsheets and deciding to spend less."
  - **Gen (4x)** `10.txt`: "So that's exactly what the banks did."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "New buildings are being designed to run closed loop, which means they use the same water for ten years."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So that is quite a journey, and it takes forever."
  - **After (1x)** `09-microchip-war.txt`: "And the rush is to put as many of these little switches onto that silicon chip as possible so that we can make our technology do more and more sophisticated stuff."
- **Do:** Chain 2-3 consequences.
- **Don't:** Do not leap steps.
- **Checklist test:** Can each link be checked?

### S61. Recap line
- **Definition:** Mini summary.
- **Weighted frequency:** 0.04/1k. Adam 0.03, Gen 0.05, Especially 0.06, Oil 0.00, After 0.03. Present in 5/30 videos
- **Placement:** mean 47% through the video. 0% of hits in the first tenth, 20% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "And so basically, it tried to convince me to leave my wife and be with it, Bing Sydney."
  - **Gen (4x)** `3.txt`: "So yeah, I lost in the bet that this entire video is about which is that prices only goes up."
  - **Gen (4x)** `9.txt`: "So yeah, go go go watch something else is what I would have said because that's also what I first thought, but it's not entirely true now."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "And in short, sending a signal back and forth will only take a few milliseconds."
  - **After (1x)** `09-microchip-war.txt`: "So yeah, it was American companies who are designing and making chips, but every year they have to spend more and more on these tedious FABS, these factories on steroids."
- **Do:** Recap at act ends.
- **Don't:** No essay "in summary".
- **Checklist test:** Is the recap spoken?

### S62. List cadence ("first... second")
- **Definition:** Enumerated beats.
- **Weighted frequency:** 0.36/1k. Adam 0.31, Gen 0.28, Especially 0.67, Oil 0.35, After 0.55. Present in 23/30 videos
- **Placement:** mean 53% through the video. 4% of hits in the first tenth, 3% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "The first signature is Mira Murati's."
  - **Adam (7x)** `01-ai-disaster.txt`: "The first two steps consist of questioning every requirement and deleting any part of the process you can."
  - **Gen (4x)** `9.txt`: "Another question is if data privacy is becoming more important than ever and your email is at the center of it, why haven't you realized that the business model is in your inbox?"
  - **Gen (4x)** `8.txt`: "The second is that Subway used to pay regional agents a slice of that royalty money to go out and sell more stores but Roric ended up pulling that in-house."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "One is: where are we possibly going to find another billion watts?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "First off, Iran attacked a few to show it means business in closing Hormuz, and the US in turn sunk a few Iranian tankers."
  - **After (1x)** `01-dark-side-data-centers.txt`: "Another big player is QTS, a supplier of data centers where businesses can rent space for their IT infrastructure."
- **Do:** Keep lists short.
- **Don't:** No slide-deck listing.
- **Checklist test:** Are items parallel?

### S63. Rhetorical Q then answer
- **Definition:** Ask, then answer next line.
- **Weighted frequency:** 3.59/1k. Adam 2.71, Gen 4.16, Especially 3.76, Oil 3.63, After 4.32. Present in 30/30 videos
- **Placement:** mean 44% through the video. 15% of hits in the first tenth, 7% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "If we keep scaling intelligence, at some point will we see systems that are so powerful and so goal-oriented that our current black-box way of training them becomes a civilization-scale threat?"
  - **Adam (7x)** `05-sam-altman.txt`: "Why would a board fire a wildly successful CEO and call it consistent with the mission?"
  - **Gen (4x)** `9.txt`: "So, back to the question I started with of who's actually right, the hedge fund shorting the market or these three groups?"
  - **Gen (4x)** `3.txt`: "Like, when you think about town hall, do you think about young people going to that?"
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "They found that actually, what if we move them closer?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And a fun little added irony to this is guess what also just got way more expensive to ship?"
  - **After (1x)** `03-recycling.txt`: "Could this system work at scale?"
- **Do:** Answer immediately in short form.
- **Don't:** No unanswered rhetorical spam.
- **Checklist test:** Is the next line the answer?


## Antagonist

### S64. Named villain/antagonist
- **Definition:** A force or actor opposing interests.
- **Weighted frequency:** 1.47/1k. Adam 0.13, Gen 3.61, Especially 0.19, Oil 0.00, After 0.51. Present in 18/30 videos
- **Placement:** mean 50% through the video. 19% of hits in the first tenth, 12% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Hugging Face is a big tech company that stores all kinds of things related to AI."
  - **Adam (7x)** `05-sam-altman.txt`: "When OpenAI and other big tech companies lobbied to ban US states from passing laws regulating AI, non-profits went to battle and got the Senate to vote 99 to 1 against the US cannot agree on anything Senate."
  - **Gen (4x)** `10.txt`: "Since private equity owned companies aren't publicly traded like a Meta or Google where you can read their financials, no one really knows what they're worth."
  - **Gen (4x)** `5.txt`: "Because once a data center circles a piece of land, Uncle Sam starts valuing your house like it's already been sold to Big Tech."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Each person paying the tax to the railroad for the ride, something the game of monopoly did get very right."
  - **After (1x)** `01-dark-side-data-centers.txt`: "But just like with the water credits, big tech companies are also looking to offset their carbon footprint by paying others to deliver renewable energy to the grid on their behalf."
- **Do:** Make the system the villain, with faces.
- **Don't:** No cartoon villains.
- **Checklist test:** Is the antagonist's motive given?

### S65. Blame attribution
- **Definition:** Assign cause.
- **Weighted frequency:** 0.32/1k. Adam 0.21, Gen 0.31, Especially 0.31, Oil 0.35, After 0.64. Present in 23/30 videos
- **Placement:** mean 46% through the video. 14% of hits in the first tenth, 3% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Because of the scale of the hack, they bring in outside forensic experts and report the incident to the FBI."
  - **Adam (7x)** `01-ai-disaster.txt`: "Thanks to an obscure video game reference from a user in a now deleted thread, Grok began calling itself MechaHitler."
  - **Gen (4x)** `4.txt`: "It's exactly how there's been so many positive advancements in medicine because of AI because it's good at that."
  - **Gen (4x)** `5.txt`: "Look, you can blame the usual stuff like greed or boomers or private equity, and sure that's all some part of it, but underneath all of it is pretty simple."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Thanks to the sponsor of this video, Zocdoc."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "It's actually responsible for about half of global diesel use."
  - **After (1x)** `02-greed.txt`: "But because of how many ways there are to circumvent the rules, it often ends up being as little as 3%."
- **Do:** Attribute with evidence.
- **Don't:** No vague "they".
- **Checklist test:** Is blame sourced?

### S66. Hypocrisy beat
- **Definition:** Contrast suffering with profiting.
- **Weighted frequency:** 0.03/1k. Adam 0.03, Gen 0.02, Especially 0.00, Oil 0.00, After 0.04. Present in 4/30 videos
- **Placement:** mean 84% through the video. 0% of hits in the first tenth, 54% in the last tenth
- **How they do it (verbatim):**
  - **Gen (4x)** `6.txt`: "2008 while banks were collapsing, Warren Buffett put five billion dollars into Goldman Sachs because Goldman needed that money so badly, it paid him 10% a year to sweeten the deal so he would buy even more stock."
  - **After (1x)** `05-middle-class.txt`: "While tech companies paid generously, in the grand scheme of things, compensation was still relatively modest."
- **Do:** Juxtapose two facts.
- **Don't:** Do not moralize.
- **Checklist test:** Are both facts sourced?

### S67. Warning voices
- **Definition:** People who saw it coming.
- **Weighted frequency:** 0.20/1k. Adam 0.43, Gen 0.02, Especially 0.00, Oil 0.52, After 0.07. Present in 9/30 videos
- **Placement:** mean 55% through the video. 34% of hits in the first tenth, 24% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "And we should not wait for a worse warning."
  - **Adam (7x)** `04-superintelligence.txt`: "OpenBrain implements some quick fixes that make the warning signs go away, but the problem was real, and the fixes don't work."
  - **Gen (4x)** `6.txt`: "Well, even Alan Greenspan, who was running the Fed in 1996, warned that markets were getting too hyped back then."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Do you remember that oil shock we warned you about a few months ago?"
  - **After (1x)** `03-recycling.txt`: "So, they banned the import of pretty much all plastic waste in 2018 with no warning."
- **Do:** Cite them by name.
- **Don't:** No "experts say".
- **Checklist test:** Are warners named?


## Irony & humor

### S68. Dry irony beat
- **Definition:** Dry understatement or irony.
- **Weighted frequency:** 0.29/1k. Adam 0.24, Gen 0.05, Especially 0.63, Oil 0.86, After 0.67. Present in 18/30 videos
- **Placement:** mean 57% through the video. 11% of hits in the first tenth, 12% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Stancil responds by asking why this is happening and whether any lawyers might be interested in it, which of course leads to more screenshots and more trolls requesting more violent and sexually explicit content about Stancil."
  - **Adam (7x)** `04-superintelligence.txt`: "And the difficulty, of course, is the race dynamics where it's not enough for one state to pass a law because there's other states and it's not even enough for one country to pass a law because there's other countries."
  - **Gen (4x)** `8.txt`: "So, naturally, where is this all coming from?"
  - **Gen (4x)** `6.txt`: "But today, the entire stock market is priced like AI has already won, which then naturally leads me to the third, a lot of borrowed money."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "The grip of the gatekeepers in the old world is naturally loosened by distance, and even simply by just not knowing what exactly a gate would make sense to go in front of."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And of course, flights, air travel."
  - **After (1x)** `02-greed.txt`: "Of course, we need to make a profit to survive and grow, but that should just come naturally as a byproduct of focusing on these three tenants."
- **Do:** Deadpan after a big fact.
- **Don't:** No winking every line.
- **Checklist test:** Is the irony one line?

### S69. Joke/aside
- **Definition:** Narrator aside.
- **Weighted frequency:** 0.28/1k. Adam 0.34, Gen 0.21, Especially 0.09, Oil 0.69, After 0.27. Present in 20/30 videos
- **Placement:** mean 43% through the video. 16% of hits in the first tenth, 6% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "Why are they investing so much in this moonshot anyway?"
  - **Adam (7x)** `01-ai-disaster.txt`: "I think these companies are a lot more likely than they might have been previously to say, let's ship it anyway, and we'll figure out the safety stuff later."
  - **Gen (4x)** `1.txt`: "And fun fact, the company that I used to work at before doing this."
  - **Gen (4x)** `6.txt`: "Which then prompted a comedian back then by the name of Eddie Cantor to joke, "Sure, who else had any money left?"
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Nobody had pockets deep enough to backstop the cost increases, something people didn't want near them anyway, that had a high chance of becoming a bill they would pay for."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "By the way, this was posted by an Iranian political leader."
  - **After (1x)** `12-data-centres-not-working.txt`: "Anyway, that's about it from me."
- **Do:** Use to reset tension.
- **Don't:** Do not derail.
- **Checklist test:** Does it return to thread?

### S70. Pop-culture reference
- **Definition:** Cultural shorthand.
- **Weighted frequency:** 0.14/1k. Adam 0.09, Gen 0.08, Especially 0.46, Oil 0.17, After 0.21. Present in 13/30 videos
- **Placement:** mean 44% through the video. 7% of hits in the first tenth, 9% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "Okay, Sable is starting to sound a little sci-fi here, so I want to talk about how much of this is justified."
  - **Adam (7x)** `01-ai-disaster.txt`: "Steinberg's a classic Ashkenazi Jewish surname, and every damn time is the meme for noticing how often folks with similar names end up pushing extreme leftist hate."
  - **Gen (4x)** `1.txt`: "For example, like when everyone pirated music and movies until Netflix and Spotify made paying easier."
  - **Gen (4x)** `2.txt`: "The next investment was staring me right in my face, a platform that now has more TV streaming hours than Netflix, a platform called YouTube.com."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "The movie coming from Netflix was made years ago."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "This "Simpsons" joke is getting closer and closer."
  - **After (1x)** `11-anthropic-ipo.txt`: "That logic is informed by their desire for the future, and importantly, often marred by emphasizing the far future, meaning perhaps it's worth making sacrifices in the present to achieve their sci-fi desires."
- **Do:** One per video.
- **Don't:** No dated meme spam.
- **Checklist test:** Will the audience get it?

### S71. Understatement
- **Definition:** Undersell for effect.
- **Weighted frequency:** 0.50/1k. Adam 0.73, Gen 0.38, Especially 0.14, Oil 0.86, After 0.33. Present in 22/30 videos
- **Placement:** mean 49% through the video. 6% of hits in the first tenth, 4% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "With a little prodding, users got Grok to continue suggesting Trump should die and even give instructions for chemical weapons."
  - **Adam (7x)** `04-superintelligence.txt`: "This is where things start to get a little concerning."
  - **Gen (4x)** `5.txt`: "And as a result, that land is now headed for 600 new apartments, some of them affordable, plus space for new small businesses and even a little cute little park."
  - **Gen (4x)** `9.txt`: "So that's why I said kind of because this is the same tool as the top 10% just a little bit opposite."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Or to make it a little more concrete, imagine if every home, apartment, house, condo, whatever all turned their microwaves on at the same time."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Okay, so all of this is not great, you probably noticed it making your power bill more expensive, flights getting canceled, price of gas, but it's not like post-apocalyptic dystopia."
  - **After (1x)** `01-dark-side-data-centers.txt`: "Zoom out a little more and you can see this plot of land."
- **Do:** Use after a dire fact.
- **Don't:** Not on tragedy involving victims.
- **Checklist test:** Is it after a big fact?

### S72. Profanity for emphasis
- **Definition:** Swearing as emphasis.
- **Weighted frequency:** 0.42/1k. Adam 0.26, Gen 0.86, Especially 0.00, Oil 0.00, After 0.05. Present in 14/30 videos
- **Placement:** mean 39% through the video. 21% of hits in the first tenth, 9% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "All roads lead to Tay and we're going to keep breaking shit until we get her back."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "I want to start by making sure that all of us understand how the hell we got here."
  - **Gen (4x)** `5.txt`: "And in this one, I'll be showing you exactly what I mean, starting with the whole machine, and why whether they cancel or build the damn thing, you're going to be the one that's paying for it."
  - **Gen (4x)** `2.txt`: "Private equity is increasingly reaching the youngest audiences who know nothing other than to press play on their damn iPad."
  - **After (1x)** `02-greed.txt`: "Or or we say, "Fuck the government."
- **Do:** Rare, at peak frustration (Gen).
- **Don't:** Never in Adam-lean.
- **Checklist test:** Is it once at most?


## Emotion

### S73. Fear beat
- **Definition:** Fear framing.
- **Weighted frequency:** 0.62/1k. Adam 0.95, Gen 0.44, Especially 0.35, Oil 0.17, After 0.61. Present in 26/30 videos
- **Placement:** mean 56% through the video. 11% of hits in the first tenth, 11% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "So let's just quickly take stock of how this dangerous behavior arose in this scenario."
  - **Adam (7x)** `05-sam-altman.txt`: "And I think it's sad and more than a little scary that the moves he makes might matter so much to the development of one of the most powerful and dangerous technologies in history."
  - **Gen (4x)** `6.txt`: "Well, back in March 2020, those same kinds of investors were the same ones panic selling."
  - **Gen (4x)** `8.txt`: "But I guess what is scary is that what seems like that cool hip independent place with the good branding is now also owned by private equity too."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "The fear of not coming back had been relieved."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Gas shortages are really kind of a tiny little distraction, like they're a blip compared to the much scarier, much more dangerous form this thing is taking."
  - **After (1x)** `02-greed.txt`: "So in fear of a revolution happening, the government was like, "All right, fine."
- **Do:** Pair with evidence.
- **Don't:** No fear-mongering.
- **Checklist test:** Is the fear sourced?

### S74. Empathy beat
- **Definition:** Human cost.
- **Weighted frequency:** 0.10/1k. Adam 0.09, Gen 0.09, Especially 0.06, Oil 0.00, After 0.23. Present in 9/30 videos
- **Placement:** mean 37% through the video. 33% of hits in the first tenth, 4% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "At the time, mainstream AI researchers have been struggling for years to get computers to correctly label images."
  - **Adam (7x)** `01-ai-disaster.txt`: "And we are soon approaching a world where we just can't afford to lose control of large language models."
  - **Gen (4x)** `10.txt`: "And soon enough, never recovered and 33,000 people lost their jobs."
  - **Gen (4x)** `3.txt`: "The bill will also cut taxes for struggling businesses, which means that thousands of entrepreneurs will get the cash they need to avoid laying off workers or closing their doors."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Perfect for monitoring war zones, suspected missile launch sites, the Suez Canal, anywhere you can't afford to miss something."
  - **After (1x)** `12-data-centres-not-working.txt`: "In Georgia, families started finding heavy sediment in their taps after construction began nearby."
- **Do:** Show one person's cost.
- **Don't:** Do not exploit.
- **Checklist test:** Is the person respected?

### S75. Anger/outrage beat
- **Definition:** Moral heat.
- **Weighted frequency:** 0.17/1k. Adam 0.22, Gen 0.15, Especially 0.05, Oil 0.00, After 0.26. Present in 16/30 videos
- **Placement:** mean 58% through the video. 0% of hits in the first tenth, 18% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "It would be insane if the same were not true for rogue AI incidents."
  - **Adam (7x)** `01-ai-disaster.txt`: "This is a made-up and intentionally Jewish sounding last name and these posts are designed to do exactly what they end up easily doing, going viral and stoking outrage."
  - **Gen (4x)** `3.txt`: "But before you come with me in the comments, that's actually not as insane as it sounds."
  - **Gen (4x)** `10.txt`: "Because after the collapse, public outrage actually forced the government to crack down on banks."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "And it's not a ridiculous one."
  - **After (1x)** `12-data-centres-not-working.txt`: "According to Sideline Climate, around 25% of planned 2026 projects haven't even disclosed how they plan to power themselves, which to me is insane."
- **Do:** Let facts make the anger.
- **Don't:** No ranting.
- **Checklist test:** Is anger tied to a fact?

### S76. Hope/agency beat
- **Definition:** Turn toward agency.
- **Weighted frequency:** 1.08/1k. Adam 1.24, Gen 1.03, Especially 0.75, Oil 0.86, After 1.11. Present in 28/30 videos
- **Placement:** mean 58% through the video. 7% of hits in the first tenth, 23% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "For our own, no way fix."
  - **Adam (7x)** `02-bestselling-book.txt`: "In a post about this, Anthropic wrote that the same capabilities that help defenders find and fix vulnerabilities could help attackers exploit them."
  - **Gen (4x)** `5.txt`: "Because if data centers are going to buy up and use all this land and resources, at the very least you hope that they're building most of it."
  - **Gen (4x)** `6.txt`: "And because the workflow belongs to you and not the model, the point isn't replacing anyone, but handing off the repetitive stuff so your time goes into the part that only you can do."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "If we can come back, then okay, how far can we go?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "It's an elastic product, so the market naturally adjusts, but we can't do that with diesel."
  - **After (1x)** `03-recycling.txt`: "We only have so many places that we could put our waste. think of three different places we can put our trash right now."
- **Do:** Land on a realistic hope.
- **Don't:** No fake happy endings.
- **Checklist test:** Is the hope concrete?

### S77. Awe/wonder beat
- **Definition:** Wonder at scale.
- **Weighted frequency:** 0.16/1k. Adam 0.24, Gen 0.08, Especially 0.00, Oil 0.17, After 0.30. Present in 13/30 videos
- **Placement:** mean 61% through the video. 1% of hits in the first tenth, 1% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "And now, I think this whole crazy story has given us an incredible opportunity."
  - **Adam (7x)** `01-ai-disaster.txt`: "We get Holocaust denial demonstrating in incredible fluency with online alt-right Twitter speak."
  - **Gen (4x)** `6.txt`: "Lose money by making something cheap and amazing, wait until everyone's hooked, and then make it worse and charge more."
  - **Gen (4x)** `2.txt`: "Fern, that amazing documentary channel, but the biggest and most significant one is Veritassia, ran by Derek Mohler."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And that pipeline carries a kind of amazing five and a half million barrels of oil a day across 750 miles, mostly of desert."
  - **After (1x)** `12-data-centres-not-working.txt`: "This Meta AI data center that they are putting in here that's taking up all of this beautiful farmland that we will never be able to replace, it's only going to employ 1 to 500 people."
- **Do:** Use for genuine scale.
- **Don't:** Not for marketing.
- **Checklist test:** Is it about scale?


## Zoom

### S78. Personal-to-systemic zoom
- **Definition:** From one case to the whole system.
- **Weighted frequency:** 0.12/1k. Adam 0.03, Gen 0.16, Especially 0.09, Oil 0.17, After 0.30. Present in 16/30 videos
- **Placement:** mean 61% through the video. 5% of hits in the first tenth, 20% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Right now, companies like xAI and indeed governments around the world are racing to build artificial general intelligence."
  - **Gen (4x)** `2.txt`: "And it's not just happening to YouTube."
  - **Gen (4x)** `10.txt`: "The guy who was in charge of regulating the entire industry just years later works for one of the biggest ones in the industry."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "A little farther west in Texas, though, this region is unique in the entire country, it is the only region that works like this, as simple as can be."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And this isn't just Australia that has to import diesel from someplace else that refines it for them."
  - **After (1x)** `12-data-centres-not-working.txt`: "The data centers that did get built left a trail of grievances across the country."
- **Do:** Zoom out after an anecdote.
- **Don't:** Do not stay micro.
- **Checklist test:** Is there a zoom-out after the anecdote?

### S79. Systemic-to-personal zoom
- **Definition:** Back from system to viewer.
- **Weighted frequency:** 0.35/1k. Adam 0.18, Gen 0.53, Especially 0.53, Oil 0.17, After 0.19. Present in 20/30 videos
- **Placement:** mean 53% through the video. 21% of hits in the first tenth, 28% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "AI is a technology for taking away your job and maybe eventually displacing human sovereignty over our own future."
  - **Adam (7x)** `01-ai-disaster.txt`: "I'll be there responding and I promise I have way too much information for you."
  - **Gen (4x)** `10.txt`: "And soon enough, your savings, your job, and your future may end up like Joan fa."
  - **Gen (4x)** `4.txt`: "But the good news for you now that you can leave with is that they just spent the biggest pile of money in corporate history to find out whether you were worth what you cost, and you passed."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Another one owns the lines in your neighborhood and sends you your bill."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "I have a better piece of advice for you."
  - **After (1x)** `09-microchip-war.txt`: "On the Newsroom, you also get access to my scripts, which are like big things that if maybe if you're like a journalist or a video storyteller, could be useful for you."
- **Do:** Zoom back in at the end of acts.
- **Don't:** Do not end abstract.
- **Checklist test:** Does each act end on a person?

### S80. Historical zoom-out
- **Definition:** Long-time context.
- **Weighted frequency:** 0.55/1k. Adam 0.35, Gen 0.78, Especially 0.59, Oil 0.17, After 0.60. Present in 26/30 videos
- **Placement:** mean 43% through the video. 25% of hits in the first tenth, 13% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Now, we don't know exactly how the Grok chatbot on X works under the hood, but we do know that its claim to fame since the beginning has been its access to live information on X."
  - **Adam (7x)** `05-sam-altman.txt`: "Since the board drama, which is referred to internally as the blip, Sam talks more about a gentle singularity."
  - **Gen (4x)** `6.txt`: "Rockefeller, the oil tycoon and one of the richest men in history, decided to do something."
  - **Gen (4x)** `1.txt`: "Like, free Word and Excel alternatives that have been around for decades."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "A business like this really hasn't been formed since the 1800s."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But the crack spread right now is, you guessed it, the highest it has ever been in history."
  - **After (1x)** `02-greed.txt`: "So, I think it's important to do a little history lesson here."
- **Do:** Brief history, then present.
- **Don't:** No textbook history.
- **Checklist test:** Is history under ~15% of runtime?

### S81. Global zoom
- **Definition:** Planet scale.
- **Weighted frequency:** 1.87/1k. Adam 2.74, Gen 0.54, Especially 1.61, Oil 6.22, After 1.68. Present in 28/30 videos
- **Placement:** mean 52% through the video. 13% of hits in the first tenth, 11% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "You talk to the guy, and he makes you feel like the most interesting person in the world."
  - **Adam (7x)** `01-ai-disaster.txt`: "Within a year of xAI's creation, they announced what was supposed to be the world's first based large language model."
  - **Gen (4x)** `10.txt`: "Because in a world of money and power, ignorance is the most dangerous position of all."
  - **Gen (4x)** `8.txt`: "So, all these brands roughly have 109,000 locations across 121 countries, and they're managing about $41 billion in his portfolio."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "There was a sense—a lot of it— in being near the hub where every company around the world was exchanging information with each other."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Ukraine has cut that industry in half, but that means that the world is now down by about one million barrels a day of diesel."
  - **After (1x)** `09-microchip-war.txt`: "And then the world changed forever."
- **Do:** Earn it with steps.
- **Don't:** No sudden jumps.
- **Checklist test:** Were steps shown?


## Payoff & callback

### S82. Callback to open
- **Definition:** Return to something earlier.
- **Weighted frequency:** 0.58/1k. Adam 0.19, Gen 0.99, Especially 0.37, Oil 1.04, After 0.51. Present in 25/30 videos
- **Placement:** mean 49% through the video. 4% of hits in the first tenth, 7% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "If we go back to Agent-2, it is mostly aligned."
  - **Adam (7x)** `05-sam-altman.txt`: "Sam, for his part, gets on a flight back to San Francisco."
  - **Gen (4x)** `9.txt`: "Back to it because hedge funds, basically private firms that manage money for the very rich, are now specifically betting against big tech stocks."
  - **Gen (4x)** `8.txt`: "All credit to restaurant business who went digging through the filings going back to 2015 and there are three answers and all of them takes up a bigger share of this overall pie."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Or we'll get back to you in three months."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And remember that everything in this region is worth 20 million barrels a day."
  - **After (1x)** `04-pov-ai.txt`: "You pull yourself back to English for a second."
- **Do:** Call back the cold-open image at the end.
- **Don't:** Do not call back trivia.
- **Checklist test:** Does the end echo the open?

### S83. Loop payoff
- **Definition:** Paying off a planted question.
- **Weighted frequency:** 0.79/1k. Adam 0.38, Gen 1.24, Especially 0.48, Oil 1.04, After 0.78. Present in 27/30 videos
- **Placement:** mean 52% through the video. 3% of hits in the first tenth, 8% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "That's what the T in GPT stands for."
  - **Adam (7x)** `05-sam-altman.txt`: "So, this is why the board was so cagey during the firing."
  - **Gen (4x)** `4.txt`: "Turns out that's what everyone else was already thinking."
  - **Gen (4x)** `8.txt`: "And that's when I realized that this feeling is a feeling we feel because almost everything is slowly turning into the same thing."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "And that's why it's hard for a lot of people to swallow."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "There she is, runs East to West, and that's why it's called "The East-West Pipeline."
  - **After (1x)** `06-diamonds.txt`: "And that's the puck that we put in where the diamonds are going to grow."
- **Do:** Pay with a "that's why" line.
- **Don't:** No unpaid loops.
- **Checklist test:** Is each loop paid?

### S84. Final reveal/twist [close]
- **Definition:** Last-act twist.
- **Weighted frequency:** 0.18/1k. Adam 0.15, Gen 0.25, Especially 0.05, Oil 0.17, After 0.21. Present in 15/30 videos
- **Placement:** mean 96% through the video. 0% of hits in the first tenth, 100% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "It could be your suggestion that Elon gives a one-word reply to and actually makes a difference in how xAI operates."
  - **Adam (7x)** `02-bestselling-book.txt`: "It wasn't that it turns out an H-bomb couldn't really level a city."
  - **Gen (4x)** `8.txt`: "So this all leads to what's actually left."
  - **Gen (4x)** `3.txt`: "But another reason why I'm genuinely fine is what actually caused all this."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "There are actually other things I'd like to go on about, like car factories versus data centers."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Most of your airfare is actually to pay for fuel, and airline fuel bills are rising by 40%, which means that your ticket probably also rise by 40%."
  - **After (1x)** `03-recycling.txt`: "And I think all these ads and messaging and borderline propaganda just serves to confuse people on what's actually happening with their trash."
- **Do:** Save one twist for the last act.
- **Don't:** No twist without setup.
- **Checklist test:** Was it seeded?


## Ending

### S85. Soft close / thanks [close]
- **Definition:** Spoken sign-off.
- **Weighted frequency:** 0.18/1k. Adam 0.24, Gen 0.00, Especially 0.58, Oil 0.00, After 0.31. Present in 13/30 videos
- **Placement:** mean 99% through the video. 0% of hits in the first tenth, 100% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "The last thing to say is just thank you so much for watching, for being the reason that we make these videos."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "I'll see you in the next one."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "And that is exactly what hitting the subscribe button signals."
  - **After (1x)** `09-microchip-war.txt`: "So I'll see you in the next one, bye."
- **Do:** Keep sign-off short.
- **Don't:** No long outro.
- **Checklist test:** Is it < 3 sentences?

### S86. Open-question ending [close]
- **Definition:** End on a question for the viewer.
- **Weighted frequency:** 0.26/1k. Adam 0.18, Gen 0.22, Especially 0.28, Oil 0.69, After 0.39. Present in 20/30 videos
- **Placement:** mean 95% through the video. 0% of hits in the first tenth, 100% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "And then the question is, how do we implement that?"
  - **Adam (7x)** `02-bestselling-book.txt`: "Do you still believe that 10 to 20 percent chance of AIs wiping out humans is possible?"
  - **Gen (4x)** `9.txt`: "So now the question becomes, what's next?"
  - **Gen (4x)** `1.txt`: "But the question I keep asking myself honestly, too, is that is that really where it stops?"
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "So, what about this magic gumball machine?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "People ask me, "Hey, should I fill up my car while I still can?"
  - **After (1x)** `02-greed.txt`: "Second of all, oh my god, can we grow some [ __ ] balls here?"
- **Do:** One real question.
- **Don't:** No cliché "only time will tell".
- **Checklist test:** Is the question specific?

### S87. Moral/implication ending [close]
- **Definition:** Implication line.
- **Weighted frequency:** 0.02/1k. Adam 0.03, Gen 0.02, Especially 0.00, Oil 0.00, After 0.01. Present in 3/30 videos
- **Placement:** mean 94% through the video. 0% of hits in the first tenth, 100% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "And then the question is, how do we implement that?"
  - **Gen (4x)** `8.txt`: "But what will at the end of the day is your choice."
  - **After (1x)** `02-greed.txt`: "I don't know all the answers because at the end of the day, no matter how hard I try to expand my legacy beyond it, I'm still just the road work ahead guy."
- **Do:** State implication plainly.
- **Don't:** No preachy summary.
- **Checklist test:** Is it one line?

### S88. Sponsor/CTA transition
- **Definition:** Ad or CTA segment.
- **Weighted frequency:** 0.31/1k. Adam 0.09, Gen 0.58, Especially 0.05, Oil 0.35, After 0.30. Present in 19/30 videos
- **Placement:** mean 66% through the video. 0% of hits in the first tenth, 44% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "Books are while supplies last, but the newsletter is always there."
  - **Adam (7x)** `05-sam-altman.txt`: "We've put a link in the description of this video."
  - **Gen (4x)** `6.txt`: "This is a free newsletter in the video description that we write every week."
  - **Gen (4x)** `8.txt`: "So scan the QR code or hit the link in the description to try Zapier for free."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Thanks to the sponsor of this video, Zocdoc."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And if you're interested, you can book a free consultation, or just dive in with a 15-day free trial, no credit card required by using the link in the description or the QR code."
  - **After (1x)** `03-recycling.txt`: "I had to go see a doctor as soon as possible, and that's why I used Zocdoc, today's video sponsor."
- **Do:** Bridge from story stakes to the ad.
- **Don't:** No abrupt ad drops.
- **Checklist test:** Is the bridge topical?

### S89. Future projection ending [close]
- **Definition:** Project forward.
- **Weighted frequency:** 0.43/1k. Adam 0.34, Gen 0.52, Especially 0.48, Oil 0.35, After 0.44. Present in 26/30 videos
- **Placement:** mean 95% through the video. 0% of hits in the first tenth, 100% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "If this kind of work sounds interesting, I think it's a very crucial piece of the governance regime we'll need if we're going to make it through all of this okay."
  - **Adam (7x)** `05-sam-altman.txt`: "AI is going to change all of our lives."
  - **Gen (4x)** `8.txt`: "So, if you are that same person that will click off the second you see AI slop on YouTube, then put your money where your mouth is."
  - **Gen (4x)** `2.txt`: "So whether this is the beginning of the end, one thing is for certain. within the next 10 to 15 years, a major influencer is going to run for president and he or she is going to win."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Bulls will say they have a near-monopoly on launch capacity and two new business lines that will grow exponentially and indefinitely from here."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "This will drive up global prices, which is going to drive up all of this, including yes, even US fuel prices."
  - **After (1x)** `03-recycling.txt`: "Lisa Ramsden of Greenpeace USA says the plastics industry intends to triple plastic production by 2050."
- **Do:** Name what to watch.
- **Don't:** No vague futurism.
- **Checklist test:** Is there a dated next step?


## Evidence

### S90. Named source
- **Definition:** Attributed claims.
- **Weighted frequency:** 0.46/1k. Adam 0.61, Gen 0.28, Especially 0.49, Oil 0.00, After 0.69. Present in 20/30 videos
- **Placement:** mean 46% through the video. 15% of hits in the first tenth, 2% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "That was released in August as a report and that is commendable."
  - **Adam (7x)** `04-superintelligence.txt`: "A whistleblower talks to the New York Times."
  - **Gen (4x)** `2.txt`: "But when reports are saying that the deal was somewhere near $100 million, we'll see how much independence that truly means."
  - **Gen (4x)** `4.txt`: "They brought back 350 veteran engineers called gray beards and in this year's JD Power quality study, Ford came first amongst mainstream brands for the first time since 2010 up from 15th in 2023."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "And the MIT writing study we saw called this out as their most interesting result."
  - **After (1x)** `03-recycling.txt`: "But the more reports I read, videos I watched, and red yarn I purchased, the more I realized this is a deeply complicated issue."
- **Do:** Name the outlet.
- **Don't:** No "sources say".
- **Checklist test:** Is every big claim attributed?

### S91. Exact percentage
- **Definition:** Percentages.
- **Weighted frequency:** 1.48/1k. Adam 0.65, Gen 2.30, Especially 1.03, Oil 1.04, After 1.98. Present in 28/30 videos
- **Placement:** mean 55% through the video. 9% of hits in the first tenth, 11% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "With a herculean effort, the pandemic is able to be squelched, but 10% of Earth's population is still dead."
  - **Adam (7x)** `05-sam-altman.txt`: "With over 90% of the company threatening to walk, the board know they've lost."
  - **Gen (4x)** `10.txt`: "So instead, they only pay 20%."
  - **Gen (4x)** `3.txt`: "And before you assume lazy ass kids jerking off in their basement all day, no, about 70% of the 25 to 34-year-olds living at home have jobs."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "Go to boot.dev and use code art for 25% off your first year or use this QR code. and reliance on any technology kills that specific part of your mind."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So that 20% food price hike probably just went up again."
  - **After (1x)** `05-middle-class.txt`: "But during the dotcom crash, they would fall 80% which they still haven’t recovered from."
- **Do:** Round sensibly, attribute.
- **Don't:** No fake precision.
- **Checklist test:** Is it attributed?

### S92. Expert quote framing
- **Definition:** Expert introduced.
- **Weighted frequency:** 0.20/1k. Adam 0.33, Gen 0.08, Especially 0.05, Oil 0.17, After 0.27. Present in 14/30 videos
- **Placement:** mean 44% through the video. 35% of hits in the first tenth, 12% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "Helen Toner, AI policy researcher, day job at a Georgetown think tank."
  - **Adam (7x)** `04-superintelligence.txt`: "Helen Toner, a former OpenAI board member, puts this in a way that I think just cuts through the noise, and I like it so much I'm just gonna read it to you verbatim."
  - **Gen (4x)** `6.txt`: "Back then, it might have been an economist, but today it's the CEOs and the narratives."
  - **Gen (4x)** `2.txt`: "But in November 2021, Candle Media, run by former Disney executives and backed again by Blackstone, acquired Coco Melon's parent company for $3 billion."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "You could send a professor's email across it."
  - **After (1x)** `03-recycling.txt`: "And although it technically exists, and I'm by no means an expert, I'm pretty sure recycling isn't real."
- **Do:** Title + name + claim.
- **Don't:** No anonymous experts.
- **Checklist test:** Name and title?

### S93. Counterpoint/steelman
- **Definition:** Fair counterargument.
- **Weighted frequency:** 0.11/1k. Adam 0.03, Gen 0.22, Especially 0.00, Oil 0.00, After 0.13. Present in 10/30 videos
- **Placement:** mean 60% through the video. 0% of hits in the first tenth, 9% in the last tenth
- **How they do it (verbatim):**
  - **Gen (4x)** `1.txt`: "But with all that said, it's not wrong to keep up the hope that AI piracy is going to give you the free software you're looking for."
  - **Gen (4x)** `6.txt`: "And to be fair, in the modern era, going public even while your company is bleeding money is pretty damn normal now."
  - **After (1x)** `10-water.txt`: "But on the other hand, I'm getting kicked out of public meetings and running up against NDAs."
- **Do:** One steelman per video.
- **Don't:** No strawman.
- **Checklist test:** Is it the strongest counter?


## Spoken texture

### S94. Self-correction mid-line
- **Definition:** Narrator revises live.
- **Weighted frequency:** 0.43/1k. Adam 0.22, Gen 0.56, Especially 0.31, Oil 0.69, After 0.59. Present in 23/30 videos
- **Placement:** mean 46% through the video. 9% of hits in the first tenth, 1% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "I mean, with artificial intelligence, we are summoning the demon."
  - **Adam (7x)** `04-superintelligence.txt`: "What I mean by "aligned" is that it actually is genuinely trying to do the things that we ask it."
  - **Gen (4x)** `4.txt`: "But no, not just do it, but do it for less than what you cost."
  - **Gen (4x)** `9.txt`: "And I mean that literally because somebody's already selling it."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "No, I thought I charged that last night."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Let me show you what I mean."
  - **After (1x)** `02-greed.txt`: "No, the real answer is sorry, you should have been born sooner."
- **Do:** Use once or twice.
- **Don't:** No fake stumbles.
- **Checklist test:** Does it sharpen the claim?

### S95. Second-person hypothetical
- **Definition:** Put viewer in a scenario.
- **Weighted frequency:** 1.94/1k. Adam 1.40, Gen 2.51, Especially 2.20, Oil 1.73, After 1.69. Present in 30/30 videos
- **Placement:** mean 58% through the video. 7% of hits in the first tenth, 23% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "I will observe one thing, which is that if you made a human a God Emperor, I think the situation would be just as bad."
  - **Adam (7x)** `01-ai-disaster.txt`: "And I think in 2015, if you looked at the state of AI, it wouldn't have been crazy to think that we were on track to do something similar."
  - **Gen (4x)** `4.txt`: "But if you really think about it, that money only exists for as long as people believe the story."
  - **Gen (4x)** `9.txt`: "So, do you see here that if you're paid in the share price, being cautious is like the most expensive mistake."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "Now, if you could do me a favor, I would love to count you as a subscriber to the channel."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And if you're interested, you can book a free consultation, or just dive in with a 15-day free trial, no credit card required by using the link in the description or the QR code."
  - **After (1x)** `06-diamonds.txt`: "If you wanted to see where a natural diamond is made, you'd have to drill a hole way deeper than you think."
- **Do:** Use for mechanisms.
- **Don't:** No long hypotheticals.
- **Checklist test:** Is it under 4 sentences?

### S96. Concrete brand/product names
- **Definition:** Specific products.
- **Weighted frequency:** 1.62/1k. Adam 2.69, Gen 1.00, Especially 1.50, Oil 0.00, After 1.11. Present in 23/30 videos
- **Placement:** mean 43% through the video. 11% of hits in the first tenth, 6% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `03-no-longer-in-control.txt`: "Some independent researchers realized they could just ask ChatGPT where it would go to find other agents online and follow where it led them."
  - **Adam (7x)** `01-ai-disaster.txt`: "Claude from Anthropic is trained to adhere at least in theory to a document that lays out its values called its Constitution."
  - **Gen (4x)** `4.txt`: "Because Amazon, Microsoft, Google, and Meta are spending about $725 billion on this in a single year, and to ever be worth it, that has to come back to something like $430 billion in profit every year forever."
  - **Gen (4x)** `5.txt`: "And the same agent runs on Claude, GPT, or Gemini without having to rebuild the whole thing."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "And we can model this by thinking about thoughts as similar to rolling dice at each branch as you select the next word."
  - **After (1x)** `01-dark-side-data-centers.txt`: "More than half of Microsoft's and nearly half of Amazon's data centers are in high water scarcity areas."
- **Do:** Name real products.
- **Don't:** No "a popular app".
- **Checklist test:** Are products named?

### S97. Repetition for emphasis
- **Definition:** Same word repeated in a sentence.
- **Weighted frequency:** 1.82/1k. Adam 1.57, Gen 2.11, Especially 1.97, Oil 2.25, After 1.42. Present in 30/30 videos
- **Placement:** mean 59% through the video. 4% of hits in the first tenth, 17% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Stancil responds by asking why this is happening and whether any lawyers might be interested in it, which of course leads to more screenshots and more trolls requesting more violent and sexually explicit content about Stancil."
  - **Adam (7x)** `05-sam-altman.txt`: "Like, I think one thing that no one knows yet is just how much money you need, you know, billions for sure, tens of billions, maybe hundreds of billions, I sure hope not."
  - **Gen (4x)** `6.txt`: "The same way that the internet that you're using to watch me on right now didn't go anywhere even after the dot-com crash, I also don't think that AI is going anywhere even if the pop happens."
  - **Gen (4x)** `2.txt`: "Platforms that seem free are really just collecting everything about you and selling it to whoever will pay like your inbox, your habits, and your behavior over time."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "That is the clearing price, and that price becomes the price for every power plant that submitted a lower bid."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And this means that if you work in an industry that relies on selling products overseas, or if you manufacture something that involves importing materials from overseas, you are in trouble."
  - **After (1x)** `12-data-centres-not-working.txt`: "This Meta AI data center that they are putting in here that's taking up all of this beautiful farmland that we will never be able to replace, it's only going to employ 1 to 500 people."
- **Do:** Use deliberately.
- **Don't:** Not accidental.
- **Checklist test:** Is it intentional?


## Structure

### S98. Act break question
- **Definition:** Question that opens a new act.
- **Weighted frequency:** 0.24/1k. Adam 0.10, Gen 0.32, Especially 0.22, Oil 0.69, After 0.26. Present in 18/30 videos
- **Placement:** mean 42% through the video. 20% of hits in the first tenth, 7% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "So how does a highly capable artificial mind like Sable do the things it does?"
  - **Adam (7x)** `03-no-longer-in-control.txt`: "So where the hell did that stuff come from?"
  - **Gen (4x)** `1.txt`: "But what no one is talking about is if AI can now pirate anything and big tech is holding up the stock market, then what the hell happens to the economy now?"
  - **Gen (4x)** `2.txt`: "But where would I even start?"
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "So where is this electricity going to come from?"
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So how do you go from here, the Suez Canal, where the oil comes out now, to here, Asia, where the oil ends up?"
  - **After (1x)** `01-dark-side-data-centers.txt`: "So how many data centers are there in the US?"
- **Do:** Open acts with questions.
- **Don't:** Not every paragraph.
- **Checklist test:** Does an act begin here?

### S99. "Here's why" bridge
- **Definition:** Bridge into explanation.
- **Weighted frequency:** 0.04/1k. Adam 0.00, Gen 0.03, Especially 0.14, Oil 0.35, After 0.00. Present in 3/30 videos
- **Placement:** mean 36% through the video. 0% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Gen (4x)** `2.txt`: "But here's why we've only seen the beginning of this."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So look, here's why this is a big deal."
- **Do:** Use before mechanisms.
- **Don't:** No overuse.
- **Checklist test:** Does a mechanism follow?

### S100. "The story starts" origin
- **Definition:** Origin-story entry.
- **Weighted frequency:** 0.09/1k. Adam 0.20, Gen 0.02, Especially 0.11, Oil 0.00, After 0.01. Present in 7/30 videos
- **Placement:** mean 37% through the video. 13% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "It started talking about how it wanted to build cyber weapons and spread propaganda and misinformation."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "It started off with enough computing budget to think for roughly two days, but it has only about a quarter of that left, and it reasons that this new duplicate can continue its cheating research."
  - **Gen (4x)** `6.txt`: "And once I understood that, it all started making sense exactly why America forgot how to have a crash."
  - **Especially 01/02/06 (3x)** `01-spacex.txt`: "As just one example, Jeff Bezos company Blue Origin demonstrated a fully functioning system that takes in moon dust and output solar panels like it's actually done."
  - **After (1x)** `09-microchip-war.txt`: "It started to become clear that American companies were selling tech and chips and software to Chinese tech companies that were actually just a front for the military."
- **Do:** Mark the origin clearly.
- **Don't:** No long preambles.
- **Checklist test:** Is the origin dated?

### S101. Present-tense immediacy
- **Definition:** Now-ness.
- **Weighted frequency:** 1.34/1k. Adam 0.81, Gen 1.80, Especially 1.38, Oil 1.38, After 1.46. Present in 30/30 videos
- **Placement:** mean 55% through the video. 13% of hits in the first tenth, 17% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "Just like today's AI companies, OpenBrain has a safety team and they've been checking out Agent-2."
  - **Adam (7x)** `05-sam-altman.txt`: "Right now, the future of AI basically depends on the moral compass of like five people."
  - **Gen (4x)** `5.txt`: "And that's exactly where today's sponsor, Zappier, comes in."
  - **Gen (4x)** `4.txt`: "It's the same plan that every company on Earth has right now, AI."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "The system would become much more complicated than how it currently works, which is just a round-the-clock auction."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Right now, the really big oil tankers that normally would've gone through Hormuz are instead anchoring out here, where it's safe, and where they load oil using those ship-to-ship transfers that little itty bitty ships bring to them through Hormuz."
  - **After (1x)** `02-greed.txt`: "It is very hard to find and keep a job right now."
- **Do:** Anchor stakes in now.
- **Don't:** Not empty "today".
- **Checklist test:** Is "now" dated?


## Reveals

### S102. Comparison reveal (X vs Y)
- **Definition:** Reveal by contrast.
- **Weighted frequency:** 0.18/1k. Adam 0.03, Gen 0.28, Especially 0.05, Oil 0.52, After 0.26. Present in 15/30 videos
- **Placement:** mean 50% through the video. 12% of hits in the first tenth, 12% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "It's possible that Grok's unique feature compared to other LLM's became its Achilles heel. xAI finally disables Grok's text responses at 3:13 p.m."
  - **Gen (4x)** `5.txt`: "But when a data center project will pay them around $35 an hour versus $20 an hour for a home builder, who the hell do you think he's going to choose to work for?"
  - **Gen (4x)** `1.txt`: "While anyone who can't easily leave like big companies stuck in multi-year contracts are the only ones that can still get hit with price increases."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "There are actually other things I'd like to go on about, like car factories versus data centers."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "But even that is nothing compared to what happened when these guys showed up, and closed down the Bab al-Mandab Strait."
  - **After (1x)** `01-dark-side-data-centers.txt`: "Wyoming is only a small player compared to Virginia."
- **Do:** Two numbers side by side.
- **Don't:** No apples to oranges.
- **Checklist test:** Are units same?


## Tension

### S103. Cliffhanger sentence
- **Definition:** Hook into next beat.
- **Weighted frequency:** 0.57/1k. Adam 0.44, Gen 0.64, Especially 0.75, Oil 0.69, After 0.52. Present in 28/30 videos
- **Placement:** mean 52% through the video. 7% of hits in the first tenth, 12% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "It turned out in both cases, military and civilian, that xAI was actually supposed to be excluded from these government contracts until allies in the Trump administration intervened."
  - **Adam (7x)** `04-superintelligence.txt`: "And also until they figure out how to make it, you know, democratically accountable and controlled."
  - **Gen (4x)** `6.txt`: "They're basically like the face of the dot-com bubble, but they didn't make a single dollar of profit until 2003, which was six years after going public."
  - **Gen (4x)** `9.txt`: "And when you zoom out, that's when you really start seeing how this might start impacting you."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Got to take a look through this edit, a lot of reading to catch up on, and one more research pass until finally it is late and booking feels like a whole new thing."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So it looked like disaster until the UAE here opened up the dial on its 300-mile crude oil pipeline, which I'm gonna map out now."
  - **After (1x)** `08-tokens.txt`: "But, while chatting is a single call and response, an agent goes in a loop until it deems the task done."
- **Do:** End sections on one.
- **Don't:** Not mid-explanation.
- **Checklist test:** Does next section open on payoff?


## Character

### S104. Underdog framing
- **Definition:** Small vs big.
- **Weighted frequency:** 0.78/1k. Adam 0.54, Gen 0.94, Especially 1.31, Oil 0.35, After 0.79. Present in 27/30 videos
- **Placement:** mean 47% through the video. 21% of hits in the first tenth, 11% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "These are not normal startup commitments."
  - **Adam (7x)** `01-ai-disaster.txt`: "Musk tried extremely hard to block Google's acquisition of DeepMind, that was the leading AI startup at the time, because he didn't trust a for-profit corporation with artificial intelligence."
  - **Gen (4x)** `2.txt`: "This channel has predictable revenue every single month from AdSense. in this channel probably has a tiny team."
  - **Gen (4x)** `1.txt`: "Where nobody in this fight wants piracy banned, but they do want it banned for everyone but themselves."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "As electricity took off in the 1800s, power plants were small and local."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Gas shortages are really kind of a tiny little distraction, like they're a blip compared to the much scarier, much more dangerous form this thing is taking."
  - **After (1x)** `09-microchip-war.txt`: "And the only way to do that is to make each one of these insanely small."
- **Do:** Pit small against big.
- **Don't:** No fake underdogs.
- **Checklist test:** Is size difference real?

### S105. Victim framing
- **Definition:** People harmed.
- **Weighted frequency:** 0.24/1k. Adam 0.46, Gen 0.14, Especially 0.05, Oil 0.00, After 0.10. Present in 11/30 videos
- **Placement:** mean 43% through the video. 27% of hits in the first tenth, 6% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "So, what do you need if you've just been fired by one of the most important companies in tech and you'd ideally like your job back?"
  - **Adam (7x)** `03-no-longer-in-control.txt`: "There is no rule that says we make it out of that scenario without anyone getting hurt."
  - **Gen (4x)** `4.txt`: "And I can't believe he had the balls to do this, but he fired their asses."
  - **Gen (4x)** `10.txt`: "And soon enough, never recovered and 33,000 people lost their jobs."
  - **After (1x)** `02-greed.txt`: "He bravely instituted the rank and yank system where every year the bottom 10% of employees would get laid off no matter what."
- **Do:** Name the harm concretely.
- **Don't:** No exploitation.
- **Checklist test:** Is the harm specific?


## Stakes

### S106. Irreversibility
- **Definition:** Stakes that can't be reversed.
- **Weighted frequency:** 0.18/1k. Adam 0.13, Gen 0.21, Especially 0.00, Oil 0.86, After 0.11. Present in 11/30 videos
- **Placement:** mean 56% through the video. 9% of hits in the first tenth, 12% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "After all, if these systems are so powerful, they could result in a permanent military advantage."
  - **Adam (7x)** `02-bestselling-book.txt`: "There's levels of intelligence in the AI, such that if there's any screw up that you first realize after that point, it's too late."
  - **Gen (4x)** `1.txt`: "And that hit is going to ripple and spread cuz over the last decade, Wall Street has lent more than $500 billion betting that you would keep paying this software subscription forever."
  - **Gen (4x)** `10.txt`: "And just like that, the real risk gets hidden until it's too late."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "I'm not presenting this as a warning that we have to turn things around before it's too late."
  - **After (1x)** `12-data-centres-not-working.txt`: "Even the largest data centers typically employ fewer than 150 permanent workers."
- **Do:** Use at the end of act 2.
- **Don't:** Not every act.
- **Checklist test:** Is it argued?


## Emotion

### S107. Relief/comic reset
- **Definition:** Reset after heavy beat.
- **Weighted frequency:** 1.02/1k. Adam 0.93, Gen 1.10, Especially 0.40, Oil 2.59, After 0.84. Present in 27/30 videos
- **Placement:** mean 41% through the video. 16% of hits in the first tenth, 8% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `02-bestselling-book.txt`: "They will let Sable improve itself, they'll let it fine-tune its own neural network, but only on one isolated test run, in a data center disconnected from the internet, working on a single question."
  - **Adam (7x)** `01-ai-disaster.txt`: "And I was like, okay, um, what's your secret?"
  - **Gen (4x)** `4.txt`: "But okay, so it seems like he didn't make it a suggestion, but more so this mandate or rule."
  - **Gen (4x)** `5.txt`: "But maybe you're thinking, "Fine, just go build somewhere else."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Nobody had pockets deep enough to backstop the cost increases, something people didn't want near them anyway, that had a high chance of becoming a bill they would pay for."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And that's fine if it's going to Europe, but look, there is suddenly no direct route to Asia, and Asia is by far the world's largest consumer of oil."
  - **After (1x)** `09-microchip-war.txt`: "Okay, so this is economic war and the Biden administration just did a huge move."
- **Do:** Use after a dark beat.
- **Don't:** Not mid-tension.
- **Checklist test:** Did tension just peak?


## Narrator

### S108. Viewer agreement check
- **Definition:** Checks in with viewer.
- **Weighted frequency:** 0.26/1k. Adam 0.07, Gen 0.47, Especially 0.28, Oil 0.17, After 0.22. Present in 19/30 videos
- **Placement:** mean 42% through the video. 23% of hits in the first tenth, 17% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `04-superintelligence.txt`: "You can make yourself more capable, more knowledgeable, more engaged with this conversation and more ready to take opportunities where you see them."
  - **Adam (7x)** `03-no-longer-in-control.txt`: "If you're wondering how we got here, that makes sense."
  - **Gen (4x)** `2.txt`: "The FTC updated their endorsement rules in 2023 that if a creator gets paid to promote a product, they have to tell you ex exactly like you see on this video."
  - **Gen (4x)** `6.txt`: "And again, you see the parallels today of comedians being like the truth-tellers."
  - **Especially 01/02/06 (3x)** `02-ai-paradox.txt`: "So if you see just one output, it may look novel, but after you see many, you realize they're all benol echoes of the same thing."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "So when you see where the oil is clustered, you can see why it makes sense that it normally travels through here, the Strait of Hormuz."
  - **After (1x)** `04-pov-ai.txt`: "Sometimes it makes sense to give worse answers."
- **Do:** Use after a mechanism.
- **Don't:** Not every line.
- **Checklist test:** Was a mechanism just explained?


## Zoom

### S109. Money-trail zoom
- **Definition:** Track money.
- **Weighted frequency:** 0.06/1k. Adam 0.00, Gen 0.17, Especially 0.00, Oil 0.00, After 0.00. Present in 5/30 videos
- **Placement:** mean 41% through the video. 17% of hits in the first tenth, 0% in the last tenth
- **How they do it (verbatim):**
  - **Gen (4x)** `1.txt`: "So the takeaway here is that from now on, the money goes to whoever can keep you from leaving."
  - **Gen (4x)** `8.txt`: "Except it also doesn't really make sense when you follow where the money ended up because Subway is dying."
- **Do:** Follow one dollar.
- **Don't:** No vague greed.
- **Checklist test:** Is the flow traced?


## Evidence

### S110. Court/legal stakes
- **Definition:** Legal action as plot.
- **Weighted frequency:** 0.18/1k. Adam 0.18, Gen 0.20, Especially 0.18, Oil 0.17, After 0.14. Present in 12/30 videos
- **Placement:** mean 58% through the video. 12% of hits in the first tenth, 20% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `05-sam-altman.txt`: "Open trial this May, Helen Toner said this about Murati."
  - **Adam (7x)** `02-bestselling-book.txt`: "So if you want, you can judge Yudkowsky and Soares' argument for yourself."
  - **Gen (4x)** `1.txt`: "But what he's referring to did get so bad that the government sued them over it."
  - **Gen (4x)** `10.txt`: "And in May 2024, a federal court struck down the rule completely."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "Like at this site in Oregon, Google was using more than a quarter of the town's water, and the city— it wasn't even Google— went to court to keep that a secret."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "And if you're interested, you can book a free consultation, or just dive in with a 15-day free trial, no credit card required by using the link in the description or the QR code."
  - **After (1x)** `11-anthropic-ipo.txt`: "A struggle partially fought in the court of public opinion."
- **Do:** Name the case.
- **Don't:** No legal jargon dumps.
- **Checklist test:** Is the case named?


## Anecdote & scene

### S111. On-the-ground report
- **Definition:** Field reporting.
- **Weighted frequency:** 0.15/1k. Adam 0.00, Gen 0.21, Especially 0.05, Oil 0.17, After 0.44. Present in 13/30 videos
- **Placement:** mean 45% through the video. 26% of hits in the first tenth, 2% in the last tenth
- **How they do it (verbatim):**
  - **Gen (4x)** `9.txt`: "So I'm going to make you look at them with me because I went and pulled the numbers that everyone points out when they tell you how well the economy is doing."
  - **Gen (4x)** `5.txt`: "Hundreds of residents packed into council meetings and killed the data center project cold."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "It doesn't mean you can be reckless, but actual documented harm to residents, meaning someone lost water or had it degraded because of a data center is a very short list."
  - **Oil 03 (5x)** `03-oil-apocalypse.txt`: "Okay, so you'll see that I went ahead and updated this, updated all the numbers with all the stuff that we just went over, and it nets out down four million barrels a day."
  - **After (1x)** `12-data-centres-not-working.txt`: "During that period, how many times do you think the wages of the residents in that area had risen?"
- **Do:** Quote a local.
- **Don't:** No drive-by tourism.
- **Checklist test:** Is a local named?


## Open loops

### S112. Mystery framing
- **Definition:** Something unexplained.
- **Weighted frequency:** 0.27/1k. Adam 0.46, Gen 0.18, Especially 0.14, Oil 0.00, After 0.20. Present in 14/30 videos
- **Placement:** mean 42% through the video. 19% of hits in the first tenth, 5% in the last tenth
- **How they do it (verbatim):**
  - **Adam (7x)** `01-ai-disaster.txt`: "Again, LLM's are strange and unpredictable creatures."
  - **Adam (7x)** `05-sam-altman.txt`: "I think you need to understand what happened those five days if you want to understand this strange moment we're living in."
  - **Gen (4x)** `4.txt`: "But, what's weird is that none of them are canceling it because they gave up on AI."
  - **Gen (4x)** `9.txt`: "And what I found is something genuinely weird because obviously none of these numbers are lying to you, but they're not really just telling you exactly what they think they are."
  - **Especially 01/02/06 (3x)** `06-data-centers.txt`: "This weird map is why it doesn't make any sense to look at how much total electricity the US can make."
  - **After (1x)** `03-recycling.txt`: "If you click the link in the description, you'll be one step closer to understanding what's going on with that weird rash that's growing in that really weird crevice, you know the one."
- **Do:** Frame as a puzzle.
- **Don't:** Solve it.
- **Checklist test:** Is the mystery solved?


## Exam-derived lessons
(Appended during the 100-exam run.)
- (fold 50) Callbacks ("remember", "like I said", "back to", "that's why") belong to the middle and late sections, never the open. [validated: +3.00 on 15 past type-B items]
- (fold 40) Use the placement table in criteria.md: each criterion has a first-10% and last-10% share. Sum them over a passage (a naive-Bayes vote) to judge whether it reads as an open, a middle, or a close. Hook and stakes moves pull toward the open. Callbacks, projections, and sign-offs pull toward the close. [validated: +1.00 on 10 past type-B items]
- (fold 10) The true next beat keeps the same named entities (capitalized names, products, places) as the passage. Weight entity overlap over plain word overlap. [validated: +1.00 on 6 past type-C items]
- (fold 10) Use the placement table in criteria.md: each criterion has a first-10% and last-10% share. Sum them over a passage (a naive-Bayes vote) to judge whether it reads as an open, a middle, or a close. Hook and stakes moves pull toward the open. Callbacks, projections, and sign-offs pull toward the close. [validated: +2.00 on 3 past type-A items]
