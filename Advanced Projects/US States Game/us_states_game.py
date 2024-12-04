import turtle
import pandas as pd


def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("U.S State Game")
    screen.setup(width=800, height=600)

    # Load the US states data
    states_data = pd.read_csv("50_states.csv")

    # Print the columns of the DataFrame
    print("Columns:", states_data.columns)

    # Load the background map image
    screen.addshape("blank_states_img.gif")
    turtle.shape("blank_states_img.gif")

    # Initialize variables
    correct_guesses = 0
    guessed_states = []

    # Game loop
    while correct_guesses < 50:  # There are 50 states in total
        # Prompt user to guess a state
        guess_state = screen.textinput(title=f"Guess the State ({correct_guesses + 1}/50)",
                                       prompt="What's the name of the state?")
        if guess_state is None:
            break

        guess_state = guess_state.title()

        # Check if the guessed state is correct
        if guess_state in states_data.values and guess_state not in guessed_states:
            correct_guesses += 1
            guessed_states.append(guess_state)

            # Get the coordinates of the guessed state
            state_info = states_data[states_data["state"] == guess_state]
            x_cor = int(state_info["x"].iloc[0])
            y_cor = int(state_info["y"].iloc[0])

            # Display the name of the state on the map
            state_label = turtle.Turtle()
            state_label.hideturtle()
            state_label.penup()
            state_label.goto(x_cor, y_cor)
            state_label.write(guess_state, align="center", font=("Arial", 8, "normal"))

    # Show the number of correct guesses
    if correct_guesses == 50:
        screen.textinput(title="Congratulations!", prompt="You've guessed all 50 states correctly!")
    else:
        screen.textinput(title="Game Over", prompt=f"Sorry, you've guessed {correct_guesses} states correctly.")

    screen.bye()


if __name__ == '__main__':
    main()
