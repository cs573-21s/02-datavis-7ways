import pandas as pd
import matplotlib.pylab  as plt 
import numpy as np
import seaborn as sns

#https://seaborn.pydata.org/generated/seaborn.scatterplot.html

#import data
data = pd.read_csv('cars-sample.csv')

#generate color map
color_map = {
    "bmw": "#2C3F51",
    "ford": "#CB2228",
    "honda": "#EF8239",
    "mercedes": "#634041",
    "toyota": "#F9B943"
}

#generate size map
avg_weight = sum(list(data['Weight']))/len(data['Weight'])

#make plot
sns.scatterplot(
    data=data, x="Weight", y="MPG", hue="Manufacturer", size="Weight",
    palette=color_map.values(),legend='brief', alpha=0.5
)

#show plot
plt.show()