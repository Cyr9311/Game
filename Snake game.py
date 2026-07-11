import turtle
import random

screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)

snake = turtle.Turtle()
snake.shape("square")
snake.penup()

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-250, 250), random.randint(-250, 250))

def move_up():
    snake.setheading(90)

def move_down():
    snake.setheading(270)

def move_left():
    snake.setheading(180)

def move_right():
    snake.setheading(0)

screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

while True:
    snake.forward(20)

    if snake.distance(food) < 20:
        food.goto(random.randint(-250, 250), random.randint(-250, 250))

    screen.update()