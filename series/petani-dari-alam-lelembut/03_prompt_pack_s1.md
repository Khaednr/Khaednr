# Petani dari Alam Lelembut — Prompt Pack Season 1 (Flow Characters + Omni Flash 1.2)

Menggantikan kolom "Prompt Omni" di `02_naskah_episode_s1.md`. Cerita, beat, dan caption di file 02 tetap berlaku. Versi yang sudah diperluas dan siap tempel ada di `04_prompt_siap_tempel.md` (dibuat dari file ini).

Status bukti pada setiap aturan: **[RESMI]** dokumen Google, **[VENDOR]** panduan penyedia pihak ketiga, **[UJI]** hipotesis yang harus Anda uji, **[DESAIN]** keputusan desain saya.

## 1. Setup karakter di Flow (kerjakan sekali, dalam satu proyek)

Fitur yang dipakai: tab **Characters** di menu kiri. Alur resmi: New Character, deskripsi, unggah atau generate **1–2 gambar** (minimal satu), isi nama, **Select a voice**, pilih atau buat suara, **Add to Character**, isi "Character info", **Done**. Karakter dipanggil di prompt dengan **`@Nama`**. Google menyebut karakter ini membundel wajah, pakaian, dan suara agar konsisten antar generasi **[RESMI: Flow Help]**.

Hal yang perlu diingat:
- Karakter bersifat **per proyek**: buat semua karakter di satu proyek, lalu kerjakan seluruh Season 1 di proyek itu. **[RESMI]**
- Referensi suara hanya bekerja di **Omni Flash** dan untuk video berbasis ingredients; referensi harus **satu pembicara**. Tidak bisa mengunggah audio untuk meniru suara. **[RESMI]**
- Batas jumlah karakter per shot di UI tidak dipublikasikan. API Omni 1.2 mengizinkan 6 gambar referensi, maksimal 3 per karakter untuk 2 karakter. Pack ini memakai **maksimal 2 karakter per shot**. **[DESAIN berdasarkan batas API]**
- Bahasa suara: Google hanya mengevaluasi bahasa Inggris untuk Omni; bahasa lain "mungkin berhasil, hasil bisa bervariasi". Hasil uji Anda sendiri adalah bukti terbaik untuk Indonesia. **[RESMI + catatan Anda]**
- Suara di Flow dibuat lewat **Create New Voice**: Base Voice (preset), Nama, **Voice Performance** (deskripsi teks gaya suara), pratinjau sampel 8 detik opsional, lalu Save New Voice. Daftar preset resmi tidak diterbitkan, jadi pilih Base Voice dengan mendengarkan. **[RESMI + gap]**

### Lembar isian per karakter

Gunakan teks Inggris untuk deskripsi (model dievaluasi dalam bahasa Inggris). Kalimat uji dibuat dalam bahasa Indonesia untuk pratinjau sampel 8 detik.

| Karakter | Nama di Flow | Character info (tempel) | Voice Performance (tempel) | Kalimat uji sampel |
|---|---|---|---|---|
| Danu | `Danu` | Danu Prasetyo, 29, laid-off Indonesian office worker turned farmer. Messy short black hair, thick eyebrows, tired kind eyes, rumpled white shirt with rolled sleeves, grey trousers, plain orange lanyard around his neck, green flip-flops. Deadpan, logical, easily flustered. | Tired, dry, deadpan young adult male voice, mid-low pitch, relaxed pace, speaks Bahasa Indonesia with a neutral Jakarta accent. | Ini bukan sihir, ini agronomi. |
| Laras | `Laras` | Laras, ghost keeper of the barn, looks seventeen. Long black hair half tied, moss-green kebaya, glowing gold sash, floats ten centimeters above the ground, pale softly blue-tinted skin, large calm eyes. Strict, formal, secretly caring. Gentle, never scary. | Soft, clear, formal young female voice with a faint ethereal echo, measured pace, speaks Bahasa Indonesia with a neutral accent. | Itu tidak tertulis di Aturan Lumbung! |
| Cokro | `Cokro` | Cokro, a knee-high bald imp (tuyul) with big round eyes, red shorts and a tiny coin pouch necklace. Cheeky, fast, greedy but loyal. | High-pitched, fast, cheeky child-like voice with a bouncy rhythm, calls Danu "Bos", speaks Bahasa Indonesia. | Aku tuyul, Bos! Spesialisasiku kepeng. |
| Gendro | `Gendro` | Juragan Gendro, a towering furry dark-brown spirit boss with warm orange eyes, brown batik beskap jacket, a large gemstone ring and a carved cane. Polite, sly, comic rather than frightening. | Deep, slow, smooth and polite villain voice with a soft chuckle "hoh-hoh", unhurried, speaks Bahasa Indonesia. | Hoh-hoh. Siapa berani menanam tanpa izinku? |
| Lurah | `Lurah` | Pak Lurah Wiro, a big friendly moss-green ogre village head with small tusks, plaid sarong and headband. Kind and anxious. | Warm, deep, slightly nervous gentle-giant voice, speaks Bahasa Indonesia. | Pupuk kandang simpanan. Cuma ini yang ada. |

Gambar tiap karakter: 1–2 gambar dari character sheet Nano Banana (depan + tiga perempat, latar polos). Aset lokasi dan Lontar tidak perlu jadi Character; masukkan sebagai ingredients bila perlu.

**Uji sebelum produksi (15 menit):** simpan setiap suara, dengarkan sampel 8 detik, dan nilai pelafalan bahasa Indonesia (1–5). Jika suara Cokro dan Danu terlalu mirip, ganti Base Voice, bukan Voice Performance.

