# in this file we will learn about the basic functions in numpy

import numpy as np

list1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
list2 = np.array([10,20,30,40,50,60,70,80,90,100])

result1 = list1 + list2
result2 = list1 - list2
result3 = list1 * list2

print(f'Addition of two numpy arrays: {result1}')  # Addition of two numpy arrays: [11 22 33 44 55 66 77 88 99 110]
print(f'Subtraction of two numpy arrays: {result2}')  # Subtraction of two numpy arrays: [-9 -18 -27 -36 -45 -54 -63 -72 -81 -90]
print(f'Multiplication of two numpy arrays: {result3}')  # Multiplication of two numpy arrays: [ 10  40  90 160 250 360 490 640 810 1000]

# comparision
comparision = list1 > list2
print(f'Comparision of two numpy arrays: {comparision}')  

# scaler
scalar_addition = list1 + 5
print(f'Scalar addition of numpy array: {scalar_addition}')  # Scalar addition of numpy array: [ 6  7  8  9 10 11 12 13 14 15]
