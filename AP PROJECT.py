#Snake Facts
import random as rand
current_number = "One"

#Different Shark Facts
Fact_1 = "Of almost 4,000 known species of snake, about 600 are considered venomous."
Fact_2 = "Snakes are strictly carnivorous and eat their prey whole."
Fact_3 = "Molting (shedding scales) helps snakes get rid of ticks and parasites."
Fact_4 = "Snakes can lay eggs and also give live birth"
Fact_5 = "Black mambas can slither at speeds up to 19km/h, while sidewinder rattlesnakes can reach speeds of up to 29km/h."
Fact_6 = "Serpents can smell in stereo, thanks to their forked tongues that they use to collect chemicals from the environment."
Fact_7 = "Lacking external ears, snakes hear by sensing vibrations through their jawbones."
Fact_8 = "Some snake venom is used in medicine to treat blood pressure issues, heart attacks, and blood disorders."
Fact_9 = "Snakes do not have vocal cords but can produce a hissing sound by forcing air through their windpipe."
Fact_10 = " Vipers, pythons, and rattlesnakes have pit holes in their faces that detect heat, allowing them to visualize warm-blooded prey."


#list of facts
snake_facts = [Fact_1, Fact_2, Fact_3, Fact_4, Fact_5, Fact_6, Fact_7, Fact_8, Fact_9, Fact_10]

non_facts = snake_facts.copy()

#no repeating facts
def no_repeat_fact():
    global non_facts

    if len(non_facts) == 0:
        non_facts = snake_facts.copy()

    fact = rand.choice(non_facts)
    non_facts.remove(fact)

    return fact
no_repeat_fact()

def give_out_facts(amount):
    for i in range(amount):
        print(no_repeat_fact())


#randomize facts
def randomize_facts():
    rand.shuffle(snake_facts)


randomize_facts()
popped_fact = snake_facts.pop()

#lists answers
all_list = ["give me all","Give me all"]
maybe_list = ["maybe","Maybe"]
no_list = ["no","No","nah","Nah"]
yes_list = ["yes","Yes","yeah","Yeah"]
One_list = ["One", "one", "1"]
Two_list = ["Two","two","2"]
Three_list = ["Three","three","3"]
Four_list = ["Four","four","4"]
Five_list = ["Five", "five", "5"]
Six_list = ["Six", "six", "6"]
Seven_list = ["Seven", "seven", "7"]
Eight_list = ["Eight", "eight", "8"]
#asking for the facts
def ask_the_facts():
    initial_answer = answer = input("Do you want to hear a Snake fact? ")

#if yes
    if initial_answer in yes_list:
        give_out_facts(1)
        amount_of_snake_facts = answer = input("How many more Snake facts 1-8 do you want to hear? Or type no to end the code ")

#possible answers
        if amount_of_snake_facts in One_list:
            give_out_facts(1)
            print("I hope you enjoyed my Snake Fact!")
        if amount_of_snake_facts in Two_list:
            give_out_facts(2)
        if amount_of_snake_facts in Three_list:
            give_out_facts(3)
        if amount_of_snake_facts in Four_list:
            give_out_facts(4)
        if amount_of_snake_facts in Five_list:
            give_out_facts(5)
        if amount_of_snake_facts in Six_list:
            give_out_facts(6)
        if amount_of_snake_facts in Seven_list:
            give_out_facts(7)
        if amount_of_snake_facts in Eight_list:
            give_out_facts(8)
        if amount_of_snake_facts in no_list:
            print("Those are my Snake Facts!")


#if said no to original question
    elif initial_answer in no_list:
        print("Buh Bye!")
    elif initial_answer in maybe_list:
        print("Okay, come back when you made your choice!")
    elif initial_answer in all_list:
        print(snake_facts)
    else:
        print("Invalid Answer, Try Again. Commands are Yes, No or Give me all")

ask_the_facts()

#end
print("Snake Facts are Cool!")