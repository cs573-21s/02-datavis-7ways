import matplotlib.pyplot as plt
import seaborn as sea
import pandas as pd

sea.set(rc={'axes.facecolor':'#ececec', 'figure.facecolor':'white'})

cars = pd.read_csv(r'cars-sample.csv')

colorMap = {'bmw': '#f3b8b4',
            'ford': '#c8c981',
            'mercedes': '#91d2f4',
            'honda': '#89d6b5',
            'toyota':'#eebbf2'}

sea.scatterplot(x="Weight", y="MPG", size="Weight",
    sizes=(75,250), hue="Manufacturer", palette=colorMap,
    alpha=0.5, data=cars, legend=False);
plt.xticks([2000,3000,4000,5000])
plt.yticks([10,20,30,40])
plt.grid(True, c='#ffffff')
plt.show()
