# Index Proyek: Riset Konten Anime dan Serial "Petani dari Alam Lelembut"

Terakhir diperbarui: 2026-11-14. Branch kerja: `ccr-55df892d-vx069r`.

Repositori ini juga repo profil GitHub (`README.md` di root adalah README profil dan tidak diubah). Seluruh isi proyek ada di tiga folder di bawah. Semua dokumen berbahasa Indonesia kecuali blok prompt (Inggris, karena Omni dan Nano Banana dievaluasi dalam bahasa Inggris).

## Alur proyek

```
Riset konten anime ─▶ Ide serial 60 detik ─▶ Riset Flow Characters + audio ─▶ Produksi serial
 (laporan 1)           (laporan 2 + pilot)     (catatan riset)                 (folder series/)
```

## 1. Laporan final (`reports/`)

| File | Isi | Dipakai untuk |
|---|---|---|
| [Konten anime YouTube TikTok](reports/Konten%20anime%20YouTube%20TikTok.md) | Format, niche, hak cipta, monetisasi, dan peluang kreator anime Indonesia di YouTube dan TikTok | Keputusan strategi platform dan risiko |
| [Ide serial anime 60 detik](reports/Ide%20serial%20anime%2060%20detik.md) | Studi kasus, tren genre, struktur episode 60 detik, kelayakan Omni Flash 1.2, 7 konsep serial, rencana 2 pilot | Memilih konsep (dipilih: Petani dari Alam Lelembut) |

## 2. Catatan riset mentah (`research_notes/`)

Setiap folder berisi catatan per peneliti dengan status bukti per klaim. Gunakan sebagai sumber sitasi dan untuk memeriksa ulang klaim laporan.

### `Konten anime YouTube TikTok/` (mendukung laporan 1)
| File | Topik |
|---|---|
| [youtube_formats_niches.md](research_notes/Konten%20anime%20YouTube%20TikTok/youtube_formats_niches.md) | Format dan niche anime di YouTube, kanal rujukan |
| [tiktok_formats_trends.md](research_notes/Konten%20anime%20YouTube%20TikTok/tiktok_formats_trends.md) | Format, hashtag, algoritma, dan skena Indonesia di TikTok |
| [copyright_policy_monetization_rules.md](research_notes/Konten%20anime%20YouTube%20TikTok/copyright_policy_monetization_rules.md) | Hak cipta, syarat YPP, Creator Rewards, UU 28/2014 |
| [monetization_indonesia_opportunities.md](research_notes/Konten%20anime%20YouTube%20TikTok/monetization_indonesia_opportunities.md) | RPM, audiens Indonesia, volume pencarian vidIQ, ceruk |

### `Ide serial anime 60 detik/` (mendukung laporan 2)
| File | Topik |
|---|---|
| [reference_series_case_studies.md](research_notes/Ide%20serial%20anime%2060%20detik/reference_series_case_studies.md) | Serial animasi/AI rujukan (Fruit Love Island, Anipops, Keluarga Somat) |
| [genre_trends_indonesia_whitespace.md](research_notes/Ide%20serial%20anime%2060%20detik/genre_trends_indonesia_whitespace.md) | Permintaan genre, horor lokal, celah pasar Indonesia |
| [episode_structure_retention.md](research_notes/Ide%20serial%20anime%2060%20detik/episode_structure_retention.md) | Struktur beat 60 detik, fitur serial TikTok dan YouTube |
| [omni_flash_feasibility_policy.md](research_notes/Ide%20serial%20anime%2060%20detik/omni_flash_feasibility_policy.md) | Kemampuan Omni 1.2, kredit, harga Indonesia, label AI |

### `Flow karakter dan prompt audio/` (mendukung folder `series/`)
| File | Topik |
|---|---|
| [flow_character_feature.md](research_notes/Flow%20karakter%20dan%20prompt%20audio/flow_character_feature.md) | Fitur Characters/Avatars/Ingredients di Flow, suara, batas, Indonesia |
| [omni_audio_prompt_syntax.md](research_notes/Flow%20karakter%20dan%20prompt%20audio/omni_audio_prompt_syntax.md) | Sintaks prompt dialog, narasi, SFX, lip-sync (resmi vs komunitas) |
| [community_references_indonesian_anime.md](research_notes/Flow%20karakter%20dan%20prompt%20audio/community_references_indonesian_anime.md) | Referensi komunitas, dialog non-Inggris, workflow konsistensi |

