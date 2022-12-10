#  python snake game, @author, 26/03/21
import turtle
import random
import time

delay = 0.1
score = 0
highestScore = 0

# snake bodies
bodies = []

# getting a screen | canvas
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray")
s.setup(width=600, height=600)

# create snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.fillcolor("blues")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0, 200)
food.st()

# score board

sb = turtle.Turtle()
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.goto(-250, -250)
sb.write("score: 0    |     Highest Score: 0")


def moveUp():
    if head.direction != "down":
        head.direction = "up"


def moveDown():
    if head.direction != "up":
        head.direction = "down"


def moveLeft():
    if head.direction != "right":
        head.direction = "left"


def moveRight():
    if head.direction != "left":
        head.direction = "right"


def moveStop():
    head.direction = "stop"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        y = head.xcor()
        head.sety(y - 20)

    if head.direction == "right":
        y = head.xcor()
        head.sety(y + 20)


#  Event Handling - Key mapping
s.listen()
s.onkey(moveUp(), "Up")
s.onkey(moveDown(), "Down")
s.onkey(moveLeft(), "Left")
s.onkey(moveRight(), "Right")
s.onkey(moveStop(), "Stop")

# main loop
while True:
    s.update()  # this is to update the screen
    # check collision with border
    if head.xcor() > 290:
        head.setx(-290)

    if head.xcor() < -290:
        head.setx(290)

    if head.ycor() > 290:
        head.sety(-290)

    if head.ycor() < -290:
        head.sety(290)
