import pandas as pd

file = '../_datasets/battledeath.xlsx'

xls = pd.ExcelFile(file)
df1 = xls.parse(0, skiprows=[0], names=['Country', 'AAM due to War (2002)'])

print(df1.head())
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])
print(df2.head())
