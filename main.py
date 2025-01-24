import random

# Choices for players
choices = ["rock", "paper", "scissors"]

# Get the player's choices through input()
while True:
  player_choice = input("Enter your choice (rock, paper or scissors): ").lower()
  if player_choice in choices:
    break
  else:
    print("Invalid choice. Please choose from the accepted values: rock, paper or scissors.")

# Get the Ai's choices through random()
ai_choice = random.choice(choices)

# Display Choices
print(f"You chose: {player_choice}")
print(f"AI chose: {ai_choice}")

# Compare player and ai choices
if player_choice == ai_choice:
    print("It's a draw!")
elif  (player_choice == "rock" and ai_choice == "scissors") or (player_choice == "paper" and ai_choice == "rock") or (player_choice == "scissors" and ai_choice == "paper"):
  print("You win!")
else:
  print("You lose!")
  