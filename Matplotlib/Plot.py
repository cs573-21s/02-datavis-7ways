import matplotlib.pyplot as plt
import matplotlib.colors
import numpy as np

# https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596
#https://www.pythonprogramming.in/customize-grid-color-and-style.html

data = np.genfromtxt('cars-sample.csv', delimiter=',', names=True)
dataColors = np.genfromtxt('cars-sample.csv', delimiter=',', names=True, dtype=None)['Manufacturer']


colorDict = {
    "bmw": "#F3B0AC",
    "ford": "#B7B74A",
    "honda": "#80D5B0",
    "mercedes": "#88CDF1",
    "toyota": "#7DCBF3"
}

color_map = [colorDict[color.strip('"')] for color in dataColors]

# Prepare a list of sizes that increases with values in val

sizevalues = [3*s//100 for s in data['Weight']]

# Draw a scatter plot of val points with sizes in sizevalues and
# colors in plotcolor
plt.scatter(data['Weight'], data['MPG'], s=sizevalues, c=color_map, alpha=0.5)


ax = plt.gca()
ax.set_facecolor('#ECECEC')

plt.setp(ax.get_xticklabels()[::2], visible=False)
plt.setp(ax.get_yticklabels()[::2], visible=False)

# Draw grid lines with red color and dashed style
plt.grid(color='white', linestyle='-', linewidth=0.7)
plt.xlabel("Weight")
plt.ylabel("MPG")
 
# Set axis limits to show the markers completely
plt.ylim(5, 47)
plt.xlim(1500, 5000)
 
plt.show()

