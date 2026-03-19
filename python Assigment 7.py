Create a Menu Driven application "CALC" by implemnting different functions for the following basic operations: 
a) Addition 
b) Subtraction
c) Multiplication
d) Division
e) Modulus

# Functions for operations
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error! Division by zero not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Modulus by zero not allowed."
    return a % b


# Main program (Menu Driven)
while True:
    print("\n------ CALC MENU ------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 6:
        print("Exiting CALC... Thank you!")
        break

    if choice in [1, 2, 3, 4, 5]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", addition(a, b))
        elif choice == 2:
            print("Result:", subtraction(a, b))
        elif choice == 3:
            print("Result:", multiplication(a, b))
        elif choice == 4:
            print("Result:", division(a, b))
        elif choice == 5:
            print("Result:", modulus(a, b))
    else:
        print("Invalid choice! Please try again.")

Output:
------ CALC MENU ------
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus
6. Exit

Enter your choice: 1
Enter first number: 8
Enter second number: 2
Result: 10.0

Enter your choice: 4
Enter first number: 8
Enter second number: 2
Result: 4.0

Enter your choice: 5
Enter first number: 8
Enter second number: 3
Result: 2.0

Create a Menu Driven program for showing details of a Bank Account by implementaing different functions for the following: 
a) Display the current Balance
b) Mechanism to Deposit an amoun
c) Mechanism to Withdraw an amount

# Initial Balance
balance = 1000.0

# Functions
def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully!")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print("Amount Withdrawn Successfully!")


# Menu Driven Program
while True:
    print("\n------ BANK MENU ------")
    print("1. Display Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        display_balance()

    elif choice == 2:
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == 3:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)

    elif choice == 4:
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice! Try again.")

Output:
------ BANK MENU ------
1. Display Balance
2. Deposit Amount
3. Withdraw Amount
4. Exit

Enter your choice: 1
Current Balance: 1000.0

Enter your choice: 2
Enter amount to deposit: 500
Amount Deposited Successfully!

Enter your choice: 1
Current Balance: 1500.0

Enter your choice: 3
Enter amount to withdraw: 700
Amount Withdrawn Successfully!

Enter your choice: 1
Current Balance: 800.0