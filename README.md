# 02-DataVis-7ways
Matthew St Louis

1. [02-DataVis-7ways](#02-datavis-7ways)
   1. [D3](#d3)
   2. [matplotlib](#matplotlib)
   3. [ggplot2](#ggplot2)
   4. [Tableau](#tableau)
   5. [Flourish](#flourish)
   6. [Excel](#excel)
   7. [Chart.js](#chartjs)
   8. [Technical Achievements](#technical-achievements)
   9. [Design Achievements](#design-achievements)
   10. [Resources Used](#resources-used)
      1. [D3 (copied from A1)](#d3-copied-from-a1)
      2. [Matplotlib](#matplotlib-1)
      3. [R](#r)
      4. [Chart JS](#chart-js)


## D3
![D3 Chart](img/d3-alt.png)
I started with D3 because I used it for the last project and I had some starting code to build on. D3 is definitely the most versatile library and seems to have the most potential for customization, though I definitely had a hard time with some parts of it.

I thought that it would be relatively easy to add onto this code, but some additions were unexpectedly difficult. I couldn't get axis labels to work right. I tried a good number of different stack overflow articles (I wish I'd saved them, but I only save the resources that end up working). My attempt at axis labels is shown below:

![D3 failed axis labels](img/d3.png)

D3 is certainly powerful, but I find it very hard to work with, especially when I'm just starting out with it. The API feels secretive and unintuitive, and the fact that the developer is responsible for every individual element of the chart is daunting.


## matplotlib
![matplotlib chart](img/matplotlib.png)
The next library I attempted was matplotlib. It seems like it will be useful for making graphs on my MQP, and I wanted to get some experience with it. This was definitely my favorite library to work with. While not as flexible as d3, it felt a lot more usable to me. The fact that the API is split between a Matlab state machine and object-oriented design is a bit weird, but it's pretty easy to find how to add chart elements.

I've gotten reasonably familiar with Pandas, and so data manipulation felt by far the most natural with matplotlib. Everything felt really straightforward to me. I was able to replicate the axis labels, scales, and color key without much issue, though I didn't figure out how to add a legend for size.

## ggplot2
![ggplot2 chart](img/ggplot.png)

The third approach I applied was ggplot2. It was advertized as being able to set up in just a few lines of code, and that's exactly how it worked. I had some trouble with getting the sizes to show up on the legend. It was really interesting to me how I didn't need to do any data processing whatsoever.

## Tableau
![Tableau chart](img/tableau.png)

Tableau was interesting to me because the fact that it's a drag-and-drop interface seems to imply that it's meant for non-technical users to be able to manipulate data easily, but the UI was so busy that it took me a while to figure out where to get started and how to display the data correctly. For some reason, the data was originally trapped in aggregations, and it took me a bit to get it to show up as individual points.

Once I had the graph displayed, I could customize it fairly easily and started to explore the UI, but the whole experience felt pretty unintuitive to me.

One problem I had with Tableau is that the color customization was very limited. I couldn't figure out how to use any custom colors outside of the provided pallets, so I went with the colorblind-friendly pallet.

Overall, I get the sense that Tableau is functional but very rigid in what customization it allows. It doesn't feel flexible enough for me to enjoy.

## Flourish
![Flourish chart](img/flourish.png)

Flourish was similar to Tableau in its simple, non-technical design, but I found it a lot more readily usable. The design were you provide columns to different encodings felt extraordinarily straightforward. It also feels more customizable than Tableau because I was able to customize the colors.

I would probably prefer Tableau if I had to work with one for a long project, but for something quick, easy, and customizable, Flourish feels more friendly to me.


## Excel
![Excel chart](img/excel.png)

Most of my experience with Excel has been high school physics graphs. Those felt pretty straightforward, so I assumed that this would be straightforward as well, and I thought that this would be as well. I was very mistaken.

I was surprised that Excel gave me the most trouble with data preparation—even more than Chart.js. I couldn't find a straightforward way to separate out the different series. There's probably a complicated way to it with obscure formulas or some pivot table nonsense, but I ended up making the data into a table, sorting the table by Manufacturer, and manually selecting each make of car as a separate series.

Excel is interesting in how it's by far the least user-friendly of the non-technical approaches. I know that it's meant to be usable for business majors, but it feels like it takes a lot of precise finnegaling to do anything interesting.

One small difficulty I ran into was that hte dots for BMW were obscured by the colors on top of them and indistinguishable from the Honda purple dots. I had to move the BMW below the other series so that it would be plotted last so it would be on top and visible.

For all of the trouble it takes to make an interesting graph, the result is not that impressive. I feel like I'll avoid Excel unless I need to make the simplest of graphs. I think that I would rather use matplotlib in most situations of medium complexity.

## Chart.js
![ChartJS chart](img/chart-js.png)

Chart JS was the last approach I used. I found it really interesting how much interactivity this graph came with out of the box. You can click on different colors on the legend to exclude them from the graph, and the graph will automatically rescale to fit the remaining data.

I had some trouble figuring out how to format the data from the documentation. I found it really annoying how every property to set takes an object with very specific attribute names. I tried to replicate the format shown on the Bubbles documentation page, but I needed to read several other pages to piece together the expected format of the data. Once I had that figured out, it was relatively straightforward to stylize the graph and further manipulate the data.

Once I learned to use the ChartJS API, I liked it a lot more than the d3 API. d3 always feels like cryptic incantations into the void to me. I don't understand what strings are arbitrary and which have special meaning. Looking up syntax in d3 feels like finding something I would have had no way to know about, and I need to figure out where it fits into the code I've written. With ChartJS, it feels a lot more natural where the pieces fit together, and VS Code's intellisense lets me find some settings on my own without the documentation. 

I think I prefer working with ChartJS's API to d3's, though the fact that there's so much interactivity built into what comes out of the box makes it feel less flexible than d3. Since everything in d3 needs to be added manually, it feels like the most versatile of any approach I used.

## Technical Achievements


## Design Achievements

For this assignment, I wanted to play around with a few of the color tools shown in class. For most visualizations ([d3](#d3), [matplotlib](#matplotlib), [chart.js](#chartjs)), I used the [Adobe Color Wheel](https://color.adobe.com/create/color-wheel) on Double Split Complementary because this felt conducive to categorical data to me. 

![Adobe Color Wheel](./img/adobe.png)

For [Excel](#excel), I tried out the [colorblind-friendly tools on the Adobe Color Wheel](https://color.adobe.com/create/color-accessibility) to come up with the following pallet.

![Adobe Color Wheel Accessible](./img/adobe-access.png)

For Tableau, I couldn't figure out custom colors, so I used their colorblind-friendly pallet, though in my opinion it doesn't make the colors distinct enough. 

For my chart with [Flourish](#flourish), I tried using [colorgorical](http://vrl.cs.brown.edu/color) to create a distinct color pallet. I had to try a few different times before the colors actually looked distinct on the graph to me.

![Colorgorical](./img/colorgorical.png)

## Resources Used
- [Gitignore](https://www.toptal.com/developers/gitignore/api/node,macos,windows,vscode,linux)
- [Glitch Hello Express](https://glitch.com/edit/#!/hello-express)
  - Express server template
  - HTML Page Template
- [Stack Overflow](https://stackoverflow.com/questions/58384179/syntaxerror-cannot-use-import-statement-outside-a-module)
  - Getting the import to work

### D3 (copied from [A1](https://github.com/mastlouis/01-ghd3))
- [Observable - Learn D3 Data](https://observablehq.com/@d3/learn-d3-data?collection=@d3/learn-d3): I used this to learn how to parse dates in D3 so that the wind data could have a meaningful X coordinate.
- [D3 Graph Gallery Scatterplot](https://www.d3-graph-gallery.com/graph/scatter_basic.html): Used as an example to get circle working
- [D3.js Version 5 Scatterplots with Shapes](https://chewett.co.uk/blog/1483/d3-js-version-5-scatterplot-with-shapes/): Used to get symbols to work
- [D3 in Depth - Shapes](https://www.d3indepth.com/shapes/): Used as a reference for different symbol types

### Matplotlib
- [Python Venv help](https://www.studytonight.com/post/python-virtual-environment-setup-on-mac-osx-easiest-way): I got stuck in venv hell, and this got me out.
- [Matplotlib Example](https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html): This example of a scatterplot with a legend is mostly what I based my code on.
- [Save Image](https://muddoo.com/tutorials/matplotlib-save-plot-to-file-in-png-or-jpg-format/)
- [What Axis Does](https://matplotlib.org/stable/api/axes_api.html#matplotlib.axes.Axes): The API took a bit of figuring out, and this definitely helped.
- [Documentation](https://matplotlib.org/stable/api/index.html): I read over some of the documentation to better understand the two parallel API's and how different pieces of the API fit together.

### R
- [Import CSV](https://www.statology.org/import-csv-into-r/)

### Chart JS
- [Documentation](https://www.chartjs.org/docs/latest/getting-started/usage.html): I learned the API by reading the documentation and copied off of their general example and Bubbles example.
- [CDN](https://cdnjs.com/libraries/Chart.js)
- [Labeling Axes](https://www.chartjs.org/docs/latest/axes/labelling.html)