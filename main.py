import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_turtle, "Up")
car_manager = CarManager()
score = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_random_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 15:
            score.game_is_over()
            game_is_on = False

    if player.is_at_finish():
        player.restart()
        car_manager.increase_speed()
        score.update_scoreboard()

screen.exitonclick()
