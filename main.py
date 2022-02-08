import turtle
import pandas

# Everything about turtle
screen = turtle.Screen()
screen.title("U.S. states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=750, height=520)
state_name = turtle.Turtle()
state_name.hideturtle()
state_name.penup()

# Everything about panda
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# Everything about game logic
correct_guesses = []
game_is_on = True
while game_is_on:
    if not correct_guesses:
        answer = (screen.textinput(title="Guess States", prompt="What's your state name guess?")).title()
    else:
        answer = (screen.textinput(title=f"{len(correct_guesses)}/{len(all_states)} States Correct",
                                   prompt="What's another state name?")).title()
    if answer in all_states:
        state_data = data[data.state == answer]
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(answer)
        correct_guesses.append(answer)
    if len(correct_guesses) == 50:
        game_is_on = False
        print("Great! You've guessed all states of America.")
    if answer == "Exit":
        states_left = [state for state in all_states if state not in correct_guesses]
        states_left_dict = {"state": states_left}
        pandas.DataFrame(states_left_dict).to_csv("states_to_learn.csv")
        break
