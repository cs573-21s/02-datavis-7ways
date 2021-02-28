library(ggplot2)
p <- ggplot(read.csv("https://raw.githubusercontent.com/wtt102/02-datavis-7ways/main/cars-sample.csv"), aes(x = Weight, y = MPG, size=Weight, color=Manufacturer)) + geom_point(alpha=0.5)
print(p)
