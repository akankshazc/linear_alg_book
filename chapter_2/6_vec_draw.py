import numpy as np
import matplotlib.pyplot as plt

# Problem 2 of the Chapter Exercise

# Define the vectors
vectors = np.array([[2, 2], [6, 12], [-1, 0], [np.pi, np.e], [1, 2], [1, 2], [1, 2], [-1, -2], [-3, 0],
                    [-4, -2], [8, 4], [-8, -4]])

# Define the origins
origins = np.array([[0, 0], [1, -2], [4, 1], [0, 0], [0, 0],
                   [-3, 0], [2, 4], [0, 0], [1, 0], [0, 3/2], [1, 1], [8, 4]])

# extract components
x_start, y_start = origins[:, 0], origins[:, 1]
x_end, y_end = vectors[:, 0], vectors[:, 1]

# Plot the vectors
plt.quiver(x_start, y_start, x_end, y_end, scale_units='xy',
           angles='xy', scale=1, color='r')

# Set the limits
plt.xlim(-10, 10)
plt.ylim(-10, 10)

# Set the grid
plt.grid()

# Show the plot
plt.show()
