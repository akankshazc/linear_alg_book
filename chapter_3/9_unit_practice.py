import numpy as np

# Practice problems for unit vectors (section 3.9)

# Problem a
v1 = np.array([1, 3])

v1_mag = np.linalg.norm(v1)

v1_unit = v1 / v1_mag

v1_unit_mag = np.linalg.norm(v1_unit)

print("Problem a")
print(
    f"The unit vector of {v1} is {v1_unit} and the magnitude of the unit vector is {v1_unit_mag}")

# Problem b
v2 = np.array([3, 4])

v2_mag = np.linalg.norm(v2)

v2_unit = v2 / v2_mag

v2_unit_mag = np.linalg.norm(v2_unit)

print("Problem b")
print(
    f"The unit vector of {v2} is {v2_unit} and the magnitude of the unit vector is {v2_unit_mag}")

# Problem c
v3 = np.array([6, -8])

v3_mag = np.linalg.norm(v3)

v3_unit = v3 / v3_mag

v3_unit_mag = np.linalg.norm(v3_unit)

print("Problem c")
print(
    f"The unit vector of {v3} is {v3_unit} and the magnitude of the unit vector is {v3_unit_mag}")

# Problem d
v4 = np.array([0.1, 0.2, 0.4, 0.2])

v4_mag = np.linalg.norm(v4)

v4_unit = v4 / v4_mag

v4_unit_mag = np.linalg.norm(v4_unit)

print("Problem d")
print(
    f"The unit vector of {v4} is {v4_unit} and the magnitude of the unit vector is {v4_unit_mag}")
