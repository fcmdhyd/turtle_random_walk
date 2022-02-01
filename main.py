import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("medium violet red")

colors = ["red","blue","green","brown","orange","yellow"]
direction = [0, 90, 180, 270]

for _ in range(250):
    tim.pensize(7)
    tim.color(random.choice(colors))
    tim.speed(8)
    tim.fd(30)
    tim.setheading(random.choice(direction))




screen = Screen()

screen.exitonclick()