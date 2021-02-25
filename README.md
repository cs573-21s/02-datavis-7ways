Assignment 2 - Data Visualization, 7 Ways  
===
# D3
JavaScript is the most popular programming language of web in the world. D3.js is a JavaScript library for manipulating documents based on data. Using the API in d3.js allows people to design their own vis with a high degree of control.

To visualize the cars dataset, I made use of API in `d3.scale` to create scales to map the “Weight” and “x”, MPG and “y”, “Weight” and circle size. Then, binded the data to the SVG, added circles to the SVG, and determined the manufacturer type of each data to fill with different colors. I made use of API in `d3-axis` to create x axis and y axis. I made us of `d3.brush()` to realize the interaction of brush. 

In the visual cars dataset, I encountered a problem when trying to map "MPG" to "y" because two data in the "MPG" attribute have NA values. In order to solve this problem, I checked the dataset in advance. If the “MPG” value of a certain data in the data set is NA, I deleted it.  In implementing the brush interaction, although it took time to view the document and code, the final effect was very exciting for me. 

I think D3 is a powerful library for creating vis. Designers can find useful tools to fulfill their specific design requirements.

![D3](img/D3.gif)

# Flourish
Flourish is a web-based visualization tool which announces itself can make beautiful and easy visualization and storytelling. Actually, it is indeed very easy to create a visualization by using Flourish. In its website, I only need to upload a csv file and set the properties I want to display, then vis was created.

In Flourish, every step to create a vis can be completed in the visual interface. The user does not need to code anymore. I think this way is very convenient for people who are not familiar with coding. And it is website based, so, people can create vis anywhere if they have internet and screen-device which can be connected to internet. In addition, when vis is done on its website, a link can be created to share with others, and this link can be used to easily nest this vis in my website page.

However, I think it also have some restriction for professional user, because its templates are set in advance. If people can’t find template which is matched to vis they want create, Flourish will be not good working.

![Flourish](img/Flourish.png)

# Tableau
Tableau is a data analysis platform which you must buy the software and download on computer. The software is so easy to get started that it helps people focus on data without spending too much time learning how to use it. 

Similar with Flourish, every step to create a vis can be done in the GUI, without people having any code experience. To create a vis, I only need to upload a csv file and set the properties I want to display.

Different with Flourish, it is as simple as dragging and dropping. In addition, you don’t need to choose a template in advance. The software will automatically create the vis in an acceptable way. Thus, users can focus on the data and dig out the information underlie the data. Moreover, Tableau can automatically create legends and some interactions, giving people a better perception. 

However, I found it is difficult to set specific values for certain properties in Tableau. For example, I want to set specific sizes for the smallest circle and the largest circle but it is difficult. I found that Tableau is easy to set the trend of size changes or change the overall size.

![Tableau](img/Tableau.png)



## Technical Achievements
- **Proved P=NP**: Using a combination of...
- **Solved AI Forever**: ...

### Design Achievements
- **Re-vamped Apple's Design Philosophy**: As demonstrated in my colorscheme...
