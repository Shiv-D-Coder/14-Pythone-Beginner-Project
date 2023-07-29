'''
PROJECT 12 : Convert Fahrenheit to Celsius

It does not need any expalnation
'''

#  C  O  D  E

def Fer_to_cel(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

print(Fer_to_cel(78))
