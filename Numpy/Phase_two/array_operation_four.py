import numpy as np

# ------------------------------------------------------------------------
# array contcatintion in numpy
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

combined = np.concatenate((arr1, arr2))
print(combined)

# ------------------------------------------------------------------------
# array compatibility
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
print(f'Array compatibility -arr3.shape == arr4.shape- : {arr3.shape == arr4.shape}')

# ------------------------------------------------------------------------
# how to add two arrays
original = np.array([[1,2,3], [4,5,6]])
new_row = np.array([[7,8,9]])
# Adding a new row to the original array
# Using np.vstack to stack the original array with the new row
original_with_new = np.vstack((original, new_row))

print(f'Original array with new row added:\n{original_with_new}')

new_col = np.array([[7], [8]])
# Adding a new column to the original array
# Using np.hstack to stack the original array with the new column
original_with_new_col = np.hstack((original, new_col))

print(f'Original array with new column added:\n{original_with_new_col}')