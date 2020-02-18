import numpy as np
import matplotlib.pyplot as plt

file = '../_datasets/seaslug.txt'

data = np.loadtxt(file, delimiter='\t', dtype=str)
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
