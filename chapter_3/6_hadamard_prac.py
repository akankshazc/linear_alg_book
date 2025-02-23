import numpy as np

# Practice problems for element wise vector product (section 3.7)

# Problem a
v1 = np.array([1, 3, 2])
v2 = np.array([-1, 1, -2])

r1 = v1 * v2

print("Answer a:", r1)

# Problem b
v3 = np.array([0, 0, 0])
v4 = np.array([np.pi, np.e**5, 2])

r2 = v3 * v4

print("Answer b:", r2)

# Problem c
v5 = np.array([1.3, 1.4, 3.2])
v6 = np.array([3, 5])

# will give error since broadcasting is not possible
# r3 = v5 * v6
