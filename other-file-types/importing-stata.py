import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_stata('../_datasets/disarea.dta')

print(df.head())

pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of coutries')
plt.show()
