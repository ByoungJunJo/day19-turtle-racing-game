# TODO: Make a turtle racing game
from turtle import Turtle, Screen
import random

def create_turtle(x, y, color):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    return new_turtle

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False
all_turtles = []

# Fixed x position
x = -230

# Starting y postion
y = -100

# Create multiple turtles and append them into the all_turtles list
i = 0
while i < len(colors):
    new_turtle = create_turtle(x=x, y=y, color=colors[i])
    all_turtles.append(new_turtle)
    i += 1
    y += 30

# Once user has bet, change the 'is_race_on' to True
if user_bet:
    is_race_on = True

# Each turtle go random amount forwards from 0 to 10
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print("You'won!")
            else:
                print("You lost!")
            print(f"You chose the {user_bet} turtle, and the winning turtle was the {winning_turtle} turtle.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()