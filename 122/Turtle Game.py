# a121_catch_a_turtle.py

#-----import statements-----
import turtle as trt
import turtle as trtl
import random as rand
import turtle as wn
import leaderboard as lb
#-----game configuration----
spot_color = "purple"
score = 0
font_setup = ("Arial",20, "normal")
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000   #1000 represents 1 second
timer_up = False
turtle_size = ["3","2","1",".8",".5"]
#-----initialize turtle-----
leaderboard_file_name = "a122_leaderboard.txt"
player_name =input("What is your name?")


#counter turtle
counter =  trtl.Turtle()
counter.penup()
counter.goto(0,250)
#clicker turtle
meowl = trtl.Turtle()
meowl.shape("circle")
meowl.color(spot_color)
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

#countdown timer start
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def size_turtle(turtle_instance, size_list):
    new_size = rand.choice(turtle_size)
    turtle_instance. shapesize(new_size)

def spot_clicked(x,y):
    global timer_up
    size_turtle()
    if timer_up == False:
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


# CODE TO ADD
# Add this function to your game code

# manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global meowl

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, meowl, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, meowl, score)




#-----events----------------
meowl.onclick(spot_clicked)




scoreBox()




# Set up the Screen
wn.bgcolor("magenta")
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()