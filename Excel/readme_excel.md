Excel
===
![Excel graph](../img/Excel.PNG)
The first step on my journey into datavis was excel. Whenever I explore a new csv file this is usually my first step because I can quickly throw together a scatterplot or other visualization with minimal efforst. So I was very surprised to discover this would be the hardest tool to use. 

Excel does not do a great job at making complex graphs. It is strict in its requirement for the number of series affecting the data points. With a bubble chart it expects three values: x, y, and bubble size. To add a fourth value of color a lot of hacky maneuvers need to be taken [1,2]. For each different color/manufacturer type, I had to create a separate series and put the weight (x values) in that and #N/A values in the column for when it was not of that type. You can see a subset of this change in the data below. When a car was a Ford it's weight would go in the ford column and a #N/A value would go in the others. Then each of these would be plotted on the graph as different colors. The nice part of this is it allowed the color legend to be auto generated.

![Excel hacks for different colors](../img/HackyExcel.PNG)

Another major draw back was there appears to be no built in way to add a weight legend to the Excel graph. Excel does support VBA scripts but I wanted to try to do everything purely with Excel. So for this legend I had to add a textbox and manually draw the weight cirles. It's tedious and not automated, but it doesn't look bad.

Excel took me a very long time to complete compared to some of the others. It's very limited in what it allows and doesn't allow much customization beyond their given features. I would not recommend Excel for fancy visualizations, but I would say it's a good choice for very simple, quick graphs like basic bar charts or 2 feature scatter plots.

## Sources
1. Conditional Coloring in Excel: http://daydreamingnumbers.com/how-to/conditional-colouring-to-scatterplots-in-excel/
2. Conditional Coloring in Excel: https://stackoverflow.com/questions/15124103/excel-how-can-i-make-a-scatter-plot-which-colors-by-a-third-column
3. Bubble Plots: https://support.microsoft.com/en-us/office/present-your-data-in-a-bubble-chart-424d7bda-93e8-4983-9b51-c766f3e330d9
4. Editing Legends: https://support.microsoft.com/en-us/office/modify-chart-legend-entries-d822dd57-af28-4c3e-93d1-d320e6239843
5. Multiple legends in excel https://stackoverflow.com/questions/33230348/multiple-legends-in-excel-chart