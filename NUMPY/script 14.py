# write a program to get the values and indices of the element that are bigger than10 in a array.
import numpy as np

# create a 2D array with random values
arr = np.random.randint(0, 20, size=(3, 4))
print("Array:\n", arr)

# get the indices and values of elements bigger than 10
indices = np.where(arr > 10)
values = arr[indices]

# print the indices and values
print("Indices of elements bigger than 10:", indices)
print("Values of elements bigger than 10:", values)
