from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
     super().__init__()
     self.shape("circle")
     self.penup()
     self.color("blue")
