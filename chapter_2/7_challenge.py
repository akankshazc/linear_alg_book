import numpy as np
import matplotlib.pyplot as plt

# Code Challenge 1

# create a 2D vector
v = np.array([1, 2])

# plot the vector
plt.plot([0, v[0]], [0, v[1]], 'r', label='v')

for i in range(10):
    s = np.random.randn()
    sv = s*v
    plt.plot([0, sv[0]], [0, sv[1]], 'b', label='sv')

plt.grid()
plt.axis([-4, 4, -4, 4])

plt.show()
