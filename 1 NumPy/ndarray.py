import numpy as np
a = np.array([1,2,3])
print a  #[1,2,3]
b = np.array([[1,2],[3,4]])
print b #[[1,2],[3,4]]
c = np.array([1,   3,  2,  5, 4,8],ndmin=4)
print c #[[[[1 3 2 5 4 8]]]]
d = np.array([1,2,3],dtype = complex)
print d #[1.+0.j 2.+0.j 3.+0.j]