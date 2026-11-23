"""Extra SFX for video-v5: wrong buzzer and soft inhale/exhale breaths (procedural, license-free).
Usage: python3 -I tools/gen_sfx_v5.py assets/sfx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np  # noqa: E402
import gen_audio as g  # noqa: E402

SR = g.SR


def wrong():
    out = []
    for f, d in ((330, 0.14), (220, 0.26)):
        t = g.t_(d)
        x = np.sign(np.sin(2 * np.pi * f * t)) * 0.5 + np.sin(2 * np.pi * f * 2 * t) * 0.2
        x = g.lowpass(x, 2200) * np.minimum(1, t / 0.005) * np.minimum(1, (d - t) / 0.03)
        out.append(x)
        out.append(np.zeros(int(0.03 * SR)))
    return np.concatenate(out)


def breath(d=0.9, inhale=True):
    t = g.t_(d)
    shape = np.sin(np.pi * t / d) ** 1.5
    cutoff = (900 + 2200 * (t / d)) if inhale else (3100 - 2200 * (t / d))
    x = g.lowpass(g.noise(d), cutoff) - g.lowpass(g.noise(d), 250) * 0.5
    return x * shape


out = Path(sys.argv[1] if len(sys.argv) > 1 else "assets/sfx")
g.write(out / "wrong.wav", wrong())
g.write(out / "inhale.wav", breath(0.9, True))
g.write(out / "exhale.wav", breath(0.8, False))
