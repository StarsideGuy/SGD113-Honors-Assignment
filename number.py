# (For SGD113.)
# This program generates a number 1-100, then has the player guess a random number.
# The game tells you if your number is higher or lower and adds an attempt to the counter, then loops the 'guessing' phase.
# If the player guesses the number right, it tells them they're correct and displays the number of attempts they took.
# Copilot was used to teach me all the basics about Python, as I've never worked with it before.

import random

def play():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

if __name__ == "__main__":
    play()
