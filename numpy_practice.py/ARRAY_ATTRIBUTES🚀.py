# Find shape of array.
import numpy as np
arr1 = np.array([1,2,3,4])
print(arr1.shape)

arr11 = np.array([[1,2,3],[5,6,7]])
print(arr11.shape)

# Find dimensions of array.
mwaah = np.array([[[1,2,4],[1,2,3],[1,2,3]]])
print(mwaah)

print(mwaah.ndim)  #dimemsions

print(mwaah.shape)  #shape of the array

print(mwaah.size)  #total size of hte array 


print(mwaah.itemsize)  #per byte of an element


print(mwaah.nbytes)  # total data store by teh array
