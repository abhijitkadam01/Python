
import numpy as np

# Creating Arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Array Operations
print("Array 1:", A)
print("Array 2:", B)

result = np.dot(A, B)  # OR simply A @ B
print("Matrix Multiplication: ", result) 

# Reshaping the Array
reshaped_A = A.reshape(1, 4)  # Reshaping from (2,2) to (1,4)
reshaped_B = B.reshape(1, 4)  # Reshaping from (2,2) to (1,4)
print("Reshaped Array: ", np.concatenate((reshaped_A, reshaped_B), axis=1))

print("Reshaped Array: ", np.concatenate((reshaped_A, reshaped_B), axis=0))

