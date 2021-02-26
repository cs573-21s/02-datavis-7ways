# This python script imputes the 2 missing MPG values
# We know both of them are 8 cylinder Ford cars
# So we will perform the imputation by finding all of the 8 Cylinder Fords and taking their average MPG values.
# Since it's only two values I am just calculating the average and then printing the output, I will manually replace the value in the csv file
# Both the original and imputed csv files can be found in the Git repository

import csv

# Read the original CSV and gather the MPG values of 8 cylinder Fords
eightCylinderFords = []

with open("./cars-sample-original.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    for row in csv_reader:
        if row['Manufacturer'] == 'ford' and row['Cylinders'] == '8' and row['MPG'] != 'NA':
            eightCylinderFords.append(float(row['MPG']))

# Calculate and print the average MPG of 8 cylinder Fords
average = sum(eightCylinderFords) / len(eightCylinderFords)
print(average)