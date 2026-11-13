# Petani dari Alam Lelembut — Prompt Nano Banana: Karakter Master, Character Sheet, Expression Sheet

Dibuat untuk tahap sebelum membuat karakter di Flow (tab Characters). Status bukti: **[RESMI]** halaman bantuan Flow, **[KOMUNITAS]** panduan pihak ketiga, **[UJI]** hipotesis yang perlu Anda uji, **[DESAIN]** keputusan saya.

## 1. Alur kerja (3 tahap per karakter)

1. **Master:** generate dari teks (tanpa referensi). Buat 4 varian, pilih satu yang paling kuat sebagai acuan permanen. **[DESAIN]**
2. **Character sheet:** lampirkan master sebagai referensi, minta turnaround (depan, tiga perempat, samping, belakang) + detail + swatch warna. **[KOMUNITAS: pola master lalu sheet lalu dipakai ulang sebagai referensi]**
3. **Expression sheet:** lampirkan master lagi (bukan sheet), minta 6 ekspresi dalam grid 3×2. **[DESAIN]**
4. Untuk Flow Characters unggah **maksimal 2 gambar**: (a) master full-body, (b) potongan wajah depan netral dari expression sheet. **Jangan unggah seluruh sheet**; dokumentasi resmi hanya menyebut "1 atau 2 gambar yang menunjukkan penampilan karakter" dan tidak membahas sheet atau kolase. **[RESMI untuk 1–2 gambar; DESAIN/UJI untuk potongan]**
5. Sheet dan ekspresi dipakai juga sebagai referensi saat membuat gambar lokasi dan storyboard still.

**Pengaturan yang disarankan** (cek ketersediaan di UI Anda): master rasio portrait (3:4 atau 9:16), character sheet 16:9, expression sheet 3:2 atau 16:9. Model: Nano Banana Pro untuk master dan sheet bila kredit cukup; Nano Banana 2.1 sebagai standar; 2 Lite hanya untuk draf cepat. Biaya kredit gambar belum ditemukan, jadi cek di kotak prompt. Gunakan model yang sama untuk satu karakter dari master sampai sheet.

## 2. Blok yang dipakai di semua prompt

- **STYLE:** 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render.
- **BG:** Plain flat light grey background, soft even studio lighting, no cast shadows.
- **ANAT:** Correct anatomy, five fingers on each hand, symmetrical eyes.
- **NOTEXT:** No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
- **REF:** Use the attached image as the exact character reference.
- **LOCK:** Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything.

Semua prompt di bawah sudah memuat blok ini, jadi tinggal salin. Teks sengaja dilarang agar tidak ada tulisan palsu di lanyard, kartu, atau sheet; label bisa ditambahkan belakangan di editor.

## 3.1 Danu Prasetyo (protagonis)

*Varian Ep 2+: caping bambu tergantung di punggung (lihat bagian varian).*

