import turtle               # allows us to use the turtles library

window = turtle.Screen()        # creates a graphics window

daisy = turtle.Turtle()
daisy.left(180)
daisy.forward(150)
daisy.left(90)
daisy.forward(150)
daisy.left(90)
daisy.forward(100)
daisy.right(180)
daisy.forward(100)
daisy.left(90)
daisy.forward(150)
daisy.left(90)
daisy.forward(150)

daisy.penup()
daisy.forward(100)
daisy.left(90)
daisy.forward(300)
daisy.left(180)
daisy.pendown()
daisy.forward(300)
daisy.left(90)
daisy.forward(150)

daisy.penup()
daisy.forward(100)
daisy.left(90)
daisy.forward(300)
daisy.left(180)
daisy.pendown()
daisy.forward(300)
daisy.left(90)
daisy.forward(150)

window.exitonclick()
