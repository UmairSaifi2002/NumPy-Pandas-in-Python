# Numpy array
import numpy as np
import time

# 1D array
array_1d = np.array([1,2,3,4])
print(array_1d)

# 2D array
array_2d = np.array([[1,2,3,4], [5,6,7,8]])
print(array_2d)

# -------------------------------------------------------------
# now we will see when we multiply a python list by 2
list = [1,2,3,4]
print(list*2) # [1, 2, 3, 4, 1, 2, 3, 4]

# now we will see when we multiply a numpy arrray by 2
np_array = np.array([1,2,3,4])
print(np_array*2) # [2 4 6 8]

# --------------------------------------------------------------
# we will se the time taken by python to create a list
# start = time.time()
# py_list = [i*2 for i in range(1000000)]
# print(f'\nPython list operation time : {time.time()-start}') # Python list operation time : 0.12753582000732422

# start = time.time()
# numpy_list = np.arange(1000000)*2
# print(f'\nPython list operation time : {time.time()-start}') # Python list operation time : 0.008434057235717773

# --------------------------------------------------------------
# Now we will learn about how to creat matrices in numpy
# first see about zeroes matrices
zero = np.zeros((2,3))
print(f'A Numpy Zeros Matrices with 2 rows and 3 columns \n{zero}')

# now we will see how to create ones matice's in numpy
ones = np.ones((3,2))
print(f'A Numpy Ones Matrices with 3 rows and 2 columns \n{ones}')

# now if we want to create a matrices of a particular number so it is ony possible in numpy
# let's supppose we have to create a matrices of 3 with 3 rows and 3 columns
full = np.full((3,3), 3)
print(f'A Numpy Matrices of "3" with 3 rows and 3 columns \n{full}')

# now if we required to create a random matrices
# so i have the solution stick to it
random_matrices = np.ceil(np.random.random((2,2))*10)
print(f'A Random Numpy Matrices with 2 rows and 2 columns \n{random_matrices}')


