'''
PROJECT 9 : GAME:Rock Paper Scissars

 In the rock, paper and scissors game our goal is to create a command-line game 
 where a user has the option to choose between rock, paper and scissors and 
 if the user wins the score is added, and at the end when the user finishes 
 the game, the score is shown to the user.
'''

#  C  O  D  E

import random
import time
choices = ["Rock", "Paper", "Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or  Scissors?").capitalize()
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        time.sleep(1)
        print(f"CPU:{cpu_score}")
        print(f"Plaer:{player_score}")
        break