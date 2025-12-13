import turtle

# Create turtle object
t = turtle.Turtle()

# Set speed
t.speed(3)

# Draw a square
for i in range(4):
    t.forward(100)   # move forward 100 units
    t.right(90)      # turn right 90 degrees

# Keep the window open
turtle.done()
