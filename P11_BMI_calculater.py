'''
PROJECT 11 : BMI(Body Mass Index) calculater

The Body Mass Index or BMI is calculated from weight and height of a Person
BMI is a measure of relative weight based on an individual’s mass and height, 
Today, Body Mass Index is commonly used to classify people as 
underweight, overweight, and even with obesity. Also, it is adopted by countries to promote 
healthy eating.
BMI can be considered as an alternative for direct measurements of body fat.
'''

#  C  O  D  E

Hight=float(input("Enter your hight in meters: "))
Weight=float(input("Enter your weight in kg: "))

BMI=Weight/(Hight*Hight)

if(BMI>0):
    if(BMI<=18.5):
        print("Your are underweight man")
    elif(BMI<=24.5):
        print("You are completly heathy")
    elif(BMI<=30):
        print("You are overweight, do some workout man")
else:
    print("Physic like that can not exist")  
    
print("Your Body Mass Index is: ", BMI)                  
    