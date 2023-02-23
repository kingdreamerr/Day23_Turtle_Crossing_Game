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



screen.exitonclick()