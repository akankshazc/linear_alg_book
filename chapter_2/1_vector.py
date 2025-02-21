import numpy as np
import matplotlib.pyplot as plt

# create a vector
v = np.array([2, -1])

# plot the vector
plt.plot([0, v[0]], [0, v[1]])
plt.axis('square')
plt.axis([-3, 3, -3, 3])
plt.grid(True)
plt.show()
