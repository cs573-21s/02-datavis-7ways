# 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===

When recreating the following chart, the seven tools I used were d3, Matplotlib, Seaborn, Vega-Lite, Excel, Flourish and Tableau.

![ggplot2](img/original.png)

# D3

D3.js is a JavaScript library for manipulating documents based on data. I had to build the x and y axes and then use the data I read from the csv file using D3.csv to plot the points. As I plotted the points, I used Scale functions to determine both the color and the size of each point according to the weight and the manufacturer. I used the following resources as I built the visualization:

https://www.d3-graph-gallery.com/graph/scatter_basic.html
http://bl.ocks.org/weiglemc/6185069

![D3](img/d3_vis.png)

# Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib was very simple to use because it had a scatter plot function that I used to recreate the visualization. All I had to do was read the data from the CSV file and then use the scatter function to plot the points. It was also easy to use the built-in functions to set other features such as the axis tick marks and colors on the chart.

![Matplotlib](img/matplotlib_vis.png)

# Seaborn

Seaborn is a Python data visualization library based on matplotlib which made it easy to build the visualization because many of the functions were very similar to functions used by Matplotlib. However it was a lot simpler to use Seaborn because all I had to do in Seaborn was use the scatterplot function and pass in the desired arguments which included mapping size and color to Weight and Manufacturer.

![Seaborn](img/seaborn_vis.png)

# Vega-Lite

Vega-Lite is a high-level grammar of interactive graphics. It uses JSON syntax so all I needed to do were set various parameters and pass in the CSV file. When mapping the size and color to Weight and Manufacturer, I was able to set the parameters for size and color with a range of values.

![Vega-Lite](img/vega-lite_vis.png)

# Excel

Microsoft Excel is a spreadsheet that features calculation, graphing tools, pivot tables, and a macro programming language called Visual Basic for Applications. In excel, I opened the CSV file as an Excel workbook and built a chart out of the Weight and MPG columns. When mapping the color of each dot to the Manufacturer, I needed the break the data into series and then manually color each series. I was not able to map the size of each point to the Weight.

![Excel](img/excel_vis.png)

# Flourish

Flourish was another no-coding tool that I used. It was very simple to use because all I needed to do was set the x and y columns and then map the size and color to Weight and Manufacturer. From there it was easy to specify the ranges for the x and y axes and the tick marks and labels.

![Flourish](img/flourish_vis.png)

# Tableau

Tableau was also simple to use and required no coding. I loaded the CSV file, specified the x and y columns. I also set the size and color to map to Weight and Manufacturer. Then it was easy to label the x and y axes how I wanted.

![Tableau](img/tableau_vis.png)

## Technical Achievements
- I tried to make the points on the chart the same sizes as the original visualization which I managed to do with most of the tools that I tried with the exception of excel, where I was not able to map the size of the data points to Weight

### Design Achievements
- I made an attempt to use the same color scheme as in the original visualization which I was able to do with all of the tools that I used,    with the exception of Tableau
