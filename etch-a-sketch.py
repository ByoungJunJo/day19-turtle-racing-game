# TODO: Make an Etch-A-Sketch App
from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterclockwise():
    tim.circle(radius=50, extent=60, steps=10)

def move_clockwise():
    tim.circle(radius=-50, extent=60, steps=10)

def clear_drawing():
    tim.reset()

screen.listen()
# Function as inputs (higher order functions); Use keyword arguments
screen.onkey(fun=move_forwards, key="W")
screen.onkey(fun=move_backwards, key="S")
screen.onkey(fun=move_counterclockwise, key="A")
screen.onkey(fun=move_clockwise, key="D")
screen.onkey(fun=clear_drawing, key="C")
screen.exitonclick()