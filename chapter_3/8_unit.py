import numpy as np

# Code block 3.9

# define a vector
v = np.array([2, 5, 4, 7])

# get the vector's magnitude
vmag = np.linalg.norm(v)

# get the unit vector
vunit = v / vmag

# print the results
print(f'unit vector for vector {v} is {vunit}')

# confirm that the unit vector has magnitude 1
unit_mag = np.linalg.norm(vunit)

print(f'magnitude of unit vector is {unit_mag}')
