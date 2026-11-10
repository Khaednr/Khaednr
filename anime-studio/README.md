# Anime Studio — pipeline motion-comic 9:16

Pipeline untuk membuat episode anime pendek (30–45 detik) gaya donghua/manhwa/webtoon
untuk TikTok, YouTube Shorts, dan Facebook Reels. Dirancang untuk **GTX 1060 6GB / RAM 16GB**:
GPU hanya dipakai untuk membuat gambar; animasi, suara, dan perakitan jalan di CPU.

```
anime-studio/
├── series-bible.md          # premis, karakter, gaya, aturan dunia
├── tools/
│   ├── assemble.py          # panel + suara + subtitle -> video 1080x1920 (SUDAH DITES)
│   └── tts.py               # narasi Indonesia via Edge-TTS (BELUM dites, butuh internet)
└── episodes/ep01/
    ├── episode.json         # urutan shot, gerak kamera, narasi, caption
    ├── prompts.md           # prompt gambar per panel
    ├── panels/              # (kamu isi) 01.png ... 10.png
    └── audio/               # (dibuat tts.py) 01.mp3 ...
```

## Alur produksi satu episode

1. **Gambar** — generate panel sesuai `episodes/epXX/prompts.md`, simpan ke `panels/`.
2. **Suara** — `python tools/tts.py episodes/ep01/episode.json`
3. **Preview cepat** — `python tools/assemble.py episodes/ep01/episode.json --preview`
4. **Render final** — `python tools/assemble.py episodes/ep01/episode.json`
5. **QA** (checklist di bawah) → upload manual, nyalakan label konten AI.

## Kebutuhan di PC

| Kebutuhan | Untuk | Cek |
|---|---|---|
| Python 3.10+ | semua skrip | `python --version` |
| FFmpeg (libx264 + libass) | `assemble.py` | `ffmpeg -version` |
| `pip install edge-tts` | `tts.py` | — |
| ComfyUI atau Forge + model anime SD1.5 | gambar panel | — |

## episode.json

Path relatif terhadap folder episode.

| Field (global) | Arti | Default |
|---|---|---|
| `size` | resolusi output | `[1080, 1920]` |
| `fps` | frame per detik | `30` |
| `font`, `fontsize` | font subtitle (harus terpasang di sistem) | `Arial`, `68` |
| `bgm`, `bgm_volume` | musik latar (di-loop, dipotong sepanjang video) | tanpa BGM, `0.12` |
| `voice_id` | suara Edge-TTS | `id-ID-ArdiNeural` |

| Field (per shot) | Arti |
|---|---|
| `image` | **wajib** — file panel |
| `duration` | durasi minimum (detik). Kalau ada `voice`, otomatis diperpanjang mengikuti suara |
| `motion` | `zoom_in`, `zoom_out`, `pan_left`, `pan_right`, `pan_up`, `pan_down`, `shake`, `static` |
| `flash` | `true` = impact frame putih di awal shot (untuk aksi) |
| `fade_in` / `fade_out` | transisi hitam 0,3 detik |
| `caption` | subtitle bawah (`\n` untuk baris baru) |
| `tag` | label kuning kecil di atas (lokasi/waktu/CTA) |
| `narasi` | teks yang dibaca `tts.py` → mengisi `voice` |
| `voice`, `voice_volume` | file suara shot ini |
| `sfx`, `sfx_delay`, `sfx_volume` | efek suara |

## Checklist QA sebelum upload
- [ ] Hook terbaca dalam 3 detik pertama
- [ ] Wajah/kostum karakter konsisten antar panel
- [ ] Subtitle tidak menutupi wajah dan tidak tertutup UI platform
- [ ] Durasi 30–45 detik
- [ ] Musik/SFX/model/LoRA berlisensi untuk penggunaan komersial
- [ ] Label konten AI dinyalakan di tiap platform
- [ ] Tidak ada tangan/anatomi rusak yang mencolok

## Status pengujian
- `assemble.py`: dites dengan panel dummy + audio sintetis (preview 540×960 dan final 1080×1920,
  semua jenis motion utama, subtitle, flash, mix suara + BGM).
- `tts.py`: **belum** dites (lingkungan pengembangan tanpa akses ke layanan TTS).
- Episode 1: naskah + prompt siap; **gambar panel belum dibuat**.
