library("ggplot2")
ggplot(carsF, aes(x = Weight, y = MPG, color = Manufacturer, size = Weight)) + 
  geom_point(alpha = 0.5) +
  theme(panel.background = element_rect(fill = "#f0f1f3")) +
  scale_color_manual(values = c("black", "blue", "red", "purple", "#dc9a09"))



