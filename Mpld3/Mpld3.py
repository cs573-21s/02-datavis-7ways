# Reference: https://mpld3.github.io/examples/html_tooltips.html
import matplotlib.pyplot as plt
import pandas as pd
import mpld3

# Define CSS to control custom labels
css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""

# load data
df = pd.read_csv('../matplotlib/cars-sample.csv')
# remove NA value
index=df.MPG.notnull()
data=df[index]
#
data_without_title = data[0:][1:]
Manufacturer = list(data.Manufacturer[1:])
Weight = list(map(float, data.Weight[1:]))
MPG = list(map(float, data.MPG[1:]))
Car = list(data.Car[1:])

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

fig, ax = plt.subplots()
ax.grid(True, alpha=0.3)

labels = []
for i in range(len(data_without_title.index)):
    label = data_without_title.iloc[[i], 2:].T
    label.columns = [Car[i]]
    labels.append(str(label.to_html()))

scatter = ax.scatter(x, y, s=linear_Weight, c=colors, alpha=0.5)
ax.set_title('A2 mpld3')
ax.set_xlabel('Weight')
ax.set_ylabel('MPG')
# Define tool tip
tooltip = mpld3.plugins.PointHTMLTooltip(scatter, labels, css=css)
mpld3.plugins.connect(fig, tooltip)
# mpld3.save_html(fig, 'index.html')
mpld3.show()