### A. Master (teks ke gambar)
```
2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Full-body character design of Danu, a 29-year-old Indonesian man, slim build, about 175 cm tall. Messy short black hair, thick dark eyebrows, tired but kind dark-brown eyes with faint eye bags, light-brown skin, small relaxed mouth. Costume: rumpled white button-up shirt with sleeves rolled to the elbows and the top button open, plain grey work trousers, a plain orange lanyard hanging around his neck with a blank plain card (no writing on it), green rubber flip-flops. Pose: relaxed neutral standing pose with arms loosely at his sides and a hint of tired resignation. Framing: full body from head to toe, centered, slight three-quarter view, with a little empty space around the figure. Plain flat light grey background, soft even studio lighting, no cast shadows. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### B. Character sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create a character turnaround sheet of the same character on one wide image. Top row: four full-body views in the same neutral standing pose, equal scale and evenly spaced: front view, three-quarter view, side view, back view. Bottom row: three close-up details (a face close-up, the blank orange lanyard card in his hand, the flip-flops and trouser hem) next to 6 flat color swatches: skin, hair, shirt, trousers, lanyard, flip-flops. Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### C. Expression sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create an expression sheet of the same character: a grid of six head-and-shoulders portraits arranged in 3 columns by 2 rows, same camera angle, same scale and same lighting in every cell. Expressions in reading order: 1) tired neutral with half-lidded eyes; 2) deadpan flat stare with one eyebrow raised; 3) flustered panic with wide eyes and a sweat drop; 4) sudden realization with bright eyes and a small confident smirk; 5) amazed with mouth slightly open and eyes wide; 6) sheepish embarrassed smile with one hand rubbing the back of his neck; Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

**Titik periksa khusus:** The lanyard must stay orange and its card blank. The flip-flops must be green.

## 3.2 Laras (arwah penjaga lumbung)

### A. Master (teks ke gambar)
```
2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Full-body character design of Laras, a gentle ghost girl who looks seventeen, slim, about 160 cm tall, floating ten centimeters above the ground with bare feet pointing slightly downward. Long straight black hair half tied up with a simple wooden hairpin, large calm dark eyes, pale skin with a very soft blue tint, small serious mouth, a gentle expression; absolutely not scary, no hollow eyes, no blood. Costume: a moss-green traditional kebaya with simple gold edging, a dark brown wrap skirt with a simple geometric batik pattern, a long gold sash (selendang) draped over her shoulders with a soft golden glow, bare feet. Pose: floating in a calm upright neutral pose with hands folded in front, hair and sash swaying slightly. Framing: full body from head to toe, centered, slight three-quarter view, with a little empty space around the figure. Plain flat light grey background, soft even studio lighting, no cast shadows. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### B. Character sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create a character turnaround sheet of the same character on one wide image. Top row: four full-body views in the same neutral standing pose, equal scale and evenly spaced: front view, three-quarter view, side view, back view. Bottom row: three close-up details (a face close-up, the glowing gold sash and a hand, the bare feet floating above the ground with a faint soft glow beneath) next to 6 flat color swatches: skin, hair, kebaya green, sash gold, skirt brown, glow gold. Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### C. Expression sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create an expression sheet of the same character: a grid of six head-and-shoulders portraits arranged in 3 columns by 2 rows, same camera angle, same scale and same lighting in every cell. Expressions in reading order: 1) calm neutral; 2) stern and strict with narrowed eyes; 3) worried with raised inner eyebrows; 4) startled gasp with a hand over her mouth; 5) soft gentle smile; 6) tearful but moved, eyes glistening with small golden sparkles; Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

**Titik periksa khusus:** Her feet must not touch the ground. Her look must stay gentle, never frightening.

## 3.3 Cokro (tuyul pencari kerja)

