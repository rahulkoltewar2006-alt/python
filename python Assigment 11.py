1: Import sales data of a Cosmetic Company. Analyze it through following ways with visualization using Matplotlib:
a) Read the total profit of all the months and visualize it using a Line Plot.
b) Read all product sales data and show it using a Multiline Plot. c) Read face cream and face wash product t sales sales data data and and show it
using the Bar chart.
d) Calculate total sale data for last year for each product and show it using a Pie chart.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales_data.csv")

# a) Line Plot - Total Profit per Month
plt.figure()
plt.plot(data['month'], data['total_profit'], marker='o')
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()


# b) Multiline Plot - All Product Sales
plt.figure()
plt.plot(data['month'], data['facecream'], label='Face Cream')
plt.plot(data['month'], data['facewash'], label='Face Wash')
plt.plot(data['month'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month'], data['shampoo'], label='Shampoo')
plt.plot(data['month'], data['moisturizer'], label='Moisturizer')

plt.title("Product Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()


# c) Bar Chart - Face Cream & Face Wash
plt.figure()
x = range(len(data['month']))

plt.bar(x, data['facecream'], width=0.4, label='Face Cream')
plt.bar([i + 0.4 for i in x], data['facewash'], width=0.4, label='Face Wash')

plt.xticks([i + 0.2 for i in x], data['month'])
plt.title("Face Cream and Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()


# d) Pie Chart - Total Sales per Product (Yearly)
total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Distribution (Yearly)")
plt.show()

Import a dataset of new recruitments in companies such as Microsoft, Google, Amazon, IBM, Deliotte,
Capmemini, ATOS Origin, Amdocs etc.
Generate & visualize reports of new recruitments using:
a) Bar Chart
b) Pie Chart
c) Customize Pie Chart
d) Doughnut Chart
Compare the new recruitments in IBM & Amdocs using visualization.

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("recruitment_data.csv")

companies = data['Company']
recruitments = data['Recruitments']

# a) Bar Chart
plt.figure()
plt.bar(companies, recruitments)
plt.title("New Recruitments in Companies")
plt.xlabel("Companies")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=45)
plt.show()


# b) Pie Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()


# c) Customized Pie Chart
plt.figure()
explode = [0, 0.1, 0, 0, 0, 0, 0, 0]  # Highlight Google
plt.pie(recruitments, labels=companies, autopct='%1.1f%%',
        explode=explode, shadow=True)
plt.title("Customized Pie Chart (Highlight Google)")
plt.show()


# d) Doughnut Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0,0), 0.5, fc='white')
plt.gca().add_artist(centre_circle)
plt.title("Doughnut Chart of Recruitments")
plt.show()


# e) Comparison: IBM vs Amdocs
ibm = data[data['Company'] == 'IBM']['Recruitments'].values[0]
amdocs = data[data['Company'] == 'Amdocs']['Recruitments'].values[0]

plt.figure()
plt.bar(['IBM', 'Amdocs'], [ibm, amdocs])
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.ylabel("Recruitments")
plt.show()

output:
Company,Recruitments
Microsoft,120
Google,150
Amazon,180
IBM,90
Deloitte,110
Capgemini,140
ATOS Origin,80
Amdocs,70