import random


def get_number_of_dice() -> int:
    while True:
        try:
            user_input = input(
                "Enter a number between 1 and 6 to choose the number of dice or type 'exit' to quit: "
            )
            if user_input.lower() == "exit":
                exit_game()
            else:
                number_of_dice = int(user_input)
                if 1 <= number_of_dice <= 6:
                    return number_of_dice
                else:
                    print("Please enter a number between 1 and 6!")
        except ValueError:
            print("Please enter a valid integer or type 'exit' to quit.")


def exit_game():
    print("Exiting the game. Goodbye!")
    exit()

5
def get_dice() -> list:
    dice = []
    for _ in range(get_number_of_dice()):
        dice.append(random.randint(1, 6))
    return dice


def dice_game():
    dice = get_dice()
    while True:
        print(dice)
        user_input = input("Type 'exit' to quit or roll the dice: ")
        if user_input.lower() == "exit":
            exit_game()
        try:
            roll = int(user_input)
            if roll == sum(dice):
                print("You got it!")
                break
            else:
                print("Wrong! Better luck next time!")
                dice = get_dice()
        except ValueError:
            print("Please enter a valid integer or type 'exit' to quit.")


if __name__ == "__main__":
    dice_game()
