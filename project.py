import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().setup(300.400)
square=turtle.Turtle()
side=4
angle=360/side
for i in range(side):
    square.forward(70)
    square.right(angle)
turtle.done()