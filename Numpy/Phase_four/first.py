import numpy as np
import matplotlib.pyplot as plt

array1 = np.array([1, 2, 3, 4, 5])
array2 = np.random.random((3,3)) 
array3 = np.zeros((4, 4))

print(f'Array 1: {array1}')
print(f'Array 2: {array2}')

# if we want to save those array in a file
np.save('array1.npy', array1)
np.save('array2.npy', array2)
np.save('array3.npy', array3)

# if we want to load those array from a file
loaded_array1 = np.load('array1.npy')
loaded_array2 = np.load('array2.npy')
loaded_array3 = np.load('array3.npy')

# load image and display it
try:
    logo = np.load('numpy_logo.npy')
    # Display the image
    plt.figure(figsize=(10,5))
    plt.subplot(1, 2, 1)
    plt.imshow(logo)
    plt.title('Numpy Logo')
    plt.grid(False)
    plt.show()
    # Dark logo 
    dark_logo = 1 - logo
    np.save('dark_numpy_logo.npy', dark_logo)
    plt.subplot(1, 2, 1)
    plt.imshow(dark_logo)
    plt.title('Dark Numpy Logo')
    plt.grid(False)
    plt.show()
except FileNotFoundError:
    print("Image file not found.")

