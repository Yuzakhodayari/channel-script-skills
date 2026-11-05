import os
import json
W=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','skills')+'/'
FS=json.load(open('final_scores.json')); FS2=json.load(open('final_scores_round2.json'))
CK={
'channel-storytelling':"""## v2 checklists (learned with 5 methods, validated on held-out videos)

**Cold open check.** Do this before writing line 1.
- [ ] The first line carries an anchor: a date or duration ("For 16 hours on Tuesday…"), a hard number, a named person or company in scene, or a direct viewer frame ("Take a look at…", "I'm sure you've heard…").
- [ ] It does NOT open on a connector or anaphor (And/But/So it/This/They). Exception: Gen's "So, let's…" invitation.
- [ ] No mechanism explanation and no hedged projection ("could", "might") in the first two lines. Those are body cues; see `references/position-signatures.md`.
- [ ] Line 2 escalates the same thread. Do not jump to context.

**Placement check.** Use it for "where does this go?"
- [ ] Past-tense, dated, in-scene narration goes in the open or middle.
- [ ] Reflection, future, hope, agency and callbacks to the opener go in the close (last 15%).
- [ ] When no cue fires, it is middle. That is the base rate, so never default to the close.

**Next-beat check (continuity).**
- [ ] The next line reuses a content word or entity from the last line (topic thread).
- [ ] It introduces at most one new named entity.
- [ ] It is not a generic line that could sit in any video.

Training material: `training/method1-contrastive-pairs.md`, `references/position-signatures.md`, `training/method3-shuffle-reorder.md`, `training/worked-examples.md` (36), `training/rule-log.md`.
""",
'channel-structure':"""## v2 checklists

**Beat position table** (median % of runtime, TRAIN videos): PROMISE/ROADMAP 6, SPONSOR 42, SECTION TURN 50, CONCLUSION 78, CTA 99.
- [ ] **Unmarked hook-end rule:** a line with no beat cue and no question closes the cold open, at about 6%. Never park uncued lines at 50%.
- [ ] A mid-video CTA (no "thanks for watching", "see you" or "bye") is still placed late. These creators rarely CTA mid-video, except through a sponsor bridge.
- [ ] A sponsor bridge ("that's exactly why…", "speaking of…") is placed between 15% and 90% and is labelled SPONSOR.
- [ ] Questions of 6 or more words mid-video are SECTION TURN re-hooks.

**Opener check (T3).**
- [ ] A real first sentence is shorter, often uses "you" or "I", and is not reflective or promise-like.
- [ ] Openers in the blend are of one kind: dated event, viewer instruction, number fact, invitation ("So, let's…") or sweeping claim.

**Reorder check (T6).** Map each beat to its table position and sort. Ties go in this order: promise, then turn, then conclusion, then CTA.

Training material: `references/position-signatures.md`, `training/method1-contrastive-pairs.md`, `training/method3-shuffle-reorder.md`, `training/worked-examples.md` (36), `training/rule-log.md`.
""",
'channel-audience':"""## v2 checklists

**Close vs mid (A4).** The close is where agency lives.
- [ ] The close uses hope, agency and choice words ("can", "could", "still", "together", "matter", "future").
- [ ] Mid-video text is past narration, dense with named entities, and opens on anaphors ("It", "This", "They").
- [ ] Do not end on fear. End on what the viewer can do or watch for.

**Hook vs mid (A2).**
- [ ] A hook line is self-contained: a dated start, a demonstrative ("This is a diamond…"), or the channel's open vocabulary.
- [ ] A hook line does not use "but", "however" or "instead". Contrast words are a body signature.
- [ ] Note: one line taken alone is often ambiguous. Judge hooks in a 2-3 line window.

**Mode (A3).** Adam: low "I", few numbers, in-scene narration. Gen: high "you" and "I", profanity, callbacks. Mechanism (Oil, Especially): number-dense, definite explanatory. Others: first-person essay.

**Realness (A5).** The real line keeps "you", spoken connectors (So, And, But), questions and intensifiers. A flattened line removes them.

Training material: `references/position-signatures.md`, `training/method1-contrastive-pairs.md`, `training/method3-shuffle-reorder.md`, `training/worked-examples.md` (35), `training/rule-log.md`.
""",
}
for k,txt in CK.items():
    p=W+k+'/SKILL.md'; s=open(p).read()
    if '## v2 checklists' in s: s=s[:s.index('## v2 checklists')]
    open(p,'w').write(s.rstrip()+'\n\n'+txt)
print('done')
