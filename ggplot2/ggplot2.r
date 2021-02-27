library(ggplot2)
data <- read.csv("../cars-sample.csv")
ggplot(data, aes(x=Weight, y=MPG)) + geom_point(aes(color=factor(Manufacturer), size=factor(Weight))) + labs(title = paste("Title"))
ggsave("ggplot2-2.png")
