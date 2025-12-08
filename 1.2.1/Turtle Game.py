# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trt
import turtle as trtl
import random as rand
#-----game configuration----
spot_color = "purple"
score = 0
font_setup = ("Arial",20, "normal")
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
#clicker turtle
counter =  trtl.Turtle()
counter.penup()
counter.goto(0,250)
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
meowl.shapesize(3)
meowl.penup()
meowl.speed(0)
#shape turtle
box_turtle = trtl.Turtle()
box_turtle.hideturtle()
#score turtle
score_writers = trtl.Turtle()
score_writers.hideturtle()
score_writers.penup()
score_writers.speed(0)
box_turtle.speed(0)
box_turtle.penup()
box_turtle.goto(300,350)
box_turtle.shapesize(1)
#-----game functions--------
#get a score boost and move randomly
# draw the box for the score
def scoreBox():
    box_turtle.goto(275,300)
    box_turtle.pendown()
    for u in range (2):
        box_turtle.forward(100)
        box_turtle.left(90)
        box_turtle.forward(50)
        box_turtle.left(90)
    score_writers.penup()
    score_writers.goto(300,310)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)


def spot_clicked(x,y):
    if timer_up is False:
        change_position()
    else:
        meowl.hideturtle()





def change_position():
    newX = rand.randint(-250,250)
    newY = rand.randint(-250, 250)
    meowl.goto(newX,newY)
    update_score()

def update_score():
    global score
    score += 1
    score_writers.clear()
    score_writers.write(score,font=font_setup)


#-----events----------------
meowl.onclick(spot_clicked)




scoreBox()




# Set up the Screen
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()