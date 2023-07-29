'''
PROJECT 1 : Acronym Name

An acronym is a short form of a word created by long words or phrases such 
as NLP for natural language processing.  
'''

#  C  O  D  E


# Take the input from user
acronym_name =input("Plese, enter full name: ")

# Type cast into list
ls=acronym_name.split()

# Return first charactar(ACRONYMS) by loop
for i in ls:
    print(i[0].upper(),end="")
    


