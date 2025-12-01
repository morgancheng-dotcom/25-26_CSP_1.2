import turtle as trtl
#to draw squares with a turtle
james = trtl.Turtle()

def drawSquare():
    for sides in range(4):
        james.forward(30)
        james.right(90)

drawSquare()
james.forward(60)
drawSquare()



wn = trtl.Screen()
wn.mainloop()