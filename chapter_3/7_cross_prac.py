import numpy as np

# Practice problems for cross product (section 3.8)

# Problem a
v1 = np.array([5, 3, 4])
v2 = np.array([-2, 1, -1])

r1 = np.cross(v1, v2)

print("Problem a:", r1)

# Problem b
v3 = np.array([1, 1, 1])
v4 = np.array([2, 2, 2])

r2 = np.cross(v3, v4)

print("Problem b:", r2)

# Problem c
v5 = np.array([1, 0, 0])
v6 = np.array([0, 1, 0])

r3 = np.cross(v5, v6)

print("Problem c:", r3)

# Problem d
v7 = np.array([1302, 1403])
v8 = np.array([3, 5])

# gives error because cross product is only defined for 3D vectors
# r4 = np.cross(v7, v8)
