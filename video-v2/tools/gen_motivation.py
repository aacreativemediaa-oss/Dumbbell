"""Motivational music bed (100 BPM, I-V-vi-IV) + SFX for video-v2.

Reuses the synth helpers in gen_audio.py. Everything is procedurally generated,
so there is nothing to license.
Usage: python3 -I tools/gen_motivation.py assets/sfx
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import numpy as np  # noqa: E402
import gen_audio as g  # noqa: E402

SR = g.SR
BPM = 100
BEAT = 60 / BPM          # 0.6 s
BAR = 4 * BEAT           # 2.4 s
DUR = 31.8
DROP = 3.6               # hook ends, full beat kicks in


def snare():
    n = g.noise(0.35)
    body = np.sin(2 * np.pi * 190 * g.t_(0.35)) * np.exp(-g.t_(0.35) * 25)
    x = g.highpass(n, 1500) * g.env(len(n), 0.001, 0.18, 5) + 0.6 * body
    # cheap room: a few decaying echoes
    out = x.copy()
    for k, d in enumerate((0.031, 0.047, 0.071, 0.093)):
        i = int(d * SR)
        out[i:] += x[:-i] * (0.35 / (k + 1))
    return out


def tom(f):
    t = g.t_(0.4)
    ff = f * (1 + 0.6 * np.exp(-t * 20))
    return np.sin(2 * np.pi * np.cumsum(ff) / SR) * np.exp(-t * 8)


def power(f, d):
    # distorted saw stack (root + fifth + octave)
    x = sum(g.saw(f * r, d) + g.saw(f * r * 1.004, d) for r in (1, 1.5, 2))
    x = np.tanh(x * 1.8)
    x = g.lowpass(x, 3200)
    return x * g.env(len(x), 0.003, d, 2.2) * 0.22


def string_pad(notes, d):
    x = sum(g.lowpass(g.saw(g.mtof(m) * r, d), 1800) for m in notes for r in (0.996, 1.004))
    t = g.t_(d)
    e = np.minimum(1, t / 0.4) * np.minimum(1, (d - t) / 0.4)
    return x * e * 0.05


def music():
    n = int(DUR * SR)
    L = np.zeros(n)
    K, S, H = g.kick(), snare(), g.hat()
    # I - V - vi - IV in C
    prog = [(36, [60, 64, 67]), (43, [59, 62, 67]), (45, [60, 64, 69]), (41, [60, 65, 69])]
    t = 0.0
    bar = 0
    while t < DUR:
        root, chord = prog[bar % 4]
        in_hook = t < DROP
        for b in range(4):
            tb = t + b * BEAT
            if tb >= DUR:
                break
            if in_hook:
                # build: toms on 8ths getting busier, kick on 1
                if b == 0:
                    g.place(L, K, tb, 0.8)
                g.place(L, tom(110 - 10 * b), tb, 0.5)
                g.place(L, tom(140 - 10 * b), tb + BEAT / 2, 0.4)
            else:
                g.place(L, K, tb, 1.0)                       # four on the floor
                if b in (1, 3):
                    g.place(L, S, tb, 0.7)
                for k in range(4):                           # 16th hats
                    g.place(L, H, tb + k * BEAT / 4, 0.35 if k % 2 else 0.18)
            # pulsing 8th bass
            for k in range(2):
                gain = 0.35 if in_hook else 0.6
                g.place(L, g.note(g.mtof(root - 12), BEAT / 2 * 0.85, "bass"), tb + k * BEAT / 2, gain)
            # power-chord stabs on 8ths after the drop
            if not in_hook:
                for k in range(2):
                    g.place(L, power(g.mtof(root + 12), BEAT / 2 * 0.8), tb + k * BEAT / 2, 0.8)
        # strings + lead arp
        g.place(L, string_pad(chord, BAR), t, 1.0 if not in_hook else 0.6)
        if not in_hook:
            arp = chord + [chord[0] + 12]
            for k in range(8):
                g.place(L, g.note(g.mtof(arp[k % 4] + 12), 0.22, "pluck"), t + k * BEAT / 2, 0.5)
        t += BAR
        bar += 1
    # snare roll into the drop
    for k in range(8):
        g.place(L, S, DROP - BEAT * 2 + k * BEAT / 4, 0.2 + 0.08 * k)
    g.place(L, g.boom(), DROP, 0.9)
    tt = np.arange(n) / SR
    duck = 1 - 0.3 * np.exp(-((tt % BEAT)) * 12) * (tt >= DROP)
    L *= duck
    L *= np.clip((DUR - tt) / 1.6, 0, 1)
    R = np.roll(L, int(0.012 * SR)) * 0.9 + L * 0.1
    return np.stack([L, R], axis=1)


def main(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    g.write(out / "music.wav", music())
    g.write(out / "whoosh.wav", g.whoosh())
    g.write(out / "swoosh.wav", g.swoosh_up())
    g.write(out / "pop.wav", g.pop())
    g.write(out / "boom.wav", g.boom())
    g.write(out / "ding.wav", g.ding())
    g.write(out / "riser.wav", g.riser())
    g.write(out / "click.wav", g.click())


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "assets/sfx")
