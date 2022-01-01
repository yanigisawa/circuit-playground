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

BPM =  204.0
HALF_NOTE = 60.0 / BPM
QUARTER_NOTE = 0.5 * HALF_NOTE
WHOLE_NOTE = 2.0 * HALF_NOTE

DOTTED_HALF_NOTE = 1.5 * HALF_NOTE


color_index = 0
pixel_number = 0


Bb3 = 116.54
C3 = 130.81
D3 = 146.83
Eb3 = 155.56
F3 = 174.61
G3 = 196

C4 = 261.63
D4 = 293.66
F4 = 349.23
E4 = 329.63
Eb4 = 311.13
G4 = 392
A4 = 440
Bb4 = 466.16
B4 = 493.88

C5 = 523.25
D5 = 587.33
E5 = 659.25


def raise_octave(pitch):
    half_step = math.pow(2, 1/12)
    tmp = pitch
    for step in range(12):
        tmp = tmp * half_step
    return tmp


def mister_sandman_soprano_1():
    # length of a beat
    # Frequency of Pitch / # of beats to play pitch
    phrase1 = [
        (-1, QUARTER_NOTE),
        (D4, QUARTER_NOTE),
        (F4, QUARTER_NOTE),
        (A4, QUARTER_NOTE),

        (G4, QUARTER_NOTE),
        (F4, QUARTER_NOTE),
        (D4, QUARTER_NOTE),
        (Bb3, QUARTER_NOTE),

        (C4, QUARTER_NOTE),
        (Eb4, QUARTER_NOTE),
        (G4, QUARTER_NOTE),
        (Bb4, QUARTER_NOTE),

        (A4, WHOLE_NOTE),

        (-1, QUARTER_NOTE),
        (D4, QUARTER_NOTE),
        (F4, QUARTER_NOTE),
        (A4, QUARTER_NOTE),

        (G4, QUARTER_NOTE),
        (F4, QUARTER_NOTE),
        (D4, QUARTER_NOTE),
        (Bb3, QUARTER_NOTE),

        (C4, QUARTER_NOTE),
        (Eb4, QUARTER_NOTE),
        (G4, QUARTER_NOTE),
        (Bb4, QUARTER_NOTE),

        (A4, QUARTER_NOTE),
        (-1, QUARTER_NOTE),
        (F4, QUARTER_NOTE),
        (G4, QUARTER_NOTE),

        (A4, QUARTER_NOTE),
        (G4, DOTTED_HALF_NOTE + HALF_NOTE),
        (-1, QUARTER_NOTE),
        (-1, QUARTER_NOTE),


    ]
    # phrase2 = [
    #     (F3, 3), (Bb3, 3),
    #     (Eb3, .5), (D3, .5), (F3, 2), (Bb3, 3),
    #     (Eb3, .5), (D3, .5), (C3, 11)
    # ]
    notes = []
    notes.extend(phrase1)
    # notes.extend(phrase2)
    # tmp = [(raise_octave(p), l) for p, l in notes]
    # notes.extend(tmp)
    # notes.append((25000, 12))

    for n in notes:
        if not cpx.switch and not cpx.button_a:
            break
        if n[0] > -1:
            cpx.start_tone(n[0])
        time.sleep(n[1])
        cpx.stop_tone()


while True:

    # If the switch is to the left, it returns True!
    cpx.red_le = cpx.switch
    # play_wavs()
    # piano()
    # if cpx.switch:
    #     cpx.play_file("rasp.wav")

    mister_sandman_soprano_1()
