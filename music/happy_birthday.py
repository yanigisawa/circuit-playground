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

# Changes to NeoPixel state will not happen without explicitly calling show()
cpx.pixels.auto_write = False

color_index = 0
pixel_number = 0


# time.monotonic() allows for non-blocking LED animations!
start = time.monotonic()

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

def random_color():
    rgb = []
    for c in range(3):
        rgb.append(random.randint(50, 255))
    return tuple(rgb)

def birthday_lights(clear=False):
    if clear:
        cpx.pixels.fill((0, 0, 0))
    pixel = random.randint(0, 9)
    cpx.pixels[pixel] = random_color()
    cpx.pixels.show()

offset = 3
def wheel_lights():
    global offset
    # ROYGBIV
    roygbiv = [
        (209, 0, 0),
        (255, 102, 34),
        (255, 218, 33),
        (51, 221, 0),
        (17, 221, 204),
        (34, 0, 102),
        (51, 0, 68)
    ]
    cpx.pixels[offset - 3] = (0, 0, 0)
    cpx.pixels[offset - 2] = (0, 0, 0)
    cpx.pixels[offset - 1] = (0, 0, 0)
    for i, c in enumerate(roygbiv):
        cpx.pixels[(offset + i) % 10] = c
    offset = (offset + 1) % 10
    cpx.pixels.show()


def alt_birthday_lights(note_length):
    cpx.pixels.fill((0, 0, 0))
    if note_length > 2:
        wheel_lights()
        return
    pixel = random.randint(0, 9)
    one = random_color()
    two = random_color()
    for i in range(5):
        cpx.pixels[i] = one
    for i in range(5, 10):
        cpx.pixels[i] = two
    cpx.pixels.show()

def happy_birthday():
    notes = [
        (c4, .75), (c4, .25),
        (d4, 1), (c4, 1), (f4, 1), (e4, 2),
        (c4, .75), (c4, .25),
        (d4, 1), (c4, 1), (g4, 1), (f4, 2),
        (c4, .75), (c4, .25),
        (c5, 1), (a4, 1), (f4, 1), (e4, 1),
        (d4, 1), (bb4, .75), (bb4, .25),
        (a4, 1), (f4, 1), (g4, 1), (f4, 2)
        ,
        (25000, 8)
    ]
    beat = 0.4
    for i, n in enumerate(notes):
        if not cpx.switch and not cpx.button_b:
            break
        begin = time.monotonic()
        cpx.start_tone(n[0])
        birthday_lights(clear=True)
        if n[1] >= 1:
            while time.monotonic() < begin + beat * n[1]:
                # alt_birthday_lights(n[1])
                wheel_lights()
        else:
            time.sleep(beat * n[1])
        cpx.stop_tone()


while True:

    # If the switch is to the left, it returns True!
    cpx.red_led = cpx.switch
    # play_wavs()
    # piano()

    happy_birthday()
    cpx.pixels.fill((0, 0, 0))
    cpx.pixels.show()
    # game_of_thrones()
