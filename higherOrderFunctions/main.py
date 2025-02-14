from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.fd(10)
def move_backward():
    tim.backward(10)
def turn_left():
    new_heading = tim.heading()
    tim.setheading(new_heading + 10)
def turn_right():
    new_heading = tim.heading()
    tim.setheading(new_heading - 10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(move_backward, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()