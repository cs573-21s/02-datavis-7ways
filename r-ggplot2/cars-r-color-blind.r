library(ggplot2)
data_ <- read.csv("/Users/macbookpro/Desktop/02-datavis-7ways-1/cars-sample.csv") 
ggplot(data_, aes(x = Weight, y = MPG, size = Weight, color = Manufacturer, shape = Manufacturer))+
  geom_point(alpha = 0.5)