### A. Master (teks ke gambar)
```
2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Full-body character design of Cokro, a knee-high mischievous imp (tuyul), a small round-bellied toddler-like creature about 50 cm tall with a head about one third of his height. Completely bald shiny head, big round bright eyes, a small button nose, a wide cheeky grin with a small gap between the teeth, warm pale skin. Costume: plain red shorts and a tiny pouch of coins hanging from a string necklace, bare feet, no shirt. Pose: standing with both hands on his hips in a proud, cheeky stance. Framing: full body from head to toe, centered, slight three-quarter view, with a little empty space around the figure. Plain flat light grey background, soft even studio lighting, no cast shadows. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### B. Character sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create a character turnaround sheet of the same character on one wide image. Top row: four full-body views in the same neutral standing pose, equal scale and evenly spaced: front view, three-quarter view, side view, back view. Bottom row: three close-up details (a face close-up, the coin pouch necklace, the small hands and bare feet) next to 5 flat color swatches: skin, shorts red, pouch brown, coin gold, eye dark. Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### C. Expression sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create an expression sheet of the same character: a grid of six head-and-shoulders portraits arranged in 3 columns by 2 rows, same camera angle, same scale and same lighting in every cell. Expressions in reading order: 1) cheeky grin; 2) sneaky sideways glance with a finger over his lips; 3) sulky pout with arms crossed; 4) shocked with eyes and mouth wide open; 5) proud smile with chest puffed out; 6) greedy sparkle in his eyes staring at coins; Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

**Titik periksa khusus:** He must stay about 50 cm tall in proportion to other characters. The shorts must stay red.

## 3.4 Juragan Gendro (antagonis)

### A. Master (teks ke gambar)
```
2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Full-body character design of Juragan Gendro, a towering furry spirit boss (genderuwo) about three and a half meters tall, broad and heavy. Thick dark-brown fur over the body, a large expressive face with warm orange eyes, a flat wide nose, thick eyebrows and a polite sly smile with small blunt teeth; comic and charming rather than frightening, no blood, no horror elements. Costume: a brown batik beskap jacket with simple geometric patterns and gold buttons, a large red-orange gemstone ring on one finger, a carved wooden cane with a decorative top, barefoot with big furry feet. Pose: standing tall and upright with one hand resting on the cane in a polite but sly posture. Framing: full body from head to toe, centered, slight three-quarter view, with a little empty space around the figure. Plain flat light grey background, soft even studio lighting, no cast shadows. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### B. Character sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create a character turnaround sheet of the same character on one wide image. Top row: four full-body views in the same neutral standing pose, equal scale and evenly spaced: front view, three-quarter view, side view, back view. Bottom row: three close-up details (a face close-up, the hand with the gemstone ring, the carved cane top and the jacket pattern) next to 6 flat color swatches: fur dark brown, eyes orange, jacket brown, gold buttons, ring red-orange, cane wood. Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### C. Expression sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create an expression sheet of the same character: a grid of six head-and-shoulders portraits arranged in 3 columns by 2 rows, same camera angle, same scale and same lighting in every cell. Expressions in reading order: 1) polite sly smile; 2) amused chuckle with eyes closed; 3) calm cold stare with one eyebrow lifted; 4) jaw-drop shock; 5) mock-friendly wide smile; 6) annoyed grumbling frown; Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

**Titik periksa khusus:** His face must stay comic, not scary. The ring must be large and red-orange.

## 3.5 Pak Lurah Wiro (kepala desa buto)

### A. Master (teks ke gambar)
```
2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Full-body character design of Pak Lurah Wiro, a big friendly moss-green ogre (buto) village head about three meters tall, heavy-set. Moss-green skin, small round tusks, a big round nose, kind worried eyes with heavy eyebrows, round cheeks. Costume: a plain dark sleeveless vest, a red-and-black plaid sarong wrapped around the waist, a simple cloth headband in the udeng style, bare feet, large hands. Pose: standing with both big hands nervously held in front of his belly. Framing: full body from head to toe, centered, slight three-quarter view, with a little empty space around the figure. Plain flat light grey background, soft even studio lighting, no cast shadows. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### B. Character sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create a character turnaround sheet of the same character on one wide image. Top row: four full-body views in the same neutral standing pose, equal scale and evenly spaced: front view, three-quarter view, side view, back view. Bottom row: three close-up details (a face close-up, the vest and plaid sarong, the big hands and bare feet) next to 6 flat color swatches: skin green, vest dark, sarong red, sarong black, headband cloth, tusk ivory. Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### C. Expression sheet (lampirkan master)
```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Create an expression sheet of the same character: a grid of six head-and-shoulders portraits arranged in 3 columns by 2 rows, same camera angle, same scale and same lighting in every cell. Expressions in reading order: 1) worried; 2) warm gentle smile; 3) nervous and sweating with darting eyes; 4) amazed, as if touching an object for the first time; 5) determined and brave; 6) sad and apologetic; Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

**Titik periksa khusus:** The tusks must stay small. The sarong must stay red-and-black plaid.

## 4. Prompt tambahan

### Lineup skala (lampirkan kelima master)

