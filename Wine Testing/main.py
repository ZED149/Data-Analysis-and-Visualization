
# this program performs data analysis on a wine.csv file
# this file contains information about various wines

# starting from here

# importing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter


# main

# reading from file
df = pd.read_csv("wines.csv")

# answering questions

# 1. How many wines have been given a rating of 100 points?
wines_with_rating_100 = df.loc[df['points'] == 100]['name'].size
print(wines_with_rating_100)
print()

# 2. What is the name of most expensive wine?
name_of_most_expensive_wine = df.loc[df['price'].idxmax()]['name']
print(name_of_most_expensive_wine)

# 3. Calculate a new column where you show the ratings in a scale from 0 to 5. Floats are allowed.
df['new'] = df['points'] / 20
print(df['new'])

# 4. Create a price histogram of wines that cost less than 100.
price_histogram = df.loc[df['price'] < 100]
price_histogram.hist(column="price")
# price_histogram.plot()
# plt.show()

# 5. Plot price horizontally against points vertically. Do you think ratings increase by price?
df.plot(x='price', y='points', kind="scatter")
plt.show()
