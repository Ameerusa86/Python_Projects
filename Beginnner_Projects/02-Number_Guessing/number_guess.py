# Guessing Game Number 1 - 10

import random


def get_number() -> int:
    return random.randint(1, 10)


def get_guess() -> int:
    while True:
        try:
            guess = int(input("Enter a number between 1 and 10: "))
            return guess
        except ValueError:
            print("Please enter a number between 1 and 10!, only numbers are allowed!")


def guess_game():
    number = get_number()
    guess = get_guess()
    while guess != number:
        if guess < number:
            print("Too low!")
            guess = get_guess()
        elif guess > number:
            print("Too high!")
            guess = get_guess()
        if guess == number:
            print("You got it!")
            break


if __name__ == "__main__":
    guess_game()
