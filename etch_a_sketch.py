from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(10)
def backwards():
    tim.backward(10)
def left_turn():
    tim.left(10)
def right_turn():
    tim.right(10)
def turn_around():
    tim.left(180)
def clear_screen():
    tim.reset()


screen.listen()
screen.onkey(key='w', fun=forwards)
screen.onkey(key='s', fun=backwards)
screen.onkey(key='a', fun=left_turn)
screen.onkey(key='d', fun=right_turn)
screen.onkey(key='t', fun=turn_around)
screen.onkey(key='c', fun=clear_screen)
screen.exitonclick()
