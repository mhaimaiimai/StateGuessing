from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
map = Turtle()
state_label = Turtle()
state_label.hideturtle()
state_label.penup()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
map.shape(image)

states_data = pd.read_csv("50_states.csv")
answered_states = []
while(len(answered_states)<50):
    answer = (screen.textinput(title=f"{len(answered_states)}/50 States Correct", prompt="What's another state's name?")).title()
    state = states_data[states_data["state"]==answer]
    if answer == "Exit":
        break
    elif state.empty:
        print("This state is not existed. Please retry.")
    else:
        print("Correct! Continue to next state!")
        state_label.setposition(int(state["x"]),int(state["y"]))
        state_label.write(state["state"].item(), move = False, font = ("Arial", 12, "normal"))
        answered_states.append(answer)

missed_states = states_data
for answer in answered_states:
    search_correct_answer = missed_states[missed_states["state"] == answer].index
    missed_states = missed_states.drop(search_correct_answer.item())
missed_states[["state"]].to_csv("missed_state.csv")