import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_states = pandas.read_csv("50_states.csv")
list_of_states = data_states["state"].to_list()

namer = turtle.Turtle()
namer.penup()
namer.hideturtle()

correct_guesses = []
num_correct = 0
while num_correct != 50:
    answer_state = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="Input a state's name").title()

    if answer_state == "Exit":
        break

    if answer_state in list_of_states:
        state = data_states[data_states.state == answer_state]
        namer.setposition(int(state.x), int(state.y))
        namer.write(answer_state)
        num_correct += 1
        correct_guesses.append(answer_state)

states_to_study = [state for state in list_of_states if state not in correct_guesses]

new_data = pandas.DataFrame(states_to_study)
new_data.to_csv("states_to_study.csv")

turtle.mainloop()
