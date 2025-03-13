import pandas as pd

food = pd.read_csv('food_data.tsv', sep='\t')

food.head() #step 4

#number of observations in the dataset:
num_observations = food.shape[0]
print("Number of observations:", num_observations)

#number of columns in the datsset
num_columns = food.shape[1]
print("Number of columns:", num_columns)


#name of all columns
print("Column names:", food.columns.tolist())

#name of the 105th column
name_105th_column = food.columns[104] 
print("Name of the 105th column:", name_105th_column)

# type of the observations of the 105th column
type_105th_column = food.dtypes[104]
print("Type of the 105th column:", type_105th_column)

#how is data indexed.
print("Dataset index:", food.index)

#Product name of the 19th observation
product_name_19th = food.iloc[18]['product_name'] 
print("Product name of the 19th observation:", product_name_19th)