## 2. Struktur prompt (satu shot = satu prompt)

Urutan lapisan, setiap lapisan satu atau dua kalimat terpisah **[RESMI: "gunakan kalimat terpisah untuk audio"; VENDOR: enam lapisan subjek, aksi, latar, kamera, cahaya, audio]**:

1. `{STYLE}`: gaya visual tetap.
2. **Shot:** `In a single continuous shot`, ukuran shot, gerak kamera, `no scene cuts`, latar dan cahaya. **[RESMI]**
3. **Action:** siapa melakukan apa, dengan `@Nama`. Maksimal dua beat bertanda waktu, mis. `[0-4s] ... [4-10s] ...`. **[RESMI: timecode blocks; VENDOR: waktu adalah anggaran, bukan titik frame presisi]**
4. **Speech:** ucapan. Format resmi Google Cloud: **titik dua setelah pembicara dan tanpa tanda kutip** untuk mencegah teks muncul di video. Contoh resmi: `A woman says: My name is Clara.` **[RESMI: Google Cloud]**. Beberapa vendor memakai tanda kutip; ini konflik terbuka (lihat uji A/B).
5. **Lip-sync:** satu kalimat tegas. Pembicara on-screen: `Her mouth moves in simple open-and-close shapes in sync with the words.` Narasi: `@Danu's mouth stays closed.` **[DESAIN/UJI]**: frasa "simple open-and-close shapes" tidak ada di dokumentasi.
6. **Sound design:** ambience dan SFX, bertanda waktu bila perlu (`At 5s a bright chime`). Awalan "Sound design:" memakai contoh resmi Google. **[RESMI]**
7. **Akhiran** (penolakan): `{END-V}` bila ada suara, `{END-S}` bila tanpa dialog. Penolakan di dalam prompt adalah cara resmi (tidak ada parameter negative prompt). **[RESMI]**

Aturan tambahan:
- **Satu pembicara per shot** bila bisa. Dua pembicara hanya jika perlu dan ditandai risiko S/T. Tulis `Only the named person speaks each line` bila ada dua. **[VENDOR]**
- Panjang ucapan: tidak ada batas resmi. Vendor menyarankan sekitar dua kalimat pendek dalam 8 detik. Pack ini menjaga ≤8 kata di klip 4 detik, ≤16 kata di klip 8–10 detik. **[VENDOR + DESAIN]**
- Prompt sedang: sekitar 80–130 kata total termasuk `{STYLE}`. Vendor melaporkan di atas ±100 kata model mulai "melawan"; keputusan presisi vs panjang ada di tangan Anda. **[VENDOR/UJI]**
- Jangan pakai tag `<FIRST_FRAME>` atau `<IMAGE_REF_0>`; Google menyebutnya usang. Pakai bahasa natural dan `@Nama`. **[RESMI]**
- Narasi dengan suara Danu saat Danu tidak terlihat: ada risiko wajahnya ikut muncul. Jika itu terjadi, ganti dengan `a deadpan young male voiceover` tanpa `@Danu`. **[UJI]**
- Edit lanjutan: satu perubahan per giliran, akhiri dengan `Keep everything else the same.` Maksimal 3–4 giliran, lalu regenerasi. **[RESMI + VENDOR]**
- Teks Lontar, angka, dan subtitle tidak dibuat Omni; tambahkan di editor. Musik dan efek tambahan juga di editor (musik milik sendiri).

## 3. Blok yang dipakai ulang

**{STYLE}**
```
2D Japanese anime, cel-shaded characters with thin dark outlines, painterly twilight backgrounds in indigo, tangerine, moss green and firefly gold, limited animation with held poses and subtle motion, soft film grain, vertical 9:16.
```

**{END-V}** (ada suara)
```
No music. No subtitles. No on-screen text. No other voice.
```

**{END-S}** (tanpa dialog)
```
No dialogue. No music. No subtitles. No on-screen text.
```

## 4. Uji A/B sebelum produksi massal

Jalankan di 360p pada shot Ep 1 S5 (Laras bicara). Catat hasil di tabel penilaian.

| Uji | Variasi A | Variasi B | Yang dinilai |
|---|---|---|---|
| T1 Format ucapan | `says in Indonesian ...: Hanya manusia ...` (tanpa kutip, resmi) | `says ...: "Hanya manusia ..."` (kutip, vendor) | Teks muncul di video? Ucapan utuh? |
| T2 Suara | Hanya `@Laras` (suara dari Characters) | `@Laras` + klausa suara di prompt (`in a calm, formal voice with a faint echo`) | Kecocokan dengan sampel suara |
| T3 Lip-sync | Dengan kalimat "simple open-and-close shapes" | Tanpa kalimat itu | Gerak mulut dan kealamian |
| T4 Narasi saat karakter tak terlihat | `A voiceover in @Danu's voice` | `A deadpan young male voiceover` | Wajah Danu ikut muncul? Kecocokan suara |
| T5 Pelafalan | Kalimat apa adanya | Suku kata dipisah dengan tanda hubung pada kata yang salah baca **[UJI, tidak ada bukti Veo/Omni menuruti ejaan fonetik]** | Pelafalan |

Tabel penilaian (isi per klip): pelafalan 1–5 · lip-sync 1–5 · kecocokan suara 1–5 · ucapan tambahan/hantu? · musik bocor? · teks/subtitle muncul? · jumlah percobaan.

