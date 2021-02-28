import matplotlib.pyplot as plt
import matplotlib.axes as ax
import matplotlib.ticker as ticker
import pandas as pd

data = pd.read_csv(r'cars-sample.csv')

colorMap = {'bmw': '#f3b8b4',
            'ford': '#c8c981',
            'mercedes': '#91d2f4',
            'honda': '#89d6b5',
            'toyota':'#eebbf2'}

fig, ax = plt.subplots()

for index, row in data.iterrows():
    ax.scatter(row["Weight"], row["MPG"], s=row["Weight"]/30, c=colorMap[row["Manufacturer"]], alpha=0.5)

plt.xlim(1500,5100)
plt.ylim(8,48)
plt.xticks([2000,3000,4000,5000])
plt.yticks([10,20,30,40])
plt.xlabel("Weight")
plt.ylabel("MPG")
ax.set_facecolor('#ececec')
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(500))
plt.grid(True, c='#ffffff')
plt.show()
