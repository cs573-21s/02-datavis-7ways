//Setting the dimensions and margins of the graph
let margin = { top: 10, right: 20, bottom: 30, left: 100 },
    width = 800 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom,
    graphWidth = 500;

// add the svg object
let svg = d3.select("#svgzone")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// read the data 
d3.csv("./cars-sample-imputed.csv").then(function (data) {
    buildVis(data);
});

function buildVis(cars) {

    // Add x axis
    let x = d3.scaleLinear()
        .domain([1500, 5000])
        .range([0, graphWidth]);
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    svg.append("text")
        .attr("x", 228)
        .attr("y", height+25)
        .text("Weight");

    // Add Y axis
    let y = d3.scaleLinear()
        .domain([8, 45])
        .range([height, 0]);
    svg.append("g")
        .call(d3.axisLeft(y));

    svg.append("text")
        .attr("x", -20)
        .attr("y", height/2)
        .text("MPG")
        .attr("transform", "rotate(-90,-20,"+(height/2)+")");

    // Add a bubble size scale
    let z = d3.scaleLinear()
        .domain([1500, 5000])
        .range([5, 10]);

    // Add bubble color scale
    let d3c10 = d3.schemeCategory10;
    console.log(d3.schemeCategory10);
    let colors = d3.scaleOrdinal()
        .domain(["bmw", "ford", "honda", "mercedes", "toyota"])
        .range(d3c10);

    // Add bubbles
    svg.append("g")
        .selectAll("dot")
        .data(cars)
        .enter()
        .append("circle")
        .attr("cx", function (d) { return x(d.Weight) })
        .attr("cy", function (d) { return y(d.MPG) })
        .attr("r", function (d) { return z(d.Weight) })
        .style("fill", function (d) { return colors(d.Manufacturer) })
        .style("opacity", "0.5");


    // Add legend dots for the colors
    let keys = ["bmw","ford","honda","mercedes","toyota"]
    svg.selectAll("manufacturerDots")
        .data(keys)
        .enter()
        .append("circle")
        .attr("cx", 500)
        .attr("cy", function (d, i) { return 100 + i * 25 }) // 100 is where the first dot appears. 25 is the distance between dots
        .attr("r", 7)
        .style("fill", function (d) { return colors(d) });

    // Add legend labels for the colors
    svg.selectAll("manufacturerLabels")
        .data(keys)
        .enter()
        .append("text")
        .attr("x", 520)
        .attr("y", function (d, i) { return 100 + i * 25 }) // 100 is where the first dot appears. 25 is the distance between dots
        .style("fill", function (d) { return colors(d) })
        .text(function (d) { return d })
        .attr("text-anchor", "left")
        .style("alignment-baseline", "middle");

    // Add the legend bubbles for the size
    let weightKeys = [2000, 3000, 4000];
    svg.selectAll("bubbleWeights")
        .data(weightKeys)
        .enter()
        .append("circle")
        .attr("cx", 500)
        .attr("cy", function(d,i){return 250 + i *25})
        .attr("r", function(d,i){return 5 + i*3})
        .style("fill", "white")
        .attr("stroke","black");

    // Add the labels for the Legend
    svg.selectAll("bubbleWeightLabels")
        .data(weightKeys)
        .enter()
        .append("text")
        .attr("x", 520)
        .attr("y", function(d,i){return 250 + i * 25})
        .text(function(d){return d})
        .attr("text-anchor", "left")
        .style("alignment-baseline","middle");

}

