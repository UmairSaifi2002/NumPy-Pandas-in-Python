import numpy as np
import matplotlib.pyplot as plt

vector1 = np.array([1,2,3,4,5])
vector2 = np.array([96,7,8,9,10])

print(f'Vector 1 + vector 2 : \n{vector1 + vector2}')

print(f'Vector 1 - vector 2 : \n{vector1 - vector2}')
print(f'Vector 1 * vector 2 : \n{vector1 * vector2}')

print(f' dot product of vector 1 and vector 2 : \n{np.dot(vector1, vector2)}')

angle = np.arccos(np.dot(vector1, vector2)/(np.linalg.norm(vector1)*np.linalg.norm(vector2))) 
print(f'Angle between vector 1 and vector 2 in radians : \n{angle}')
print(f'Angle between vector 1 and vector 2 in degrees : \n{np.degrees(angle)}')

# ---------------------------------------------------------------------------------------------------
# vectorize operations on a 2D array

restuarent_types = np.array(['Paradise Biryani', 'Karachi Biryani', 'Biryani House', 'Biryani King', 'Biryani Palace'])

vectorized_upper = np.vectorize(str.upper)
print(f'Vectorized Upper Case of Restuarent Types : \n{vectorized_upper(restuarent_types)}')



