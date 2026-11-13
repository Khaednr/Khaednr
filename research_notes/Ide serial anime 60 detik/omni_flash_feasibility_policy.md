# Production feasibility of anime-style 60s serials on Google Flow Omni Flash 1.2, plus AI-content policy (as of 13 Nov 2026)

Source-reliability legend: [OFFICIAL] = Google/TikTok/YouTube first-party page. [3P] = third-party blog or vendor (often has a commercial angle). [SNIPPET] = only a search-result excerpt was seen; the page could not be opened (Reddit and YouTube were not scrapable here).

## 1. What Omni 1.2 Flash officially does, and its hard limits (the "feasibility filter" facts)

### Takeaway
Omni 1.2 Flash (released 5 Nov 2026) generates 3-15 s clips with native audio and supports reference images, conversational editing, extension and video-to-video restyle ("Make this video anime"). Several limits matter for a serial: first/last-frame interpolation caps at 10 s, extension is 3-10 s per turn, and there are no audio references or voice editing. Google itself says fast sports action, rapid script changes and complex physics are still being improved.

### Cited Findings
- [OFFICIAL] Launch on 5 Nov 2026: native 15 s clips (up from 10 s in 1.1), 1-second duration increments from 3 to 15 s, "better reference adherence", multi-turn conversational editing, more natural speech, 30% lower API price ($0.07/s at 720p) — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- [OFFICIAL] Draft at 360p or 720p, fix details with a follow-up edit instead of regenerating, then upscale the best clips to 1080p or 4K — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- [OFFICIAL] References: character/product/style images, short motion clips (up to 3 s) and audio cues. Faces, garments and typography are claimed to stay consistent "across camera angles", with "less visual drift or morphing" — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- [OFFICIAL] Official demo: one scene image plus four character, mouth and one-second voice references produced a 15 s animated scene in which each sampled voice was "routed to the right character" with lip-sync. Marketing demo only; not verified here for anime — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- [OFFICIAL] Camera: continuous moves (FPV flythrough, crash zoom-out, orbit) with "significantly fewer unwanted jump cuts" — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- [OFFICIAL] Google's own caveat: "development is ongoing to further improve things like fast sports action, rapid script changes and complex physics" — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- [OFFICIAL, API docs] Reference limits: up to 6 reference images in total, and up to 3 images per character for up to 2 characters. Videos of 11-15 s take only 1 reference video (up to 3 s); videos of 3-10 s take up to 3 — [AI Studio Omni docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL, API docs] First+last frame interpolation only works for 3-10 s (more than 10 s with two frames returns an error). Single-image generation goes up to 15 s — [AI Studio Omni docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL, API docs] Extension adds 3-10 s per turn, up to 30 s total. It uses only the last 10 s of the input as context, so a character who appeared earlier must be re-prompted or re-referenced. It appends at the end only. Dialogue can be added when extending model-generated video via multi-turn, but not when extending uploaded video of someone talking — [AI Studio Omni docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL, API docs] Not supported: voice editing, audio inputs or audio references, system instructions, negative-prompt parameter (write negatives inside the prompt). Aspect ratios are only 9:16 and 16:9. Native resolutions are 360p and 720p (default); 1080p and 4K are upscaled — [AI Studio Omni docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL, API docs] Language: "English is fully supported, but other languages have not been evaluated, so they may work but results can vary." — [AI Studio Omni docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL, API docs] Prompting: by default Omni tries to create a few different shots with its own narrative. For one shot, say "single unbroken scene / single continuous shot / no scene cuts". Timecodes work (`[0-5s] ... [5-10s] ...`) and "Every 2s cut to a new frame" works. Say "No dialogue" or "No extra sound effects" when unwanted. For edits, keep prompts simple and add "Keep everything else the same". "Make this video anime" is a listed example edit prompt — [AI Studio Omni docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL, API docs] Text in video: "you can prompt to include text and Gemini Omni will render in a way that is correct and readable"; defining the exact text helps — [AI Studio Omni docs](https://aistudio.google.com/docs/omni). Contradicted in practice, see section 3.
- [OFFICIAL] All outputs carry an invisible SynthID watermark — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/), [AI Studio docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL, Flow help] In Flow, Omni Flash 1.1, Veo 3.1 Fast and Veo 3.1 Quality retire on 5 Dec 2026, and Veo Extend was retired on 5 Nov 2026. Extending now requires an Omni Flash 1.2 subscriber (Plus, Pro or Ultra) — [Flow credits help](https://support.google.com/flow/answer/16526234?hl=en)

### Inferences
- A 60 s episode has to be assembled from separate clips (4-6 shots, each at most 15 s, or at most 10 s if first+last frame is used). Extension (30 s total) is the only way to get a longer continuous shot, and it re-uses only the last 10 s as context.
- Because of the 10 s lookback, scene-to-scene continuity should come from re-supplying the same reference images on every shot, not from relying on the model's memory.
- Indonesian dialogue is a risk: Google states only English is evaluated.

### Gaps
- Flow UI limits for "ingredients" (how many images, whether the same 6-image / 2-character caps apply) were not found in Flow help pages; the numbers above are from the Gemini API docs.
- No official Google statement on 2D/anime quality specifically; the Google blog says nothing about anime or cel-shading.

## 2. Anime / 2D quality: strengths, failure modes, prompts that work

### Takeaway
Independent sources agree on a pattern: strong first-frame anime stills anchor the look, and Omni adds extra micro-motion ("over-animated"), which is the opposite of limited animation, so it must be prompted down. Character consistency across cuts is only moderate (3/5 in one reviewer's test). Dialogue and high-motion work are called weak in one hands-on review, while another vendor (AutoWeeb) claims sports/action motion is a strength. These conflict with each other, and Google's own caveat sides with caution on fast action.

### Cited Findings
- [3P, AutoWeeb, an anime-tool vendor selling Seedance-based tools; tested with matched starting images] Omni Flash "adds more micro-movement, which can make a quiet vending-machine moment feel busier than intended", while Seedance 2 has a "stronger 24fps feel, calmer holds". A sharp anime still with clear linework "anchors the motion closer to what you want"; photoreal or soft-illustration stills give the model "more room to over-animate" — [AutoWeeb comparison](https://autoweeb.com/blog/seedance-2-vs-omni-flash-which-to-use-for-anime)
- [3P, AutoWeeb] Omni is "more likely to add unrequested character dialogue", so write "no dialogue" or give exact lines. It honours explicit `[cut to a new scene]` language more reliably than Seedance. Audio is prompt-driven only — [AutoWeeb comparison](https://autoweeb.com/blog/seedance-2-vs-omni-flash-which-to-use-for-anime), [AutoWeeb how-to](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash)
- [3P, AutoWeeb] Claims Omni is stronger on sports/athletic motion and weight transfer than Seedance 2; Seedance is rated better for slice-of-life and dialogue pacing. Their tests were on the earlier preview/1.1-era model (their how-to cites `gemini-omni-flash-preview`), so this may not describe 1.2 — [AutoWeeb comparison](https://autoweeb.com/blog/seedance-2-vs-omni-flash-which-to-use-for-anime), [AutoWeeb how-to](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash). Conflicts with Google's statement that fast sports action is still being improved ([Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)) and with the Reddit snippet below.
- [SNIPPET, Reddit r/VEO3 and r/GeminiAI, "Tested Gemini Omni Flash for a day — 3 things it nails, 2 it can't"] "Omni Flash is impressive on the architectural leap but the gap on dialogue + high-motion work is real today." Full post could not be opened, and it is likely about 1.1 — [r/VEO3 result](https://www.reddit.com/r/VEO3/comments/1tj784z/tested_gemini_omni_flash_for_a_day_3_things_it/)
- [SNIPPET, Reddit r/VEO3] A user compared Omni Flash with Veo 3.1 Fast and concluded Omni quality was worse (title: "Is Omni Flash video quality worst than Veo 3.1 Fast?"); details not retrievable — [r/VEO3 result](https://www.reddit.com/r/VEO3/comments/1tqkrav/is_omni_flash_video_quality_worst_than_veo_31_fast/)
- [3P, Atlas Cloud blog quoting an AI Analytics Diaries Medium review] Omni's character consistency was scored 3/5 vs Seedance 2.0. Quote: "Both models struggle with character consistency across multiple cuts". Omni's strength is stateful multi-turn editing; Seedance uses up to 9 references — [Atlas Cloud](https://www.atlascloud.ai/blog/ai-updates/gemini-omni-multi-turn-consistency-editing). Atlas Cloud sells model access, so treat it as a reseller view.
- [3P, promptslove review of 1.1] Multi-turn editing: motion degradation and character drift "setting in around turn 5, with 4 turns being the reliable working window"; generation times vary from under a minute to multiple hours; Google's model card lists consistency through edits, complex motion and accurate text as open challenges — [promptslove](https://promptslove.com/blog/gemini-omni-1-1-flash-review/). This is about 1.1; 1.2 claims improvements, and I found no independent 1.2 re-test of the turn limit.
- [3P, vendor demos] A YouTube tutorial titled "Create Stunning 2D Cartoon Movies with Google Flow Omni Flash" and "Omni Flash + Nano Banana = CRAZY Animations" exist (animation-specific tests), but content was not extractable — [YouTube 2D cartoon](https://www.youtube.com/watch?v=oTcqQplFudQ), [YouTube Omni+Nano Banana](https://www.youtube.com/watch?v=JiNEHqDYla4)
- Prompt patterns that are documented and work: timecoded blocks, e.g. `<FIRST_FRAME> [0-3s] Medium shot ... [cut to a new scene] [3-6s] Close-up ... Sound design: vending machine hum, no music. She says quietly: "..." No extra sound effects.` — [AutoWeeb how-to](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash). Note the docs call tags like `<FIRST_FRAME>` / `<IMAGE_REF_0>` "deprecated and unsupported in future models" and tell users to describe image roles in natural language ([AI Studio docs](https://aistudio.google.com/docs/omni)). The official page wins; the AutoWeeb tag syntax is a conflict to avoid.

### Inferences
- For limited-animation anime the model's default over-animation is the main style risk. Mitigate with: strict anime still as first frame, "held pose, minimal movement, only hair/eyes/mouth move, static camera / slow push-in", single-shot wording, and 360p drafts to catch drift cheaply.
- Fast fight choreography, crowd scenes and rapid script changes are inconsistent with Google's own caveat. Treat them as high-risk and design episodes around dialogue, reaction shots and atmosphere instead.

### Gaps
- No reliable 1.2-specific, anime-specific hands-on review was found (Reddit and YouTube bodies could not be read). Most independent evidence is on 1.1 or the preview.
- Cel-shading line-boil, flicker and "flat colour" stability were not covered by any source found.
- Hands, crowds and multi-character blocking in anime style: no specific source found; treat as unknown.

## 3. Shot types: cheap/reliable vs unreliable; text; lip-sync; the "limited animation" approach

### Takeaway
Evidence supports building episodes from dialogue close-ups and medium shots, slow pushes/pans, establishing shots and still-image-plus-subtle-motion. It cautions against fast action, crowds, and any readable text (especially Japanese). This matches how anime limited animation works, so the style choice and the model limits align. The "limited animation" mapping below is my recommendation, not a documented Google workflow.

### Cited Findings
- [OFFICIAL] Single-image generation (image-to-video) can run up to 15 s, and docs recommend detailed motion descriptions with high-resolution images; "make it move" prompts give weaker results — [AI Studio docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL] Speech: "clearer lip-sync, distinct multi-speaker conditioning" claimed; multi-character voices routed correctly in one official demo — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/). Independent reports say dialogue is still a gap versus other tools ([r/VEO3 snippet](https://www.reddit.com/r/VEO3/comments/1tj784z/tested_gemini_omni_flash_for_a_day_3_things_it/)).
- [3P, K-Dense 35-case benchmark of Omni Flash for scientific video] "stunning" visual quality but "unreliable text, physics, and factual" accuracy — [K-Dense](https://www.k-dense.ai/blog/benchmarking-google-omni-flash-scientific-video)
- [3P, promptslove] CJK text is measurably worse: only 11 of 46 hiragana characters rendered correctly in documented testing; high-stroke-count Chinese malformed — [promptslove](https://promptslove.com/blog/gemini-omni-1-1-flash-review/) (1.1 data)
- [OFFICIAL] Google markets accurate, motion-tracked callout text in its 1.2 demo (English infographic) — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- [OFFICIAL] Extra caveat: people-related filters. Uploading/editing images with recognisable people or minors is restricted in places; safety filters apply to prompts and outputs — [AI Studio docs](https://aistudio.google.com/docs/omni). Anime characters that look like minors may hit the minors rule only in EEA/CH/UK per the docs; Indonesia is not listed (see section 7).

### Inferences
Suggested "limited animation" shot menu for a 60 s episode (reliability ranking is my judgement from the sources above, not measured):
- Most reliable/cheap: establishing shots with slow pan or push; dialogue close-up with static camera; reaction shot (eye/hair movement); still image + parallax or ambient motion (rain, wind, light shift); "held pose, only mouth and hair move".
- Medium risk: two-character dialogue with voice routing (Google demo exists; test in your language); camera orbits; first-frame-to-last-frame transitions (max 10 s).
- High risk: fast fights, impact frames, crowds, hands doing fine tasks, readable in-scene text, Japanese text, rapid script changes.
- Workarounds: do on-screen text (titles, SFX words, subtitles) in editing software, not in the model; hide impact via cutaways, silhouettes, speed-line stills; use short 3-6 s action beats.

### Gaps
- Lip-sync quality for Indonesian speech: no source; Google says non-English not evaluated.
- No source quantifies hand or crowd failure rates for anime style.

## 4. Consistency across 4-6 clips per 60 s episode: ingredient setups and creator workflows

### Takeaway
Official guidance is to feed character-sheet references on every shot (max 6 images; max 3 per character for 2 characters), keep a strong first-frame still, prefer short per-shot clips, and repair details with conversational edits. Creator workflow of record is: character sheet in Nano Banana, then storyboard stills, then 360p drafts, then upscale. Independent evidence says consistency across cuts is still imperfect.

### Cited Findings
- [OFFICIAL] Use character sheets as references: "turn existing product photography or character sheets into ... clips" — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/)
- [OFFICIAL] Subject reference supports "up to 3 images per character for up to 2 characters" within the 6-image cap — [AI Studio docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL] Stateful editing keeps unmentioned elements; add "Keep everything else the same". Setting `store=false` disables later editing of that output (API only) — [AI Studio docs](https://aistudio.google.com/docs/omni)
- [OFFICIAL] On extension, characters that appeared only before the last 10 s must be re-mentioned or re-referenced — [AI Studio docs](https://aistudio.google.com/docs/omni)
- [3P, AutoWeeb] "Build polished anime still" as first frame: "if it is not in the starting image, Omni Flash has to invent it, and invented details drift"; separate character sheet, location still and style anchor into distinct image roles — [AutoWeeb how-to](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash). (Vendor selling a competing pipeline; advice is plausible and consistent with Google docs.)
- [3P, 1.1-era] Character drift appears around turn 5 of repeated edits; plan around ~4 edit turns per clip — [promptslove](https://promptslove.com/blog/gemini-omni-1-1-flash-review/)
- [3P] Consistent-character tutorials exist: "I Fixed Character consistency in Gemini Omni with this SIMPLE method | Google Flow" and "Google Omni Flash: AI Filmmaking with CONSISTENT Characters (FULL WORKFLOW)" (BigWiz Media) — not extractable here — [YouTube fix](https://www.youtube.com/watch?v=aiHxjrX8k1U), [YouTube full workflow](https://www.youtube.com/watch?v=uI8lul2JFaQ)
- [3P, vendor/blog] Nano Banana character-sheet advice: multi-angle reference sheets (8-14 angles claimed to reach "95% consistency") — [Selfie Lab blog](https://selfielabstudio.com/blog/nano-banana-pro-reference-sheet-tutorials-for-consistent-characters-20260226). Treat the 95% figure as unverified marketing.
- [OFFICIAL, Indonesia plan page] Flow plans include "limited access to Nano Banana Pro" even on the free tier — [Gemini Indonesia plans](https://gemini.google/subscriptions/?hl=id)

### Inferences
Recommended ingredient setup (my synthesis):
- Per shot supply: (1) the character reference sheet crop (front + 3/4 + expression), (2) the shot's storyboard still as first frame, (3) a location/style still. Never exceed 6 images or 3 per character; for a 2-person scene use 3+3.
- Keep each shot to a single scene with explicit "single continuous shot, no scene cuts" and do cuts in the editor. Re-state outfit and colours in text each time.
- Generate the storyboard stills in Nano Banana with the same sheet attached, so the first frames are already consistent before video.
- Limit edit turns per clip to about 3-4; regenerate rather than chain edits.
- Fix a world "bible" (palette, line weight, background style) as a text block pasted into every prompt.

### Gaps
- No documented Flow UI "ingredients" recipe from Google with limits; the API numbers are the best official data.
- No source tested long-run (10+ episodes) character stability.

## 5. Credit costs and 60 s episode math

### Takeaway
Official Flow help gives per-second credit costs. A 60 s episode of 6x10 s shots costs 60 credits per 360p draft pass; the 1080p upscale of a 10 s clip is free. With 3 draft takes per shot, about 180 credits/episode, or roughly 5 episodes per month on Google AI Pro (1,000 credits).

### Cited Findings
- [OFFICIAL] Omni Flash 1.2 credits (Flow help, page says "limits are subject to change"; check Settings in the prompt box): generate or edit up to 10 s = 1 credit/s at 360p and 3 credits/s at 720p for all users; 11-15 s (subscribers only) = 1 credit/s up to 10 s then 2 credits per extra second at 360p, and 3 then 6 at 720p; extend 3-10 s = 1 credit per added second at 360p and 3 at 720p; upscale to 720p/1080p = 0 credits for 1-10 s plus 1 credit per extra second over 10 s (subscribers); upscale to 4K = 50 credits flat for 1-10 s plus 5 per extra second (Ultra only) — [Flow credits help](https://support.google.com/flow/answer/16526234?hl=en)
- [OFFICIAL] Free credits: 50 per day (no rollover), triggered by first generation. Plus 200/month, Pro 1,000/month, Ultra $100 tier 10,000/month, Ultra $200 tier 25,000/month; monthly credits do not roll over; AI credits can be bought in supported regions (not Japan) — [Flow credits help](https://support.google.com/flow/answer/16526234?hl=en)
- [OFFICIAL] Non-subscribers: 15 s clips unavailable; video generation may be unavailable at peak hours (about 14:00-17:00 UTC; this is 21:00-24:00 WIB) — [Flow credits help](https://support.google.com/flow/answer/16526234?hl=en)
- [OFFICIAL] Veo 3.1 Lite (4/6/8 s, 720p) costs 10 credits (5 for Ultra) per generation — a cheaper option for non-dialogue inserts — [Flow credits help](https://support.google.com/flow/answer/16526234?hl=en)
- [OFFICIAL] API price for comparison: $0.07/s at 720p, so about $0.70 per 10 s and about $1.04 per 15 s clip per a pricing-page excerpt — [Gemini API pricing](https://aistudio.google.com/docs/pricing) (SNIPPET only)

Calculated scenarios (my arithmetic from the official table; assumes a final 720p/1080p result is made either by native 720p generation or by upscaling an approved 360p clip, and that upscaling reproduces the 360p content; whether quality equals native 720p is unverified):

| Layout (60 s) | 360p draft, 1 pass | Native 720p, 1 pass | Upscale approved 360p to 1080p |
|---|---|---|---|
| 6 x 10 s | 6 x 10 = 60 | 6 x 30 = 180 | 0 |
| 5 x 12 s | 5 x 14 = 70 | 5 x 42 = 210 | 5 x 2 = 10 |
| 4 x 15 s | 4 x 20 = 80 | 4 x 60 = 240 | 4 x 5 = 20 |

- Example budget, 6 x 10 s with 3 drafts per shot plus upscale: 3 x 60 + 0 = 180 credits/episode. With 5 takes per shot: 300 credits.
- Pro (1,000 credits): about 5 episodes at 180, about 3 at 300. Plus (200 credits): about 1 episode at 180. Ultra $100 tier (10,000): about 55 at 180. Native-720p-only route (no drafts, 3 takes): 540 credits/episode.
- Edits cost credits like generations (docs say "Generate or edit"); Nano Banana image costs in Flow were not found.

### Inferences
- The cheapest route is: 360p drafts (10 s clips are cheapest per second), approve, then upscale (free up to 10 s). 10 s shots are the sweet spot; 11-15 s clips double the per-second cost beyond 10 s.
- The free 50 credits/day alone allows about 50 s of 360p drafts per day (clips of 10 s or less), but peak-hour blocks for non-subscribers and the subscriber-only 15 s limit apply.

### Gaps
- Whether Flow's 1080p "upscale" visually matches native 720p generation: untested.
- Nano Banana (image) credit cost inside Flow: not found.
- The 4K flat 50-credit rate is clear; no source on whether upscaling is billed per resolution step.

## 6. Plan prices (Indonesia and global) and source reliability

### Takeaway
Google's own Indonesian plans page (cached 12 Nov 2026) lists Plus Rp75,000, Pro Rp309,000, Ultra Rp1,579,000 (5x) and Rp3,399,000 (20x) per month, and names Gemini Omni Flash with 200 / 1,000 / 10,000 or 25,000 Flow credits. Third-party figures differ slightly.

### Cited Findings
- [OFFICIAL, Indonesia] Plus Rp75,000/mo with 200 Flow credits and "access to Gemini Omni Flash"; Pro Rp309,000/mo with 1,000 credits; Ultra from Rp1,579,000/mo (5x) and Rp3,399,000/mo (20x) with 10,000 or 25,000 credits — [Gemini ID subscriptions](https://gemini.google/subscriptions/?hl=id). Footnote: Flow features "can differ by plan tier, platform and region".
- [OFFICIAL, US] Plus $4.99, Pro $19.99, Ultra 5x $99.99, Ultra 20x $199.99; credits 200 / 1,000 / 10,000 / 25,000 — [Google AI plans](https://one.google.com/about/google-ai-plans/)
- [3P] Third-party guide tested with an Indonesian account in May 2026 reported Pro about Rp320,000 and Ultra about Rp4,000,000 — via [search summary of gptprompts.ai](https://gptprompts.ai/id/harga-gemini) (snippet only). Differs from the official page above; prefer the official numbers and re-check at checkout.
- [3P] AI Plus launched in Indonesia at Rp75,000/month, reportedly with a 50% discount for the first six months for new subscribers (2025 launch) — [Selular.ID](https://selular.id/2025/09/google-ai-plus-resmi-hadir-di-indonesia-harga-rp75-ribu-per-bulan/) (snippet; promo may have ended)

Derived effective cost per credit (my arithmetic from official Indonesia prices): Plus about Rp375, Pro about Rp309, Ultra 5x about Rp158, Ultra 20x about Rp136. An episode at 180 credits is therefore about Rp56,000 on Pro; at 300 credits about Rp93,000.

### Inferences
- If producing 8+ episodes per month, Pro runs out; Ultra 5x is about 5x Pro's price for 10x the credits. Pro is the sensible starting plan for 4-5 episodes per month.

### Gaps
- Whether the Indonesian price includes tax (PPN), and current promos: not confirmed.
- Whether the plan page's "Ultra" tier has Indonesia-specific credit counts: page lists the same global figures.

## 7. Availability in Indonesia (Flow, Omni features, voices)

### Takeaway
Indonesia is on Google's official Flow supported-countries list, and no Omni-related regional restriction in the help pages names Indonesia. Restrictions found apply to the EEA, Switzerland and the UK, not Indonesia.

### Cited Findings
- [OFFICIAL] Flow help "Where you can use Flow": Indonesia is in the supported list for desktop and mobile; the page does not mention Omni Flash specifically — [Flow availability](https://support.google.com/flow/answer/16353544). (Read via a page-summarising fetch; verify on the page.)
- [OFFICIAL] Regional limits listed there: editing uploaded videos unavailable in EEA/Switzerland/UK; Avatars unavailable in EEA/Switzerland/UK; AI credits purchase unavailable in Japan; identifiable minors and prominent people restricted, "may vary by region"; changing what people say in uploaded videos unsupported everywhere — [Flow availability](https://support.google.com/flow/answer/16353544)
- [OFFICIAL] The Indonesian plans page advertises Flow with Gemini Omni Flash for Plus/Pro/Ultra in Indonesia — [Gemini ID subscriptions](https://gemini.google/subscriptions/?hl=id)
- [OFFICIAL] Omni docs: English fully supported; other languages not evaluated — [AI Studio docs](https://aistudio.google.com/docs/omni)

### Inferences
- Omni Flash in Flow should be usable from Indonesia on Plus or higher; verify by checking the Flow settings after subscribing, since the plans page itself says Flow features can vary by region.

### Gaps
- No source on voice availability or accent/voice options per region, or whether Indonesian speech quality is acceptable. Test with a short script before committing to a dialogue-heavy format.
- Not verified whether 15 s generation is enabled for Indonesian accounts on every plan (help page says subscribers only, without regional exceptions).

## 8. TikTok and YouTube: labeling, disclosure and monetization risk

### Takeaway
Both platforms allow AI content. YouTube requires disclosure only for realistic synthetic content, and stylised animation is explicitly exempt from the toggle (though labels can still be added automatically). TikTok requires labeling of realistic AIGC and auto-labels via C2PA. The real monetization risk is "inauthentic/mass-produced" (YouTube) and "original / minimal original input" (TikTok Creator Rewards, which also needs videos over 1 minute).

### Cited Findings
YouTube
- [OFFICIAL] July 15, 2025: "repetitious content" renamed "inauthentic content" (mass-produced or repetitive); described as a clarification, not a new rule; "These guidelines apply regardless of how the content was made." — [YouTube monetization policies](https://support.google.com/youtube/answer/1311392?hl=en), [Team YouTube announcement](https://support.google.com/youtube/thread/356734251/response-to-creator-questions-about-ypp-policies-july-2025?hl=en)
- [OFFICIAL] Violating example: "AI-generated content made with generic or unoriginal templates giving the impression of mass production without adding the creator's original, authentic insights". Allowed example: "using AI to visualize a unique character and narrative you invented" — [YouTube monetization policies](https://support.google.com/youtube/answer/1311392?hl=en)
- [OFFICIAL] "Channels that use AI in their content remain eligible to monetize", but creators "are required to disclose when their realistic content is altered or synthetic" — [Team YouTube announcement](https://support.google.com/youtube/thread/356734251/response-to-creator-questions-about-ypp-policies-july-2025?hl=en)
- [OFFICIAL] Enforcement is channel-level: monetization "may be removed from your entire channel" — via [PPC Land summary of the policy](https://ppc.land/youtube-clarifies-inauthentic-content-policy-changes/) (3P summary)
- [OFFICIAL via page fetch] Disclosure help page: required for realistic content (real person saying/doing something they did not, altered real events/places, realistic scene that did not occur). Exempt: unrealistic content (e.g. "an animated missile in a fully animated video"), minor edits, production assistance (scripts, thumbnails, captions, upscaling). Labels for non-photorealistic/animated content, when added, appear in the expanded description, not on the player. YouTube may auto-label (its own AI tools, C2PA, detection). Disclosure alone does not limit audience or monetization; repeated non-disclosure can lead to labels applied manually, removal or YPP suspension — [YouTube altered/synthetic content help](https://support.google.com/youtube/answer/14328491)
- [3P, reference site, updated 6 Nov 2026] No evidence that YouTube's ranking penalises the disclosure label; the monetization risk is the inauthentic-content rule — [Layer3 Labs](https://www.layer3labs.io/guides/youtube-ai-content-policy)
- [OFFICIAL, Team YouTube thread, community replies Jun-Nov 2026] Creators in the thread still report demonetization disputes (reused/inauthentic content) in Nov 2026; anecdotal only — [YouTube thread](https://support.google.com/youtube/thread/356734251/response-to-creator-questions-about-ypp-policies-july-2025?hl=en)

TikTok
- [OFFICIAL] Creators must label AI-generated content with realistic images/audio/video; labeling is encouraged for content completely generated or significantly edited by AI. Tools: AI-generated content toggle, "Creator labeled as AI-generated" label, auto label (TikTok effects or C2PA Content Credentials); an auto label cannot be removed. "Turning on the AI-generated content setting won't affect the distribution of your video as long as it doesn't violate our Community Guidelines." Prohibited even if labeled: fake authoritative sources/crisis events, and likeness of under-18s or private adults without permission — [TikTok AI-generated content help](https://support.tiktok.com/en/using-tiktok/creating-videos/ai-generated-content)
- [OFFICIAL] Creator Rewards Program: original content "filmed, designed, and produced entirely by yourself"; at least 18; personal accounts; videos over 1 minute; "unoriginal" includes content "copied from others or has minimal original input or edits"; Stitch/Duet and long copyrighted music excluded — [TikTok Creator Rewards eligibility](https://support.tiktok.com/en/business-and-creator/creator-rewards-program), [Creator Academy](https://www.tiktok.com/creator-academy/article/creator-rewards-program)
- [3P] Claims that TikTok "explicitly prohibits fully AI-generated content" from Creator Rewards and that 5 unoriginal flags in 30 days remove an account from the program — [Storrito](https://storrito.com/resources/what-tiktoks-ai-monetization-restrictions-signal-for-creator-income/), [Reddit r/TikTokMonetizing snippet](https://www.reddit.com/r/TikTokMonetizing/comments/1qn03oq/tiktok_flagged_my_100_original_videos_as/). Not confirmed on the official pages I could read. Flag as unverified and potentially a conflict with the first official page's wording ("designed, filmed, produced by you").
- [3P, unverified] Reports that labeled AI content gets suppressed vs. TikTok's own statement that the label is not a distribution signal: [Shortform Nation](https://www.shortformnation.com/blog/ai-generated-ugc-for-tiktok-shop-what-actually-works-and-what-gets-you-demonetized-2026-guide) vs [Audit Socials](https://www.auditsocials.com/blog/tiktok-ai-content-disclosure-rules-2026). Both are low-reliability blogs with inconsistent claims; do not rely on either.

Indonesia
- [3P news, Sept 2026] Komdigi's two AI Perpres (AI roadmap and AI ethics) were still awaiting the President's signature as of early/mid Sept 2026; a ministerial regulation (Permen) requiring labels on generative-AI content was being prepared per Antara; a Katadata story on a leaked draft covers human role and content labels — [Bisnis.com 10 Sep 2026](https://teknologi.bisnis.com/read/20260910/84/2003182/komdigi-perkuat-regulasi-dan-keamanan-siber-penggunaan-ai), [Selular.ID Sept 2026](https://selular.id/2026/09/dua-perpres-ai-tunggu-tanda-tangan-presiden-prabowo/), [Katadata leaked draft](https://katadata.co.id/amp/digital/teknologi/69cb710dbfa04/bocoran-perpres-ai-atur-peran-manusia-dan-label-konten/) (headlines/snippets read via search summary; not independently opened)

### Inferences
- Stylised anime characters in a fictional narrative are likely "unrealistic" for YouTube's disclosure toggle, but synthetic voices and "realistic" audio are a grey area (the help page puts non-music AI audio labels in the expanded description). A conservative approach is to tick the AI disclosure anyway on both platforms; YouTube says disclosure does not affect monetization, and TikTok says the label does not affect distribution.
- Biggest monetization risk is template sameness: a serial with the same structure, same voices and same look every episode, produced in bulk, resembles "mass-produced". Mitigate with original story, scripts written by a human, visible creative authorship (character design, narrative arcs, edits) and variation in episodes.
- TikTok Creator Rewards requires over 1 minute, so a "60-second" episode (exactly 60 s) might fall short; plan 61-65 s or compile to a longer cut. Verify the exact threshold in-app.
- SynthID is invisible; whether Flow exports also carry C2PA metadata (which TikTok/YouTube use for auto-labeling) was not found, so expect auto-labels may or may not appear.

### Gaps
- Not found: official YouTube/TikTok statement specific to "AI anime series" or to Omni/Flow outputs.
- Not found: whether Flow output carries C2PA Content Credentials.
- Not found: any enacted Indonesian law/regulation requiring AI labels as of 13 Nov 2026; status of the Perpres and Permen after Sept 2026 is unconfirmed. Existing general rules (UU ITE, copyright, personal data law) were not researched.
- Not found: Google/Flow terms on commercial use of outputs and copyrightability of AI-generated anime characters (check Flow/Google AI terms before monetizing); character IP filters block recognisable franchise characters per [AutoWeeb](https://autoweeb.com/blog/how-to-create-anime-videos-with-google-omni-flash) (3P).
