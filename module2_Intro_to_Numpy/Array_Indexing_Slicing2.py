# in this we will learn about the numpy array list indexing and slicing
import numpy as np

list1 = np.array([1,2,3,4,5,6,7,8,9,10])

# indexing
# accessing the element at index 3
element = list1[3]
print(f'Original list: {list1}') # Original list: [ 1  2  3  4  5  6  7  8  9 10]
print(f'Element at index 3 is: {element}')  # Element at index 3 is: 4

# Slicing
# accessing elements from index 2 to 5 (exclusive)
sliced_elelment = list1[2:5]
print(f'Sliced eleement from index 2 to 5 is: {sliced_elelment}')  # Sliced eleement from index 2 to 5 is: [3 4 5]

# Reshaping
# reshaping the numpy array to 2D with 2 rows and 5 columns
reshaped_array = list1.reshape(5, 2)
print(f'Reshaped array to 2D with 2 rows and 5 columns: \n{reshaped_array}') # Reshaped array to 2D with 2 rows and 5 columns: 
# using reshape function we can reshape the data in the numpy array

