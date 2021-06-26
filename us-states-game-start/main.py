import turtle
import pandas

INITIAL_PROMPT = "What's a state's name?"
PROMPT = "What's another state's name?"
NUMBER_OF_STATES = 50

# Creating screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Getting the states csv
data = pandas.read_csv("50_states.csv")

# Making a list from the state column
all_states = data.state.to_list()
# Keeping track of correct guesses
correct_guesses = 0

guessed_states = []
# Looping while all states haven't been guessed
game_on = True
while game_on:

    # Initial popup question
    if correct_guesses == 0:
        answer_state = screen.textinput("Guess a State", prompt=INITIAL_PROMPT)
    else:
        answer_state = screen.textinput(f"Correct: {correct_guesses}/{NUMBER_OF_STATES}", prompt=PROMPT)

    # Check if answer is in the state list
    if answer_state.title() in all_states:
        # Make turtle object go to x,y position defined in csv and write the state name
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Getting the row of corresponding state
        state_data = data[data.state == answer_state.title()]

        # Writing the state name on the map
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state.title())

        correct_guesses += 1

    # If all states have been guessed, end loop
    if correct_guesses == 50:
        game_on = False

turtle.mainloop()
