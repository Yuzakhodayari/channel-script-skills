# Contrastive pairs (Method 1) — real TRAIN passage vs flattened AI version

Each pair: the AI version says the same facts. The diff list is what the creator does that the model doesn't.

## Pair 1 — AIC (Altman firing, train, w7)
AI: "On November 17th, 2023, OpenAI's board unexpectedly removed CEO Sam Altman, a decision that sent shockwaves through the technology landscape."
REAL (paraphrase-faithful): "Friday, November 17th, 2023. Sam Altman is in Las Vegas. He gets a text asking him to join a call at noon. It is not a routine call."
Diff: present tense; date as a header fragment; place + device detail; the drama is withheld into a 5-word punch; no cliché ("shockwaves", "landscape").

## Pair 2 — Gen (piracy, train, w5)
AI: "Streaming services have become increasingly expensive and fragmented, leading many consumers to reconsider piracy."
REAL style: "Remember this? Back when Netflix was ten bucks and had everything? Yeah. Now you need four subscriptions to watch one show, and the price keeps going up. So people are doing what they did in 2005. They're pirating again."
Diff: opens on a shared memory; question + one-word answer; second person; concrete price; And/So starters; time-anchor (2005).

## Pair 3 — Fisher (North Korea, train, w6)
AI: "North Korea's cyber operations generate significant revenue relative to its economy."
REAL style: "They stole about $1.5 billion in one heist. For North Korea, that is enormous. It would be like if the US pulled in trillions of dollars from a single trade deal."
Diff: one number, then a rescaling analogy to the viewer's country; "It would be like if…".

## Pair 4 — Maxinomics (AI and your job, train, w4.5)
AI: "Many jobs consist of a variety of routine digital tasks that could be automated."
REAL style: "Think about what you actually do all day. Menus. Clicking buttons. Messaging. Sorting. Waiting on hold."
Diff: imperative to the viewer; fragment list; physical verbs; zero abstraction nouns.

## Pair 5 — AotP (debt paradox, train, w4)
AI: "Modern money is fundamentally based on debt and trust in institutions."
REAL style: "Imagine a village with no money. A farmer has rice. A smith has tools. Now one of them writes an IOU."
Diff: toy model; staged one-step-per-sentence; the abstract claim arrives only after the model.

## Checklist distilled from the pairs
1 abstraction→object; 2 summary→scene; 3 balanced compound→short+punch; 4 add viewer ("you"/"remember"); 5 add one rescaling comparison; 6 strip the cliché noun; 7 one starter of And/So/But per ~6 sentences.
