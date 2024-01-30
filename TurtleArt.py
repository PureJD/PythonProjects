import turtle as t
from random import random

for i in range(10000):
    t.bgcolor('black')
    t.width(10)
    t.color('cyan')
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps) 
    t.speed(1000)

    for i in range(1):
        t.bgcolor('black')
        t.width(10)
        t.color('red')
        steps = int(random() * 100)
        angle = int(random() * 360)
        t.right(angle)
        t.fd(steps)

        for i in range(1):
            t.bgcolor('black')
            t.width(10)
            t.color('green')
            steps = int(random() * 100)
            angle = int(random() * 360)
            t.right(angle)
            t.fd(steps)