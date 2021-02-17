import matplotlib.pyplot as plt
import csv

# Set up some variables
MPG = []
Weight = []
BubbleWeight = []
Manufacturer = []

# Color array needs to be color or numeric for matplotlib
# Manufacturer is a string so we need to convert
def numericManufacturer(m):
    if m == 'bmw':
        return "#2377B4"
    elif m == 'ford':
        return "#FF7F0E"
    elif m == 'honda':
        return "#2CA02C"
    elif m == 'mercedes':
        return "#D62728"
    else:
        return "#9467BD"

# Load the data
with open("../cars-sample.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        # skip the rows with no MPG values
        if row['MPG'] != 'NA':
            MPG.append(float(row['MPG']))
            Weight.append(float(row['Weight']))
            BubbleWeight.append(float(row['Weight'])*0.03)
            Manufacturer.append(numericManufacturer(row['Manufacturer']))


# plot the data
# s=size of bubble
# c = color
plt.scatter(Weight, MPG, s=BubbleWeight, c=Manufacturer, cmap="Blues", alpha=0.5)

plt.xlabel("Weight")
plt.ylabel("MPG")

plt.show()


