import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__))

cars = pd.read_csv("../cars-sample.csv")

colors = {
    'bmw': '#7AE600',
    'ford': '#E6AD4D',
    'honda': '#F05D89',
    'mercedes': '#52A9FF',
    'toyota': '#A62FFF',
}

# cars["Colors"] = [colors[make] for make in colors["Manufacturer"]]

fig, ax = plt.subplots()
for make, color in colors.items():
    x = cars.loc[cars["Manufacturer"] == make, ["Weight"]]
    y = cars.loc[cars["Manufacturer"] == make, ["MPG"]]
    scale = 0.1 * cars.loc[cars["Manufacturer"] == make, ["Weight"]]
    ax.scatter(x, y, c=[color for _ in range(len(x))], s=scale, label=make,
               alpha=0.3, edgecolors='none')

ax.legend()
ax.grid(True)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.title('Weight vs MPG Matplotlib')
plt.savefig('matplotlib.png')

plt.show()
