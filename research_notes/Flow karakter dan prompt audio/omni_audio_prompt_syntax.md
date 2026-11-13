# Gemini Omni 1.2 Flash: audio prompt syntax reference (dialogue, VO, SFX, ambience, music, lip-sync) as of 13 Nov 2026

Source-grade key used below: [OFFICIAL] = Google-owned docs (aistudio.google.com, docs.cloud.google.com). [VENDOR] = third-party API host or tool vendor docs. [COMMUNITY/UNVERIFIED] = blogs, tutorials, forum posts. Nothing in the community tier has been confirmed by Google.

Not reached: the Reddit r/GeminiAI "trial and error" post (scraper blocked; only the search snippet "You write Dialogue: [line], SFX: [sound], Ambient: [background] in the prompt and it generates all three in sync" was visible), the blog.google announcement, the DeepMind model card, and Flow help-center pages. None of these were read directly. Where I cite them, it is through secondary sources.

## 1. What Google's official docs say about audio, dialogue, timecodes, "single continuous shot", "no dialogue", "Keep everything else the same", and edit/extend turns

### Takeaway
The AI Studio Omni doc (model `gemini-omni-1.2-flash`, up to 15 s with native audio) gives only light audio guidance: audio is on by default, you steer it in natural language, and negatives go in the prompt. The most specific official dialogue syntax is in Google Cloud's "Best practices" and "Video generation prompt guide". It says to write speech with a colon after the speaker and WITHOUT quotation marks. Several vendor guides do the opposite (quoted lines), so this is an unresolved conflict. Test both.

### Cited Findings
- Omni 1.2 Flash generates "synchronized video and native audio up to 15 seconds long". Duration is any whole second from 3 to 15, default 10 s. A `duration` set in `response_format` overrides any length mentioned in the prompt text. — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Audio default and music: "By default the model will try to generate an appropriate audio track for a video. This might not always be what you want. You can use your prompt to describe the type of audio you want. This is especially important if you want music in your video." Official examples: "Include calm background music" / "The video has a high energy techno beat" / "The audio is a low tinny radio broadcast in the background, playing a song". — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Removing unwanted elements, official negatives: "No dialogue", "No embellishments", "No extra sound effects". — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- No negative-prompt parameter: "System instructions, temperature, top_p, stop sequences, and negative prompts are not supported (you can put your negatives in the regular prompt: e.g., "Do not do X")." — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Official single-scene and audio example, verbatim: `Continuous, unbroken handheld shot of a fluffy tabby cat sitting on a sunny windowsill, looking out into a leafy garden. The cat's tail twitches slowly, and its ears rotate slightly toward ambient noises. Sunbeams illuminate dust motes in the air. Sound design: Gentle breeze, distant bird chirps. No dialogue.` — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Official single-shot phrases: "In a single unbroken scene", "In a single continuous shot", "No scene cuts". The doc says Omni by default "will try to create a video with a few different shots". — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Official timing, natural language: "After 3 seconds, a woman enters the scene." / "At 5s the chorus starts in the background audio." / "Every 2s cut to a new frame." / "In a rapid fire sequence, every half a second (12 frames at 24fps) change the scene to a new location." The doc says "there is no precise syntax needed".
- Official timecode blocks (verbatim):
  ```
  [0-5s] A person is walking down a quiet street
  [5-10s] They stop and turn around toward a glowing doorway
  [10-15s] They start running into the portal
  ```
  — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Official edit prompts: "Make this video anime", "Put a fashionable hat on this person". "When editing a specific aspect of the video, include "Keep everything else the same" to maintain visual consistency." Official before/after: "Add a cat that jumps onto his lap, he begins to pet it. Keep everything else the same." and "Make the phone invisible. Keep everything else the same." — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Extension audio: "Describe the audio in your extended scene, especially if you need it to change: "The music continues into the chorus"". Timestamps in an extension restart: "0s refers to the beginning of the extended part of the video" (e.g. "After 2s cut to a new scene with the same characters" on a 10 s video cuts at 12 s). — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Extension covers 3 to 10 s per turn, up to 30 s total, using the last 10 s of the input as context. — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Dialogue limits in editing and extension: you cannot extend an uploaded video where someone is talking to add dialogue. Speech on extension works only for model-generated videos via `previous_interaction_id`. "Voice editing is not supported." "Uploading audio inputs or audio references is unsupported". Audio inside a reference video is ignored. — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Deprecated control strings: "Do not include control strings (such as <FIRST_FRAME>, <LAST_FRAME>, <IMAGE_REF_0>, or <VIDEO_REF_0>) in your text prompts. These tags are deprecated and unsupported in future models. Describe how each image or video should be used in natural language instead." — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Dialogue syntax (the key official rule). Google Cloud best practices, "Avoid quotation marks": "To prevent the model from rendering text in the video, use a colon (:) after the speaker's action to denote speech and avoid using quotation marks ("). Not recommended: A woman says: "My name is Clara." Recommended: A woman says: My name is Clara." The page covers "Gemini Omni and Veo videos"; last updated 2026-11-12. — [Google Cloud: Best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)
