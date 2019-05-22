# CircuitPlaygroundExpress_DigitalIO

import time

import board
from touchio import TouchIn
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

button = DigitalInOut(board.BUTTON_A)
button.direction = Direction.INPUT
button.pull = Pull.DOWN

touch1 = TouchIn(board.A4)
# touch1.direction = Direction.INPUT
touch2 = DigitalInOut(board.A1)
touch2.direction = Direction.OUTPUT

print(dir(board))

while True:

    touch2.value = not touch1.value

    if button.value:  # button is pushed
        print('begin button press')
        led.value = True
        # touch2.value = False
    else:
        led.value = False
        # touch2.value = True


    if touch1.value:
        led.value = True
    time.sleep(0.01)
