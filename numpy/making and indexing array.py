import numpy as np;
a = np.array([1,2,3]);
b = np.array([[1,2,3],[4,5,6],[7,8,9]]);
print(a.ndim);  #gives the dimension of array
print(b.shape); #gives the shape(rows,coloumn) of array
print(b[1,2]);  #specific element
print(b[1,:]);  #specific row
print(b[: , 1]); #specific column
