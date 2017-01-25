def ShapeCreator(turName, numSides, sideLength):
    import turtle
    turName = turtle.Turtle()
    turName.color("Lime Green")
    wn = turtle.Screen()
    wn.bgcolor("Black")
    wn.title("Shape Creator!")
    ang = (360/numSides)
    for i in range(numSides):
        turName.fd(sideLength)
        turName.left(ang)
    wn.exitonclick()
