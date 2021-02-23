import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# load data
data = pd.read_csv('cars-sample.csv')

# set figure size
sns.set(rc={'figure.figsize':(6,5)})

# plot
sns.scatterplot(
    data=data,
    x='Weight',
    y='MPG',
    hue='Manufacturer',
    size='Weight',
    alpha=0.5,
    palette=['#b4b650', '#dfa9e0', '#f3b6b7', '#93d8bc', '#56B4E9']
)
plt.legend(fontsize='xx-small')

plt.show()