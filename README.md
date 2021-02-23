Assignment 2 - Data Visualization, 7 Ways  
===
CS 573: Data Visualization

Due 26 Feb 2021

Imogen Cleaver-Stigum



Place all code, Excel sheets, etcetera in a named folder. For example, `r-ggplot, matlab, mathematica, excel` and so on.



# 1. d3 (Javascript)

![caption](img/<imgname>)

- Write a paragraph for each visualization tool you use. What was easy? Difficult? Where could you see the tool being useful in the future? Did you have to use any hacks or data manipulation to get the right chart?

## Technical Achievements 

interaction

## Design Achievements 

consistent color choice, font choice, element size (e.g. the size of the circles)

# 2. ggplot2 (R)
![caption](img/<imgname>)
## Technical Achievements 

## Design Achievements 


# 3. Matplotlib (Python)
![caption](img/<imgname>)
## Technical Achievements 

## Design Achievements 


# 4. R built in scatterplot tool
![caption](img/<imgname>)
## Technical Achievements 

## Design Achievements 


# 5. p5 (Javascript)
![caption](img/<imgname>)
## Technical Achievements 

## Design Achievements 


# 6. Python
![caption](img/<imgname>)
## Technical Achievements 

## Design Achievements 


# 7. Tableau
![caption](img/<imgname>)
## Technical Achievements 

## Design Achievements 


# 8. Microsoft BI 
![caption](img/<imgname>)
## Technical Achievements 

## Design Achievements 





![ggplot2](img/ggplot2.png)

These features should be preserved as much as possible in your replication:

- Data positioning: it should be a downward-trending scatterplot as shown.  Weight should be on the x-axis and MPG on the y-axis.
- Scales: Note the scales do not start at 0.
- Axis ticks and labels: both axes are labeled and there are tick marks at 10, 20, 30, etcetera.
- Color mapping to Manufacturer.
- Size mapping to Weight.
- Opacity of circles set to 0.5 or 50%.

Other features are not required. This includes:

- The background grid.
- The legends.

Note that some software packages will make it **impossible** to perfectly preserve the above requirements. 
Be sure to note where these deviate.

- R + ggplot2 `<- definitely worth trying`
- Excel
- d3 `<- since the rest of the class uses this, we're requiring it`
- Matplotlib
- three.js `<- well, it's a 3d library. not really recommended, but could be "interesting"`
- p5js `<- good for playing around. not really a chart lib`
- Tableau
- Java 2d
- GNUplot
- Vega-lite <- `<- recently much better. look for the high level js implementations`
- Flourish <- `<- popular last year`
- PowerBI
- SPSS

- If you're using d3, key to this assignment is knowing how to load data.
You will likely use the [`d3.json` or `d3.csv` functions](https://github.com/mbostock/d3/wiki/Requests) to load the data you found.
Beware that these functions are *asynchronous*, meaning it's possible to "build" an empty visualization before the data actually loads.

# R + ggplot2 + R Markdown

R is a language primarily focused on statistical computing.
ggplot2 is a popular library for charting in R.
R Markdown is a document format that compiles to HTML or PDF and allows you to include the output of R code directly in the document.

To visualized the cars dataset, I made use of ggplot2's `geom_point()` layer, with aesthetics functions for the color and size.

While it takes time to find the correct documentation, these functions made the effort creating this chart minimal.

![ggplot2](img/ggplot2.png)
