# 4. Create two arrays A and B of shape (3, 3) with random integers. Perform and print the following:

import numpy as np
A = np.random.randint(1, 10, size=(3, 3))
B = np.random.randint(1, 10, size=(3, 3))

# a) Element-wise addition and multiplication.

elementwise_addition = A + B
elementwise_multiplication = A * B

# b) Calculate the square root of all elements in A.

sqrt_A = np.sqrt(A)

# c) Compute the matrix multiplication of A and B.

matrix_multiplication = np.dot(A, B)
print("Matrix multiplication of A and B:\n", matrix_multiplication)