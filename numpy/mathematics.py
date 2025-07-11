import numpy as np;
#=,-,*,/ all can be used with array and they just apply that to all elements of the array

a = np.array([1,2,3,4]);
print(a*2);

b = np.array([1,0,1,0]);
print(a+b);

print(np.sin(a));
print(np.matmul(a,b)); #matrix mutiplication of a and b.. NOTE:- a*b will just multiply each element of a with corresponding elemnt of b and return the result

c = np.array([[1,2],[3,4]]);
print(np.linalg.det(c)); #find the det of matrix



#NOTE :- Refer :- https://docs.scipy.org/doc/numpy/reference/routines.linalg.html