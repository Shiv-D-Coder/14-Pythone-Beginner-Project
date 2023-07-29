'''
PROJECT 9 : Making Qizze

The Quiz game asks the player questions about animals. They have three chances 
to answer each question you don’t want to take the quiz too difficult. 
Each correct answer will score a point. At the end of the game, 
the program will reveal the player’s final score
'''

#  C  O  D  E
import time

name = input("Enter your name: ")
print("Starting the quiz...")
time.sleep(2)

count = 0
print("What is the name of our national animal? /n")
ans1 = input("Your ans: ").lower()
for attmept in range(0, 2):
    if ans1 == "tiger":
        print("Correct")
        count += 1
        break
    else:
        print(f"{ans1} is not correct one")
        ans1 = input("Please, write your answer again: ")

print("Wait, another qustion will apper sortly..")
time.sleep(1)
print("What is known as king of fruits? /n")
ans2 = input("Your ans: ",).lower()
for attempt2 in range(0, 2):
    if ans2 == "mango":
        print("correct")
        count += 1
        break
    else:
        print(f"{ans2} is not correct")
        ans2 = input("Please, write your answer again: ")

if count == 2: performence = "EXELENT"
if count == 1: performence = "GOOD,try to score perfect next time"
if count == 0: performence = "VERY POOR, you need to study hard"

print(f"{name} Preparing your scorecard...")
time.sleep(1)
print(f"\n{name} your score is {count}, you performed {performence}")
