# Print first element.
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[0])
print(arr[1])
print(arr[5])
print(arr[:])
print(arr[-1])
print(arr[1:])

# Print elements from index 2 to 6
arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1[2:6])

# Reverse an array.
print(arr1[::-1])

# Print alternate elements
print(arr1[::2])
print(arr[1::2])

# Create 3×3 matrix and print second row.
arr2 = np.array([[1,2,4],[5,6,7],[9,8,0]])
print(arr2)
print(arr2[0, :])
print(arr2[1, :])
print(arr2[2, :])

# Print third column from matrix.
print(arr2[:, 0])
print(arr2[:, 1])
print(arr2[:, 2])

arr2[0,0] =100
print(arr2)