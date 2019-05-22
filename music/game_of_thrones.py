"""For a detailed guide on all the features of the Circuit Playground Express (cpx) library:
https://adafru.it/cp-made-easy-on-cpx"""
import time
import math
import random
import microcontroller
from adafruit_circuitplayground.express import cpx

# Set this as a float from 0 to 1 to change the brightness. The decimal represents a percentage.
# So, 0.3 means 30% brightness!
cpx.pixels.brightness = 0.01


color_index = 0
pixel_number = 0


g3 = 196
c3 = 130.81
eb3 = 155.56
f3 = 174.61
d3 = 146.83
bb3 = 116.54

c4 = 261.63
d4 = 293.66
f4 = 349.23
e4 = 329.63
g4 = 392

a4 = 440
g4 = 392
bb4 = 466.16
b4 = 493.88
c5 = 523.25
d5 = 587.33
e5 = 659.25


def raise_octave(pitch):
    half_step = math.pow(2, 1/12)
    tmp = pitch
    for step in range(12):
        tmp = tmp * half_step
    return tmp


def game_of_thrones():
    # length of a beat
    beat = .1
    # Frequency of Pitch / # of beats to play pitch
    phrase1 = [
        (g3, 3), (c3, 3),
        (eb3, 0.5), (f3, 0.5), (g3, 2),
        (c3, 2), (eb3, .5), (f3, .5), (d3, 12)
    ]
    phrase2 = [
        (f3, 3), (bb3, 3),
        (eb3, .5), (d3, .5), (f3, 2), (bb3, 3),
        (eb3, .5), (d3, .5), (c3, 11)
    ]
    notes = []
    notes.extend(phrase1)
    notes.extend(phrase2)
    tmp = [(raise_octave(p), l) for p, l in notes]
    notes.extend(tmp)
    notes.append((25000, 12))

    for n in notes:
        if not cpx.switch and not cpx.button_a:
            break
        cpx.start_tone(n[0])
        time.sleep(beat * n[1])
        cpx.stop_tone()


while True:

    # If the switch is to the left, it returns True!
    cpx.red_le = cpx.switch
    # play_wavs()
    # piano()

    game_of_thrones()
