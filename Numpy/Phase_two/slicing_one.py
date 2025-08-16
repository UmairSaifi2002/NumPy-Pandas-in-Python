import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])

print(f'Basic Slicing {arr[2:7]}')
print(f'With Steps {arr[1:8:2]}')
print(f'Negative Indexing {arr[-3]}')

#---------------------------------------------------------------------

# Slicing in two-dimensional array

arr1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(f'Specific Element : {arr1[1,2]}')
print(f'Entire Row : {arr1[1]}')
print(f'Entire Column : {arr1[:,1]}')


