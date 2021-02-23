#install.packages("ggplot2")
# Setup
options(scipen=999)  # turn off scientific notation like 1e+06
library(ggplot2)
#load data
cars <- read.csv("cars-sample.csv")

# Init Ggplot
ggplot(cars, aes(x=Weight, y=MPG, size=Weight, color=Manufacturer)) + 
  geom_point(alpha = 0.5)
