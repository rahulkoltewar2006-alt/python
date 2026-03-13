Perform the following operations using Numpy:

a) Construct a Python program using NumPy to generate a 4x4 identity matrix. 
b) Develop a Python program to generate two 3x3 matrices filled with random integers (1 to 9), then perform matrix
addition and matrix multiplication

# Generate two 3x3 matrices with random integers from 1 to 9
matrix1 = np.random.randint(1, 10, (3,3))
matrix2 = np.random.randint(1, 10, (3,3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

# Matrix Addition
addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)

# Matrix Multiplication
multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)

[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]

 Develop a NumPy program to multiply a 5X3 matrix by a 3X2 matrix and create a product matrix, also print the product matrix. Take input data from user.

 import numpy as np

# Input for 5x3 matrix
print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    A.append(row)

A = np.array(A)

# Input for 3x2 matrix
print("\nEnter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input(f"Enter 2 elements for row {i+1}: ").split()))
    B.append(row)

B = np.array(B)

# Matrix multiplication
product = np.dot(A, B)

# Display matrices and result
print("\nMatrix A (5x3):")
print(A)

print("\nMatrix B (3x2):")
print(B)

print("\nProduct Matrix (5x2):")
print(product)