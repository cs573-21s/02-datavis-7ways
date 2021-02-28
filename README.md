# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===

## Libraries Used:
- Seaborn
- Matplotlib
- R
- D3
- Vega-lite
- Tableau
- Excel

(Languages used: Python, html/javascript, R)

# Seaborn (Python)
- ![seaborn.png](https://github.com/wtt102/02-datavis-7ways/blob/main/seaborn.png)
- https://seaborn.pydata.org/generated/seaborn.scatterplot.html﻿
  - Seaborn is a bit more consise to use than Matplotlib. Scaling for the sizes and colors are handled automatically. The legends are generated automatically as well. A lot of this library's utility is based in parameter inputs in the main function call. Seaborn allows you to input dataframes or import data from their database. The handling of preprocessing automatically is quite helpful
# Matplotlib (Python)
- ![matplotlib.png](https://github.com/wtt102/02-datavis-7ways/blob/main/matplotlib.png)
- https://matplotlib.org/stable/index.html
  - It's implementation is very similar to Seaborn with more customization necessary to achieve the same thing. Axis labels were necessary to create manually. Grid lines as well. Preprocessing had to be completed before the graphic could generate. The color bar requires extra steps to setup and implement. The only thing matplotlib provides by default is the tick labels. The legends had to be created manually as well. While the code could be written consisely using list comprehensions, there weren't any quick utilities I could find that could do this that already came with Matplotlib.
# ggplot2 (R)
- ![R.png](https://github.com/wtt102/02-datavis-7ways/blob/main/R.png)
- https://r-coder.com/scatter-plot-r/﻿
  - R is a language that is primarily used for statistical analysis. As such, many of its functions are already designed specifically for creating pltos representitive of the data's properties very efficiently. It only took 3 lines to code, and two of these were for housekeeping. Finding the proper functions took some time to setup, as I wasn't familiar with running R scripts before. I think this language offered the best output for the least amount of input. The sizes were scaled such that there was a big enough variation between data points with small "weight" attributes and those with big ones.
# D3 (html/javascript)
- ![d3.png](https://github.com/wtt102/02-datavis-7ways/blob/main/d3.png)
- https://www.d3-graph-gallery.com/graph/scatter_basic.html
- https://stackoverflow.com/questions/11189284/d3-axis-labeling﻿
  - I hadn't used D3 for data representation before in Assignment 1, but some of the knowledge transfered over into this assignment. I found D3 to be by far the most customizable out of all the different scatterplot makers. Things like adding an on-click event is very easy whereas this functionality is not easily accessible with prepackaged libraries such as Seaborn and matplotlib. The data importing took some time to figure out because of javascript privacy configuration to not allow local files to be retrieved. I do find Python to be the better language than javascript for manipulating the data in csv files. A lot of the data management happens behind the scenes. Nevertheless, it was still very easy to figure out how to retreive the data parameters. Labels were not given automatically, but they were pretty easy to add with a text object.
# Vega-lite (html/json)
- ![vega-lite.png](https://github.com/wtt102/02-datavis-7ways/blob/main/vega-lite.png)
- https://vega.github.io/vega-lite/tutorials/getting_started.html
- https://vega.github.io/vega/examples/scatter-plot/﻿
  - This was a very quick implementation and user friendly. The json structure was very navigable. Things like positioning were very intuitive to figure out. Labels were given automatically. The colors were easy to setup.
# Tableau
- ![tableau.png](https://github.com/wtt102/02-datavis-7ways/blob/main/tableau.png)
  - This software was confusing at first because the aggregate setting was switch on initially. This meant 5 data points showed up, each one summing the total of each car manufacturer. After finally realizing this setting was the cause, the software was very easy to adapt to. It was easy to select the size based upon the weight attribute, and color based upon manufacturer. Transparency was easy to change as well. Legends were created automatically. They also provide popups that include information about each data point. I implemented this D3 as well.
# Excel
- ![excel.png](https://github.com/wtt102/02-datavis-7ways/blob/main/excel.png)
  - I was surprised to find that this was by far the most time consuming data vis creation method for me. This software was also a bit tricky at first. I settled on sorting the columns by manufacturer type, then manually adding 5 different series. There are also some issues with the order in which you do things. For instance, changing the relative size of the points in the graph after creating the data points ungroups some of the data points. This means if you later want to change the colors of the circles, you have to do this individually.

## Technical Achievements
- Added hover menu that shows information about data points in D3 implementation.
- Custom legends in matplotlib

## Design Achievements
- Used color blind friendly color schemes and colors schemes generated by AI. Respective links provided as follows:
  - https://davidmathlogic.com/colorblind
  - http://colormind.io/
- Created custom dark mode in Excel with glow.
