print("day_4 project -rock paper scissors")
import random

# Rock
Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [Rock,Paper,Scissors]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for paper, 2 for Scissors\n"))
print(game_images[user_choice])
# 0, 1 , 2
computer_choice = random.randint(0,2)
print(f"computer choice {computer_choice}")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("you typed invalid number. you lose!")
elif user_choice ==  0 and computer_choice == 2:
    print("you win!")
elif computer_choice ==  2 and user_choice == 0:
    print("computer wins!")
elif computer_choice > user_choice:
    print("computer wins!")
elif user_choice > computer_choice:
    print("you win!")
elif user_choice == computer_choice:
    print("It's a draw!")