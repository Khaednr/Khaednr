# Ep 1 — Prompt gambar per panel

Simpan hasil sebagai `panels/01.png` … `panels/10.png` (potret, 512×912 untuk SD1.5,
lalu upscale 2× bila sempat). Prompt berbahasa Inggris karena model dilatih dengan tag Inggris.

## Blok tetap (tempel di SETIAP prompt)

**STYLE**
```
masterpiece, best quality, manhwa style, webtoon style, clean lineart, soft cel shading,
warm golden hour lighting, detailed background, vertical composition
```

**RAKA**
```
1boy, 17 years old, short messy black hair, dark brown eyes, white school uniform shirt,
beige apron, long wooden spoon in apron pocket
```

**GELISAH**
```
small shadow creature, dark purple black smoke body, round white glowing eyes, wispy edges
```

**NEGATIVE**
```
lowres, bad anatomy, bad hands, extra fingers, missing fingers, text, watermark, signature,
blurry, jpeg artifacts, deformed face, extra limbs, nsfw
```

Tips konsistensi: pakai **seed sama** untuk panel dengan karakter sama, dan setelah punya
15–20 gambar Raka yang bagus → latih LoRA "raka" lalu ganti blok RAKA dengan trigger LoRA.

## Panel

| # | Isi adegan | Tambahan prompt (setelah STYLE) |
|---|---|---|
| 01 | Establishing: kedai kopi kecil di gang, sore, lampu hangat | `no humans, small cozy coffee shop exterior, narrow alley, wooden signboard, potted plants, sunset sky, warm window light` |
| 02 | Raka di balik meja bar, mengelap gelas, Mocha tidur di kasir | RAKA + `behind coffee counter, wiping a glass, calm expression, fat orange cat sleeping on cash register, coffee shop interior, upper body` |
| 03 | Mahasiswi kelelahan di meja pojok, laptop, kantung mata | `1girl, 22 years old, university student, long black hair in loose bun, dark circles under eyes, tired, oversized gray hoodie, laptop, stacks of paper, coffee cup, sitting at corner table, coffee shop interior` |
| 04 | Close-up bahu si mahasiswi: Gelisah menempel | panel 03 + GELISAH + `creature sitting on her shoulder, close-up, from behind, slightly ominous` |
| 05 | Gelisah membesar, latar menggelap ke teal-ungu | GELISAH + `large, looming, growing bigger, dark teal and purple background, dramatic lighting, low angle` |
| 06 | AKSI: Raka mencabut sendok kayu, speed lines | RAKA + `dynamic pose, drawing wooden spoon like a sword, determined eyes, speed lines, action lines, dark teal background, dramatic angle` |
| 07 | AKSI: ketukan — Gelisah pecah jadi serpihan cahaya | `wooden spoon striking, shadow creature bursting into warm golden light particles, impact, sparkles, radial light, dynamic composition, no humans` |
| 08 | Mahasiswi meregangkan badan, tersenyum tipis, cahaya hangat lagi | panel 03 tanpa `tired` + `stretching arms, small relieved smile, warm sunlight through window, floating golden light particles` |
| 09 | Raka menyelipkan sendok ke saku, Mocha membuka satu mata | RAKA + `putting wooden spoon back into apron pocket, gentle smile, orange cat opening one eye, coffee counter, evening light` |
| 10 | Teaser: siluet gadis jaket kuning di pintu, bayangan besar di belakangnya | `1girl, silhouette at coffee shop doorway, yellow jacket, ponytail, backlit by sunset, large shadow creature with white eyes behind her, mysterious, cinematic` |

## Pengaturan generate (SD1.5, GTX 1060 6GB)
- Resolusi **512×912**, sampler DPM++ 2M Karras, 24–28 steps, CFG 6–7.
- Hires fix / upscale 2× hanya untuk panel yang sudah lolos seleksi (hemat waktu).
- Buat 4 variasi per panel, pilih 1. Target: 10 panel jadi dalam ±1 jam.

## Caption & hashtag (draf)
> Ada yang menempel di bahumu hari ini? ☕ Kedai Senja — Episode 1.
> #KedaiSenja #animeindonesia #webtoonindonesia #manhwa #sliceoflife #ceritapendek

Catatan: jam posting dan hashtag masih **hipotesis** — belum ada data akun. Uji 2 minggu, baru putuskan.
