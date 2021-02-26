import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import pandas as pd
#import numpy as np
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

#https://towardsdatascience.com/one-bubble-chart-comparing-9-data-visualization-tools-7308b893950a
data = pd.read_csv('cars-sample.csv')

plt.figure(figsize=(10,8))
colors = ("#f6938c", "#b5b639", "#cb91c0", "#4ebd94", "#45bced")

def attribute_color(manufacturer):
    colors = {
        'bmw':'#f6938c',
        'ford':'#b5b639',
        'toyota':'#cb91c0',
        'honda':'#4ebd94',
        'mercedes':'#45bced'
    }
    return colors.get(manufacturer, 'grey')

color_region = list()
numManu = len(data['Manufacturer'])
 
for manu in range(numManu):
    color_region.append(attribute_color(data['Manufacturer'][manu]))

fig = plt.scatter(x = data['Weight'], y = data['MPG'], s = (data['Weight']/30), c = color_region, alpha = 0.5)
ax = plt.axes()
plt.xlabel('Weight')
plt.ylabel('MPG')


plt.ylim(6, 46)
plt.xlim(1400, 5300)

ax.xaxis.set_major_locator(plt.MultipleLocator(1000))
ax.xaxis.set_minor_locator(plt.MultipleLocator(500))

ax.yaxis.set_major_locator(plt.MultipleLocator(10))
ax.yaxis.set_minor_locator(plt.MultipleLocator(5))

manufacturers = ['bmw', 'ford', 'toyota', 'honda', 'mercedes']
plt.savefig('pythonMatplotLib.png')


plt.show()
