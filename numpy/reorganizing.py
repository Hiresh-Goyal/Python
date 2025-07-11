import numpy as np;

before = np.array([[1,2,3,4],[5,6,7,8]]);
after = before.reshape((8,1));
print(after);

v1 = np.array([[1,2,3,4],[9,10,11,12]]);
v2 = np.array([[5,6,7,8],[13,14,15,16]]);
print(np.vstack([v1,v2,v1]));
print(np.hstack([v1,v2]));