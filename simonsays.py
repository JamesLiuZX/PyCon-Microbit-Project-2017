from microbit import *
from random import randint

arr = []

def read():
    if pin0.read_digital()==1:
        return 0
    elif pin12.read_digital()==1:
        return 1
    elif pin16.read_digital()==1:
        return 2
    else:
        return 3
        
def show(x):
    if x == 0:
        pin1.write_digital(1)
    elif x == 1:
        pin8.write_digital(1)
    elif x == 2:
        pin2.write_digital(1)
    sleep(500)
    pin1.write_digital(0)
    pin8.write_digital(0)
    pin2.write_digital(0)
    sleep(500)

failed = False        
while not failed:
    arr.append(randint(0,2))
    for i in arr:
        show(i)
    for i in arr:
        cin = 3
        while cin== 3:
            cin = read()
            show(cin)
            sleep(100)
        if cin != i:
            failed = True
            pin3.write_analog(500)
            display.show(str(len(arr)))
            break
    sleep(2000)
