cars = open("cars.txt","r")
print(cars.readable())    #checks if file is readable
print(cars.readline())    #print a single line
print(cars.readlines())   #print lines as a list
cars.close()