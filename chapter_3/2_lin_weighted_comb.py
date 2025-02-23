import numpy as np

# Code block 3.3

# define the scalars
l1, l2, l3 = 1, 2, -3

# define the vectors
v1 = np.array([4, 5, 1])
v2 = np.array([-4, 0, -4])
v3 = np.array([1, 3, 2])

# calculate the linear weighted combination
v = l1*v1 + l2*v2 + l3*v3

# print the result
print(v)
