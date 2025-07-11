numbers = [0,1,2,3,"4",True]
friends = ["negi","krishna","saransh","harry"]

print(numbers)
print(numbers[1])
print(numbers[-1])
print(numbers[3:])
print(numbers[3:5])
numbers[4] = "hi i got replaced"
print(numbers[3:5])


friends.append("rangwani")
print(friends)

friends.extend(numbers)
print(friends)

friends.insert(1,"my pc")
print(friends)

friends.remove(1)
print(friends)

friends.append("krishna")
friends.remove("krishna")
print(friends)

friends.clear()
print(friends)

print(numbers)
numbers.pop()
print(numbers)

numbers.append("sung jinwoo")
print(numbers.index("sung jinwoo"))

number2 = ["a",'b','c','d','a','e','a']
print(number2.count('a'))

print(number2)
number2.sort()
print("The sorted list is as follows :-")
print(number2)

number3 = [5,2,8,0,1,4,7]
print(number3)
number3.reverse()
print("The reversed list is as follows :-")
print(number3)

number4 = number3.copy()
print("this is number 4:-")
print(number4)