'''
PROJECT 13 : Taking Multiple input

Suppose you are prompted to write a Python program that interacts with a user 
in a console window. You may be accepting input to send to a database, 
or reading numbers to use in a calculation.

Whatever the purpose, you should code a loop that reads one or multiple user 
inputs from a user typing on a keyboard and prints a result for each. In other
words, you have to write a classic print loop program.
'''

#  C  O  D  E
import time
import random
import colorama
from colorama import Fore,Back,Style

print("Wellcome to my dating App, Here you can find your dream partnar")
choice=input("Are you intrested in Girl or Boy? ").lower()
print("\n Start seaching...")
print("\nFinding best opption for you...")
time.sleep(2)

Girls=["Shivangi","Muskan","Shweta","Mallika","Tanushree ","Riya","Priya","Ragini"]
Boys=["Shiv","Harsh","Darshan","Kalp","Manth","Jinesh","Rakesh","Kashish"]
partnar_words=["Wanna grabe coffee","Wannna play COD","I kindda like you",
               "We have very same intrest in movies","Love for anime",
               "Ya,we can talk more","Plase go away"]

if choice=="girl":
    Dream_girl=random.choice(Boys)
    print(f"Seems you find {Dream_girl}")
if choice=="boy":
    Dream_boy=random.choice(Girls)    
    print(f"Seems you find {Dream_boy}")
partnar=random.choice(partnar_words)

for you in range (60):
    colorama.init(autoreset=True)
    you=input(f"{Fore.GREEN}{Style.BRIGHT}Write here:{Fore.RED} ")
    time.sleep(0.8)
    print(f"{Fore.CYAN}partnar says {Fore.GREEN} {partnar}")
    
    if you=="number".lower():
        print(f"{Fore.BLUE}{Style.BRIGHT}Now you can excahange numbers")
        print(f"{Fore.MAGENTA}Your partnars Phone numbers is: ",end="")
        for Baby_number in range(10):
            Baby_number=random.randint(0,9)
            print(Baby_number,end="")
    print()        
    if you == "next".lower():
        partnar_words.append("It was nice taking to you see you soon") 
        random.choices(partnar_words , k=8)  
        break 
    
       
    

    
       
    
