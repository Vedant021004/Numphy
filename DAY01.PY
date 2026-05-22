import numpy as np
arr1 = np.array([1,2,3,4,5])

print(arr1)
print(arr1.ndim)

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr1.ndim)

# applying the operation on array
arr1 = arr1+5
print(arr1)
arr1 = arr1*3
print(arr1)

#printing the zero matirx of 3x3
np.zeros((3,3))
print(np.zeros((3,3)))