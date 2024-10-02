# rock paper scissors game

import random

choices = ["rock", "paper", "scissor"]

computer_choose = random.choice(choices)

player_choose = input("rock, paper or scissor? :")

print("\nYou choose: ",player_choose)
print("Computer choose: ",computer_choose)
print("\n")
if player_choose not in choices:
    print("Invalid input! Please choose rock, paper or scissor! ")
    
else:
    if computer_choose == player_choose:
        print("Its draw!\n")
    
    elif computer_choose == choices[0] and player_choose == choices[1]:
        print("You Win!\n")

    elif computer_choose == choices[1] and player_choose == choices[2]:
        print("You Win!\n")

    elif computer_choose == choices[2] and player_choose == choices[0]:
        print("You Win!\n")

    else:
        print("Computer Win!\n")