Aturan keputusan: pilih variasi pemenang per uji, **bekukan** menjadi template, lalu perbarui `{STYLE}` dan pola ucapan di seluruh pack. Jangan ganti template di tengah musim.

---

## EP 1 — Sawah Tengah Malam

### S1 · 4 dtk · R · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous static extreme close-up, no scene cuts. A crumpled blank white paper letter drops into shallow muddy paddy water at night under cold moonlight.
Action: The paper lands and sinks slightly; concentric ripples spread and moonlight glints on the water.
Speech: A voiceover in @Danu's voice, tired and deadpan, says: Jumat, jam lima sore. Aku dipecat. @Danu is not visible.
Sound design: At 0s a soft plop of water, then quiet crickets and night wind.
{END-V}
```

### S2 · 8 dtk · R · cast: @Danu
```
{STYLE}
Shot: In a single continuous medium shot slowly pushing in to a medium close-up, no scene cuts. Night, cold moonlight, a narrow paddy dike between two cracked dry rice plots.
Action: @Danu stands on the dike looking down at the cracked earth, shoulders slumped, orange lanyard hanging; he moves only with a tired blink and a slow exhale.
Speech: A voiceover in @Danu's voice, tired and deadpan, says at 1s: Aset tersisa: dua petak sawah warisan kakek. Retak. Tak ada air. @Danu's mouth stays closed.
Sound design: Faint crickets, dry wind over cracked soil.
{END-V}
```

### S3 · 10 dtk · R · cast: @Danu
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. Night over dry paddy fields.
Action: [0-4s] Thick pale mist rises from the cracked paddy and fireflies drift upward. [4-10s] The night sky slowly warms into tangerine twilight while @Danu takes one step back, then holds the pose with widening eyes.
Speech: A voiceover in @Danu's voice, deadpan and uneasy, says at 3s: Kabutnya aneh. Terlalu hangat untuk tengah malam. @Danu's mouth stays closed.
Sound design: Crickets fade out at 4s, replaced by a low warm hum and a soft gust of wind.
{END-V}
```

### S4 · 10 dtk · R · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous slow lateral pan to the right, wide, no scene cuts. A village of wooden houses stacked on glowing rice terraces under a permanent orange twilight sky, paper lanterns and drifting fireflies, no people visible.
Speech: A voiceover in @Danu's voice, deadpan and amazed, says at 2s: Ini bukan kampungku. Ini Alam Lelembut. @Danu is not visible.
Sound design: Distant wind chimes, soft wind, a faint insect hum.
{END-V}
```

### S5 · 10 dtk · S · cast: @Laras, @Danu
```
{STYLE}
Shot: In a single continuous medium two-shot with a slow drift in, no scene cuts. Twilight mist at the edge of the village.
Action: @Laras floats out of the mist toward @Danu and points at a huge wooden barn far behind her; @Danu stares at it, startled. Her hair and gold sash sway gently; otherwise both hold their poses.
Speech: At 2s, @Laras says in Indonesian, in a calm, formal voice with a faint echo: Hanya manusia yang bisa menanam. Kami tidak bisa menyentuh apa pun. While speaking, her mouth moves in simple open-and-close shapes in sync with the words. @Danu does not speak.
Sound design: A soft shimmering echo around her voice, distant lantern chimes.
{END-V}
```
Uji A/B: T1–T3 di shot ini.

### S6 · 10 dtk · S · cast: @Danu
```
{STYLE}
Shot: In a single continuous slow push-in, no scene cuts. Inside a huge empty wooden rice barn, dust floating in beams of orange light.
Action: [0-5s] @Danu walks in, small against the vast space, one hand trailing along the wooden wall. [5-10s] A blank, softly glowing palm-leaf scroll fades into the air in front of him and floats there; there is no writing on it.
Speech: A voiceover in @Danu's voice says at 6s: Lalu benda ini muncul. @Danu's mouth stays closed.
Sound design: Footsteps on old wood and echoing room tone; at 5s a bright magical chime as the scroll appears.
{END-V}
```

### S7 · 8 dtk · S · cast: @Laras
```
{STYLE}
Shot: In a single continuous shot, no scene cuts: a close-up of a floating blank glowing palm-leaf scroll, then a slow pull-back revealing @Laras behind it.
Action: [0-3s] The scroll glows steadily. [3-8s] The camera pulls back to @Laras staring at it; her eyes dim and her expression turns grave; she holds the pose.
Speech: At 3s, @Laras says in Indonesian, in a calm, formal voice with a faint echo: Waktumu tujuh senja. Gagal, kau jadi penghuni. Her mouth moves in simple open-and-close shapes in sync with the words.
Sound design: A soft low rumble underneath and a faint shimmering echo on her voice.
{END-V}
```

---

## EP 2 — Tanah yang Lelah

### S1 · 4 dtk · R · cast: (suara @Laras)
```
{STYLE}
Shot: In a single continuous static extreme close-up, no scene cuts. A hand crushes a fistful of hard, cracked dark soil that crumbles like dust; no worms, no roots.
Action: Fingers close on the soil and dust trickles between them.
Speech: At 1s, from off-screen, @Laras says in Indonesian, soft and grave: Tanah ini dikutuk. @Laras is not visible.
Sound design: Dry crumbling soil and a faint wind.
{END-V}
```

### S2 · 8 dtk · R · cast: @Danu, @Laras
```
{STYLE}
Shot: In a single continuous medium two-shot with a slow push-in, no scene cuts. Orange twilight over a barren plot.
Action: @Danu kneels and squeezes a handful of soil into a ball that stays hard and cracks apart; @Laras hovers beside him with her arms crossed and a worried frown.
Speech: A voiceover in @Danu's voice, deadpan and analytical, says at 1s: Tes genggam: liat, padat, bahan organik nol. Ini bukan kutukan. Ini tanah lelah. @Danu's mouth stays closed; @Laras does not speak.
Sound design: Soil crumbling, a faint wind, lantern chimes far away.
{END-V}
```

### S3 · 10 dtk · S · cast: @Lurah
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. The village edge at dusk with a bamboo fence and wooden windows; translucent blue ghost villagers peek out and whisper, fireflies drifting.
Action: [0-6s] @Lurah drags a heavy sack across the ground toward the foreground, sweating and worried. [6-10s] He stops and lets the sack drop.
Speech: At 3s, @Lurah says in Indonesian, in a warm, deep, slightly nervous voice: Pupuk kandang simpanan. Cuma ini yang ada. His mouth moves in simple open-and-close shapes in sync with the words; the background villagers only whisper without words.
Sound design: Sack scraping on dirt, soft airy whispers, a heavy thud at 8s.
{END-V}
```

