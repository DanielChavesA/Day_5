import pandas as pd

# Create an example dataframe about a fictional army
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

df=pd.DataFrame(raw_data)
print(df)

# Step 4: Set 'origin' as the index
df.set_index('origin', inplace=True)

print(df.columns)

print(df['veterans'])

print(df[['veterans', 'deaths']])

print("Column names:", df.columns.tolist())

result = df.loc[['Maine', 'Alaska'], ['deaths', 'size', 'deserters']]
print(result)

result = df.iloc[2:7, 2:6]
print(result)

result = df.iloc[4:]  
print(result)

result = df.iloc[:4]  
print(result)

result = df.iloc[:, 2:7]  
print(result)

result = df[df['deaths'] > 50]
print(result)

# Step 14: Select rows where df.deaths is greater than 500 or less than 50
result = df[(df['deaths'] > 500) | (df['deaths'] < 50)]
print(result)

result = df[df['regiment'] != 'Dragoons']
print(result)


result = df.loc[['Texas', 'Arizona']]
print(result)

result = df.loc['Arizona', 'deaths']
print("Third cell in the row named Arizona:", result)

result = df['deaths'].iloc[2]
print("Third cell in the 'deaths' column:", result)