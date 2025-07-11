for letter in "Hi everyone":
    print(letter)

friends = ["negi","krishna","saransh","harry"]
for i in friends:
    print(i)

for i in range(10):  #range(10) gives 0 to 9
    print(i)

print()

for i in range(5,10):  #range(5,10) gives 5 to 9
    print(i)

for name in range(len(friends)):
    print(friends[name])

mylist = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for row in mylist:
    print(row)

for row in mylist:
    for col in row:
        print(col)