## 3. Produksi serial (`series/petani-dari-alam-lelembut/`)

Urutan baca dan pakai:

| # | File | Fungsi | Status |
|---|---|---|---|
| 01 | [series_dan_character_bible](series/petani-dari-alam-lelembut/01_series_dan_character_bible.md) | Premis, aturan dunia, 5 karakter, lokasi, palet, aturan produksi, busur 8 episode | Final draf |
| 02 | [naskah_episode_s1](series/petani-dari-alam-lelembut/02_naskah_episode_s1.md) | Beat, durasi, caption, CTA, rencana produksi dan uji. Kolom prompt-nya draf awal | Beat berlaku; prompt digantikan 03 |
| 03 | [prompt_pack_s1](series/petani-dari-alam-lelembut/03_prompt_pack_s1.md) | Setup Flow Characters, struktur prompt 7 lapisan, uji A/B T1–T5, 56 prompt per shot (dengan placeholder) | **Sumber prompt utama** |
| 04 | [prompt_siap_tempel](series/petani-dari-alam-lelembut/04_prompt_siap_tempel.md) | Hasil perluasan 03 (STYLE/END sudah ditempel) | Dibuat dari 03; jangan edit langsung |
| 05 | [prompt_nano_banana_karakter](series/petani-dari-alam-lelembut/05_prompt_nano_banana_karakter.md) | 20 prompt gambar: master, character sheet, expression sheet, lineup skala, varian caping | Siap pakai |

Alur kerja berikutnya (langkah Anda): buat gambar karakter dengan 05 → buat 5 karakter di Flow dan uji suara (03 §1) → uji A/B T1–T3 di Ep 1 S5 → produksi Ep 1–3 dengan 04 → ukur retensi.

## Keputusan yang sudah dikunci

- Pilot: **Petani dari Alam Lelembut** (isekai desa + sistem status, latar Nusantara), bukan Pantangan Desa.
- Format: vertikal 9:16, 8 episode × 60 detik (render 61–65 detik untuk TikTok, 60 detik untuk YouTube Shorts).
- Produksi: Google Flow, Omni Flash 1.2. **Audio, dialog, dan lip-sync dibuat di Omni** (tanpa VO terpisah), karakter lewat fitur **Characters** (`@Nama`).
- Grid shot tetap: 4/8/10/10/10/10/8 detik, semua ≤10 detik, draf di 360p.
- Karakter dan folklor orisinal; label AI diaktifkan; tidak ada elemen ritual atau agama.

## Status bukti (ringkas)

- **Resmi/terverifikasi:** syarat YPP, fitur Characters Flow, parameter Omni, harga paket Indonesia, kebijakan inauthentic content.
- **Estimasi:** semua RPM, biaya kredit per episode, ranking konsep, ambang metrik.
- **Belum ada bukti:** kualitas suara dan lip-sync bahasa Indonesia di Omni (hasil uji Anda adalah dasar), drift suara di banyak klip, retensi 60 detik untuk anime AI, kelayakan TikTok Creator Rewards di Indonesia.
- **Konflik terbuka:** ucapan tanpa kutip (Google Cloud) vs dengan kutip (vendor). Uji T1 di file 03.

## Belum dikerjakan

- Prompt gambar lokasi (Desa Sidasenja, Lumbung, ladang, bendungan, pematang) dan Lontar Pamor.
- Pembuatan karakter di Flow dan hasil uji T1–T5.
- Produksi dan unggah episode. Tidak ada yang dijadwalkan atau diposting.
- UU ITE dan regulasi label AI Indonesia belum diriset.

## Konvensi

- Nama folder riset = judul laporan; catatan memuat tiga bagian (Takeaway, Cited Findings dengan Inferences, Gaps).
- Tag bukti: **[RESMI]** dokumen Google/platform · **[VENDOR]** pihak ketiga · **[KOMUNITAS]** blog atau forum · **[UJI]** hipotesis · **[DESAIN]** keputusan desain.
- Placeholder prompt: `{STYLE}`, `{END-V}`, `{END-S}` hanya di file 03; file 04 sudah diperluas.
- Commit dibuat per tahap kerja pada branch di atas.
