import turtle as trtl
#to draw squares with a turtle
james = trtl.Turtle()

def drawSquare(length):
    for sides in range(4):
        james.forward(length)
        james.right(90)

drawSquare(61)
james.forward(60)
drawSquare(47)



wn = trtl.Screen()
wn.mainloop()