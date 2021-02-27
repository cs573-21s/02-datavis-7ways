import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

df = pd.read_csv('cars-clean.csv')
df.drop(df.columns[[0,1]], axis=1, inplace=True)

# Seaborn code

import seaborn as sns

sns.set_theme(style="darkgrid")
# plt.legend(loc='upper right')
sns.relplot(x='Weight', y='MPG', hue='Manufacturer', size='Weight', sizes=(40,400), alpha=0.6, palette='muted', height=6, data=df)
# plt.legend(loc='center left', bbox_to_anchor=(1.25, 0.5))
plt.show()
