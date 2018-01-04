# Pandas dataframes are more like excel sheets

import numpy as np
import pandas as pd

random_data = np.random.randn(2, 3)
x_index = ['Criminal Ratio', 'Education Ratio']
y_index = ['Tamilnadu', 'Kerala', 'Andra']

df = pd.DataFrame(random_data, x_index, y_index)
print(df)

# Creating a new column
df['Karnataka'] = df['Kerala'] + df['Andra']
print(df)

# Dropping a column in dataframes
df.drop('Karnataka', axis = 1, inplace = True)
print(df)

# MultiIndex DataFrame
outside = ['G1', 'G2']
inside = [1,2,3,1,2,3]
raw_index = list(zip(outside, inside))
row_index = pd.MultiIndex.from_tuples(raw_index)            # MultiIndex Generation
column_index = ['A', 'B']

multi_df = pd.DataFrame(np.random.randn(6, 2))
print(multi_df)
