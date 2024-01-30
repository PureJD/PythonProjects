import turtle

s = turtle.Screen()
turtle.bgcolor('gray')
t = turtle.Turtle()

# Define a function to draw a figure
def drawDavid(t):
    # Move the turtle to an initial angle
    t.left(120)

    # Draw the first set of three lines in the shape of a triangle
    for i in range(0, 3):
       
        t.forward(100)  # Move the turtle forward by 100 units
        t.right(120)    # Turn the turtle right by 120 degrees

    # Lift the pen (stop drawing)
    t.penup()

    # Move the turtle to a new position
    t.goto(-50, 30)

    # Put the pen down (start drawing again)
    t.pendown()

    # Rotate the turtle to a new angle
    t.right(120)

    # Draw the second set of three lines in the shape of an inverted triangle
    for i in range(0, 3):
        t.forward(100)  # Move the turtle forward by 100 units
        t.left(120)     # Turn the turtle left by 120 degrees

    # Indicate that the drawing is done
    turtle.done()

# Call the function to draw the figure using the turtle object 't'
drawDavid(t)