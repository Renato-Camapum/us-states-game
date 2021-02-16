from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's the next State's name?").title()
    state_data = data[data.state == answer_state]

    if answer_state in states_list:
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)
        # print(guessed_states)

    if answer_state == "Exit":
        for st in guessed_states:
            states_list.remove(st)
            missed_states = pandas.DataFrame(states_list)
            missed_states.to_csv("Missed_states.csv")
        print(missed_states)
        break
