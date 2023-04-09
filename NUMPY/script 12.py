# write a program to convert a list of numeric value into one-dimensional.
import numpy as np
# create a list of numeric values
lst = [12.23, 13.32, 100, 36.32]
print("Original List:", lst)
# convert the list to a one-dimensional NumPy array
arr = np.array(lst)
print("One-dimensional NumPy array:", arr)
# print the dimension, size, and memory usage of the array
print("Dimension of the array:", arr.ndim)
print("Size of each element in the array:", arr.itemsize)
print("Size of the array in memory:", arr.size * arr.itemsize, "bytes")
