# Based on: https://www.r-graph-gallery.com/320-the-basis-of-bubble-plot.html
# and https://datatofish.com/import-csv-r/
# and https://www.youtube.com/watch?v=h8dn6nbCznQ&ab_channel=MichaelToth

# libraries
library(ggplot2)
library(dplyr)

# Hardcoded for now, not sure how to make this dynamic in R
# RGui seems to run from it's directory instead of the scripts
data <- read.csv("D:/GenericFiles/Documents/573/02-datavis-7ways-1/cars-sample-imputed.csv", header=TRUE)

# d3 category 10 colors
colors <- c("bmw"="#2377B4","ford"="#FF7F0E","honda"="#2CA02C","mercedes"="#D62728","toyota"="#9467BD")


# Bubble plot
ggplot(data, aes(x=Weight, y=MPG, size=Weight, color=Manufacturer)) + geom_point(alpha=0.5) +
scale_color_manual(values=colors)