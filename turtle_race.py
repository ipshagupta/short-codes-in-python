from turtle import Turtle, Screen
import random

# defining the screen and screen width
screen = Screen()
screen.setup(width=400, height=400)

# defining all the turtles of different colors and placing them at different starting points
y1 = -80
colors = ['red', 'green', 'blue', 'orange', 'purple']
all_turtles = []
for i in range(5):
    chosen_color = colors[i]
    turtle = Turtle(shape='turtle')
    turtle.color(chosen_color)
    turtle.penup()
    turtle.goto(x=-175, y=y1)
    all_turtles.append(turtle)
    y1 = y1 + 40

# taking the bet from the user
is_race_on = False
bet = screen.textinput(title='Place your bet', prompt='Enter the turtle\'s color you want to win')

if bet:
    is_race_on = True

while is_race_on:
    turtle_move = random.randint(0, 10)
    new_turtle = random.choice(all_turtles)
    new_turtle.forward(turtle_move)
    if new_turtle.xcor() > 175:
        winner = new_turtle.pencolor()
        if bet == winner:
            print(f"Congratulations! The {winner} turtle won the race. You won the bet!")
        else:
            print(f"You lose! The {winner} turtle won the race.")
        is_race_on = False


screen.exitonclick()
