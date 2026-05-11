import random

# Options
choices = ["rock", "paper", "scissors"]

# Take user input
user_choice = input("Enter rock, paper, or scissors: ").lower()

# Computer choice
computer_choice = random.choice(choices)

print("Computer chose:", computer_choice)

# Game logic
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
elif user_choice in choices:
    print("You lose!")
else:
    print("Invalid input! Please choose rock, paper, or scissors.")
    