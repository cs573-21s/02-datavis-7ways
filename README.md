Assignment 2 - Data Visualization, 7 Ways  
===
#### By Andrew Nolan

For this assignment we are tasked with recreating the following graph using 7 different tools.

!["The target graph"](./img/TargetGraph.png)
This graph was provided by Professor Harrison along with a cars dataset

For this project I chose the following 7 tools, I will discuss them in more detail in the sections below:
1. Microsoft Excel
2. MATLAB R2020B
3. R + ggplot2
4. Python + Matplotlib
5. d3
6. Vega-lite
7. Tableau 

## Excel
The first step on my journey into datavis was excel. Whenever I explore a new csv file this is usually my first step because I can quickly throw together a scatterplot. Little did I know this would be the hardest tool to use. 
- Can't make bubble size legend
- Hacky way of doing different color series
- Not very intuitive and lacking documentation for fancy graphs
- longest time

## MATLAB R2020B
- I work there
- New R2020B feature makes it much easier (bubblegraph)
- Hacky color legend
- decently long to get hacky color
- lots of cool built in features

## R + ggplot2
- Super fast
- easy documentation
- does what you say

## Python + matplotlib
- hard to get custom colors working
- medium amount of time
- legends not automatic

## d3
- very open ended
- can do whatever you want
- pure code nothing automated really
- long but good documentation

## vega-lite
- Super easy to use
- I liked the json format, it was clean to me
- does what you say and does it nicely
- hard to adjust size

## Tableau
- very easy no documentation needed
- fast and learnable
- does everything

# Achievements

## Technical Achievements
- **Made a website with bar charts comparing the results** Bar charts showing the ranking comparisons of different groups
- **Imputed (is that the right word?) values for the NaN instead of skipping them** Wrote a quick python script to cluster by manufacturer and average the MPG that was NaN

## Design Achievements
- **Ensured Colorblind Appropriate Colors**: Instead of using the default R categorical colors, I decided to use a predefined color pallette that would display categorical data in a distinct way. I chose the d3 catgory 10 color pallette, and then used the first 5 colors. I tested the results for someone with tritanopia, protanopia, and deuteranopia using the chrome plugin: "Colorblinding" found here: https://chrome.google.com/webstore/detail/colorblinding/dgbgleaofjainknadoffbjkclicbbgaa/related?hl=en. The categories are still distinct with this color scale, sadly the transparency makes it a little hard to see still.

Colors: 
rgb(31, 119, 180); #2377B4
rgb(255, 127, 14); #FF7F0E
rgb(44, 160, 44); #2CA02C
rgb(214, 39, 40); #D62728
rgb(148, 103, 189); #9467BD