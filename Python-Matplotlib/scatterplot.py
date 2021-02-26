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
# cars-sample-original can be swapped in if you want to see the NA MPG rows skipped instead of imputed
with open("../cars-sample-imputed.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        # skip the rows with no MPG values
        if row['MPG'] != 'NA':
            MPG.append(float(row['MPG']))
            Weight.append(float(row['Weight']))
            BubbleWeight.append(float(row['Weight'])*0.03)
            Manufacturer.append(numericManufacturer(row['Manufacturer']))


# scatter plot
# It's nice and easy to make the bubble chart
fig, ax = plt.subplots()
scatter = ax.scatter(Weight, MPG, s=BubbleWeight, c=Manufacturer, alpha=0.5)
ax.set_ylabel('MPG')
ax.set_xlabel('Weight')

# Add the legends
# It's very annoying to make bubble or color legends. I had to do some weird stuff
import matplotlib.patches as mpatches

# Make the color legend
classes = ['bmw','ford','honda','mercedes','toyota']
class_colours = ['#2377B480','#FF7F0E80','#2CA02C80','#D6272880','#9467BD80']
recs = []
for i in range(0,len(class_colours)):
    recs.append(mpatches.Rectangle((0,0),1,1,fc=class_colours[i]))
colorLegend = ax.legend(recs,classes,loc='upper right')

ax.add_artist(colorLegend)

# Make the weight legend
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.5,num=4)
handles.pop(3)
labels = ['$\\mathdefault{2000}$', '$\\mathdefault{3000}$', '$\\mathdefault{4000}$']
weightLegend = ax.legend(handles, labels, title="Weight",loc="lower left")

# Display the graph
plt.show()