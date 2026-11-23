# Dumbbell video edits (HyperFrames)

Each edit lives in its own HyperFrames project folder (`video/`, `video-v2/`, `video-v3/`, …).
Start new edits as a new folder; do not overwrite earlier versions.

## Typography (mandatory for all new edits, from 2026-11-22)

Canvas is 1080×1920. Use exactly these font sizes:

| Text role | Size |
|---|---|
| Headline (hook, section titles, CTA main line) | **100px** |
| Sub-headline / "save" sticker | **47px** |
| Caption (body lines, checklist items, reps) | **40px** |
| Heart-rate number | **64px** |
| Chip, colour name, zone label (small tags, weight labels, counters) | **19px** |

Previous sizes, now retired: headline 150, sub-headline 70, caption 60, heart-rate 96, chip 28.
`video/`, `video-v2/` and `video-v3/` were made before this rule and still use the old sizes.

## Workflow notes

- The Drive folder lists more than one page of files: always paginate (`nextPageToken`) before
  deciding what footage exists.
- Footage so far has no speech; still transcribe (Whisper large-v3, `language="ms"`, VAD) and report it.
- Cut clips from the original 4K files, at the frame rate the brief asks for (v3: 1080×1920 @ 60fps).
- **Output format is SDR 1080×1920 @ 60fps, BT.709.** The iPhone `IMG_*.MOV` files are HDR
  (HLG / Dolby Vision, BT.2020, 10-bit). Always tone-map them when cutting, and tag BT.709:
  `zscale=tin=arib-std-b67:min=bt2020nc:pin=bt2020:t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p`
  plus `-color_primaries bt709 -color_trc bt709 -colorspace bt709`. Render with
  `hyperframes render --sdr --video-frame-format png`; never let HDR auto-promotion happen
  (it makes the video look washed-out and too bright on phones). The `lv_0_*` files are already SDR.
- Hooks: no shot shorter than ~1.5 s; prefer one continuous shot under the hook text.
- Keep text inside the social safe zone: x 120–888, y 288–1248 (x ≤ 780 below y 840).
- When a music track is supplied, run `npx hyperframes beats` and put cuts and text hits on beats.
- Run `npm run check` and look at `npx hyperframes snapshot` frames before rendering.
