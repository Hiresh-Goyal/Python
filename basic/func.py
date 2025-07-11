def sayhi():
    print("hi my user")
    print("hope you are doing well")

sayhi()

def para_say_hi(name):
    print("hi "+name)
    print("hope you are doing well")

para_say_hi("Mike")

from math import *

def cube(num):
    return(pow(num,3))

print("Cube of 4 = " +str(cube(4)))

def exponent(a,b):
    return(pow(a,b))

print("5 ^ 3 = " + str(exponent(5,3)))
print(5.5**3)