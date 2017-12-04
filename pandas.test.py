import pandas as pd
import numpy
# creating a python dictionary for creating the dataframe

name = ['Athul', 'Aswini', 'Mohan', 'Srini', 'Rubanraj']
age = [25, 23, 35, 23, 22]
role = ['frontend', 'testing', 'manager', 'frontend', 'data scientist']
d = {
    'name': pd.Series(name, index=['a', 'b', 'c', 'd', 'e']),
    'age': pd.Series(age, index=['a', 'b', 'c', 'd', 'e']),
    'role': pd.Series(role, index=['a', 'b', 'c', 'd', 'e'])
}

df = pd.DataFrame(d)

print(df)

# getting mean value for each row
print(df['age'].apply(numpy.mean))

print(df['age'].applymap(lambda x: x >= 1))
