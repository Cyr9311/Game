import random

choices = ["rock", "paper", "scissors"]

player = input("Rock, Paper, or Scissors? ").lower()
computer = random.choice(choices)

print("Computer:", computer)

if player == computer:
    print("Draw!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You Win!")
else:
    print("You Lose!")
