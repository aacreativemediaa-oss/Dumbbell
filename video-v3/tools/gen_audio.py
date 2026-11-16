"""Procedurally generate the music bed and sound effects for the edit.

Everything is synthesised with numpy, so there are no licensing issues.
Usage: python3 -I tools/gen_audio.py assets/sfx
"""
import sys
import wave
from pathlib import Path

import numpy as np
from scipy.signal import lfilter

SR = 48000
BPM = 120
BEAT = 60 / BPM
DUR = 30.5
rng = np.random.default_rng(7)  # deterministic


def write(path, x):
    x = np.asarray(x, dtype=np.float64)
    if x.ndim == 1:
        x = np.stack([x, x], axis=1)
    peak = np.max(np.abs(x)) or 1.0
    x = x / peak * 0.89
    data = (x * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data.tobytes())


def t_(d):
    return np.arange(int(d * SR)) / SR


def env(n, a=0.002, d=0.2, curve=4.0):
    t = np.arange(n) / SR
    att = np.clip(t / max(a, 1e-6), 0, 1)
    dec = np.exp(-np.maximum(t - a, 0) * curve / max(d, 1e-6))
    return att * dec


def lowpass(x, cutoff):
    # one-pole lowpass; cutoff may be a scalar or a per-sample array
    if np.isscalar(cutoff):
        a = 1 - np.exp(-2 * np.pi * cutoff / SR)
        return lfilter([a], [1, -(1 - a)], x)
    cutoff = np.broadcast_to(cutoff, x.shape)
    a = 1 - np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc += a[i] * (x[i] - acc)
        y[i] = acc
    return y


def highpass(x, cutoff):
    return x - lowpass(x, cutoff)


def noise(d):
    return rng.uniform(-1, 1, int(d * SR))


# ---------------------------------------------------------------- drums
def kick():
    t = t_(0.45)
    f = 45 + 110 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 7) + 0.3 * np.sin(ph * 2) * np.exp(-t * 30)


def clap():
    n = noise(0.25)
    e = np.zeros_like(n)
    for off in (0, 0.012, 0.024):
        i = int(off * SR)
        e[i:] += env(len(n) - i, 0.001, 0.08, 6)
    return highpass(n * e, 900) * 0.8


def hat(open_=False):
    d = 0.18 if open_ else 0.05
    n = noise(d)
    return highpass(n, 7000) * env(len(n), 0.001, d, 5) * 0.35


# ---------------------------------------------------------------- tonal
def saw(f, d):
    t = t_(d)
    return 2 * ((t * f) % 1.0) - 1


def note(f, d, kind="bass"):
    if kind == "bass":
        x = 0.7 * np.sin(2 * np.pi * f * t_(d)) + 0.35 * lowpass(saw(f, d), 500)
        return x * env(len(x), 0.004, d * 0.9, 3)
    if kind == "pluck":
        x = lowpass(saw(f, d) + saw(f * 1.006, d), 2600)
        return x * env(len(x), 0.002, 0.18, 5) * 0.35
    if kind == "pad":
        x = sum(lowpass(saw(f * r, d), 1200) for r in (0.995, 1.0, 1.005))
        e = np.minimum(1, t_(d) / 0.2) * np.minimum(1, (d - t_(d)) / 0.3)
        return x * e * 0.08
    raise ValueError(kind)


def mtof(m):
    return 440 * 2 ** ((m - 69) / 12)


def place(buf, x, at, gain=1.0):
    i = int(at * SR)
    j = min(len(buf), i + len(x))
    if i < len(buf):
        buf[i:j] += x[: j - i] * gain


def music():
    n = int(DUR * SR)
    L = np.zeros(n)
    K, C, H, OH = kick(), clap(), hat(), hat(True)
    # chord progression (A minor-ish, upbeat): Am F C G — one bar each
    prog = [(57, [69, 72, 76]), (53, [65, 69, 72]), (48, [64, 67, 72]), (55, [67, 71, 74])]
    bars = int(DUR / (4 * BEAT)) + 1
    for b in range(bars):
        t0 = b * 4 * BEAT
        root, chord = prog[b % 4]
        hook_section = t0 < 4.0  # first 2 bars: lighter, then drop
        for k in range(4):
            tb = t0 + k * BEAT
            if not hook_section or k in (0, 2):
                place(L, K, tb, 0.95)
            if k in (1, 3):
                place(L, C, tb, 0.55 if not hook_section else 0.35)
            place(L, H, tb + BEAT / 2, 0.6)
            if not hook_section:
                place(L, H, tb + BEAT / 4, 0.25)
                place(L, H, tb + 3 * BEAT / 4, 0.25)
        if not hook_section:
            place(L, OH, t0 + 3.5 * BEAT, 0.5)
        # bass: offbeat eighths
        for k in range(8):
            if k % 2 == 1 or not hook_section:
                place(L, note(mtof(root - 12), BEAT / 2 * 0.9, "bass"), t0 + k * BEAT / 2, 0.55)
        # pad
        for m in chord:
            place(L, note(mtof(m), 4 * BEAT, "pad"), t0, 1.0)
        # pluck arpeggio
        if not hook_section:
            arp = chord + [chord[1] + 12]
            for k in range(8):
                place(L, note(mtof(arp[k % 4] + 12), 0.25, "pluck"), t0 + k * BEAT / 2, 0.45)
    # simple sidechain feel: duck on each beat
    t = np.arange(n) / SR
    duck = 1 - 0.35 * np.exp(-((t % BEAT)) * 14)
    L *= duck
    # fade out last 1.5 s
    L *= np.clip((DUR - t) / 1.5, 0, 1)
    # tiny stereo width via delay on right
    R = np.roll(L, int(0.011 * SR)) * 0.92 + L * 0.08
    return np.stack([L, R], axis=1)


# ---------------------------------------------------------------- sfx
def whoosh(d=0.45, rev=False):
    n = noise(d)
    t = t_(d)
    sweep = 400 + 6000 * np.sin(np.pi * t / d) ** 2
    x = lowpass(n, sweep) * np.sin(np.pi * t / d) ** 2
    return x[::-1] if rev else x


def pop():
    t = t_(0.12)
    f = 900 * np.exp(-t * 18) + 300
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), 0.001, 0.08, 5)


def boom():
    t = t_(1.4)
    f = 32 + 90 * np.exp(-t * 9)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.4)
    crack = lowpass(noise(1.4), 2500) * np.exp(-t * 14) * 0.8
    return sub + crack


def ding():
    t = t_(1.2)
    x = sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t * k) for f, a, k in
            [(1568, 1.0, 3.5), (2093, 0.6, 4.5), (3136, 0.35, 6), (4186, 0.2, 8)])
    return x * np.minimum(1, t / 0.002)


def riser(d=1.2):
    t = t_(d)
    n = lowpass(noise(d), 300 + 8000 * (t / d) ** 2)
    tone = np.sin(2 * np.pi * np.cumsum(200 + 900 * (t / d) ** 2) / SR) * 0.25
    return (n + tone) * (t / d) ** 2


def click():
    t = t_(0.03)
    return np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 200)


def swoosh_up():
    return whoosh(0.3)


def main(out):
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    write(out / "music.wav", music())
    write(out / "whoosh.wav", whoosh())
    write(out / "swoosh.wav", swoosh_up())
    write(out / "pop.wav", pop())
    write(out / "boom.wav", boom())
    write(out / "ding.wav", ding())
    write(out / "riser.wav", riser())
    write(out / "click.wav", click())


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "assets/sfx")
