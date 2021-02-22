import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("https://raw.githubusercontent.com/geacquista/02-datavis-7ways/main/cars-sample.csv")
weight = data['Weight']
mpg = data['MPG']
plt.scatter(weight, MPG)
plt.xlabel('Weight')
plt.ylabel('MPG')
plt.show()
