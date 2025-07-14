import numpy as np

list = [1,2,4,5,6,7,8,9,10]
numpy_array = np.array(list)

print(f'python list: {list}') # python list: [1, 2, 4, 5, 6, 7, 8, 9, 10]
print(f'Numpy list: {numpy_array}') # Numpy list: [ 1  2  4  5  6  7  8  9 10]

# creating the 2D numpy list 
# which helps dealing with the matrix and the tabular data
list2 = [[1,2,3],[4,5,6],[7,8,9]]
numpy_2d_array = np.array(list2)
print(f'2D Numpy list: {numpy_2d_array}') # 2D Numpy list: [[1 2 3] [4 5 6] [7 8 9]]

# creating a float 2D numpy list
list3 = [[1,2,3],[4,5,6],[7,8,9]]
numpy_float_array = np.array(list3, dtype=float)

print(f'Original list : {list3}')
print(f'Numpy float array list: {numpy_float_array}') # Numpy float array list: [[1. 2. 3.] [4. 5. 6.] [7. 8. 9.]]


