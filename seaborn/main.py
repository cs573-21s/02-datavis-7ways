import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# load data
data = pd.read_csv('../cars-sample.csv')

# set figure size
sns.set(rc={'figure.figsize':(6,5)})

# plot
scatter = sns.scatterplot(
    data=data,
    x='Weight',
    y='MPG',
    hue='Manufacturer',
    size='Weight',
    alpha=0.5,
    palette=['#a3a500', '#e76bf3', '#f8766d', '#00bf7d', '#00b0f6']
)
plt.legend(fontsize='xx-small')
plt.show()
