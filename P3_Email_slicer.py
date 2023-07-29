'''
PROJECT 3 : Email Slicer

our task is to write a program that can retrieve the username and the 
domain name of the email. 
For example, look at the image below which shows the domain and username of 
“swordshiv@toopscode.com”:
'''

#  C  O  D  E

Mail=input("Enter you E-mail here: ")

# finding "@" here
sepratar=Mail.find("@")

# giving them index accordingly
user_name=Mail[:sepratar]
domain_name=Mail[sepratar+1:]

print(f"User name is: {user_name}")
print(f"Domain name is: {domain_name}")

