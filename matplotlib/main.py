'''
Reference: https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html
'''

import matplotlib.pyplot as plt
import pandas as pd

# load data
data = pd.read_csv('../cars-sample.csv', header=None)
# remove NA value
index=data[3].notnull()
data=data[index]

Manufacturer = data[2][1:]
Weight = list(map(float, data[7][1:]))
MPG = list(map(float, data[3][1:]))

x = Weight
y = MPG
linear_Weight = [0.06*n-90 for n in Weight]
colors = []
for i in Manufacturer:
    if i == 'bmw':
        colors.append('#f8766d')
    elif i == 'ford':
        colors.append('#a3a500')
    elif i == 'honda':
        colors.append('#00bf7d')
    elif i == 'mercedes':
        colors.append('#00b0f6')
    elif i == 'toyota':
        colors.append('#e76bf3')
    else:
        continue

# set axes & grid
plt.rcParams['axes.facecolor'] = '#ececec'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.grid'] = True
plt.rcParams['axes.axisbelow'] = True
plt.rcParams['grid.color'] = "#fefefe"

# scatter plot
plt.title('A2 matplotlib')
plt.scatter(x, y, s=linear_Weight, c=colors, alpha=0.5)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()