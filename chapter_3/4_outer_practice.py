import numpy as np

# Practice problems for calculating the outer product (section 3.6)

# Problem a
v1 = np.array([-1, 1])
v2 = np.array([2, 3])

r1 = np.outer(v1, v2)

print('Answer a:', r1)

# Problem b
v3 = np.array([4, 6])
v4 = np.array([2, 3])

r2 = np.outer(v3, v4)

print('Answer b:', r2)

# Problem c
v5 = np.array([-1, 0, 1])
v6 = np.array([1, 2, 3])

r3 = np.outer(v5, v6)

print('Answer c:', r3)

# Problem d
v7 = np.array([1, 3, 5, 7])
v8 = np.array([0, 1, 1, 0])

r4 = np.outer(v7, v8)

print('Answer d:', r4)
