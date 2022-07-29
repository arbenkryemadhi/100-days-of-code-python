import random

from art import logo

random_number = random.randint(1, 100)
guesses = 0


def difficulty_chooser():
    global guesses
    difficulty_user_input = input(
        "Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty_user_input == "easy":
        guesses = 10
        print("You have 10 guesses!")
    elif difficulty_user_input == "hard":
        guesses = 5
        print("You have 5 guesses!")
    else:
        print("Incorrect Input: Please try again!")
        difficulty_chooser()


print(f"""
{logo}
Welcome to the Number Guessing Game
""")
difficulty_chooser()
while True:
    if guesses == 0:
        print("No more guesses left, Game Over!")
        break
    number_chosen = int(input("Chose a number between 1-100: "))

    if number_chosen > random_number:
        print("Too high, guess again.")
        guesses -= 1
        print(f"Guesses left: {guesses}")
    elif number_chosen < random_number:
        print("Too low, guess again.")
        guesses -= 1
        print(f"Guesses left: {guesses}")
    else:
        print(f"Good Job! You found the secret number: {random_number}")
        break
