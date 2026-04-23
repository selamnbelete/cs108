from lab3.Sound_base import *

freq = 440
dur  = 1.5
t    = timeline(dur)

Sine_Wave     = 0.3 * np.sin(2 * np.pi * freq * t)
square_wave   = 0.3 * np.sign(np.sin(2 * np.pi * freq * t))
sawtooth_wave = 0.3 * (2 * (t * freq % 1) - 1)
triangle_wave = 0.3 * (2 * np.abs(2 * (t * freq % 1) - 1) - 1)

for wave, name in [
    (Sine_Wave,     "sine"),
    (square_wave,   "square"),
    (sawtooth_wave, "sawtooth"),
    (triangle_wave, "triangle"),
]:
    show(wave, name)
    play(wave)
