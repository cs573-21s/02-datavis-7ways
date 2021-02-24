# Stephanie Strom 02-DataVis-7ways

Assignment 2 - Data Visualization, 7 Ways  
===

# R + ggplot2 + R Markdown

I used RStudio and a tutorial video to replicate the chart for the assignment and used this as the starting point to consistently replicate in 6 other tools. I made changes to the color of the marks and background.


![ggplot2](img/ggplot2.png)

# d3

d3 was by far the most challenging and what I spent the most time on. 

<a href = "https://www.essycode.com/posts/adding-gridlines-chart-d3/">https://www.essycode.com/posts/adding-gridlines-chart-d3/</a>

# Excel

To meet the requirement for color by manufacturer and size by weight I seperated the data in to series. I split the weight evenly in 500 lb increments so I needed 7 series just for Ford for example. I could not figure out how to get the tick marks to start somewhere other than the start of the range. So on the x-axis they start at 8 instead of 10. Also the format of the tick marks seems connected to the border of the axis so I was not able to match that exactly to ggplot.

Creating the chart in Excel was pretty easy though it did require some manipulation of the data to get the desired seperation of color and size of the marks. 

# Flourish

Flourish was pretty straightforward to use and was simply a matter of modifying all the options to match the style of the chart. There is no option for minor gridelines. So I chose to only have major gridelines rather than increase the number of tickmarks. The options for the legend are only top and bottom so I decided to leave the legend out for this tool. I used an "Adjust" column for size of the marks with a range of 1-7 (broken down every 500 lbs) to get more variation in size of the marks rather than using the weight data which did not give much variation in size. I went back and made one 0.5 to match the one little mark from ggplot. I also put the opacity to 0.4 because that seemed to match the other chart better than 0.5.

# Tableau

I found Tableau fairly frustrating to use. I found the GUI to be confusing and unintuitive. Color options were limited. I couldn't find a way to add a border to the marks that matched to border fill color. The options seemed to be to have one border color for all marks or no border. I don't think there was a way to turn on minor gridelines but there was a way for minor tick marks. 

# Matplotlib

It was challenging just to get the libraries installed correctly. I am not very proficient in Terminal and things kept going wrong. And I have never worked in Python either. Once I got things working I watched this 10 part series of tutorial videos to learn how to make charts in Matplotlib [Matplotlib Tutorials] (https://www.youtube.com/watch?v=UO98lJQ3QGI&list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB)


## Technical Achievements
- **Tableau**: Created a custom color palette. Also added color matching borders to the marks which I thought was going to be impossible following this website <a href = "https://playfairdata.com/3-ways-to-make-stunning-scatter-plots-in-tableau"/> playfairdata.com </a>
- **Sizing**: I spent a considerable amount of time getting the size of the marks consistent between tools. Many of the tools had an automatic way to size based on the attribute of weight. However I found that making a seperate attribute which I called "Adjust" with a range of 0.5-7 dividing the weight in increments of 500 lbs gave me results closer to the ggplot mark size for some of the tools.
- **Learning libraries and languages**: This class is my first experience using any of these tools (other than Excel) and languages. It's quite a learning curve.

### Design Achievements
- **Color**: I played around with the colors of the marks and background a good amount to come up with a color scheme that I found visually appealing and where the marks stood out from each other and the background while meeting the requirements of 50% opacity. 
- **Consistency**:
