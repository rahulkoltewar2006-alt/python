Task 1
# Pattern 1
print("Pattern 1")
print("1")
print("2")
print("**")

# Pattern 2
print("\nPattern 2")
for i in range(2):
    for j in range(i+2):
        if j % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()

# Pattern 3
print("\nPattern 3")
num = 4
print(num)
num += 4
for i in range(3):
    print(num, end=" ")
    num += 2
print()
print(num)
num += 2
for i in range(3):
    print(num, end=" ")
    num += 2
print()

# Pattern 4
print("\nPattern 4")
for i in range(4):
    print("*", end="")
print()

# Pattern 5
print("\nPattern 5")
for i in range(2,6):
    for j in range(1,i+1):
        print(j, end="")
    print()

# Pattern 6
print("\nPattern 6")
for i in range(2,6):
    for j in range(i):
        print(i, end="")
    print()

# Pattern 7
print("\nPattern 7")
for i in range(2,6):
    for j in range(i,0,-1):
        print(j, end="")
    print()

# Pattern 8
print("\nPattern 8")
for i in range(5):
    print("*", end="")
print()

# Pattern 9
print("\nPattern 9")
for i in range(4,6):
    for j in range(i):
        if j % 2 == 0:
            print(1, end="")
        else:
            print(0, end="")
    print()

    Task 3
    The included code stub will read an integer n , from STDIN.
Without using any string methods, try to print the following:
123…….n
Note that &quot;……&quot; represents the consecutive values in between.

n = int(input())

for i in range(1, n + 1):
    print(i, end="")
   Task 4
    Construct a program to print the following pattern on the screen:
* * * * *
* * * *
* * *
* *
*

rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

    Task 5

    rows = 5
for i in range(rows):
    # Print leading spaces
    print(' ' * (rows - i - 1), end='')
    # Print stars
    print('*' * (2 * i + 1))
    Task 6

    Prime Number Finder
Write a program that finds and prints all the prime numbers between two numbers
entered by the user. Use a while loop to take input and validate it, and a for loop
to check for primality.

# Prime Number Finder

# Input with validation using while loop
while True:
    start = int(input("Enter the first number: "))
    end = int(input("Enter the second number: "))
    
    if start < end:
        break
    else:
        print("First number must be smaller than the second number. Try again.")

print("Prime numbers between", start, "and", end, "are:")

# Check for prime numbers using for loop
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)