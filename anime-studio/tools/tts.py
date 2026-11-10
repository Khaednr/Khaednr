#!/usr/bin/env python3
"""Buat voiceover Bahasa Indonesia per shot dari episode.json memakai Edge-TTS.

Install:  pip install edge-tts
Pakai:    python tools/tts.py episodes/ep01/episode.json
          python tools/tts.py episodes/ep01/episode.json --voice id-ID-GadisNeural --rate=-5%

Setiap shot yang punya field "narasi" (teks yang dibaca) akan dibuatkan
audio/NN.mp3 dan field "voice" di JSON diisi otomatis.

CATATAN: Edge-TTS memakai layanan online Microsoft lewat library tidak resmi.
Cek syarat penggunaannya sebelum memonetisasi. Skrip ini BELUM dites di
lingkungan pengembangan (tanpa internet ke layanan tsb) -> tes di PC kamu.
"""
import argparse
import asyncio
import json
import sys
from pathlib import Path


async def synth(edge_tts, text, voice, rate, pitch, out):
    await edge_tts.Communicate(text, voice, rate=rate, pitch=pitch).save(str(out))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("episode_json")
    ap.add_argument("--voice", default=None, help="default: field 'voice_id' di JSON, atau id-ID-ArdiNeural")
    ap.add_argument("--rate", default="+0%")
    ap.add_argument("--pitch", default="+0Hz")
    ap.add_argument("--force", action="store_true", help="timpa audio yang sudah ada")
    args = ap.parse_args()

    try:
        import edge_tts
    except ImportError:
        sys.exit("Install dulu: pip install edge-tts")

    ep_path = Path(args.episode_json).resolve()
    base = ep_path.parent
    ep = json.loads(ep_path.read_text(encoding="utf-8"))
    voice = args.voice or ep.get("voice_id", "id-ID-ArdiNeural")
    (base / "audio").mkdir(exist_ok=True)

    for i, s in enumerate(ep["shots"], 1):
        text = s.get("narasi")
        if not text:
            continue
        rel = f"audio/{i:02d}.mp3"
        out = base / rel
        if out.exists() and not args.force:
            print(f"lewati {rel} (sudah ada, pakai --force untuk timpa)")
        else:
            print(f"buat {rel}: {text[:50]}")
            asyncio.run(synth(edge_tts, text, voice, args.rate, args.pitch, out))
        s["voice"] = rel

    ep_path.write_text(json.dumps(ep, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("episode.json diperbarui.")


if __name__ == "__main__":
    main()
