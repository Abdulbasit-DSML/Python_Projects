from turtle import Turtle
class ScoreBoard(Turtle):
def __init__(self):
        super().__init__()
        with open("data.txt", "r") as data:
        self.high_score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

def update_scoreboard(self):
        self.clear()
        
