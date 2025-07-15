import numpy as np

# square root
array = np.array([1,4,9,16,25,36,49,64,81,100])
sqrt = np.sqrt(array)
print(f'Square root of the numpy array: {sqrt}')  # Square root of the numpy array: [ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

#sin functioin
angles = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
result = np.sin(angles)
print(f'Sine of the angles in numpy array: {result}')  # Sine of the angles in numpy array: [ 0.  1.  0. -1.  0.]

# exponential function
exp_array = np.array([1,2,3,4,5,6,7,8,9,10])
exp_rresult = np.exp(exp_array)
print(f'Exponential of the numpy array: {exp_rresult}')  # Exponential of the numpy array: [2.71828183 7.3890561  20.08553692 54.59815003 148.4131591  403.42879349 1096.63315843 2980.95798704 8103.08392758 22026.46579481]
