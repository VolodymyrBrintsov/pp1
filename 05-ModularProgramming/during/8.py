import turtle
speed = 0.1
pen = turtle.Turtle()

def drawSquare(x,y,n):
    
    pen.speed(0)
    pen.penup()
    pen.setposition(x*100,y*100)
    pen.pendown()
    for i in range(4):
        pen.forward(100*n)
        pen.right(90)     # Rotate clockwise by 90 degrees
    

ix=0
iy=0

for ix in range(4):
    drawSquare(ix,iy,1)
    for iy in range(4):
        drawSquare(ix,iy,1)