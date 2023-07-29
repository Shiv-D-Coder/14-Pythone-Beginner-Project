'''
PROJECT 4 : Story Genrator

Our task is to generate a random story every time the user runs the program. 
I will first store the parts of the stories in different lists, 
then the "RANDOM MODULE" can be used to select the random parts of the story stored 
in different lists:
'''

#  C  O  D  E

import random

when = ['A few years ago', 'Yesterday',
        'Last night', 'A long time ago', 'On 07th Oct']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Shiv', 'Ram', 'Depp', 'Samay', 'Rudra']
residence = ['Korea', 'India', 'Russia', 'Japan', 'England']
went = ['cinema', 'university', 'seminar', 'school', 'laundry']
happened = ['hit on random cheaks', 'Eats a Pizza at Drizzel',
            'found a girl', 'solved a DMS problem', 'watched ANIME']

print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(
    residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
