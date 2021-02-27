# R and ggplot2

# Libraries
library(ggplot2)
library(readr)
library(RColorBrewer)
library(wesanderson)

# Get the data
data2 <- read_csv("/Users/Jyalu/Documents/Ramen/3/C/Data-Vis/02-datavis-7ways/data/cars_cleaned.csv")

pal <- wes_palette('Darjeeling1', 5)
pal_r <- rev(unique(pal))
pal2 <- brewer.pal(n = 5, name = "Dark2")
pal2_r <- rev(unique(pal2))

# Plot
ggplot(data=data2, aes(x=Weight, y=MPG, color=Manufacturer)) +
  geom_point(aes(size=Weight), alpha = 0.5) +
  scale_size(range = c(0.5, 12)) +
  scale_color_manual(values = pal2_r)
  
  
  