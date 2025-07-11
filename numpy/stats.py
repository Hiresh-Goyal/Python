import numpy as np;
a = np.array([[1,2,3],[0,5,6],[11,2,9]]);
print(np.min(a));
print(np.max(a,axis = 0));
print(np.max(a,axis = 1));
print(np.sum(a));
print(np.sum(a,axis = 0));  