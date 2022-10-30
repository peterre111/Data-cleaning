import pandas as pd

df = pd.read_csv('data.csv')

df.dropna(inplace = True)

print(df.to_string())

#some rows have been removed (row 20, 24 and 30).

#These rows had cells with empty values.
