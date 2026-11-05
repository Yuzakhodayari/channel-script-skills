# Hook & close types (TRAIN, weighted, regex-classified; first 2 / last 6 sentences)

Heuristic first-match classifier, order as listed; treat as approximate.

| opener type | weighted % |
|---|---|
|claim/other|35|
|scene-date|30|
|memory/you-question|17|
|artifact-show|14|
|paradox|3|
|game/imagine|1|

| close type | weighted % |
|---|---|
|thesis+CTA|43|
|agency/ask|34|
|uncertainty|19|
|philosophical|4|

- [7.0] ai-in-context — We are no longer in control of the AI situation.: OPEN=paradox; CLOSE=thesis+CTA
- [7.0] ai-in-context — You really should, unfortunately, be worried about Sam Altman: OPEN=scene-date; CLOSE=thesis+CTA
- [6.0] ai-in-context — This best-selling book is freaking out national security advisors: OPEN=scene-date; CLOSE=agency/ask
- [1.0] art-of-the-problem — Public Key Cryptography: RSA Encryption: OPEN=claim/other; CLOSE=thesis+CTA
- [1.0] art-of-the-problem — Diffie-Hellman Key Exchange: OPEN=claim/other; CLOSE=thesis+CTA
- [3.0] art-of-the-problem — The Polymarket Paradox: OPEN=scene-date; CLOSE=agency/ask
- [4.0] art-of-the-problem — The Debt Paradox: OPEN=scene-date; CLOSE=agency/ask
- [4.0] art-of-the-problem — The Stock Market Always Wins: OPEN=claim/other; CLOSE=thesis+CTA
- [4.0] art-of-the-problem — I Gave ChatGPT a Body: OPEN=claim/other; CLOSE=agency/ask
- [3.0] art-of-the-problem — The Profit Paradox: OPEN=claim/other; CLOSE=thesis+CTA
- [3.0] art-of-the-problem — The Computer That Runs The World: OPEN=claim/other; CLOSE=agency/ask
- [2.0] coldfusion — AI Keeps Pissing Off Mathematicians: OPEN=claim/other; CLOSE=uncertainty
- [2.0] coldfusion — Why Building AI Data Centres Isn’t Working Anymore: OPEN=scene-date; CLOSE=thesis+CTA
- [3.0] coldfusion — Dropbox Was Worth $10 Billion. Then Everyone Left: OPEN=claim/other; CLOSE=uncertainty
- [1.0] economics-explained — How China Is Restarting Its Economy: OPEN=scene-date; CLOSE=thesis+CTA
- [1.0] economics-explained — How Old Money Kills Economies: OPEN=claim/other; CLOSE=thesis+CTA
- [3.0] especially-misc — The Airline Industry’s Problem with Absolutely Ancient IT: OPEN=scene-date; CLOSE=agency/ask
- [3.0] especially-misc — How to ████ ██ a Data Center: OPEN=claim/other; CLOSE=uncertainty
- [3.0] especially-misc — What They're Not Telling You About Data Centers: OPEN=claim/other; CLOSE=thesis+CTA
- [3.0] especially-misc — How SpaceX Is Making America Uncatchable: OPEN=claim/other; CLOSE=thesis+CTA
- [3.0] especially-misc — The AI Paradox: OPEN=claim/other; CLOSE=thesis+CTA
- [1.0] gen — Asking Harvard Students Thought-Provoking Questions: OPEN=scene-date; CLOSE=agency/ask
- [3.0] gen — WTF Is Happening To The Stock Market?: OPEN=claim/other; CLOSE=agency/ask
- [1.0] gen — Inside America’s Most Dangerous Cartel City (Police Tour) | PT. 1: OPEN=scene-date; CLOSE=agency/ask
- [1.0] gen — Gen Z's Social Skills Are Disappearing, Here's Why.: OPEN=scene-date; CLOSE=agency/ask
- [1.0] gen — How a False Accusation Almost Ruined my Life.: OPEN=claim/other; CLOSE=agency/ask
- [5.0] gen — How Private Equity Made Piracy Great Again: OPEN=memory/you-question; CLOSE=agency/ask
- [5.0] gen — Why Everyone Wants You To Believe AI is a Bubble: OPEN=memory/you-question; CLOSE=agency/ask
- [5.0] gen — How Slop Bowls Replaced Actual Food: OPEN=memory/you-question; CLOSE=agency/ask
- [1.0] gen — Inside America’s Most Dangerous Cartel City (Police Tour) | PT. 2: OPEN=scene-date; CLOSE=agency/ask
- [3.0] gen — Why Canceling Data Centers is Going Horribly Wrong: OPEN=claim/other; CLOSE=agency/ask
- [5.0] gen — WTF Is Happening to Delivery Apps?: OPEN=scene-date; CLOSE=uncertainty
- [5.0] gen — How This $110M Lawsuit Could End False Accusations Forever: OPEN=scene-date; CLOSE=agency/ask
- [1.0] gen — Overnight In America's Most Racist Town: OPEN=memory/you-question; CLOSE=uncertainty
- [1.0] gen — Birth Rates Are Falling. Here's Why.: OPEN=scene-date; CLOSE=agency/ask
- [5.0] gen — How Private Equity Will Break America (Like 2008): OPEN=scene-date; CLOSE=uncertainty
- [3.0] gen — Why Everyone Wants You To Believe The Market Is Crashing: OPEN=game/imagine; CLOSE=thesis+CTA
- [1.0] gen — I Investigated The Most Intense Israel vs Palestine Protest: OPEN=scene-date; CLOSE=agency/ask
- [3.0] gen — How Gambling Predicts the Next Recession: OPEN=memory/you-question; CLOSE=uncertainty
- [5.0] gen — How These Bullsh*t Companies Will Break America: OPEN=memory/you-question; CLOSE=agency/ask
- [5.0] gen — How Gambling Money Will Break America: OPEN=claim/other; CLOSE=thesis+CTA
- [1.0] gen — "Why ""Average"" Americans are Prepping for Society's Collapse": OPEN=scene-date; CLOSE=agency/ask
- [1.0] how-money-works — Why A National Debt Default Now Looks Genuinely Possible... (sort of): OPEN=memory/you-question; CLOSE=thesis+CTA
- [2.0] how-money-works — "How Sports Predicted ""The Everything Bubble""": OPEN=memory/you-question; CLOSE=uncertainty
- [2.0] johnny-harris — How Money Actually Works: OPEN=memory/you-question; CLOSE=thesis+CTA
- [2.0] johnny-harris — The American war machine, explained: OPEN=artifact-show; CLOSE=thesis+CTA
- [6.0] max-fisher — The oil apocalypse is here: OPEN=artifact-show; CLOSE=uncertainty
- [6.0] max-fisher — The US-Canada War has begun: OPEN=scene-date; CLOSE=uncertainty
- [5.0] max-fisher — What I’ve learned about China: OPEN=artifact-show; CLOSE=thesis+CTA
- [5.0] max-fisher — America's job market is collapsing: OPEN=artifact-show; CLOSE=thesis+CTA
- [6.0] max-fisher — North Korea just did the impossible: OPEN=scene-date; CLOSE=thesis+CTA
- [6.0] max-fisher — America’s housing crisis is deliberate: OPEN=artifact-show; CLOSE=agency/ask
- [5.0] max-fisher — The Iran oil shock is about to hit: OPEN=claim/other; CLOSE=thesis+CTA
- [5.0] max-fisher — The real reason dating is broken: OPEN=claim/other; CLOSE=agency/ask
- [3.5] maxinomics — Saudi Arabia Has Oil, America Has This: OPEN=artifact-show; CLOSE=philosophical
- [4.5] maxinomics — AI Was Supposed To Take Your Job. Why Hasn't It?: OPEN=scene-date; CLOSE=uncertainty
- [3.5] maxinomics — Was Elon Musk Right About Tesla?: OPEN=claim/other; CLOSE=uncertainty
- [3.5] maxinomics — How Their House Became Everyone’s Problem: OPEN=claim/other; CLOSE=thesis+CTA
- [3.5] maxinomics — Americans Are About to Get a Lot Richer: OPEN=claim/other; CLOSE=philosophical
- [4.5] maxinomics — Everyone is Suddenly Turning on Airbnb, Here's Why: OPEN=memory/you-question; CLOSE=thesis+CTA
- [4.5] maxinomics — It Was Saudi Arabia That Broke Iran, Not the US: OPEN=claim/other; CLOSE=thesis+CTA
- [4.5] maxinomics — China Will Never Beat Taiwan, Here’s Why: OPEN=memory/you-question; CLOSE=thesis+CTA
- [4.5] maxinomics — The Hidden Force That Made Everyone Wear Wide Leg Pants: OPEN=scene-date; CLOSE=thesis+CTA
- [3.5] maxinomics — America Will Be the Last Superpower, Here’s Why: OPEN=artifact-show; CLOSE=agency/ask
- [1.0] other — i’m pretty sure recycling isn’t real…: OPEN=claim/other; CLOSE=thesis+CTA
- [1.0] other — The $1 Trillion Problem Diamonds Can Solve: OPEN=artifact-show; CLOSE=philosophical
- [1.0] other — Why Anthropic’s IPO Is So Dangerous: OPEN=memory/you-question; CLOSE=thesis+CTA
- [1.0] other — Tech Is Permanently Redefining The Middle Class: OPEN=claim/other; CLOSE=philosophical
- [2.0] other — The Trump family’s corruption is backfiring: OPEN=claim/other; CLOSE=agency/ask
- [2.0] other — Exposing The Dark Side of America's AI Data Center Explosion | View From Above | Business : OPEN=claim/other; CLOSE=thesis+CTA
- [1.0] other — Uh oh, tokens are getting too expensive...: OPEN=claim/other; CLOSE=philosophical
- [1.0] patrick-boyle — The Bond Market Has Singled Out France: OPEN=memory/you-question; CLOSE=agency/ask
- [2.0] patrick-boyle — Turkey's $20 Billion Fund Collapse Explained: OPEN=scene-date; CLOSE=agency/ask
- [2.0] species — The First 48 Hours of an AI Civil War - A Realistic Scenario: OPEN=claim/other; CLOSE=uncertainty
- [2.0] species — 72-Hour AI Takeover: A Realistic Scenario: OPEN=artifact-show; CLOSE=thesis+CTA