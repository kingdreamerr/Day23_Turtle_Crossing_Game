import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()

screen.onkeypress(player.move, 'Up')
game_is_on = True
car_manager = CarManager()

while game_is_on:
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move()
    screen.update()import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()



screen.exitonclick()