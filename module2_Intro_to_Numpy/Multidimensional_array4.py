# we will learn about multidimensional arrays using numpy
import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

print(f'2D Array:\n{array_2d}')  # 2D Array: [[1 2 3] [4 5 6] [7 8 9]]
print(f'3D Array:\n{array_3d}')  # 3D Array: [[[1 2] [3 4]] [[5 6] [7 8]]]

# some indexing in the multidimensional array
element_2d = array_2d[1, 2]  # Accessing element at row 1, column 2
print(f'Element at row 1, column 2 in 2D array: {element_2d}')  # Element at row 1, column 2 in 2D array: 6
element_3d = array_3d[1, 0, 1]  # Accessing element at depth 1, row 0, column 1
print(f'Element at depth 1, row 0, column 1 in 3D array: {element_3d}')  # Element at depth 1, row 0, column 1 in 3D array: 6

# slicing in the multidimensional array
sliced_2d = array_2d[0:2, 1:3]  # Slicing rows 0 to 1 and columns 1 to 2
print(f'Sliced 2D array (rows 0 to 1, columns 1 to 2):\n{sliced_2d}')  # Sliced 2D array: [[2 3] [5 6]]
sliced_3d = array_3d[:, 1, :]  # Slicing all depths, row 1, and all columns
print(f'Sliced 3D array (all depths, row 1, all columns):\n{sliced_3d}')  # Sliced 3D array: [[3 4] [7 8] [11 12]]
