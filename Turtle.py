""" Create a Turtle, name it, make it BLUE and draw a Smiley Face"""

import turtle
p = turtle.Turtle()
p.color("Blue")
p.right(90)
p.fd(50)
p.pu()
p.goto(25,0)
p.pd()
p.fd(50)
p.pu()
p.goto(-25,-50)
p.pd()
for i in range(20):
    p.fd(6)
    p.left(10)
