import numpy as np
import matplotlib.pyplot as plt

# Data Set is here for some practice
# Data Structur : [restaurant_id, year_1_sales, year_2_sales, year_3_sales, year_4_sales]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000], # Paradise Biryani
    [2, 160000, 190000, 230000, 260000], # Karachi Biryani
    [3, 170000, 200000, 240000, 270000], # Biryani House
    [4, 180000, 210000, 250000, 280000], # Biryani King
    [5, 190000, 220000, 260000, 290000]  # Biryani Palace
])

print(f'{sales_data.shape}')

print(f'Fetching the first row of the array : \n{sales_data[0]}')

print(f'Fetching the first column of the array : \n{sales_data[:, 0]}')

print(f'Fetching the first three rows of the array : \n{sales_data[:3]}')

print(f'Fetching the sales columns of the array : \n{sales_data[:, 1:]}')

# Total Sales per year
print(f'Total Sales per year : \n{np.sum(sales_data[:,1:], axis=0)}')

# Minimum Sales per restuarent
# here we are using axis=1 to get the minimum sales for each restaurant across all years
# axis=1 means we are looking across the columns for each row
print(f'Minimum Sales per restuarent : \n{np.min(sales_data[:,1:], axis=1)}')

# Maximum Sales per year
print(f'Maximum Sales per year : \n{np.max(sales_data[:,1:], axis=0)}')

# Average Sales per restuarent
print(f'Average Sales per restuarent : \n{np.mean(sales_data[:,1:], axis=1)}')

# cummeulative sales for each restaurant
cumsum = np.cumsum(sales_data[:,1:], axis=1)
print(f'Cumulative Sales for each restaurant : \n{cumsum}')

plt.figure(figsize=(10, 6))
plt.plot(np.mean(cumsum, axis=0))
plt.title('Average Cumulative Sales Over Years')
plt.xlabel('Years')
plt.ylabel('Average Cumulative Sales')
plt.grid(True)
plt.show()

