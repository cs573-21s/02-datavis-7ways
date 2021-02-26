// Bar Charts to Rank the Visualization Tools
// By Andrew Nolan

/* Sources:
 * Changing Bar Charts: https://www.d3-graph-gallery.com/graph/barplot_button_data_hard.html
 * Tooltips on Bar Charts: https://bl.ocks.org/alandunning/274bf248fd0f362d64674920e85c1eb7
 */

// The data
let learnability = [
    { vis: 'Excel', value: '7th', color: '#008000', tooltip:'Excel had very old documentation<br>and not many tutorials'},
    { vis: 'MATLAB', value: '5th', color: '#d0530f', tooltip:'The documentation was very good for the basic<br> bubble chart, but it was hard to expand beyond their examples.' },
    { vis: 'R + ggplot2', value: '2nd', color: '#2569c0', tooltip:'The documentation was super clear and easy to follow.' },
    { vis: 'Python + Matplotlib', value: '4th', color: '#ffdd54',tooltip:'The documentation mostly covered everything, but as they say<br> "Matplotlib makes easy things easy and hard things possible".<br> It still had challenges, as described in the report.' },
    { vis: 'd3', value: '6th', color: '#000000', tooltip:'I feel a little bad about this one, d3 has fantastic documentation. <br>It just also had a steep learning curve and a lot to learn <br>since you have to do everything yourself.' },
    { vis: 'Vega-Lite', value: '3rd', color: '#274c71', tooltip:'The JSON format was very structured and nice to learn, documentation was helpful.' },
    { vis: 'Tableau', value: '1st', color: '#1c437e', tooltip:'Tableau was clearly designed to build visualizations.<br>It is clear to use and guides you nicely with prompts.<br>I needed to use no tutorials or documentation to learn this tool.' },
];

let fileSize = [
    { vis: 'Excel', value: '7th', color: '#008000', tooltip:'34kb' }, //34kb
    { vis: 'MATLAB', value: '3rd', color: '#d0530f', tooltip:'2kb'}, //2kb
    { vis: 'R + ggplot2', value: '1st', color: '#2569c0',tooltip:'1kb 19 lines of code' }, //1kb 19 lines
    { vis: 'Python + Matplotlib', value: '4th', color: '#ffdd54', tooltip:'3kb, 65 lines of code' }, //3kb 65 lines
    { vis: 'd3', value: '5th', color: '#000000', tooltip:'3kb 119 lines of code'}, //3kb 119 lines
    { vis: 'Vega-Lite', value: '2nd', color: '#274c71', tooltip:'1kb 28 lines of code' }, //1kb 28 lines
    { vis: 'Tableau', value: '6th', color: '#1c437e', tooltip:'33kb' }, //33 kb
];

let customization = [
    { vis: 'Excel', value: '7th', color: '#008000', tooltip:'Limited customization beyond the predefined graph type' },
    { vis: 'MATLAB', value: '3rd', color: '#d0530f', tooltip:'Lots of customization, available to the full power of MATLAB.<br>Although it can be difficult.' },
    { vis: 'R + ggplot2', value: '4th', color: '#2569c0', tooltip:'Likely customization to the full power of R as a programming language,<br>but I did not experience it in my work for this project.' },
    { vis: 'Python + Matplotlib', value: '2nd', color: '#ffdd54', tooltip:'Lots of customization, if you can code it in python it can happen.' },
    { vis: 'd3', value: '1st', color: '#000000', tooltip:'Nothing is done for you, everything is customized.<br>You could do whatever you imagine.' },
    { vis: 'Vega-Lite', value: '5th', color: '#274c71', tooltip:'Stuck to the rigid JSON formatting and what it allows you to add.<br>It encompasses a lot but might prevent some things.' },
    { vis: 'Tableau', value: '6th', color: '#1c437e', tooltip:'Tableau lets you do a lot, but you could not<br>add something creative if it did not suport it.' },
];

let hackiness = [
    { vis: 'Excel', value: '7th', color: '#008000', tooltip:'Required hacks for multiple colors and both legends.' },
    { vis: 'MATLAB', value: '6th', color: '#d0530f', tooltip:'Required dummy data points to get the color legend.' },
    { vis: 'R + ggplot2', value: '1st', color: '#2569c0', tooltip:'Tied for first, no hacks needed to make the plot.' },
    { vis: 'Python + Matplotlib', value: '5th', color: '#ffdd54', tooltip:'Required some weird code to get the legends created correctly.' },
    { vis: 'd3', value: '4th', color: '#000000', tooltip:'Nothing really hacky, except that you need to code everything by hand.' },
    { vis: 'Vega-Lite', value: '1st', color: '#274c71', tooltip:'Tied for first, no hacks needed to make the plot.' },
    { vis: 'Tableau', value: '1st', color: '#1c437e', tooltip:'Tied for first, no hacks needed to make the plot.' },
];

