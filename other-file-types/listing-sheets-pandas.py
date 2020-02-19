import pandas as pd

file = '../_datasets/battledeath.xlsx'
xls = pd.ExcelFile(file)
print(xls.sheet_names)
