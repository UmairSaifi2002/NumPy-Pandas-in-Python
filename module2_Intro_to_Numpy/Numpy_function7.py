import numpy as np

list1 = np.array([1,2,3,4,5])
list2 = np.array([6,7,8,9,10])

sum = list1 + list2
product = list1 * list2

print(f'Sum of two numpy arrays: {sum}')  # Sum of two numpy arrays: [ 7  9 11 13 15]
print(f'Product of two numpy arrays: {product}')  # Product of two numpy arrays: [ 6 14 24 36 50]

a = np.array([[1,2,3],[4,5,6]])
b = np.array([1,0,1])

result = a + b
print(f'Adition of numpy array and scalar: {result}') # Addition of numpy array and scalar: [[2 2 4] [5 5 7]]

data = np.array([[10, 20], [30, 40], [50, 60]])
print(f'Sum of the data array is: {np.sum(data)}') # Sum of the data array is: 210
print(f'Mean of the data array is: {np.mean(data)}')  # Mean of the data array is: 35.0
print(f'Standard deviation of the data array is: {np.std(data)}')  # Standard deviation of the data array is: 17.07825127659933
print(f'Maximum value in the data array is: {np.max(data)}')  # Maximum value in the data array is: 60
print(f'Minimum value in the data array is: {np.min(data)}')  # Minimum value in the data array is: 10
print(f'Variance of the data array is: {np.var(data)}')  # Variance of the data array is: 292.85714285714283

# axis = 0 for column-wise operations, axis = 1 for row-wise operations

print(f'Max per column in the data array: {np.max(data, axis=0)}')  # Max per column in the data array: [50 60]
print(f'Min per column in the data array: {np.min(data, axis=0)}')  # Min per column in the data array: [10 20]
print(f'Max per row in the data array: {np.max(data, axis=1)}')  # Max per row in the data array: [20 40 60]
print(f'Min per row in the data array: {np.min(data, axis=1)}')  # Min per row in the data array: [10 30 50]

print(f'Sum per column in the data array: {np.sum(data, axis=0)}')  # Sum per column in the data array: [90 120]
print(f'Sum per row in the data array: {np.sum(data, axis=1)}')  # Sum per row in the data array: [30 70 110]
print(f'Mean per column in the data array: {np.mean(data, axis=0)}')  # Mean per column in the data array: [30. 40.]
print(f'Mean per row in the data array: {np.mean(data, axis=1)}')  # Mean per row in the data array: [15. 35. 55.]

# some new
arr = np.array([1,2,3,4,5,6,7,8,9,10])
mask = arr > 4
filtered_arr = arr[mask]
print(f'Filtered array with values greater than 4: {filtered_arr}')  # Filtered array with values greater than 4: [ 5  6  7  8  9 10]