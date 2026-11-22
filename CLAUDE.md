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
- Keep text inside the social safe zone: x 120–888, y 288–1248 (x ≤ 780 below y 840).
- When a music track is supplied, run `npx hyperframes beats` and put cuts and text hits on beats.
- Run `npm run check` and look at `npx hyperframes snapshot` frames before rendering.
