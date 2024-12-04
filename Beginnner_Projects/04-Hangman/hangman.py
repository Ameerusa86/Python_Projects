import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "coding", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("\nWord: " + current_display)
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter. Try again.")
                continue

            guessed_letters.append(guess)

            if guess not in word_to_guess:
                attempts += 1
                print("Incorrect guess. Attempts left: {}".format(max_attempts - attempts))
                if attempts == max_attempts:
                    print("Sorry, you ran out of attempts. The word was '{}'.".format(word_to_guess))
                    break
            else:
                print("Good guess!")

            if "_" not in display_word(word_to_guess, guessed_letters):
                print("Congratulations! You guessed the word: '{}'".format(word_to_guess))
                break
        else:
            print("Invalid input. Please enter a single letter.")

if __name__ == "__main__":
    hangman()
