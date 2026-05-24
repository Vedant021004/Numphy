import numpy as np
arr = np.array([1.1, 2.2, 3.3], dtype = int)

print(arr)

# using fancy function to extract the even number
arr1 = np.array([1,2,3,4,5,6,7,8,9])
print(arr1[arr1%2==0])
idx = [1,3,5,7]
print(arr1[idx])

# Reshape a 1D array of size 9 into a 3×3 matrix.
arr2 = np.array([1,2,3,4,5,6,7,8,9])
print(arr2)
print(arr2.reshape(3,3))


