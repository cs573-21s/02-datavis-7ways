# Based on: https://www.r-graph-gallery.com/320-the-basis-of-bubble-plot.html
# and https://datatofish.com/import-csv-r/

# libraries
library(ggplot2)
library(dplyr)

# Hardcoded for now, not sure how to make this dynamic in R
# RGui seems to run from it's directory instead of the scripts
data <- read.csv("D:/GenericFiles/Documents/573/02-datavis-7ways-1/cars-sample.csv", header=TRUE)

# Bubble plot
ggplot(data, aes(x=Weight, y=MPG, size=Weight, color=Manufacturer)) + geom_point(alpha=0.5)