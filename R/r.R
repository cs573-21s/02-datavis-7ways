library(tidyverse)
library(ggplot2)

df <- read_csv("cars-sample.csv")
plt <- ggplot(data=df, aes(x=Weight, y=MPG)) 
plt <- plt + geom_point(aes(size=Weight, color=Manufacturer), alpha=0.5)

print(plt)


