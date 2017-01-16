import turtle
import time
import os
while True:
    yep = input('What should I draw? A square, a circle or a triangle. ')
    t = turtle.Pen()
    if yep == 'square':
        for x in range(0, 4):
            t.fd(50)
            t.rt(90)
        t.ht()
        time.sleep(10)
        exit()
    elif yep == 'circle':
        for x in range(0, 360):
            t.fd(1)
            t.rt(1)
        t.ht()
        time.sleep(10)
        exit()
    elif yep == 'triangle':
        t.rt(270)
        for x in range(0, 3):
            t.fd(90)
            t.rt(120)
        t.ht()
        time.sleep(10)
        exit()
    else:
        print('''I didn't understand what you said.''')