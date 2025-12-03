# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spot_color = "purple"

#-----initialize turtle-----
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()

#-----game functions--------
#get a score boost and move randomly
def spot_clicked(x,y):
    print("turtle was clicked")
    newX = rand.randint(-250,250)
    newY = rand.randint(-250, 250)
    meowl.goto(newX,newY)


#-----events----------------
meowl.onclick(spot_clicked)


# Set up the Screen
wn = trtl.Screen()
wn.mainloop()