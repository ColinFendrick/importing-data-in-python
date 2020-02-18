import numpy as np

file = '../_datasets/digits_header.txt'

data = np.loadtxt(file, delimiter='\t', skiprows=1, usecols=[0, 2])
print(data)
