'''
PROJECT 5 : Password Genrator

To create a password with Python, we need to create a program that takes 
the length of the password and generates a random password of the same length
To write a Python program to create a password, declare a 
string of "numbers + uppercase + lowercase + special characters". 
'''

#  C  O  D  E

import random

len_pass = int(input("Enter the length of pssword: "))

string = ("a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 0 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ! @ # $ % ^ & * ? ")
list_of_charactars = string.split()

print("\nGenrating password of given length... ")
print("\nYour password is: ", end="")

for i in range(len_pass):
    x = random.choice(list_of_charactars)
    print(x, end="")
