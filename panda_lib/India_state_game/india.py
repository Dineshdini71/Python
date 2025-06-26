import turtle
import pandas as pd
screen = turtle.Screen()
screen.title('INDIA State Game')
# screen.setup(width=600, height=600)
image = ('india_state.gif')
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('india_states.csv')
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name ?")
all_states = data.state.to_list()
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())

turtle.exitonclick()
