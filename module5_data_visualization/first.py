import pandas as pd
import matplotlib.pyplot as plt

# data = {
#     'Day' : ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
#     'Sales' : [200, 220, 250, 275, 300, 320, 280]
# }

# df = pd.DataFrame(data)

# df.plot(kind = 'bar', x = 'Day', y = 'Sales',  color = 'skyblue', legend = False)

# plt.title('Weekly Sales Data')
# plt.xlabel('Days of the Week')
# plt.ylabel('Sales Amount')
# plt.show()

# # ----------- Advanced Visualization charts like histogram, scatter plot, and box plot ------------

# data1 = {
#     'Age' : [22, 25, 27, 30, 32, 35, 40, 45, 50, 55]
# }

# df1 = pd.DataFrame(data1)

# df1.plot(kind='hist', y='Age', bins=7, edgecolor='black')
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Frequency')

# plt.show()

# ---------------------------------------------------------------------------------------------------
data2 = {    
    'Height' : [150, 160, 165, 170, 175, 180, 185, 190, 195, 200],
    'Weight' : [50, 60, 65, 70, 75, 80, 85, 90, 95, 100]
}

df2 = pd.DataFrame(data2)

df2.plot(kind='scatter', x='Height', y='Weight', color='red')
plt.title('Height vs Weight Scatter Plot.')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.show()



