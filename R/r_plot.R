library(ggplot2)
data <- read.csv ("https://raw.githubusercontent.com/geacquista/02-datavis-7ways/main/cars-sample.csv")
ggplot(data, aes(y=MPG, x = Weight, size = Weight, color = Manufacturer)) + geom_point(alpha = 0.5)