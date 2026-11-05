#!/usr/bin/env python3
"""
Build a practical "Getting Started with ServiceNow SAM" MP4 from the
storyboard in methodology/VIDEO_GUIDE_SAM_GETTING_STARTED.md.

Method: render every storyboard beat to a 1920x1080 PNG with PIL (embedding the
repo's own SVG-derived diagrams), then stitch the PNGs with ffmpeg. No moviepy.

Optional narration: pass --voice to synthesise a track per slide with espeak-ng
and mux it in. Slide duration then follows the audio length.

Usage:
    python3 video/build_sam_video.py                  # silent video
    python3 video/build_sam_video.py --voice          # narrated video
    python3 video/build_sam_video.py --slides-only    # PNGs only
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# --------------------------------------------------------------------------
# Paths
# --------------------------------------------------------------------------
HERE = Path(__file__).resolve().parent
REPO = HERE.parent
ASSETS = HERE / "assets"
OUT = HERE / "out"
MP4 = OUT / "sam_getting_started.mp4"
IMG_DIR = REPO / "images"

# --------------------------------------------------------------------------
# Canvas + palette
# --------------------------------------------------------------------------
W, H = 1920, 1080
MARGIN = 110

BG_TOP = (9, 22, 40)
BG_BOTTOM = (3, 9, 18)
CARD = (17, 38, 62)
ACCENT = (61, 181, 245)      # SAM blue
ACCENT_ALT = (255, 176, 59)  # warning amber
TEXT = (238, 244, 250)
TEXT_MUTED = (146, 170, 190)
RULE = (34, 62, 92)

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
]


def find_font(name: str) -> str:
    for d in FONT_DIRS:
        p = Path(d) / name
        if p.exists():
            return str(p)
    raise SystemExit(f"Font not found: {name} (looked in {FONT_DIRS})")


F_BOLD = find_font("DejaVuSans-Bold.ttf")
F_REG = find_font("DejaVuSans.ttf")
F_MONO = find_font("DejaVuSansMono.ttf")


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


# --------------------------------------------------------------------------
# Storyboard — transcribed from VIDEO_GUIDE_SAM_GETTING_STARTED.md
# --------------------------------------------------------------------------
@dataclass
class Slide:
    heading: str
    narration: str
    eyebrow: str = ""
    timecode: str = ""
    bullets: list[str] = field(default_factory=list)
    caption: str = ""
    image: str = ""       # filename under images/
    kind: str = "content"  # content | title | image | recap


SLIDES: list[Slide] = [
    Slide(
        eyebrow="ServiceNow SAM · Getting Started",
        heading="A licence position you can defend",
        timecode="0:00 – 0:30",
        narration=(
            "Software Asset Management in ServiceNow is not about tracking what "
            "you have. It is about building a licence position you can defend in "
            "an audit. If you are only tracking installs, you are doing asset "
            "management, not SAM. In this video we walk the three hard gates that "
            "make SAM data trustworthy."
        ),
        bullets=[
            "Tracking installs  →  asset register",
            "Rights vs installs  →  SAM",
        ],
        kind="title",
    ),
    Slide(
        eyebrow="Gate check",
        heading="Three hard gates",
        timecode="0:30 – 2:30",
        narration=(
            "SAM has three hard gates. Miss any one and every number you produce "
            "afterwards is fiction, no matter how tidy the configuration looks. "
            "First, SAM schema and entitlement: you need the plugin and the right "
            "entitlement tables. Second, a populated CMDB with identification "
            "rules, because duplicate configuration items mean duplicate installs "
            "and an inflated gap. Third, a real discovery or connector feed. "
            "Hand-typed installs are an asset register, not SAM."
        ),
        caption="Any missing gate → the compliance number is fiction",
        image="sam-readiness-gates.png",
        kind="image",
    ),
    Slide(
        eyebrow="Build order",
        heading="Do not reorder these nine steps",
        timecode="2:30 – 5:00",
        narration=(
            "Do not reorder these steps, each one assumes the previous checkpoint. "
            "Install or confirm the plugin. Run Guided Setup, but read every step "
            "before clicking. Create roles and a dedicated non-human integration "
            "user. Connect one discovery feed with a small scope. Normalise your "
            "top titles against the content library. Load entitlements from "
            "contracts and purchase orders. Define licence metrics per publisher. "
            "Reconcile and explain your exceptions. Then publish dashboards to a "
            "named owner on a cadence."
        ),
        caption="Each step depends on the checkpoint above it",
        image="sam-build-order.png",
        kind="image",
    ),
    Slide(
        eyebrow="The question everyone asks",
        heading="Identification rules are CMDB, not SAM",
        timecode="5:00 – 7:30",
        narration=(
            "The most misattributed control in this track. CI identification rules "
            "live in the CMDB and answer: is this a new configuration item, or the "
            "one I already have? They apply to every CI, and hardware asset "
            "management depends on them directly. SAM has no identification rules "
            "for software titles. Instead you normalise, mapping 'Microsoft Office "
            "2021' and 'MS Office 21' to the same product. But every install record "
            "hangs off a CI, so duplicate CIs duplicate installs. Fix computer-class "
            "identification before you reconcile, or you will spend a week "
            "explaining a shortage that is really a duplicate."
        ),
        bullets=[
            "Deduplicating a machine   →  CMDB / IRE",
            "Deduplicating a title      →  SAM normalisation",
            "Deduplicating rights       →  licence metric (commercial decision)",
        ],
    ),
    Slide(
        eyebrow="Fields",
        heading="Which fields actually decide the answer",
        timecode="7:30 – 10:00",
        narration=(
            "For entitlements the decisive field is the metric: per user, per "
            "device, or per core. That is a commercial decision, not a technical "
            "one. For software installs it is the normalised product. Leave it "
            "empty and your reconciliation report is empty. For assets it is the "
            "model. Get the model wrong and the licence metric will not apply "
            "correctly. Also note there are three kinds of required in ServiceNow: "
            "dictionary mandatory, UI policy mandatory, and data policy mandatory. "
            "Only the dictionary one survives an API call or an import."
        ),
        bullets=[
            "Entitlement  →  product, quantity, metric, start/end, licence type",
            "Install  →  linked CI, normalised product",
            "Asset  →  asset tag, model, state, assigned to",
        ],
    ),
    Slide(
        eyebrow="Reporting",
        heading="Metrics that lie",
        timecode="10:00 – 11:30",
        narration=(
            "Be careful which numbers you publish. Unlicensed installs on their own "
            "is fear, not information, without discovery coverage beside it. Raw "
            "install count is not usage: installed does not mean used. Your best "
            "first key performance indicator is installs without a normalised "
            "product, because it predicts every other number you will report. "
            "Publish discovery coverage percentage next to any licence position."
        ),
        bullets=[
            "Installs without a normalised product  →  use it, best first KPI",
            "Renewals inside 90 days  →  use it, cheapest trust builder",
            "Unlicensed installs alone  →  do not, fear without coverage",
            "Raw install count as usage  →  do not, installed is not used",
        ],
    ),
    Slide(
        eyebrow="Recap",
        heading="Three titles, one defensible number",
        timecode="11:30 – 12:30",
        narration=(
            "You have seen the gates, the build order, and the traps. Now go to the "
            "lab and build a real compliance number for three titles. Then break it "
            "by changing the licence metric and watch the answer flip. That is the "
            "moment SAM stops being data entry and becomes a business conversation."
        ),
        bullets=[
            "Run the readiness probe, then fix CMDB identification",
            "Normalise your top five titles to exactly one product each",
            "Load entitlements that trace to a contract or PO",
            "Complete the SAM baseline lab, then change the metric",
        ],
        kind="recap",
    ),
]


# --------------------------------------------------------------------------
# Rendering helpers
# --------------------------------------------------------------------------
def make_bg() -> Image.Image:
    img = Image.new("RGB", (W, H), BG_TOP)
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        c = tuple(int(BG_TOP[i] + (BG_BOTTOM[i] - BG_TOP[i]) * t) for i in range(3))
        d.line([(0, y), (W, y)], fill=c)
    glow = Image.new("RGB", (W, H), BG_BOTTOM)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([W - 560, -360, W + 300, 420], fill=(14, 62, 108))
    return Image.blend(img, glow, 0.30)


BG_IMG = make_bg()


def wrap(d: ImageDraw.ImageDraw, text: str, fnt, max_w: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if d.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_header(d: ImageDraw.ImageDraw, slide: Slide, size: int = 62) -> int:
    """Draw eyebrow + heading + rule. Returns the y cursor below it."""
    y = MARGIN
    if slide.eyebrow:
        d.text((MARGIN, y), slide.eyebrow.upper(), font=font(F_BOLD, 28),
               fill=ACCENT)
        y += 50
    f_head = font(F_BOLD, size)
    for line in wrap(d, slide.heading, f_head, W - 2 * MARGIN):
        d.text((MARGIN, y), line, font=f_head, fill=TEXT)
        y += int(size * 1.22)
    y += 14
    d.rectangle([MARGIN, y, MARGIN + 120, y + 5], fill=ACCENT)
    return y + 32


def paste_image(img: Image.Image, d: ImageDraw.ImageDraw, name: str,
                top: int, bottom: int) -> None:
    src_path = IMG_DIR / name
    if not src_path.exists():
        raise SystemExit(f"missing diagram: {src_path}")
    art = Image.open(src_path).convert("RGBA")

    avail_w = W - 2 * MARGIN
    avail_h = bottom - top
    scale = min(avail_w / art.width, avail_h / art.height, 1.0)
    nw, nh = max(1, int(art.width * scale)), max(1, int(art.height * scale))
    art = art.resize((nw, nh), Image.LANCZOS)

    x = (W - nw) // 2
    panel = Image.new("RGBA", (nw + 2, nh + 2), (0, 0, 0, 0))
    panel.paste(art, (1, 1), art)
    img.paste(panel, (x, top), panel)
    d.rectangle([x - 1, top - 1, x + nw, top + nh], outline=RULE, width=2)


def render(slide: Slide, idx: int, total: int) -> Image.Image:
    img = BG_IMG.copy()
    d = ImageDraw.Draw(img)

    bar_y = H - 62
    usable_bottom = bar_y - 26

    head_size = 76 if slide.kind == "title" else 60
    y = draw_header(d, slide, head_size)

    if slide.image:
        # Diagram-forward slide: heading, then the picture fills the rest.
        cap_h = 46 if slide.caption else 0
        paste_image(img, d, slide.image, y + 10, usable_bottom - cap_h)
        if slide.caption:
            f_cap = font(F_REG, 26)
            w_txt = d.textlength(slide.caption, font=f_cap)
            d.text(((W - w_txt) // 2, usable_bottom - 34), slide.caption,
                   font=f_cap, fill=TEXT_MUTED)
    else:
        if slide.timecode:
            d.text((MARGIN, y), slide.timecode, font=font(F_MONO, 26),
                   fill=TEXT_MUTED)
            y += 46

        f_body = font(F_REG, 33)
        for line in wrap(d, slide.narration, f_body, W - 2 * MARGIN):
            if y > usable_bottom - 150:
                break
            d.text((MARGIN, y), line, font=f_body, fill=TEXT)
            y += int(f_body.size * 1.40)

        if slide.bullets:
            y += 26
            f_b = font(F_REG, 30)
            for b in slide.bullets:
                if y > usable_bottom - 10:
                    break
                colour = ACCENT_ALT if slide.kind == "recap" else ACCENT
                d.rectangle([MARGIN, y + 11, MARGIN + 9, y + 20], fill=colour)
                for bl in wrap(d, b, f_b, W - 2 * MARGIN - 42):
                    d.text((MARGIN + 34, y), bl, font=f_b, fill=TEXT_MUTED)
                    y += int(f_b.size * 1.32)
                y += 8

    # Progress bar + footer
    d.rectangle([MARGIN, bar_y, W - MARGIN, bar_y + 4], fill=RULE)
    done = (idx + 1) / total
    d.rectangle([MARGIN, bar_y, MARGIN + int((W - 2 * MARGIN) * done), bar_y + 4],
                fill=ACCENT)

    f_foot = font(F_REG, 22)
    d.text((MARGIN, bar_y + 16),
           "ServiceNow SAM · Getting Started · SNRLM Step 1-3",
           font=f_foot, fill=TEXT_MUTED)
    counter = f"{idx + 1} / {total}"
    d.text((W - MARGIN - d.textlength(counter, font=f_foot), bar_y + 16),
           counter, font=f_foot, fill=TEXT_MUTED)
    return img


# --------------------------------------------------------------------------
# Timing + audio
# --------------------------------------------------------------------------
def reading_seconds(slide: Slide, wpm: float = 195.0, floor: float = 6.0,
                    cap: float = 30.0) -> float:
    """Silent-read time for narration + bullets, clamped."""
    words = len(slide.narration.split()) + sum(len(b.split()) for b in slide.bullets)
    return round(min(cap, max(floor, (words / wpm) * 60.0)), 2)


def probe_duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def synth_voice(slide: Slide, dest: Path, wpm: int = 165) -> float:
    """Render narration to a wav with espeak-ng. Returns its duration."""
    text = slide.narration
    if slide.bullets:
        text += ". " + ". ".join(slide.bullets)
    subprocess.run(
        ["espeak-ng", "-v", "en-us", "-s", str(wpm), "-p", "42",
         "-w", str(dest), text],
        check=True)
    return probe_duration(dest)


# --------------------------------------------------------------------------
# Assembly
# --------------------------------------------------------------------------
def build(slides: list[Slide], fps: int, voice: bool, crossfade: float) -> None:
    if not shutil.which("ffmpeg"):
        raise SystemExit("ffmpeg not found on PATH")
    if voice and not shutil.which("espeak-ng"):
        raise SystemExit("--voice requested but espeak-ng is not installed")

    OUT.mkdir(parents=True, exist_ok=True)
    seg_dir = OUT / "segments"
    if seg_dir.exists():
        shutil.rmtree(seg_dir)
    seg_dir.mkdir(parents=True)

    pngs = sorted(ASSETS.glob("slide_*.png"))
    if len(pngs) != len(slides):
        raise SystemExit(f"expected {len(slides)} slides, found {len(pngs)}")

    segs: list[Path] = []
    durs: list[float] = []

    for i, (png, slide) in enumerate(zip(pngs, slides), start=1):
        dur = reading_seconds(slide)
        audio: Path | None = None
        if voice:
            audio = seg_dir / f"vo_{i:02d}.wav"
            dur = max(dur, round(synth_voice(slide, audio) + 0.9, 2))
        durs.append(dur)

        seg = seg_dir / f"seg_{i:02d}.mp4"
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", str(png)]
        if audio:
            cmd += ["-i", str(audio)]
        cmd += [
            "-t", f"{dur}",
            "-vf", f"fps={fps},format=yuv420p",
            "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        ]
        if audio:
            cmd += ["-c:a", "aac", "-b:a", "128k", "-shortest"]
        cmd += ["-movflags", "+faststart", str(seg)]
        subprocess.run(cmd, check=True)
        segs.append(seg)
        print(f"  segment {i:02d}/{len(slides)}  {dur:>6.2f}s  {slide.heading}")

    # Concatenate. Crossfade only makes sense without audio.
    use_fade = crossfade > 0 and not voice and len(segs) > 1
    if use_fade:
        cmd = ["ffmpeg", "-y", "-loglevel", "error"]
        for s in segs:
            cmd += ["-i", str(s)]
        offsets, acc = [], 0.0
        for i, dur in enumerate(durs):
            acc += dur
            if i < len(durs) - 1:
                offsets.append(acc - crossfade * (i + 1))
        chain, prev = "", "0:v"
        for i in range(1, len(segs)):
            lbl = f"v{i}"
            chain += (f"[{prev}][{i}:v]xfade=transition=fade"
                      f":duration={crossfade}:offset={offsets[i-1]:.2f}[{lbl}];")
            prev = lbl
        cmd += ["-filter_complex", chain.rstrip(";"), "-map", f"[{prev}]",
                "-c:v", "libx264", "-preset", "medium", "-crf", "20",
                "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(MP4)]
        subprocess.run(cmd, check=True)
    else:
        lst = OUT / "concat.txt"
        lst.write_text("".join(f"file '{s.resolve()}'\n" for s in segs))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat",
                        "-safe", "0", "-i", str(lst), "-c", "copy",
                        "-movflags", "+faststart", str(MP4)], check=True)

    total = probe_duration(MP4)
    print(f"\n+ wrote {MP4}")
    print(f"  duration {total:.1f}s  ({int(total // 60)}m{int(total % 60):02d}s)"
          f"  size {MP4.stat().st_size / 1e6:.2f} MB  voice={'yes' if voice else 'no'}")


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--slides-only", action="store_true",
                    help="render PNGs only, skip ffmpeg")
    ap.add_argument("--voice", action="store_true",
                    help="synthesise narration with espeak-ng and mux it in")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--crossfade", type=float, default=0.5,
                    help="crossfade seconds between silent slides (0 = hard cut)")
    args = ap.parse_args()

    ASSETS.mkdir(parents=True, exist_ok=True)
    for old in ASSETS.glob("slide_*.png"):
        old.unlink()

    total = len(SLIDES)
    for i, slide in enumerate(SLIDES):
        img = render(slide, i, total)
        p = ASSETS / f"slide_{i+1:02d}.png"
        img.save(p, "PNG")
        print(f"  rendered {p.name}  ({reading_seconds(slide):>6.2f}s)")

    print(f"\n{total} slides -> {ASSETS}")
    if args.slides_only:
        return 0

    build(SLIDES, args.fps, args.voice, args.crossfade)
    return 0


if __name__ == "__main__":
    sys.exit(main())