```
Use the five attached images as the exact character references. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Show all five characters standing side by side on flat ground, full body, in one row, at correct relative scale: Danu is 175 cm and is the human reference, Laras is 160 cm and floats ten centimeters above the ground, Cokro is only 50 cm tall and reaches Danu's knee, Lurah is 300 cm tall, Gendro is 350 cm tall and the tallest. Plain flat light grey background, soft even studio lighting, no cast shadows. Keep the face, hair, proportions, colors and costume exactly identical to the reference image; do not redesign anything. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### Varian Danu dengan caping (Ep 2+; lampirkan master Danu)

```
Use the attached image as the exact character reference. 2D Japanese anime character illustration, cel-shaded flat colors with soft two-tone shadows, clean thin dark outlines with consistent line weight, simple shading, no photorealism, no 3D render. Same character, same pose, same framing. Change only this: add a conical woven bamboo farmer's hat (caping) hanging on his back from a cord around his neck, resting between his shoulder blades. Keep everything else the same. Plain flat light grey background, soft even studio lighting, no cast shadows. Correct anatomy, five fingers on each hand, symmetrical eyes. No text, no letters, no numbers, no labels, no captions, no logos, no watermark.
```

### Perbaikan cepat (satu perubahan per giliran)

Pola: `Change only <X>. Keep everything else the same.` Pola ini resmi untuk edit video Omni; untuk gambar adalah **[UJI]**. Contoh:

```
Change only the lanyard card so it is completely blank with no writing. Keep everything else the same.
```
```
Change only the hands so each hand has exactly five fingers. Keep everything else the same.
```
```
Change only the background so it is plain flat light grey with no objects. Keep everything else the same.
```

## 5. Daftar periksa mutu gambar (sebelum diunggah ke Flow)

- [ ] Latar polos, tidak ada objek atau tulisan
- [ ] Lima jari di setiap tangan, mata simetris
- [ ] Warna dan kostum identik di master, sheet, dan ekspresi
- [ ] Garis tepi tipis dan konsisten
- [ ] Ciri khas ada: lanyard oranye polos (Danu), selendang emas dan kaki tidak menyentuh tanah (Laras), celana merah dan kantong kepeng (Cokro), cincin batu dan tongkat (Gendro), sarung kotak-kotak dan taring kecil (Lurah)
- [ ] Tidak menyeramkan (Laras dan Gendro harus tetap lembut/komik)
- [ ] Tinggi relatif benar di lineup skala
- [ ] Master dan potongan wajah siap untuk 1–2 gambar di Flow

## 6. Setelah gambar jadi

1. Buat 5 karakter di satu proyek Flow, isi Character info dan Voice Performance dari `03_prompt_pack_s1.md` bagian 1.
2. Dengarkan sampel suara 8 detik, nilai pelafalan Indonesia, lalu jalankan uji T1–T3 di Ep 1 S5.
3. Setelah karakter beres, kita lanjut ke prompt gambar lokasi dan Lontar Pamor.

## 7. Sumber dan batas bukti

- Resmi: [Flow Help: Characters](https://support.google.com/flow/answer/16935308?hl=en) (1–2 gambar, minimal satu, deskripsikan karakter secara rinci). Halaman itu tidak membahas format gambar, latar, atau sheet.
- Komunitas (tidak diverifikasi Google): pola master lalu sheet lalu dipakai ulang sebagai referensi, grid turnaround dan ekspresi, serta klausa "konsistensi" seperti LOCK ([Consistent Character Sheets in Nano Banana](https://videohighlight.com/v/f4HcdR3cd4M), [Aktagon: consistent imagery with Gemini](https://signals.aktagon.com/articles/2026/03/generating-consistent-imagery-with-gemini-a-practical-guide-to-building-a-prompt-based-generation-pipeline/), [Runware: character consistency](https://runware.ai/docs/models/google-nano-banana-2/guides/character-consistency.md)). Klaim persentase konsistensi di blog-blog itu tidak terverifikasi.
- Rancangan saya, perlu diuji: potongan wajah sebagai gambar kedua, grid 3×2, lineup skala, dan pola edit satu perubahan untuk gambar.
