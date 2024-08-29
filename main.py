from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

python = Snake()
food = Food()
detect = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=python.up)
screen.onkey(key="Right", fun=python.right)
screen.onkey(key="Left", fun=python.left)
screen.onkey(key="Down", fun=python.down)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    python.move()

    # Detect collision with food.
    if python.head.distance(food) < 15:
        food.refresh()
        python.extend()
        detect.increase_score()

    # Detect collision with wall.
    if python.head.xcor() > 290 or python.head.xcor() < -290 or python.head.ycor() > 290 or python.head.ycor() < -290:
        detect.reset()
        python.reset()

    # Detect collision with tail.
    for segment in python.segments[1:]:
        if python.head.distance(segment) < 10:
            detect.reset()
            python.reset()

screen.exitonclick()
