# Community evidence and reference prompts: Indonesian/non-English dialogue and anime/2D multi-shot work in Flow / Veo / Omni (2025-2026)

Method note: Reddit, Facebook and some YouTube pages could not be fetched (blocked). Reddit items below rest on search-result snippets only and are labeled "snippet only". Many "guides" are vendor/SEO blogs; they are marked as such. No Indonesian-language Veo/Omni quality report with lip-sync/accent details was found.

## Which creators/posts show Indonesian (or Malay, Javanese, Thai, other SEA) dialogue in Veo/Omni, and what quality did they report?

### Takeaway
I found no verified, detailed report on Indonesian lip-sync, accent or voice stability in Veo/Omni. The closest evidence is one Malaysian Malay prompt (with an explicit "not Bahasa Indonesia" instruction), snippet-level hints that Indonesian prompts exist in Facebook/Google-forum posts, and generic multilingual caveats (accent drift, Flow refusing non-English prompts, English fallback).

### Cited Findings
- A Malaysian creator (@cikgumuktasim, 2026-02-14, 8s clip, ~25k views) published a full Veo-style prompt in Malay: reference image as character, "speaks in clear Malaysian Malay, not Bahasa Indonesia, with standard pronunciation", "lip-sync very precise", static camera on face/upper body, a fixed script marked "KEKALKAN AYAT INI" (keep this sentence), plus a voice/expression block (language, tone, pace, expression, mouth movement). The post does not state which tool generated it, and no quality assessment is given. — [TikTok](https://www.tiktok.com/@cikgumuktasim/video/7606603961570790664)
- A Facebook group post (snippet only, unverified) shows a prompt line "The entire dialogue must be in Bahasa Indonesia ... and the order of the lines must NOT be swapped: The orangutan speaks ...". It indicates Indonesian creators use an English wrapper plus an explicit language and line-order constraint; results not visible. — [Facebook group post](https://www.facebook.com/groups/439058929064196/posts/720983320871754/)
- A Google Gemini support thread (snippet only) has a self-identified Indonesian user saying an English prompt with the line translated to Indonesian "works for me" for a Veo 3 error about "prompts only in English". The page body was truncated, so I could not verify the prompt or the audio quality. — [Google support thread](https://support.google.com/gemini/thread/347700144/veo-3-keeps-saying-prompts-only-in-english-even-when-the-prompt-is-already-in-english?hl=en)
- A LinkedIn post (Tianyu Xu) lists the recipe: specify the spoken language, write the dialogue in that language, and prefer the Gemini/Veo API for better success. Known issues listed: Flow may reject non-English prompts, Latin-script languages may work better, audio sometimes fails to generate, and accents can come out unexpected. Bahasa Indonesia appears among the supported-language list in the snippet. — [LinkedIn](https://www.linkedin.com/posts/tianyuxu_make-your-veo-3-character-speak-another-language-activity-7362063072250748928-ujOC)
- r/VEO3 threads (snippet only) report the opposite failure: the model "understands the text perfectly" but speaks the line in English, and another thread says videos stay English even with dialogue in other languages. — [r/VEO3 thread 1](https://www.reddit.com/r/VEO3/comments/1lb770z/how_do_you_get_veo3_to_speak_in_another_language/), [r/VEO3 thread 2](https://www.reddit.com/r/VEO3/comments/1mgoq95/veo_3_problem_language_always_english/)
- A multi-language single-clip test exists on r/singularity (snippet only; results not read). — [r/singularity](https://www.reddit.com/r/singularity/comments/1kusqcx/language_test_on_veo_3_multiple_languages_in_one/)
- Vendor blog claim: writing the line in the target language inside quotes lets Veo 3.1 "handle the accent and lip-sync automatically"; the same page tells readers to quote one short line and warns quotes do not guarantee correct speech. — [GlobalGPT guide](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/)
- Unverified secondary claim (no methodology): single-speaker English lip-sync ~80%, multi-speaker under 40%, Chinese ~30%. — [eastondev blog](https://eastondev.com/blog/en/posts/ai/20251207-veo3-audio-generation-guide/)
- No Javanese or Thai Veo/Omni dialogue report was found.

### Inferences
- Indonesian is workable in practice (people post prompts for it) but with no published quality data; plan to QA every line with a native listener.
- The Malay prompt's explicit "not Bahasa Indonesia" line suggests the model can blur Malay/Indonesian accents; the mirror-image instruction ("Indonesian, not Malay, standard Jakarta accent") is a reasonable test to run (inference, untested).

### Gaps
- No YouTube/Reddit/X thread with real Indonesian Omni Flash 1.2 / Veo 3.x results and lip-sync notes was retrievable. Reddit/Facebook/X pages could not be fetched.
- "Omni Flash 1.2" specifics: only an invideo FAQ (via search snippet) mentions "Google Omni Flash" with ~6-7 s accurate single-speaker lip-sync; unverified.

## Which anime/2D character series made with Flow/Veo/Omni exist, and what is their consistency workflow?

### Takeaway
I found strong workflow documentation for consistency (contact sheets, scene grids, Ingredients to Video, same references per shot) but no verified anime-series channel with published voice workflow. Voice consistency is generally handled outside Veo (ElevenLabs) or by repeating the same voice descriptor.

### Cited Findings
- Dan Kuda AI (Flow/Veo 3.1/Omni 1.1/ElevenLabs channel) published a 5-step workflow (2026-03-11): reference image per character, a character "contact sheet" (close-ups plus front/side/back on a gray background), a 2x2 scene grid (four angles in one generation so shots match), frame extraction via a dedicated prompt that takes appearance only from contact sheets and scene only from the grid, then Ingredients to Video with an "animation instructions header" (author admits it is "in test mode"). He generates one clip at a time and re-runs prompts if unhappy. Prompts are downloadable from the video description (OneDrive links, not read). Not anime-specific. — [YouTube](https://www.youtube.com/watch?v=Egmh0jC8cEU)
- Same channel also has "Why I Don't Use Google Flow Storyboard for Consistency" (title only seen). — [YouTube](https://www.youtube.com/watch?v=QE9FemXDOP0)
- Google's official post (2026-01-13) on Veo 3.1 Ingredients to Video covers reference-image consistency, in Flow/Gemini app/API. — [Google blog](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/)
- Community post (Skool "Consistent Characters", snippet only; body not retrievable): experimental "Voice" ingredients for Ultra plan: pick an image ingredient of a single character, then choose a voice in the Voice menu; voice ingredients do not carry over with Extend; use single-speaker reference images. Unverified, may have changed. — [Skool](https://www.skool.com/consistentcharacters-7595/veo-31-fast-experimental-voice-ingredients-ultra-plan)
- Guide advice: build a reusable ingredient library, change one element per clip; mismatched tone/voice between clips is a listed failure mode. — [veo3gen.app](https://www.veo3gen.app/blog/veo-31-ingredients-in-flow-a-creator-workflow-to-lock-characters-props-and-locat) (vendor blog)
- Tutorial summary says Veo voices vary and ElevenLabs voice cloning improves consistency. — [coconote summary](https://coconote.app/notes/de746c6a-ee1a-4652-a851-c643de1b9d53)
- Voice vs face: GlobalGPT guide says a consistent face does not prove a consistent voice; replacing audio with ElevenLabs does not re-animate lips, so a lip-sync pass or timing match is needed. — [GlobalGPT](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/)

### Inferences
- For a 7-clip episode: lock (a) one approved character sheet/reference, (b) one copy-pasted voice descriptor string, (c) same ingredients every clip, and regenerate until the voice matches; treat Flow voice ingredients as optional and experimental.
- No source showed a named anime/2D series with Indonesian dialogue.

### Gaps
- No verified anime-specific Flow series with a published prompt set found; Reddit r/aivideo and X were not retrievable.
- Dan Kuda prompt files were not opened (external OneDrive).

## What detailed shot-prompt templates and frameworks exist (shot bible, prompt macro, timecode, audio layering)? 5+ concrete examples

### Takeaway
Google's official guide gives a formula and timestamp syntax; community guides add audio layering and storyboard tables. The terms "shot bible" and "prompt macro" are not established terms in sources I found; the closest are a storyboard table and a reusable header.

### Cited Findings
1. Google formula: [Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]; dialogue in quotes; `SFX:` and `Ambient noise:` prefixes. — [Google Cloud guide](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1)
2. Google timestamp template: `[00:00-00:02] Medium shot from behind ...` / `[00:02-00:04] Reverse shot ... SFX: ...` / `[00:04-00:06] Tracking shot ... Emotion: ...` / `[00:06-00:08] Wide, high-angle crane shot ...` (multi-shot inside one 8 s generation). — same source.
3. Google dialogue example: `A woman says, "We have to leave now."` (quoted-line pattern). — same source.
4. Single-speaker audio-separated template: camera + subject + action + setting, then dialogue sentence, then separate sentences for narration and ambience, ending "No on-screen captions"; "The woman in the red jacket says..." to disambiguate speakers. These are suggested starting prompts, not reported test results. — [GlobalGPT](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/)
5. Malay character+voice block (language, tone, pace, expression, mouth movement, fixed script). — [TikTok](https://www.tiktok.com/@cikgumuktasim/video/7606603961570790664)
6. Storyboard table columns (Shot #, Timecode, Visual Goal, Camera Intent, Action Beats, Continuity Must-Haves, Avoid), closest to a "shot bible"; plus a loop where Gemini revises shot text and updates the bible. — [veo3 longform storyboard workflow](https://veo3-ecru.vercel.app/blog/veo-3-longform-storyboard-workflow-2026) (blog; only seen via snippet)
7. Lip-sync prompting advice: "clearly enunciates", "visible mouth openings", speaking duration, "no background music". — [Skywork](https://skywork.ai/blog/ai-video/how-to-prompt-lip-synced-dialogue-google-veo-3)
8. Dev guide on timestamp prompting and multi-shot (not opened). — [dev.to](https://dev.to/akaranjkar08/veo-31-developer-guide-timestamp-prompting-multi-shot-video-and-full-api-june-2026-3l5i)
9. Reusable "animation instructions header" pasted before every scene description (a de facto prompt macro). — [Dan Kuda AI](https://www.youtube.com/watch?v=Egmh0jC8cEU)

### Inferences
- A workable per-shot layout: [HEADER macro: style + character IDs] / [Shot: camera] / [Action] / [Voice block: speaker, voice descriptor, language, line in quotes] / [Ambience + SFX] / [Negatives]. This is a synthesis of the above, not a quoted creator template.

### Gaps
- No anime-specific, creator-authored full shot prompts with links beyond the above (several are generic live-action). The Facebook/Reddit prompt posts were unreadable.
- Timestamps are described as requested timing, not frame-accurate ([GlobalGPT](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/)).

## How do creators handle unwanted behavior (extra dialogue, subtitles, music), voice consistency across clips, and mispronunciations?

### Takeaway
Subtitles: add "no subtitles/captions" (reported, not guaranteed). Music: "no background music / clean dialogue only". Wrong speaker or swapped lines: name speakers, one speaker per shot, keep clips short. Pronunciation: no Veo-specific phonetic-spelling evidence was found; test respellings.

### Cited Findings
- Veo adds unwanted subtitles that cover mouths; "No subtitles" reported to stop it, but instruction is not a guarantee. — [MIT Technology Review on Veo 3 subtitles problem](https://www.technologyreview.com/2025/07/15/1120156/googles-generative-video-model-veo-3-has-a-subtitles-problem/amp/); [GlobalGPT](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/)
- "No music"/"Clean dialogue only" suggested for easier editing. — [GlobalGPT](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/)
- Wrong person speaks or lines swap: r/VEO3 threads (snippet only) say Veo 3.1 often swaps lines, and one advice snippet says to describe visible lip movement per speaker. — [r/VEO3 dialogue challenge](https://www.reddit.com/r/VEO3/comments/1pzs0wf/dialogue_challenge_in_veo_31/), [r/VEO3 mix-up](https://www.reddit.com/r/VEO3/comments/1ohhx9n/how_to_fix_dialogue_mix_up_between_2_characters/)
- Speech cut off: shorten the line or split across shots; 4-8 s clips; medium close-up gives best lip-sync. — [GlobalGPT](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/)
- Voice consistency: reuse same references and description, re-run, or replace audio with ElevenLabs then lip-sync. — [GlobalGPT](https://www.glbgpt.com/hub/how-to-make-characters-speak-in-veo-3-1-the-ultimate-guide-to-dialogue-audio-lip-sync/)
- Pronunciation: general TTS advice is to respell phonetically or substitute easier words; ElevenLabs offers alias/pronunciation dictionaries. Not shown to work in Veo; a fluent reviewer should check non-English output. — [ElevenLabs best practices](https://elevenlabs.io/docs/overview/capabilities/text-to-speech/best-practices); [magichour guide](https://magichour.ai/blog/how-to-prompt-for-speaking-in-veo-3)

### Inferences
- For Indonesian, test: standard spelling first; if a word fails, try hyphenated syllables or a simpler synonym; avoid code-mixed English words and numerals (write out numbers as words). These are untested hypotheses.
- If Veo voice drift is unacceptable, generate video silent-ish ("no dialogue audio") and add ElevenLabs Indonesian voice + lip-sync pass (hybrid), per the GlobalGPT guidance.

### Gaps
- No evidence of Veo honoring phonetic respellings; no Indonesian-specific mispronunciation threads found.
- Extra-dialogue (hallucinated chatter) handling: only "one visible speaker", short lines, and naming speakers were found; no dedicated source.
