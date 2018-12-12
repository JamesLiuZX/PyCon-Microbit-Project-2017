# Author: Tang Yew Seng
# School: Dunman High School
# Email: tang.yewseng@dhs.sg

from microbit import *
import radio

total = 0
scorex = 0
scorey = 0
scorez = 0

radio.on()

while running_time() < 5000:
    display.show(Image.ALL_CLOCKS)
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()
    incoming = radio.receive()
    if incoming == 'reset':
        reset()

while running_time() > 5000 and running_time() < 15000:
    newx = accelerometer.get_x()
    newy = accelerometer.get_y()
    newz = accelerometer.get_z()
    display.clear()
    if newx > x + 40 or newx < x - 40:
        scorex += 1
        display.show("X")
    if newy > y + 40 or newy < y - 40:
        scorey += 1
        display.show("Y")
    if newz > z + 40 or newz < z - 40:
        scorez += 1
        display.show("Z")
    else:
        display.clear
    total = scorex + scorey + scorez
    incoming = radio.receive()
    if incoming == 'reset':
        reset()
display.scroll(str(total), loop=False)

while running_time() > 15000:
    if button_a.was_pressed():
        display.show(str(total))
    incoming = radio.receive()
    if incoming == 'reset':
        reset()
