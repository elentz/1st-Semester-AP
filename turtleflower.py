import turtle               # allows us to use the turtles library

window = turtle.Screen()        # creates a graphics window

daisy = turtle.Turtle()
for i in range(12):
    for i in range(4):
        daisy.forward(75)
        daisy.left(90)
    daisy.penup
    daisy.left(30)
    daisy.forward(25)
    daisy.pendown


window.exitonclick()
