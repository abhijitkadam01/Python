import numpy as np

# Creating Arrays
arr1 = np.array([1, 2, 3, 4, 5])       # 1D array
arr2 = np.array([[1, 2], [3, 4]])      # 2D array

# Array Operations
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Sum:", arr1 + 5)               # Add scalar
print("Element-wise Addition:", arr1 + arr1)  # Add arrays

# Array Properties
print("Shape:", arr2.shape)
print("Data Type:", arr1.dtype)
print("Dimensions:", arr2.ndim)