### S4 · 10 dtk · R · cast: @Danu
```
{STYLE}
Shot: In a single continuous medium shot, static camera, no scene cuts. A shallow pit at the edge of a dark plot at twilight.
Action: @Danu layers dry leaves, rice straw and manure into the pit, covers it with soil, then waters it from a bamboo dipper in smooth deliberate motions.
Speech: A voiceover in @Danu's voice, deadpan, says at 1s: Daun kering, jerami, pupuk kandang. Dicampur, ditutup, disiram. Itu kompos. @Danu's mouth stays closed.
Sound design: Rustling leaves, soil falling, water pouring, crickets.
{END-V}
```

### S5 · 10 dtk · S · cast: @Laras (latar), suara @Danu
```
{STYLE}
Shot: In a single continuous close-up of hands with a slow push-in, no scene cuts. Dark rich compost being worked into the soil.
Action: [0-6s] Bare hands mix dark compost into the soil. [6-10s] The soil seems to exhale a soft pale-green mist that rises. @Laras gasps, blurred in the soft-focus background.
Speech: At 2s, @Laras says in Indonesian, startled: Ini sihir! At 6s, a voiceover in @Danu's voice, calm and deadpan, says: Ini bukan sihir. Ini agronomi. Only the named person speaks each line; only @Laras is lip-synced.
Sound design: Wet crunch of soil, a soft exhale of air as the mist rises, a faint sparkle.
{END-V}
```

### S6 · 10 dtk · R · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous macro shot with a slow push-in, no scene cuts. A patch of dark, crumbly soil.
Action: A tiny green sprout pushes up through the soil and slowly unfolds two leaves while golden fireflies gather around it.
Speech: A voiceover in @Danu's voice, quiet and amazed, says at 4s: Tunas pertama. @Danu is not visible.
Sound design: Gentle soil crackle and a soft bright chime as the sprout opens.
{END-V}
```

### S7 · 8 dtk · S · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous static macro shot, no scene cuts. The same green sprout in dark soil.
Action: [0-3s] The sprout sways slightly. [3-5s] A tiny three-fingered hand reaches in from the side and plucks it out; the sprout vanishes. [5-8s] Hold on the empty soil.
Speech: At 5s, from off-screen, @Danu shouts in Indonesian: Siapa yang cabut?! @Danu is not visible.
Sound design: A small mischievous giggle at 4s, a tiny pluck, then silence.
{END-V}
```

---

## EP 3 — Tuyul Cari Kerja

### S1 · 4 dtk · R · cast: @Cokro
```
{STYLE}
Shot: In a single continuous static close-up, no scene cuts. A burlap sack of seeds at twilight.
Action: @Cokro grins slyly and stuffs seeds into his tiny coin pouch, glancing sideways.
Speech: A voiceover in @Danu's voice, deadpan, says at 1s: Tertangkap basah. @Cokro does not speak.
Sound design: Seeds rattling and a small sneaky giggle.
{END-V}
```

### S2 · 8 dtk · R · cast: @Danu, @Cokro
```
{STYLE}
Shot: In a single continuous medium shot, static camera, no scene cuts. Twilight village edge.
Action: @Danu holds @Cokro up at eye level by the waistband of his red shorts; @Cokro dangles with his small legs kicking and a sheepish grin.
Speech: At 1s, @Cokro says in Indonesian, high-pitched, fast and cheeky: Aku tuyul, Bos! Spesialisasiku kepeng, tapi di sini nggak ada kepeng! His mouth moves in simple open-and-close shapes in sync with the words. @Danu does not speak.
Sound design: Small kicking and fabric rustle, twilight crickets.
{END-V}
```

### S3 · 10 dtk · R · cast: @Danu, @Cokro
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. A plot overgrown with weeds at twilight.
Action: @Danu points at the weeds, then turns to @Cokro, who pouts with his arms crossed.
Speech: At 1s, @Danu says in Indonesian, tired and deadpan: Gulma rebutan cahaya, air, dan pupuk. Kau pencabutnya. Upah: sepertiga hasil. His mouth moves in simple open-and-close shapes in sync with the words. @Cokro does not speak.
Sound design: Rustling weeds and a light wind.
{END-V}
```

### S4 · 10 dtk · T · cast: @Danu, @Cokro (fallback: gambar diam + speed lines)
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. The same weedy plot at twilight.
Action: [0-3s] @Danu stands counting on his fingers. [3-7s] @Cokro sprints across the plot as a stylized speed-line blur and rows of weeds fly into the air. [7-10s] The plot is clear and @Cokro stands proudly.
Speech: A voiceover in @Danu's voice, deadpan and impressed, says at 7s: Dua ratus gulma. Delapan detik. @Danu's mouth stays closed.
Sound design: A fast zip at 3s, rustling plants flung into the air, a soft thud as they land.
{END-V}
```

