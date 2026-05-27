# Create a NumPy array from a Python list.
import numpy as np
arr = np.array([2,4,6,8,10])
print(arr)

# Create an array containing numbers from 1 to 20.
import numpy as np
arr1 = np.arange(1,21)
print(arr1)

# Create an array of zeros of size 10.
arr2 = np.zeros(10)
print(arr2)

# Create an array of ones of shape 3×3
arr3 = np.ones((3,3))
print(arr3)

# Create an identity matrix of size 4×4
arr4 = np.eye(4)
print(4)

# Create an array using arange()
arr5 = np.arange(1,2,0.1)
print(arr5)

arr55 = np.arange(30)
print(arr55)

arr51 = np.arange(1,5,1)
print(arr51)

# Create an array using linspace().
arr6 = np.linspace(1,2,5)
print(arr6)

# Find datatype of array elements.
arr7 = np.array([12,1,4,2])
print(arr7.dtype)

# Convert float array into integer array.
arr8 = np.array([0.1,0.2,0.3,0.4], dtype =int)
print(arr8.dtype)

arr81 = np.array([1.1,2.2,5.6,8.7])
print(arr81.astype(int))

# Create an array with boolean datatype
arr9 = np.array([1,3.5,7,12])
idx = arr9%2==0
print(idx)