let appeal = [
    { vis: 'Excel', value: '7th', color: '#008000', tooltip:'Some of the data points are cut off, looks the worst'},
    { vis: 'MATLAB', value: '6th', color: '#d0530f', tooltip:'The legends are not appealing in my opinion.' },
    { vis: 'R + ggplot2', value: '3rd', color: '#2569c0', tooltip:'Looks good, no problems with it. Just not as snazzy as Matplotlib and Vega-Lite' },
    { vis: 'Python + Matplotlib', value: '2nd', color: '#ffdd54', tooltip:'I think it looks sleek and the legends are nice.' },
    { vis: 'd3', value: '5th', color: '#000000', tooltip:'This one is on me, but it was hard to get d3 to look good,<br> the other tools have predefined graphs designed to look good.' },
    { vis: 'Vega-Lite', value: '1st', color: '#274c71', tooltip:'Something about the way Vega rendered the colors is just eye catching to me.' },
    { vis: 'Tableau', value: '4th', color: '#1c437e', tooltip:'Kind of looks white washed as if the saturation<br> was reduced or the brightness was increased.' },
];


// THE CHART
//Setting the dimensions and margins of the graph
let margin = { top: 10, right: 20, bottom: 50, left: 100 },
    width = 900 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom,
    graphWidth = 700;

// add the svg object
let svg = d3.select("#svgzone")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// Add x axis
let x = d3.scaleBand()
    .domain(['Excel', 'MATLAB', 'R + ggplot2', 'Python + Matplotlib', 'd3', 'Vega-Lite', 'Tableau'])
    .range([0, graphWidth]);
svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

// Add Y axis
let y = d3.scaleBand()
    .domain(['7th', '6th', '5th', '4th', '3rd', '2nd', '1st'])
    .range([height, 0]);
svg.append("g")
    .call(d3.axisLeft(y));

svg.append("text")
    .attr("x", -30)
    .attr("y", height / 2)
    .text("Rank")
    .attr("transform", "rotate(-90,-30," + (height / 2) + ")");

// Create the tooltip
let tooltip = d3.select("body").append("div").attr("class", "toolTip");

// Function to update the bars
function update(data) {
    let bars = svg.selectAll("rect")
        .data(data);
    bars.enter()
        .append("rect")
        .merge(bars)
        .on("mousemove", function (d,e) {
            tooltip
                .style("left", event.pageX - 100 + "px")
                .style("top", event.pageY - 100 + "px")
                .style("display", "inline-block")
                .html(e.tooltip);
        })
        .on("mouseout", function (d) { tooltip.style("display", "none"); })
        .transition()
        .duration(1000)
        .attr("x", function (d) { return x(d.vis) + 10 })
        .attr("y", function (d) { return y(d.value) + 25 })
        .attr("width", x.bandwidth() - 20)
        .attr("height", function (d) { return height - y(d.value) - 25 })
        .attr("fill", function (d) { return d.color });
}

// start with learnability
update(learnability);

// Update the bars based on the dropdown menu
optionList = document.getElementById("optionList");
graphTitle = document.getElementById("graphTitle");
description = document.getElementById("description");
optionList.addEventListener("change", function () {
    if (optionList.value === "learnability") {
        update(learnability);
        graphTitle.innerText = "Learnability";
        description.innerText = "This shows the ranking of the tools based on a combination of how easy they were to learn and the quality of their documentation. This is the most important metric in my opinion.";
    } else if (optionList.value === "fileSize") {
        update(fileSize)
        graphTitle.innerText = "Smallest File Size";
        description.innerText = "This shows the ranking of the tools based on the size of the file needed to produce the vis (install size of the program not counted). This is the least important metric in my opinion.";
    } else if (optionList.value === "customization") {
        update(customization)
        graphTitle.innerText = "Customization";
        description.innerText = "This shows the ranking of the tools based on how easy they are to customize beyond the default plot settings. Libraries performed better here because they let you code whatever you like.";
    } else if (optionList.value === "hackiness") {
        update(hackiness)
        graphTitle.innerText = "Least Hacky Code";
        description.innerText = "This shows the ranking of the tools based on how many hacky maneuvers were needed to produce the graph. This includes things such as adding dummy data points to produce legends."
    } else {
        update(appeal)
        graphTitle.innerText = "Visual Appeal";
        description.innerText = "This very subjective category ranks the tools based on how good I think the resulting graph looks. I did get a second opinion from my girlfriend as well so it's not 100% biased."
    }
});