### S5 · 10 dtk · R · cast: @Cokro, @Danu
```
{STYLE}
Shot: In a single continuous close two-shot with a slow push-in, no scene cuts. Twilight light.
Action: @Cokro proudly drags a heavy burlap seed sack stamped with a plain round emblem toward @Danu; @Danu frowns, picks out one seed and cracks it open between his thumbnails.
Speech: At 2s, @Cokro says in Indonesian, cheeky: Benih dari Juragan Gendro, Bos. Mahal, tapi katanya unggul. His mouth moves in simple open-and-close shapes in sync with the words. @Danu does not speak.
Sound design: Sack scraping and a tiny crack of the seed.
{END-V}
```

### S6 · 10 dtk · S · cast: @Laras
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. A twilight village square.
Action: A line of translucent blue ghost villagers holds empty sacks stamped with the same round emblem; @Laras stands at the front watching sadly, her hair and sash swaying.
Speech: At 3s, @Laras says in Indonesian, soft and formal with a faint echo: Setiap musim kami beli lagi. Selalu. Her mouth moves in simple open-and-close shapes in sync with the words; the villagers stay silent.
Sound design: Soft wind and a distant lantern chime.
{END-V}
```

### S7 · 8 dtk · R · cast: @Danu, @Gendro
```
{STYLE}
Shot: In a single continuous static close-up of @Danu's face, no scene cuts. Far behind him, a huge silhouette of @Gendro with a cane stands against the orange sky.
Action: @Danu's eyes narrow slowly while the silhouette stays still.
Speech: A voiceover in @Danu's voice, deadpan and sharp, says at 1s: Sekali tanam, lalu beli lagi? Itu bukan unggul. Itu langganan. @Danu's mouth stays closed.
Sound design: A low rising rumble underneath and a single cane tap at 6s.
{END-V}
```

---

## EP 4 — Benih Langganan

### S1 · 4 dtk · R · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous static extreme close-up, no scene cuts. A wooden plank holds two small piles of rice seeds side by side, one glossy and uniform, one dull and mixed.
Action: A gentle breeze moves a single husk.
Speech: A voiceover in @Danu's voice, deadpan, says at 0.5s: Satu bikin untung. Satu bikin buntung. @Danu is not visible.
Sound design: Soft wood creak and a light wind.
{END-V}
```

### S2 · 8 dtk · R · cast: @Danu
```
{STYLE}
Shot: In a single continuous wide shot, no scene cuts. A second-generation paddy plot with uneven plant heights and empty grain heads at twilight.
Action: @Danu walks slowly along the dike, glancing at the plants.
Speech: A voiceover in @Danu's voice, deadpan, says at 1s: Generasi pertama rapi. Generasi kedua kacau. Hibrida tidak diwariskan. @Danu's mouth stays closed.
Sound design: Wind through uneven rice and slow footsteps.
{END-V}
```

### S3 · 10 dtk · R · cast: @Laras, @Danu
```
{STYLE}
Shot: In a single continuous medium two-shot with a slow push-in, no scene cuts. The uneven plot at twilight.
Action: @Laras floats beside @Danu looking down at the uneven plants with a crushed expression; @Danu rubs the back of his neck.
Speech: At 2s, @Laras says in Indonesian, soft and formal with a faint echo: Kami kira desa ini dikutuk. Ternyata cuma salah beli. Her mouth moves in simple open-and-close shapes in sync with the words. @Danu does not speak.
Sound design: Wind and distant lantern chimes.
{END-V}
```

### S4 · 10 dtk · S · cast: @Laras, @Danu
```
{STYLE}
Shot: In a single continuous medium shot, static camera, no scene cuts. The floor of the big barn in orange light.
Action: @Laras points at a wooden floorboard; @Danu kneels and pries it open, revealing a dark hollow beneath.
Speech: At 1s, @Laras says in Indonesian, soft and formal: Satu yang tak pernah dijual Gendro: padi tua simpanan kami. Her mouth moves in simple open-and-close shapes in sync with the words. @Danu does not speak.
Sound design: Wood scraping, a plank creak at 6s, soft echo in the barn.
{END-V}
```

