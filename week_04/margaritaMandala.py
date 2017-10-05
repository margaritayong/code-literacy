import turtle

loadWindow = turtle.Screen() # create window
turtle.speed(0) # turn off draw mode
turtle.colormode(255) # set color RGB
turtle.bgcolor("black") # set background color

# color palette
red = 255, 87, 87
orange = 232, 162, 65
green = 151, 255, 127
blue = 82, 191, 255
purple = 153, 93, 232

myColors = [red, orange, green, blue, purple]

# spiral shape
def spiralShape():
    for i in range(7):
        turtle.circle(10*i)
        turtle.circle(-10*i)
        

def moveShape():
    turtle.right(90)
    turtle.forward(90)
    turtle.left(18)
    turtle.forward(90)

def drawStar():
    for i in myColors:
        turtle.color(i)
        spiralShape()
        moveShape()

for i in range(20):
    drawStar()
    turtle.forward(100)
    turtle.left(45)

#wait for user to end
turtle.exitonclick()