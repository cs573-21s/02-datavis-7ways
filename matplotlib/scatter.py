import numpy as np
import matplotlib.pyplot as plt
import csv

with open('cars-sample.csv', newline='') as cars:
    car_reader = csv.reader(cars, delimiter='\r', quotechar='|')
    weight = []
    mpg = []
    color = []

    for row in car_reader:
        data = row[0].split(',')
        if (data[3] != 'NA' and data[7] != 'Weight'):
            weight.append(float(data[7]))
            mpg.append(float(data[3]))
            if data[2] == "bmw":
                color.append("red")
            elif data[2] == "ford":
                color.append("green")
            elif data[2] == "honda":
                color.append("teal")
            elif data[2] == "mercedes":
                color.append("blue")
            elif data[2] == "toyota":
                color.append("purple")
            else:
                color.append("gray")

    fig, ax = plt.subplots()

    ax.scatter(weight, mpg, alpha=0.5, c=color, s=list(map(lambda x: x / 50, weight)))
    ax.set_xlabel('Weight', fontsize=15)
    ax.set_ylabel('MPG', fontsize=15)
    ax.set_title('Cars by Weight and Volume')

    ax.grid(True)
    fig.tight_layout()

    plt.show()
