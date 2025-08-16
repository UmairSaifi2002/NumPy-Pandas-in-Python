import numpy as np

# today i will learn about the Filter in numpy

# Filter
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_number = numbers[numbers % 2 == 0]
print(f'Even Numbers : \n{even_number}')

#---------------------------------------------------------------------
# Filter with mask
mask = numbers % 2 != 0
print(f'ODD numbers : \n{numbers[mask]}')

# #---------------------------------------------------------------------
# Fancy indexing vs np.where()