### S5 · 10 dtk · R · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous close-up with a slow push-in, no scene cuts. A dark hollow beneath the barn floor.
Action: An old clay jar filled with glowing golden rice grains sits in the hollow; fireflies gather around its opening.
Speech: A voiceover in @Danu's voice, quiet and amazed, says at 2s: Pari Lelembut. Varietas lokal. Hasil panennya boleh jadi benih lagi. @Danu is not visible.
Sound design: Grains shifting inside the jar and a warm soft chime.
{END-V}
```

### S6 · 10 dtk · R · cast: @Danu, @Cokro
```
{STYLE}
Shot: In a single continuous medium shot, static camera, no scene cuts. A dark plot at dusk.
Action: @Danu and @Cokro kneel and plant seedlings in a neat row; @Cokro pats the soil proudly.
Speech: A voiceover in @Danu's voice, deadpan and warm, says at 2s: Mulai sekarang kita tidak beli. Kita menabung benih. @Danu's mouth stays closed.
Sound design: Soil being patted, seedlings rustling, crickets.
{END-V}
```

### S7 · 8 dtk · S · cast: @Gendro
```
{STYLE}
Shot: In a single continuous low-angle static shot, no scene cuts. The big barn doors at dusk.
Action: The doors burst open and the huge silhouette of @Gendro with his cane fills the doorway while paper lanterns swing.
Speech: At 3s, @Gendro says in Indonesian, deep, slow and smooth, with a soft chuckle: Hoh-hoh. Siapa berani menanam tanpa izinku? Only his voice speaks.
Sound design: Doors slam open at 0s, lanterns creak and swing.
{END-V}
```

---

## EP 5 — Bunga Berbunga

### S1 · 4 dtk · R · cast: @Gendro
```
{STYLE}
Shot: In a single continuous static close-up, no scene cuts. A wooden table in a village hall.
Action: @Gendro's huge furry hand with a big gemstone ring slides a rolled scroll onto the table; his face stays out of frame.
Speech: At 1s, @Gendro says in Indonesian, deep and smooth: Hutang desa: seratus pikul. His face is not visible.
Sound design: A scroll rolling on wood and a ring clink.
{END-V}
```

### S2 · 8 dtk · S · cast: @Gendro, @Lurah
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. A village meeting hall with wooden pillars and paper lanterns.
Action: @Gendro sits grinning at the table; @Lurah stands sweating and wringing his hands.
Speech: At 1s, @Gendro says in Indonesian, deep, smooth and polite: Bunga dua puluh persen per senja. Cicil kapan saja, Lurah. His mouth moves in simple open-and-close shapes in sync with the words. @Lurah does not speak.
Sound design: Lantern creak and a nervous gulp.
{END-V}
```

### S3 · 10 dtk · R · cast: @Danu, @Gendro (kabur)
```
{STYLE}
Shot: In a single continuous foreground close-up, static, no scene cuts. A twig draws blank lines in the soil while @Danu crouches; @Gendro stands out of focus in the background.
Action: The twig scratches several straight lines into the soil; there is no writing.
Speech: A voiceover in @Danu's voice, deadpan, says at 1s: Seratus kali satu koma dua, tujuh kali: tiga ratus lima puluh delapan pikul. @Danu's mouth stays closed.
Sound design: A twig scratching soil.
{END-V}
```

### S4 · 10 dtk · S · cast: @Lurah
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. A village hall at twilight.
Action: Translucent blue villagers gasp with their hands over their mouths and soft shock lines around their heads; @Lurah stands among them with wide eyes.
Speech: At 2s, @Lurah says in Indonesian, in a warm, deep, nervous voice: Astaga... His mouth moves in sync; the other villagers gasp wordlessly.
Sound design: A collective soft gasp.
{END-V}
```

### S5 · 10 dtk · R · cast: @Danu, @Gendro
```
{STYLE}
Shot: In a single continuous medium two-shot, static camera, no scene cuts. Twilight in front of the barn.
Action: @Danu stands and offers a handshake to @Gendro, who looks at the hand with amusement.
Speech: At 1s, @Danu says in Indonesian, calm and deadpan: Bunga tetap, bukan berbunga. Lunas saat panen. Gagal, tanah desa jadi milikmu. His mouth moves in simple open-and-close shapes in sync with the words. @Gendro does not speak.
Sound design: A low murmur of the village at dusk.
{END-V}
```

### S6 · 10 dtk · R · cast: @Gendro, @Danu
```
{STYLE}
Shot: In a single continuous close-up of two hands with a slow push-in, no scene cuts. @Gendro's ring-heavy hand shakes @Danu's hand; the ring glints in the twilight.
Speech: At 3s, @Gendro says in Indonesian, deep and smooth: Tujuh senja, anak muda. Tak sehari lebih. His face is not visible.
Sound design: A ring clink and a leather creak.
{END-V}
```

### S7 · 8 dtk · R · cast: @Danu, @Laras
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. The edge of a dry field under tangerine twilight.
Action: @Danu stands alone in front; @Laras floats a little behind him looking worried.
Speech: A voiceover in @Danu's voice, deadpan and resolved, says at 2s: Aku butuh air. Banyak. @Danu's mouth stays closed.
Sound design: A soft wind.
{END-V}
```

---

## EP 6 — Air Terkunci

