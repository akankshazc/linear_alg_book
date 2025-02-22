import numpy as np

# Vector Addition and Subtraction (Practice problems in Section 2.5)

# a) v1 = [4,5,1,0] and v2 = [-4,-3,3,10]
v1 = np.array([[4, 5, 1, 0]])
v2 = np.array([[-4, -3, 3, 10]])

r1 = v1 + v2

print('Answer a:', r1)

# b) v3 = [4,5,0], v4 = [6,-4,60], and v5 = [2,-5,40]
v3 = np.array([[4], [2], [0]])
v4 = np.array([[6], [-4], [60]])
v5 = np.array([[2], [-5], [40]])

r2 = v3 - v4 + v5

print('Answer b:', r2)

# c) v6 = [1,0] and v7 = [1,2]
v6 = np.array([[1], [0]])
v7 = np.array([[1], [2]])

r3 = v6 + v7

print('Answer c:', r3)

# d) v8 = [2,2] and v9 = [3,4]
v8 = np.array([[2], [2]])
v9 = np.array([[3], [4]])

r4 = v8 - v9

print('Answer d:', r4)

# e) v10 = [-3,1] and v11 = [3,-1]
v10 = np.array([[-3], [1]])
v11 = np.array([[3], [-1]])

r5 = v10 + v11

print('Answer e:', r5)

# f) v12 = [1,4] and v13 = [2,8]
v12 = np.array([[1], [4]])
v13 = np.array([[2], [8]])

r6 = v12 + v13

print('Answer f:', r6)
