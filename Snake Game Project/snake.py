from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT =0

def __init__(self):
        self.segments= []
        self.create_snake()
        self.head = self.segments[0]
        
def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

 def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

def extend(self):
        self.add_segment(self.segments[-1].position())

def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

