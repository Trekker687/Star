import turtle 

turtle.Screen().bgcolor("white")
pen = turtle.Turtle()
pen.color("blue")

pen.forward(100)

for i in range(2):
    pen.left(120)
    pen.forward(100)

pen.penup()
pen.right(150)
pen.forward(50)

pen.pendown()
pen.right(90)
pen.forward(100)

for i in range(2):
    pen.right(120)
    pen.forward(100)


turtle.done()