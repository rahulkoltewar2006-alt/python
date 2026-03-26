1. Diamonds Dataframe:

     carat cut     color    clarity  depth  table  price    x      y       z

0    0.23  Ideal    E       S12      61.5   55.5   326     3.95    3.98     2.43
1    0.21  Premium  E       s11      59.8   61.0   326     3.89    3.84     2.31
2    0.23  Good     E       VS1      56.9   65.0   327     4.05    4.07     2.31
3    0.29  Premium  I       VS2      62.4   58.0   334     4.20    4.23     2.63
4    0.31  Good     J       SI2      63.3   58.0   335     4.34    4.35     2.75
Do following:
i) Calculate the mean of price for each cut of diamonds DataFrame given above.
ii) Print count of diamond, minimum and maximum price for each cut of diamonds in
above given DataFrame
Calculate and print average value of parameter x, y, and z separately.

import pandas as pd

# Creating the DataFrame
data = {
    "carat": [0.23, 0.21, 0.23, 0.29, 0.31],
    "cut": ["Ideal", "Premium", "Good", "Premium", "Good"],
    "color": ["E", "E", "E", "I", "J"],
    "clarity": ["SI2", "SI1", "VS1", "VS2", "SI2"],
    "depth": [61.5, 59.8, 56.9, 62.4, 63.3],
    "table": [55.0, 61.0, 65.0, 58.0, 58.0],
    "price": [326, 326, 327, 334, 335],
    "x": [3.95, 3.89, 4.05, 4.20, 4.34],
    "y": [3.98, 3.84, 4.07, 4.23, 4.35],
    "z": [2.43, 2.31, 2.31, 2.63, 2.75]
}

df = pd.DataFrame(data)

# i) Mean price for each cut
mean_price = df.groupby("cut")["price"].mean()
print("Mean price for each cut:\n", mean_price)

# ii) Count, Min and Max price for each cut
stats = df.groupby("cut")["price"].agg(["count", "min", "max"])
print("\nCount, Min and Max price for each cut:\n", stats)

# iii) Average values of x, y, z
avg_values = df[["x", "y", "z"]].mean()
print("\nAverage values of x, y, z:\n", avg_values)

cut
Good       331.0
Ideal      326.0
Premium    330.0

count   min   max
cut
Good         2   327   335
Ideal        1   326   326
Premium      2   326   334

x    4.086
y    4.094
z    2.486

Create a program that reads "employee.xlsx" file of Infosys Software Solutions which includes columns such as Employee ID, Employee Name, Depatment, Designation etc. Construct a program to print the following reports: 
a) Print the list of employees working for "Automotive" domain.
b) Print the details of an employee with employee ID given by an end user. 
d) Print the list of all the Developers of Infosys.

import pandas as pd

# Read Excel file
data = pd.read_excel("employee.xlsx")

# a) Employees in Automotive Domain
print("Employees working in Automotive Domain:")
auto_emp = data[data['Department'] == 'Automotive']
print(auto_emp)


# b) Search employee by ID
emp_id = int(input("Enter Employee ID: "))
emp_details = data[data['Employee ID'] == emp_id]

print("\nEmployee Details:")
if not emp_details.empty:
    print(emp_details)
else:
    print("Employee not found!")


# c) List of all Developers
print("\nList of Developers:")
developers = data[data['Designation'] == 'Developer']
print(developers)