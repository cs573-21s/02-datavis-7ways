library("ggplot2")
cars <- read.csv("~/Documents/02-datavis-7ways/GGPlot2/cars-sample.csv", header = TRUE, sep = ",")
ggplot(data=cars, aes(x=Weight, y=MPG)) + geom_point(aes(colour = Manufacturer, size=Weight, alpha = 0.5))

