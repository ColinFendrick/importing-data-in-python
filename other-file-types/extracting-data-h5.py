# Import packages
import numpy as np
import h5py
import matplotlib.pyplot as plt

file = '../_datasets/LIGO_data.hdf5'
data = h5py.File(file, 'r')


group = data['strain']

for key in group.keys():
    print(key)

strain = data['strain']['Strain'].value

num_samples = 10000
time = np.arange(0, 1, 1/num_samples)

plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()
