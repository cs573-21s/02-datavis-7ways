# install.packages("ggplot2")
library(ggplot2)

df <- read_csv("GitHub/02-datavis-7ways/cars-sample.csv")
plt <- ggplot(data=df, aes(x=Weight, y=MPG)) 
plt <- plt + geom_point(aes(size=Weight, color=Manufacturer), alpha=0.5)

print(plt)


