from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
segment = [] 

snake = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()


    #Detect collision Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        score.game_over()
    # Detect collision the tail
    for seg in snake.segment[1:]:
        if snake.head.distance(seg) < 10:
            is_game_on = False
            score.game_over()




screen.exitonclick()