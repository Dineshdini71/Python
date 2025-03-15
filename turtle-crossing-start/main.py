import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    #detect collision with wall
    for each_car in car.all_car:
        if each_car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish():
        player.go_to()
        score.increase_level()


screen.exitonclick()