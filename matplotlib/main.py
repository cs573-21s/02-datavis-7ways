import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)

# Reading in the CSV
df = pd.read_csv("cars-sample.csv")

# values
x = df.Weight.values
y = df.MPG.values
colors = {'bmw':"#eb5e34", "ford":"#4e9e37", "honda":"#00ffd0", "mercedes":"blue", "toyota":"#eb00eb"}
size = df['Weight'].to_numpy()
s = [(s/1000)**3 for s in size]

# Making Plot
fig, ax = plt.subplots()
plt.xlabel("Weight")
plt.ylabel("MPG")

ax.yaxis.set_major_locator(MultipleLocator(10))     # idk why y axis isn't get
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.xaxis.set_major_locator(MultipleLocator(1000))
ax.xaxis.set_minor_locator(MultipleLocator(500))

plt.scatter(x, y, s=s, c=df["Manufacturer"].map(colors), alpha=0.5)
plt.yscale('linear')
plt.show()
