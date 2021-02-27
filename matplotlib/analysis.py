import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

df = pd.read_csv('cars-clean.csv')
df.drop(df.columns[[0,1]], axis=1, inplace=True)

manus = df['Manufacturer'].unique()

colorDict = {'bmw': '#e9bbb5',
             'ford': '#c6c683',
             'honda': '#a3d5bc',
             'mercedes': '#9fcff1',
             'toyota': '#e0a8ee'}

colors = ['#e9bbb5', '#c6c683', '#a3d5bc', '#9fcff1', '#e0a8ee']

# for manu, color in zip(manus, colors):
#     temp = df.loc[df.Manufacturer == manu]
#     plt.scatter(df['Weight'], df['MPG'], alpha=0.2, s=df['Weight']/10, c=color)

fig, ax = plt.subplots()

ax.set_facecolor((.94,.94,.94))
ax.grid(color='w', linestyle='-', linewidth=1)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

for manu, i in zip(manus, range(manus.size)):
    temp = df.loc[df['Manufacturer'] == manu]
    ax.scatter(temp['Weight'], temp['MPG'], alpha=0.65, s=np.round(temp['Weight'] / 70), c=temp['Manufacturer'].map(colorDict), label= manu)


# ax.scatter(df['Weight'], df['MPG'], alpha=0.8, s=np.round(np.power(1.2, df['Weight']/300)), c=df['Manufacturer'].map(colorDict))
# ax.scatter(df['Weight'], df['MPG'], alpha=0.65, s=np.round(df['Weight']/70), c=df['Manufacturer'].map(colorDict))
ax.set_axisbelow(True)
# ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
plt.xlabel('Weight')
plt.ylabel('MPG')
# plt.legend()

legend_elements = [Line2D([0], [0], marker='o', color='w', label='2000', markerfacecolor='#999999', markersize=5),
                   Line2D([0], [0], marker='o', color='w', label='3000', markerfacecolor='#999999', markersize=6),
                   Line2D([0], [0], marker='o', color='w', label='4000', markerfacecolor='#999999', markersize=8)]

# Create the figure
# fig, ax = plt.subplots()
legend1 = plt.legend(handles=legend_elements, bbox_to_anchor=(1.05, 0.45), loc='center left', title='Weight', fontsize='x-small', frameon=False)
ax.add_artist(legend1)
plt.legend(title='Manufacturer', bbox_to_anchor=(1.05, 0.8), loc='upper left', fontsize='x-small', frameon=False)
plt.plot()
plt.show()


