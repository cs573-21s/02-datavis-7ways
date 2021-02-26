import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))


csv_data = pd.read_csv('matplotlib/cars-sample.csv')
Weight = csv_data['Weight']
Mpg = csv_data['MPG']


def cars_Pating():
    color = []
    for Manufactor in csv_data['Manufacturer']:
        if Manufactor == 'ford':
            color.append('#cacb8a')
        elif Manufactor == 'bmw':
            color.append('#f3b8b4')
        elif Manufactor == 'mercedes':
            color.append('#98d8f9')
        elif Manufactor == 'toyota':
            color.append('#edb0f2')
        elif Manufactor == 'honda':
            color.append('#82d5b1')
    return color


def circle_Sizing():
    Size = []
    max_Size = 100
    min_Size = 40
    for cars in Weight:
        Size.append((cars - Weight.min())*(max_Size-min_Size) /
                    (Weight.max()-Weight.min())**0.8)
    return Size


cars_Size = circle_Sizing()
cars_color = cars_Pating()


fig, ax = plt.subplots()
ax.scatter(Weight, Mpg, c=cars_color, alpha=0.5, s=cars_Size)

ax.set_xlabel('Weight')
ax.set_ylabel('MPG')
plt.xticks(np.arange(2000, 6000, 1000))
plt.yticks(np.arange(10, 50, 10))

plt.show()
