from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_back():
    tim.back(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.reset()
    screen.reset()


screen.listen()

screen.onkey(move_forward, "Right")
screen.onkey(move_back, "Left")
screen.onkey(turn_left, "Up")
screen.onkey(turn_right,"Down")
screen.onkey(clear, "c")

screen.exitonclick()
