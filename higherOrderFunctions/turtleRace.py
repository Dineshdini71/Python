import turtle
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(height=500, width=500)
user_bet = screen.textinput(title="Make a bet", prompt="which turtle will win the race? Enter a color: " )
colors = ["red", "yellow", "blue", "green", "purple", "orange"]
y_postions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    newTurtle = Turtle(shape="turtle")
    newTurtle.color(colors[turtle_index])
    newTurtle.penup()
    newTurtle.goto(x=-230, y=y_postions[turtle_index])
    all_turtle.append(newTurtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for tur in all_turtle:
        if tur.xcor() > 230:
            is_race_on = False
            winning_turtle = tur.pencolor()
            if winning_turtle == user_bet:
                print(f"You won the race, {winning_turtle} turtle is the win th race!")
            else:
                print(f"You lose the race, {winning_turtle} turtle is the winner")
        ran_distances = random.randint(0,10)
        tur.fd(ran_distances)

















screen.exitonclick()