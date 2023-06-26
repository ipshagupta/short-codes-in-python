# files used here are: 50_states.csv and blank_states_img.gif

import turtle
import pandas as pd
t = turtle.Turtle()
s = turtle.Turtle()
screen = turtle.Screen()
screen.title("Guess the U.S. State!")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50_states.csv")
game_over = False
score = 0
s.hideturtle()
s.penup()
s.goto(0, 230)
s.write(f'{score}/50', font=('arial', 17, 'bold'))

guesses = []

while not game_over or score == 50:
    answer = screen.textinput(title='Guess the State Name', prompt='Enter the state name').title()
    if answer == 'Exit':
        break
    if score == 50:
        t.hideturtle()
        s.write("GAME OVER", font=('arial', 17, 'bold'))

    for entry in data['state']:
        if answer == entry:
            guesses.append(answer)
            x_cor = int(data[data.state == answer].x)
            y_cor = int(data[data.state == answer].y)

            t.hideturtle()
            t.penup()
            t.goto(x_cor, y_cor)
            t.write(answer)

            score += 1
            s.clear()
            s.write(f'{score}/50', font=('arial', 17, 'bold'))


print(guesses)
print(score)
