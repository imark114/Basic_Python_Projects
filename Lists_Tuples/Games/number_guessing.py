# Number Guessing Game: Generate a random number and ask the user to guess it. Keep track of the number of attempts using a list.
import random

def number_gussing_game():
    target_number = random.randint(1,100)
    attempts = []

    while True:
        guess = int(input("Enter a Number between 1 and 100: "))
        attempts.append(guess)

        if target_number == guess:
            print("Congratulations! You guessed the number in", len(attempts), "attempts.")
            return
        elif target_number > guess:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

number_gussing_game()