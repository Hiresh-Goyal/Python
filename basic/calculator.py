from math import *
n1=input("Please enter the first number\n")
n2=input("Please enter the first number\n")
ch = 1
while(ch!=0):
    print("Enter 0 to exit")
    print("Enter 1 to perform addition")
    print("Enter 2 to perform subtraction")
    print("Enter 3 to perform multiplication")
    print("Enter 4 to perform division")
    print("Enter 5 to find number 1 ^ number 2")
    print("Enter 6 to find square root of number 1 and number 2")
    ch = input()
    if(int(ch) == 1):
        print(n1 +" + "+ n2 + " = " +str((float(n1)+float(n2))))
    elif(int(ch) == 2):
        print(n1 +" - "+ n2 + " = " +str((float(n1)-float(n2))))
    elif(int(ch) == 3):
        print(n1 +" * "+ n2 + " = " +str((float(n1)*float(n2))))
    elif(int(ch) == 4):
        print(n1 +" / "+ n2 + " = " +str((float(n1)/float(n2))))
    elif(int(ch) == 5):
        print(n1 +" ^ "+ n2 + " = " +str(pow(float(n1),float(n2))))
    elif(int(ch) == 6):
        print("square root of " +n1+ " = " +str(sqrt(float(n1))))
        print("square root of " +n2+ " = " +str(sqrt(float(n2))))
    else:
        break;