- Official voice/character consistency recipe: give the character a name and a specific voice style, paste the identical character description into every scene, and vary only the action and setting. The official voice clause is: "In a voice that is crisp and clear, with a thoughtful, analytical tone and a standard American accent, Clara says: It has to be here". The page also suggests "Use the same seed parameter" for visual and voice consistency, but the AI Studio Omni page lists no seed parameter (see Gaps). — [Google Cloud: Best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)
- Official audio element list: "Clearly specify if you want audio. We recommend that you use separate sentences in your prompt to describe the audio." Examples: SFX "the sound of a phone ringing"; ambient "the sounds of city traffic and distant sirens"; dialogue "the man in the red hat says: Where is the rabbit?"; narration "a voiceover with a polished British accent speaks in a serious, urgent tone". — [Google Cloud: Video generation prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide)
- Official multi-speaker example, unquoted and colon-based: `The seasoned detective says: Your story has holes. The nervous informant, sweating under a single bare bulb, replies: I'm telling you everything I know. The only other sounds are the slow, rhythmic ticking of a wall clock and the faint sound of rain against the window` — [Google Cloud: Video generation prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide)
- One-scene rule: for short videos, "Trying to chain multiple distinct events (A then B then C) in one prompt for a short video often leads to muddled or incomplete videos." — [Google Cloud: Best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)
- Conflict inside Google's own docs on negatives. The Cloud prompt guide (which also covers Veo) says "no"/"don't" wording is "Not recommended" and that you should instead list what you do not want ("wall, frame"). The AI Studio Omni doc says to put negatives in the prompt and gives "No dialogue" / "Do not do X" style examples. For Omni, follow the AI Studio doc (it is model-specific); the Cloud negative-prompt section appears to be Veo-era. — [Google Cloud: prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide); [AI Studio](https://aistudio.google.com/docs/omni)

### Inferences
- Safest official-aligned dialogue template is `[Visible speaker description] says: <line, no quotes>`, with voice style stated in an "In a voice that is ..., [Name] says: ..." clause. This is derived from the Cloud docs, not from AI Studio.
- To keep audio separate from visuals, put audio in its own sentence(s) ("Sound design: ... No music.") as Google suggests and uses in the tabby-cat example.
- Because timecode origin resets on extension, per-turn prompts should restart at [0-...s].

### Gaps
- blog.google announcement, DeepMind model card/prompt guide, and Flow help-center text were not read directly. Flow-specific UI (for example, a voice or character field) is undocumented in what I found.
- The AI Studio doc never says anything about quotes vs colons, so the Cloud rule is the only official source; its model scope is "Gemini Omni and Veo".

## 2. Prompt structure used by experienced creators, plus real example prompts with sources

### Takeaway
Credible vendors converge on layered prompts: subject, action, setting, camera, lighting, then an explicit audio layer, then exclusions. Timecode blocks are used for multi-beat prompts. Every example below is a text prompt; none has been independently verified to produce the claimed audio. Vendors disagree with Google on quoting dialogue.

