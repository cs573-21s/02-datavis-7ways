cars.sample<-read.csv("cars-sample.csv")
library(ggplot2)
p<-ggplot(
  data=cars.sample,
  mapping = aes(
    x = Weight,
    y = MPG,
    color = Manufacturer,
    size = Weight
  )
)
p + geom_point(alpha=0.5)
