# in this file we will learn how to creat and read existing file
import numpy as np

# creating a numpy array and saving it to a text file
array = np.array([[1,2,3],[4,5,6],[7,8,9]])
np.savetxt('data.text', array, delimiter=',')
np.save('data.npy', array)  # Saving as a binary file with .npy extension
print('Data saved to data.text file')

# reading the numpy array from the text file
loaded_array = np.loadtxt('data.text', delimiter=',')
print(f'Loaded array from file: \n{loaded_array}') # Loaded array from file: [[1. 2. 3.] [4. 5. 6.] [7. 8. 9.]]

loaded_array_binary = np.load('data.npy')  # Reading from the binary file
print(f'Loaded array from binary file: \n{loaded_array_binary}')  # Loaded array from binary file: [[1 2 3] [4 5 6] [7 8 9]]
