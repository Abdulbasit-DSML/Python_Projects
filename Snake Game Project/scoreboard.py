from turtle import Turtle
class ScoreBoard(Turtle):
def __init__(self):
        super().__init__()
        with open("data.txt", "r") as data:
