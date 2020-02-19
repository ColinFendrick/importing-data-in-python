import numpy as np
import h5py

file = '../_datasets/LIGO_data.hdf5'

data = h5py.File(file, 'r')
print(type(data))

for key in data.keys():
    print(key)
