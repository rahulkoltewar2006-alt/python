Create a Panda Dataframe script by reading a file "books.csv". The "books.csv" contains information regarding the books such as title, name of author, edition, publication year and publishing house, price. Create an application to perform the following operations:
a) Print the complete report of books in a Tabular form.
b) Print the list of available books of a gieyn author
c) Print the list of available books of a given publishing house
d) Print the Titles of cheapest & costliest book avaialble
e) Print the list by sorting based on the year of publication

import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("\n--- Complete Book Report ---")
print(df.to_string(index=False))

# b) Books by a given author
author_name = input("\nEnter author name: ")
books_by_author = df[df['Author'] == author_name]

print(f"\n--- Books by {author_name} ---")
print(books_by_author.to_string(index=False))

# c) Books by a given publishing house
publisher_name = input("\nEnter publishing house: ")
books_by_publisher = df[df['Publishing House'] == publisher_name]

print(f"\n--- Books by {publisher_name} ---")
print(books_by_publisher.to_string(index=False))

# d) Cheapest and costliest book
cheapest_book = df[df['Price'] == df['Price'].min()]
costliest_book = df[df['Price'] == df['Price'].max()]

print("\n--- Cheapest Book ---")
print(cheapest_book[['Title', 'Price']].to_string(index=False))

print("\n--- Costliest Book ---")
print(costliest_book[['Title', 'Price']].to_string(index=False))

# e) Sort by year of publication
sorted_books = df.sort_values(by='Publication Year')

print("\n--- Books Sorted by Publication Year ---")
print(sorted_books.to_string(index=False))

output: 
--- Complete Book Report ---
          Title       Author  Edition  Publication Year Publishing House  Price
  Python Basics   John Smith        1              2020   ABC Publishers    300
   Data Science     Jane Doe        2              2018   XYZ Publishers    450
Java Programming   John Smith        3              2022   ABC Publishers    500
  C Programming    Raj Patel        1              2015   LMN Publishers    250


  Create a table showing information about 5 states such as:

a) Name of the state
b) Area
c) Population
Generate the following reports:

a) Print the complete information of states
b) Print the name of the State having largest Area
c) Print the name of State having largest population
d) Create a mechanism to calculate the population density of States
e) Determine the name of State with highest population density
c) Print the name of State having largest population
d) Create a mechanism to calculate the population density of States e) Determine the name of State with highest population density

import pandas as pd

# Create DataFrame
data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Tamil Nadu", "Uttar Pradesh"],
    "Area": [307713, 196244, 342239, 130058, 240928],   # in sq km
    "Population": [124000000, 68000000, 81000000, 78000000, 240000000]
}

df = pd.DataFrame(data)

# a) Complete information
print("\n--- Complete State Information ---")
print(df.to_string(index=False))

# b) State with largest Area
largest_area = df.loc[df['Area'].idxmax()]
print("\nState with Largest Area:", largest_area['State'])

# c) State with largest Population
largest_population = df.loc[df['Population'].idxmax()]
print("State with Largest Population:", largest_population['State'])

# d) Calculate Population Density
df['Density'] = df['Population'] / df['Area']

print("\n--- Population Density ---")
print(df[['State', 'Density']].to_string(index=False))

# e) State with highest Density
highest_density = df.loc[df['Density'].idxmax()]
print("\nState with Highest Population Density:", highest_density['State'])

output:
--- Population Density ---
        State     Density
  Maharashtra   402.98
      Gujarat   346.55
    Rajasthan   236.68
   Tamil Nadu   599.75
Uttar Pradesh   995.32