Develop a program that asks the user to enter a series of integers and and store them ina Tuple. Develop a program that asks the user to enter a series of integers and store them in a Tuple. Perform the following: a) Print the total number of items in the Tuple.

b) Print the last item in the Tuple.

c) Print the Tuple elements in reverse order.

d) Print Yes if the Tuple contains an integer 5 and No otherwise.

e) Remove the first and last items from the Tuple, sort the remaining items, and print the result.

# Take input from user
numbers = input("Enter integers separated by space: ")

# Convert input into tuple of integers
t = tuple(map(int, numbers.split()))

# a) Total number of items in the tuple
print("Total number of items:", len(t))

# b) Last item in the tuple
print("Last item in the tuple:", t[-1])

# c) Tuple elements in reverse order
print("Tuple in reverse order:", t[::-1])

# d) Check if tuple contains integer 5
if 5 in t:
    print("Yes")
else:
    print("No")

# e) Remove first and last items, sort remaining items
remaining = list(t[1:-1])   # remove first and last
remaining.sort()

print("Sorted tuple after removing first and last items:", tuple(remaining))
output:
Enter integers separated by space: 2 5 7 9 1 4

Total number of items: 6
Last item in the tuple: 4
Tuple in reverse order: (4, 1, 9, 7, 5, 2)
Yes
Sorted tuple after removing first and last items: (1, 5, 7, 9)


Create a program to store the Prices of sold items on a particular day of a shop in a Tuple.

Perform the following operations:

a) Print the total number of items sold

b) Print the price of cheapest item sold

c) Print the price of costliest item sold

d) Print the price list in ascending order

e) Print the number of costliest items sold on the day

# Take input from user
prices = input("Enter the prices of sold items separated by space: ")

# Convert input into tuple of integers
t = tuple(map(int, prices.split()))

# a) Total number of items sold
print("Total number of items sold:", len(t))

# b) Price of cheapest item
print("Cheapest item price:", min(t))

# c) Price of costliest item
print("Costliest item price:", max(t))

# d) Price list in ascending order
sorted_prices = tuple(sorted(t))
print("Prices in ascending order:", sorted_prices)

# e) Number of costliest items sold
costliest = max(t)
count_costliest = t.count(costliest)
print("Number of costliest items sold:", count_costliest)
output:
Enter the prices of sold items separated by space: 120 200 150 200 90

Total number of items sold: 5
Cheapest item price: 90
Costliest item price: 200
Prices in ascending order: (90, 120, 150, 200, 200)
Number of costliest items sold: 2