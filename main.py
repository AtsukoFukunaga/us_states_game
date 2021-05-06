import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('U.S. States Game')
screen.bgpic('blank_states_img.gif')
screen.setup(width=800, height=500)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()

player = turtle.Turtle()
player.hideturtle()
player.penup()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 states correct',
                                    prompt='What is another state\'s name?').title()
    if answer_state == 'Exit':
        states_to_learn = [state for state in all_states if state not in guessed_states]
        pd.DataFrame(states_to_learn).to_csv('states_to_learn.csv')
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        player.goto(int(state_data.x), int(state_data.y))
        player.write(answer_state, align='center', font=('Arial', 12, 'normal'))

screen.exitonclick()
