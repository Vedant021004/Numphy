import numpy as np
# arr = np.array([1.1, 2.2, 3.3], dtype = int)

# print(arr)

# # using fancy function to extract the even number
# arr1 = np.array([1,2,3,4,5,6,7,8,9])
# print(arr1[arr1%2==0])
# idx = [1,3,5,7]
# print(arr1[idx])

# # Reshape a 1D array of size 9 into a 3×3 matrix.
# arr2 = np.array([1,2,3,4,5,6,7,8,9])
# print(arr2)
# print(arr2.reshape(3,3))


#operations on an array of numpy
matrix = np.array([[[1,2,3],[4,5,6]]
                   ,[[7,8,9],[10,11,12]]])
# a = np.sum(matrix , axis = 0)
# print(a)
# b = np.sum(matrix , axis = 1)
# print(b)

# print(matrix.shape)

# matrix [1,:] = 0
# print(matrix)

first_col = matrix[:, 0]
flat2 = first_col.flatten()
print(flat2)

first_row = matrix[0, :]
flat1 = first_row.flatten()
print(flat1)

# Get the first row from each "sheet" in a 3D array
first_rows = matrix[:, 0, :]
flat = first_rows.flatten()
print(flat)


# changing the datatype of the array
arr = np.array([1.1,2.2,3.3,4.4])
print(arr.dtype)
print(arr.astype(int))

brr = np.array([0.1,0.2,0.3,0.4], dtype = int)
print(brr.dtype)
print(brr)


