import matplotlib.pyplot as plt
import pandas as pd
import mpld3

# load data
data = pd.read_csv('../matplotlib/cars-sample.csv', header=None)
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
    if i == 'ford':
        colors.append('#a3a500')
    if i == 'honda':
        colors.append('#00bf7d')
    if i == 'mercedes':
        colors.append('#00b0f6')
    if i == 'toyota':
        colors.append('#e76bf3')

# plot
fig, ax = plt.subplots()
scatter = ax.scatter(x, y, s=linear_Weight, c=colors, alpha=0.5)
ax.grid(color='white', alpha=0.1)
ax.set_title('A2 mpld3')
ax.set_xlabel('Weight')
ax.set_ylabel('MPG')
ax.set_facecolor('#ebebeb')
mpld3.save_html(fig, 'index.html')
# mpld3.show()