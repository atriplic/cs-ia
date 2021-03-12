import pandas as pd
cols = [0, 3]
df = pd.read_excel (r'sports_table_test.xlsx', usecols=cols)
print (df)