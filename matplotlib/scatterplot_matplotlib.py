import pandas as pd
import matplotlib.pylab  as plt 
import numpy as np

#import data
data = pd.read_csv('https://raw.githubusercontent.com/wtt102/02-datavis-7ways/main/cars-sample.csv')

#generate color map
color_map = {
    "bmw": "#2C3F51",
    "ford": "#CB2228",
    "honda": "#EF8239",
    "mercedes": "#634041",
    "toyota": "#612C49"
}

#generate size map
avg_weight = sum(list(data['Weight']))/len(data['Weight'])
size_map = [50*(w-avg_weight/1.8)/(avg_weight/1.8) for w in data['Weight']]

#add the points
plt.scatter(data['Weight'], data['MPG'],c=data['Manufacturer'].map(color_map),s=size_map, alpha=0.5)

#add gridlines
plt.grid(True, linewidth=0.5, color='#ff0000', linestyle='-', alpha=0.1)

#add labels
plt.xlabel("Weight")
plt.ylabel("MPG")

#get legend data
points_size_legend = [plt.scatter([],[], s=50*(i*1000-avg_weight/1.8)/(avg_weight/1.8), edgecolors='none',c=['Black'],alpha=0.6,edgecolor='black') for i in range(2,5)]
points_color_legend = [plt.scatter([],[], s=50, c=[color_map[manu]],alpha=0.5) for manu in color_map.keys()]

#create legends
leg_color = plt.legend(points_color_legend, color_map.keys(), loc='upper right')
ax = plt.gca().add_artist(leg_color)
leg_size = plt.legend(points_size_legend, ["2000", "3000", "4000"],title="Weight", loc='right')

#show plot
plt.show()