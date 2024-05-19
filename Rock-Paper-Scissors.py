import random

# Define the options
options = ["Rock", "Paper", "Scissors"]

# Get the player's choice
player_choice = input("Choose Rock, Paper, or Scissors: ")

# Generate the computer's choice
computer_choice = random.choice(options)

# Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes scissors! You win!")
elif player_choice == "Rock" and computer_choice == "Paper":
    print("Paper covers rock! You lose.")
elif player_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers rock! You win!")
elif player_choice == "Paper" and computer_choice == "Scissors":
    print("Scissors cuts paper! You lose.")
elif player_choice == "Scissors" and computer_choice == "Rock":
    print("Rock smashes scissors! You lose.")
elif player_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cuts paper! You win!")