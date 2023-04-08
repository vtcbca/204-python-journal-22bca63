# write numpy program to create a new shape to an array without changing its data.
import numpy as np

# create a 3x2 array
arr = np.array([[1, 2], [3, 4], [5, 6]])

# reshape the array to 2x3 without changing its data
new_arr = arr.reshape(2, 3)

# print the original and reshaped arrays
print("Original array:\n", arr)
print("Reshaped array:\n", new_arr)
