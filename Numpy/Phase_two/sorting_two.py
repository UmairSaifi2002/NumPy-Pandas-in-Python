import numpy as np

#---------------------------------------------------------------------
# sorting in one-dimensional array
unsorted = np.array([3,4,1,5,1,2,6,3,9,7])
sorted = np.sort(unsorted)
print(f'Sorted array :\n{sorted}')


#---------------------------------------------------------------------
# sorting in  a two-dimensional array
unsorted_2d_array = np.array([[1,2],[3,1],[8,2],[6,1]])
sorted_2d_array = np.sort(unsorted_2d_array)
print(f'Sorted 2D Array : \n{sorted_2d_array}')






