# Method 3: Shuffle-reorder and rewrite-diff (VAL videos)

## Shuffle-reorder
Five passages from one video were shuffled. Restore the order with the position table, then check against the truth.

**adam video (Adam)**
- 8%: "But as long as your AIs are good at following instructions, then you're fine. The instructions …" → cues starts_connector, you, number, mechanism, contrast
- 12%: "But the authors who put together ExploitGym estimate that 30 to 40% of them are just …" → cues starts_connector, number, in_medias_res, past, hope, mechanism
- 25%: "So it's like, yes, that worked. Repeat this enough times and you can end up with …" → cues starts_connector, you, past, hedge_project, contrast
- 54%: "Over the next two days, a couple of agents pursued those private datasets in a relatively …" → cues past, stakes, mechanism, contrast, list_marker
- 64%: "OpenAI are among the best in the world at understanding and working with these models. If …" → cues question, past, superlative

**gen video (Gen)**
- 10%: "See for yourself, but the people back then sound and act exactly like us today. Because …" → cues you, we, number, in_medias_res, past, stakes
- 18%: "The point is, none of this stopped the fall, and less than 3 years, 89% of …" → cues callback, you, i_me, number, past, definite_unest
- 66%: "So, if SpaceX goes up 10% in a day, you make 20%. But, if it drops …" → cues starts_connector, you, i_me, number, in_medias_res, hedge_project
- 94%: "And right now, before any official crash, it's already happening. Last year, about 6% of Vanguard …" → cues starts_connector, callback, question, number, in_medias_res, past
- 99%: "This is not a course. This is a free newsletter in the video description that we …" → cues starts_anaphor, you, i_me, we, number, in_medias_res

**gen video (Gen)**
- 4%: "I bought a plane ticket I guess Yale got me that ticket Yale was my ticket …" → cues i_me, number, in_medias_res, past, contrast
- 11%: "closest to you against you my dad didn't talk to me for years uh my mom …" → cues you, i_me, past, reflective
- 27%: "sometimes government or you see this with Twitter or elsewhere and so um people then work …" → cues you, i_me, past, mechanism
- 55%: "reality in the context just how media can influence public opinion can student opinion also influenc …" → cues i_me, number, in_medias_res, past
- 58%: "court administration had to uh where Justice is blind and so that's why they had to …" → cues callback, i_me, past, mechanism, superlative

**esp video (Especially)**
- 10%: "It's an encoded debate. The oral Torah had to be spoken, discussed, regenerated each generation. Buddhist …" → cues starts_anaphor, past, mechanism
- 12%: "First with people, then with ourselves. Crying is the first step. When your child cries, he …" → cues you, future, stakes, contrast, superlative, list_marker
- 37%: "It's the Socratic method for learning to code. If you're serious about learning back-end development, Python …" → cues starts_anaphor, you, number, in_medias_res, hope, sponsor
- 68%: "Once you seed an AI with a unique persona, the same problem persists. If you ask …" → cues you, number, in_medias_res, past, hedge_project, contrast
- 92%: "And ironically, the only AI input that properly reflects me is the one that has been …" → cues starts_connector, you, i_me, past, stakes, mechanism

**after video (Others)**
- 8%: "The luxury resort. The ties to President Trump's family is now fueling a revolution in Albania. …" → cues number, past, hedge_project, definite_unest
- 16%: "In 1944, Enver Hoxha led the forces that liberated Albania from Nazi occupation. He established a …" → cues number, year_date, past, superlative, dated_start
- 34%: "Zvernec also includes private land. That was the site of a long-running dispute between a few …" → cues you, i_me, past, stakes, mechanism
- 86%: "In each case, Kushner is making the same mistake. He didn't have any understanding, he didn't …" → cues you, in_medias_res, hedge_project, mechanism, contrast
- 95%: "(gentle forlorn music ends) All right, thanks again for watching another episode of "Search Party." If …" → cues callback, you, i_me, past, hope, signoff

**after video (Others)**
- 5%: "It feels like just a few months ago, companies were pushing every employee to spend as …" → cues starts_anaphor, you, number, year_date, in_medias_res, past
- 8%: "Then, Uber placed a cap on employee AI spend, after going through their entire AI budget …" → cues starts_connector, callback, you, i_me, number, in_medias_res
- 27%: "“Which drives the real-world acceptance rate down between 10% and 30% of generated code.” GitClear found …" → cues starts_connector, number, past, contrast
- 44%: "According to NVIDIA: “The goal is to achieve the fastest processing time and lowest cost per …" → cues i_me, number, past, mechanism, contrast
- 72%: "With this in mind, you can see how easy it would be for employees to waste …" → cues callback, you, we, question, past, hope

**after video (Others)**
- 18%: "What is happening? This is magic. Oh, and it's not just tech bros in the sixties …" → cues we, question, in_medias_res, past, future, superlative
- 22%: "Oh, and look, it's Steve Jobs and Bill Gates. Yes. - They're using these more sophisticated …" → cues number, past, stakes, list_marker
- 43%: "Like to keep some perspective, look at this graph. This is the number of transistors on …" → cues you, we, number, year_date, in_medias_res, future
- 59%: "Lucky for them, in China, there's a blurry line between businesses and the military. It's all …" → cues we, past, contrast
- 78%: "Okay, so this is economic war and the Biden administration just did a huge move. Reminder …" → cues in_medias_res, past, future, mechanism, contrast

## Rewrite-diff
Take a real cold open, strip its OPEN cues (the date, the in-scene verb, the number), and see what is left. What remains reads as body text, which shows those cues are what make it an opener.

- original: "For 16 hours on Tuesday, July 8th, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown."
  - stripped: "July someth, Elon Musk's AI had what can only be described as a full-scale Nazi meltdown.". It loses its anchor and reads like the middle of a video.
- original: "In the year 2000, a 21-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being …"
  - stripped: "a some-year-old middle school dropout named Eliezer Yudkowsky set out to build machines smarter than any human being who had ever lived.". It loses its anchor and reads like the middle of a video.
- original: "So, software as we know it might be cooked."
  - stripped: "So, software as we know it might be cooked.". It loses its anchor and reads like the middle of a video.
- original: "Take a look at the YouTube channels that you're subscribed to."
  - stripped: "Take a look at the YouTube channels that you're subscribed to.". It loses its anchor and reads like the middle of a video.
- original: "So, let's buy a house together."
  - stripped: "So, let's buy a house together.". It loses its anchor and reads like the middle of a video.
- original: "So, come with me, you guys, to replace my employee with AI."
  - stripped: "So, come with me, you guys, to replace my employee with AI.". It loses its anchor and reads like the middle of a video.
- original: "Ladies and gentlemen, data centers are getting canceled."
  - stripped: "Ladies and gentlemen, data centers are getting canceled.". It loses its anchor and reads like the middle of a video.
- original: "90% of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth …"
  - stripped: "some of the stuff headed to space this year will be carried on a SpaceX rocket, but the useful space around Earth …". It loses its anchor and reads like the middle of a video.
