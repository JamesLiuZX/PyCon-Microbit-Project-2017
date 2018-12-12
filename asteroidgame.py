from microbit import *
import random

display.show("A")
while True:
    if button_a.is_pressed():
        grid = [["0","0","0","0","0"] for i in range(4)]
        play = 2
        while True:
            if button_b.is_pressed():
                display.show("E")
                break
            if grid[3][play]=="4":
                display.show("O")
                break
            en = random.randint(0,4)
            grid[3] = grid[2]
            grid[2] = grid[1]
            grid[1] = grid[0]
            grid[0] = ["0","0","0","0","0"]
            if random.randint(0,3) != 0:
                grid[0][en] = "4"
            read = accelerometer.get_x()
            if read > 200 and play <=4:
                play += 1
            elif read < -200 and play >0:
                play -= 1
            image = ""
            for i in range(4):
                image += ''.join(grid[i]) + ":"
            player = ["0","0","0","0","0"]
            player[play] = "9"
            image += ''.join(player)
            img = Image(image)
            display.show(img)
            sleep(700)
