import numpy as np

# genreating random numbers
random_numbers = np.random.rand(10)  # Generates 10 random numbers between 0 and 1
print(f'Random numbers between 0 and 1: {random_numbers}')  # Random

# generating random integers
random_integers = np.random.randint(1,100, size=10)
print(f'10 Random integers between 1 and 100: {random_integers}') # 10 Random integers between 1 and 100

# normal distribution
normal_distribution = np.random.randn(6)  # Generates 10 random numbers from a normal distribution
print(f'Random numbers from a normal distribution: {normal_distribution}')  # Random numbers from
