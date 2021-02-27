library(readr)
# dataset <- read_csv("WPI/research/ResponseTimeDecomposition/data/all_hint_action_GMM.csv")
dataset <- read_csv("cars-clean.csv")
# View(dataset)

library(ggplot2)
library(dplyr)

ggplot(dataset, aes(x=Weight, y=MPG, size = Weight)) + geom_point(alpha=0.7)

# Most basic bubble plot
dataset %>%
  arrange(desc(Weight)) %>%
  # mutate(Manufacturer = factor(Manufacturer, Manufacturer)) %>%
  ggplot(aes(x=Weight, y=MPG, size=Weight, color=Manufacturer)) +
  geom_point(alpha=0.5) +
  scale_size(range = c(.1, 6), name="Weight")
