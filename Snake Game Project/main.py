import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()

screen.setup(600,600)
screen.bgcolor("black")

screen.title("My sanke game")
screen.tracer(0)

snake = Snake()
