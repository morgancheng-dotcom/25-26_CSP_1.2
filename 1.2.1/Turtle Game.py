# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trt
import turtle as trtl
import random as rand
#-----game configuration----
spot_color = "purple"
score = 0

#-----initialize turtle-----
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()
meowl.speed(0)
score_writers = trt
score_writers.penup()
score_writers.speed(0)
score_writers.goto(0,250)
score_writers.shapesize(11)
#-----game functions--------
#get a score boost and move randomly
def spot_clicked(x,y):
    change_position()

def

def change_position():
    newX = rand.randint(-250,250)
    newY = rand.randint(-250, 250)
    meowl.goto(newX,newY)
    update_score()

def update_score():
    global score
    score += 1
    print(score)


#-----events----------------
meowl.onclick(spot_clicked)




# Set up the Screen
wn = trtl.Screen()
wn.mainloop()