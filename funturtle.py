import turtle # python needs this to use all the turtle functions
turtle.shape('turtle') # changes the shape to a turtle
finn = turtle.clone() # creates new turtle and saves it in finn
finn.goto(100,0)
finn.goto(100,100)
finn.goto(0,100)
finn.goto(0,0)

charlie= finn.clone()
charlie.shape("triangle")
charlie.penup()
charlie.goto(-50,0)
charlie.pendown()
charlie.goto(-100,0)
charlie.left(90)
charlie.goto(-100,100)
charlie.right(30)
charlie.goto(-50,0)
charlie.penup
charlie.goto(200,0)
charlie.pendown()
charlie.stamp()
charlie.goto(200,100)

turtle.mainloop()
