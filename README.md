Assignment 2 - Data Visualization, 7 Ways  
===

# D3
![ggplot2](img/MikeD3.png)

D3 was probably the most intuitive tool for me in comparison to all the other tools when it came to creativity and having full control of what I was visualizing. This could be due to the fact that our first assignment was in D3 and I personally have a decent background using javascript. It was the very first tool I used, but it did also come with its problems.

I did run into the asychronous bug at first. It was interesting because I knew what the problem was, but fixing the problem was not as easy as I thought it would have been.

D3 in comparison to the rest was limited in terms of very specific scatterplot customizations. Like if I wanted to very quickly skip every other label this was a hazel. The good thing about D3 though is that every thing was attached to the html dom. I was able to manipulate that freely and pretty quickly. For me in the future if I had to visualize something that may be discrete or unknown data. I would for sure start with D3 because of its freedom to maniuplate almost everything you place on the dom.

#### Get Started

```
- Cd Into the D3 folder
- Open a terminal at that location
- Run a local http server. ie: python -m SimpleHTTPServer
```



# Flourish 
![ggplot2](img/MikeFlourish.png)


Flourish was for sure an interesting experience as well. I think as a developer it appeared limited to me, however, if I were to put a nondeveloper lens on than I think Flourish was great. If someone was specifically in need of using an online gui tool to create a simple scatterplot Flourish is very good at doing so.

I enjoyed their support that they gave when it came to embedding the visualizations in your html files which made it very easy to freely share. Flourish was the only non-coding library I used. I actually found myself having a harder time manipulating data visualizations that didn't allow you to code like Excel or Flourish. 

It did take me a little while to learn their user interface, but after I did it was fairly intuitive and efficient.


#### Get Started

```
- Cd Into the Flourish folder
- Either open the terminal and enter open . then double click index.html
- Or open the terminal and enter open index.html in the command line.
```


# GGPlot2 
![ggplot2](img/MikeGGPlot2.png)

In my opinion, R Studio was probably the easiest to use out of all of the tools. I think this had a lot to do with the fact that the example itself utilized GGPlot. I think one important factor when using a tool that relies on coding is that parsing the csv and reading that csv is the most time consuming tasks. 

When it came to parsing the CSV, and reading the data I needed to read in the scatterplot, this was very simple in ggplot2. 


#### Get Started

```
- Open R Studio
- Open Plot.R
- Run install.packages("ggplot2") to install ggplot2 and initalize it
- Make sure you know the location to the cars-sample.csv
- Hit Run
```


# Matlab 
![ggplot2](img/MikeMatlab.png)


Matlab was probably one of the hardest to visually represent the data in the same fashion that I did with the others. I think I was limited in terms of manipulating size of the markers, but when it came to visualizing the points and reading the data. That was pretty straight forward and it only took a few lines of code.

I did have to do alot of reading on the documentations here to understand how color mapping worked. I'd honestly say this was the hardest part in matlab. Unlike most of the other programs that supported hex. Ofcourse, Matlab didn't so I spent alot of time trying to understand the usage of rgb in matlab and how we could map specific attributes to their specific colormapping.

#### Get Started

```
- Open Matlab
- cd into the folder Matlab and make sure that contains Plot.m and cars-sample.csv.
- Make it your working directly
- Open Plot.m
- Hit Run
```


# Matplotlib 
![ggplot2](img/MikeMatplotlib.png)

I really did enjoy using Python again. Python has to be probably my favorite language. In this case with Matplotlib, though, it was probably the second hardest tool I used in this assignment. Instead of typically using the panda library to help you read csv files. I chose another path of using numpy. This definitely complicated things and made reading data from the CSV a lot harder than it should have been.

There were many smooth features in Matplotlib though that I noticed a lot of the other tools lacked like skipping label intervals for instance. I think I used a hacky way of skipping intervals by using setp and changing visibility on ticklabels, but with a very few lines of code I was still able to get a pretty clean result.

#### Get Started

```
- cd into Matplotlib folder.
- pip install matplotlib, if you don't have it already
- Open the terminal, run python Plot.py
```


# Vegalite 
![ggplot2](img/MikeVegaLite.png)

Vegalite was probably one of the easiest implementations to create outside of Flourish. I think me so happening to choose to do Vegalite right after doing my D3 implementation helped greatly. D3 to me was very smooth in terms of manipulating the dom and so forth but when I found out that Vegalite was utilizing canvas I was sold in terms of which one i'd probably use if I had to choose one for this assignment. 

One hacky thing I did do with vegalite was use an html block to give the grid a backdrop. I didn't have to do this step in any other interrations, but I did notice that something as simple as changing the backdrop to only be bounded by the axies was a little harder than expected. They support people changing the background of the whole canvas, but in the case of this project I only needed what was inside the bounds.

#### Get Started

```
- Cd Into the VegaLite folder
- Open a terminal at that location
- Run a local http server. ie: python -m SimpleHTTPServer
```



# Plotly 
![ggplot2](img/MikePlotly.png)

Plotly in terms of Python frameworks that I used, was probably the simplest of all. Unlike my numpy implementation that I used for Matplotlib, I chose to use panda in this case and make use of their native scatter function. I actually can say this was the smoothest go around of all of them. I used the least amount of code, while producing probably one of the best replications, all while having access to the power Python language.

#### Get Started

```
- cd into Plotly folder.
- pip install plotly plotly-express pandas, if you don't have it already
- Open the terminal, run python Plot.py
```


## Technical Achievements
- I was able to implement numpy genfromtxt in order to render a graph in Matplotlib without the use of Panda
- I was able to translate between datatypes in order to match csv values manually with a self created dictionary in python. Translation was done between NumpyArrays and standard Python Dictionaries
- Dynamically used recursion to implement grid lines in certain tools that did not have easy support of creating a grid

### Design Achievements
- Visually, I was able to rerender a grid background in every tool I used. This came in many forms. For D3 for instance I used the power of their custom objects to render the gray overlay. In the case of Vega Lite I utilized the html canvas to render the gray background
- In order to show every other label on the axies, I manually manipulated the dom to remove ticks in order to more reflect the original plot
- Utilized Cascading Styling Sheets (CSS) in some cases to override html elements in order to fully match the appearance to the original plot 


