import numpy as np;
print(np.zeros((2,4)));   #all 0 array
print(np.ones((2,4)));    #all 1 array
print(np.full((2,3),5));  #all 5 array
print(np.random.rand(2,3));  #random no. between 0 and 1
print(np.random.randint(2,100, size = (2,3)));  #int no's between 2-100
print(np.identity(3));  # 3x3 indentity matrix

a = np.array ([[1,2,3]]);
b= np.repeat(a,3,axis = 0);  #repeats a 3 times
c= np.repeat(a,3,axis = 1);
print(b);
print(c);

a = np.ones((5,5));
a[1:4,1:4] = 0;
a[2,2] = 9;
print(a);