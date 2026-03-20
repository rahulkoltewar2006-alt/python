Create a class Employee inherits it into another class Manager. Add methods to get input & print information
of employees. Consider the attributes name, age, salary, address etc. process the information of 10 managers

# Base class
class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.salary = 0
        self.address = ""

    def get_input(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


# Derived class
class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.department = ""

    def get_input(self):
        super().get_input()
        self.department = input("Enter Department: ")

    def display(self):
        super().display()
        print("Department:", self.department)
        print("-" * 30)


# Main program
managers = []

print("Enter details of 10 Managers:\n")

for i in range(10):
    print(f"\nManager {i+1}:")
    m = Manager()
    m.get_input()
    managers.append(m)

print("\n--- Manager Details ---\n")

for m in managers:
    m.display()

output:
Enter details of 10 Managers:


Manager 1:
Enter Name: Rahul
Enter Age: 21
Enter Salary: 50000
Enter Address: Pune
Enter Department: HR

Manager 2:
Enter Name: Amit
Enter Age: 30
Enter Salary: 60000
Enter Address: Mumbai
Enter Department: Finance

Manager 3:
Enter Name: Neha
Enter Age: 28
Enter Salary: 55000
Enter Address: Nashik
Enter Department: IT

... (similar input continues up to Manager 10)


Manager Details

Name: Rahul
Age: 21
Salary: 50000.0
Address: Pune
Department: HR

Name: Amit
Age: 30
Salary: 60000.0
Address: Mumbai
Department: Finance

Name: Neha
Age: 28
Salary: 55000.0
Address: Nashik
Department: IT


Create a Library Management System n with with the following mechanisms
a) Design classes for Book, Member, and Library. 
b) Implement t methods me for adding books, lending books to members, returning books, and displaying book information.
C) Create a menu-driven interface for the library management system.

# Book Class
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


# Member Class
class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)


# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully!")

    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        member = Member(member_id, name)
        self.members.append(member)
        print("Member added successfully!")

    def lend_book(self):
        book_id = input("Enter Book ID to lend: ")
        member_id = input("Enter Member ID: ")

        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    for member in self.members:
                        if member.member_id == member_id:
                            book.is_issued = True
                            member.borrowed_books.append(book.title)
                            print("Book issued successfully!")
                            return
                    print("Member not found!")
                    return
                else:
                    print("Book already issued!")
                    return
        print("Book not found!")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        member_id = input("Enter Member ID: ")

        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    for member in self.members:
                        if member.member_id == member_id:
                            if book.title in member.borrowed_books:
                                book.is_issued = False
                                member.borrowed_books.remove(book.title)
                                print("Book returned successfully!")
                                return
                    print("Member not found or book not borrowed by member!")
                    return
                else:
                    print("Book was not issued!")
                    return
        print("Book not found!")

    def display_books(self):
        if not self.books:
            print("No books in library.")
        else:
            print("\n--- Book List ---")
            for book in self.books:
                book.display()


# Main Menu
library = Library()

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Lend Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        library.add_book()
    elif choice == '2':
        library.add_member()
    elif choice == '3':
        library.lend_book()
    elif choice == '4':
        library.return_book()
    elif choice == '5':
        library.display_books()
    elif choice == '6':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")

output:

===== Library Menu =====
1. Add Book
2. Add Member
3. Lend Book
4. Return Book
5. Display Books
6. Exit
Enter your choice: 1

Enter Book ID: B101
Enter Title: Python Basics
Enter Author: John Smith
Book added successfully!

===== Library Menu =====
Enter your choice: 1

Enter Book ID: B102
Enter Title: Data Structures
Enter Author: Raj Patel
Book added successfully!

===== Library Menu =====
Enter your choice: 2

Enter Member ID: M01
Enter Member Name: Rahul
Member added successfully!

===== Library Menu =====
Enter your choice: 3

Enter Book ID to lend: B101
Enter Member ID: M01
Book issued successfully!

===== Library Menu =====
Enter your choice: 5

--- Book List ---
ID: B101, Title: Python Basics, Author: John Smith, Status: Issued
ID: B102, Title: Data Structures, Author: Raj Patel, Status: Available

===== Library Menu =====
Enter your choice: 4

Enter Book ID to return: B101
Enter Member ID: M01
Book returned successfully!

===== Library Menu =====
Enter your choice: 5

--- Book List ---
ID: B101, Title: Python Basics, Author: John Smith, Status: Available
ID: B102, Title: Data Structures, Author: Raj Patel, Status: Available

===== Library Menu =====
Enter your choice: 6
Exiting program...