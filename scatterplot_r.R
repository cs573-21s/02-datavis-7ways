#Use the following line if it can't detect file
#setwd("C:/YOUR_DIRECTORY_HERE")
library(ggplot2)
p <- ggplot(read.csv("cars-sample.csv"), aes(x = Weight, y = MPG, size=Weight, color=Manufacturer))
print(p)