import random

print("Welcome to Rock Paper Scissors Game. Made by Arben KRYEMADHI!")
user_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_input = random.randint(0, 2)

result = ""

# RPS Images
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

if user_input >= 3:
    print("Chose a smaller number!")
elif user_input == computer_input:
    result = "draw"
elif abs(user_input - computer_input) == 1:
    if user_input > computer_input:
        result = "human_win"
    else:
        result = "computer_win"
else:
    if user_input > computer_input:
        result = "computer_win"
    else:
        result = "human_win"

if result == "human_win":
    print(f"""
    You chose:
    {game_images[user_input]}
    Computer chose:
    {game_images[computer_input]}
    You won!
    """)
elif result == "computer_win":
    print(f"""
    You chose:
    {game_images[user_input]}
    Computer chose:
    {game_images[computer_input]}
    You lost!
    """)
elif result == "draw":
    print(f"""
    You chose:
    {game_images[user_input]}
    Computer chose:
    {game_images[computer_input]}
    Draw!
    """)
