'''
PROJECT 10 : Colour text

Using the Colorama module we can print colored text with Python. We can use 
it and call its built-in variables which are aliases for the desired ANSI codes. 
This makes our code more readable and works better with Windows command 
prompts after calling colorama.init() at the start of your script.
'''

#  C  O  D  E

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# CHANGE IN FONT
print(Fore.BLUE+Back.YELLOW+"Hi I am shiv patel "+ Fore.YELLOW+ Back.BLUE+"I am learing python programing")
print(Fore.RED+"Hey there ")
print(Fore.BLUE+"Nice to meet ya")
print(Fore.GREEN+"I am shiv")

# CHANGE IN BACKGROUND
print(Back.MAGENTA + "Background chance")
print(Back.BLUE+"Background chance")

# RANINBOW COLOUR CHANGE
print(f"{Fore.RED}H{Fore.YELLOW}E{Fore.GREEN}L{Fore.BLUE}L{Fore.MAGENTA}O")
print(f"{Fore.RED}W{Fore.YELLOW}O{Fore.GREEN}R{Fore.BLUE}L{Fore.MAGENTA}D")
print(f"{Back.RED}H{Back.YELLOW}E{Back.GREEN}L{Back.BLUE}L{Back.MAGENTA}O")
print(f"{Back.RED}W{Back.YELLOW}O{Back.GREEN}R{Back.BLUE}L{Back.MAGENTA}O")


# USING STYLE
print(f"{Fore.RED}{Back.WHITE}{Style.BRIGHT}THIS IS BRIGHT")

print(f"{Fore.RED}{Back.WHITE}{Style.NORMAL}THIS IS NORMAL")
print(f"{Fore.RED}{Back.WHITE}{Style.DIM}THIS IS DIM")