import numpy as np

# Now we will see about the vector, matrix, tensor

# vector is a one-dimensional array
vector = np.array([1,2,3,4,5])
print(f'Vector or One-Dimensional array : \n{vector}')

# matix is a two-dimentional array
matrix = np.array([[1,2,3,4], [5,6,7,8]])
print(f'Matrix or Two-Dimensional array : \n{matrix}')

# Tensor is a Three or more Dimensional array
tensor = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f'Tensor a Multi-Dimensional Array : \n{tensor}')

# -----------------------------------------------------------------

# some basic properties of array or matrix or tensor

arr = np.array([[1,2,3], [4,5,6]])

print(f'Shape of arr : {arr.shape}')
print(f'Dimensions of arr : {arr.ndim}')
print(f'Size (Total number of elements is arr) of arr : {arr.size}')
print(f'Data Type of arr : {arr.dtype}')

#---------------------------------------------------------------------

# Reshapping of a array

original_array = np.arange(12)
print(f'Original Array :\n{original_array}')

reshaped_array = original_array.reshape(3,4)
print(f'Reshaped array in 3 rows and 4 columns :\n{reshaped_array}')

# if we want to flat the array again
flattened_array = reshaped_array.flatten()
print(f'Flattened array : \n{flattened_array}')

# intrviwerer asked about ravel method
# it returns view, instead of copy
ravaled_array = reshaped_array.ravel()
print(f'Ravel array : \n{ravaled_array}')

# Transpose of an array
transposed_array = reshaped_array.T
print(f'Transppose of an array :\n{transposed_array}')



