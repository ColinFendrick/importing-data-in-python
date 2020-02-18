import numpy as np

file = '../_datasets/titanic.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file)

print(d[:3])