### Cited Findings
- Runware (Omni 1.2 API host) states six layers "subject, action, setting, camera, lighting, and audio" plus a closing exclusions clause. "Any layer you skip is left to the model... Without the audio clause, it picks its own music and sound." Runware says there is no audio parameter and "no negative prompt". — [Runware: Omni 1.2 prompting guide](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting) [VENDOR]
- Hoox says short prompts and iteration work better than long ones, and splits a prompt into six dimensions: camera framing, style, lighting, scene, action, audio. It states its tips "are not official Google specs." — [Hoox guide](https://www.hoox.video/en/blog/gemini-omni-flash-the-ultimate-guide-to-googles-video-model-2026) [COMMUNITY/UNVERIFIED]
- Morphic (an Omni 1.1 guide): the audio lever is "No music, just room tone. Or a spoken line"; its reason is "Silence must be asked for, or you get invented music". It says timecode ranges "are budgets, not frame-accurate edit points", and that undefined on-screen text gets invented. — [Morphic guide](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide) [COMMUNITY/UNVERIFIED, written for 1.1]
- Promptslove (Nov 2026 tool page for 1.2) recommends 30 to 80 words, saying "past ~100 words you start fighting the model". It also claims pixel-level camera specs (ISO, f-stop, mm) degrade results, and that "explicit negation stopped unwanted stock music in about half of documented tests". Those are the site's own claims and the underlying tests are not cited. — [Promptslove Omni 1.2 generator](https://promptslove.com/free-tools/google-omni-prompt-generator/) [COMMUNITY/UNVERIFIED]

Example prompts (all verbatim from the cited source; label shows credibility):

1. [OFFICIAL] Tabby cat, SFX + ambience + "No dialogue" — see Section 1 above. [AI Studio](https://aistudio.google.com/docs/omni)
2. [OFFICIAL, Cloud docs] Dialogue, two speakers, unquoted: the detective/informant prompt in Section 1. [Google Cloud prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide)
3. [OFFICIAL, Cloud docs] Named character with voice clause: "...In a voice that is crisp and clear, with a thoughtful, analytical tone and a standard American accent, Clara says: It has to be here" (full scene prompt in the source). [Google Cloud best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)
4. [VENDOR] Runware, dialogue to camera, quoted, 8 s:
   `The owner of a small dog-grooming salon, a woman in her forties with short gray hair and a navy apron, stands beside a grooming table where a freshly groomed white poodle sits. Single continuous shot, medium close-up at eye level, static camera. She smiles and says to the camera: "We just opened on Maple Street. Book this week and get twenty percent off your first groom." Audio: her voice clear and close, with the soft hum of a dryer and a collar jingling in the background. No music. No subtitles.` — [Runware](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting)
5. [VENDOR] Runware, off-screen voiceover while the on-screen person stays silent, music genre+mood:
   `A man in his fifties in a gray T-shirt does a guided stretching routine on a yoga mat on a sunny apartment balcony in the early evening, following the app on a phone propped against a plant pot. He reaches both arms overhead, then folds forward into a slow hamstring stretch. Single continuous shot, the camera drifting slowly closer at waist height. Audio: a calm female voiceover, the app's coach, says: "Reach up tall. Now fold forward slowly and let your breath do the work." Soft piano music with a warm, unhurried mood, and quiet city traffic far below. He does not speak. No subtitles.` — [Runware](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting)
6. [VENDOR] Runware, timecode block with an audio line, 8 s:
   `A road cyclist in a yellow jersey and white helmet climbs a mountain pass on a clear summer afternoon.` / `[0-3s] Wide aerial shot of the switchback road as she rounds a hairpin bend.` / `[3-6s] Low close-up from the roadside as she rises out of the saddle and powers past the camera.` / `[6-8s] Front view at the top of the pass as she sits up, raises both arms and smiles.` / `Audio: wind, the whir of the chain and her hard breathing over a driving rock beat that builds to the top. No dialogue. No on-screen text.` (one timecode per line) — [Runware](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting)
7. [VENDOR] Runware, single-sentence "hero" prompt with every layer: `A trail runner in her early thirties wearing a coral tank top and black running shorts, running at a steady pace along a narrow gravel path, on a grassy coastal clifftop high above a blue ocean, one continuous tracking shot from the side at hip height with no cuts, low early-morning sun behind her with a warm rim light on her hair and shoulders, the sound of her footsteps crunching on gravel, her steady breathing, waves breaking far below and an upbeat indie-pop track, no dialogue and no on-screen text.` — [Runware](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting)
8. [VENDOR] Atlas Cloud, two-speaker script with labels, 12 s:
   `Dialogue, spoken exactly in this order:` / `Speaker A: "Can we publish the page now?"` / `Speaker B: "Almost. One link needs fixing."` ... then `Only the named person speaks each line. The listener stays silent and reacts naturally. Keep each voice attached to the same person throughout. Show the correct mouth moving for every line, with brief natural pauses. Quiet room tone. No narrator, third voice, subtitles, music, or logos.` The article itself says the supplied videos' words and lip-sync "have not been independently verified". — [Atlas Cloud: multi-speaker dialogue](https://www.atlascloud.ai/blog/tips/gemini-omni-1.2-flash-multi-speaker-dialogue) [COMMUNITY/UNVERIFIED]
9. [COMMUNITY/UNVERIFIED] AutoWeeb, anime slice-of-life, 9:16, timecodes + sound design + dialogue (written for the preview model, uses now-deprecated tags):
   `<FIRST_FRAME> [0-3s] Medium shot, a lavender-haired student in a navy school blazer stands at a vending machine, warm afternoon light through the window. She selects a canned coffee. [cut to a new scene] [3-6s] Close-up of her face as she takes a sip, eyes softening. Sound design: vending machine hum, distant school bell, no music. She says quietly: "today was long." No extra sound effects.` — [AutoWeeb anime guide](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash)
10. [COMMUNITY/UNVERIFIED] Atlas Cloud 5-part tag formula for image-to-video: `[Subject]: ... [Motion]: ... [Camera]: ... [Style]: ... [Audio]: Heavy downpour, distant thunder, and a soft sigh.` — [Atlas Cloud I2V tips](https://www.atlascloud.ai/blog/tips/gemini-omni-flash-1.1-image-to-video) (seen in search snippet only)
11. [COMMUNITY/UNVERIFIED] Promptslove templates (dialogue after a colon; trigger-anchored SFX): `...says: [LINE OF DIALOGUE, UNQUOTED]` / `Sound design: [AMBIENT BED] kept low under the voice. No music. In a single continuous shot.` and `Add [SOUND, e.g. soft harp notes] synchronized to exactly when [TRIGGER EVENT, e.g. the hand touches each fern leaf]. Underneath: [AMBIENT BED...]. No music, no dialogue, no narration.` — [Promptslove](https://promptslove.com/free-tools/google-omni-prompt-generator/)
12. [COMMUNITY/UNVERIFIED] Hoox, French UGC voiceover and lip-sync: `Close-up, iPhone UGC style, natural window light. A woman holds a face cream in her bathroom. She smiles and shows the jar to the camera. Voiceover in French: "Three weeks, and my skin has changed." Ratio 9:16.` — [Hoox](https://www.hoox.video/en/blog/gemini-omni-flash-the-ultimate-guide-to-googles-video-model-2026)
13. [COMMUNITY/UNVERIFIED] GitHub awesome list (Flaq AI), per-recipe audio lines: `Audio: close tire crunch and chain movement, strong ridge wind, one distant bird at 7s. No music or narration.` and a timed exact line in Japanese: `Exact dialogue at 6s, spoken once with natural conversational pacing: "今日は、遠回りして帰ろう。"` — [flaqai/awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) (written for 1.1)

### Inferences
- The only element all sources agree on is: state the audio layer explicitly, in its own sentence, with explicit exclusions.
- Vendor "Audio: ..." and "Sound design: ..." prefixes are consistent with Google's own "Sound design:" example, so they are low risk.
- The quoted-vs-unquoted question is open. A practical A/B: run the same 8 s clip with `says: line` and `says: "line"` and watch for burned-in text and the spoken result. This is my recommendation, not a documented procedure.

### Gaps
- No Reddit/X/Flow-user prompts with outputs confirmed could be fetched (Reddit and X blocked). The r/GeminiAI "Dialogue:/SFX:/Ambient:" prefix syntax is known only from a search snippet (see [Reddit post](https://www.reddit.com/r/GeminiAI/comments/1tzu0uo/after_a_lot_of_trial_and_error_with_gemini_omni/)). Treat as unverified.
- None of the vendor example prompts were run by me, so no output verification.

## 3. Documented limits (words per clip, speech rate, lip-sync accuracy, languages, voice consistency, music leakage, text artifacts)

### Takeaway
There is no official words-per-second limit. Only English is "fully supported"; other languages "may work but results can vary". Google claims clearer lip-sync and distinct multi-speaker conditioning in 1.2, but no accuracy number was found.

### Cited Findings
- Language: "English (EN) is fully supported, but other languages have not been evaluated, so they may work but results can vary." — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Clip length: 3 to 15 s (default 10 s). First/last-frame interpolation 3 to 10 s. Extension adds 3 to 10 s per turn up to 30 s total. — [AI Studio: Omni docs](https://aistudio.google.com/docs/omni)
- Google's 1.2 claims, via a secondary source: "more fluid dialogue, clearer lip sync, and distinct multi-speaker conditioning" (announced 5 Nov 2026). Atlas Cloud adds that "a prompt cannot guarantee clean speaker assignment on the first render". — [Atlas Cloud](https://www.atlascloud.ai/blog/tips/gemini-omni-1.2-flash-multi-speaker-dialogue) [COMMUNITY/UNVERIFIED]; also corroborated by Promptslove's summary [Promptslove](https://promptslove.com/free-tools/google-omni-prompt-generator/)
- Words per clip: no official figure. Runware advises "keep it to what a person can say comfortably in the clip, here two short sentences in eight seconds". Atlas Cloud's eight-turn, 15 s cafe script is described as "the most demanding timing test" and "not a universal words-per-second threshold". — [Runware](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting); [Atlas Cloud](https://www.atlascloud.ai/blog/tips/gemini-omni-1.2-flash-multi-speaker-dialogue) [VENDOR/UNVERIFIED]
- Voice persistence: Morphic says dialogue comes back "in a voice that persists across edits and extensions" (Omni 1.1 guide). Google's own recipe for consistency across separate clips is the repeated name plus identical voice clause (Section 1). — [Morphic](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide) [COMMUNITY/UNVERIFIED]
- Non-Latin on-screen text: Morphic reports Japanese and Chinese glyphs "render as convincing inventions" (1.1). This concerns text in frame, not speech. — [Morphic](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide) [COMMUNITY/UNVERIFIED]
- Four or more tracked subjects "merge or drift" (1.1); hold to three. — [Morphic](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide) [COMMUNITY/UNVERIFIED]
- Silence has to be requested: "Silence must be asked for, or you get invented music" ([Morphic](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide)); "Omni Flash still generates ambient audio" and is "more likely to add character dialogue ... even when you did not ask" than Seedance 2 ([AutoWeeb](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash)) [COMMUNITY/UNVERIFIED].
- Language/accent drift report: a Google AI forum user generated a non-English video and "the accent sounds very different"; the thread got no solution (a Google staffer redirected to Flow feedback; a later poster says "so there is still no solution"). Date: Aug-Oct 2026, may predate 1.2. — [Google AI forum: Lip Sync in Google Flow](https://discuss.ai.google.dev/t/lip-sync-in-google-flow/179960)
- Non-English wins reported on Google's own showcase page (as seen in a search snippet): a partner quote about "accurately rendered and synced Punjabi spoken dialogue". Not read in full, treat as marketing. — [DeepMind Gemini Omni page](https://deepmind.google/models/gemini-omni/) (snippet only)
- Indonesian/Bahasa: I found no source with an Indonesian-language Omni dialogue test. The GitHub awesome list has a Bahasa Indonesia translation of its README (documentation only, not dialogue evidence). The list's own advice: "English is the only officially fully evaluated language. For production, keep shot, movement, and continuity control in English; lock dialogue and on-screen text verbatim in the target language; then approve each locale as a separate 360p draft." — [flaqai/awesome-gemini-omni-flash](https://github.com/flaqai/awesome-gemini-omni-flash) [COMMUNITY/UNVERIFIED]
- Pricing and drafts (useful for iteration): about $0.07 per second at 720p per Promptslove summary, not verified against Google's pricing page. — [Promptslove](https://promptslove.com/free-tools/google-omni-prompt-generator/) [COMMUNITY/UNVERIFIED]

### Inferences
- For Indonesian dialogue, the practical approach is the one the vendors suggest for any non-English: keep scene/camera control in English and put the exact target-language line after `says:`. State the language and accent explicitly (for example "says in Indonesian with a neutral Jakarta accent:"). The wording is an inference from Google's "voice that is ..., [Name] says:" pattern, not an official Indonesian recipe. Draft at 360p first to check pronunciation and lip-sync.
- Expect accent bleed toward English for non-English speech (supported by the forum report), so the accent clause is worth repeating.

### Gaps
- No quantitative lip-sync accuracy, speech-rate, or max-word data from Google.
- No verified Indonesian result.
- No data on music leakage rates beyond vendor claims.
- Whether the "same seed" advice in Google Cloud docs applies to Omni in Flow/AI Studio is unclear: the AI Studio Omni page lists no seed parameter and Runware says "There is no seed" for Omni 1.2 (Runware's page).

## 4. Known pitfalls and fixes (subtitles, speaker swaps, invented dialogue, music)

### Takeaway
Most fixes are prompt-level exclusions ("No subtitles", "No dialogue", "No music") plus naming each speaker and keeping one to two actions per clip. Unquoted speech is Google's stated way to avoid burned-in text.

### Cited Findings
- Burned-in text/subtitles from quotes (official rule): use `says: line` without quotation marks "to prevent the model from rendering text in the video". — [Google Cloud: Best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)
- Add explicit "No subtitles" / "No on-screen text": Runware prompts do this, and explain "'No subtitles' keeps captions out of the frame so you can add your own in the edit". — [Runware](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting) [VENDOR]
- Omni can also generate on-screen subtitles/titles on request ("add subtitles and titles"; Instagram reel about "animated 3D subtitles"), so subtitles are a controllable feature, not only an artifact. — [YouTube: 8 Insane Ways to Use Omni Flash](https://www.youtube.com/watch?v=6G5-tz6yiYs); [Instagram reel](https://www.instagram.com/reel/DZkbB4bKPNn/) (search snippets only) [COMMUNITY/UNVERIFIED]
- Voiceover vs on-screen speaker confusion: say who the voice belongs to and "He does not speak"; do not combine "No dialogue" with a requested voiceover ("leave out any that would contradict a layer you asked for"). — [Runware](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting) [VENDOR]
- Speaker swaps: give each speaker a visual position/clothing and a distinct voice; add "Only the named person speaks each line. The listener stays silent"; keep both faces visible in a continuous two-shot; change one variable per retry. — [Atlas Cloud](https://www.atlascloud.ai/blog/tips/gemini-omni-1.2-flash-multi-speaker-dialogue) [COMMUNITY/UNVERIFIED]
- Last line dropped or rushed: shorten the script or lengthen duration (within 15 s); "A long line invites rushing or omission near the end." — [Atlas Cloud](https://www.atlascloud.ai/blog/tips/gemini-omni-1.2-flash-multi-speaker-dialogue) [COMMUNITY/UNVERIFIED]
- Invented dialogue and music: negate explicitly ("No dialogue", "No music", "No extra sound effects"); Morphic and AutoWeeb both report the model invents audio otherwise. — [AI Studio](https://aistudio.google.com/docs/omni); [Morphic](https://morphic.com/resources/how-to/gemini-omni-flash-1-1-guide); [AutoWeeb](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash)
- Voice drift across edits: re-anchor with preservation clauses; Hoox suggests "Keep the character, their clothes, and voice the same." — [Hoox](https://www.hoox.video/en/blog/gemini-omni-flash-the-ultimate-guide-to-googles-video-model-2026) [COMMUNITY/UNVERIFIED]. Edit chains degrade after about four turns per Morphic and Promptslove.
- Mid-shot cuts hiding mouths: ask for "single continuous shot" (official); Runware's side-by-side shows the cut behavior without it. — [Runware](https://runware.ai/docs/models/google-gemini-omni-flash-1-2/guides/prompting)
- Warning on stale advice: MindStudio's "Google Flow / Omni" tutorial describes Veo 3-era behavior ("not precise sync", "plan to replace [audio] in post") and is not Omni-specific; do not use it as evidence about Omni 1.2. — [MindStudio](https://www.mindstudio.ai/blog/how-to-use-google-flow-gemini-omni-video-editing)

### Inferences
- A defensive audio tail for a silent-dialogue anime shot: "Sound design: [ambience]. No dialogue. No music. No subtitles. No extra sound effects." This combines official negatives with the vendor "No subtitles" and has not been tested by me.
- For speaker-swap risk, a colon-format script (official) plus per-speaker "name + clothing + voice" lines is the best-supported approach, even though Atlas's examples use quotes.

### Gaps
- No Flow-specific bug reports (subtitle artifacts, speaker swaps) were retrievable; Reddit blocked.
- No official statement that "No subtitles" is a recognized phrase; it is vendor-proven only.

## 5. Anime/2D audio and lip-sync

### Takeaway
There is almost no verified 2D-specific lip-sync guidance. The official Cloud guide lists "Japanese anime style" and "cel-shaded animation" as valid style terms, and the one anime-specific vendor guide says Omni tends to be "over-animated" on quiet scenes and over-eager to add dialogue. No source documents "limited animation" phrasing for mouths.

### Cited Findings
- Official style vocabulary: "Animation styles: "Japanese anime style", "classic Disney animation style," "Pixar-like 3D animation", "claymation style", "stop-motion animation", "cel-shaded animation"". Official anime example: `A dynamic scene in a vibrant Japanese anime style. A magical girl with silver hair and glowing blue eyes walks in a forest. The style features sharp lines, bright, saturated colors, and expressive` (as published, truncated). — [Google Cloud: prompt guide](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/video-gen-prompt-guide)
- Official restyle edit: "Make this video anime". — [AI Studio](https://aistudio.google.com/docs/omni)
- AutoWeeb (anime-focused vendor): Omni "can look over-animated compared to the calmer 24fps cadence Seedance 2 tends toward"; extra micro-movement in "hair, fabric, and facial expression"; a more anime-looking starting image helps; it "is more likely to add character dialogue ... even when you did not ask for it", so write "no dialogue" for silent characters; for speech, be explicit about what is said. It reports that explicit cut language "[cut to a new scene]" works. — [AutoWeeb](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash) [COMMUNITY/UNVERIFIED; written on preview model, uses deprecated tags]
- Image-to-video official rule (applies to anime stills): "Prompt for motion only" and refer to the character generically ("the subject", "she"); re-describing the image "confuse[s] the model". — [Google Cloud: Best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice)
- Audio is text-only: audio references are not supported, so a recorded voice cannot drive an anime mouth. — [AI Studio](https://aistudio.google.com/docs/omni); the forum user who tried replacing the voice in post found lips did not match the new audio: [Google AI forum](https://discuss.ai.google.dev/t/lip-sync-in-google-flow/179960)

### Inferences
- "Limited animation" phrasing is not documented anywhere I found. Reasonable test phrasings, derived from the vocabulary above and not from a source, are "limited animation, held poses, minimal in-between frames, mouth flaps simple open-close shapes in sync with the spoken line". Mark any such phrase as an experiment to compare against "Japanese anime style" / "cel-shaded animation" baselines.
- For a calm, quiet 2D dialogue shot, counter the "over-animated" tendency with an explicit camera/pacing instruction ("static camera", "subtle movement") and one or two actions only, in line with Google's single-scene advice.

### Gaps
- No cel-shaded lip-sync accuracy data, no examples of mouth-shape behavior, and no limited-animation prompt with verified output. The "Create Stunning 2D Cartoon Movies with Google Flow Omni" YouTube result was seen only as a snippet and was not reviewed.

## Quick syntax reference (assembled; each line traces to a section above)

| Need | Phrase | Grade |
|---|---|---|
| Spoken line | `A woman says: My name is Clara.` (colon, no quotes) | OFFICIAL (Google Cloud) |
| Voice description | `In a voice that is crisp and clear, with a thoughtful, analytical tone and a standard American accent, Clara says: ...` | OFFICIAL (Google Cloud) |
| Two speakers | `The detective says: ... The informant ... replies: ...` | OFFICIAL (Google Cloud) |
| Narration | `a voiceover with a polished British accent speaks in a serious, urgent tone` | OFFICIAL (Google Cloud) |
| Off-screen VO, on-screen silent | `a calm female voiceover, the app's coach, says: ... He does not speak.` | VENDOR (Runware, uses quotes) |
| SFX / ambience | `Sound design: Gentle breeze, distant bird chirps.` | OFFICIAL (AI Studio) |
| Music on | `Include calm background music` / `high energy techno beat` | OFFICIAL (AI Studio) |
| Music/dialogue/SFX off | `No dialogue.` / `No extra sound effects.` / `No music.` | OFFICIAL (first two) / VENDOR (No music) |
| Subtitles off | `No subtitles.` / `No on-screen text.` | VENDOR |
| Single take | `In a single continuous shot` / `No scene cuts` | OFFICIAL |
| Timecode block | `[0-5s] ...` newline `[5-10s] ...` | OFFICIAL |
| Timed audio event | `At 5s the chorus starts in the background audio.` | OFFICIAL |
| Edit turn | `<one change>. Keep everything else the same.` | OFFICIAL |
| Extend audio | `The music continues into the chorus` | OFFICIAL |
| Trigger-synced SFX | `Add [sound] synchronized to exactly when [event]` | COMMUNITY/UNVERIFIED |
