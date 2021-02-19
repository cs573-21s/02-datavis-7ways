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


# scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(Weight, MPG, s=BubbleWeight, c=Manufacturer, alpha=0.5)

import matplotlib.patches as mpatches

classes = ['bmw','ford','honda','mercedes','toyota']
class_colours = ['#2377B4','#FF7F0E','#2CA02C','#D62728','#9467BD']
recs = []
for i in range(0,len(class_colours)):
    recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))
colorLegend = ax.legend(recs,classes,loc='upper right')

#colorLegend = ax.legend(scatter.legend_elements(),title="Manufacturers",loc="lower left")

ax.add_artist(colorLegend)

handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5,num=4)
handles.pop(3)
labels = ['$\\mathdefault{2000}$', '$\\mathdefault{3000}$', '$\\mathdefault{4000}$']
weightLegend = ax.legend(handles, labels, title="Weight",loc="lower left")


plt.show()

# plot the data
# s=size of bubble
# c = color
#scatter = plt.scatter(Weight, MPG, s=BubbleWeight, c=Manufacturer, alpha=0.5)

#plt.xlabel("Weight")
#plt.ylabel("MPG")

#plt.show()

