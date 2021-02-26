library(ggplot2)

cars = read.csv("C:\\Users\\jpk25\\Desktop\\data-vis\\02-datavis-7ways\\cars-sample.csv", header = TRUE)

ggplot(cars, aes(x = Weight, y = MPG, size = Weight, color = Manufacturer, alpha=.5)) +
  geom_point()

