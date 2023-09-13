# Paul Math 5e p. 83 ex. 7 Draw triangle
# Cahier de cmpetances birder editeur
# Ex. 4 Construire un trianble isocel en O
# OR = 4.2 cm, <ROI = 42°
import turtle
t = turtle.Pen()
t.pencolor('blue')
t.width(1)

t.forward(-420)
t.right(42)
t.forward(420)
t.goto(0, 0)

# La base horisontale
t.setheading(0)
t.left(69)
t.forward(420)
t.right(180 - 42)
t.forward(420)
t.goto(0, 0)
turtle.done()
turtle.bye()
