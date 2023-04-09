# write a program to creaate a 3X3 matrix with values ranging from 2 to 10.
import numpy as np

# create a 3x3 matrix with values ranging from 2 to 10
arr = np.arange(2, 11).reshape(3, 3)
print("Array:\n", arr)

# print the dimension and size of the array
print("Dimension of the array:", arr.ndim)
print("Size of each element in the array:", arr.itemsize)
print("Size of the array in memory:", arr.size * arr.itemsize, "bytes")
