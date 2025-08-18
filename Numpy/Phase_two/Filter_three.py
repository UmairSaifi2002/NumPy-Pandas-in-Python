import numpy as np

# today i will learn about the Filter in numpy

# Filter
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_number = numbers[numbers % 2 == 0]
print(f'Even Numbers : \n{even_number}')

# -----------------------------------------------------------------------
# Filter with mask
mask = numbers % 2 != 0
print(f'ODD numbers : \n{numbers[mask]}')

# -----------------------------------------------------------------------
# Fancy indexing vs np.where()
# Fancy indexing
indices = [0, 2, 4]
print(f'Fancy indexing -numbers[indices]- : \n{numbers[indices]}')

# Where
where_result = np.where(numbers > 5) # it stores the indexes of the element's which is greater than 5
print(f'where function in numpy : {numbers[where_result]}')

# -----------------------------------------------------------------------
# condition array
# it is important
condition_array = np.where(numbers > 5)
print(condition_array) # it also stores the indexes of the element is greater than 5

condition_array_one = np.where(numbers > 5, numbers * 4, numbers)
print(f'Condition array with operations -np.where(numbers > 5, numbers * 4, numbers)- : \n{condition_array_one}')




