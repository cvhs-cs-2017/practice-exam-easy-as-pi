"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""

import turtle
Pro = turtle.Turtle()
for i in range(100):
    Pro.fd(5)
    Pro.left(3.6)
