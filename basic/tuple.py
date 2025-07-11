coords = (450,960)   #tuples cant be changed later on like you cant do coords[1] = 500
print(coords[1])
print(coords)

coords = (340,321)   #but you can do this
print(coords)

new_coords = [(1,2),(3,4),(5,6)] #lsit of tuples
print(new_coords)
new_coords[1] = (420,960)
print(new_coords)

#new_coords[1][0] = 32        This cannot be done as we are trying to change value of tuple which is not possible