### S1 · 4 dtk · R · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. A dry riverbed with cracked stones, a huge wooden dam far in the distance, orange sky.
Speech: A voiceover in @Danu's voice, deadpan, says at 0.5s: Sungai ada. Airnya dikunci. @Danu is not visible.
Sound design: Dry wind and distant creaking wood.
{END-V}
```

### S2 · 8 dtk · R · cast: @Danu, @Lurah
```
{STYLE}
Shot: In a single continuous medium two-shot, static camera, no scene cuts. Dry village irrigation channels at twilight.
Action: @Lurah shrugs sadly while @Danu looks at the empty channel.
Speech: At 2s, @Lurah says in Indonesian, in a warm, deep, gloomy voice: Bendungnya milik Juragan. His mouth moves in simple open-and-close shapes in sync with the words. @Danu does not speak.
Sound design: Dry wind.
{END-V}
```

### S3 · 10 dtk · S · cast: @Danu, @Cokro
```
{STYLE}
Shot: In a single continuous close two-shot, no scene cuts. Soft twilight with light glinting on water.
Action: @Cokro holds a long transparent bamboo pipe filled with water, both ends resting against two sticks; @Danu kneels and sights along it.
Speech: A voiceover in @Danu's voice, deadpan, says at 1s: Pipa berisi air: kedua ujung selalu sama tinggi. Waterpass murah dan akurat. @Danu's mouth stays closed.
Sound design: Water sloshing in the pipe.
{END-V}
```

### S4 · 10 dtk · S · cast: @Danu, @Cokro
```
{STYLE}
Shot: In a single continuous high-angle wide shot with a slow pan, no scene cuts. Terraced fields at twilight.
Action: @Danu points along a diagonal line down the slope while @Cokro digs a shallow channel along the contour; a few blue silhouette villagers help in the distance.
Speech: A voiceover in @Danu's voice, deadpan, says at 1s: Salurannya mengikuti kontur, miring tipis. Biar air mengalir sendiri. @Danu's mouth stays closed.
Sound design: Digging and scraping soil.
{END-V}
```

### S5 · 10 dtk · R · cast: @Laras, @Lurah
```
{STYLE}
Shot: In a single continuous medium shot, static camera, no scene cuts. Sunset light over a channel.
Action: @Laras floats over the channel pointing upstream; @Lurah stands holding a hoe behind her.
Speech: At 2s, @Laras says in Indonesian, with newfound confidence and a faint echo: Pasal empat Aturan Lumbung: sepertiga air sungai milik desa. Itu tertulis! Her mouth moves in simple open-and-close shapes in sync with the words. @Lurah does not speak.
Sound design: A soft lantern chime.
{END-V}
```

### S6 · 10 dtk · S · cast: @Lurah
```
{STYLE}
Shot: In a single continuous wide shot, no scene cuts. A dam at dusk with a channel running below it.
Action: @Lurah lifts a wooden sluice gate on the dam and water bursts through, flowing down the contour channel lit by drifting fireflies toward the dry plots.
Speech: A voiceover in @Danu's voice, quiet and amazed, says at 6s: Air datang. @Danu is not visible.
Sound design: Wood groaning, rushing water that settles into a gentle gurgle.
{END-V}
```

### S7 · 8 dtk · R · cast: @Gendro
```
{STYLE}
Shot: In a single continuous low-angle static shot, no scene cuts. The top of the dam against the orange sky.
Action: The silhouette of @Gendro stands on the dam looking down at the flowing channel, tapping his cane, with a sly smile.
Speech: At 2s, @Gendro says in Indonesian, deep, slow and smooth: Pasal empat, ya? Kalau begitu, kuberi mereka hadiah. Only his voice speaks.
Sound design: A cane tap and distant water far below.
{END-V}
```

---

## EP 7 — Ulat Api

### S1 · 4 dtk · R · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous static macro shot, no scene cuts. Glowing red caterpillars crawl across green rice leaves that are full of holes.
Speech: A voiceover in @Danu's voice, grim and deadpan, says at 0.5s: Ulat api. Dalam semalam. @Danu is not visible.
Sound design: Tiny munching and leaf crinkle.
{END-V}
```

### S2 · 8 dtk · R · cast: @Danu
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. Paddy plots with chewed leaves and trails of caterpillars at twilight.
Action: @Danu stands pensive in the foreground with his arms crossed; translucent villagers in the background panic silently.
Speech: A voiceover in @Danu's voice, deadpan, says at 1s: Hama titipan. Pasti kiriman Gendro. @Danu's mouth stays closed.
Sound design: Wind and faint munching.
{END-V}
```

### S3 · 10 dtk · T · cast: @Danu, @Laras (dua pembicara)
```
{STYLE}
Shot: In a single continuous close two-shot, static camera, no scene cuts. Twilight in the paddy.
Action: @Danu calmly picks one caterpillar off a leaf with two fingers while @Laras throws her arms wide in alarm.
Speech: At 1s, @Laras says in Indonesian, alarmed: Pakai mantra! At 4s, @Danu replies in Indonesian, calm and deadpan: Hitung dulu. Semprot sembarangan membunuh musuh alami. Only the named person speaks each line. Each mouth moves in simple open-and-close shapes in sync with their own line only.
Sound design: A light breeze.
{END-V}
```
Fallback jika suara tertukar: pecah menjadi dua klip (Laras sendiri, lalu Danu sendiri).

### S4 · 10 dtk · S · cast: @Cokro, @Danu
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. The edge of a paddy at twilight with fireflies.
Action: @Cokro plants rows of bright orange and pink cosmos flowers along the paddy edges while @Danu points to where to plant.
Speech: A voiceover in @Danu's voice, deadpan, says at 1s: Bunga kenikir di pematang. Mengundang predator alami. @Danu's mouth stays closed.
Sound design: Soil digging and rustling flowers.
{END-V}
```

### S5 · 10 dtk · S · cast: @Laras
```
{STYLE}
Shot: In a single continuous close-up with a slow push-in, no scene cuts. A single flower stem in the twilight.
Action: @Laras's trembling hand reaches out and, for the first time, her fingers close around a flower stem instead of passing through; a soft gold flash.
Speech: At 2s, @Laras says in Indonesian, softly and amazed: Aku... memegangnya? At 6s, a voiceover in @Danu's voice, warm, says: Yang kutanam bisa kau sentuh. Only the named person speaks each line.
Sound design: A soft gold chime when her fingers close.
{END-V}
```

