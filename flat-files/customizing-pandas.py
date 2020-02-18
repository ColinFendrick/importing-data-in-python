import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = '../_datasets/titanic_corrupt.txt'

data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

print(data.head())

pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
