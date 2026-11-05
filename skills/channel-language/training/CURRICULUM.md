# Training curriculum (channel-language)

Learn it, don't just read it. Run this before the first real writing task in a new session, and again after any long break.

## Protocol (follow exactly)
1. Read SKILL.md, then references/criteria.md (skim), then 10 examples per creator from references/examples.md, out loud in your head.
2. For each level L1 to L5: **write all your answers first** in a scratch block without looking at the answer key. Then open `answer-keys.md`, score yourself with `rubric.md`, and write every miss into `lessons-learned.md` as: `date | level | item | what I did | what the real text does | rule I'll follow`.
3. Pass marks: L1 90%, L2 70%, L3 85%, L4 avg 4/5, L5 avg 4/5. If you fail a level, re-read the criteria your misses point to, then redo **only the missed items** plus 5 new items from references/examples.md (mask or transform them yourself the same way).
4. Before writing for real, re-read your last 10 lines of lessons-learned.md.
5. Do not peek. If you saw the answer before answering, mark the item "contaminated" and don't count it.

## Levels
- **L1 Recognition** (`L1-recognition.md`): spot every AI tell in transformed sentences
- **L2 Cloze** (`L2-cloze.md`): restore the masked opener/filler in real host passages
- **L3 Discrimination** (`L3-discrimination.md`): which version is the real creator and which is AI
- **L4 Rewrite** (`L4-rewrite.md`): humanize AI-ified passages, gold originals in the key
- **L5 Production** (`L5-production.md`): write from briefs, score with the rubric, and compare against the cited real passages

Items are sampled by corpus weight (Adam 7x, Gen 4x, Oil 5x, Especially 3x, After 1x per file). Training passages are disjoint from the exam passages.