### S6 · 10 dtk · S · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous dawn wide shot, no scene cuts. Golden morning light over a paddy.
Action: Tiny birds land across the paddy and glittering spider webs spread over the leaves as the caterpillars vanish.
Speech: A voiceover in @Danu's voice, deadpan and satisfied, says at 2s: Burung kecil dan laba-laba bekerja. Gratis. @Danu is not visible.
Sound design: Birdsong and soft dawn ambience.
{END-V}
```

### S7 · 8 dtk · T · cast: @Danu, @Lurah (fallback: 3 siluet saja)
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. Dusk at the edge of the paddy.
Action: A line of buto silhouettes carrying torches marches toward the paddy in the far distance; @Lurah steps forward beside @Danu and stands protectively.
Speech: A voiceover in @Danu's voice, deadpan and tense, says at 2s: Besok panen. Dan dia sudah di sini. @Danu's mouth stays closed.
Sound design: Distant marching and crackling torches.
{END-V}
```

---

## EP 8 — Panen Pertama

### S1 · 4 dtk · R · cast: (suara @Danu)
```
{STYLE}
Shot: In a single continuous static extreme close-up, no scene cuts. Golden rice stalks heavy with grain sway, backlit by a tangerine sky.
Speech: A voiceover in @Danu's voice, quiet and solemn, says at 0.5s: Senja ketujuh. @Danu is not visible.
Sound design: Rustling rice and a light wind.
{END-V}
```

### S2 · 8 dtk · S · cast: @Danu
```
{STYLE}
Shot: In a single continuous wide static shot, no scene cuts. A golden paddy at twilight.
Action: Translucent villagers watch from the edge, unable to touch the crop; @Danu bows to cut a stalk with a sickle; a line of buto silhouettes waits opposite.
Speech: A voiceover in @Danu's voice, calm and warm, says at 1s: Aturannya: yang tumbuh dari tangan manusia, bisa disentuh siapa pun. @Danu's mouth stays closed.
Sound design: Sickle cuts and wind.
{END-V}
```

### S3 · 10 dtk · S · cast: @Danu, @Lurah
```
{STYLE}
Shot: In a single continuous medium close-up, static camera, no scene cuts. Golden twilight.
Action: @Danu hands a sickle to @Lurah, who takes it tentatively; his hand does not pass through and his eyes widen.
Speech: At 4s, @Lurah says in Indonesian, in a warm, deep, amazed voice: Aku... bisa memegangnya? His mouth moves in simple open-and-close shapes in sync with the words. @Danu does not speak.
Sound design: A wooden handle clack and a soft chime when he grips it.
{END-V}
```

### S4 · 10 dtk · T · cast: @Laras, @Cokro (fallback: gambar diam + gerak ambien)
```
{STYLE}
Shot: In a single continuous wide slow pan, no scene cuts. A golden paddy under a tangerine sky.
Action: @Laras and @Cokro harvest golden rice bundles together with a few glowing blue silhouette villagers; fireflies stream upward.
Sound design: Rustling rice, sickles cutting, a gentle chime of fireflies.
{END-S}
```

### S5 · 10 dtk · S · cast: @Danu, @Gendro
```
{STYLE}
Shot: In a single continuous close two-shot, static camera, no scene cuts. Inside the barn, a mountain of rice sacks glowing in orange light.
Action: @Gendro stands before the sacks with his jaw dropping and his ring dimming; @Danu counts with small twigs.
Speech: At 1s, @Danu says in Indonesian, calm and triumphant: Hutang seratus pikul, bunga tetap dua puluh. Total seratus dua puluh. Lunas. His mouth moves in simple open-and-close shapes in sync with the words. @Gendro does not speak.
Sound design: Twigs clicking and the barn's soft echo.
{END-V}
```

### S6 · 10 dtk · S · cast: @Laras
```
{STYLE}
Shot: In a single continuous slow push-in, no scene cuts. The barn interior glowing with grain.
Action: @Laras holds a rice stalk in both hands; golden sparks fall from her eyes.
Speech: At 3s, @Laras says in Indonesian, in a trembling, soft voice with a faint echo: Seratus tahun. Aku tak pernah memegang padi. Her mouth moves in simple open-and-close shapes in sync with the words.
Sound design: A soft shimmering echo and the rustle of rice.
{END-V}
```

### S7 · 8 dtk · R · cast: @Danu
```
{STYLE}
Shot: In a single continuous close-up of @Danu's face lit by a screen, static camera, no scene cuts. A misty paddy edge with a faintly glowing portal in the dike.
Action: @Danu holds an old smartphone that lights up and vibrates; his eyes widen and he holds the pose.
Speech: At 3s, a tinny voice from the phone speaker, an unseen middle-aged man, says in Indonesian: Danu, kami butuh kamu kembali. Gaji dua kali lipat. @Danu does not speak and his mouth stays closed.
Sound design: A phone ringtone for the first 2 seconds, then a faint mist hum.
{END-V}
```

---

## Hal yang belum terverifikasi (dari riset)

- Kualitas dan lip-sync bahasa Indonesia di Omni belum ada sumber; hasil uji Anda adalah dasar.
- Tidak ada daftar resmi suara preset, bahasa per suara, atau uji drift suara/kostum di banyak klip.
- Batas karakter per shot di UI Flow tidak dipublikasikan; pack memakai maksimal 2.
- Format ucapan: dokumen Google Cloud menyarankan tanpa kutip; vendor memakai kutip. Uji T1.
- Frasa lip-sync "simple open-and-close shapes" dan klausa "limited animation" adalah rancangan saya.
- Biaya kredit Nano Banana di Flow tidak ditemukan. Biaya klip: lihat file 01 (60 kredit per putaran 60 detik di 360p).
