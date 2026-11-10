#!/usr/bin/env python3
"""Rakit video motion-comic vertikal (9:16) dari panel gambar + suara + subtitle.

Hanya butuh: Python 3.8+ dan FFmpeg (dengan libx264, libass). Jalan di CPU.

Pakai:
    python tools/assemble.py episodes/ep01/episode.json
    python tools/assemble.py episodes/ep01/episode.json --out hasil.mp4 --preview

Format episode.json -> lihat anime-studio/README.md bagian "episode.json".
Path di dalam JSON relatif terhadap folder tempat episode.json berada.
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MOTIONS = ("zoom_in", "zoom_out", "pan_left", "pan_right", "pan_up", "pan_down", "shake", "static")


def run(cmd):
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if r.returncode != 0:
        sys.exit("FFmpeg gagal:\n$ " + " ".join(map(str, cmd)) + "\n" + r.stderr[-2000:])
    return r.stdout


def probe_duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "default=nw=1:nk=1", str(path)])
    return float(out.strip())


def zoompan_expr(motion, frames):
    """Return (z, x, y) ekspresi zoompan. 'on' = nomor frame, 'zoom' = zoom saat ini."""
    cx = "iw/2-(iw/zoom/2)"
    cy = "ih/2-(ih/zoom/2)"
    p = f"on/{max(frames - 1, 1)}"  # progres 0..1
    if motion == "zoom_in":
        return f"1+0.18*{p}", cx, cy
    if motion == "zoom_out":
        return f"1.18-0.18*{p}", cx, cy
    if motion == "pan_left":
        return "1.15", f"(iw-iw/zoom)*(1-{p})", cy
    if motion == "pan_right":
        return "1.15", f"(iw-iw/zoom)*{p}", cy
    if motion == "pan_up":
        return "1.15", cx, f"(ih-ih/zoom)*(1-{p})"
    if motion == "pan_down":
        return "1.15", cx, f"(ih-ih/zoom)*{p}"
    if motion == "shake":
        # getaran cepat meluruh -> kesan impact
        decay = f"(1-{p})"
        return ("1.12",
                f"{cx}+28*sin(on*1.7)*{decay}",
                f"{cy}+22*cos(on*2.3)*{decay}")
    return "1.0", cx, cy  # static


def build_shot(shot, dur, size, fps, out_path):
    w, h = size
    frames = max(int(round(dur * fps)), 1)
    z, x, y = zoompan_expr(shot.get("motion", "zoom_in"), frames)
    # Upscale 2x dulu agar zoompan tidak "bergetar" (jitter) lalu cover-crop ke 9:16.
    vf = [
        f"scale={w * 2}:{h * 2}:force_original_aspect_ratio=increase:flags=lanczos",
        f"crop={w * 2}:{h * 2}",
        f"zoompan=z='{z}':x='{x}':y='{y}':d={frames}:s={w}x{h}:fps={fps}",
    ]
    if shot.get("flash"):  # impact frame: putih sekejap di awal shot
        vf.append("fade=t=in:st=0:d=0.18:color=white")
    elif shot.get("fade_in", False):
        vf.append("fade=t=in:st=0:d=0.3")
    if shot.get("fade_out", False):
        vf.append(f"fade=t=out:st={max(dur - 0.3, 0):.2f}:d=0.3")
    vf.append("format=yuv420p")
    run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(shot["_image"]),
         "-vf", ",".join(vf), "-frames:v", str(frames), "-r", str(fps),
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-an", str(out_path)])


def ass_time(t):
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def build_ass(events, size, font, fontsize, path):
    w, h = size
    k = w / 1080  # skala margin/outline agar preview sama dengan hasil akhir
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {w}
PlayResY: {h}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,{font},{fontsize},&H00FFFFFF,&H000000FF,&H00101010,&H80000000,-1,0,0,0,100,100,0,0,1,{max(int(6*k),1)},2,2,{int(70*k)},{int(70*k)},{int(330*k)},1
Style: Tag,{font},{int(fontsize * 0.8)},&H0000D7FF,&H000000FF,&H00101010,&H80000000,-1,0,0,0,100,100,0,0,1,{max(int(5*k),1)},2,8,{int(70*k)},{int(70*k)},{int(260*k)},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    for start, end, style, text in events:
        text = text.replace("\\", "").replace("\n", "\\N").replace("{", "(").replace("}", ")")
        lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},{style},,0,0,0,,{{\\fad(120,120)}}{text}")
    Path(path).write_text(header + "\n".join(lines) + "\n", encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("episode_json")
    ap.add_argument("--out", help="file output .mp4 (default: <folder episode>/output.mp4)")
    ap.add_argument("--preview", action="store_true", help="resolusi 540x960, render cepat untuk cek timing")
    args = ap.parse_args()

    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            sys.exit(f"{tool} tidak ditemukan. Install FFmpeg dulu dan pastikan ada di PATH.")

    ep_path = Path(args.episode_json).resolve()
    base = ep_path.parent
    ep = json.loads(ep_path.read_text(encoding="utf-8"))
    fps = int(ep.get("fps", 30))
    size = tuple(ep.get("size", [1080, 1920]))
    if args.preview:
        size = (540, 960)
    font = ep.get("font", "Arial")
    fontsize = int(ep.get("fontsize", 68)) * size[0] // 1080
    out = Path(args.out) if args.out else base / ("preview.mp4" if args.preview else "output.mp4")

    shots = ep["shots"]
    if not shots:
        sys.exit("episode.json tidak punya shot.")

    # 1) Resolusi path + hitung durasi (suara menentukan batas bawah durasi shot)
    t = 0.0
    timeline = []
    for i, s in enumerate(shots, 1):
        img = base / s["image"]
        if not img.exists():
            sys.exit(f"Shot {i}: gambar tidak ada: {img}")
        s["_image"] = img
        if s.get("motion", "zoom_in") not in MOTIONS:
            sys.exit(f"Shot {i}: motion '{s['motion']}' tidak dikenal. Pilihan: {', '.join(MOTIONS)}")
        dur = float(s.get("duration", 3.0))
        voice = base / s["voice"] if s.get("voice") else None
        if voice:
            if not voice.exists():
                sys.exit(f"Shot {i}: file suara tidak ada: {voice}")
            dur = max(dur, probe_duration(voice) + float(s.get("voice_pad", 0.35)))
        timeline.append((s, dur, t, voice))
        t += dur
    total = t
    print(f"{len(shots)} shot, total {total:.1f} detik")
    if total > 60:
        print("PERINGATAN: durasi > 60 detik. Target episode 30-45 detik.")

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        # 2) Render tiap shot
        clips = []
        for i, (s, dur, start, _v) in enumerate(timeline, 1):
            clip = tmp / f"shot{i:02d}.mp4"
            print(f"  shot {i:02d}: {dur:.2f}s  {s.get('motion', 'zoom_in')}")
            build_shot(s, dur, size, fps, clip)
            clips.append(clip)
        listfile = tmp / "list.txt"
        listfile.write_text("".join(f"file '{c.as_posix()}'\n" for c in clips), encoding="utf-8")
        silent = tmp / "silent.mp4"
        run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(listfile),
             "-c", "copy", str(silent)])

        # 3) Subtitle (ASS)
        events = []
        for s, dur, start, _v in timeline:
            if s.get("caption"):
                delay = float(s.get("caption_delay", 0.15))
                events.append((start + delay, start + dur - 0.05, "Cap", s["caption"]))
            if s.get("tag"):  # label kecil di atas, mis. "SORE HARI - KEDAI SENJA"
                events.append((start + 0.1, start + dur - 0.05, "Tag", s["tag"]))
        ass = tmp / "subs.ass"
        build_ass(events, size, font, fontsize, ass)

        # 4) Audio: suara per shot di-offset ke awal shot + BGM + SFX opsional
        inputs, filters, labels = [], [], []
        idx = 1  # input 0 = video

        def add_audio(path, start, vol, trim=None, loop=False):
            nonlocal idx
            if loop:
                inputs.extend(["-stream_loop", "-1"])
            inputs.extend(["-i", str(path)])
            f = f"[{idx}:a]aresample=44100,aformat=channel_layouts=stereo"
            if trim:
                f += f",atrim=0:{trim:.2f},asetpts=PTS-STARTPTS"
            if start > 0:
                ms = int(start * 1000)
                f += f",adelay={ms}|{ms}"
            f += f",volume={vol}[a{idx}]"
            filters.append(f)
            labels.append(f"[a{idx}]")
            idx += 1

        for s, dur, start, voice in timeline:
            if voice:
                add_audio(voice, start, float(s.get("voice_volume", 1.0)))
            if s.get("sfx"):
                sfx = base / s["sfx"]
                if not sfx.exists():
                    sys.exit(f"SFX tidak ada: {sfx}")
                add_audio(sfx, start + float(s.get("sfx_delay", 0.0)), float(s.get("sfx_volume", 0.8)))
        if ep.get("bgm"):
            bgm = base / ep["bgm"]
            if not bgm.exists():
                sys.exit(f"BGM tidak ada: {bgm}")
            add_audio(bgm, 0, float(ep.get("bgm_volume", 0.12)), trim=total, loop=True)

        final_cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(silent)] + inputs
        vf = f"subtitles='{ass.as_posix().replace(':', chr(92) + ':')}'"
        if labels:
            mix = "".join(labels) + f"amix=inputs={len(labels)}:duration=longest:normalize=0,alimiter=limit=0.95[aout]"
            final_cmd += ["-filter_complex", ";".join(filters + [mix, f"[0:v]{vf}[vout]"]),
                          "-map", "[vout]", "-map", "[aout]", "-c:a", "aac", "-b:a", "160k"]
        else:
            final_cmd += ["-vf", vf, "-an"]
        final_cmd += ["-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                      "-movflags", "+faststart", "-t", f"{total:.2f}", str(out)]
        run(final_cmd)

    print(f"Selesai -> {out}")


if __name__ == "__main__":
    main()
