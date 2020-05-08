import turtle
import numpy as np

running = True

class Harmonic:
    def __init__(self, x, y, mag, change):
        self.x = x
        self.y = y
        self.change = change
        self.angle = -1
        self.mag = mag
        self.t = turtle.Turtle()
        self.t.penup()
        self.t.goto(x,y)
        self.t.shape("square")
        self.t.speed(1)
        self.t.setheading(270)

    def move(self):
        k = np.sin(self.angle) * self.mag
        self.t.forward(k)
        self.angle += self.change

    def stretch(self):
        k = np.cos(self.angle) * self.mag
        self.t.shapesize(1,k, outline=1)
        self.angle += self.change

foo = Harmonic(-50, -50, 5, 0.05)
bar = Harmonic(50, -50, 10, 0.05)

while running:
    foo.move()
    bar.stretch()



