import pandas as pd

# Step 2: Import the dataset
url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv"
drinks = pd.read_csv(url)

beer_consumption = drinks.groupby('continent')['beer_servings'].mean()
print("Average beer consumption per continent:")
print(beer_consumption)


max_beer_continent = beer_consumption.idxmax()
print("\nContinent that drinks the most beer on average:", max_beer_continent)

wine_stats = drinks.groupby('continent')['wine_servings'].describe()
print("Wine consumption statistics per continent:")
print(wine_stats)

# Step 6: Print the mean alcohol consumption per continent for every column
mean_alcohol_consumption = drinks.groupby('continent').mean(numeric_only=True)
print("Mean alcohol consumption per continent:")
print(mean_alcohol_consumption)

# Step 7: Print the median alcohol consumption per continent for every column
median_alcohol_consumption = drinks.groupby('continent').median(numeric_only=True)
print("Median alcohol consumption per continent:")
print(median_alcohol_consumption)

# Step 8: Print the mean, min, and max values for spirit consumption
spirit_stats = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])
print("Spirit consumption statistics per continent:")
print(spirit_stats)